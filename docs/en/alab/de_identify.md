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

## Introducing Support for De-Identification in Generative AI Lab 6.4
We are happy to announce the release of Generative AI Lab 6.4, bringing exciting new features and enhancements. Leading this release is the support for de-identification projects, which enables users to anonymize documents containing sensitive data, such as PII (Personally Identifiable Information) and PHI (Protected Health Information). This ensures robust data privacy and compliance with privacy regulations while maintaining the utility of the data for further analysis and processing. 

Additionally, version 6.4 enhances collaboration and quality control in the annotation process by allowing annotators to view completions submitted by reviewers. Annotators can now view and clone reviewed submissions, make corrections, or add comments directly on the annotated chunks, providing clear communication and improving overall annotation quality. The new release also simplifies the identification of differences between two completions by automatically highlighting discrepancies, streamlining the validation process. 

Alongside these major updates, this release includes numerous improvements and bug fixes, making Generative AI Lab more efficient and user-friendly than ever.

</div><div class="h3-box" markdown="1">

## Support for De-identification
Version 6.4 of the Generative AI Lab introduces a new de-identification feature, enabling users to anonymize documents containing sensitive information such as PII (Personally Identifiable Information) and PHI (Protected Health Information). This functionality is intended to protect data privacy and ensure compliance with privacy regulations while preserving the data’s usefulness for subsequent analysis and processing.

**De-identification Projects:** When creating a new project in the Generative AI Lab, users can mark it as De-Identification specific. These projects allow the use of manually trained or pre-trained text-based NER models, together with prompts, rules, and custom labels created by the user for identifying sensitive data inside of tasks. Once the sensitive data is identified (either automatically or manually) and validated by human users, it can be exported for further processing. 
When creating De-identification projects make sure you only target sensitive entities as part of your project configuration and avoid annotating relevant data you need for downstream processing as all those entities will be removed when exporting the project tasks as de-identified documents. The best practice, in this case, is to re-use de-identification specific models combined with custom prompts/rules. 

**Exporting De-identified Documents:** The tasks of your project with PII/PHI labeled entities can be exported as de-identified documents. During the export process, labeled entities will be replaced by the label names, or special characters (such as "*"), or obfuscated and replaced with fake data. This ensures that sensitive information is removed and not available for downstream analysis.

**Re-importing and Further Processing:** The de-identified documents can be re-imported into any text-based project. This allows for further labeling and data preparation for model training/tuning by annotators, ensuring that the de-identified data can be utilized effectively.

</div><div class="h3-box" markdown="1">

### Types of De-identification
Generative AI Lab supports four kinds of de-identification:
1.	**Mask with Entity Labels:** Identified tokens are replaced with their respective label names. For instance, in the text " John Davies is a 62 y.o. patient admitted to ICU after an MVA." where John Davies is labeled as Patient and 62 as Age, the de-identified exported text would be: "\<Patient\> is a \<Age\> y.o. patient admitted to ICU after an MVA. "
2.	**Mask with Characters:** All characters of the identified tokens are replaced by *. For the above example, if John Davies was labeled as Patient and 62 was labeled as Age, then on task export, the resulting text will look like "``****`` ``******`` is a ``**`` y.o. patient admitted to ICU after an MVA." This option ensures the number of characters is kept the same between the original document and the anonymized one.
3.	**Mask with Fixed Length Characters:** The identified tokens are replaced by ``****`` (4 star characters). For the same example, the output will be "``****`` ``****`` is a ``****`` y.o. patient admitted to ICU after an MVA."
4.	**Obfuscation:** The identified tokens are replaced by new (fake) tokens. For the above example, the obfuscated result will be "Mark Doe is a 48 y.o. patient admitted to ICU after an MVA. "

</div><div class="h3-box" markdown="1">

### Working with de-identification projects

**Step 1.** When creating a new project, after defining the project name and general settings, check the de-identification option at the bottom of the Project setup page, and select the type of anonymization you prefer.

![GenaiImage](/assets/images/annotation_lab/6.4.0/1.png)

**Step 2.** Configure your project to reuse sensitive labels from existing NER Models, Rules, Prompts. It is also possible to create custom labels that can be used to manually annotate the entities you want to anonymize in your documents.

When selecting pre-annotation resources for your project, ensure that no critical downstream data is inadvertently identified and removed. For instance, if you pre-annotate documents with models, rules, or prompts that identify diseases, those labels will be anonymized upon export, rendering them unavailable to document consumers.

To mitigate this, employ pre-trained or custom de-identification models and augment them with rules and prompts tailored to your specific use cases (e.g., unique identifiers present in your documents). You can also selectively include specific labels from each model in your project configuration. For example, if age information is essential for your consumers, you can exclude this label from the project configuration to retain the data in your document.

![GenaiImage](/assets/images/annotation_lab/6.4.0/2.png)

**Step 3.** Pre-annotate your documents, then have your team review them for any overlooked sensitive data. Once your project is set up and tasks are imported, use the pre-annotation feature to automatically identify sensitive information.
Incorporate a review process where your team checks the pre-annotations using the standard annotation workflow, making manual corrections or annotations to any sensitive segments as necessary. Ensure that all sensitive information is accurately labeled for effective de-identification.

