import base64
import hashlib
import json
import os
import random
import string
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Dict, List
# imports related to get access token with PKCE Oauth
from urllib import parse
from urllib.request import Request, urlopen

from johnsnowlabs.utils.enums import ProductName

LICENSE_SERVER_ORIGIN = os.environ.get("LICENSE_SERVER_ORIGIN", "https://license.johnsnowlabs.com")

MYJSL_ORIGIN = os.environ.get("MYJSL_ORIGIN", "https://my.johnsnowlabs.com")

# save_path that license should be downloaded there
LICENSE_PATH = "downloaded-license.json"


# using urllib to avoid additional package dependencies like requests


class LibSecretResponse:
    product: ProductName
    version: str
    secret: str
    isLatest: bool

    def __init__(
        self,
        product: str,
        version: str,
        secret: str,
        isLatest: bool,
    ):
        self.product = ProductName.from_jsl_api(product)
        self.version = version
        self.secret = secret
        self.isLatest = isLatest
        self.version_secret = secret.split("-")[0]


class LicenseResponse:
    products: List[ProductName]
    id: str
    type: str
    endDate: bool
    platform: bool

    def __init__(
        self,
        products: List[Dict[str, str]],
        id: str,
        type: str,
        endDate: str,
        platform: str,
    ):
        self.products = [ProductName.from_jsl_api(p["name"]) for p in products]
        self.id = id
        self.type = type
        self.endDate = endDate
        self.platform = platform


# def pick_compatible_secrets()


def is_in_colab_notebook():
    try:
        from IPython import get_ipython

        return "google.colab" in str(get_ipython())
    except:
        return False


def http_request(url, data=None, method="POST", is_json=True, access_token=None):
    if data:
        if is_json:
            data = json.dumps(data).encode("utf-8")
        else:
            data = parse.urlencode(data).encode("utf-8")
    request = Request(url, data=data, method=method)
    if access_token:
        request.add_header("Authorization", f"Bearer {access_token}")
    if is_json:
        request.add_header("Content-Type", "application/json")
    else:
        request.add_header("Content-type", "application/x-www-form-urlencoded")
    response = urlopen(request)
    status_code = response.getcode()
    return (
        json.loads(response.read().decode("utf-8"))
        if 200 <= status_code < 300
        else None
    )


def get_access_token(email, password):
    """get access token (expires in 12h)"""
    data = http_request(
        MYJSL_ORIGIN + "/graphql",
        data={
            "query": """mutation($input: LoginInput!) {
                getAccessToken(input: $input) {
                    ok {token}
                    error {
                        errors {
                          key
                          message
                        }
                    }
                }
            }""",
            "variables": {"input": {"email": email, "password": password}},
        },
    )
    if data["data"]["getAccessToken"]["error"]:
        errors = "\n".join(
            [
                error["message"]
                for error in data["data"]["getAccessToken"]["error"]["errors"]
            ]
        )
        print(f"Cannot login. error={errors}")
        exit(1)
    access_token = data["data"]["getAccessToken"]["ok"]["token"]
    return access_token

def get_secrets(license):
    try:
        data = http_request(url=f"{LICENSE_SERVER_ORIGIN}/johnsnowlabs/releases/", method="GET", access_token=license)
        if data:
            return [LibSecretResponse(
                isLatest=r.get("is_latest"),
                product=r.get("product"),
                secret=r.get("secret"),
                version=r.get("version"),
            ) for r in data]
    except Exception:
        raise ValueError("Usage of invalid/expired license.")

def get_user_lib_secrets(access_token):
    secrets_query = """query ReleasesQuery {
	releases {
		product
		version
		secret
		isLatest
	}
}"""
    data = http_request(
        f"{MYJSL_ORIGIN}/graphql", {"query": secrets_query}, access_token=access_token
    )
    if data:
        if "errors" in data:
            raise Exception("Invalid or Expired token.")
        return [LibSecretResponse(**r) for r in data["data"]["releases"]]
    else:
        raise Exception("Something went wrong...")


def get_user_licenses(access_token):
    licenses_query = """query LicensesQuery {
  licenses(isValid: true, platforms: ["Airgap", "Floating", "PAYG"]) {
    edges {
      node {
        id
        type
        endDate
        platform {
          name
          type
        }
        products {
          name
        }
      }
    }
  }
}
 """

    data = http_request(
        f"{MYJSL_ORIGIN}/graphql", {"query": licenses_query}, access_token=access_token
    )
    if data:
        if "errors" in data:
            raise Exception("Invalid or Expired token.")
        return [LicenseResponse(**s["node"]) for s in data["data"]["licenses"]["edges"]]

    else:
        raise Exception("Something went wrong...")


