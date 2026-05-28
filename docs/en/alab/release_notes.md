---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Release Notes
permalink: /docs/en/alab/release_notes
key: docs-training
modify_date: "2026-05-27"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">


## Generative AI Lab 8.1.1

### Bug Fixes

- **Completion Submission Errors in PDF with Text Projects**

   Completion submission could fail in PDF with Text projects, preventing users from successfully submitting annotation results. Submission workflows have been corrected and verified across PDF with Text Annotation, Visual NER, and Side-by-Side project types.

- **Synthetic Task ADHOC Validation API Compatibility with Custom LLMs**

   The Synthetic Task ADHOC validation API was not fully aligned with the updated Custom LLM integration architecture, which could result in validation inconsistencies. Validation workflows have been updated to support the latest Custom LLM configuration behavior.

- **Unable to Upload Authentication Scripts for Custom LLM Providers**

   Authentication script uploads could fail during Custom LLM configuration, preventing integrations that require custom authentication logic. Script upload, validation, and Custom LLM authentication workflows now function correctly.

- **Bulk Delete Not Working with "Delete All Occurrences"**

   The "Delete All Occurrences" option on the labeling page could fail to remove all matching annotations after entity deletion. Bulk deletion workflows have been corrected and now remove all matching occurrences as expected.

- **IAA Percentage Charts Exceeding Expected Scale**

   Percentage-based Inter-Annotator Agreement charts could display values outside the expected percentage range. Chart scaling has been corrected, and percentage charts now use a maximum value of 100%.

- **Incorrect Anthropic Base URL During Configuration**

   Selecting Anthropic as an LLM provider could incorrectly populate the OpenAI base URL, causing confusion during provider setup. Provider-specific endpoint handling has been corrected, and URLs now update dynamically based on the selected provider.

- **SageMaker Integration Issues**

   Certain SageMaker integrations could fail during synthetic task generation and LLM evaluation workflows. SageMaker provider support has been corrected and validated across supported project types.

- **Custom LLM Authentication Script Access Permissions**

   Permission restrictions could prevent Custom LLM integrations from accessing required authentication script resources. Access controls have been updated to support authentication-script-based integrations.

- **Progress Chart Handling for Incomplete Tasks**

   Progress chart behavior has been aligned with assignment workflows. Incomplete task counts are now displayed according to task assignment status, ensuring consistent reporting across analytics dashboards.

---
## Versions

</div>

<ul class="pagination owl-carousel pagination_big">
    <li class="active"><a href="annotation_labs_releases/release_notes_8_1_1">8.1.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_8_1_0">8.1.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_8_0_0">8.0.1</a></li>
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