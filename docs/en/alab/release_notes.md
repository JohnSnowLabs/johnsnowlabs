---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Release Notes
permalink: /docs/en/alab/release_notes
key: docs-training
modify_date: "2026-04-13"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">



## Generative AI Lab 8.0.1

### Bug Fixes

- **System Resources Not Displayed on Cluster Page for EKS Deployments**

   System resource metrics (CPU, memory, and storage) could appear as blank on the Cluster page in EKS deployments. Resource monitoring has been corrected, and metrics are now displayed accurately.


- **Project Managers with Annotator or Supervisor Role Cannot Edit Project Description When Project Creation Is Disabled**

   When project creation was disabled in settings, users with Annotator or Supervisor roles were unable to edit the project description, even if assigned as Project Managers. This restriction has been removed, and project description editing is now correctly permitted based on project-level permissions.


- **Pre-Annotation Failure for `assertion_bert_classification_jsl`**

   Pre-annotation could fail when using the `assertion_bert_classification_jsl` model due to inconsistencies between document and chunk alignment during processing. The pipeline handling has been corrected, and pre-annotation with this model now completes successfully.


---
## Versions

</div>

<ul class="pagination owl-carousel pagination_big">
    <li class="active"><a href="annotation_labs_releases/release_notes_8_0_1">8.0.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_8_0_0">8.0.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_8_2">7.8.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_8_1">7.8.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_8">7.8</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_7">7.7</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_5_1">7.6.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_5_1">7.5.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_5_0">7.5.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_3_3">7.4.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_3_3">7.3.3</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_3_1">7.3.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_3_0">7.3.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_2_2">7.2.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_2_1">7.2.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_2_0">7.2.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_1_0">7.1.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_0_1">7.0.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_0_0">7.0.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_11_3">6.11.3</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_11_2">6.11.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_11_1">6.11.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_11_0">6.11.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_10_1">6.10.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_10_0">6.10.0</a></li>
</ul>