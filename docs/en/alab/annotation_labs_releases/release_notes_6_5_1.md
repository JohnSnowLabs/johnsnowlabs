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
- In Visual NER annotation, the selection indication is now cleared when a chunk is selected without a label and then saved.
- Enhanced the user interface for the Templatic Augmentation option.

### Bug Fixes
- The test status will now correctly display as “pending” when the model-test server is in a pending state.
- Fixed an issue where XML validation would fail if a user removed a model linked to tasks with labels or choices in a multi-model configuration.
- Corrected the visibility behavior of the “Show submit button” feature for text areas; it now functions according to the configured settings.
- Resolved a DB session rollback error appearing in pod logs
- The “Template Augmentation” option has been renamed to “Templatic Augmentation.”
- Addressed a bug that prevented adding relations without NER labels during project configuration; relations can now be added in Visual NER projects.
- Fixed the “list index out of range” error that was occurring on the configuration page for newly created projects.


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}
