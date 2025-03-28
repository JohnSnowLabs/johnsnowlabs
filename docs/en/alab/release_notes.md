---
layout: docs
comment: no
header: true
seotitle: Release Notes | John Snow Labs
title: Release Notes
permalink: /docs/en/alab/release_notes
key: docs-training
modify_date: "2024-03-27"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## Generative AI Lab 7: Accelerating Clinical Annotation with HCC Coding

Generative AI Lab 7 brings many improvements that directly support real-world healthcare annotation and coding use cases. Most notably, it introduces support for Hierarchical Condition Category (HCC) coding—enabling users to streamline clinical risk adjustment workflows by automatically linking ICD codes to HCC categories, prioritizing high-value tasks, and validating codes more efficiently. The release also enables HTML-based projects to leverage Inter-Annotator Agreement (IAA) analytics for quality assurance, simplifies licensing across the suite of John Snow Labs products, and improves training scalability with dataset sampling. Enhancements to the annotation interface—including bulk label management and more precise zoom controls—further increase speed and usability. Combined with a robust set of stability and performance fixes, these capabilities give medical coders, clinicians, and data scientists the tools they need to annotate faster, train better models, and ensure higher data accuracy across large-scale projects.

## Support for HCC Coding
This release introduces support for HCC Coding for text and PDF content. The system now maps detected ICD-10 codes to their corresponding HCC codes, streamlining clinical risk adjustment workflows and insurance claim verification. 

**New project types:**
1. **HCC Coding for Text**
2. **HCC Coding for PDF and Text (side by side)**
   
These project types enable the association of HCC codes with annotated clinical entities using preconfigured lookup datasets, reducing manual input and improving consistency in medical coding.

![700image](/assets/images/annotation_lab/7.0.0/1.png)

### Usage Instructions
To enable **HCC Coding Support**, follow these steps:  

To enable HCC Coding Support, follow these steps:
1. **Project Setup**
- Select either of the new project templates during project creation. 
- Choose the HCC Coding for PDF and Text (side by side) option if you need a visual representation of the original document while performing HCC coding.

![700image](/assets/images/annotation_lab/7.0.0/2.png)

2. **Label Customization** - On the Customize Labels page, users can either:
- Apply a lookup dataset globally, to all labels in your taxonomy at once.
- Assign Lookup options to specific labels.

![700image](/assets/images/annotation_lab/7.0.0/3.png)

3. **Annotation Process**
- Annotate entities and assign codes using the annotation widget.
- Edit codes inline or through the Annotation Widget from the right panel.
- Annotated chunks are listed under their respective labels. Users can expand labels by clicking the down arrow to view all chunks associated with them.
- Lookup code can be edited or updated directly from labeled tokens or via the labeling section by clicking the edit button.
- Predictions can be copied to generate a completion, allowing the HCC code to be reviewed using the annotation widget on the right.

![700image](/assets/images/annotation_lab/7.0.0/4.gif)

4. **Review and Confirmation**
Once a task is labeled and lookup codes are assigned along with HCC Codes, reviewers have the following options:
- Accept and confirm the labeled text.
- Decline and remove the labels.
- Tag the label as non-billable, if necessary.

![700image](/assets/images/annotation_lab/7.0.0/5.png)

### Raking Score Integration

Tasks can now include **ranking scores** to support triaging and prioritization, allowing users to manage large annotation datasets more effectively. When importing tasks, users can associate each task with a ranking score that reflects its clinical significance or urgency. These scores are then displayed in the task list and can be used to sort and filter tasks dynamically. This functionality is particularly beneficial in risk adjustment workflows where prioritizing complex or high-impact cases is critical. Ranking scores also integrate with the HCC coding workflow, enabling annotators and reviewers to systematically focus on the most relevant cases for validation.

![700image](/assets/images/annotation_lab/7.0.0/6.png)

## IAA for HTML Projects with NER Labels
Inter-Annotator Agreement (IAA) analytics are now supported inside HTML projects with NER labels. This feature ensures more robust validation of annotation accuracy and promotes better alignment among annotators, enhancing overall project quality.

The existing workflow remains unchanged. Once an analytics request is granted, a new "Inter-Annotator Agreement" tab becomes available under the Analytics page in HTML projects, allowing users to access and interpret IAA metrics seamlessly.

- Access the new "Inter-Annotator Agreement" tab from the Analytics page.
- Visualize agreement charts and compare annotations across multiple users.

![700image](/assets/images/annotation_lab/7.0.0/7.png)

## Support for Universal Licenses

Licensing complexity is now significantly reduced through the addition of a universal license key that governs all John Snow Labs libraries and products. Before this update, customers faced the challenge of managing multiple licenses—a separate one for the application and others for using specific functionalities like the Visual or Healthcare features (e.g. in training or preannotation). This complexity often led to additional administrative burdens.

This enhancement simplifies deployments, and license tracking across enterprise environments. It also increases flexibility, boosts efficiency, and provides a seamless experience across all John Snow Labs products. The same license key can be moved to other products – Medical LLMs, Terminology Server, or can be used to experiment with the Healthcare or Visual libraries in Python, as long as it contains a sufficient number of credits.

![700image](/assets/images/annotation_lab/7.0.0/8.png)

## Dataset Sampling for Efficient Model Training
To enhance the training process for **NER (Named Entity Recognition)** projects this version introduces data sampling. In the past, training models on extensive datasets could lead to lengthy training periods or even failures due to the limitations of the existing infrastructure.
This update introduces a new feature that allows users to specify a sampling fraction in the training configuration page, enabling controlled dataset selection. A new parameter has been added to the Training page called Sampling Fraction, where users can specify the portion of the dataset they wish to use for training. The system automatically applies this setting, using only the specified fraction of the dataset for training, thereby optimizing the training process and improving overall efficiency.

