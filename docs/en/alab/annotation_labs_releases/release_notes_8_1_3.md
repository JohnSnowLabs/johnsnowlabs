---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 8.1.3
permalink: /docs/en/alab/annotation_labs_releases/release_notes_8_1_3
key: docs-licensed-release-notes
modify_date: 2026-06-10
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">



## Bug Fixes

- **Cloud Task Import Failure from AWS S3**

   Task imports from cloud storage could fail when importing files from supported AWS S3 locations, preventing tasks from being created successfully despite valid import sources.
   Cloud import handling has been corrected, and tasks can now be imported successfully from configured AWS S3 paths.

- **Internal Server Error While Viewing Logs from Cluster Page**

   Viewing server logs from the Cluster page could trigger an Internal Server Error, preventing users from accessing deployment and troubleshooting information.
   Log retrieval and display functionality has been corrected, and users can now view Cluster page logs successfully without errors.

---
## Versions

</div>

{%- include docs-annotation-pagination.html -%}