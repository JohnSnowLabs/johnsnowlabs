---
layout: docs
comment: no
header: true
seotitle: Release Notes | John Snow Labs
title: Release Notes
permalink: /docs/en/alab/release_notes
key: docs-training
modify_date: "2025-09-10"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## Generative AI Lab 7.4: Chunk Comments, XML Tooltips, Prompt Imports, Analytics, Claude Support
<p style="text-align:center;">Release date: 09-10-2025</p>

We’re excited to announce the release of Generative AI Lab 7.4, a version focused on improving usability, flexibility, and evaluation workflows for LLM projects. This update brings significant enhancements such as long-form chunk-level comments for LLM evaluation annotations, real-time tooltips for XML creation, and expanded LLM integration options.

Alongside these major updates, we’ve introduced improvements to analytics, simplified prompt import workflows, and added support for Claude across all key features. Usability has been further refined with better project configuration, user filtering in analytics, and external ID support for users.

This release also includes numerous bug fixes to ensure smoother workflows, stronger stability, and more consistent performance across annotation, evaluation, and integration processes.

## Support Long-form Comments at Chunk-Level for LLM Evaluation Annotations 

**What’s New:**  

Generative AI Lab 7.4 introduces support for **long-form, chunk-level comments** in LLM evaluation and comparison projects. Users can now add dedicated, long-form comments to each annotation span in LLM evaluation projects, separate from the existing meta field. These comments provide detailed explanations for labels such as "hallucinations" and other NER-style annotations  

**Technical Implementation:**  

- Each annotation span has its own comment field, separate from the meta field.
- Comments support long-form input for detailed notes, for example, facts, contradictions, or references.
- Accessible via the annotation widget — appears when a chunk is clicked or labeled.
- Comments are saved with the chunk’s annotation data; they do not change existing
meta logic.
- Supported for both **HyperTextLabels** and **Labels**.
- Annotation widget resized to fill the full vertical space; when relations exist, space
is split 60/40 between NER spans and relations.

![740image](/assets/images/annotation_lab/7.4.0/1.png)

**User Benefits**

- **Reliable data export** – Comments are included in the JSON output as text and as key value metadata, so downstream systems receive complete information.
- **Seamless commenting experience** – Users can add and view chunk-level comments directly in the annotation workflow.
- **No migration worries** – Older annotations remain fully compatible, so existing work is preserved without extra effort.
- **Improved usability** – The annotation widget automatically adjusts its size to provide the best experience, whether relation annotations are present or not.  

**Example Use Case:**  

During evaluation, a user labels a text span as a "hallucination" and adds a detailed comment explaining why it is factually incorrect, providing context for future reviewers and model fine-tuning.  

## Add Tag-Level Tooltip During XML Creation in Customize Label Page

**What’s New:**

Users now receive **real-time tag-level tooltips** while creating XML configurations in the **Customize Label** page. These tooltips provide clear descriptions and value suggestions for each tag, making XML creation more accurate and efficient.

**Technical Implementation:**
-   Tooltip appears dynamically as the user types a tag during XML creation.  
-   Tooltip content includes:
    -   Description of the tag   
    -   Expected attributes (if any)  
-   Implemented for all supported tags and attributes in the Customize Label page.

![740image](/assets/images/annotation_lab/7.4.0/2.png)

**User Benefits:**

-   **New Users:** Understand tag semantics easily, reducing the learning curve and setup errors.
-   **Experienced Users:** Speed up XML configuration with real-time guidance and attribute suggestions.

**Example Use Case:**

A team setting up custom XML configurations for their project can now view **tooltips** for each tag, ensuring correct attribute usage and minimizing errors during the configuration process.

![740image](/assets/images/annotation_lab/7.4.0/3.gif)

## Improvements

### LLM Evaluation Improvements:

### **Enable Users to Add LLMs from Configuration Page and Request Admin Approval**

**What’s New:**

