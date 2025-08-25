---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 7.3.1
permalink: /docs/en/alab/annotation_labs_releases/release_notes_7_3_1
key: docs-licensed-release-notes
modify_date: 2025-07-31
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">

## Generative AI Lab 7.3.1
<p style="text-align:center;">Release date: 07-31-2025</p>

This patch release brings important improvements to cloud project import workflows, enhanced session handling, and better control over import permissions to ensure a smoother, more secure experience.

## Bug Fixes & Improvements

- **Flexible Session Token Updates** You can now update the session token during cloud import without losing previously saved credentials—no need to re-enter everything from scratch.

- **Reliable Cloud Import & Export** Resolved an issue that prevented importing or exporting projects from cloud storage, restoring full functionality for remote workflows.

- **Complete API Visibility** Missing endpoints have been added back to the Swagger documentation, ensuring developers have full access to all available APIs.

- **Crash-Free Page Refresh** Addressed a crash that occurred when refreshing the import page with the local import feature disabled.

- **Enforced Import Restrictions** When local import is disabled, users are now fully restricted from uploading projects from local files, ensuring consistent access control.

- **Unblocked Cloud Import Flow** Fixed an issue where users were unable to import from cloud storage unless they checked the "Save Credential" box. Cloud import now works seamlessly without requiring that extra step.


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}