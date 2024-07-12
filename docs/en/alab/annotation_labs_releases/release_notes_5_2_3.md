---
layout: docs
header: true
seotitle: NLP Lab | John Snow Labs
title: NLP Lab Release Notes 5.2.3
permalink: /docs/en/alab/annotation_labs_releases/release_notes_5_2_3
key: docs-licensed-release-notes
modify_date: 2023-08-10
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 5.2.3

Release date: **10-08-2023**

We are pleased to announce the release of v5.2.3 which includes the following bug fixes:

- Text Generation Error Removal: Resolved an issue where there was no option to remove text generations with errors from the Result section.	
- CSV Download Retry: Fixed the problem with CSV download for generated tasks, which was failing on the first attempt after correcting an invalid secret key.	
- Exported Failed Tasks: Addressed the problem where failed generated tasks were being exported as blank tasks in the CSV file. These blank tasks could also be imported, which has been rectified.
- Unauthorized Page Navigation: Users were encountering an "Unauthorized" page when attempting to navigate to the configuration page. This issue has been resolved, and users can now access the configuration page without any problem.
- Scheduled Synthetic Dag: The generation of synthetic Dags was erroneously scheduled even if the feature was disabled. This behavior has been fixed, and synthetic Dags will now respect the disabled setting.	
- Ad-hoc Task Generation: Corrected the issue where ad-hoc synthetic tasks were not being generated for projects with long names.	
- UI Crash on History Button Click: Resolved a production UI crash that occurred when users clicked on the History button on the train page when the trained failed due to max server count.	
- Firefox Compatibility: Fixed the problem where importing generated tasks was not functioning correctly in the Firefox browser.	
- Visual NER Project Export: Fixed a 500 Error that was preventing the export of tagged Visual NER tasks.


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}