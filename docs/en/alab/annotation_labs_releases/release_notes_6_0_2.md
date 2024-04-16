---
layout: docs
header: true
seotitle: NLP Lab | John Snow Labs
title: NLP Lab Release Notes 6.0.2
permalink: /docs/en/alab/annotation_labs_releases/release_notes_6_0_2
key: docs-licensed-release-notes
modify_date: 2024-04-11
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 6.0.2

Release date: **04-16-2024**

### Improvements
- Fixed inconsistency in the behavior of Next and Previous Button tasks
- "Continuous Server Usage" warning is only shown when idle servers are present on the cluster page

### Bug Fixes
- List of Lookup codes pop-up is not visible when the user opens the pop-up from the bottom of the labeling page
- Embeddings parameter can be changed after selecting model in Transfer learning dropdown
- When transfer learning is selected, the user should not be able to change the automatically selected license and embedding parameters
- Large annotated chunks are separated in UI based on previously selected chunks
- PayG license is not listed in the License import popup list
- Restored Airgap and Floating Licenses from non-AMI instance are Working in 600 AMI
- Label Names are lost when saving/updating completions if "Show Meta in regions" is enabled


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}
