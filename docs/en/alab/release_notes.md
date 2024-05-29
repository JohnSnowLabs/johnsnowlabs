---
layout: docs
comment: no
header: true
seotitle: Release Notes | John Snow Labs
title: Release Notes
permalink: /docs/en/alab/release_notes
key: docs-training
modify_date: "2024-04-11"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## Project Merging, Bulk Pre-Annotations and Ad-hoc backups in the Generative AI Lab 6.1
We're excited to introduce Generative AI Lab 6.1, featuring several upgrades to enhance your NLP experience. A standout feature is the ability to merge tasks across different projects, which improves annotator agreement analytics and enriches the training models with superior data completions. Additionally, the bulk pre-annotation of incomplete tasks simplifies workflows by removing the need for manual sorting and saves valuable time. The new capability to assign multiple annotators to a single task promotes teamwork. Users also have the option to initiate ad-hoc backups from the backup page, reinforcing data security on demand. Furthermore, the import page has been revamped, now offering separate tabs for cloud and local uploads, creating a cleaner and more user-friendly interface. For a detailed overview, please review the release notes below. 

## Enhanced Project Collaboration with Task Merging Capability 
Version 6.1 brings a new feature that enables the merging of tasks from two different projects. This functionality allows the consolidation of annotations created as part of different projects into one project, optimizing the processes for training and analysis.

**Key Features:**
**Merging Tasks Across Projects:** Users can now combine tasks from two different projects into a single project, provided that the projects share the same configuration and labels. If the tasks and their IDs are identical, their completions will be merged. If not, the imported tasks are added as new, while preserving any existing completions. 

**Streamlined Workflow:** Merging tasks is a straightforward process:
  1. Export tasks from one project. 
  2. Go to the import page of the target project. 
  3. Import the tasks.
     
 ![zeroPrompt](/assets/images/annotation_lab/6.1.0/2.gif)

In previous versions, importing task with task IDs and task contents identical to existing tasks was not possible. With the introduction of this new feature, users can now seamlessly merge projects without having to delete existing tasks or overwrite completions. 

This improvement simplifies project management and enhances collaboration by enabling users to effortlessly consolidate annotations from multiple projects. 

## Bulk Pre-Annotation of All Incomplete Tasks
Version 6.1 brings a new feature that facilitates the bulk pre-annotation of all incomplete tasks. This upgrade streamlines the pre-annotation process, enabling users to apply pre-annotations to all incomplete tasks simultaneously, eliminating the need for manual filtering or selection.

**Key Features:**
- **Bulk Pre-Annotation:** Users can now apply pre-annotations to all incomplete tasks in one go. 
- **Simplified Workflow:** This feature removes the need to manually filter or select tasks for pre-annotation.
  
 ![zeroPrompt](/assets/images/annotation_lab/6.1.0/3.png)

This enhancement not only saves time and effort by removing the need for manual task selection but also boosts efficiency and effectiveness in the pre-annotation process, enhancing overall workflow productivity. 

## Assign multiple annotators to tasks
Previously, task assignments were restricted to one annotator at a time, requiring repetitive processes to assign multiple annotators to a single task. With version 6.1. the platform offers the possibility to simultaneously assign multiple annotators to a task, greatly reducing time and simplifying the task management work. Assignments are visually confirmed with a tick mark next to each assigned annotator. Clicking on an annotator's name a second time will remove them from the task. However, the assignment of reviewers has not changed; only one reviewer can be assigned per task. 

 ![zeroPrompt](/assets/images/annotation_lab/6.1.0/4.gif)

## Improvements
### Trigger Ad-hoc backups
Version 6.1 introduces the ability for users to initiate ad-hoc backups directly from the backup page on demand. Previously, triggering backups required manual editing of the cronjob from the backend to manage file and database backups outside of the scheduled times. This update simplifies the process, enabling users to easily start backups with just a click. 

**Key Features:**
**On-Demand Backup:** Users can now trigger ad-hoc backups at any time from the backup page. The backup process involves:
  1. Entering the S3/Azure Blob credentials. 
  2. Clicking the backup button. 
     
 ![zeroPrompt](/assets/images/annotation_lab/6.1.0/5.png)

**Simplified Interactions:** Prior to this update, initiating backups outside of the scheduled times required manual cronjob modifications. Now, backups can be initiated directly from the UI.

This enhancement gives users increased flexibility and control, making it easy and efficient to initiate backups whenever necessary with just a click.

### Optimized Import Page
Generative AI Lab 6.1 comes with an optimized import page, improving user experience. The page retains all its original functions but now includes separate tabs for cloud imports and local imports, creating a more streamlined and user-friendly layout. 

