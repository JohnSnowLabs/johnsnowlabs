---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab Release Notes 6.10.0
permalink: /docs/en/alab/annotation_labs_releases/release_notes_6_10_0
key: docs-licensed-release-notes
modify_date: 2024-08-25
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 6.10.0

Release date: **01-13-2025**

## Generative AI Lab 6.10.0: Faster Preannotation along with De-identification, and Improved Non-Overlapping Relations
Generative AI Lab 6.10 brings an update that makes marked improvements to the speed of our Pre-annotation function, and De-identification projects. Additionally, we’ve made usability improvements to relation visualizations, allowing for a clearer view of projects. 

Additional features include the ability to use annotation guidelines in HTML projects, a UI improvement to the analytics request page, and other small improvements. 

## Enhanced NER Pre-annotation and De-identification
Version 6.10.0 focused on an upgrade to the Pre-annotation and De-identification processes, combining speed, efficiency, and reliability. Pre-annotation processes have been fine-tuned, dramatically reducing processing time. De-identification workflows now leverage advanced pipelines for faster and more accurate results.

Redesigning our workflow for these processes allows for an increase in performance of up to **3x**. Our benchmark data showed consistently that for datasets that were routinely being pre-annotated at a rate of 300 tasks per hour, we are now able to pre-annotate at a rate of 1100 tasks per hour. This was a necessary feature to support our customers who rely on this feature for their teams of annotators.

Users can seamlessly transition to this version without requiring additional training or adjustments to their workflow.

## Improved Non-Overlapping Relations
In earlier versions, when multiple relations were defined between text chunks positioned close to each other, the arrows and labels representing these relations would often overlap. This overlap created visual clutter, making it difficult for users to accurately distinguish and interpret the relations.

**Before:**
![6100image](/assets/images/annotation_lab/6.10.0/1.png)

The display logic for relation lines has been refined to prevent overlapping. Relation arrows and labels are now strategically spaced and arranged into tiers based on the number of overlaps for each line, providing a clean and organized visual presentation. This improvement significantly enhances readability and reduces confusion when analyzing complex relationships between text chunks.

**After:**
![6100image](/assets/images/annotation_lab/6.10.0/2.png)

The improved relation visualization feature, "**Accommodate Relation Overlap**" is now enabled by default, though it can be disabled for instances where overlapping of many relationships makes the text difficult to read. The goal of this feature is to decrease ambiguity in relations.

![6100image](/assets/images/annotation_lab/6.10.0/3.png)

## Improvements
### Highlighted Model Versioning Option

The model versioning option is now highlighted in the training page, to avoid confusion and promote the use of this pivotal feature.

![6100image](/assets/images/annotation_lab/6.10.0/4.png)

### Redesigned Analytics Permission Request Page
To enhance user experience and clarity, the Analytics Dashboard activation process has been updated with the following improvements:

When navigating to the **Analytics** page for a project where the dashboard is not enabled, users are presented with:
- Two buttons: “**Go Back**” and “**Send Request**”
- A clear informational message:
"**Analytics Dashboard Not Enabled for This Project**
`Request the Generative AI Lab administrator to enable the Analytics Dashboard for this project.`"

![6100image](/assets/images/annotation_lab/6.10.0/5.png)

Upon clicking the “**Send Request**” button, the message updates to:

"**Analytics Dashboard Request Sent.**
`Once the request is approved by the admin, the dashboard will be available for use.`".

Also, the “**Send Request**” button becomes disabled, preventing duplicate submissions.

![6100image](/assets/images/annotation_lab/6.10.0/6.png)

When the “**Go Back**” button is clicked, users are redirected to the previous page allowing them to continue with other tasks while awaiting approval for the Analytics Dashboard or without submitting a request. These updates deliver a clean UI for users to request dashboard access, ensuring clarity and transparency in the activation process.

### Highlight Drafts on Annotation page 
As part of our continuous efforts to improve the user experience, the Completions section has been updated to ensure consistent capitalization throughout the interface. Additionally, the text color for these messages has been changed to orange to enhance visibility and emphasis.

Message in the Completion Tab When a Draft Is Saved:
![6100image](/assets/images/annotation_lab/6.10.0/7.png)>

Message in the Completion Tab When Viewing the Last Saved Annotation:
![6100image](/assets/images/annotation_lab/6.10.0/8.png)

### Bug Fixes

- **De-identification not working in Section Based Annotation-enabled project**

  Section-based annotation filters tasks by relevant sections. When such tasks are pre-annotated using models and then de-identified, the de-identified text was previously not visible in these sections, as shown in the comparison screenshot below. This issue has now been resolved, and users can view the de-identified text by clicking the **Compare De-identified Data** button and then be exported as needed.
  
  **Before:**
  ![6100image](/assets/images/annotation_lab/6.10.0/9.png)

  **After:**
  ![6100image](/assets/images/annotation_lab/6.10.0/10.png)>

- **Model Publishing Fails with Error**

  Users can once again publish their models to the models hub.
  
- **Users attempting External Prompts in Visual NER projects**

  Visual NER Projects now have validation to prevent relation prompts and external prompts from being attempted, as this feature is not currently available.

- **Users can combine Visual NER model with Rules during project configuration**

  Rules are not supported for Visual NER projects, so a validation error is now displayed when users attempt to add rules alongside a Visual NER model.

- **"Define What to Annotate" tab is hidden if the user tries to add/remove the External Classification Prompt**

  The issue has been resolved now and users can no longer add classification prompts to the visual project hence the behaviour will no longer be an issue.


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}