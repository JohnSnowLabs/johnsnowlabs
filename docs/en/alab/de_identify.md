---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: De-Identification
permalink: /docs/en/alab/de_identify
key: docs-training
modify_date: "2024-08-26"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">

   # De-Identification Pipeline Tools and Entity Level Annotation Instruction
From Generative Ai Lab Version 6.7.0 onwards, improvements to the De-identification feature have been made. With this update, users can choose on a per-entity basis which de-identification method they would like to use. In addition to the de-identification pipeline that is the default, there is now support for custom models, rules, and prompts for identifying sensitive data. 

</div><div class="h3-box" markdown="1">

## Support for De-identification Pipelines
Version 6.7.0 updates the existing de-identification feature, which has been significantly expanded to give more control over how de-identification is applied, how different entities are treated, and how to integrate pre-trained de-identification pipelines, models, rules, and zero-shot prompts to help identify and anonymize sensitive data. 

De-identification has now moved from the Project Details page to the Content Type page during Project Configuration, where it is a separate project type.

</div><div class="h3-box" markdown="1">

### Creating a De-identification Project:
Users can use the de-identification feature if a valid license is available in the application: 
1. **Create a New Project**:
   During the project configuration, select **De-identification** as the project type.
2. **Automatic Pipeline Download**:
   A default de-identification pipeline (`clinical_deidentification`) will automatically download if not previously available or it will use the default de-identification project template. All the downloaded pipelines are available on the **Pipeline** page.
   
![670image](/assets/images/annotation_lab/6.7.0/1.png)

</div><div class="h3-box" markdown="1">

### New Pipeline Tab and Customization:
In the **Reuse Resource** page, a new **Pipelines Tab** is now available for de-identification projects. Here, all the downloaded de-identification pipelines are listed. Users can also use and apply pre-trained and trained models, rules, and zero-shot prompts.

![670image](/assets/images/annotation_lab/6.7.0/2.png)

In the **Customize Labels** page, users can configure the type of de-identification. Apart from all the deidentification types that are already supported, in version 6.7.0, users can even configure **different de-identification types for different labels** as well.

![670image](/assets/images/annotation_lab/6.7.0/3.png)

Additionally, users can upload custom obfuscation files in JSON format on the Customize Labels page.

![670image](/assets/images/annotation_lab/6.7.0/4.gif)

</div><div class="h3-box" markdown="1">

### De-identification Process:
The de-identification process remains similar to the existing pre-annotation workflow:

1. **Import Tasks**:
   Initially, tasks are imported, and the `NonDeidentified` tag is automatically added to the tasks. It helps users to know which tasks have been deidentified and which are yet to be de-identified.

   ![670image](/assets/images/annotation_lab/6.7.0/5.gif)

3. **Pre-annotate/De-identify**:
   Click the **De-identification (pre-annotate)** button to deploy the de-identification pipeline and pre-annotate and de-identify tasks. Once the task is pre-annotated and de-identified, the de-identification status changes to either green, red, or grey, just like pre-annotation status. 

   This is the biggest change to the de-identification workflow.

   ![670image](/assets/images/annotation_lab/6.7.0/6.gif)

5. **Labeling Page**:
   On the labeling page, users can either make corrections or accept the predictions made by the pipeline.

   ![670image](/assets/images/annotation_lab/6.7.0/7.gif)

7. **Re-run De-identification**:
   After saving or submitting the tasks, users can click the de-identify button again to run the process on either manually annotated completions or all completions and can view the de-identification in real-time from the labeling page. Users can click the **De-identification View** button (located next to the Compare Completion button), to view the de-identified tasks in real-time. All de-identified completions will show **(De-identified)** next to the completion ID.

   ![670image](/assets/images/annotation_lab/6.7.0/8.gif)

</div><div class="h3-box" markdown="1">

### Exporting De-identified Tasks:
Only de-identified completions submitted as **ground truth** are exported. Also, if a task has multiple ground truths from different users, the completion from the user with the **highest priority** will be exported.

![670image](/assets/images/annotation_lab/6.7.0/9.gif)

These updates are built on top of the current structure, ensuring ease of use and a smooth transition without disrupting productivity. 

</div><div class="h3-box" markdown="1">

## Introducing Support for De-Identification in Generative AI Lab 6.4
We are happy to announce the release of Generative AI Lab 6.4, bringing exciting new features and enhancements. Leading this release is the support for de-identification projects, which enables users to anonymize documents containing sensitive data, such as PII (Personally Identifiable Information) and PHI (Protected Health Information). This ensures robust data privacy and compliance with privacy regulations while maintaining the utility of the data for further analysis and processing. 

Additionally, version 6.4 enhances collaboration and quality control in the annotation process by allowing annotators to view completions submitted by reviewers. Annotators can now view and clone reviewed submissions, make corrections, or add comments directly on the annotated chunks, providing clear communication and improving overall annotation quality. The new release also simplifies the identification of differences between two completions by automatically highlighting discrepancies, streamlining the validation process. 

Alongside these major updates, this release includes numerous improvements and bug fixes, making Generative AI Lab more efficient and user-friendly than ever.

</div><div class="h3-box" markdown="1">

### Exporting De-identified Tasks:
Only de-identified completions submitted as **ground truth** are exported. Also, if a task has multiple ground truths from different users, the completion from the user with the **highest priority** will be exported.

![670image](/assets/images/annotation_lab/6.7.0/9.gif)

These updates are built on top of the current structure, ensuring ease of use and a smooth transition without disrupting productivity. 

</div>