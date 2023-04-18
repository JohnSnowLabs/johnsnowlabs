---
layout: docs
seotitle: Getting Started | John Snow Labs
title: Getting Started
permalink: /docs/en/deidentification_lab/getting_started
key: docs-install
modify_date: "2023-04-13"
header: true
show_nav: true
sidebar:
    nav: deidentification_lab
---

<div class="main-docs" markdown="1"><div class="h3-box" markdown="1">

## Overview

</div><a href="https://www.nist.gov/itl/applied-cybersecurity/privacy-engineering/collaboration-space/introduction">De-identification is a technique or process applied to a dataset with the goal of preventing or limiting certain types of privacy risks to individuals, protected groups, and establishments, while still allowing for the production of aggregate statistics.</a>
De-identification is essential for companies working with sensitive and highly regulated data, such as health records, financial transactions, or personal information. De-identification of data can help companies reduce their risk of leaking or accidentally disclosing personally identifiable information (PII) and personal health information (PHI). John Snow Labs' De-identification Lab has been built with the following salient features:

- The ability to de-identify sensitive data like personally identifiable information (PII) using various techniques such as redaction, masking, etc. 
- The ability to preserve the utility of the data for joining or analytics while reducing the risk of handling the data by obfuscating the raw sensitive identifiers. 
- The ability to comply with data privacy regulations such as HIPAA, GDPR, CCPA, etc. that require de-identification of data before sharing or processing. 
</div>


## Features

<div>
 De-identification Lab has been built keeping in mind usability, accessibility, simplicity and intuitiveness. It offers a smooth and pleasant user experience. The customer, thought a simple two-step process, using an intuitive User Interface, can choose which PII or PHI entities to de-identify, which de-identification methods to apply and where to store the de-iddentified files. 

In compliance with HIPAA, GDPR and other regulations, John Snow Labs De-identification Lab is able to de-identify a wide range identifiers so that health information cannot be used to identify individuals. The entire suite can run in customer's own IT environment or on cloud in the account of their own choice. John Snow Labs, at any point in time, neither accesses or store any customer data.
  
De-identification Lab supports a variety of document formats ranging from unstructured text (txt), PDF (text and image), DICOM files including the metadata and filenames.
</div>
<p></p>
<img class="image image__shadow image__align--left " src="/assets/images/deidentification_lab/deidentification_formats.jpg" style="width:25%;"/>
<img class="image image__shadow image__align--right" src="/assets/images/deidentification_lab/deidentification_run_cloud_onpremise.png" style="width:25%;"/>
## Accuracy

<div>To determine the accuracy of the underlying engine, tests were conducted using following data sets. 
<ul>
<li>2014 i2b2 de-identification challenge dataset</li>
<li>A sample of 100 notes from MIMIC-III dataset</li>
</ul>


On the first data set, the underlying models achieved a micro-F1 score of 0.955 and 0.978 on coarse 7 labels and granular 13 labels respectively. A comparison study with Commercial Cloud API's such as AWS Medical Comprehend, Microsoft Azure Text Analytics for Healthcare and Google Cloud Platform Healthcare APIs was also performed using the second dataset. Our underlying engine yielded an average F1score of 0.96 and performed better than the commercial APIs. 
</div>
<p></p>
<img class="image image__shadow image__align--center" src="/assets/images/deidentification_lab/2014_i2b2_Challenge.png" style="width:100%;"/>
<div></div>
<img class="image image__shadow image__align--center" src="/assets/images/deidentification_lab/comparison_with_cloud_apis.png" style="width:100%;"/>
