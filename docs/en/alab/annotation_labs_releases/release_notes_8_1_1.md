---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 8.1.1
permalink: /docs/en/alab/annotation_labs_releases/release_notes_8_1_1
key: docs-licensed-release-notes
modify_date: 2026-05-27
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">



## Bug Fixes

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

{%- include docs-annotation-pagination.html -%}