---
layout: docs
header: true
seotitle: NLP Lab | John Snow Labs
title: NLP Lab Release Notes 5.7.1
permalink: /docs/en/alab/annotation_labs_releases/release_notes_5_7_1
key: docs-licensed-release-notes
modify_date: 2023-12-12
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 5.7.1

Release date: **12-27-2023**

### Improvement
- Dynamic Task Pagination: Validation message to be shown when the character/page count exceeds the system limit

### Bug Fixes
- Compact View: While making quick submissions, the last made submission is not always the final starred completion.
- Compact View: "Classify in Place" turns off at times automatically when moving to any other page
- Compact View: Clicking the same multi-select Classification option multiple times submits a blank submission with a 500 Error
- Compact View: Using the "Focus on one classifier" settings malfunctions at times
- Compact View: For single classifier project the options are listed in single row
- Compact View: Using the "Focus on one classifier" settings malfunctions at times
- Filter pre-annotations according to my latest completion
- The "Eye" Icon placement is dependent on the annotated Text width 
- Undo/Redo/Reset buttons does not work for manually created sections
- Compact View settings is still available (but won't apply) even when the classifications models are removed from the project
- PDF cannot be imported to Rate PDF project
- When trying to perform annotations on image task with SBA, the page crashes
- Exception is seen when exporting project
- No tasks are listed when user navigates from other pages to task page with compact view is enabled
- Visual NER models added to Visual NER Project Config is added in a separate <RectangleLabels> tags with wrong attributes
- Task import in NER project is failing and giving can't upload file on server side error


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}
