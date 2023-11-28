---
layout: docs
comment: no
header: true
seotitle: Release Notes | John Snow Labs
title: Release Notes
permalink: /docs/en/alab/release_notes
key: docs-training
modify_date: "2023-11-28"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 5.6.0

Release date: **10-24-2023**

## Streamlined Task Classification and Targeted Exports in NLP Lab 5.6 
NLP Lab 5.6 introduces features that speed up text classification, simplify data exports, and offer more intuitive management of project resources. The Compact View option allows one to classify short tasks from the Tasks page, bypassing the need to open each task individually. Further enhancing this, the Focus View feature aids in managing multiple classification models by allowing users to focus on one at a time. 
Significant enhancements have also been added to the export process. The new annotator-specific export filters streamline the segregation of annotations by individual annotators, reducing the effort involved in processing exported files. Additionally, a filter for exporting tasks with pre-annotation results has been added for more targeted data export. Improvements extend to user interface enhancements in the "Reuse Resources" settings and the Train page, making project configuration and training more user-friendly and efficient.

## New: Classify Short Text on the Tasks View 
In the realm of text classification, particularly for projects involving short content tasks, enhancing productivity becomes crucial. To address this challenge in view of optimizing annotation speed and convenience, NLP Lab 5.6. introduces a new layout of the Tasks screen - the Compact View-  optimizing space and enabling annotators to classify tasks directly from the Task List page. This bypasses the conventional, more time-consuming method of individually opening and submitting completions for each task. 
First, let us see how one can enable the "Compact View" for NLP Lab Projects.

### Activating the Compact View Option 

Within the Project Configuration screen, under the “Customize Labels” Tab a new checkbox option was added as part of the “Configure Annotation Experience” Section - “Allow compact view for tasks list”. 

![Compact VIew in Project Configuration](/assets/images/annotation_lab/5.6.0/1.gif)

Once this option is activated by a project owner or manager, annotators can configure and manage the Compact View settings directly on the Task List page.

### Compact View

A convenient “Show Compact View” checkbox is available on the pop-up activated by the "3-dot Menu". Once the option is activated, a compact view of each task is displayed on the tasks page, allowing annotators to quickly go over the short texts and classify them in place. Despite its compact nature, this view retains all the functionalities of the standard Task List view, offering annotators the flexibility to switch back to the normal view at any time.

![Enable the compact View](/assets/images/annotation_lab/5.6.0/2.gif)

### Classify in Place

Further enhancing the utility of the Compact View is the “Classify in Place” feature. With this option enabled, annotators can classify tasks without leaving the Task List page. The UI allows annotators to focus on each one of the choices presented in the project configuration for each task, thus enabling efficient and rapid task classification. When a user chooses one classification option for a given task, a completion is automatically generated, submitted as Ground Truth (Starred Completion), and the task is marked as "Submitted". This entire process streamlines task handling, eliminating the need to open individual tasks. 

![Classify in Place](/assets/images/annotation_lab/5.6.0/3.gif)

### Focus on One Classifier at a Time

For projects involving multiple classification options, when showing all choices on the Compact View the page becomes crowded. In this situation, the Focus View feature helps eliminate some of the options and allows users to focus on one classification dimension at a time. This declutters the view and enhances the annotation process's efficiency and effectiveness. Annotators can effortlessly switch between classifiers in the Focus View, adapting to their needs throughout the annotation process.

![Focus View](/assets/images/annotation_lab/5.6.0/4.gif)

## New: Filter Exported Completions by Annotator
Previously, the task of segregating data annotations made by specific annotators was a laborious process, involving the examination and processing (either manual or via custom code) of the exported JSON files to identify target completions. This method was not only time-consuming but also prone to errors. Addressing this drawback, NLP Lab 5.6 introduced an enhanced export feature that simplifies the process.

![demoExportByAnnotator](/assets/images/annotation_lab/5.6.0/5.gif)

Users can now easily select the data they want to export by applying annotator-based filters as shown in the video above. This is achieved through new selectors added to the Export page, that ensure a more targeted and efficient export experience. Once the desired annotators are selected, the completions they created can be further filtered based on their status for a refined JSON export. Specifically, users can filter out tasks that either lack completions or are marked with a starred completion, thus enabling a targeted export process. This enhancement combines with the task-based filters already in place and saves time but also increases the accuracy and relevance of the exported data, making it a valuable tool for users engaged in extensive data annotation projects. 

## New: Filter Export by Predictions
This feature empowers users to selectively filter out tasks lacking pre-annotation results when exporting tasks and completions. By integrating this option, NLP Lab further improves the export process, allowing users to focus on tasks with pre-annotation outcomes.

