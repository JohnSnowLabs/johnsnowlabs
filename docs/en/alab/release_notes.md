---
layout: docs
comment: no
header: true
seotitle: Release Notes | John Snow Labs
title: Release Notes
permalink: /docs/en/alab/release_notes
key: docs-training
modify_date: "2024-11-15"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## Easy Migration to Generative AI Lab - 6.8 
Generative AI Lab 6.8 introduces new features designed for users migrating from NLP Lab onto the newest version of Generative AI Lab. With the new Backup and Restore feature, you can transfer projects, annotated data, models, and configurations to the Generative AI Lab 6.8 and above. Simply back up your projects and resources to cloud storage services like Azure Blob or AWS S3, then restore them directly into the new environment, entirely through the user interface.

This release also introduces other small enhancements to existing features, including a “None” option in the de-identification dropdown, allowing you to label text without altering the original content. We’ve also added a helpful visual indicator for labels with associated annotation guidelines—now marked with a colored dot matching the label’s color. 

</div><div class="h3-box" markdown="1">

## Migrate your NLP Lab Backup to Generative AI Lab
Migration to the new version is now a seamless process. Users of the NLP Lab can transfer their models, projects, annotated data and configuration settings to the Generative AI Lab using our Backup and Restore feature. Once backed up, configurations can be easily restored to a Generative AI Lab server. To migrate your data, the process is as follows:

### Steps to Backup Data from NLP Lab
1. **Login** to your current NLP Lab deployment as the admin user.
2. Go to the **`System Settings`** page.
3. Navigate to the **`Backup`** tab.
4. Enter the required **backup details**.
5. Schedule an immediate backup using the **`Backup now`** feature.
6. Monitor the **backup pod status** to ensure the process completes successfully.
```bash
kubectl get pods
```
**Verify Backup:** Upon completion, your backed-up database and files will be visible in cloud storage.

<iframe width="800" height="450" src="https://www.youtube.com/embed/wUiDq5peZK4?si=v2Q6XCtK01KmcKJa&hd=1" title="NLP Lab to Generative AI Lab migration - Step 1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Steps to Restore Data

1. **Deploy** a fresh instance of Generative AI Lab version 6.8.0 or higher from the marketplace.
2. **Login** to the UI as the admin user.
3. Go to the **`System Settings`** page.
4. Click on the **`Restore`** tab and fill in the necessary details.
5. Click on **`Restore Now`** to initiate the process.
6. Monitor the **restore pod status** to ensure successful completion.
```bash
kubectl get pods
```

**Verify Restoration:** Access the UI, all projects, models, data and files should now be successfully restored.

<iframe width="800" height="450" src="https://www.youtube.com/embed/8JihFXLfHGc?si=hczRk74snB9cP8Es&hd=1" title="NLP Lab to Generative AI Lab migration - Step 2" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

</div><div class="h3-box" markdown="1">

## Improvements
### Exclude Labels from De-identification 
Generative AI Lab 6.8 introduces a  `None**` option in the de-identification selection dropdown. When selected, this option will only label the text without performing any de-identification. This provides users with greater flexibility by allowing them to annotate the text while leaving the original content intact. 

![680image](/assets/images/annotation_lab/6.8.0/3.png)

### Mark the labels with annotation guideline
A new enhancement has been introduced to easily distinguish labels with annotation guidelines. Labels that have associated annotation guidelines are now marked with a colored dot at the top-right corner. This feature applies to both NER and VisualNER projects. If the annotation guidelines are deleted for a label, the dot will be automatically removed.

![680image](/assets/images/annotation_lab/6.8.0/4.png)

### Change the pop-up message when the model downloading is canceled
The pop-up message that appears when a model download is canceled has been updated for better clarity. Previously, the message displayed the title `Warning: Delete Model?`, which could confuse. It has now been changed to `Warning: Cancel Model Download?` with a more accurate description. This update provides clearer communication to users when they choose to stop a model download in progress, improving the overall user experience.

![680image](/assets/images/annotation_lab/6.8.0/5.png)

### Improvements in XML editor
The issue of overlapping parent option buttons and top child option buttons when hovered, specifically when the `Show parent action buttons on hover` option was enabled, has been resolved. This fix provides a more polished user experience by ensuring the buttons are properly aligned. Now, the buttons no longer interfere with each other, offering smoother interaction with the interface.

![680image](/assets/images/annotation_lab/6.8.0/6.png)

Tooltips have been enhanced to display the correct tag name for each section, improving the usability of the XML editor. Previously, the tooltip and the menu name that appeared on hover were identical for each container, making it difficult to distinguish between them. With this update, each container now has a unique tooltip, ensuring that users can easily identify where they clicked. For example, `Edit Tag` has been updated to `Edit Text Tag` to provide clearer context and improve navigation within the editor.

![680image](/assets/images/annotation_lab/6.8.0/7.gif)

A validation error is now triggered when quick filters are incorrectly attached to elements other than labels or ellipse labels.

![680image](/assets/images/annotation_lab/6.8.0/8.png)

The `Maximum rating value` of the `Rating` element now includes validation. A red color warning is displayed when an invalid value is entered. Only positive numbers are allowed, ensuring that users input appropriate values and improving the overall accuracy of ratings.

![680image](/assets/images/annotation_lab/6.8.0/9.png)

### Increased readability for test cases view
 
Users can now read the test cases better with two-tone text distinguished between test types.

![680image](/assets/images/annotation_lab/6.8.0/10.png)

### Bug Fixes
- **Annotation guidelines now visible in the horizontal layout**
  
Users can now see Annotation guidelines in the horizontal layout.

![680image](/assets/images/annotation_lab/6.8.0/11.png)

- **Confidence score of classifier is only shown for the first section in SBA text task**
  
 The confidence score is now correctly displayed for predictions across all sections, ensuring consistent feedback throughout the entire task.

![680image](/assets/images/annotation_lab/6.8.0/12.gif)

- **Toast Message-warning users of Expiring License with each API call**
  
    The issue with frequent toast message pop-ups has been largely resolved. However, the message may still reappear when the user refreshes the page or navigates to different sections. While the message is now less intrusive, it is still visible during certain actions such as page reloads or navigation.

- **File Backup is uploaded to the DB file backup path**
  
    Users can now successfully designate different paths for ad-hoc backing up databases and files. The system will correctly store database ad-hoc backups in the specified database path, while file ad-hoc backups will be saved in their intended separate location.
    
</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

<ul class="pagination owl-carousel pagination_big">
    <li class="active"><a href="annotation_labs_releases/release_notes_6_8_0">6.8.0</a></li>
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