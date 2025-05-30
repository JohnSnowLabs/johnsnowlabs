---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: License Management
permalink: /docs/en/alab/byol
key: docs-training
modify_date: "2023-06-09"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

By default, the Generative AI Lab allows access to community pre-trained models and embeddings. Those are available on the **Models Hub** page. To gain access to licensed resources (e.g. pre-trained models and embeddings) _admin_ user can import a license (Healthcare, Finance, Legal, or Visual NLP) which will activate additional features:

- Access to licensed models for pre-annotation
- Access to healthcare, finance, and legal embeddings
- Access to rules
- Access to optimized annotators
- Access to training custom models using licensed embeddings

The _admin_ user can upload a Spark NLP license JSON file by visiting the License page. The license is generated by the John Snow Labs license server and is available on [my.johnsnowlabs.com](https://my.johnsnowlabs.com/).
Once a valid license is uploaded, all the licensed (Healthcare, Finance, Legal, and Visual NLP) models and embeddings become available for download. The License page shows the history of license uploads with detailed information like _License Info_, _Status_, _Renewal Date_, and _License Secrets_.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/add_license.png" style="width:100%;"/>

## Support for Universal Licenses

Licensing complexity is now significantly reduced through the addition of a universal license key that governs all John Snow Labs libraries and products. Before this update, customers faced the challenge of managing multiple licenses—a separate one for the application and others for using specific functionalities like the Visual or Healthcare features (e.g. in training or preannotation). This complexity often led to additional administrative burdens.

This enhancement simplifies deployments, and license tracking across enterprise environments. It also increases flexibility, boosts efficiency, and provides a seamless experience across all John Snow Labs products. The same license key can be moved to other products – Medical LLMs, Terminology Server, or can be used to experiment with the Healthcare or Visual libraries in Python, as long as it contains a sufficient number of credits.

![700image](/assets/images/annotation_lab/7.0.0/8.png)

## Support for Floating Licenses

Generative AI Lab supports floating licenses with different scopes (_ocr: training_, _ocr: inference_, _healthcare: inference_, _healthcare: training_, _finance: inference_, _finance: training_, _legal: inference_, _legal: training_). Depending on the scope of the available license, users can perform model training and/or deploy pre-annotation servers.
Licenses are a must for training Healthcare, Finance, and Legal models and deploying these models as pre-annotation servers.
Floating licenses can be acquired on self-service via [my.johnsnowlabs.com](https://my.johnsnowlabs.com/).

One floating license is bound to only one server (pre-annotation server, OCR server, training job) at a time. To run multiple model training jobs and/or pre-annotations servers, users must provide multiple floating licenses.

Generative AI Lab supports either floating licenses or air-gapped licenses. Mixing floating and air-gapped licenses on the same Generative AI Lab instance is not allowed.

### In-App Trial License Generation

Version 4.10 offers an updated License page layout that streamlines the process of obtaining a trial license. This updated design enables users to initiate a trial license request directly from the License page, thereby eliminating the need for external page navigation. This enhanced workflow incorporates a new “Get License” tab, while maintaining the status quo of the Import License and Existing Licenses tabs.

To obtain a trial license, users are required to fill out the form on the “Get License” tab, providing their organizational email. Once the form is submitted, a validation link is sent to the provided email address, and the trial license is automatically imported to the Generative AI Lab when the link is clicked, making it readily available for use.

![trial-license](/assets/images/annotation_lab/4.10.0/1.png)

### Usage of NLP Licenses

The number of available floating licenses can influence the creation of multiple training and pre-annotation servers. For example, to deploy 5 pre-annotation servers using Spark NLP for Healthcare models or embeddings, across 5 different projects, you will need 5 floating licenses.

Since one floating license can only be used for one server, it is not possible to deploy a pre-annotation server and then trigger training from the same project when only one license is available. In this case, the pre-annotation server has to be deleted first, and then the training can be started.

Those restrictions do not apply when using Spark NLP models and embeddings.

## Support for PAYG License
With the release of version 6.0.0, Generative AI Lab now offers support for the PAYG (Pay-As-You-Go) license option alongside the existing license options. The PAYG license introduces a flexible pay-per-usage billing model, reducing costs and providing the mechanism for paying only for the utilized resources.

**Key Features and Current Implementation of PAYG License:**
- **Opt-In Option for manually installed application:** For manually installed Generative AI Lab, users can choose the PAYG license when purchasing licenses from my.johnsnowlabs.com, download it, and import it to Generative AI Lab from the License page. Currently, importing PAYG License directly from the license page by logging into my.johnsnowlabs.com from within the application is not possible.
- **Flexible Billing:** With the PAYG license, users are billed based on only the resources they use, offering a more tailored and cost-effective pricing model.
- **Support for Multiple Servers:** PAYG license also comes with support for running multiple training and pre-annotation servers in parallel. PAYG license enables users to deploy and utilize multiple pre-annotation servers and training instances in parallel. This boosts workflow efficiency and productivity, allowing the execution of tasks simultaneously and accelerating project completion.

![MultipleServerDeploymentWithPayG](/assets/images/annotation_lab/6.0.0/3.png)


### PAYG License Included in AMI Installation

With the release of version 6.0.0, Generative AI Lab's AMI installation comes equipped with the PayG (Pay-As-You-Go) license. This license is autogenerated and readily available on the License page within the AMI environment, eliminating the need for users to manually add the license.

**Features of PAYG License in AMI:**
- **Automated License Generation and Simplified Management:** The PAYG license is autogenerated and readily available on the License page of the AMI installation. Users no longer need to worry about manually adding the license. Therefore, concerns regarding expiration or accidental deletion are eliminated. The license renewal process is smooth, the PayG license doesn't need to be renewed and a new license gets generated automatically once the existing one expires. 
- **Exclusive Support:** Generative AI Lab in AWS AMI exclusively supports the PAYG license. Users cannot upload any other types of licenses. The license page in AMI only shows the current PayG license and users cannot add or delete licenses from this page.
  
![LicensePageInAMI](/assets/images/annotation_lab/6.0.0/4.png)


This enhancement streamlines the licensing process for AMI users, ensuring continuous access to a valid license without any manual intervention or risk of license issues.

### Cost Awareness Banner for PAYG License
In this version, with the introduction of the PAYG license, proactive measures have been introduced to inform users about the potential costs associated with the new license. Users will now be presented with a noticeable message banner at the top of the page, stating: "Continuous Server Usage Incurs Costs! Please check the deployed server." The message is always shown even if no server is deployed on the cluster page. It helps users to be aware of the fact that they are billed based on application and resource usage.

![LicensePageInAMI](/assets/images/annotation_lab/6.0.0/5.gif)

By presenting this message, users are reminded to monitor their server usage and associated costs, promoting cost-conscious behavior. This feature enhances user awareness and ensures transparency regarding the cost implications of utilizing the PAYG license within Generative AI Lab.

It's important to note that there is no change in the existing functionality of Generative AI Lab. Users can continue to access and use all features and functionalities as before.

This introduction of the PAYG (Pay-As-You-Go) license option reflects our commitment to providing users with flexible licensing options that best suit their needs and usage patterns.

### Application License Requirement for On-Prem Deployments
With the latest version, Generative AI Lab now requires an application license for on-premises installations. This change brings on-prem licensing in line with our cloud deployments via AWS Marketplace AMI and Azure Marketplace, where usage has been metered.

On-prem users will now need to import an application license on the same License page where other library licenses are managed. This ensures a smooth experience while maintaining flexibility across different deployment environments.

Our commitment remains to provide a powerful and efficient annotation tool while supporting ongoing innovation and improvements. We appreciate your continued support and look forward to introducing more enhancements to Generative AI Lab.

![6110image](/assets/images/annotation_lab/6.11.0/5.png)