## Improvements
### Keyboard Shortcut for "Accept Prediction"
A keyboard shortcut was added for the "Accept prediction" button. This feature, useful for creating and submitting completions based on automatic pre-annotations can now be activated via the keyboard shortcut, allowing users to stay focused and work efficiently without changing their interaction context. Additionally, the "Accept prediction" button, which was previously unavailable in pre-annotated tasks for Visual NER projects, has been made accessible for an enhanced experience of handling pre-annotated tasks in Visual NER projects.

![demoExportByAnnotator](/assets/images/annotation_lab/5.6.0/6.png)

### Readiness Check for OCR Server on Image and PDF Import
The process of selecting OCR servers for image and/or PDF-focused projects has been refined for greater efficiency. Previously, when visual documents were imported, the system would automatically select any available OCR server on the import page. This approach, though straightforward, did not consider the specific readiness status of the project's designated OCR server. Recognizing this limitation, NLP Lab 5.6 introduces a more intelligent selection mechanism.
With the recent enhancement, the user interface is designed to temporarily pause when the project's dedicated OCR server is in the process of deployment. This pause ensures that the OCR integration aligns with the project's readiness, avoiding potential mismatches or delays that could affect the project workflow. Once the deployment of the OCR server is complete, the system automatically sets this newly deployed server as the default OCR server for the project. This ensures that the processing of images is timely for each project, enhancing the overall efficiency and effectiveness of document ingestion.


![rediness](/assets/images/annotation_lab/5.6.0/7.gif)

### Enhanced Usability of the "Re-use Resources" Settings
The "Reuse Resources" section – step 3 of the Project Configuration – has now an improved user experience and allows more efficient resource management. Initially, users faced challenges in identifying which resources (Models, Rules, or Prompts) were already incorporated into a project when visiting this section during project configuration. 

![Marked Resources](/assets/images/annotation_lab/5.6.0/8.gif)

Addressing this issue, the "Reuse Resource" tab now prominently identifies the models, prompts, and rules added to the project. Furthermore, the "Reuse Resources" feature was expanded to provide an in-depth view of specific labels, choices, or relations selected. This detailed visualization ensures users are fully informed about the resources currently in use in the project. Such transparency is crucial in aiding users to make well-informed decisions regarding the addition or removal of resources, thereby streamlining the processes within the Project Configuration Settings.

### Enhanced UI for Reuse Resource
The Reuse Resource Page has also undergone a series of enhancements, focusing on improving user navigation and the resource addition process. These updates are designed to augment the user interface while retaining the core functionality of the application, ensuring that users benefit from a more intuitive experience without having to adapt to significant workflow changes.
One of the improvements is the introduction of tab-based navigation for selecting Models, Prompts, and Rules. This shift from the previous button-based system to tabs enhances both the visual organization and the ease of navigation on the Reuse Resource page. Users can now more intuitively and efficiently locate and manage the resources they need for their projects.

Additionally, the process of adding resources to a project has been updated. Users are no longer required to click "Add to Project Configuration" button each time they select a new model, prompt, or rule. Instead, the system automatically incorporates the chosen resource into the project configuration. This refinement eliminates repetitive steps, saving users time and simplifying the process of resource selection.

These UI updates, implemented to enrich the user experience, ensure that users can manage resources more effectively while following the same workflow. The focus remains on user convenience and efficiency, underscoring the NLP Lab's commitment to continuous improvement in response to user needs and feedback.

![ReuseResourcePageUI](/assets/images/annotation_lab/5.6.0/9.png)

### Enhanced UI for Model Training
NLP Lab 5.6. updates to the User Interface of the Traininig & Active Learning page for an improved user experience and streamlined interactions. The buttons located at the top of the page have been redesigned to be more **compact** for optimized screen space, allowing users to focus on the essential elements of the page without distraction.
Another enhancement is the introduction of **sticky buttons** at the bottom of the Train page. This feature ensures that critical features, such as “Train” and “Save,” remain accessible at all times, regardless of the user’s position on the page. By eliminating the need to scroll, users can enjoy a more convenient and efficient workflow. This thoughtful design change underscores our commitment to continuously improving the user interface to meet the evolving needs of our users in the NLP Lab.
  
