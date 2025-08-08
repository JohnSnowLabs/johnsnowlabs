---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 7.0.1
permalink: /docs/en/alab/annotation_labs_releases/release_notes_7_2_1
key: docs-licensed-release-notes
modify_date: 2025-04-09
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 7.2.1

<p style="text-align:center;">Release date: 07-01-2025</p>

### Improvements
- Added re-initialization logic for the application license to handle validation failures gracefully, ensuring smoother application startup and reliability.
 
### Bug Fixes
- Fixed an issue where elements added from the Customize Label Page were only applied to the first response in LLM Evaluation Comparison Projects.
- Resolved a bug where the first Adhoc LLM Provider was not visible when added to LLM Evaluation Comparison Project Types.
- Added missing pagination to the task list view in both LLM Evaluation and LLM Evaluation Comparison Projects.
- Fixed an issue where analytics were not populated for LLM Evaluation Projects configured with Adhoc External Service Providers.
- Fixed UI inconsistencies for SageMaker credentials – added show/hide logic and enabled saving without a session token.
- Addressed discrepancies in input fields during SageMaker external provider integration.
 
### Tasks
- Updated LLM Evaluation Analytics to only include ground truth (GT) when "No Choice Selected" is configured.
- Minor improvements and optimizations in the SageMaker integration flow.

</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}