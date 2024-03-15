---
layout: docs
header: true
seotitle: NLP Lab | John Snow Labs
title: NLP Lab Release Notes 5.8.1
permalink: /docs/en/alab/annotation_labs_releases/release_notes_5_9_1
key: docs-licensed-release-notes
modify_date: 2024-03-15
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 5.9.1

Release date: **03-15-2024**

### Improvement
- User should only be able to pair resolver with models of the same domain for pre-annotation

### Bug
- Firefox issue: CSV task import fails
- File with empty field is downloaded when, tasks without completions are exported as CSV
- Users that were created and assigned admin role cannot be deleted
- Generic error messsage "Invalid bucket file path" is seen while importing the valid unsupported file types and invalid bucket/blob files
- Adding an external prompt to a project doesn't automatically integrate the project with the external prompt after the first time
- Status of playground is displayed as 'Busy' in cluster page even if the playground server is in 'Pending' state
- Texts aren't labeled when testing external Prompts
- When multiple Lookup datasets are associated with different labels, the list shows "undefined" while trying to add the look up code to text during annotation.
- Lookup codes cannot be added for texts that span over multiple line
- When a label for a text is changed, then the new label is automatically assigned to next text that is selected.

</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}
