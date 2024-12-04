---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: De-Identification
permalink: /docs/en/alab/de_identify
key: docs-training
modify_date: "2024-12-03"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">

## Support for De-identification
Version 6.4 of Generative AI Lab introduces a new de-identification feature, enabling users to anonymize documents containing sensitive information such as PII (Personally Identifiable Information) and PHI (Protected Health Information). This functionality is intended to protect data privacy and ensure compliance with privacy regulations while preserving the data’s usefulness for subsequent analysis and processing.

Version 6.7 of Generative AI Lab improves on the original feature to allow for custom methods of de-identification for each entity label and support for the newest John Snow Labs De-identification Pipeline. 

**De-identification Projects** When creating a new project in the Generative AI Lab, users can mark it as De-Identification specific. These projects allow the use of manually trained or pre-trained text-based NER models, together with prompts, rules, and custom labels created by the user for identifying sensitive data inside of tasks. Once the sensitive data is identified (either automatically or manually) and validated by human users, it can be exported for further processing. 
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

To create a De-identification project, in the first step ot he Project Configuration wizzard, select the `De-identification` template available under the `TEXT` tab. 

</div><div class="h3-box" markdown="1">

### Creating a De-identification Project
Users can use the de-identification feature if a valid license is available in the application: 
1. **Create a New Project**:
   During the project configuration, select **De-identification** as the project type.
2. **Automatic Pipeline Download**:
   A default de-identification pipeline (`clinical_deidentification`) will automatically download if not previously available or it will use the default de-identification project template. All the downloaded pipelines are available on the **Pipeline** page.
   
![670image](/assets/images/annotation_lab/6.7.0/1.png)

</div><div class="h3-box" markdown="1">

### New Pipeline Tab and Customization
In the **Reuse Resource** page, a new **Pipelines Tab** is now available for de-identification projects. Here, all the downloaded de-identification pipelines are listed. Users can also use and apply pre-trained and trained models, rules, and zero-shot prompts.


![670image](/assets/images/annotation_lab/6.7.0/2.png)


In the **Customize Labels** page, users can first select the overall de-identification strategies to use. Furthermore, it is also possible to specify parand use entity level configurations.

![670image](/assets/images/annotation_lab/6.7.0/3.png)

Users can also upload custom obfuscation configurations in JSON format via the Customize Labels page, enabling the seamless reuse of obfuscation rules across multiple projects.

![670image](/assets/images/annotation_lab/6.7.0/4.gif)

</div><div class="h3-box" markdown="1">

### De-identification Process

The de-identification process is similar to the existing pre-annotation workflow:

1. **Import Tasks**


   Initially, tasks are imported, and the `NonDeidentified` tag is automatically added to the tasks. It helps users know which tasks have been deidentified and which are yet to be de-identified.

   ![670image](/assets/images/annotation_lab/6.7.0/5.gif)

2. **Pre-annotate/De-identify**


   Click the **De-identification (pre-annotate)** button to deploy the de-identification pipeline and pre-annotate your tasks. During the pre-annotation stage, there is a status indicator (the colored circle) next to each task that changes to either green, red, or grey, just like the pre-annotation status. 

   ![670image](/assets/images/annotation_lab/6.7.0/6.gif)

3. **Labeling Page**


   On the labeling page, users can either make corrections or accept the predictions made by the pipeline.

   ![670image](/assets/images/annotation_lab/6.7.0/7.gif)

4. **Re-run De-identification**


   After saving and submitting the tasks, users can click the de-identify button again to run the de-identification process. This will change the content of your tasks by applying the specified de-identification configurations on all automatic and manual annotations. You can then view the de-identification results on the labeling page. Users can click the **De-identification View** button (located next to the Compare Completion button), to view the de-identified tasks in comparison with the original version. All de-identified completions will show **(De-identified)** next to the completion ID.

   ![670image](/assets/images/annotation_lab/6.7.0/8.gif)

</div>

### Exporting De-identified Tasks


Only de-identified completions submitted as **ground truth** are exported. Also, if a task has multiple ground truths from different users, the completion from the user with the **highest priority** will be exported.

![670image](/assets/images/annotation_lab/6.7.0/9.gif)

These updates are built on top of the current structure, ensuring ease of use and a smooth transition without disrupting productivity. 

> **_HOW TO:_** De-identification projects can be easily identified without opening them. A small de-identification icon is displayed in the bottom left corner of the project card, clearly indicating the project's status.


> **_LIMITATION:_** Projects must be designated as de-identification projects during their initial creation. It is not possible to convert existing projects or newly created non-de-identification projects into de-identification projects.


### Export of De-identified tasks


**Submitted Completions:** Pre-annotations alone are not sufficient for exporting de-identified data. Only starred completions are considered during the export of de-identified tasks. This means that each task intended for de-identified export must be validated by a human user, with at least one completion marked with a star by an annotator, reviewer, or manager.

**Multiple Completions:** In cases where multiple submissions exist from various annotators, the de-identification process will prioritize the starred completion from the highest priority user as specified on the Teams page. This ensures that de-identification is based on the most relevant and prioritized annotations.

This new de-identification feature significantly enhances data privacy by anonymizing sensitive document information. We are confident that this feature will empower users to handle sensitive data responsibly while maintaining the integrity and usability of their datasets.
