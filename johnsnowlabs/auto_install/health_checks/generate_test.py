import inspect

import johnsnowlabs.auto_install.health_checks.endpoint_test as endp_test
import johnsnowlabs.auto_install.health_checks.load_predict_test as load_predict_test


def generate_endpoint_test(model, lic):
    # read source of endpoint_test.py and replace placeholders with actual values and return new source code
    return (
        inspect.getsource(endp_test)
        .replace("ENDPOINT LICENSE", lic)
        .replace("MODEL TO TEST", model)
    )


def generate_load_predict_test(model):
    # read source of endpoint_test.py and replace placeholders with actual values and return new source code
    return inspect.getsource(load_predict_test).replace("<MODEL>", model)
