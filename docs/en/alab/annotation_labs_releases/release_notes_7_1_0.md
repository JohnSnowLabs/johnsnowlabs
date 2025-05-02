---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 7.1
permalink: /docs/en/alab/annotation_labs_releases/release_notes_7_1_0
key: docs-licensed-release-notes
modify_date: 2025-04-29
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">


## Generative AI Lab 7.1: Enhanced Auditability and Workflow Efficiency
Release date: 04-29-2024

Generative AI Lab 7.1 introduces several new features and improvements focused on enhancing observability, task management, data governance, and annotation workflows. It includes support for real-time log indexing for audit and compliance needs, automatic bulk task assignment for annotators, as well as improved project setup and annotation flows. These updates aim to improve system usability, transparency, and operational efficiency.

## Advanced Audit Logging and Monitoring 
Generative AI Lab now supports real-time, high-performance audit logging. This feature enhances traceability and compliance readiness without compromising security or performance. 

### Key Capabilities 

- **Real-Time Indexing:** Captures user activities and system events, including project lifecycle actions, configuration changes, model hub events, and administrative operations. 

- **Configurable Deployment:** Elastic Search can be deployed internally or connected to an external cluster for complete data ownership. 

- **Privacy First:** Metadata such as user ID, API method, timestamp, and context are logged without exposing sensitive payloads. 

- **Log Management:** Supports backup to S3, configurable retention policies, and restores for robust governance. 

- **User Benefit:** Enables organizations to achieve secure, tamper-proof auditability critical for compliance and operational transparency. 

**Steps to enable Audit Logs on your Generative AI Lab instance:**

This feature can be enabled if needed for environments that require advanced auditing or compliance tracking. For maximum control and security, administrators can configure Generative AI Lab to use an externally hosted Elastic Search cluster. 

To install Elastic Search locally in Gen AI Lab, add the following parameter to the installer or updater script and then run the installation or update: 

```bash
--set installElasticsearch=true
```

Once installed, enable Elastic Search by adding the following parameter to the installer or updater script and then run the installation or update: 

```bash
--set global.elasticsearch.enable=true
```

One can disable Elastic Search as well. To disable it, add the following parameter to the installer or updater script and then run the installation or update:

```bash
--set global.elasticsearch.enable=false
```

To include user logs in Elastic Search, add the following parameters to the installer or updater script and then run the installation or update: 

```bash
--set global.elasticsearch.includeKeycloak=true \
--set global.azure.images.keycloak.tag=keycloak-<GenAI Lab Version> \
--set global.azure.images.keycloak.image=annotationlab \
--set global.azure.images.keycloak.registry=docker.io/johnsnowlabs
```
**Note:** Replace GenAI Lab Version with the appropriate Generative AI Lab version that you want to install or upgrade to. 

Once the features are enabled, the system starts real-time indexing of user and system activity while ensuring privacy and performance. All logs include metadata like user ID, API method and path, timestamp, and event context, without exposing sensitive payloads such as passwords, PHI, and PII.  

![710image](/assets/images/annotation_lab/7.1.0/1.png)

### What Gets Indexed
- **Project Lifecycle**: Creation and deletion of projects.
- **Configuration Changes**: Updates to teams, model assignments, external integrations, and label settings.
- **Import/Export Activities**: Logs for task imports/exports.
- **Models Hub Events**: Events such as model import/export and model downloads.
- **Administrative Actions**: Logs related to user creation, updates, deletions, license upload and deletion, enabling/disabling local export toggles, analytics approval, and system backups.

### Log Management Features
- **Backup & Restore**: Schedule automatic dumps of indexed logs directly to S3 buckets for backup and recovery.
- **Retention Policies**: Configure automated deletion of old logs to optimize storage and comply with data governance policies.
- **External Elastic Support**: Connect to your company's existing ES logging infrastructure to unify and enhance your organization's knowledge base with integrated log data.

This new feature enhances Generative AI Lab with secure, tamper-proof logging and flexible log data management, offering robust observability without disrupting workflows. It’s an essential addition for teams focused on security, compliance, and operational transparency.