For example, if there are 500 tasks in total and the user sets the sampling fraction to 0.5, the system will randomly select 250 tasks (50% of the dataset) for training instead of using the entire dataset.

This enhancement eliminates the need for manual dataset selection, as training can now be initiated based on a randomized subset, optimizing efficiency and resource utilization.

![700image](/assets/images/annotation_lab/7.0.0/9.png)

### Improvements

### Bulk Hide Labels Post-Annotation

Users can now hide multiple labels at once, significantly improving efficiency when working with large documents. Previously, labels had to be hidden individually, making the process tedious and time-consuming. With this update, an eye icon has been added to the Annotations widget, enabling users to hide all annotations for a given Label with a single click. To use this feature, users must switch from Region View to Labels View in the annotation widget.

With this improvement, users can manage labels more effectively, reducing manual effort and enhancing focus during the annotation process.

![700image](/assets/images/annotation_lab/7.0.0/10.gif)

### Improved Zoom Controls
Zooming in Visual NER projects is now more intuitive and controlled:
- Prevents excessive zoom-out, which previously caused annotation regions to overlap or disappear from view. This restriction ensures annotations remain visible and usable during review and editing.
- Restricts zoom-in to avoid unnecessary magnification into white space or low-content areas, which often led to loss of context or inefficient navigation.
- Improved positional control allows annotators to adjust the viewport while zoomed in or out, enabling smoother transitions and more precise annotation without losing sight of the surrounding content.  

![700image](/assets/images/annotation_lab/7.0.0/11.gif)

### Bug Fixes

- **Tooltip for Section Names Now Supports Multi-Row Display**

	Previously, tooltips for Section Names displayed text in a single row, making long sentences difficult to read and causing words to disappear. This fix enables multi-row tooltips, ensuring better readability and text visibility.  

- **'Show Labels Inside Region' Now Works Correctly in NER Projects**

	The 'Show Labels Inside Region' setting on the labeling page was not functioning in NER Projects. With this fix, labels now properly show or hide based on the setting, improving task visibility and usability.  

- **Removed Unnecessary "check_pre_annotation_status" Logs**

	Unnecessary `check_pre_annotation_status` logs were generated in the AnnotationLab pod each time users navigated to the task page, cluttering the logs. This fix eliminates redundant log entries, ensuring cleaner and more efficient logging.  

- **Assertion Training Now Works for Side-by-Side Projects**

	Assertion training previously failed in Side-by-Side project types, disrupting the training process. This issue has been resolved, ensuring a seamless training experience.  

- **Tasks Now Load Correctly in SBA-Enabled Projects**

	Users encountered a "Something Went Wrong" error when trying to view tasks in SBA-enabled projects. This issue has been fixed, allowing users to open, view, and annotate tasks without any errors.  

- **Fixed Annotation Mismatches in Visual NER and Side-by-Side Projects**

	Switching between completions in Visual NER Projects caused annotation inconsistencies. This issue, also present in Side-by-Side Projects, has been resolved to maintain annotation consistency across completions.  

- **Templatic Augmentation Task Generation Now Works Without Errors**

	Users faced errors when generating tasks via Templatic Augmentation, preventing the creation of augmented tasks. This issue has been fixed, and augmented task generation now works as expected.  

- **Corrected Side-by-Side Annotation Alignment for Image and Text**

	Annotations were misaligned when comparing images and text in Side-by-Side comparisons, leading to discrepancies. This fix ensures correct annotation alignment across both modalities, improving annotation accuracy.  

- **Invalid Hotkeys No Longer Trigger "Something Went Wrong" Page**

	Pressing an incorrect hotkey in Image and Text Side-by-Side Projects previously redirected users to a "Something Went Wrong" page. Now, invalid hotkeys simply have no effect, preventing unnecessary disruptions.  

- **Fixed "Completion Not Found" Error When Navigating Pages**

	Users encountered a "Completion Not Found" error when switching pages in Image and Text Side-by-Side Projects. This issue has been fixed, allowing seamless navigation without errors.  

- **Playground Now Opens Properly from Cluster Page**

	Users were unable to access the Playground from the Cluster Page due to a launch issue. This has been fixed, and the Playground now opens in a new window as intended.  

- **Prevented Duplicate Model Names in Local Models Page**

	Users could rename trained models with existing names on the Local Models Page, causing duplicate entries. This fix enforces unique names for each model, preventing naming conflicts.  

- **Deleted Chunks No Longer Reappear When Selecting a Label**

	Previously deleted chunks were unintentionally reannotated when selecting a label, causing unwanted label restoration. This issue has been resolved, ensuring deleted chunks remain removed unless explicitly re-added.  

- **'Keep Label Selected' Setting Now Works as Expected**

	The ‘Keep Label Selected After Creating a Region’ setting remained active even when disabled. This has been corrected, ensuring label selection behavior follows user preferences accurately.  


## Versions

</div>

<ul class="pagination owl-carousel pagination_big">
    <li class="active"><a href="annotation_labs_releases/release_notes_7_0_0">7.0.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_11_3">6.11.3</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_11_2">6.11.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_11_1">6.11.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_11_0">6.11.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_10_1">6.10.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_10_0">6.10.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_9_1">6.9.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_9_0">6.9.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_8_1">6.8.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_8_0">6.8.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_7_2">6.7.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_7_0">6.7.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_6_0">6.6.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_5_1">6.5.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_5_0">6.5.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_4_1">6.4.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_4_0">6.4.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_3_2">6.3.2</a></li> 
    <li><a href="annotation_labs_releases/release_notes_6_3_0">6.3.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_2_1">6.2.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_2_0">6.2.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_1_2">6.1.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_1_1">6.1.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_1_0">6.1.0</a></li>
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
</ul>