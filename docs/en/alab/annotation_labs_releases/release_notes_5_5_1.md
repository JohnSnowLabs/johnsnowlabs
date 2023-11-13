---
layout: docs
header: true
seotitle: NLP Lab | John Snow Labs
title: NLP Lab Release Notes 5.5.1
permalink: /docs/en/alab/annotation_labs_releases/release_notes_5_5_1
key: docs-licensed-release-notes
modify_date: 2023-11-13
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 5.5.1

Release date: **10-13-2023**

We are delighted to announce release of NLP Lab 5.5.1
 
### Additional Meta Data on NER Label
 
In an NER project, users have the capability to include multiple pieces of metadata for each extraction. While annotating a text document, users can now incorporate metadata in either the "String" or "Key Value" format. It is now possible to attach multiple entries of metadata to a single label during the annotation process.

 ![metadata](/assets/images/annotation_lab/5.5.0/111.png)

 
### Bug Fixes:
- Eliminated the occurrence of multiple entries of the same model in the models.json file across all containers (annotation, training, pre-annotation).
- Addressed a problem where deploying a free rule in the playground and performing pre-annotation resulted in a server crash.
- Resolved the issue where the "Remove Duplicates" button is now accessible exclusively to users with the role of "Annotator."

</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}