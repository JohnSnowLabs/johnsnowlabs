---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: HIPAA Compliance
permalink: /docs/en/alab/hipaa_compliance
key: docs-training
modify_date: "2025-07-28"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## Advanced Audit Logging and Monitoring 
Generative AI Lab provides robust real-time audit logging and monitoring capabilities to ensure security, compliance, and operational transparency—all without compromising performance.

### Key Capabilities 

- **Real-Time Activity Logging:** Captures user activities and system events, including project lifecycle actions, configuration changes, model hub events, and administrative operations. 

- **Flexible Deployment:** Elastic Search can be deployed internally or connected to an external cluster for complete data ownership. 

- **Privacy First:** Metadata such as user ID, API method, timestamp, and context are logged without exposing sensitive payloads. 

- **Log Management:** Supports backup to S3, configurable retention policies, and restores for robust governance. 



### Enabling Audit Logs

This feature can be enabled if needed for environments that require advanced auditing or compliance tracking. For maximum control and security, administrators can configure Generative AI Lab to use an externally hosted Elastic Search cluster. 

To install Elastic Search locally in Gen AI Lab, add the following parameter to the installer or updater script and then run the installation or update: 

```bash
--set installElasticsearch=true
```

Once installed, enable Elastic Search by adding the following parameter to the installer or updater script and then run the installation or update: 

```bash
--set global.elasticsearch.enable=true
```

One can disable Elastic Search as well. To disable it, add the following parameter to the installer or updater script and then run the installation or update:

```bash
--set global.elasticsearch.enable=false
```

To include user logs in Elastic Search, add the following parameters to the installer or updater script and then run the installation or update: 

```bash
--set global.elasticsearch.includeKeycloak=true \
--set global.azure.images.keycloak.tag=keycloak-<version> \
--set global.azure.images.keycloak.image=annotationlab \
--set global.azure.images.keycloak.registry=docker.io/johnsnowlabs
```
**Note:** Replace `<version>` with the appropriate Generative AI Lab version that you want to install or upgrade to. 

Once the features are enabled, the system starts real-time indexing of user and system activity while ensuring privacy and performance. All logs include metadata like user ID, API method and path, timestamp, and event context, without exposing sensitive payloads such as passwords, PHI, and PII.  

![710image](/assets/images/annotation_lab/7.1.0/1.png)

### Logged Events
- **Project Lifecycle**: Creation and deletion of projects.
- **Configuration Changes**: Updates to teams, model assignments, external integrations, and label settings.
- **Import/Export Activities**: Logs for task imports/exports.
- **Models Hub Events**: Events such as model import/export and model downloads.
- **Administrative Actions**: Logs related to user creation, updates, deletions, license upload and deletion, enabling/disabling local export toggles, analytics approval, and system backups.

### Log Management Features
- **Backup & Restore**: Schedule automatic dumps of indexed logs directly to S3 buckets for backup and recovery.
- **Retention Policies**: Configure automated deletion of old logs to optimize storage and comply with data governance policies.
- **External Elastic Support**: Connect to your company's existing ES logging infrastructure to unify and enhance your organization's knowledge base with integrated log data.

These features provide tamper-proof audit trails and centralized observability ideal for high-compliance environments.

## Restricting Local Imports
Administrators can globally disable local file imports to enforce strict data governance. This enhances control by ensuring only cloud-based sources like S3 or Azure Blob Storage are used.

**Implementation:**
- Managed in System Settings → General tab
- Project-level exceptions are available through the dedicated Exceptions widget
- When this option is enabled, only cloud storage imports (Amazon S3, Azure Blob Storage) are permitted.
- Setting applies globally across all projects unless explicitly exempted

![730image](/assets/images/annotation_lab/7.3.0/1.png)

**User Benefits:**
- **Healthcare Organizations:** Ensures all patient data flows through auditable, encrypted cloud channels rather than local file systems.
- **Enterprise Teams:** Eliminates the risk of sensitive data being imported from uncontrolled local sources.
- **Compliance Officers:** Provides granular control over data ingress while maintaining operational flexibility for approved projects.

![730image](/assets/images/annotation_lab/7.3.0/2.png)

**Example Use Case:** A healthcare system can disable local imports for all PHI processing projects while maintaining exceptions for internal development projects that use synthetic data.

## Restricting Local Exports

Local data export can be restricted to enforce cloud-only workflows and reduce risk when handling sensitive data.

**Configuration**
System administrators can manage export settings from the System Settings page. By enabling the "Disable Local Export" option, the export to a local workstation for all projects is turned off.

**Selective Export Exceptions**

Administrators have the flexibility to specify projects that can still use local export if needed. To do this, click on the "Add Project" button from the Exceptions widget and search for the projects to add to the exceptions list.

**S3 Bucket Export**

With the "Disable Local Export" option activated, users can only export tasks and projects to Amazon S3 bucket paths. This ensures the protection of sensitive data that will be stored securely in the cloud.

![disableExport2](/assets/images/annotation_lab/5.2.2/3.gif)


## Project Creation Restricted to Admin Users
To prevent unregulated resource usage, administrators can restrict project creation rights to Admin users only.

**Configuration**
- "Only Admins Can Create Projects" toggle in System Settings → General tab
- Affects all user roles: Annotator and Supervisor roles lose project creation privileges when enabled
- Existing projects remain accessible to all assigned users

**User Benefits**
- **Resource Control:** Prevents uncontrolled project proliferation and associated compute costs
- **Governance:** Ensures all projects go through proper approval workflows before resource allocation
- **Simplified Oversight:** Reduces support overhead from unauthorized or misconfigured projects

**Example Use Case:** A research organization can ensure that only approved team leads (Admin users) can create new annotation projects, preventing individual researchers from accidentally spawning resource-intensive preannotation jobs without budget approval.es.

![730image](/assets/images/annotation_lab/7.3.0/8.png)

</div>