
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: License Management
permalink: /docs/en/alab/byol
key: docs-training
modify_date: "2025-11-27"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab

## License Management

By default, the Generative AI Lab allows access to community pre-trained models and embeddings, available on the **Models Hub** page.  
To gain access to licensed resources (such as Healthcare, Finance, Legal, or Visual NLP models), an **admin user** can import a valid license file from the **License Management** page.

Once uploaded, the license activates additional capabilities, including:

- Access to licensed models for pre-annotation  
- Access to healthcare, finance, and legal embeddings  
- Access to rules and optimized annotators  
- Ability to train custom models using licensed embeddings  

Licenses are generated through the [John Snow Labs License Server](https://my.johnsnowlabs.com/) and downloaded as JSON files. After import, all corresponding licensed models and embeddings become available within the Lab.  
The License Management page lists all licenses with detailed information such as **License Info**, **Status**, **Renewal Date**, and **License Secrets**.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/add_license.png" style="width:100%;"/>

### License Page Controls and Administration

The License Management page provides options to **upload new licenses**, as well as **delete or replace an existing license** directly from the interface.  
Administrators can now rotate or switch licenses—such as changing between Healthcare and Visual NLP keys, or replacing expired licenses—without downtime.  
This functionality helps maintain compliance and simplifies license renewal workflows in enterprise environments.

## Support for Universal Licenses

Licensing complexity has been reduced through a **universal license key** that governs all John Snow Labs libraries and products.  
Previously, customers managed separate licenses for the application and for specialized modules such as Healthcare or Visual NLP.  
Now, a single universal key enables access across all compatible John Snow Labs tools, including **Medical LLMs**, **Terminology Server**, and others—provided the license contains sufficient credits.

This unified approach simplifies deployment, increases flexibility, and improves tracking across enterprise environments.

![700image](/assets/images/annotation_lab/7.0.0/8.png)

## Support for Floating Licenses

Generative AI Lab supports **floating licenses** with various scopes (e.g., _ocr: training_, _ocr: inference_, _healthcare: training_, _finance: inference_, etc.).  
These determine whether users can train models, run inference, or deploy pre-annotation servers.  
Floating licenses can be obtained through [my.johnsnowlabs.com](https://my.johnsnowlabs.com/) and are required for Healthcare, Finance, and Legal model training or deployment.

Each floating license is bound to a single server or job at a time (training or pre-annotation). Running multiple simultaneous servers requires multiple floating licenses.  
Floating and air-gapped licenses cannot be mixed within the same instance.

### In-App Trial License Generation

The License page includes an integrated **trial license request** form under the **Get License** tab.  
Users can request a temporary license directly from the application—no external navigation required.  
After submitting an organizational email, a validation link is sent; once confirmed, the trial license is automatically imported into Generative AI Lab.

![trial-license](/assets/images/annotation_lab/4.10.0/1.png)

### Using NLP Licenses

The number of floating licenses determines how many concurrent training or pre-annotation servers can run.  
For example, deploying five pre-annotation servers with Healthcare models across different projects requires five floating licenses.  
A single floating license cannot run both a training job and a pre-annotation server simultaneously.

These restrictions do not apply to community Spark NLP models and embeddings.

## Support for PAYG (Pay-As-You-Go) Licenses

Generative AI Lab supports a **Pay-As-You-Go (PAYG)** license option alongside traditional fixed licenses.  
PAYG introduces a usage-based billing model, allowing teams to pay only for what they use and scale resources more efficiently.

**Key Features:**
- **Manual Installations:** Users can choose the PAYG option when purchasing from [my.johnsnowlabs.com](https://my.johnsnowlabs.com/) and import it through the License page.  
- **Flexible Billing:** Costs are based on actual usage, ensuring efficiency and cost control.  
- **Multiple Server Support:** PAYG licenses allow parallel deployment of multiple training and pre-annotation servers.

![MultipleServerDeploymentWithPayG](/assets/images/annotation_lab/6.0.0/3.png)

### PAYG License Included with AMI Installation

For **AWS AMI installations**, a PAYG license is preconfigured and automatically generated.  
Users do not need to manually import or renew the license—it regenerates seamlessly when it expires.  
The License page in AMI environments displays the current PAYG license for reference but does not allow adding or deleting licenses.

![LicensePageInAMI](/assets/images/annotation_lab/6.0.0/4.png)

### Cost Awareness Banner for PAYG Licenses

To ensure transparency, users see a top-page banner reminding them that continuous server usage incurs costs:

> “Continuous Server Usage Incurs Costs! Please check the deployed server.”

This message is displayed even if no servers are active, promoting cost-conscious usage habits.

![LicensePageInAMI](/assets/images/annotation_lab/6.0.0/5.gif)

## Application License for On-Prem Deployments

For on-premise installations, Generative AI Lab now requires an **application license**—similar to cloud marketplace versions (AWS, Azure).  
This ensures consistent management across environments.  
Admins can import this license on the same License page used for other John Snow Labs library keys.

![6110image](/assets/images/annotation_lab/6.11.0/5.png)


In summary, the **License Management** page now provides a complete set of administrative controls for managing all John Snow Labs licenses — including uploading, replacing, and deleting active licenses — ensuring flexibility, compliance, and uninterrupted access to licensed NLP functionality.