Users can now add LLMs from the Configuration page and submit a request for admin approval to use those models for response generation. Once an approval is granted, the selected LLM appears as a selectable option wherever responses are generated, and administrators can revoke that permission at any time without affecting other models. In addition, ADHOC providers created by users are now listed on the Configuration page, improving visibility and making provider management easier.

**Technical Implementation:**
-   All available LLMs are listed on the Configuration and Integration page.    
-   Users can select an LLM and submit an approval request to the admin.    
-   **Before approval:** 
    - The **Generate Response** button redirects to the setup page.    
-   **After approval:** 
    - The project owner can use the approved LLM to generate responses.    
-   ADHOC providers created by users are included in the LLM list.    
-   Admins can revoke or restore permissions for any LLM.

![740image](/assets/images/annotation_lab/7.4.0/4.gif)

**User Benefits:**
-   **Teams:** Streamlines integrating LLMs and getting admin approval without navigating multiple steps.    
-   **Admins:** Maintains control over LLM usage while allowing flexibility in project setup.
**Example Use Case:**  
A project team can select an LLM from the Configuration page and request approval. After the admin approves, they can start generating responses immediately. This reduces setup delays and improves operational efficiency.
***Notes:***
-   _Users cannot request a revoked LLM_    
-   _Once an LLM is re-approved, it is automatically listed in the project LLM list without requiring a new request._

![740image](/assets/images/annotation_lab/7.4.0/5.gif)

### Enhance Project Configuration Wizard: Skip LLM Setup with Custom LLMs

**What’s New:**

The project configuration wizard for LLM projects now allows users to **skip the LLM configuration step**. By creating a **custom LLM**, users can **customize labels and view analytics** without needing to configure any external LLM service provider.
**Technical Implementation:**
-   The wizard now allows **skipping the LLM configuration step** for LLM projects.    
-   Users can create a **custom LLM** and proceed directly to **label customization and analytics**.

![740image](/assets/images/annotation_lab/7.4.0/6.gif)

**User Benefits:**
-   **Project Teams:** Quickly set up projects and access analytics without relying on external LLMs.    
-   **Annotators:** Start customizing labels immediately and reduce setup time.    
-   **Data Analysts:** View project insights and metrics without waiting for LLM configuration.
**Example Use Case:**
A user setting up an LLM project can create a **custom LLM**, skip the external configuration steps, and immediately **customize labels and view project analytics**.
***Notes:***
_If a user attempts to generate responses without any configured LLM, they will be redirected to the setup page to complete the necessary steps._

![740image](/assets/images/annotation_lab/7.4.0/7.gif)

### Update Analytics in LLM-Based Projects to Support Multiple Ratings, HypertextLabels, and Choices

**What’s New:**

The Analytics page in **LLM-based projects** now supports **multiple rating sections, HypertextLabels, and Choices** within the evaluation block. This provides more **detailed and accurate analytics** for completed evaluations.
**Technical Implementation:**
-   Added support for **multiple rating sections** in evaluation blocks.    
-   HypertextLabels and Choices are now **fully displayed and counted** in analytics.    
-   Updated chart behavior:    
    -   Chart titles are always displayed.        
    -   Subtitles now show _“No data available yet”_ if no data exists.

![740image](/assets/images/annotation_lab/7.4.0/8.gif)

**User Benefits:**
-   **Project Teams:** Can view more detailed and accurate analytics with multiple rating sections.    
-   **Data Analysts:** Better insights into responses with full support for HypertextLabels and Choices.    
-   **Managers/Reviewers:** Clearer visualization of results and improved consistency in the interface.
**Example Use Case:**
A user reviewing an LLM-based project can now analyze multiple ratings, choices, and hypertext labels for each evaluation. This ensures more accurate reporting of team performance and evaluation results.

***Note:***
_All labels, classifications, and ratings defined after the following XML line will be included in the LLM analytics._

```xml
<View orientation="vertical" pretty="true" style="overflow-y: auto;" evaluation_block="true">
```

## Simplified Prompt Import for LLM Evaluation and Comparison Projects

