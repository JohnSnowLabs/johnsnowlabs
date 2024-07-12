---
layout: docs
header: true
seotitle: NLP Lab | John Snow Labs
title: NLP Lab Release Notes 5.6.1
permalink: /docs/en/alab/annotation_labs_releases/release_notes_5_6_1
key: docs-licensed-release-notes
modify_date: 2023-12-05
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 5.6.1

Release date: **05-12-2023**

### Improvement
- Now in Compact View, the Task ID and pre-annotation statuses are show as in default task view
- The Show Meta in Regions is disabled by default for new projects
- Updated Icons for tools in the Labeling page

### Bug Fixes
- Fixed issue regarding creations of sections according to the users need in text project.
- "Only Ground Truth" filter exports tasks with only predictions without any ground truth completions.
- "Preview Window" is stuck on loading when switching between different project "Content types"
- When "label all occurrence is enabled", Label and Region selection parameters in annotation settings are ignored.
- User must select a model in order to save project configuration in Reuse Resource page
- Visual NER pre-annotation does not recognize numbers
- Prompts/Rules disappear when adding or viewing them from re-use resources page (Only on the UI)
- Error in Reuse Resource page when user navigates to the page after submitting the task
- When comment is added to a task, the page crashes with "Something went wrong"

</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}
