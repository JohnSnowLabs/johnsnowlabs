---
layout: docs
comment: no
header: true
seotitle: Release Notes | John Snow Labs
title: Release Notes
permalink: /docs/en/alab/release_notes
key: docs-training
modify_date: "2023-12-21"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## NLP Lab 5.8 – NER Models for Visual NER, Import Export to Azure Blob, and Gesture-based annotations for Assertions.
We are excited to release NLP Lab 5.8, bringing significant updates designed to enhance and expand the capabilities of your NLP workflows. This release marks a milestone in our commitment to providing comprehensive NLP solutions, introducing a suite of powerful features and improvements. With the integration of the entire NER model library for text data into Visual NER projects, seamless Import and Export functionality for Azure Blob, and innovative gesture-based annotations for assertions, NLP Lab 5.8 is set to change the way you manage and annotate tasks, in particular those focused on PDF and image documents. These advancements, alongside our continuous focus on performance and user experience improvements, demonstrates our dedication to supporting the evolving needs of the NLP community. Explore the boundless possibilities with NLP Lab 5.8 and elevate your NLP projects to new heights.

## Features
## Repurpose text-based NER models for PDF and images 
NLP Lab 5.8 introduces a groundbreaking enhancement to Visual NER projects by allowing users to leverage the vast library of pre-trained NER models specific for text content [6,600+ models available on the Models Hub](https://nlp.johnsnowlabs.com/models?task=Named+Entity+Recognition), for the pre-annotation of PDF or image tasks. This addition not only expands pre-annotation options but also significantly streamlines the annotation process, saving users precious time and effort. 
With this game-changing enhancement, users can now:
- **Effortlessly Jumpstart Data Preparation Projects:** Quickly initiate data preparation projects for training small Visual NER models tailored to specific tasks, reducing the time and resources required for manual labeling.
- **Utilize Existing Domain-Specific Expertise** Leverage the extensive library of NER models, including domain-specialized models that were previously confined to text-based tasks. This opens up new possibilities for processing image and PDF documents with specialized NER models, enhancing the accuracy and effectiveness of pre-annotation.
- **Streamline Workflow with Pre-trained Models:** Eliminate the need for training Visual NER models just to predict specific labels when those are already available in existing text processing models. Simply select the relevant pre-trained NER model(s) you need directly from the NLP Lab library and seamlessly integrate them into your projects.
## Effortlessly Pre-annotate PDF or Image Documents with NER Models
Configuring your Visual NER project to use text-specific NER models for pre-annotation is a breeze:
- **Project Configuration:** Begin by creating a new project and selecting the Visual NER Template during configuration. This sets the stage for seamless integration of NER models into your project.
- **NER Model Selection:** From the Re-use Resource page, navigate through the vast library of NER models and choose the one that best suits your project's requirements. Once selected, save the project configuration to apply the chosen model.
- **OCR Document Import:** Import the OCR documents containing the data you wish to pre-annotate. These documents can be in PDF or image format, catering to a wide range of document types.
- **Pre-annotation Automation:** Leverage the selected NER model to automatically pre-annotate the imported OCR documents. This eliminates the need for manual labor and significantly expedites the pre-annotation process.
- **Accuracy Verification:** After pre-annotation, meticulously review the automatically generated annotations to ensure accuracy and address any discrepancies.

![1](/assets/images/annotation_lab/5.8.0/1.gif)

This new feature empowers users to seamlessly integrate NER models into their Visual NER projects, fostering greater flexibility and efficiency in document annotation workflows within NLP Lab. By leveraging the power of NER models, users can streamline pre-annotation processes, reduce training time, and achieve enhanced accuracy, ultimately accelerating their data preparation efforts.

## Azure Integration for Enhanced Task Management

NLP Lab 5.8 introduces a pivotal enhancement that expands task management capabilities by seamlessly integrating with Azure Blob storage, complementing the existing support for AWS S3. This integration empowers users to streamline task import and export processes, fostering greater efficiency and flexibility in their data handling workflows within the NLP Lab platform.

### Effortless Task Import from Azure Blob Storage:

Importing tasks from Azure storage containers is now as straightforward and intuitive as importing from AWS S3. Follow these simple steps to effortlessly integrate your Azure data into NLP Lab projects:
- **Prepare the Azure Source:** Ensure the Azure storage container from which you intend to import tasks is readily accessible and the target files are available. NLP Lab can currently accommodate various document types such as text, PDF, images, videos, and sound files.
- **In your NLP Lab project:** Navigate to the Task Import page of the project where you wish to import tasks.
- **Select Azure Blob Storage:** Choose the "Azure BLOB" import option by clicking on the corresponding radio button on the Import page.
- **Enter Azure Credentials:** Provide the Azure connection details: Azure Container Name, Azure Account Name, and Azure Account Secret Key.
- **Initiate Import Process:**  Click the "Import" button to seamlessly transfer compatible documents from the specified Azure container into the current NLP Lab project.

![1](/assets/images/annotation_lab/5.8.0/2.gif)

### Seamless Task Export to Azure Blob Storage:

Exporting projects to Azure Blob storage is now an equally streamlined process:

- **Access Export Page:** Navigate to the "Export Tasks" page within the NLP Lab platform.
- **Specify the Tasks to Export:** Use the filter on the page to select the tasks you want to export as well as the target format and click the Export button.
- **Select Cloud Export Option:** Navigate to the "Cloud Export" tab on the pop-up and select "Azure BLOB" from the available cloud storage options.
- **Enter Azure Credentials:** Provide the Azure connection details: Azure Container Name, Azure Account Name, and Azure Account Secret Key.
- **Optionally Save Credentials:** Save the credentials for future use to expedite subsequent exports to Azure Blob storage.
- **Initiate Export Process:** Click the "Export" button to seamlessly transfer the selected project tasks into the specified Azure Blob container, ensuring effortless data backup and management.

This integration with Azure Blob storage empowers NLP Lab users to manage tasks with unparalleled efficiency and flexibility. By leveraging the power of Azure, users can seamlessly import and export tasks, streamline data handling processes, and enhance their overall NLP Lab experience.

![1](/assets/images/annotation_lab/5.8.0/11.gif)

## Centralized Log Access from Clusters Page
NLP Lab 5.8 introduces another new feature that simplifies server management by granting users direct access to server logs from the Clusters page. This feature provides critical insights, especially when troubleshooting issues across various server functions. This enhancement eliminates the need for manual command-line access, ensuring easy log retrieval and facilitating efficient troubleshooting. 

### Effortless Log Viewing from the Clusters Page
Navigating to the Clusters page, users can now easily access logs for all deployed servers, including training, preannotation, OCR, and playground servers. A dedicated button has been added to the cluster page, providing a single point of access for viewing server logs.

![1](/assets/images/annotation_lab/5.8.0/3.png)

This streamlined approach to viewing server logs enhances the user experience and operational efficiency within NLP Lab, offering a more intuitive and accessible way to manage and diagnose server-related issues.

![1](/assets/images/annotation_lab/5.8.0/4.png)

### Improvements

#### New Gesture for Assertion Status Annotation 
Annotating assertions has historically been a tedious task, requiring users to repeatedly select an already annotated text fragment and assign an assertion label. To address this issue, we introduce a gesture-based annotation mechanism that simplifies the process significantly.

This new gesture enables users to annotate a text chunk with a single click, followed by the selection of the desired assertion label. This immediate action eliminates the need for repeated selections, significantly reducing annotation time and effort. The new gesture applies specifically to the assertion label on the clicked token or chunk, ensuring precise annotation without ambiguity.

To further enhance user experience, assertion labels in the label selection widget are now decorated with a dotted line, effectively distinguishing them from NER labels and preventing any potential confusion. This visual indication reinforces the distinction between assertion labels and NER labels, allowing users to make informed choices seamlessly.

![1](/assets/images/annotation_lab/5.8.0/6.jpeg)

#### Model Evaluation servers are now queued
A refinement has been implemented in version 5.8, whereby the Test Configuration for Model Evaluation is queued when there are insufficient resources. Users now can abort the test configuration (evaluation) if triggered unintentionally. Furthermore, a pop-up is presented to guide users in deleting an existing server when the maximum server count is reached.

NLP Lab 5.8 adds another improvement addressing resource constraints during model evaluation. The Test Configuration feature, which evaluates a model for the current project tasks, is now intelligently queued until sufficient resources are available. Additionally, a user-friendly feature allows users to abort the test configuration in case of accidental initiation. Furthermore, a helpful popup appears when the maximum server count is reached, guiding users through the process of deleting an existing server to free up resources for new evaluations.

![1](/assets/images/annotation_lab/5.8.0/6.jpeg)

#### Task Assignment from the Tasks Page
Another enhancement introduced by NLP Lab 5.8 refers to the process of assigning annotators and reviewers to specific tasks. Now, directly from the task details page, users can allocate annotators and reviewers to a tasks without the need to navigate to the tasks list, and thus lose the current work context. This improvement not only saves valuable time but also enhances the user experience by simplifying task management within the platform. 

By enabling direct assignment of annotators and reviewers from the task details, we ensure a more efficient workflow, allowing users to focus on project execution with fewer interruptions and less navigational overhead.

![1](/assets/images/annotation_lab/5.8.0/7.gif)

#### Alphabet Resource Support in Rules for Enhanced Language Processing
NLP Lab 5.8 offers language support for French, German, Greek, and Spanish characters within free rules. This enhancement empowers users to incorporate special characters such as é, í, α, β, γ, δ, ü, ß, and more into their dictionaries while creating rules and using them for pre-annotation, expanding the application's versatility in handling diverse language requirements.

By incorporating special characters into free rules, users can achieve more accurate and reliable pre-annotation results, enhancing their overall workflow efficiency and productivity.

![1](/assets/images/annotation_lab/5.8.0/8.gif)

#### Disable "Filter Tasks by Tags" when Tasks Splitting with Test/Train Tags is Selected
When segregating training data based on Test/Train tags, the system now omits the tag-based filter. As a result, tasks marked for testing are exclusively considered for the testing phase, whereas the remaining tasks are automatically designated for training.

![1](/assets/images/annotation_lab/5.8.0/9.png)

#### Updated Filter: "Filter Pre-annotation according to the sections of my latest completion"

For Section-Based Projects, where one task can have different section segmentations created by different annotators as part of their work, NLP Lab provides the ability to pre-annotate tasks for all the available sections. To enhance intuitiveness, a filter is provided to selectively display pre-annotation labels only for the sections of the latest completion of each task. The filter description has been updated to better convey its functionality to our users.

#### Enhanced Performance in Visual NER Pipeline
Version 5.8 introduces substantial efficiency improvement of task import within OCR-based projects. These improvements are primarily aimed at reducing memory consumption and enhancing the loading efficiency of pipelines, thereby elevating overall performance during task import.

Key updates include a more memory-efficient OCR pipeline that eliminates the need for multiple loadings throughout the task import process. This refinement leads to a more streamlined and effective use of memory, facilitating a smoother import experience.

Users leveraging OCR pipelines for task imports in NER projects should note:

- Server operations may still halt upon reaching memory capacity limits, which is to be anticipated.
- In scenarios where multiple pipelines are deployed for task imports, performance, and memory usage metrics are consistent with those observed in the previous release.
- 
#### Improved Experience on Upgrade
The upgrade pathway in NLP Lab has been refined in version 5.8, particularly addressing the challenges related to admin password changes through the UI. Previously, such changes led to upgrade failures, necessitating a manual update of the password in the 'annotationlab-updater' configuration. We are pleased to report that this issue has been effectively resolved in the latest release, ensuring a more fluid and user-friendly upgrade process.

![1](/assets/images/annotation_lab/5.8.0/10.png)

When initiating an upgrade to version 5.8 or beyond, users will be prompted to enter the new admin password, should it have been modified. This step is designed to automate the admin password update, thereby removing the need for manual adjustments to configuration files. Users who have not changed their admin password can simply proceed by pressing "Enter." This enhancement not only streamlines the upgrade process but also minimizes the likelihood of errors and saves valuable time.
### Bug Fixes
- **Filter in Models Hub page incorrectly lists Pipelines when Healthcare is selected in edition filter**
    
    In the past, when utilizing filters on the Models Hub page to display healthcare-type models, pipelines were inadvertently included in the list. The filter conditions have now been refined to accurately distinguish between models and pipelines. As a result, the Models Hub page no longer displays OCR pipelines when filtered specifically for healthcare-related content.

- **Downloaded embedding status not updating without refresh**

    In the past, after an Embedding was successfully downloaded, it continued to display the status "downloading," leaving the user waiting without notification. This issue has now been resolved.

- **SDOH classification models do not give any pre-annotation results**

    Previously, there was an issue where SDOH classification models did not provide results for any task. This issue has been resolved, and the model can now be deployed in the playground and utilized for pre-annotation in projects without encountering any errors.

- **Error When users without admin privilege import projects**

    Previously, non-admin users attempting to import a project with team members encountered an internal server error. This issue has been addressed, and now, if a non-admin user attempts to import a project with users not yet existing in the application, the import process fails with an appropriate error message.

- **During bulk pre-annotation if it fails for a single task, pre-annotation fails for all the tasks in the Visual NER project**

    Previously, users were unable to pre-annotate multiple tasks simultaneously, and if one pre-annotation failed, the entire batch of selected tasks would also fail. The current implementation has enhanced memory usage, allowing for improved bulk pre-annotation. Now, pre-annotation for all tasks does not fail as it did before. However, tasks are pre-annotated until the pre-annotation server memory limit is reached. Subsequently, pre-annotation fails for the remaining tasks, which need to be selected and pre-annotated again.

- **Clicking on the labels part of edition dropdown in NLP Models Hub Page does not select/unselect the checkbox**

    Previously, clicking on labels in the edition dropdown on the NLP Models Hub Page did not effectively select/unselect the checkbox. This issue has been resolved, filters are now successfully selected when the corresponding text is clicked.

- **Benchmarking details Popup for trained RE Models shows Epoch values**

    Initially, the Training Logs for the RE model did not display Benchmarking data. Clicking on the Benchmarking button presented Epoch Values instead of the expected Benchmarking Data in the Benchmarking PopUp. Now, the Benchmarking Data is appropriately shown at the end of the training logs for RE models. Additionally, this Benchmarking Data is also visible on the Benchmarking UI on the Models Page.

- **Reuse Resources: Unable to remove RE models from the models list shown during "Multi-embeddings detected" case**

    Previously, attempting to remove the RE model from the Multi-embeddings detected list displayed a confirmation message, but it was not effectively removed from the configuration. The tick mark associated with the RE model persisted. Now, the RE model is removed from the Multi Embeddings detected list in the same manner as other models, ensuring both the confirmation message and the tick mark are appropriately handled.

- **Training Page: Saved Training Settings are reset when the training type changes**

    On the Training Page, there was a problem where saved training settings would be reset when the training type was changed. Initially, the saved settings, including embeddings, license type, and Transfer Learning, were not persisting. However, this issue has now been resolved, and the saved settings remain unchanged when altering the training type.

- **Playground: The text field to insert text to test models/prompts/rules in playground is disabled but editable**

    In the Playground, the text field for inserting text to test models/prompts/rules was disabled yet still editable. Although the added text did not affect the results, the disabled text field allowed editing. Now, users cannot edit the text field when it is disabled.

- **Task name not imported while importing tasks for Rate PDF projects**

    Previously, when importing tasks for Rate PDF projects, the task name was not included. This issue has been resolved, the imported tasks can be opened without encountering any errors.

- **Error when importing sample task for SBA project**

    In the previous version, sample tasks were not imported for both text and visual-based SBA projects. Issue is now fixed.

</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

<ul class="pagination owl-carousel pagination_big">
    <li><a href="annotation_labs_releases/release_notes_5_8_1">5.8.1</a></li>
    <li class="active"><a href="annotation_labs_releases/release_notes_5_8_0">5.8.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_7_1">5.7.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_7_0">5.7.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_6_2">5.6.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_6_1">5.6.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_6_0">5.6.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_5_3">5.5.3</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_5_2">5.5.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_5_1">5.5.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_5_0">5.5.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_4_1">5.4.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_3_2">5.3.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_2_3">5.2.3</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_2_2">5.2.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_1_1">5.1.1</a></li> 
    <li><a href="annotation_labs_releases/release_notes_5_1_0">5.1.0</a></li> 
    <li><a href="annotation_labs_releases/release_notes_4_10_1">4.10.1</a></li> 
    <li><a href="annotation_labs_releases/release_notes_4_10_0">4.10.0</a></li> 
    <li><a href="annotation_labs_releases/release_notes_4_9_2">4.9.2</a></li> 
    <li><a href="annotation_labs_releases/release_notes_4_8_4">4.8.4</a></li> 
    <li><a href="annotation_labs_releases/release_notes_4_8_3">4.8.3</a></li> 
    <li><a href="annotation_labs_releases/release_notes_4_8_2">4.8.2</a></li> 
    <li><a href="annotation_labs_releases/release_notes_4_8_1">4.8.1</a></li> 
    <li><a href="annotation_labs_releases/release_notes_4_7_4">4.7.4</a></li>   
    <li><a href="annotation_labs_releases/release_notes_4_7_1">4.7.1</a></li>        
    <li><a href="annotation_labs_releases/release_notes_4_6_5">4.6.5</a></li>    
    <li><a href="annotation_labs_releases/release_notes_4_6_3">4.6.3</a></li>
    <li><a href="annotation_labs_releases/release_notes_4_6_2">4.6.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_4_5_1">4.5.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_4_5_0">4.5.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_4_4_1">4.4.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_4_4_0">4.4.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_4_3_0">4.3.0</a></li>
	<li><a href="annotation_labs_releases/release_notes_4_2_0">4.2.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_4_1_0">4.1.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_5_0">3.5.0</a></li>
	<li><a href="annotation_labs_releases/release_notes_3_4_1">3.4.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_4_0">3.4.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_3_1">3.3.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_3_0">3.3.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_2_0">3.2.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_1_1">3.1.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_1_0">3.1.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_0_1">3.0.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_0_0">3.0.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_8_0">2.8.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_7_2">2.7.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_7_1">2.7.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_7_0">2.7.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_6_0">2.6.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_5_0">2.5.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_4_0">2.4.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_3_0">2.3.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_2_2">2.2.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_1_0">2.1.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_0_1">2.0.1</a></li>
</ul>
