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

## Native LLM Evaluation Workflow with Multi-Provider Integration Generative AI Lab 7.2.0
<p style="text-align:center;">Release date: 06-23-2025</p>

Generative AI Lab 7.2.0 introduces native LLM evaluation capabilities, enabling complete end-to-end workflows for importing prompts, generating responses via external providers (OpenAI, Azure OpenAI, Amazon SageMaker), and collecting human feedback within a unified interface. The new LLM Evaluation and LLM Evaluation Comparison project types support both single-model assessment and side-by-side comparative analysis, with dedicated analytics dashboards providing statistical insights and visual summaries of evaluation results.

New annotation capabilities include support for CPT code lookup for medical and clinical text processing, enabling direct mapping of labeled entities to standardized terminology systems.  

The release also delivers performance improvements through background import processing that reduces large dataset import times by 50% (from 20 minutes to under 10 minutes for 5000+ files) using dedicated 2-CPU, 5GB memory clusters.  

Furthermore, annotation workflows now benefit from streamlined NER interfaces that eliminate visual clutter while preserving complete data integrity in JSON exports. Also, the system now enforces strict resource compatibility validation during project configuration, preventing misconfigurations between models, rules, and prompts.  

Additionally, 20+ bug fixes address critical issues, including sample task import failures, PDF annotation stability, and annotator access permissions. 

Whether you're tuning model performance, running human-in-the-loop evaluations, or scaling annotation tasks, Generative AI Lab 7.2.0 provides the tools to do it faster, smarter, and more accurately.

## New Features
## LLM Evaluation Project Types with Multi-Provider Integration

Two new project types enable systematic evaluation of large language model outputs:

Two new project types enable the systematic evaluation of large language model outputs:
• **LLM Evaluation:** Assess single model responses against custom criteria
• **LLM Evaluation Comparison:** Side-by-side evaluation of responses from two different
models

Supported Providers:
- **OpenAI**
- **Azure OpenAI**
- **Amazon SageMaker**

#### Service Configuration Process
1. Navigate to **Settings → System Settings → Integration**.
2. Click **Add** and enter your provider credentials.
3. Save the configuration.