**Key Features:**
- **Optimized User Interface:** The import options for cloud and local uploads are now distinctly separated into different tabs. 
- **Cleaner Interface:**  The import page sports a cleaner, more organized design, improving user interaction.
- **Consistent Functionality:** Despite the redesign, all the existing import functionalities remain unchanged, providing users with stability. 

**Local Import**

 ![zeroPrompt](/assets/images/annotation_lab/6.1.0/6.png)

**Cloud Import**

 ![zeroPrompt](/assets/images/annotation_lab/6.1.0/7.png)

This redesign enhances the user experience by offering a more structured and intuitive interface for importing tasks, while preserving all the previous capabilities. 

### Optimized Team Members Page
   1. Previously, the Team Members Page included already assigned users in the search results, complicating navigation. Now, search results exclusively show unassigned users. 
   2. The "Dismiss" button on the user card has been removed as it was redundant. 
   3. The user card design has been refined to use space more efficiently. Although it is smaller overall, it now adjusts its size for larger screens to maintain a uniform and appealing display across various devices. 
   4. To better accommodate smaller screens, the spacing between elements on the page has been significantly reduced. This adjustment ensures that all components fit well within the screen's limits, enhancing the user experience on smaller devices.

 ![zeroPrompt](/assets/images/annotation_lab/6.1.0/8.png)

### Optimized Relation Widget
Previously, the display of relationships in the sidebar only included generic labels such as "from" and "to," which made it challenging to quickly grasp the specific connections between entities, particularly when multiple relations were involved

To enhance clarity, the "Relation" widget has been updated to display the actual labeled text for both the "from" and "to" entities, whether positioned on the right side or at the bottom of the interface. Furthermore, if the full labeled text does not fit within the widget, hovering over it will display the complete text, facilitating easier identification of relations in any context. The widget shows more text when positioned at the bottom and less when on the right side. 

 ![zeroPrompt](/assets/images/annotation_lab/6.1.0/9.gif)

### Targeted Tasks Import from Azure Blob Storage 
Previously, task imports from Azure Blob were restricted to using the container name, which affected all tasks within the import. Recent updates have introduced greater flexibility by allowing users to specify individual tasks for import using a detailed syntax: {container_name}/{complete_file_path}. 

This enhancement provides a more precise method for importing tasks, enabling users to selectively import specific tasks from a container instead of indiscriminately importing all tasks. 

 ![zeroPrompt](/assets/images/annotation_lab/6.1.0/10.gif)

### Enhanced Prompt Filters 
The Prompts List Page has been updated to provide users with more refined filtering capabilities. New options include "Open Source" and "External" for filtering by Domain, and "Classification" for filtering by Type. Selecting "Open Source" will display prompts related to the Open Source domain, while choosing "External" will show all prompts from External LLMs. The "Classification" option filters the prompts to show only those related to Classification tasks. Users can easily switch between filters to update the displayed prompts or remove a filter by reselecting the same option, which will show all prompts without any filters. 

 ![zeroPrompt](/assets/images/annotation_lab/6.1.0/11.gif)

### Label Editing for Uploaded Models
Previously, correcting even a single typo in a model's labels required users to delete and then re-upload the model with the correct prediction entities. Now, admin and supervisor users can edit the labels of uploaded models that are currently not in use in the project.

 ![zeroPrompt](/assets/images/annotation_lab/6.1.0/12.gif)

### Incorporating Base Model Prediction Labels in Transfer Learning Training 
In previous versions, during transfer learning, only the labels used in the current project configuration were transferred from the base model to the newly trained model. Now, with the introduction of the "Include Base Model Labels" checkbox in the training settings, users have the option to ensure that all labels from the base model are incorporated into the training of the new model when this option is activated..

 ![zeroPrompt](/assets/images/annotation_lab/6.0.0/13.png)

### Enhanced Search Functionality on Models Hub Page 
Version 6.1 brings another improvement to the search capabilities on the ModelHub page, enhancing both efficiency and user experience. By extending the debounce time, the search functionality has become more responsive and effective. Users will now enjoy quicker and more precise search results, facilitating an easier and more streamlined model selection process. 

This enhancement ensures a smoother and more efficient experience for users when searching for models. 

### Bug Fixes

- **User can see add group to a shared project**
	
	Previously, the system permitted users to access the "Groups" action for both owned and shared projects. However, if a user tried to assign a group to a shared project, an error message was displayed: “User 'admin' not allowed to assign/revoke group from projects(s)!” Moreover, when users selected both owned and shared projects simultaneously for group assignment, the system displayed a success message, but only the owned project was actually assigned to the group.
	
	Now, the functionality has been updated to allow users to assign groups only to projects they own. The group assignment option is disabled for shared projects, preventing any confusion or error messages.

