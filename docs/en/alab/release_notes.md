---
layout: docs
comment: no
header: true
seotitle: Release Notes | John Snow Labs
title: Release Notes
permalink: /docs/en/alab/release_notes
key: docs-training
modify_date: "2023-06-02"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 4.10.0

Release date: **04-05-2023**

## Trial License Integration, Comment and Tag Functionality, and Enhanced Task Export Filters NLP Lab 4.10

We are thrilled to announce the release of NLP Lab version 4.10, which comes with an array of exciting new features aimed at enhancing user experience and improving the efficiency of the platform. Among the notable additions are the integration of a trial license, enabling users to explore the full potential of NLP Lab, and the seamless automatic import of the trial license into the platform. 

Additionally, users can now conveniently add comments in the Labeling Page, providing a more collaborative and organized environment for annotation tasks. Another valuable feature introduced in this release is the ability to add tags directly in the Labeling Screen, allowing for better categorization and management of labeled data. Lastly, the update includes an expanded range of filters when exporting tasks, empowering users to customize and streamline their task exports.

Here are the highlights of this release:

## Get trial license from License page

In version 4.10.0, we have implemented an updated License page layout, providing a simpler process for acquiring a trial license. Users can now request a trial license directly from the License page, eliminating the need to navigate to external pages. This new workflow introduces a dedicated "Get License" tab, while the Import License and Existing Licenses tabs remain unchanged.

To obtain a trial license, users are required to fill out the form on the "Get License" tab, providing their organizational email. Once the form is submitted, a validation link is sent to the provided email address and the trial license is automatically imported to the NLP Lab when the link is clicked, making it readily available for use.
![trial-license](/assets/images/annotation_lab/4.10.0/1.png)

## Comments in the Labeling Page

NLP Lab 4.10 introduces an enhanced comment feature for labeling pages, enabling users to easily add, update, and delete comments within labeling pages. This feature significantly improves work efficiency and productivity and enhances communication between team members, leading to faster delivery and more effective collaboration. To access this feature, users can find the New Burger menu located at the top right of the labeling page. Within the burger menu, users will find an option for Comments, which displays the total number of comments. By clicking this option, a new pop-up window will appear, providing access to various commenting features.

![Comments](/assets/images/annotation_lab/4.10.0/2.gif)

## Tags from the Labeling Screen

NLP Lab 4.10 introduces an enhanced tags feature for labeling pages. This feature provide users with a convenient way to create, add, and remove tags from tasks directly on the labeling page. It significantly contributes to better organization and enahnced productivity streamlining task management by offering users increased flexibility in categorizing and tracking their labeled data. Similar to the comment feature described above, the tag feature can be accessed through the burger menu located at the top right corner. The burger menu displays the total number of tags associated with its functions. By clicking the burger menu option, a new popup window appears, allowing users to add existing tags or create new ones. 

![tags](/assets/images/annotation_lab/4.10.0/3.gif)

## Filters for exporting tasks

This version of NLP Lab (v4.10.0) comes with a new feature: selective annotation exports. Users can now choose which annotations to export by using two new filters on the export page. These new filters can be combined with other filter options like tags, Only ground truth, and Exclude tasks without Completions. 
1. Filter Exported Annotations by Task:
  this filter allows users to select annotations based on the task (NER, Classification, Assertion, Relation Extraction) 
2. Select Annotations to Include In the Export:
  this filter can be used to select available labels, classes, assertion labels, or relations.
![add-filter-for-export](/assets/images/annotation_lab/4.10.0/4.gif)

## Improvements

### Add video template to the project content type

The current release, re-introduces the Video content type to the project configuration page. This provides the users with a flexible way to annotate projects that are based on video content.

![videotemplate](/assets/images/annotation_lab/4.10.0/5.png)

