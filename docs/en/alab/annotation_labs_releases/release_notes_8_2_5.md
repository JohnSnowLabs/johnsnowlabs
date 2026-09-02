---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 8.2.5
permalink: /docs/en/alab/annotation_labs_releases/release_notes_8_2_5
key: docs-licensed-release-notes
modify_date: 2026-08-30
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">

**Generative AI Lab 8.2.5** is a maintenance release focused on annotation reliability, DICOM usability, backup and restore stability, and deployment infrastructure. This release also introduces Kubernetes scheduling support for managed pods and improves pod status monitoring.

## Improvements

### Taints and Tolerations Support for Managed Pods

**What's Improved**

Managed pods now support Kubernetes taints and tolerations, providing greater control over pod scheduling in environments with dedicated or restricted cluster nodes.
This enables administrators to align Generative AI Lab workloads with existing Kubernetes scheduling and infrastructure policies.

### Improved Pod Status Monitoring

**What's Improved**

Pod status monitoring has been updated to replace the previous HTTP polling loop, improving how the platform tracks the state and availability of deployed pods.

## Bug Fixes

- **Annotation Discrepancy in NER Projects**

  Annotations could behave inconsistently in NER projects, with some annotations not being created as expected during labeling. Annotation handling has been corrected to ensure entities are created accurately and consistently throughout NER annotation workflows.

- **Backup and Restore Failure**

  Restore operations could fail because kubectl was missing from the backup image. The backup environment has been corrected, and both backup and restore workflows now complete successfully.

- **Unable to Move Images in DICOM Projects**

  Image movement controls could become unavailable after opening a task in DICOM projects, preventing users from repositioning medical images during review. Image interaction has been corrected, and users can now move images normally within DICOM tasks.


---
## Versions

</div>

{%- include docs-annotation-pagination.html -%}