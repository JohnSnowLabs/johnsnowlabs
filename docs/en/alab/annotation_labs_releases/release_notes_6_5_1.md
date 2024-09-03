---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab Release Notes 6.4.1
permalink: /docs/en/alab/annotation_labs_releases/release_notes_6_5_1
key: docs-licensed-release-notes
modify_date: 2024-06-21
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 6.5.1

Release date: **09-03-2024**

### Improvements
- In Visual NER annotation, when a chunk is selected without a label and saved, the selection indication should be removed
- Improvements on Template Augmentation

### Bug Fixes
- The test status should be "pending" when the model-test server is in the pending state
- XML Validation Fails When a User Removes a Model Linked to Tasks with Labels/Choices from the Removed Model in Multi-Model Configuration
- "Show submit button" is not working as expected for the textarea
- The API "api/test_suite/test_suite_config" is called twice while creating a new test suite
- DB Session Rollback error on pod logs
- Rename "Template Augmentation" to "Templatic Augmentation"
- Relations cannot be added without NER Labels during Project Configuration
- Project Configuration error when new project is created 
- Error "list index out of range" is seen in the new project's configuration 


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}