![IntegrateExternalProvider](https://github.com/user-attachments/assets/6992c45d-edcd-413e-89d0-36f2d3ed2ee9)

### LLM Evaluation Project Creation

1. Navigate to the Projects page and click New.
2. After filling in the project details and assigning to the project team, proceed to the
Configuration page.
3. Under the Text tab on step 1 - Content Type, select LLM Evaluation task and click on
Next.
4. On the Select LLM Providers page, you can either:
   - Click Add button to create an external provider specific to the project (this provider will only be used within this project), or
   - Click Go to External Service Page to be redirected to Integration page, associate
the project with one of the supported external LLM providers, and return
to Project → Configuration → Select LLM Response Provider,
5. Choose the provider you want to use, save the configuration and click on Next.
6. Customize labels and choices as needed in the Customize Labels section, and save the configuration.

![Configure-LLMEvaluation](https://github.com/user-attachments/assets/59288e56-22e2-495c-9bd4-b1a77a7fd453)

For **LLM Evaluation Comparison** projects, follow the same steps, but associate the project with **two** different external providers and select both on the **LLM Response Provider** page.

### Sample Import Format for LLM Evaluation

To start working with prompts:
1. Go to the **Tasks** page and click **Import**.
2. Upload your prompts in either .json or .zip format. Following is a Sample JSON Format to import prompt:

#### Sample JSON for LLM Evaluation Project
```json
{
  "data": {
    "prompt": "Give me a diet plan for a diabetic 35 year old with reference links",
    "response1": "",
    "llm_details": [
      { "synthetic_tasks_service_provider_id": 2, "response_key": "response1" }
    ],
    "title": "DietPlan"
  }
}
```
#### Sample JSON for LLM Evaluation Comparision Project
```json
{
  "data": {
    "prompt": "Give me a diet plan for a diabetic 35 year old with reference links",
    "response1": "",
    "response2": "",
    "llm_details": [
      { "synthetic_tasks_service_provider_id": 2, "response_key": "response1" },
       { "synthetic_tasks_service_provider_id": 2, "response_key": "response2" }
    ],
    "title": "DietPlan"
  }
}
```
3. Once the prompts are imported as tasks, click the **Generate Response** button to generate LLM responses.

![ImportAndGenerateRespone](https://github.com/user-attachments/assets/3057814a-f480-423c-9020-102965430c18)

After responses are generated, users can begin evaluating them directly within the task interface.

### Analytics Dashboard for LLM Evaluation Projects

A dedicated analytics tab provides quantitative insights for LLM evaluation projects:

- Bar graphs for each evaluation label and choice option
- Statistical summaries derived from submitted completions
- Multi-annotator scenarios prioritize submissions from highest-priority users
- Analytics calculations exclude draft completions (submitted tasks only)

![Analytics-LLM](https://github.com/user-attachments/assets/fe03702d-85cb-4d53-b423-3d3ca200d330)

The general workflow for these projects aligns with the existing annotation flow in Generative AI Lab. The key difference lies in the integration with external LLM providers and the ability to generate model responses directly within the application for evaluation.

These new project types provide teams with a structured approach to assess and compare LLM outputs efficiently, whether for performance tuning, QA validation, or human-in-the-loop benchmarking.

## CPT Lookup Dataset Integration for Annotation Extraction
NER projects now support CPT codes lookup for standardized entity mapping. Setting up lookup datasets is simple and can be done via the Customize Labels page in the project configuration wizard.

#### Use Cases:
- Map clinical text to CPT codes
- Link entities to normalized terminology systems
- Enhance downstream processing with standardized metadata

#### Configuration:
1. Navigate to Customize Labels during project setup
2. Click on the label you want to enrich
3. Select your desired Lookup Dataset from the dropdown list
4. Go to the Task Page to start annotating — lookup information can now be attached to the labeled texts

<img width="1302" alt="Screenshot 2025-06-10 at 10 55 50 AM" src="https://github.com/user-attachments/assets/03a55c5a-3737-4d56-911f-12d656637b2b" />

## Improvements
## Redesigned Annotation Interface for NER Projects
The annotation widget interface has been streamlined for Text and Visual NER project types. This update focuses on enhancing clarity, reducing visual clutter, and improving overall usability, without altering the core workflow. All previously available data remains intact in the exported JSON, even if not shown in the UI. 

### Enhancements in Name Entity Recognition and Visual NER Labeling Project Types
- Removed redundant or non-essential data from the annotation view.
- Grouped the Meta section visually to distinguish it clearly and associate the delete button specifically with metadata entries.
- Default confidence scores display (1.00) with green highlighting.
   Hover functionality on labeled text reveals text ID.

![NER-Project-Annotation](https://github.com/user-attachments/assets/e822e21b-3d08-4df7-85c0-59ba65e0daff)

#### Visual NER Specific Updates
- **X-position** data relocated to detailed section
- **Recognized text** is now placed at the top of the widget for improved readability.
- Maintained data integrity in JSON exports despite UI simplification

![VisualNER-Annotation](https://github.com/user-attachments/assets/7875878c-2f6e-4b94-94d3-46e1b5c6c752)

These enhancements contribute to a cleaner, more intuitive user interface, helping users focus on relevant information during annotation without losing access to critical data in exports.

### Optimized Import Processing for Large Datasets
The background processing architecture now handles large-scale imports without UI disruption through intelligent format detection and dynamic resource allocation. When users upload tasks as a ZIP file or through a cloud source, Generative AI Lab automatically detects the format and uses the import server to handle the data in the background — ensuring smooth and efficient processing, even for large volumes. 

For smaller, individual files — whether selected manually or added via drag-and-drop — imports are handled directly without background processing, allowing for quick and immediate task creation.

**Note:** Background import is applied only for ZIP and cloud-based imports.

**Automatic Processing Mode Selection:**
- ZIP files and cloud-based imports: Automatically routed to background processing via dedicated import server
-  Individual files (manual selection or drag-and-drop): Processed directly for immediate task creation
- The system dynamically determines optimal processing path based on import source and volume

<img width="1540" alt="Screenshot 2025-06-03 at 8 44 27 PM" src="https://github.com/user-attachments/assets/e3ef153a-1e38-42f6-b482-a94fbc696fbc" />

**Technical Architecture:**
- Dedicated import cluster with auto-provisioning: 2 CPUs, 5GB memory (non-configurable)
- Cluster spins up automatically during ZIP and cloud imports
- Automatic deallocation upon completion to optimize resource utilization
- Sequential file processing methodology reduces system load and improves reliability
- Import status is tracked and visible on the Import page, allowing users to easily monitor
progress and confirm successful uploads.

<img width="898" alt="Screenshot 2025-06-03 at 8 41 48 PM" src="https://github.com/user-attachments/assets/6e505c44-e8af-4d82-b8db-e64c06866ca4" />

**Performance Improvements:**
- Large dataset imports (5000+ files): Previously 20+ minutes, now less than 10 minutes
- Elimination of UI freezing during bulk operations
- Improved system stability under high-volume import loads

***Note: Import server created during task import is counted as an active server.***

### Refined Resource Compatibility Validation
In previous versions, while validation mechanisms were in place to prevent users from combining incompatible model types, rules, and prompts, the application still allowed access to unsupported resources. This occasionally led to confusion, as the Reuse Resource page displayed models or components not applicable to the selected project type. With version 7.2.0, the project configuration enforces strict compatibility between models, rules, and prompts:
- Reuse Resource page hidden for unsupported project types
- Configuration interface displays only compatible resources for selected project type

![FilterModels](https://github.com/user-attachments/assets/fba83d42-4c37-4a34-a9bb-002974bbe7b0)

These updates ensure a smoother project setup experience and prevent misconfigurations by guiding users more effectively through supported options.

### Bug Fixes
**Sample Task Import **Resolution****
- **Issue:** Sample task import failures in HTML projects with NER labels
- **Resolution**: Sample tasks now import successfully into HTML projects containing NER labels

**PDF Annotation Stability**
- **Issue:** PDF page refreshes when adding lookup codes in Side-by-Side projects
- **Resolution**: PDF viewport maintains position during lookup data entry

**Lang Test Model Versioning**
- **Issue:** Test execution errors for v1-generated test cases after model retraining to v2
- **Resolution**: Previously generated test cases execute successfully across model versions

**Relation Tag Display Logic**
- **Issue:** Relations with "O" tag inappropriately displayed in UI
- **Resolution**: "O" tagged relations properly excluded from UI display

**License Banner Event Handling**
- **Issue:** license_banner_dismiss event triggered on page refresh
- **Resolution**: Event triggers only on explicit user dismissal

**Task Selection Interface Stability**
- **Issue:** Assignee button resizing and task-per-page selection failures when all tasks selected
- **Resolution**: UI elements maintain consistent sizing during bulk operations

**Demo Project Access Control**
- **Issue:** Admin users automatically added to Demo De-identification projects
- **Resolution**: Admin users no longer added by default to demo projects

**Annotator Access Permissions**
- **Issue:** "User doesn't have permission" errors for assigned annotators in de-identification
projects
- **Resolution**: Annotators with task assignments can access task pages without permission
errors

### Features
- [ALAB-6326] Add feature to Import Questions, Generate LLM Responses, and Analyze Annotator Feedback 
- [ALAB-6170] Label Widget Makeover: Streamlined UI for Better Usability

### Improvements
- [ALAB-5901] Implement background processing service to support large-scale task imports
- [ALAB-6368] Add CPT lookup table
- [ALAB-6019] Maintain consistency while showing validation error message in Re-use resource page

### Bug Fixes
- [ALAB-5932] ZIP file is not imported
- [ALAB-6076] Sample task is not imported into the HTML projects with NER labels
- [ALAB-6195] Clicking on the arrow to add lookup code refreshes the PDF
- [ALAB-6318] Lang Test Error When Running Test
- [ALAB-6323] Relations with tag 0 are shown on the UI
- [ALAB-6346] license_banner_dismiss Triggered on Refresh Without User Dismissal of Banner
- [ALAB-6352] Assignee Button Resizes and Task Per Page Selection Fails When All Tasks Are Selected
- [ALAB-6353] Admin user is added to Demo De-identification project by default
- [ALAB-6354] Error while the user annotates the Prompt Section and tries to save the task in LLM Response Comparison 
- [ALAB-6355] Unused/missing imports causing annotationlab container to crash in Docker
- [ALAB-6362] "User doesn't have permission to access the resource" error when annotator navigates to the task page
- [ALAB-6363] Loading button missing and task page is not auto refreshing during task import
- [ALAB-6364] Import Server is not automatically deleted from the Cluster Page after task import is complete
- [ALAB-6369] Pre-annotation fails when using External Prompt and NER Model in a single project
- [ALAB-6378] Validation fails even when correct credentials are used while integrating external provider
- [ALAB-6380] Users cannot integrate and save the external provider for Sagemaker
- [ALAB-6381] Users cannot validate external prompt created using Sagemaker
- [ALAB-6383] Synthetic tasks aren't generated with valid credentials
- [ALAB-6385] Regions are not visible in Visual NER Project
- [ALAB-6386] "Select LLM Response Provider" page cannot be used if user deletes external service provider from Integration Page
- [ALAB-6388] "Something went wrong" when users navigate to Rules Page
- [ALAB-6391] Users cannot create "LLM Evaluation" and LLM Evaluation Comparison" projects
- [ALAB-6392] Data not populated in Inter Annotator Agreement tab in Analytics Page

### Tasks
- [ALAB-6301] Fetch AWS credentials for floating/payg license using LV instead of using license server
- [ALAB-6333] Track import task status while importing tasks from import_tasks server
- [ALAB-6339] Update import_tasks script to read one file at a time
- [ALAB-6358] UI: LLM question pre-annotation comparison 
- [ALAB-6387] Update the URL for open-source models.json
- [ALAB-6390] Fix issue with active learning build due to apt repository

</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}