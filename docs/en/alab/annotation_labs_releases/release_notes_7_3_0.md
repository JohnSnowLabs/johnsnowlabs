---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 7.3
permalink: /docs/en/alab/annotation_labs_releases/release_notes_7_3_0
key: docs-licensed-release-notes
modify_date: 2025-04-29
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">

## Generative AI Lab 7.3 – Stronger Compliance, Expanded LLM Integrations, and Modernized Analytics
<p style="text-align:center;">Release date: 07-25-2025</p>

Generative AI Lab 7.3.0 delivers significant enhancements in data governance, LLM integration capabilities, and user interface modernization. This release addresses enterprise compliance requirements while expanding model evaluation functionality and improving operational efficiency.

## New Features
## Enhanced HIPAA Compliance: Disabled Local Import Capability
What's New: Administrators can now disable local file imports system-wide, complementing existing local export restrictions to create complete data flow control.

**Technical Implementation:**
- New "Disable Local Import" setting in System Settings → General tab
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

## Support for Claude in LLM Evaluation Projects
**What's New:** Claude is now available as a supported provider in LLM Evaluation and LLM Evaluation Comparison projects, joining existing providers (OpenAI, Azure OpenAI, Amazon SageMaker).

![730image](/assets/images/annotation_lab/7.3.0/3.gif)

**Technical Implementation:**
- Full integration with Anthropic's Claude API
- Support for both single-model evaluation and comparative analysis workflows
- Same evaluation metrics and prompt testing capabilities as other providers

**User Benefits:**
- **AI Researchers:** Can now benchmark Claude's performance against other models using identical test datasets and evaluation criteria
- **Safety-Critical Applications:** Leverage Claude's instruction-following capabilities and lower hallucination rates for regulated domains
- **Model Selection Teams:** Access to a broader provider ecosystem enables more informed model selection decisions

![730image](/assets/images/annotation_lab/7.3.0/4.gif)
<p align="center">Figure 1 - LLM Evaluation</p>


![730image](/assets/images/annotation_lab/7.3.0/5.gif)
<p align="center">Figure 2 - LLM Comparison</p>


**Example Use Case:** A financial services team can compare Claude's performance against GPT-4 for regulatory document summarization, using consistent evaluation metrics to determine which model best maintains factual accuracy while avoiding hallucinations.

## Cloud Storage Credential Management
**What's New:** Cloud storage credentials (AWS S3, Azure Blob Storage) can now be saved at the project level, eliminating repetitive credential entry while maintaining security isolation.

**Technical Implementation:**
- Credentials stored per-project, not globally
- Automatic credential reuse for subsequent import/export operations within the same project
- Dedicated UI controls for managing credentials during Import and Export
- Credentials excluded from project ZIP exports for security compliance
- Support for credential updates through explicit save actions

![730image](/assets/images/annotation_lab/7.3.0/6.gif)

**User Benefits:**
- **Data Scientists:** Eliminates manual credential re-entry for frequent data operations, reducing setup time by 60-80% for iterative workflows
- **Multi-Team Organizations:** Each project team can manage its cloud access without sharing credentials
- **DevOps Teams:** Reduces credential management overhead while maintaining security boundaries

![730image](/assets/images/annotation_lab/7.3.0/7.gif)

**Note:-** Credentials, once saved, will remain associated with the project and will be auto-filled when revisiting the Import or Export pages—even if a different path or new credentials are used temporarily. To update them, users must explicitly choose to save new credentials.*

**Note:-** If credentials are saved for a different cloud provider within the same project (e.g., switching from AWS to Azure), the previously stored credentials will be overwritten with the new set.

**Example Use Case:** A medical coding organization can save their S3 credentials once to import daily batches of clinical documents for human-in-the-loop validation, while simultaneously maintaining separate Azure credentials for exporting coded results to their analytics platform—eliminating daily credential re-entry across both cloud providers.

## Project Creation Restricted to Admin Users
**What's New:** New setting restricts project creation to Admin users only, preventing unauthorized resource consumption and improving governance.

**Technical Implementation:**
- "Only Admins Can Create Projects" toggle in System Settings → General tab
- Affects all user roles: Annotator and Supervisor roles lose project creation privileges when enabled
- Existing projects remain accessible to all assigned users

**User Benefits:**
- **Resource Managers:** Prevents uncontrolled project proliferation and associated compute costs
- **Data Governance Teams:** Ensures all projects go through proper approval workflows before resource allocation
- **System Administrators:** Reduces support overhead from unauthorized or misconfigured projects

**Example Use Case:** A research organization can ensure that only approved team leads (Admin users) can create new annotation projects, preventing individual researchers from accidentally spawning resource-intensive preannotation jobs without budget approval.es.

![730image](/assets/images/annotation_lab/7.3.0/8.png)

## Improvements

### Modernized Analytics Dashboard
**What's New:** Redesign of the Analytics page with modern chart types, improved visual clarity, and responsive layouts.

**Technical Improvements:**
- Added scatter plots and line charts for enhanced data analysis
- Responsive design adapts to various screen sizes
- Improved color schemes and chart styling
- Better layout flexibility for comparing multiple metrics

![730image](/assets/images/annotation_lab/7.3.0/9.gif)

**User Benefits:**
- **Project Managers:** Faster identification of performance trends and anomalies through clearer visualizations
- **Quality Assurance Teams:** More intuitive comparison of annotation quality metrics across different annotators
- **Stakeholders:** Professional-grade reporting visuals suitable for executive presentations

