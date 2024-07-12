---
layout: docs
header: true
seotitle: NLP Lab | John Snow Labs
title: NLP Lab Release Notes 5.1.1
permalink: /docs/en/alab/annotation_labs_releases/release_notes_5_1_1
key: docs-licensed-release-notes
modify_date: 2023-07-10
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 5.1.1

Release date: **10-07-2023**

We are pleased to announce the release of v5.1.1 which includes the following Section Based Annotation bug fixes:

- Relevant sections are now listed in the "export JSON" task for Section Based Annotation enabled projects.
- Section based annotation enabled visual NER projects now support import of annotated tasks. The imported tasks are split on the basis of the rules and relevant sections are captured.
- The side menu options will now show a hover state only when they are clickable.
- Error messages will now be shown when invalid section rules for "Section Index" are entered.
- Section Index now supports Index with single value (1, 2, 3, ...) and series index (1-5) in the same rule.
- Manually created relevant sections of a deleted completion were still visible for section based tasks. This issue has been fixed.
- In the previous version, when a model was trained in a Visual NER project, the trained model did not have any prediction labels. This issue has been fixed.

</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}