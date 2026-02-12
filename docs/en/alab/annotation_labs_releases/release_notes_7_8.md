---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 7.8
permalink: /docs/en/alab/annotation_labs_releases/release_notes_7_8
key: docs-licensed-release-notes
modify_date: 2026-02-13
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">



## Generative AI Lab 7.8 with HIPAA-Grade Auditability for Human-in-the-Loop Workflows

Generative AI Lab **7.8** release focused on **HIPAA-grade auditability**, stronger platform governance, and a smoother annotation experience across NER, Visual NER, and PDF workflows.

This version introduces the new **Audit Logs Dashboard**, delivering system-wide visibility into user activity, exports, project lifecycle events, and API behavior—helping teams meet compliance requirements while improving security and operational transparency.

Alongside auditing, **7.8** includes multiple usability improvements to Visual Projects, stronger pre-annotation feedback and deployment behavior, enhanced comment navigation for faster review, improved analytics rendering on low-resolution displays, and a wide set of bug fixes across imports, annotation, integrations, and system stability.

## Audit Logs Dashboard
**What's New**

Generative AI Lab 7.8 introduces the **Audit Logs Dashboard**, a HIPAA-compliant, system-wide auditing solution that provides **real-time, granular visibility into all platform activities**. This new dashboard supports compliance requirements, strengthens security posture, and enhances accountability for every action across projects and users.

![78image](../../assets/images/annotation_lab/7.8/1.png)

**Key highlights include:**

- Centralized logging of user actions, data access, modifications, deletions, and exports  
- Intuitive visualizations for anomaly detection, project activity, and export tracking  
- Granular monitoring of user activity within individual projects  
- System-level insights including API usage trends, server response codes, and platform usage heatmaps  
- Flexible filtering and custom dashboards by project, user, date range, and event type  

![78image](../../assets/images/annotation_lab/7.8/2.png)

**Technical Details**

- **Activity Tracking:** Logs all critical system events with timestamps tied to specific users  
- **Data Retention:** Audit log retention is user-configurable to support long-term investigations and compliance
- **Dashboards & Visualizations:** Includes project activity heatmaps, new/deleted project trends, export monitoring, API usage, HTTP status distributions, and user activity tables  
- **Customizable Views:** Filter by project, user, event type, and date range to create tailored audit views  
- **Enablement:** Turn on audit logging globally via **two installer flags**; Elasticsearch backend is automatically provisioned if not already present  

**Steps to Enable During Installation**

1. Run the installer with the audit logs flag:

```bash
./annotationlab-installer.sh --enable-audit-logs
```
2.	The system automatically provisions the necessary backend services (including Elasticsearch) if not already present.

**Steps to Enable During Upgrade**

1.	Run the updater with the audit logs flag:

```bash
./annotationlab-updater.sh --enable-audit-logs
```
2.	Existing services are updated, and audit logging is enabled without affecting existing data or configurations.

**User Benefits**

- **HIPAA Compliance:** Track access to PHI, modifications, and data exports for regulatory readiness  
- **Transparency & Accountability:** Full visibility into user actions across projects and the platform  
- **Faster Troubleshooting:** Quickly identify the root cause of issues or suspicious activity  
- **Data-Driven Insights:** Monitor platform usage, detect anomalies, and optimize resource planning  
- **Flexible & Developer-Friendly:** Easy to enable, customize, and integrate into existing workflows  

**Example Use Case**

A compliance officer can use the **Audit Logs Dashboard** to investigate a spike in project deletions:  
1. Filter by project and date range to identify affected projects  
2. See which user performed each deletion and when  
3. Check for corresponding exports or modifications  
4. Review system-level activity to confirm whether the behavior was expected or anomalous  

This workflow provides **full visibility, accountability, and compliance assurance**, reducing risk and simplifying investigations in regulated healthcare environments.