### Image path for visual NER task export JSON should always be in list
The inconsistency with regards to the format of the image property value in the exported task JSON was eliminated in the current version. When there was a single image task, the image property had a value of string type, but for multiple images, it was of list type. To ensure consistency, the image property will now always have a value of list type.

### Remove items in chart with empty value  for "Tasks by Status" chart

In the previous versions, "Tasks by status" chart displayed redundant values(0.00%) when there are no tasks for the specific status category. In the current release, these redundant values have been removed from "Tasks by status" chart in the analytics page.

![taskschart](/assets/images/annotation_lab/4.10.0/6.png)

### Tasks and Project filters based on multiple tags

Filtering tasks based on tags , inside the task view's tag filter has been updated to allow users to select multiple tags from the Tags dropdown. This allows filtering of the tasks based on multiple criteria. In our  previous versions, the users were limited to selecting only one tag at a time, making the filtering mechanism restrictive when attempting to narrow down tasks based on multiple tags simultaneously. The new functionality increases productivity by allowing users to apply multiple filter criteria for retreiving the desired list of tasks, matching at least one of the selected tags.

![filter](/assets/images/annotation_lab/4.10.0/7.gif)

Additionally, the same improved filter behaivour can be found in project page too. This provides users with increased flexibility and efficiency in filtering tasks based on multiple tags, thereby improving task and project management and facilitating a more streamlined workflow.

### Bug Fixes
- **ALAB-2212 Audio/Video cannot be played after the completion is submitted** 
  
    In previous versions, users were not able to play/pause Audio/Video after the completion is submited. The bug has been resolved in the latest release, allowing users to play/pause Audio/Video after the completion is submitted.

- **ALAB-2312 When the group color is white the project name, description and instructions cannot be seen on the project card**
    
    In the latest release, the problem with the visibility of the project name, description, and instructions on the projects page has been resolved. Previously, when assigning the group color white to the project group, the text was not visible because it blended with the white background.
    
- **ALAB-3133 Validation is missing in the UI from the configuration when invalid orientation is added**

    This release includes the addition of validation for incorrect orientation in project configuration, accompanied by appropriate error messaging.  Hence, project configurations will only permit the inclusion of "Vertical Layout," "Horizontal Layout," and "Horizontal-Sticky Layout.

![filter](/assets/images/annotation_lab/4.10.0/8.gif)

- **Databricks license should not be imported into NLP Lab**
  
  It is no longer possible to import Spark NLP licenses generated for Databricks into the NLP Lab. Users will be presented with an error message in the UI if they attempt to upload such licenses.

![filter](/assets/images/annotation_lab/4.10.0/9.png)

- **By modifying the URL, the user can access pages of projects that have not been shared with them.**

  In previous versions, users were able to access configuration pages of projects that had not been shared with them by modifying the URL. However, this issue has been resolved in the current version.

- **Pretrained assertions are listed in dropdown when creating relation prompts**

  When creating relation prompts, a list of labels is displayed. However, the list previously included assertion labels, which are not supported for creating relation prompts. As a result, the assertion label will no longer be shown when users create relation prompts.

- **ALAB-3365 Single-word annotation is split into multiple blocks when the user is annotating a task** 

  In earlier version, annotating a single word would result in it being split into multiple blocks instead of being annotated as a single word. This issue occurred when highlighting only a few characters of the word without selecting any label initially and later attempting to annotate the entire word. This bug has been fixed in the latest release.

- **ALAB-3368 Pre-annotation button becomes irresponsive in a project with 1000s of pre-annotated task** 

  Previously, after running pre-annotation on thousands of tasks, the pre-annotation status was missing from the task cards on the Tasks page. Additionally, the pre-annotation button was unresponsive. These issues have been resolved in the latest release. The responsiveness of the pre-annotation button has also users can navigate seamlessly between different pages on the Tasks page.

</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

<ul class="pagination owl-carousel pagination_big">]
    <li class="active"><a href="annotation_labs_releases/release_notes_4_10_0">4.10.0</a></li>
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