![730image](/assets/images/annotation_lab/7.3.0/10.gif)

![730image](/assets/images/annotation_lab/7.3.0/11.png)

### Added Hotkey Option in Visual Builder
**What's New:** Users can now configure custom hotkeys for annotation actions in the Visual Builder interface.

**Technical Implementation**  
- Hotkey configuration available in **Setup → Configuration → Customize Labels**  
- User-defined shortcuts for frequently used annotation actions  
- Reserved system keys (`r`, `m`, `u`, `h`) remain protected  
- Per-label hotkey assignment  

![730image](/assets/images/annotation_lab/7.3.0/12.gif)

**Note:** Certain keys—such as `r`, `m`, `u`, and `h`—are reserved for system-level functions and cannot be reassigned.

**User Benefits**  
- **High-Volume Annotators:** Customizable shortcuts can improve annotation speed by 30–40% for repetitive tasks  
- **Teams with Accessibility Needs:** Allows accommodation of different physical capabilities and preferences  
- **Multi-Language Projects:** Enables hotkey assignment that matches users' keyboard layouts and language preferences  

### Interface Enhancements
### Improved Efficiency of the Annotation Workflow

**Connected Words and Relations Tooltips**  
- Hover tooltips display full text for truncated entity names and relations  
- Eliminates the need to scroll back to the main annotation area for context  
- Reduces annotation review time, especially for longer entity phrases

![730image](/assets/images/annotation_lab/7.3.0/13.png)

**Page-Wise Relation Display**  
- Relations are now displayed per-page instead of document-wide in multi-page documents  
- Cleaner interface reduces cognitive load for complex document annotation  
- Improves accuracy by focusing attention on relevant page-specific relationships  

![730image](/assets/images/annotation_lab/7.3.0/14.gif)

**Streamlined Label Display**  
- Removed redundant label displays in annotation widgets when sorted by label  
- Cleaner interface reduces visual clutter during annotation review

![730image](/assets/images/annotation_lab/7.3.0/15.png)

### Support for Healthcare NLP 6.0
**What's New:** Integration with John Snow Labs Spark NLP 6 libraries (Spark NLP 6.0.2, Healthcare NLP 6.0.2, Visual NLP 6.0.0).

**Technical Improvements**  
- Enhanced OCR accuracy for scanned documents  
- Improved image-to-text extraction capabilities  
- Access to the latest medical and visual NLP models via Online Models Hub  
- Better support for privacy-preserving NLP workflows  

**User Benefits**  
- **Healthcare Teams:** Higher accuracy in processing medical documents and clinical notes  
- **Document Processing Teams:** Improved extraction quality from scanned forms, contracts, and legacy documents  
- **Compliance Teams:** Enhanced privacy-preserving capabilities for sensitive document processing  

### Bug Fixes
- **No UI error when Project import fails due to missing or invalid application license**  
  - *Issue:* No error message was shown when project import failed due to missing or invalid license.  
  - *Resolution:* An error message now appears in a toast notification if the license is missing or invalid during project import.

- **Rules tab missing in Re-use Resource page for de-identification Project**  
  - *Issue:* Rules tab was not visible in Re-use Resource page for de-identification projects.  
  - *Resolution:* Rules tab now appears as expected, and rules can be used to identify PII/PHI in de-identification projects.

- **External Service Provider can be created without the required secret key**  
  - *Issue:* External service providers could be created without providing a secret key.  
  - *Resolution:* Secret key is now mandatory when creating external service providers.

- **Users are seeing "Generate Response" even when no service providers are configured in the project**  
  - *Issue:* "Generate Response" button was shown even when no service providers were configured.  
  - *Resolution:* A dialog now guides users to the LLM Configuration page if no provider is set.

- **Fix placement of radio button after text title**  
  - *Issue:* Radio buttons were misaligned after text titles in LLM Evaluation and Comparison projects.  
  - *Resolution:* Radio buttons are now properly aligned with their respective text titles.

- **Users cannot assign groups to the project**  
  - *Issue:* Users were unable to assign groups to projects.  
  - *Resolution:* Users can now create, update, delete, and assign groups to projects without issues.

- **User is not able to edit LLM prompt**  
  - *Issue:* External LLM prompts could not be edited.  
  - *Resolution:* External LLM prompts can now be edited and updated seamlessly.

- **Validation is successful even with an invalid Service Provider**  
  - *Issue:* Validation passed even with invalid external service provider details.  
  - *Resolution:* Endpoint URLs are now properly validated on the frontend during validation.

- **Text Over Flow in Result Section for External prompt**  
  - *Issue:* Large external prompt texts overflowed in the result section.  
  - *Resolution:* Scroll functionality has been added to handle large prompt results without overflow.

- **Unable to Click "No" Button on Configuration Navigation Confirmation Popup**  
  - *Issue:* "No" button on the configuration navigation confirmation popup was unresponsive.  
  - *Resolution:* The confirmation dialog now works correctly, and the "No" button is fully functional.

- **Triple Dot Menu Not Accessible for Users Listed After Search**  
  - *Issue:* The triple dot menu (⋮) was inaccessible for users listed after a search.  
  - *Resolution:* The menu is now accessible, allowing edit and delete actions as expected.

- **Error while changing user roles due to certain characters in a task**  
  - *Issue:* Errors occurred when changing user roles if tasks contained certain unsupported characters (e.g. \u0000, \u007f, \u009f, \u0001).  
  - *Resolution:* These characters are now handled properly, and user roles can be changed without issues.


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}