## Improvements
### Restrict Pipeline Visibility to Originating Project Type
To improve clarity and prevent incompatible pipeline usage, deployed pipelines are now visible only within the project type in which they were originally created and deployed.
Previously, pipelines deployed in one project type (such as NER or Visual NER) were displayed across multiple project types. This could lead to confusion and increase the risk of selecting an incompatible pipeline.
This improvement ensures better project-type consistency and safer pipeline selection.

**Technical Details**
-   Pipeline visibility is now restricted to the project type where the deployment was performed.
-   Cross-project-type pipeline listing has been removed.   
-   The filtering logic is applied consistently across relevant deployment and selection workflows.

![78image](../../assets/images/annotation_lab/7.8/7.png)
Cluster page view for the Preannotation server

![78image](../../assets/images/annotation_lab/7.8/8.png)
Preannotation server available for the Preannotation

**User Benefits**
-   **Improved clarity:** Users see only relevant pipelines for their project type.
-   **Reduced errors:** Prevents accidental selection of incompatible pipelines.
-   **Better consistency:** Maintains clear separation between different project workflows.
-   **Enhanced usability:** Simplifies pipeline selection and management.
    
**Example Use Case**

A user deploys a pipeline in a Visual NER project. When working in an NER project, this pipeline will no longer appear in the pre-annotation selection list, ensuring that only compatible pipelines are available for use.

### Improved Pre-Annotation Pop-Up Behavior During Deployment

**What’s Improved**

In version **7.8**, the pre-annotation experience has been improved to provide clearer and more reliable feedback during deployment. The pre-annotation pop-up now stays open after deployment is triggered, allowing users to continuously track the server startup process.

**Technical Details**

- The pre-annotation pop-up remains visible while the pre-annotation server is initializing, instead of closing immediately after deployment is triggered.
- If the pop-up is manually closed during this process, the **Pre-Annotate** button displays a loading indicator to reflect the ongoing state.
- The button remains interactive and automatically updates once the server is ready, reappearing in its active state to indicate availability.
- UI state handling has been refined to ensure accurate synchronization between deployment progress and user-facing indicators.

![PopupremainOpen](../../assets/images/annotation_lab/7.8/10.gif)

**User Benefits**

- Clear, continuous visibility into pre-annotation deployment status.
- Reduced confusion about whether deployment is still in progress.
- Consistent and accurate UI feedback, even if the pop-up is closed.
- Smoother and more transparent pre-annotation workflow.

**Example Use Case**

A user triggers pre-annotation on a large project and monitors the deployment process. While the server is starting, the pop-up remains open to show progress. If the user closes the pop-up to continue working elsewhere, the **Pre-Annotate** button clearly indicates that deployment is still in progress and updates automatically once the server is ready, ensuring confidence in the system’s state.

### Notify the user when the test is completed or failed in the playground

**What’s Improved**

In version **7.8**, the Playground now provides clear and immediate feedback when a pre-annotation test completes. Users are explicitly notified whether the test succeeded with results, completed without producing results, or failed, removing ambiguity around test outcomes.

**Technical Details**

The Playground has been enhanced to display outcome-based status notifications after a pre-annotation run finishes. The system evaluates the execution result and surfaces a contextual message using standardized visual cues:
- A **green success message** is shown when pre-annotation completes and generates results.
- A **gray informational message** appears when pre-annotation completes successfully, but no results are produced.
- A **red failure message** is displayed when the pre-annotation process fails.

![78image](../../assets/images/annotation_lab/7.8/5.png)

![78image](../../assets/images/annotation_lab/7.8/6.png)

These notifications are shown immediately upon completion and do not alter the existing pre-annotation execution flow or configuration.

**User Benefits**

- Clear visibility into pre-annotation outcomes.
- Faster understanding of whether results were generated or if follow-up action is needed.
- Reduced confusion when a test completes but produces no output.
- Improved confidence and usability when experimenting in the Playground.

**Example Use Case**