## Smarter Task Distribution: Bulk Assignment at Scale
Generative AI Lab now offers bulk task assignment capabilities, allowing up to 200 unassigned tasks to be allocated simultaneously to selected annotators. 

### Key Capabilities
- Sequential or Random Assignment: Tasks can be distributed in order or randomly from the unassigned pool. 
- Efficient Scaling: Reduces manual effort in large-scale projects, optimizing resource utilization. 

**User Benefit:** Accelerates task distribution, improving operational efficiency and annotation throughput. 

### Bulk Assignment Process:
- Click on the "Assign Task" button.
- Select the annotators to whom you wish to assign tasks.
- Specify the number of tasks to assign to each annotator.
- Define any required criteria for task selection.
- Click on "Assign" to complete the process.​

![710image](/assets/images/annotation_lab/7.1.0/2.gif)

**Notes**
_- The maximum number of tasks that can be assigned at once is 200._
_- If the total number of unassigned tasks is less than the selected task count, all unassigned tasks will be assigned to the first selected annotator._

![710image](/assets/images/annotation_lab/7.1.0/3.gif)

## Improvements

### Only What You Need: Resource Filtering by Project Type
Generative AI Lab enhances the Reuse Resource interface by displaying only compatible models, prompts, and rules based on the selected project type.

**Context-Aware Resource Display:** When a project type is selected, the Reuse Resource page now filters and displays only those models, prompts, and rules that are compatible with that specific project type.​

Example – Visual NER projects, for example, will only show supported text NER models and skip unsupported resource types. Resources such as assertion models, Classification models, and OpenAI prompts, which are not supported, will not be shown. 

For Visual NER project:

![710image](/assets/images/annotation_lab/7.1.0/4.gif)


For Checkbox Detection project:


![710image](/assets/images/annotation_lab/7.1.0/5.gif)

**User Benefit**: Simplifies resource selection, eliminates validation errors, and accelerates project setup. 

### Effortless Project Resets: Bulk Task Deletion
Generative AI Lab now introduces a one-click bulk deletion option for project tasks. This enhancement eliminates the need to remove tasks individually, facilitating more efficient project management, especially during large-scale cleanups.​ 

**Feature Details:** 
- User Interface Integration: Accessible directly from the project task page. 
- Cautionary Control:** Deletion is irreversible, ensuring that users proceed with clarity and intent. 

**User Benefit:** Facilitates efficient large-scale project resets and cleanups. 

![710image](/assets/images/annotation_lab/7.1.0/6.gif)

Note: _Irreversible Action: Please note that deleting tasks in bulk is irreversible. Ensure that all necessary data is backed up or no longer needed before proceeding with this action._

### More Control, More Confidence: Split Actions for PHI De-Identification 
The de-identification process has been redesigned into two discrete steps: identification and removal of sensitive data, giving users better control over the workflow.

**New Workflow:**

- Step 1: Identify PHI/PII within documents. 
- Step 2: Review, adjust if necessary, then finalize de-identification. 

**User Benefit:** Provides greater transparency, enabling careful review before sensitive information is permanently removed. 

![710image](/assets/images/annotation_lab/7.1.0/7.png)

By splitting identification and de-identification into separate steps, the new process provides greater transparency and allows annotators to review and confirm all changes before finalizing the output.

### Stay Focused: Pre-Annotation Defaults to Current Page 
Pre-annotation now defaults to tasks on the current page instead of the entire project. Previously, users had to manually select this option; now, it is the default behavior. 

**Change Impact:** 
- **Error Prevention:** Reduces the risk of accidentally pre-annotating full projects. 
- **Faster Processing:** Localizes the workload for quicker completions. 

**User Benefit:** Speeds up workflow and minimizes unintentional system load. 

![710image](/assets/images/annotation_lab/7.1.0/8.png)

### Seamless Zoom: Persistent PDF Zoom Levels 

Zoom levels in PDF tasks are now preserved across navigation actions within the same task session. The zoom setting remains consistent during annotation, saving, and page navigation, and only resets if the page is manually refreshed. 

Previously, the zoom level would reset after each action, which could disrupt the annotation workflow. This update ensures a more consistent and uninterrupted experience when working with PDF documents. 

**User Benefit:** Enhances user comfort and consistency when working through multi-page PDF annotations. 

