---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Release Notes
permalink: /docs/en/alab/release_notes
key: docs-training
modify_date: "2026-02-23"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">



## Generative AI Lab 7.8.1

### Improvements

- **Secure Elasticsearch Communication and S3 Log Backup**
  Elasticsearch jobs now use HTTPS for secure communication, and support has been added for backing up logs to Amazon S3 to improve durability, compliance, and disaster recovery readiness.

- **Improved Backup Lifecycle Management**
  Backup workflows have been enhanced to better handle large backup files and ensure reliable periodic cleanup of older backups, reducing the risk of timeouts and improving storage efficiency.

- **Kibana Support for Azure Marketplace and Air-Gapped Environments**
  Deployment workflows now support Kibana in Azure Marketplace and fully air-gapped environments, enabling operational visibility and compliance without requiring external connectivity.

- **Automated Post-Install Elasticsearch Configuration**
  Elasticsearch post-deployment configuration, including log retention and backup settings, is now applied automatically to ensure consistent setup immediately after installation or upgrade.

- **One-Line Enablement for Audit Logs**
  Audit logging can now be enabled during installation or upgrade using a single command, simplifying setup and reducing configuration overhead.

- **Installation Flag for Kibana Audit Enablement**
  A dedicated installation flag is now available to enable Kibana audit capabilities during deployment or upgrade, streamlining configuration for audit and monitoring workflows.


### Bug Fixes

- **S3 Task Import Not Creating Tasks**
  In certain scenarios, task imports from S3 could report success while no tasks were created. Import handling has been corrected to ensure tasks are properly created and that import status messages reflect actual results.

- **Annotations Becoming Invisible When Zooming in the Labeling Page**
  Previously, annotations could become invisible on the labeling page when zooming into visual documents. Annotation rendering has been corrected, and annotations now remain visible and intact across zoom levels.

- **External Provider Deletion Validation**
  In earlier versions, deleting an external provider could fail without indicating that associated projects or prompts were preventing deletion. Deletion behavior has been corrected to provide clear validation messaging when providers are linked to projects or prompts, and providers can now be deleted successfully once dependencies are removed.

- **Pipeline Tab Access for Annotator Role**
  Previously, users with the Annotator role could encounter permission-related issues when accessing the Pipeline tab on the Reuse Resource page. Access controls have been corrected, allowing annotators to view and interact with available pipelines without errors while maintaining proper role-based permissions across other user roles.

- **Move Tool Stability in Visual NER Documents**
  Inconsistent behavior could occur when using the move tool in Visual NER documents, particularly after extended interaction. The move functionality has been stabilized to ensure consistent navigation and positioning during document review.




---
## Versions

</div>

<ul class="pagination owl-carousel pagination_big">
    <li class="active"><a href="annotation_labs_releases/release_notes_7_8_1">7.8.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_8">7.8</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_7">7.7</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_5_1">7.6.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_5_1">7.5.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_5_0">7.5.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_3_3">7.4.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_3_3">7.3.3</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_3_1">7.3.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_3_0">7.3.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_2_2">7.2.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_2_1">7.2.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_2_0">7.2.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_1_0">7.1.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_0_1">7.0.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_0_0">7.0.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_11_3">6.11.3</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_11_2">6.11.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_11_1">6.11.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_11_0">6.11.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_10_1">6.10.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_6_10_0">6.10.0</a></li>
</ul>