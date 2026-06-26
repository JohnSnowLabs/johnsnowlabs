---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 8.1.2
permalink: /docs/en/alab/annotation_labs_releases/release_notes_8_1_2
key: docs-licensed-release-notes
modify_date: 2026-06-04
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">



## Bug Fixes

- **Integration Page Error After Restore**

   The Integration page could return an Internal Server Error after restoring an instance to version 8.1.1, preventing users from accessing configured integrations.
   Backup and restore compatibility has been improved, and the Integration page now loads correctly after restore operations across supported versions.

- **LLM Integration Configuration & Validation Improvements**

   Several issues affecting LLM integration workflows have been resolved:

    - Editing an existing integrated LLM could redirect users to the “Something Went Wrong” page, preventing configuration updates.
    - Azure OpenAI integrations used overly restrictive api_base validation rules that could block valid endpoint configurations.
    - Authentication scripts could remain cached and be unintentionally included in validation and integration requests for unrelated LLM providers.

- **Synthetic Task ADHOC Interface Improvements**

   The Request and Response panels within Synthetic Task ADHOC workflows have been repositioned and optimized to provide additional workspace for reviewing and editing generated content.


---
## Versions

</div>

{%- include docs-annotation-pagination.html -%}