A user runs a pre-annotation test in the Playground to validate a model, rule, or Prompt before adding it to a project. Once the test completes, the Playground clearly indicates the outcome—confirming success with generated results, signaling a successful run with no matches, or highlighting a failure—allowing the user to immediately decide whether to proceed, update the test text, or troubleshoot other configurations.

### Improved Comment Navigation for Better Review Context

**What’s Improved**

In version **7.8**, comment navigation has been enhanced to improve context awareness during review. Clicking on a comment now automatically redirects users to the exact location in the task where the comment was originally added.

**Technical Details**

- Comment click behavior has been updated to include positional mapping between comments and their associated content.
- When a comment is selected, the system scrolls to the corresponding section in the task.
- The relevant text or area is brought into view and visually highlighted to clearly indicate the comment’s context.
- This enhancement applies to previously added comments without requiring any data migration or user action.

![Comments](../../assets/images/annotation_lab/7.8/11.gif)

**User Benefits**

- Faster understanding of comment context without manual searching.
- Improved review and collaboration experience.
- Reduced confusion when navigating tasks with multiple comments.
- More intuitive and efficient feedback workflows.

**Example Use Case**

During task review, a user clicks on a comment discussing an issue in a specific section of the document. Instead of manually scrolling to locate the referenced content, the system automatically navigates to and highlights the exact section, allowing the user to immediately understand and act on the feedback.
  
### Analytics Charts Now Render Correctly on Low-Resolution Screens

**What’s Improved**

In version **7.8**, the Analytics dashboard has been improved to ensure charts render correctly on smaller screens. Chart elements that previously overlapped in constrained viewports are now displayed clearly, maintaining readability and visual consistency.

**Technical Details**

The layout and spacing logic for Analytics charts has been refined to better adapt to smaller screen sizes and standard zoom levels. Chart regions, labels, legends, and visual elements now adjust dynamically to the available screen space, preventing overlap and preserving the intended structure of each visualization.

![AnalyticsZoomIn](../../assets/images/annotation_lab/7.8/9.gif)

**User Benefits**

- Clear and readable charts on smaller screens and laptops.
- No overlapping labels, legends, or chart regions at normal zoom levels.
- More reliable analytics viewing without needing manual zoom or window resizing.
- Improved overall usability and visual consistency across devices.

**Example Use Case**

A user reviews analytics on a laptop or a smaller monitor. With the updated responsive behavior, all chart elements are clearly visible and properly spaced, allowing users to interpret analytics and metrics without adjusting the zoom or switching devices.

### Horizontal Scroll Bar in the Visual NER Labeling Page

**What’s Improved**

In version 7.8, navigation for visual documents has been enhanced with the addition of both horizontal and vertical scrollbars. This improvement makes it easier to move through large or high-resolution documents without relying solely on manual repositioning.

**Technical Details**

Visual document viewer in Generative AI Lab now supports native horizontal and vertical scrolling. The scrollbars are enabled automatically for documents that extend beyond the visible viewport, allowing smooth navigation across all directions. This enhancement works alongside existing interaction features and does not change the underlying document rendering or annotation behavior.

![78image](../../assets/images/annotation_lab/7.8/3.gif)

**User Benefits**

- Easier and more intuitive navigation for large or zoomed-in visual documents.
- Reduced reliance on the move or drag-to-position feature.
- Faster access to different areas of a document during review or annotation.
- Improved usability, especially for complex or high-resolution files.

**Example Use Case**

An annotator working on a large visual document, such as a detailed diagram or scanned form, needs to review content across multiple sections on a page. With the newly added horizontal and vertical scrollbars, the annotator can smoothly navigate to any part of the document using standard scrolling, making the review process more efficient and less disruptive.

### New buttons for zoom in/out/drag for image documents

**What’s Improved**

In version 7.8, the interaction controls for visual documents have been refined in Visual Projects. The zoom in, zoom out, and move position buttons have been updated to provide a clearer and more consistent experience when viewing PDF and image-based documents.

**Technical Details**

