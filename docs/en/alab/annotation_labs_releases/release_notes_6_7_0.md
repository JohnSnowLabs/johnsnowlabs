---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab Release Notes 6.7.0
permalink: /docs/en/alab/annotation_labs_releases/release_notes_6_7_0
key: docs-licensed-release-notes
modify_date: 2024-08-25
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 6.7.0

Release date: **09-30-2024**

## De-Identification Pipeline Tools and Entity Level Annotation Instruction in Generative AI Lab - 6.7
Generative AI Labs version 6.7 introduces improvements to the De-identification feature. With this update, users can choose on a per-entity basis which de-identification method they would like to use. In addition to the de-identification pipeline that is the default, there is now support for custom models, rules, and prompts for identifying sensitive data. 
 
This release also brings the ability for admin users to add annotation instructions to labels from within the project, allowing for improved label accuracy and consistency between annotators. This updated feature is available for NER and VisualNER project types.

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

## Annotation Instructions for Labels
Generative AI Lab 6.7 introduces a new feature allowing admin users to add annotation instructions to labels directly from the `Customize Labels` page. This enhancement ensures that annotators have clear and consistent guidelines, improving labeling accuracy and quality. The annotation guidelines are available for both NER (Named Entity Recognition) and VisualNER project types, offering flexibility across different project formats. 

To add annotation instructions to a label, follow these steps:
 - Navigate to the `Customize Labels` section, where all your project’s labels are listed.
 - Click on the `Edit` icon next to the label for which you want to add instructions. This action will take you to the `Edit Label` page.
 - Enter the guidelines under the `Label Instructions` field.
 - Click on `Save Label` to store the instructions.
 - Click on `Save Config` to save the configuration.

![670image](/assets/images/annotation_lab/6.7.0/10.gif)

Once annotation instructions are added, they can be viewed from the labeling page in the widget area on the right side. Users can enable or disable the annotation guidelines through the `Annotation Guidelines` toggle. To view the guidelines, the label must first be activated by clicking on it, which will display the label under the `Annotation Guideline` section. Clicking on the label text will then reveal the annotation instructions for that label. 

![670image](/assets/images/annotation_lab/6.7.0/11.gif)

Users with the Project Manager role can edit and delete annotation guidelines directly from the labeling page. However, users with the Annotator and Reviewer roles can only view the guidelines and do not have permission to edit or delete them. 

Remove the annotation instructions from the labeling page: 

![670image](/assets/images/annotation_lab/6.7.0/12.gif)

Edit the annotation instructions from the Labeling page: 

![670image](/assets/images/annotation_lab/6.7.0/13.gif)

When multiple labels are selected, the guidelines for each label can be viewed one at a time by clicking on the corresponding label text.

![670image](/assets/images/annotation_lab/6.7.0/14.gif)

Annotation guidelines can also be downloaded in JSON format by clicking on the Download icon from the Customize Labels page.

![670image](/assets/images/annotation_lab/6.7.0/15.png)

Additionally, annotation guidelines are available for Assertion Labels as well. 

![670image](/assets/images/annotation_lab/6.7.0/16.gif)

## Improvements
### Automatically turn off the "wizard mode" after the user trains the model using wizard mode

Once the training is completed, the wizard mode is automatically turned off, and users are navigated to the regular **Train** page. Here, all relevant information is displayed along with a message indicating whether the training was successful or not. 

![670image](/assets/images/annotation_lab/6.7.0/17.gif)

### Clicking on the direction arrow for a relation should jump to the respective relation in the region panel
A new improvement has been introduced which allows users to click on any of the relation lines, which will take them directly to the corresponding relation in the **Relation** section.

![670image](/assets/images/annotation_lab/6.7.0/18.gif)

### Escape key should close the dialog boxes and warnings
Users can now simply press the **Esc** key to close dialog boxes and warnings that appear in the top banner. Instead of clicking the ‘x’ every time. 
 
### The name of the model should be shown in the playground heading
The model names are shown, providing users with a clearer insight into which models are being tested. 

![670image](/assets/images/annotation_lab/6.7.0/19.gif)

### Add Quick Submit button for Visual NER task
A new ability to "Submit completions without Saving" can be enabled on the **Advanced Configuration** page when setting up Visual NER projects. This feature allows users to see and use the "Submit" button on the labeling page right from the start, enabling them to submit their completions directly without the need to save them first. 

![670image](/assets/images/annotation_lab/6.7.0/20.gif)

### Bug Fixes: 
- **Unexpected behavior corrected for relations when added in the first line of the tasks**

	Users can again see relations for submitted tasks when added in the first line. 

- **Vague error messages are now replaced with accurate notifications during task import validation**

	Users now receive meaningful error messages in the dialog when task imports fail due to validation issues. 

- **Unclear error message for importing tasks larger than 200MB addressed**

	Users will now see accurate and user-friendly error messages when attempting to import tasks that exceed the 200MB size limit. 

- **Filter Exported Annotations by Task is now disabled for de-identification projects**

	Users can no longer pick and choose labels after de-identification, ensuring consistency in exported annotations. 

- **Multiple individual files can now be uploaded at once for task import**

	Users can efficiently upload multiple files simultaneously within a project. 

- **Synthetic task list now refreshes automatically during CRUD operations**

	The synthetic task list updates in real-time during task creation, update, and deletion. 

- **"Failed to Load PDF File" error resolved for RatePDF projects with hidecontextmenu enabled**

	Users can now view tasks normally even when the hidecontextmenu property is used in RatePDF projects. 

- **Internal server error when creating RatePDF project types has been fixed**

	Users can now create RatePDF projects without encountering internal server errors. 

- **Text enclosed with <> is now visible on the labeling page**

	Users can see text within angle brackets on the labeling page, addressing the previous visibility issue. 

- **Confirmation dialog box no longer overlaps with the Labels section**

	The confirmation dialog box now displays correctly without being obscured when submitting completions from the Comparison and De-identification views. 

- **Special characters are now correctly handled when importing files from Azure SAS URL**

	Tasks can be imported from Azure SAS URLs without issues related to special character permissions. 

- **Internal server error when adding 'Test' or 'Train' tags has been resolved**

	Users can now add 'Test' or 'Train' tags to tasks from the labeling page without encountering errors. 
 
- **Classification models are now visible in the Select Classifier dropdown**

	Classification models are correctly listed for selection in the dropdown menu. 
	
</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}