![img width="1510" alt="TrainingPageUI](/assets/images/annotation_lab/5.6.0/10.png)

### Bug Fixes
- **Grid showing the generated synthetic task is not showing the generated result**
	
	In the previous version, providing an incorrect secret key to generate synthetic tasks followed by the generation of synthetic tasks using the correct secret key prevented the display of results in the synthetic tasks grid view, even after providing the correct secret key. Version 5.6.0 addresses this issue, ensuring that tasks are consistently generated, and the grid is populated as intended, irrespective of the sequence of secret key inputs. Users will now experience improved reliability and seamless task generation in all scenarios.

- **Publish Model: "Python Code" Field to be prefilled with the correct embeddings as per the License type used** 
	
	The submission form for publishing Trained Models featured the Python Code Field which is prepopulated with a sample value code. In NLP Lab 5.6.0, the prefilled sample code now accurately reflects the embedding value, aligned with the appropriate license type for the model being published.

  ![Publish Model Embeddings](/assets/images/annotation_lab/5.6.0/11.gif)

- **External Classification Prompt added to Project Config, a <label> Tag is added which creates issue while saving the project**
	
	In the previous version, a label tag was automatically generated and added to the project configuration when a classification prompt was added to the project configuration, requiring users to manually remove the tag. In this release, this issue has been successfully addressed. Users can now enjoy a smoother experience, as no extra tags are added to the project configuration when utilizing classification prompts. This improvement ensures a more streamlined workflow and reduces the need for manual intervention.

- **External Classification Prompt: "Pre-annotation Failed" Status is frequently shown for no Prediction cases**
	
	In the last version, if tasks didn't give results with a certain external prompt, it wrongly showed "pre-annotation failed.” The issue has been resolved now and in this version, the right pre-annotation status when no predictions are made for a task is shown. This improvement makes it clearer and more accurate, helping users to understand task status better.


- **External Classification Prompt: "Prediction Generated" state shown even when no predictions can be seen**
	
	In the previous version, after pre-annotation, tasks were displayed with a green status, indicating that a prediction had been made. However, upon opening the task, no actual predictions were visible, creating confusion. Upon closer inspection, a phantom option, "None of the above," was inaccurately shown as predicted, even though it wasn't part of the original prompt. In this version, we've successfully addressed this issue. Now, there's no ghost option, ensuring that pre-annotation is accurate and reflective of the actual predictions made. This improvement enhances the clarity and reliability of the pre-annotation process.

- **User is not able to tag a task from the labeling page**
	
	In the last version, tagging a task from the labeling page led to an error page, preventing successful tagging. This issue has been fixed in the current version, users can now seamlessly tag tasks directly from the labeling page without encountering any errors, enhancing the overall usability of the feature.

- **Warning is shown if users attempt to add a reviewer when no reviewers have been assigned to the task**
	
	In previous versions, when users attempted to add a reviewer to a task, an unnecessary warning pop-up would appear, cautioning about replacing a reviewer even when no reviewers were initially assigned. We're pleased to share that this issue has been resolved in version 5.6.0. Now, the warning pop-up will only appear if the task already has a reviewer assigned, providing users with more accurate and relevant notifications when attempting to assign a different reviewer to the task. This enhancement ensures a smoother user experience and avoids unnecessary alerts in scenarios where they are not applicable.

- **"Delete Duplicate Tasks" feature shows all tasks as duplicates for Visual NER project**
	
	In earlier versions, attempting to delete duplicate tasks in a project using the Delete Duplicate buttons incorrectly identified all tasks as duplicates for Visual New or Image Classification projects. We're happy to let users know that this issue has been resolved in the current version. Now, the Delete Duplicate functionality accurately identifies duplicate tasks specifically for document-related projects, ensuring more precise and effective management of duplicate tasks within the project. This fix enhances the reliability of the duplicate task identification process for Visual New or Image Classification projects.

- **Removing a project that was allowed to use synthetic task provider giving Internal Server Error when  navigating to Integration Page**
	
	In previous versions, if a project initially permitted the use of an external service provider from the Integration page, and the project was later deleted from the project page, users encountered an Internal Server Error when attempting to navigate to the Integration page. This error prevented the display of external providers on the Integration page. This issue has been resolved in the latest version. Now, when a project is deleted from the project page, it is automatically removed from the allowed project list on the Integration page. This ensures a smoother experience, preventing errors and accurately reflecting the project status across pages.

- **User is not able to add "External Service Provider"**
	
	In earlier versions, deleting projects that were authorized to use an external service provider resulted in users encountering an Internal Server error. To address this issue, users had to manually delete the project IDs of the deleted projects from the backend. This bug has been resolved in the latest version, now users will no longer encounter an Internal Server error. This improvement streamlines the user experience by eliminating unnecessary errors and manual interventions

- **Unable to enable any of the settings for Annotation Experience in Config**
	
	In this version due to UI updates, initially, users experienced difficulties in enabling or disabling settings within "Configure Annotation Experience" on the "Customize Labels" page during project configurations, resulting in glitches. This issue has been successfully resolved , users can now enable or disable settings without encountering errors, and the functionality is working as expected. This fix ensures a smoother and more reliable customization experience for project configurations.


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

<ul class="pagination owl-carousel pagination_big">
    <li class="active"><a href="annotation_labs_releases/release_notes_5_6_0">5.6.0</a></li>
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