![710image](/assets/images/annotation_lab/7.1.0/9.gif)

### Color-Coded Clarity: Random Colors for Visual Builder Labels 
When adding multiple labels in the Visual Builder, each label is now assigned a random color by default. While users could previously add multiple labels at once using the Visual Builder, all labels were assigned the same default color, making it harder to visually distinguish them during annotation, and users had to manually update the colors for each label.

![710image](/assets/images/annotation_lab/7.1.0/10.gif)

**User Benefit:** Saves setup time and improves usability during annotation tasks. 

### Find It Fast: Auto-Expanded Labels in Page-Wise Annotation View 
For HCC Coding projects, annotations are now organized page-by-page, with clicked labels auto-expanded in the sidebar. 

**Enhanced Navigation with Label Spotlighting:** Clicking a labeled text highlights and expands the corresponding annotation entry. 

**User Benefit:** Streamlines navigation, improves editing accuracy and simplifies the review of complex multi-page documents. 

![710image](/assets/images/annotation_lab/7.1.0/11.gif)


## Bug Fixes

- **License server is not deployed in AMI**

	Previously, the license server failed to deploy in the AMI environment. This issue has now been fixed, and the license server deploys successfully without errors for AMI.

- **User can add licensed healthcare models to project and save configurations without any error**

	Users were previously able to add licensed healthcare models to a project without a valid license if the models were already downloaded. The issue has been fixed, and now, licensed models cannot be used in a project without a valid license, even if they are already present in the instance.

- **Model Finner_header cannot be used along with other models due to missing embedding**

	Previously, the Finner_Header model could not be used alongside other models due to missing embeddings. This issue has been fixed, and the required embeddings are now downloaded automatically, allowing users to use the model without any problems.

- **"Last Training Succeeded" status is shown even when training was aborted**

	The "Last Training Succeeded" status was shown even after the training was aborted (i.e., when the server was deleted from the cluster page). This has been fixed, and the correct "Aborted" message is now displayed, even after refreshing the page.

- **Users cannot import external Prompts**

	When attempting to import an external prompt, users would encounter an error dialog even with a valid prompt file. This issue has been fixed, and users can now import external prompts successfully without any errors.

- **Validation error is observed when user tries to update the project configuration (remove labels) even when there are no tasks**

	A validation error occurred when users tried to update the project configuration by removing an existing model and adding a new one, even when no tasks were present. This issue has been resolved, and users can now update the project configuration seamlessly when no tasks are present.

- **Sometimes the UI crashes while clicking/dragging in PDF file in VisualNER project**

	The UI would occasionally crash when interacting with the image section of PDF files, particularly during clicking or dragging actions in VisualNER projects. It has now been fixed, ensuring that the UI remains stable and responsive during all interactions.

- **Deployed De-identification server abruptly stopped in AMI instance**

	Previously, the deployed De-identification server would stop suddenly on the cluster page after a few minutes in the AMI instance. This issue has been fixed, and the server now remains idle unless manually stopped by the user.

- **Hotkey Tooltip Overflow in Region Section Buttons**

	Hotkey tooltips for the Region section buttons were not displayed properly, with some overlapping onto button text and others being partially hidden. This issue has been fixed, and the tooltips are now clearly visible and correctly positioned.

- **Training fails with 'Out Of Memory' when training large dataset with sampling**

	Previously, training would fail when using a dataset with large sampling. This issue has been fixed, and training now completes successfully even with larger datasets.

- **Unable to Manually Enter Color Code in Edit Label**

	While editing a label in the Customize Labels section, entering a valid hex color code did not reflect the correct color in the color picker. This issue has been fixed, and the color picker now accurately displays the corresponding color when a valid hex code is entered.

- **UI Freeze and 404 Error During LangTest Execution**

	Previously, running a LangTest would freeze the UI and result in a 404 error, despite the test completing successfully. This issue has now been resolved, and the LangTest runs smoothly without causing any UI freezes.

- **User navigates to something went wrong page while selecting external prompt or rules for side-by-side project**

	Users were redirected to a "Something went wrong" page when attempting to select external prompts or rules in side-by-side projects. This issue has been fixed, and users can now select prompts and rules without errors.


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}