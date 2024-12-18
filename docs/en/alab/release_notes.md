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

## Model Versioning during Training and Visual Model Updates in 6.9.0
Generative AI Lab version 6.9.0, introduces new features designed to improve visual projects as well as model training. This release introduces model versioning as well as new project types, expanding the use cases for our product. With this update, you can streamline tasks such as checkbox identification, handwritten text detection, and model management.

Other small improvements have been made to Generative AI Lab including to the updater script, and ensuring the default colors on labels remain high contrast. 

## Model Versioning when Training Models
Generative AI Lab 6.9 introduces model versioning for the following project types: Named Entity Recognition (NER), Classification, Assertion, Relation, and Visual NER. In the **TRAINING SETTINGS** section of the **Train** page, a toggle labeled **Enable Versioning** is now available. By default, model versioning is disabled. To enable it, toggle **Enable Versioning** to **on**. 

![690image](/assets/images/annotation_lab/6.9.0/5.png)

When enabled, models are saved with versioned names following the format **projecttype_projectname_v1**, **projecttype_projectname_v2**, and so on. If model deployment is enabled after training is complete, the most recently trained model is automatically applied to the project configuration. If model deployment after training is not enabled, the project configuration remains unchanged. All versions of trained models are accessible on the Reuse Resource page, allowing users to browse and select specific model versions for reuse in other projects.

![690image](/assets/images/annotation_lab/6.9.0/6.png)

Model versioning is also supported for previously created projects. If versioning is disabled, subsequent training overwrites the most recent model without creating a new version. When re-enabled, versioning resumes from the latest version rather than starting over from v1. This feature simplifies model management by enabling version tracking and reusability, offering seamless integration for new and existing projects.

Note: The **Enable Versioning** toggle is disabled during training. 

## Identify and Validate Checkboxes with Precision
Version 6.9.0 introduces a new project type called **Checkbox Detection**. With the new update, users can now use the model offered by Generative AI Lab to identify checkboxes in the tasks, including the **checked** and **unchecked** status in the respective tasks.

This project type can be selected from the **Content Type** page under the **Image** tab during project setup. The default model associated with Checkbox Detection is automatically downloaded from the **Models Hub** page and added to the project configuration.

![690image](/assets/images/annotation_lab/6.9.0/1.png)

After the project is configured, users can add relevant tasks and leverage the model to detect checkboxes and their respective checked and unchecked statuses.

![690image](/assets/images/annotation_lab/6.9.0/2.png)

This new update integrates seamlessly with the existing workflow, ensuring no changes or disruptions to the current application processes.

This model can not currently be combined with other models.

## Detect and Validate Handwritten Text and Signatures
This update continues with the **Handwritten Text and Signature Detection** project type. This new feature enables the automatic identification and annotation of handwritten text and signatures within documents, using John Snow Lab's Visual NLP Library. The new project type can be selected from the **Content Type** page under **Image** tab during project configuration. Upon selection, the default model for Handwritten Text and Signature Detection is automatically downloaded from the **Models Hub** and integrated into the project configuration.

![690image](/assets/images/annotation_lab/6.9.0/3.png)

Users can then add relevant tasks to the project and use the model to identify and annotate handwritten content and signatures in documents efficiently.

![690image](/assets/images/annotation_lab/6.9.0/4.png)

This feature doesn't change the existing application workflow, and can not be combined with other models at this time.

## Improvements
### Enhanced label readability by using high-contrast default colors.
To improve readability and accessibility, randomly assigned colors will now meet a minimum contrast standard by default, ensuring they are easy to read. This new default simplifies the project creation experience.

![690image](/assets/images/annotation_lab/6.9.0/7.png)

### Improvements to the updater script
First, a retry mechanism has been implemented to pull images during updates and installations. Each image will now be attempted up to three times to ensure successful retrieval.

When training or pre-annotation servers are running during an upgrade, a prompt appears:
"**Do you want to proceed with deleting these pods? (y/N):**"

- If "**No**" is selected, the upgrade process is exited.
- If "**Yes**" is selected, the running training/pre-annotation pods are deleted, and the upgrade continues.
- If no matching training or pre-annotation pods are running, the message "**No preannotator/training pods matching criteria found.**" is displayed, and the upgrade proceeds.

A new "**silent**" flag can now be passed while executing the upgrade script. 

``./annotationlab-updater.sh --silent``

When "**silent**" flag is used:
- It automatically deletes running training/pre-annotation servers without prompting.
- It uses the default admin password for the upgrade procedure.

## Bug Fixes
- **Prediction results are missing in Section Based Classification Projects when exported tasks are re-imported** 

Previously, in Section-Based Classification projects, prediction results were missing when exported tasks were re-imported back to Generative AI Lab project. This issue has been resolved. Prediction results now remain intact when tasks are re-imported for SBA-enabled projects, ensuring data consistency.

- **Multiple API calls are made during pre-annotation on the task page**

 The **Task** page now operates efficiently without making multiple API calls or unexpected refreshes.

- **De-identify dialog box is not updated after the server is ready with the de-identification pipeline**

The De-Identification pop-up now auto-refreshes and appears as expected once the de-identification pipeline is ready for deployment.

- **Rule for section classifier is set to default value when the user navigates back to Relevant Page**

 For SBA-enabled projects, the selected classifier model is now correctly displayed in the dropdown when users return to the page for reconfiguration or confirmation.

- **Training status still showing as 'Running' when the user checks the training history after aborting the training**

The training history now accurately reflects the correct training status with the appropriate status color.

- **When de-identification pipeline is deployed glove_100 is shown as deployed embeddings**

In earlier versions, the default embedding glove_100 was incorrectly displayed as deployed when the de-identification pipeline was deployed, even if no embeddings were available. This issue has been resolved. The correct embedding is now displayed when an embedding is used. An empty embedding is shown when no embedding is used. This ensures an accurate representation of the deployed embeddings in the pipeline.

- **"Model type not available " error is seen frequently while navigating to the Train page**

Previously, users frequently encountered the "**Model type not available**" error when navigating to the **Train** page. This issue has been resolved, and the error no longer appears while accessing the **Train** page from different locations within the project.

- **Backup fails for Azure Blob Storage**

An issue affecting backups to Azure Blob Storage has been resolved. Backups now function correctly, ensuring reliable data storage and recovery.

- **Labels with instructions cannot be deleted and added from the project configuration**

We now allow users to seamlessly add labels with instructions or delete labels that contain instructions as needed.

- **Active learning is not triggered for the second trigger**

Active learning will now wait for the license to be free before triggering training, ensuring a smoother and more reliable process. Additionally, when the active learning condition is met and the system is waiting for the license, this status will be displayed on the training page.

## Versions

</div>

<ul class="pagination owl-carousel pagination_big">
    <li><a href="annotation_labs_releases/release_notes_6_9_1">6.9.1</a></li>
    <li class="active"><a href="annotation_labs_releases/release_notes_6_9_0">6.9.0</a></li>
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