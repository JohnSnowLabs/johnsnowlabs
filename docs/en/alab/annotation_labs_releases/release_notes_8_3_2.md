---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 8.3.2
permalink: /docs/en/alab/annotation_labs_releases/release_notes_8_3_2
key: docs-licensed-release-notes
modify_date: 2026-10-22
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">



**Generative AI Lab 8.3.2** focuses on improving support for air-gapped environments, strengthening license validation, and addressing deployment and application stability issues.

This release introduces offline Universal License validation, allowing organizations operating in restricted or disconnected environments to validate their licenses without requiring an internet connection. Audit logging is now also supported in Azure Marketplace deployments.

Additional bug fixes address Models Hub availability, Universal License recognition, air-gapped deployment stability, and file imports.

## Improvements

### Audit Logging Support for Azure Marketplace Deployments

**What's Improved**

Azure Marketplace deployments now include an option to enable audit logging directly during deployment, simplifying the configuration of Elasticsearch and Kibana for audit log management.The deployment process has been updated to include a dedicated checkbox that allows customers to enable audit logging when deploying Generative AI Lab through Azure Marketplace.

**Technical Details**

- Deployment Configuration: A new checkbox in the Azure Marketplace deployment interface allows customers to enable audit logging.
- Elasticsearch and Kibana Support: The deployment process now supports the Elasticsearch and Kibana components required for audit log management.
- Simplified Setup: Customers can enable audit logging during deployment without requiring additional manual configuration.


### Offline Universal License Validation for Air-Gapped Environments

**What's Improved**

Air-gapped deployments now support offline validation of Universal Licenses, allowing organizations to enforce license validity without requiring an internet connection.

Previously, license validation had to be disabled for air-gapped deployments, allowing the application to operate without enforcing license expiration dates.

With the updated licensing workflow, organizations can validate their Universal License locally, ensuring the application remains operational only while the license is valid.

**Technical Details**

The licensing configuration supports two operating modes:

- Standard License Validation: The application requires a valid application license with one FC to operate.
- Offline Universal License Validation: Online license checks are disabled, but local validation remains enabled. The application requires a valid Universal License and enforces its validity period without connecting to an external licensing service.

Offline validation is configured using the following settings:
```
--set configuration.echo.enabled=true \
--set configuration.echo.offline=true
```

**User Benefits**

- Fully Offline License Validation: Validate Universal Licenses without an internet connection.
- License Expiration Enforcement: Ensure application access remains aligned with the purchased license validity period.
- Support for Restricted Environments: Deploy and operate Generative AI Lab in air-gapped environments while maintaining license enforcement.
- Flexible Licensing Configuration: Support both standard online validation and offline licensing workflows according to deployment requirements.

**Example Use Case**

A healthcare organization deploys Generative AI Lab in an air-gapped environment where external network access is prohibited.

Using offline Universal License validation, the organization can import its license and operate the application without an internet connection. The application validates the license locally and enforces its expiration date according to the purchased license.


## Bug Fixes

### Models Hub and Online Model Catalog
- **Internal Server Error on the Online Model Page**

  The Online Model page could fail to load due to an Internal Server Error when accessing the /api/modelshub/models endpoint. The underlying API issue has been addressed, restoring access to the online model catalog.

- **Models Not Listed in Models Hub**

  Models could fail to appear in the Models Hub because the model listing API encountered a KeyError when the compatible_editions field was missing from model metadata. Model listing now handles this condition, allowing available models to be displayed correctly.

### Licensing and Air-Gapped Deployments
- **Application License Not Recognized with a Valid Universal License**

  Deployments using a valid Universal License could incorrectly display an "Application License Missing" error, preventing normal application operations. The issue also affected Universal License imports in offline mode. Valid licenses are now recognized correctly, allowing users to import licenses, perform application operations, and access licensed pre-annotation and OCR functionality according to their configuration.

- **Pods Failing to Restart in Air-Gapped Environments**

  Application pods could fail to restart when an air-gapped instance was stopped and started again. Pod startup and recovery have been corrected, allowing services to return to a stable state after instance restarts.

- **Docker Image Compatibility in Air-Gapped EKS Deployments**

  Docker image issues could interfere with successful installation and startup in air-gapped Amazon EKS environments. Deployment images have been updated to support successful installation and application access.

- **Image Mismatches in Air-Gapped Deployments**

  Image mismatches affecting air-gapped deployments have been addressed to improve deployment compatibility and reliability.

- **Broken Image References After the Apache Airflow Upgrade**

  Image references affected by the Apache Airflow upgrade could interfere with air-gapped installations. The references have been corrected, restoring successful installation and application startup.

### Task Import
- **Non-DICOM File Imports Failing Through the Import Server**

  The Import Server could process DICOM files while failing to import other supported file types, including PDF documents using Docling-based extraction. Import functionality has been restored for supported non-DICOM files, allowing users to import documents through the Import Server.
---
## Versions

</div>

{%- include docs-annotation-pagination.html -%}