- **The first token in the dictionary of a rule is not pre-annotated**
	
	Previously, the first entity in the dictionary rule was reserved for the name of the rule. However, this reservation has been removed. Now, the first entity in the dictionary rule is pre-annotated.

- **Relation prompt is also shown in the list of NER prompts during pre-annotation**

	Previously, the first entity in the dictionary rule was specifically designated as the name of the rule. This requirement has now been eliminated. Currently, the first entity in the dictionary rule is used for pre-annotation.

- **In Visual NER projects the special characters are included along with the texts when labeled, but in NER project only text is labeled** 
		
	Previously, in Visual NER projects, special characters were inadvertently included with the text during labeling. In contrast, only the text was labeled in NER projects when tasks were pre-annotated using NER models. This inconsistency has now been addressed. Special characters are no longer included with the tokens, resulting in more accurate predictions in Visual NER projects when utilizing NER models.

	![zeroPrompt](/assets/images/annotation_lab/6.1.0/14.png)

- **Separate texts are labeled as one in Visual NER project when separated by special characters**
		
	Currently, in Visual NER projects, texts separated by a comma were incorrectly labeled as a single entity during pre-annotation with the NER model. This problem has been resolved. Now, tokens separated by special characters are appropriately recognized and labeled as distinct texts.

- **Uppercase words are skipped when pre-annotating tasks in VisualNER project**
			
	Previously, uppercase words were overlooked during prediction. This issue has now been corrected, and tokens are no longer omitted during pre-annotation..

- **Validation for External Service Provider is not working during edit**
		
	In edit mode, the "VALIDATE" option is initially disabled. However, once the user modifies the Secret Key, validation becomes available and is now operating correctly.

- **Relations point to empty tokens when the right sidebar shrinks**
		
	Previously, during the review of pre-annotations, relations would incorrectly point to empty tokens when the left sidebar was minimized. This issue has been addressed, ensuring that relation lines now remain consistent and no longer point to empty tokens, regardless of whether the sidebar is expanded or collapsed.

- **"Server limit reached" dialog box is not shown when trying to deploy the configuration from Customize Labels page**
        
    Previously, when the server limit was reached during an attempt to deploy the configuration from the Customize Labels page, the dialog box that should indicate this did not appear. Now, this dialog box is properly displayed as expected.

- **Hotkey shortcut "m" in labeling page to "Add metadata when region is selected" is not working currently**
        
    Previously, the "m" hotkey shortcut on the labeling page, which was intended to "Add metadata when region is selected," was malfunctioning. This issue prevented users from efficiently attaching metadata to labeled text. Now, pressing the "m" key while a label is selected will properly activate the text area for adding metadata, allowing users to smoothly input the necessary information.

- **Pressing Hotkey shortcut "alt+tab" in labeling page is not working as expected.**

	Previously, the hotkey function "alt+tab" was problematic. Rather than allowing users to navigate between labeled texts within a specific task, pressing "alt+tab" mistakenly triggered navigation across various sections of the webpage, behaving like a typical browser shortcut. This caused users to unintentionally move between different sections of the webpage, rather than navigating through the labeled texts of the task at hand.

	Now, users can press the shortcut key "alt+tab" to navigate between different labeled texts as intended.

- **Same rules are imported multiple times when importing Demo Project**
		
    Previously, importing Demo Projects led to duplicate rule downloads. Now, upon importing a project, its associated rules will only be downloaded once.

- **Tasks are still classified based on labels that were removed from project configuration**
		
    In the past, tasks were categorized according to labels that had been removed from the project configuration. Now, tasks are no longer categorized for labels that are not included in the project configuration.

- **Exporting Tasks without completions include tasks with deleted completions**
		
	Previously, when exporting tasks without completions, it included tasks with deleted completions. This issue has now been fixed.

- **Images/PDFs are not exported for Image Classification and Rate PDF Project type**
		
    Previously, Images/PDFs were not exported for Image Classification and Rate PDF Project types. This issue has now been resolved.

 
</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

<ul class="pagination owl-carousel pagination_big">
    <li><a href="annotation_labs_releases/release_notes_6_1_2">6.1.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_1_1">6.1.1</a></li>
    <li class="active"><a href="annotation_labs_releases/release_notes_6_1_0">6.1.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_0_2">6.0.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_0_0">6.0.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_9_3">5.9.3</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_9_2">5.9.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_9_1">5.9.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_9_0">5.9.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_8_1">5.8.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_8_0">5.8.0</a></li>
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
</ul>
