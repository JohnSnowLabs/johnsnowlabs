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

## Accuracy

<div>To determine the accuracy of the underlying engine, tests were conducted using following data sets. 
<ul>
<li>2014 i2b2 de-identification challenge dataset</li>
<li>A sample of 100 notes from MIMIC-III dataset</li>
</ul>


On the first data set, the underlying models achieved a micro-F1 score of 0.955 and 0.978 on coarse 7 labels and granular 13 labels respectively. 
<br><br>
<img class="image image__shadow image__align--center" src="/assets/images/deidentification_lab/2014_i2b2_Challenge.png" style="width:100%;"/>
<br>
In the second experiment, a comparison study with Commercial Cloud API's such as AWS Medical Comprehend, Microsoft Azure Text Analytics for Healthcare and Google Cloud Platform Healthcare APIs was a  lso performed using a sample of 100 notes from MIMIC-III dataset. The JSL library that powers De-identification Lab yielded an average F1 score of 0.96 and performed better than the commercial APIs. 
<br><br>
<img class="image image__shadow image__align--center" src="/assets/images/deidentification_lab/comparison_with_cloud_apis.png" style="width:100%;"/>
</div>
<p></p>