Generative AI Lab 7.4 introduces usability improvements for Large Language Model (LLM) evaluation workflows, making it easier for teams to import prompts in both JSON and CSV formats.

**What’s New:**

Users can now import prompts using a simple JSON or CSV format across all LLM project types, replacing the previously complex JSON structure.

**Technical Implementation:**

- New lightweight JSON schema for prompt import:
```json
{ "text": "Your Prompt Here" }
```

- Supports batch imports via JSON arrays or CSV files:

```json
[
  {"text":"Your Prompt Here"},
  {"text":"Your Another Prompt Here"}
]
```

- Import available for:
	- LLM Evaluation (Text & HTML types)
	- LLM Comparison (Text & HTML types)

- Added ability to download a sample JSON directly from the import page.
- Updated “Import Sample Task” to use real prompts that generate LLM responses.

![740image](/assets/images/annotation_lab/7.4.0/9.gif)

**User Benefits:**

- **Simplified Workflow:** Removes the need for verbose completion-task JSON structures.
- **Cross-Project Consistency:** Same import structure now works for both LLM and Text projects.
- **Faster Onboarding:** Downloadable samples reduce setup errors and accelerate project configuration.
- **Flexible Input Options:** Teams can choose between JSON or CSV depending on workflow preference.

**Example Use Case:**

A research team setting up an LLM Response Comparison project can quickly import 500 test prompts from a CSV file instead of building complex JSON payloads, allowing them to focus on analyzing model quality instead of data formatting.

### Support Claude for all features

**What’s New:**

The application now provides **full support for Claude** across all major features, including:
-   **Synthetic Task Generation**    
-   **External LLM Prompts**
-   **LangTest Augmented Tasks**
This enhancement ensures seamless integration of Claude for multiple workflows, expanding flexibility and choice for users working with LLM-based tasks.
**Technical Implementation:**
-   Added **Claude integration** for generating synthetic tasks.    
-   Enabled **Claude as a provider** for external LLM prompts.    
-   Extended **LangTest pipeline** to support Claude for augmented task generation.
  
**_Synthetic Tasks_**
 ![740image](/assets/images/annotation_lab/7.4.0/10.gif)


**_Exernal Prompt_**
 ![740image](/assets/images/annotation_lab/7.4.0/11.gif)
 
**User Benefits:**
-   **Flexibility:** Users can now select Claude as an alternative LLM for synthetic data generation and task augmentation.    
-   **Consistency:** Claude is supported across all major LLM-related features for a unified experience.
**Example Use Case:**
A user creating synthetic tasks for evaluation can now select Claude as the LLM to generate tasks.

### **Add User Filtering in "Submitted Completions Over Time" Chart**

**What’s New:**  

The **"Submitted Completions Over Time"** chart in the **Team Productivity** section now includes an option to filter submissions by individual users instead of viewing all users collectively.
**User Benefit:**  
Users can analyze team productivity in more detail by filtering data for a specific user, making performance tracking more accurate.
**Technical Implementation:**
-   Added **user filter dropdown** to the chart component in the **Analytics Dashboard**.    
-   Handled UI state management so that when a user is unselected, the chart resets to show data for all users.

![740image](/assets/images/annotation_lab/7.4.0/12.gif)

**Example Use Case:**  
A project manager can now select a single user in the chart to check how many completions that user submitted over time.

### **Add New Field: External ID for Users**

**What’s New:**  

Admins can now add an External ID when creating a user. This field links a Generative AI Lab user to the matching account in an external application.

**User Benefit:**  
Better mapping between Generative AI Lab and external systems, which improves integration and makes user management easier.
**Technical Implementation:**
- The User Creation form includes an External ID field with input validation. The field accepts any string, including special characters, up to 50 characters.

 ![740image](/assets/images/annotation_lab/7.4.0/13.gif)

**Example:**  
An admin creating a new user for an enterprise integration can set the External ID as extemp-1023 to map the Generative AI Lab user with the enterprise HR system.

### Bug Fixes