The document viewer toolbar for Visual Projects has been enhanced with updated controls for zooming and repositioning content. These controls are now more clearly presented and consistently available when working with PDF and image documents. The underlying zoom and pan functionality remains unchanged, ensuring full backward compatibility with existing workflows.

![78image](../../assets/images/annotation_lab/7.8/4.png)

**User Benefits**

- Improved clarity and discoverability of zoom and move controls.
- Smoother interaction when inspecting PDFs and image documents.
- Reduced friction when switching between navigation actions.
- A more polished and consistent viewing experience across Visual Projects.

**Example Use Case**

While reviewing a scanned PDF in a Visual Project, a user frequently zooms in to inspect fine details and repositions the document to continue annotation. With the updated zoom and move controls, these actions are quicker and more intuitive, allowing the user to stay focused on the review task without interruption.
  

## Bug Fixes

### UI & User Experience
- **UI Shift When Renaming Service Provider to an Existing Name**

  In earlier versions, renaming a service provider to an existing name could cause brief UI shifts or visual glitches during validation. The interface now remains stable while validation is in progress and displays a clear toast error message when a duplicate name is detected.

- **Redirect to “Something Went Wrong” Page When Clicking Comments**
  
  An issue was identified where selecting Comments in the Annotation section could trigger an unintended redirect to a “Something went wrong” page. This behavior has been corrected, and comments can now be accessed reliably without unexpected navigation.

- **Unable to View Classification and Comments for Previously Annotated Chunks**
  
  In some previously configured projects, classifications and comments were not displayed correctly for already annotated chunks. This behavior has been corrected.
  
  In addition, validation and UI behavior have been strengthened through improved project configuration enforcement:

  **Required Field Validation**
  
  - If a classification or NER field is configured as required, the UI now correctly enforces it.
  - Required annotations now properly validate associated required fields, such as comments.

  **Conditional / Dependent Fields**
  
  - Fields that depend on earlier selections are now enforced correctly.
  - Follow-up fields become mandatory only when the preceding field is filled.

- **Pagination Not Visible for Long Tasks in Comparison and De-Identification Views**

   Under certain conditions, pagination controls were not visible for longer tasks in the Comparison view and were inconsistently displayed in the De-Identification view. Pagination is now consistently rendered and functions correctly in both views.

- **Rating Tooltip Not Available Beyond 5 Stars in Rate PDF Projects**

   When Rate PDF projects were configured with more than five stars, rating tooltips were not displayed as expected. This behavior has been corrected. New Rate PDF projects now default to a five-star configuration, ensuring consistent tooltip behavior.

- **Button Flicker After Re-Deploying Pre-Annotation Server**

   A visual flicker could occur on the deploy/pre-annotation button after re-deploying the pre-annotation server in NER projects. This issue has been corrected. The button now remains visually stable and accurately reflects the current deployment state.

### Annotation, Models & Pre-Annotation
-  **Slow pre-annotation using NER, rules, and prompts**

   Performance degradation was observed when running pre-annotation using a combination of NER models, rules, and prompts. Pre-annotation execution has been optimized and now processes tasks more efficiently with improved responsiveness.

-  **Multi-line annotation inconsistencies**

   In certain scenarios, multi-line annotations did not behave as expected. Automatic clicks no longer expand existing annotations incorrectly, and multiple selections no longer result in inactive grey/red regions. Multi-line annotation behavior has been corrected and now operates reliably.

-  **Token highlighted instead of full span in PDF projects**

   In PDF projects, annotations previously highlighted individual tokens rather than the full annotated span. Full spans are now highlighted correctly during annotation and review.

-  **Pre-annotation server deployment failure for checkbox and handwritten projects**

   Deployment failures could occur when starting pre-annotation servers for Checkbox Detection and Handwriting projects. These deployment issues have been resolved, and servers now deploy successfully and support pre-annotation as expected.

-  **Pre-annotation button missing task count**

   The Pre-Annotation button did not consistently display the number of tasks being processed during execution. Task count information is now displayed correctly.

