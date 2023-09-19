---
layout: docs
seotitle: NLP | John Snow Labs
title: Utilities for AWS EMR
permalink: /docs/en/jsl/aws-emr-utils
key: docs-install
modify_date: '2020-05-26'
header: true
show_nav: true
sidebar:
  nav: jsl
---

<div class="main-docs" markdown="1">

## AWS EMR Cluster Creation

You can create an AWS EMR Cluster with few lines of code. This ensures that John Snow Labs products are properly installed and ready for usage in an AWS EMR environment.

See [AWS EMR Cluster Creation Notebook](https://github.com/JohnSnowLabs/johnsnowlabs/tree/main/notebooks/create_emr_cluster.ipynb)

```python
!pip install johnsnowlabs

from johnsnowlabs import nlp
nlp.install_to_emr()
```

`nlp.install_to_emr` has the following parameters:

### AWS specific parameters

| Parameter              | Description                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `boto_session`         | The Boto Session used to authorize requests to your AWS Account. If not provided, default session with environment variables is created. Refer [this](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html) for more information                                                                                                            |
| `bootstrap_bucket`     | S3 bucket to store your EMR bootstrap scripts. If not provided, one is created.                                                                                                                                                                                                                                                                                            |
| `s3_logs_path`         | S3 path to store logs.                                                                                                                                                                                                                                                                                                                                                     |
| `service_role`         | Service role for your AWS EMR cluster. Default: `EMR_DefaultRole`. In order to use the default role, you must have already created it using the AWS CLI or console. <br />To create them, use `aws emr create-default-roles`. Refer [this](https://docs.aws.amazon.com/cli/latest/reference/emr/create-default-roles.html) for more information                            |
| `job_flow_role`        | The EC2 instance profile for each instances in EMR Cluster. Default: `EMR_EC2_DefaultRole`. In order to use the default role, you must have already created it using the AWS CLI or console. <br />To create them, use `aws emr create-default-roles`. Refer [this](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-role-for-ec2.html) for more information |
| `subnet_id`            | The subnet to launch the EMR cluster in. Refer [this](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-vpc-subnet.html) for more information                                                                                                                                                                                                                |
| `ec2_key_name`         | The key pair name to ssh into your EMR cluster                                                                                                                                                                                                                                                                                                                             |
| `auto_terminate_hours` | The idle hours to wait before the cluster teminated. Default: 1 hour                                                                                                                                                                                                                                                                                                       |

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

</div>
