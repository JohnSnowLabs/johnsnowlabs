---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 8.2.1
permalink: /docs/en/alab/annotation_labs_releases/release_notes_8_2_1
key: docs-licensed-release-notes
modify_date: 2026-07-14
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">



## Bug Fixes

- **Terminology Server Deployment Stability**

  Deploying a Terminology Server after an existing Healthcare model could result in orphaned server deployments. Server lifecycle management has been corrected to ensure Healthcare and Terminology Server deployments are associated and managed correctly.

- **Connected Word Selection in Visual NER**

  Selecting previously created connected words in Visual NER projects could redirect users to the "Something Went Wrong" page, interrupting annotation workflows. Connected word selection now functions correctly, allowing annotations to be reviewed and edited without errors.

- **Request Center Notification Reliability**

  Request Center notifications could behave inconsistently across supported workflows. Notification handling has been improved to ensure requests and related updates are displayed reliably.

- **Medical Terminology Lookup Positioning**

  The Medical Terminology lookup dropdown could appear in the incorrect location instead of next to the selected annotation. Dropdown positioning has been corrected, providing a more consistent annotation experience.

- **Reuse Resource Rule Visibility**

  The Reuse Resource page displayed only the first 15 available rules, preventing users from accessing larger rule collections. Rule listing has been updated so all available rules are displayed correctly.

---
## Versions

</div>

{%- include docs-annotation-pagination.html -%}