-  **Annotation blocked in PDF+Text projects when “label all occurrences” is enabled**

   When the “Label All Occurrences” option was enabled, annotation actions could be blocked in PDF+Text projects. This behavior has been corrected, and annotation now functions correctly with this option enabled.

### PDF, OCR & Imports
- **PDF Files Incorrectly Importable into Audio and Video Projects**

   The system previously allowed PDF files to be imported into Audio and Video project types, which are intended to support only audio or video inputs. The OCR import option has been removed for Audio and Video projects, preventing PDF files from being imported into unsupported project types.

- **Error During PDF Import via Cloud for Text-Based Projects**

   Importing PDF files from cloud sources in text-based projects could result in an unexpected “Something went wrong” error. Users can now successfully import cloud-based PDF files into NER projects without unexpected errors or redirection.

- **Mixed PDF (Image and Text) Not Supported in Text-Based Projects**

   Mixed PDFs containing both image-based and text-based content could cause import failures in text-based projects. Mixed PDFs are now handled correctly, and imports complete without errors.
  
- **Cloud Credentials Not Saved or Updated During PDF Import in NER Projects**

   Cloud credentials provided during PDF import were not always saved or refreshed, resulting in outdated credentials being reused. Cloud credentials are now saved and refreshed correctly, and the import process uses the most recently provided credentials.
  
- **OCR Server Field Not Auto-Refreshing on Import Page**

   The OCR Server field on the Import page did not automatically refresh when the server became ready, requiring a manual page reload. The Import page now updates automatically to reflect server readiness.
  
- **Unable to Import OCR Documents in NER Projects**

   OCR documents could not be imported into NER projects under certain conditions. OCR documents can now be imported successfully through both local and cloud imports, and PDF imports function as expected without errors.

### Analytics, Integrations & System Stability
- **Annotator Comparison Chart Not Working in Visual NER**

   In Visual NER projects, the annotator comparison chart did not consistently load or render data correctly.

- **Blind evaluation choices are editable without new completion**

   Submitted completions in Blind Evaluation projects could be edited using keyboard shortcuts without creating a new completion. This behavior has been restricted. A new completion is now required before edits can be made.

- **Task imports allowed during ongoing import after refresh**

   Refreshing the page during an active import could allow additional imports to be initiated concurrently. Import actions now remain disabled until the current process completes.

- **Chart update errors in Generative AI Lab logs**

   During Analytics Dashboard refresh operations, “Couldn’t update chart” messages were observed in the Annotation Lab pod logs. Chart data now updates correctly without generating system errors.

- **LLM response not generated with special characters in response name**

   LLM responses failed to generate when response names contained supported special characters. This limitation has been removed, and responses are now generated successfully regardless of supported character usage.

- **Deletion of integrated external service providers is not restricted**

   Integrated external service providers could previously be deleted without sufficient validation. Deletion behavior has been restricted to prevent unintended configuration loss.

- **Synthetic task generation fails with integrated LLM providers**

   Synthetic task generation could fail when using integrated LLM providers. This behavior has been corrected, and synthetic tasks are now generated reliably across supported providers.

-  **Persistent “Cannot Delete Provider” message on Integration page**

   The “Cannot Delete Provider” message could persist when navigating the Integration page, even when no deletion error was present. This message is no longer displayed incorrectly.

-  **License-related error after open-source training completion**

   License-related errors appeared in training server logs after open-source model training completed. License validation is no longer triggered for open-source training workflows.

-  **OIDC/SAML configuration issues after restore**

   After system restore, OIDC/SAML authentication could redirect users to profile update flows instead of completing login. Authentication behavior has been corrected, and users are now logged in correctly after restore.

-  **Internal server error when viewing cluster logs**

   Accessing cluster logs could result in internal server errors under certain conditions. Cluster logs are now accessible reliably without system failures.

---
## Versions

</div>

{%- include docs-annotation-pagination.html -%}