![GenaiImage](/assets/images/annotation_lab/6.4.0/3.png)

**Step 4.** Export De-identified Documents. After completing the labeling process, proceed to export the de-identified documents. Ensure the "Export with De-identification" option is selected on the export page to generate de-identified documents.

During the export process, de-identification is executed based on the type of anonymization selected during project setup. This de-identification option can be updated at any time if necessary.

![GenaiImage](/assets/images/annotation_lab/6.4.0/4.png)

**Step 5.** Import the de-identified tasks in a new project for further processing. These tasks, once exported, can be re-imported into any text-based project in case you need to extract additional data or in case you want to use them for model training/tuning.

![GenaiImage](/assets/images/annotation_lab/6.4.0/5.png)

> **_HOW TO:_** De-identification projects can be easily identified without opening them. A small de-identification icon is displayed in the bottom left corner of the project card, clearly indicating the project's status.


> **_LIMITATION:_** Projects must be designated as de-identification projects during their initial creation. It is not possible to convert existing projects or newly created non-de-identification projects into de-identification projects.

</div><div class="h3-box" markdown="1">

### Export of De-identified tasks
**Completion Submission:** Pre-annotations alone are not sufficient for exporting de-identified data. Only starred completions are considered during the export of de-identified tasks. This means that each task intended for de-identified export must be validated by a human user, with at least one completion marked with a star by an annotator, reviewer, or manager.

**Multiple Submissions:** In instances where multiple submissions exist from various annotators, the de-identification process will prioritize the starred completion from the highest priority user as specified on the Teams page. This ensures that de-identification is based on the most relevant and prioritized annotations.

This new de-identification feature significantly enhances data privacy by anonymizing sensitive document information. We are confident that this feature will empower users to handle sensitive data responsibly while maintaining the integrity and usability of their datasets.

## Support for De-identification Pipelines
Version 6.7.0 updates the existing de-identification feature, which has been significantly expanded to give more control over how de-identification is applied, how different entities are treated, and how to integrate pre-trained de-identification pipelines, models, rules, and zero-shot prompts to help identify and anonymize sensitive data. 

De-identification has now moved from the Project Details page to the Content Type page during Project Configuration, where it is a separate project type.

### Creating a De-identification Project:
Users can use the de-identification feature if a valid license is available in the application: 
1. **Create a New Project**:
   During the project configuration, select **De-identification** as the project type.
2. **Automatic Pipeline Download**:
   A default de-identification pipeline (`clinical_deidentification`) will automatically download if not previously available or it will use the default de-identification project template. All the downloaded pipelines are available on the **Pipeline** page.
   
![670image](/assets/images/annotation_lab/6.7.0/1.png)

### New Pipeline Tab and Customization:
In the **Reuse Resource** page, a new **Pipelines Tab** is now available for de-identification projects. Here, all the downloaded de-identification pipelines are listed. Users can also use and apply pre-trained and trained models, rules, and zero-shot prompts.

![670image](/assets/images/annotation_lab/6.7.0/2.png)

In the **Customize Labels** page, users can configure the type of de-identification. Apart from all the deidentification types that are already supported, in version 6.7.0, users can even configure **different de-identification types for different labels** as well.

![670image](/assets/images/annotation_lab/6.7.0/3.png)

Additionally, users can upload custom obfuscation files in JSON format on the Customize Labels page.

![670image](/assets/images/annotation_lab/6.7.0/4.gif)

### De-identification Process:
The de-identification process remains similar to the existing pre-annotation workflow:

1. **Import Tasks**:
   Initially, tasks are imported, and the `NonDeidentified` tag is automatically added to the tasks. It helps users to know which tasks have been deidentified and which are yet to be de-identified.

   ![670image](/assets/images/annotation_lab/6.7.0/5.gif)

3. **Pre-annotate/De-identify**:
   Click the **De-identification (pre-annotate)** button to deploy the de-identification pipeline and pre-annotate and de-identify tasks. Once the task is pre-annotated and de-identified, the de-identification status changes to either green, red, or grey, just like pre-annotation status. 

   ![670image](/assets/images/annotation_lab/6.7.0/6.gif)

5. **Labeling Page**:
   On the labeling page, users can either make corrections or accept the predictions made by the pipeline.

   ![670image](/assets/images/annotation_lab/6.7.0/7.gif)

7. **Re-run De-identification**:
   After saving or submitting the tasks, users can click the de-identify button again to run the process on either manually annotated completions or all completions and can view the de-identification in real-time from the labeling page. Users can click the **De-identification View** button (located next to the Compare Completion button), to view the de-identified tasks in real-time. All de-identified completions will show **(De-identified)** next to the completion ID.

   ![670image](/assets/images/annotation_lab/6.7.0/8.gif)

### Exporting De-identified Tasks:
Only de-identified completions submitted as **ground truth** are exported. Also, if a task has multiple ground truths from different users, the completion from the user with the **highest priority** will be exported.

![670image](/assets/images/annotation_lab/6.7.0/9.gif)

These updates are built on top of the current structure, ensuring ease of use and a smooth transition without disrupting productivity. 

</div>