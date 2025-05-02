---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 7.0.1
permalink: /docs/en/alab/annotation_labs_releases/release_notes_7_0_1
key: docs-licensed-release-notes
modify_date: 2025-04-09
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 7.0.1

This release addresses several key issues related to annotation workflows and server responsiveness. The following bugs have been resolved:

- **LLM Comparion Template**
We’ve added a new template under both Text and HTML types that lets you easily compare responses from multiple LLMs side by side — perfect for faster and clearer model evaluation.


- **Incorrect Annotation Placement in NER Annotation**
Fixed an issue where NER annotations were being placed incorrectly on the text, ensuring accurate and consistent label positioning.

- **Delay While Loading Servers in Cluster Page and Import Task Page**
Resolved performance delays occurring when OCR servers were already deployed and ready. Server lists now load promptly across relevant pages.

- **Unable to Add Key-Value Metadata to NER Labels**
Fixed a bug preventing users from adding custom metadata to NER labels. Users can now seamlessly assign key-value metadata to improve label context and utility.

- **License with Scope app:GenerativeAI Not Supported**
Fixed an issue where licenses with the scope app:GenerativeAI were not recognized. Such licenses are now correctly processed and validated.

- **Incorrect Floating License Scope Information Displayed**
Resolved a display bug where incorrect scope details were shown for floating licenses. Scope information is now accurately presented to users.

**HCC Bug Fixes**
- Fixed issue where task ranking was not included during export in HCC projects.
- Resolved bug causing HCC codes to be hidden in the annotation section despite being mapped and visible in tasks.
- Addressed issue where the lookup code was not selected by default in the dataset list.
- Ensured consistent state of labels in the annotation section when selected in HCC projects.
- Fixed a UI crash that occurred when users clicked on predicted labels for prediction completions in HCC projects.
- Resolved error preventing resolvers from being added to HCC project entities due to domain mismatch.
- Enabled usage of the ICD10 resolver model mpnetresolve_icd10_cms_hcc_2024_midyear in HCC projects.

</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}