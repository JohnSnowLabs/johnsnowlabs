---
layout: docs
seotitle: NLP | John Snow Labs
title: Utilities for AWS EMR
permalink: /docs/en/jsl/aws-glue-utils
key: docs-install
modify_date: '2020-05-26'
header: true
show_nav: true
sidebar:
  nav: jsl
---

<div class="main-docs" markdown="1"><div class="h3-box" markdown="1">

## AWS Glue Setup

You can quickly setup John Snow Labs products in AWS Glue environment with few lines of code.

See [AWS Glue Setup Notebook](https://github.com/JohnSnowLabs/johnsnowlabs/tree/main/notebooks/setup_glue_notebook.ipynb)

```python
!pip install johnsnowlabs

from johnsnowlabs import nlp
nlp.install_to_glue()
```

`nlp.install_to_glue` has the following parameters:

</div><div class="h3-box" markdown="1">

### AWS specific parameters

| Parameter            | Description                                                                                                                                                                                                                                                     |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `boto_session`       | The Boto Session used to authorize requests to your AWS Account. If not provided, default session with environment variables is created. Refer [this](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html) for more information |
| `glue_assets_bucket` | S3 bucket to store johnsnowlabs python packages and jars. If not provided, one is created.                                                                                                                                                                      |

</div><div class="h3-box" markdown="1">

### License Retrieval Parameters

| Parameter           | Description                                                                                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `browser_login`     | Enable or disable browser based login and pop up if no license is provided or automatically detected. Defaults to True.                                             |
| `force_browser`     | If a cached license if found, no browser pop up occurs. Set True to force the browser pop up, so that you can download different license, if you have several ones. |
| `access_token`      | Use access token to fetch license from your account in https://my.johnsnowlabs.com account.                                                                         |
| `json_license_path` | Load license from your downloaded json license file                                                                                                                 |
| `license`           | License key as part of [Manual license installation](https://nlp.johnsnowlabs.com/docs/en/jsl/install_advanced#via-manually-defining-secrets)                       |
| `aws_access_key`    | JSL AWS Secret Key as part of [Manual license installation](https://nlp.johnsnowlabs.com/docs/en/jsl/install_advanced#via-manually-defining-secrets)                |
| `aws_key_id`        | JSL AWS Access Key as part of [Manual license installation](https://nlp.johnsnowlabs.com/docs/en/jsl/install_advanced#via-manually-defining-secrets)                |

Refer [this](https://nlp.johnsnowlabs.com/docs/en/jsl/install_advanced) for more information

</div></div>