- **Credentials Not Saved for Project Cloud Export/Import**

	Fixed an issue where S3 credentials were not being persisted for project export/import operations, requiring users to re-enter them each time. Credentials are now stored securely and reused across sessions. Additionally, sensitive credential information is no longer exposed in API payloads, improving security.

- **Save Credentials in Import Project Form**

	Fixed an issue where the Save Credentials option in the Import Project form was not working as expected. Previously, credentials could not be saved and must be re-entered for each import. This functionality now works correctly, allowing credentials to be securely saved and reused.

- **Analytics Discrepancy with Multiple Ground Truth Completions**

	Fixed an issue where the Analytics page did not correctly use the highest-priority user’s submission when multiple ground truth completions existed. Previously, analytics could display results from a lower-priority user instead of the intended highest-priority user. This has been resolved, and analytics now consistently reflect the highest-priority user’s data.

- **Missing Titles in Analytics Charts**

	Fixed an issue where the titles for the “Average edit time” and “Average number of edits per task” charts were displayed even when the charts were empty. These charts are now hidden when no data is available, ensuring a cleaner Analytics view.

- **Triple Dot Menu Inaccessible After User Search**

	Fixed an issue where the triple dot menu (⋮) next to users in the search results was not accessible. This occurred because normal users and users created through security providers were listed in the same category. The system now separates them into their respective categories, ensuring the triple dot menu is fully accessible for normal users after performing a search.

- **'h' Hotkey Assignment Blocked Due to Default Hide Label Shortcut**

	Fixed an issue where the 'h' key could not be assigned as a hotkey in text-based projects because it conflicted with the default “hide labels” shortcut. The system now properly handles such conflicts by either preventing reassignment with a clear message or allowing reassignment if the default shortcut is intentionally overridden.

- **LLM Response Fails to Generate with Invalid Input**

	Resolved a bug where responses failed to generate if the input textbox contained spaces for the "responseName". The system now blocks spaces and only allows valid characters. Also the search bar now remains visible regardless of search results. 

- **Element Name Matching for Labeling in LLM Evaluation and Comparison**

	Fixed an issue where labeling did not work unless the element name matched the expected response name. The system now correctly enforces the required names: This ensures labeling works reliably in both evaluation and comparison workflows.

- **Task ID Not Generated on First Azure Import**

	Fixed an issue where task IDs were not generated during the first import from Azure, causing the import process to fail. Task IDs are now correctly generated on initial imports, ensuring successful project setup from Azure.

- **Optimize API calls to check the deployed pre-annotation servers**

	Fixed an issue where the get_server API was being called on every page, causing unnecessary requests. The API is now called only on the Cluster page, while the Task page uses the new get_model_server API to check for an active Pay-As-You-Go server (has-payg-server). This improves performance and reduces redundant API calls.

- **Cloud Import Fails for Visual NER Projects When Local Import Is Disabled**

	Fixed an issue where users could not import tasks from the cloud for Visual NER projects if local import was disabled in system settings. Cloud import now works correctly regardless of the local import configuration.

- **Revoke Data Missing for LLM Request**

	Fixed an issue where the Revoke section did not display any data, even when items had been revoked. The section now correctly shows all revoked items, ensuring accurate visibility for LLM requests.

- **Server Status Inconsistency and OCR Server Auto-Selection**

	Fixed an issue where the server status appeared as idle on the Cluster page but was incorrectly marked as busy on the Pre-annotation page. Server status now displays consistently across both pages.

	Fixed an OCR server auto-selection issue on the import page. Users can now intentionally choose the OCR server or rely on automatic pre-selection.

- **Empty CSV Exported for De-identified Text**

	Fixed an issue where exporting tasks as CSV for de-identified text resulted in an empty file. Exporting in JSON, CSV, or TSV formats now correctly includes all de-identified task data.

## Versions

</div>

<ul class="pagination owl-carousel pagination_big">
    <li class="active"><a href="annotation_labs_releases/release_notes_7_4_0">7.4.0</a></li>
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