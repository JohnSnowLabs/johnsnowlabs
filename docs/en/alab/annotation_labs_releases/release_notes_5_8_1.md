---
layout: docs
header: true
seotitle: NLP Lab | John Snow Labs
title: NLP Lab Release Notes 5.8.1
permalink: /docs/en/alab/annotation_labs_releases/release_notes_5_8_1
key: docs-licensed-release-notes
modify_date: 2023-12-12
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 5.8.1

Release date: **02-01-2024**

### Improvement
- Prediction of text should match in both NER project and Visual NER project when same NER model is used for Pre-annotation of same texts. 

### Bug Fixes
- Connected Words in Visual NER project are not consistent when pre-annotated using NER models
- Embeddings and models cannot be manually uploaded in NLP Lab
- RE prompt created with rules and entity cannot be tested in Playground
- Backup to S3 bucket and Azure blob is not working and giving error related to Azure blob
- Issue on deleting task through Swagger API


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}
