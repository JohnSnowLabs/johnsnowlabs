---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 8.0.1
permalink: /docs/en/alab/annotation_labs_releases/release_notes_8_0_1
key: docs-licensed-release-notes
modify_date: 2026-04-13
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">



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

{%- include docs-annotation-pagination.html -%}