def download_license(license: LicenseResponse, access_token):
    print("Downloading license...")
    data = http_request(
        "{}/attachments/{}".format(MYJSL_ORIGIN, license.id),
        method="GET",
        access_token=access_token,
    )
    if data:
        print("Licenses extracted successfully")
        return data
    else:
        raise Exception(f"Failed fetching license.")


def ensure_correct_choice(licenses_count):
    license_id = input()
    if license_id.isnumeric():
        index = int(license_id) - 1
        if licenses_count > index:
            return index
        else:
            print(f"Please select value between 1 and {licenses_count}")
            return ensure_correct_choice(licenses_count)
    else:
        print(f"Please select value between 1 and {licenses_count}")
        return ensure_correct_choice(licenses_count)


def get_user_license_choice(licenses):
    print("Please select the license to use.")
    for idx, license in enumerate(licenses):
        products = ",".join(s["file_name"] for s in license["products"])
        if license["platform"] is None:
            scope = "Airgap"
        else:
            scope = license["platform"]["file_name"]
            type = license["platform"]["type"]
            if scope == "Floating":
                if type:
                    scope = scope + "," + type.capitalize()

        print(
            "{}. Libraries: {}\n   License Type: {}\n   Expiration Date: {}\n   Scope: {}".format(
                idx + 1, products, license["type"], license["endDate"], scope
            )
        )

    choice = ensure_correct_choice(len(licenses))
    return licenses[choice]


def open_authorized_url(url, in_colab=False):
    if in_colab:
        from IPython.display import Javascript, display

        display(
            Javascript(
                """
        var a = document.createElement("a");
        a.id="auth-btn"
        a.setAttribute("target", "_blank");
        a.href="{{URL}}";
        a.style="padding:15px 20px;background-color:#0298d9;border-radius:7px;color:white;text-decoration:none;"
        a.innerText="Click here to Authorize on My.Johnsnowlabs.com"
        document.body.appendChild(a);
        document.body.style = "text-align:center;padding-top:15px;"
        a.click()
      """.replace(
                    "{{URL}}", url
                )
            )
        )
    else:
        print("Please confirm authorization on :", url)
        webbrowser.open_new_tab(url)


def get_access_key_from_browser():
    in_colab = is_in_colab_notebook()
    client_id = "2hfGX0iZ5lvyxvLaK3IEzS9Bc9LGfTYCwVvKFfjY"

    class OauthRequestHandler(BaseHTTPRequestHandler):
        code = None

        def response(self, msg, code):
            self.send_response(code)
            self.end_headers()
            self.wfile.write(
                f"<html><head><title>Johnsnowlabs</title><head><body>"
                f"<div style='text-align:center;margin-top:100px;'>"
                f"<span style='color:{'#0298d9' if code == 200 else '#c0392b'};font-size:24px'>{msg}</span>"
                f"</body></html>".encode("utf-8")
            )

        def do_GET(self):
            global access_token
            url_parts = parse.urlsplit(self.path)
            if url_parts.path == "/login":
                params = dict(parse.parse_qsl(url_parts.query))
                OauthRequestHandler.code = params.get("code")
                if OauthRequestHandler.code:
                    self.response("Authorization successful!", 200)
                else:
                    self.response("Authorization failed! please try again.", 400)

    verifier = "".join(
        [random.choice(string.ascii_letters + string.digits) for _ in range(64)]
    )
    hashed = hashlib.sha256(verifier.encode("utf-8")).digest()
    challenge = base64.urlsafe_b64encode(hashed)[:-1].decode("utf-8")
    if in_colab:
        port = 8000
        from google.colab.output import eval_js

        redirect_uri = eval_js("google.colab.kernel.proxyPort(8000)") + "login"
    else:
        port = 0

    with HTTPServer(("", port), OauthRequestHandler) as httpd:
        if port == 0:
            port = httpd.server_port
            redirect_uri = f"http://localhost:{port}/login"
        url = "{}/oauth/authorize/?{}".format(
            MYJSL_ORIGIN,
            parse.urlencode(
                {
                    "client_id": client_id,
                    "response_type": "code",
                    "code_challenge_method": "S256",
                    "code_challenge": challenge,
                    "redirect_uri": redirect_uri,
                }
            ),
        )
        open_authorized_url(url, in_colab)
        httpd.handle_request()
        if in_colab:
            from IPython.display import Javascript, display

            display(Javascript("document.body.removeChild(a);"))

    if OauthRequestHandler.code:
        data = http_request(
            f"{MYJSL_ORIGIN}/oauth/token/",
            data={
                "grant_type": "authorization_code",
                "client_id": client_id,
                "code_verifier": verifier,
                "code": OauthRequestHandler.code,
                "redirect_uri": redirect_uri,
            },
            is_json=False,
        )
        return data["access_token"]
    return None
