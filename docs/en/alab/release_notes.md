---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Release Notes
permalink: /docs/en/alab/release_notes
key: docs-training
modify_date: "2026-05-19"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">



## Generative AI Lab 8.1: Custom LLM Integration and Next-Generation Multi-Tab Analytics Dashboard

Generative AI Lab 8.1 introduces major enhancements focused on analytics visibility, custom LLM integration, annotation workflow efficiency, and healthcare terminology management.

The headline feature of this release is the redesigned multi-tab Analytics Dashboard, which provides project managers and annotation teams with a more scalable and structured way to monitor project progress, team productivity, annotation quality, inter-annotator agreement, and LLM evaluation metrics. The new analytics experience improves discoverability and navigation by organizing operational insights into dedicated dashboard sections and contextual tabs.

Version 8.1 also introduces Custom LLM Integration support, enabling organizations to connect external, private, or self-hosted Large Language Models directly into Generative AI Lab workflows. Teams can now use organization-specific models alongside supported providers across evaluation, annotation, response comparison, and synthetic task generation workflows.

In addition, this release delivers multiple usability and workflow improvements across Visual NER, annotation management, relation extraction, and Medical Terminology workflows. Enhancements such as Zero-Shot prompt support for Visual NER De-Identification projects, improved annotation workspace responsiveness, faster terminology lookup performance, and safer Medical Terminology management further improve operational efficiency across enterprise annotation projects.

Together, these updates improve scalability, analytics visibility, workflow flexibility, and overall annotation efficiency across complex AI and healthcare data workflows.


## Redesigned Multi-Tab Analytics Dashboard

Version **8.1** introduces a completely redesigned **Analytics Dashboard** experience for Generative AI Lab, providing project managers, reviewers, and annotation teams with a centralized and scalable interface for monitoring project activity, productivity, annotation quality, and inter-annotator agreement.

Previously, analytics charts, tables, and metrics were displayed together within a single scrolling page, which could become difficult to navigate as projects increased in size and complexity. The new analytics experience reorganizes reporting capabilities into structured analytics pages with dynamic horizontal tabs, allowing users to quickly locate relevant insights without excessive scrolling or manual filtering.

![Redesigned Analytics Dashboard with multi-tab navigation](/assets/images/annotation_lab/8.1.0/5.gif)
*<center>The redesigned Analytics Dashboard organizes operational insights into dedicated analytics sections and contextual tabs, improving navigation and scalability across large annotation projects.</center>*

The redesigned dashboard introduces dedicated sections for:

- Project overview and task monitoring
- Label distribution and data quality analysis
- Team productivity and review statistics
- Inter-Annotator Agreement (IAA) analysis
- LLM response comparison analytics

This update significantly improves discoverability, navigation efficiency, scalability, and overall usability across large annotation projects.

*<center>The redesigned Analytics Dashboard introduces a multi-tab navigation experience that organizes project insights into dedicated analytics sections for improved visibility and usability.</center>*

## Technical Details

### Navigation Architecture

The Analytics module now uses a hierarchical navigation structure integrated directly within the project sidebar:

- Projects → Project Name → Analytics
- Expandable analytics categories
- Collapsible sidebar navigation
- Dynamic horizontal tabs that change based on selected analytics page

The following analytics pages are now available:

- **Overview**
- **Labels & Data Quality**
- **Team Productivity**
- **Inter-Annotator Agreement**
- **LLM Response Comparison**

Each analytics page includes dedicated tab groups optimized for the selected analytics workflow.

![Analytics sidebar navigation and dashboard structure](/assets/images/annotation_lab/8.1.0/6.png)
*<center>The Analytics sidebar provides structured navigation across multiple analytics categories, enabling faster access to project insights and operational metrics.</center>*

### Global Dashboard UI Improvements

The Analytics Dashboard UI has been refined to provide a cleaner and more consistent visual experience across all analytics pages.

#### UI and Styling Improvements
- Dashboard typography now uses the **Inter** font family for improved readability and consistency.
- Borders and shadows have been removed from chart containers to provide a cleaner and more minimal interface.
- Chart heights have been reduced to improve dashboard density and reduce unnecessary scrolling.

#### Layout and Responsiveness
- Grid alignment and spacing have been standardized across all analytics dashboards.
- Controls, titles, and charts now maintain consistent spacing and alignment.
- Inline filters and controls have been optimized to prevent layout wrapping issues.
- Scroll behavior has been improved to ensure dashboards remain responsive across different viewport sizes.

#### Analytics Header Cleanup
- The visible **Last updated** and **Updated by** labels have been removed from analytics headers to reduce UI clutter.
- Underlying update metadata is still retained internally and is now displayed through hover tooltips on the **Update Analytics** button.

#### Interactive Chart Range Slider
  Charts with large datasets now support an interactive range slider that allows users to define visible x-axis ranges dynamically. This improves readability and navigation when analyzing high-volume datasets.

![Interactive analytics chart range slider](/assets/images/annotation_lab/8.1.0/7.gif)
*<center>Interactive range sliders allow users to dynamically focus on specific subsets of analytics data, improving readability and navigation across large datasets.</center>*

### Overview Dashboard Redesign

The **Overview** page has been redesigned to provide analytics data at a glance across:
- Task Summary
- Productivity
- Inter-Annotator Agreement

The page now acts as a centralized high-level project analytics view for project managers and reviewers.

![Overview analytics dashboard with KPI widgets and operational insights](/assets/images/annotation_lab/8.1.0/8.gif)
*<center>The redesigned Overview dashboard centralizes KPI widgets, productivity metrics, and inter-annotator agreement insights into a unified operational analytics experience.</center>*

#### Task Summary Section

The Task Summary section includes multiple KPI cards and status visualizations designed to provide quick operational visibility.

##### KPI Cards
The following KPI widgets are available:

- **Total Tasks**
  Displays the total number of imported tasks along with a side indicator showing the number of tasks imported within the last 30 days.

- **Completion Rate**
  Displays the percentage of submitted tasks relative to all imported tasks.

- **Reviewed Rate**
  Displays the percentage of reviewed tasks relative to all submitted tasks.

- **Total Completions**
  Displays the total number of submitted completions across all annotators.
  
  Additional side indicators display:
  - Number of starred completions
  - Number of draft completions
  
  A time-period filter allows users to analyze completion data across different time ranges.

*<center>The Overview dashboard provides centralized visibility into task progress, completion activity, and annotation performance through consolidated KPI widgets and operational charts.</center>*

#### Productivity Section

The Productivity tab includes:
- Submitted completions timeline analytics
- Average task length analysis by annotator

#### Inter-Annotator Agreement Section

The Inter-Annotator Agreement section includes:
- Annotator comparison dropdown filters
- Entity type selection
- NER and Assertion agreement analysis
- Chunk-level agreement comparison charts

*<center>The Overview dashboard consolidates project KPIs, productivity insights, and inter-annotator agreement metrics into a unified analytics experience.</center>*

### Labels & Data Quality Dashboard

A dedicated **Labels & Data Quality** page has been added to support annotation quality analysis and label distribution monitoring.

#### Label Frequency Analytics
The Label Frequency section includes:
- Ground Truth completion-based calculations
- Label distribution visualizations
- Team-level label frequency analysis

#### Label Variability Analytics
The Label Variability section includes:
- Total vs distinct value analysis
- Average token distribution per label
- Variability tracking across annotations

*<center>The Labels & Data Quality page provides dedicated analytics for label distribution, variability analysis, and annotation consistency monitoring.</center>*

### Team Productivity Dashboard

The **Team Productivity** page organizes productivity analytics into dedicated tabs:

- Completions
- Time Metrics
- Review

![Team Productivity analytics dashboard with completion and review metrics](/assets/images/annotation_lab/8.1.0/9.png)
*<center>The Team Productivity dashboard organizes completion trends, review analytics, and time-based productivity metrics into dedicated tabs for improved operational visibility.</center>*

#### Completions Tab
The dashboard now focuses primarily on completion trend analysis.

The following items were removed from this tab to reduce duplication:
- Total Completions widget row
- Completions by Status chart
- Time Period selector

#### Review Metrics
The Review section includes:
- Average tokens for submitted and reviewed tasks
- Average reviews per annotator
- Submitted vs reviewed task ratios
- Total tokens across submitted and reviewed tasks

#### Time Metrics
The Time Metrics section includes:
- Average time spent per task
- Average edit time per task
- Average number of edits per task

*<center>The Team Productivity page provides structured visibility into annotation throughput, editing activity, and review efficiency across teams.</center>*

### Inter-Annotator Agreement Dashboard

The **Inter-Annotator Agreement** dashboard has been redesigned into dedicated analytical sections for agreement analysis.

![Inter-Annotator Agreement dashboard with chunk-level comparison analytics](/assets/images/annotation_lab/8.1.0/10.png)
*<center>The redesigned Inter-Annotator Agreement dashboard provides detailed agreement analysis, chunk-level comparison metrics, and disagreement tracking across annotation teams.</center>*

#### Overview Tab
The Overview tab includes:
- Annotator comparison filters
- Entity type selection
- NER and Assertion agreement metrics
- Chunk-level agreement visualization
- Detailed agreement tables for common tasks

#### Chunk Level Analysis
The section includes:
- Chunk extraction tables by annotator
- Chunk frequency analysis
- Label-based chunk cross-reference tables

*<center>The redesigned Inter-Annotator Agreement dashboard enables detailed comparison of annotator agreement, disagreement trends, and chunk-level analysis.</center>*

### LLM Response Comparison Dashboard

The **LLM Response Comparison** dashboard has been redesigned with a dedicated tabbed analytics experience optimized for LLM evaluation workflows.

The dashboard now includes the following dynamic tabs:

- **LLM Choices**
- **Labels**
- **Quality Ratings**

The active tab is highlighted visually, and switching tabs updates dashboard content dynamically without requiring page reloads.

![LLM Response Comparison dashboard with LLM choice analytics](/assets/images/annotation_lab/8.1.0/11.png)
*<center>The LLM Choices tab visualizes annotator preferences across multiple LLM responses through result summaries and provider selection frequency analytics.</center>*

#### LLM Choices Tab
The LLM Choices tab includes:

##### Result Summary
- Donut chart visualization showing the percentage distribution of selected LLM responses based on annotator selections.

##### Choice Frequency by Annotator
- Dynamic bar chart showing:
  
  > {LLM Name} – Choice Frequency by Annotator

- Includes an LLM selector dropdown populated dynamically from configured project LLMs.
- The chart updates automatically when a different LLM is selected.

#### Labels Insights Tab
The Labels Insights tab consolidates all label-related charts into a dedicated section.

![LLM label insights analytics dashboard](/assets/images/annotation_lab/8.1.0/12.png)
*<center>The Label Insights tab centralizes label-based evaluation analytics, enabling comparison of hallucination patterns, citation issues, and response quality indicators across LLM providers.</center>*

#### Quality Score Tab
The Quality Score tab groups all quality rating analytics into a dedicated section.

![LLM quality score analytics dashboard](/assets/images/annotation_lab/8.1.0/13.png)
*<center>The Quality Scores tab provides structured analytics for reference quality, coherence, relevance, and coverage ratings across evaluated LLM providers.</center>*

## User Benefits

- **Improved Analytics Discoverability**
  Quickly locate relevant charts, KPIs, and tables through structured navigation and contextual tabs.

- **Better Scalability for Large Projects**
  Organized dashboard sections reduce clutter and improve usability for projects with extensive analytics data.

- **Cleaner and More Focused UI**
  Reduced chart clutter, standardized layouts, and simplified dashboards improve readability and reduce cognitive overhead.

- **Faster Decision-Making**
  Centralized analytics and interactive filtering provide quicker access to operational insights and quality metrics.

- **Enhanced Annotation Oversight**
  Monitor project progress, team productivity, review activity, and inter-annotator agreement from a unified interface.

- **Improved Quality Analysis**
  Dedicated data quality and agreement sections enable better identification of annotation inconsistencies and disagreement patterns.

- **Optimized LLM Evaluation Workflows**
  Specialized analytics for LLM-comparison projects provide structured visibility into model evaluation trends.

- **More Efficient Navigation**
  Multi-tab navigation eliminates excessive scrolling and improves movement between analytics categories.

- **Improved Responsiveness**
  Standardized layouts and responsive controls improve usability across different screen sizes and dashboard configurations.


## Example Use Case

A project manager overseeing a large healthcare annotation project opens the redesigned Analytics Dashboard to review project progress.

Using the new sidebar navigation, the manager switches between:
- **Overview** to monitor task completion and submission trends
- **Team Productivity** to identify annotator throughput and review performance
- **Labels & Data Quality** to analyze label imbalance and annotation consistency
- **Inter-Annotator Agreement** to investigate disagreement patterns between reviewers
- **LLM Response Comparison** to evaluate annotator preferences across multiple LLM responses

Instead of scrolling through a single analytics page, the manager can quickly navigate through dedicated tabs and filtered views to locate specific operational insights. This enables faster decision-making, improved project oversight, and more efficient quality management across large annotation teams.


## Custom LLM Integration: Connect Private and Self-Hosted Models
Generative AI Lab now supports **Custom LLM Integration**, allowing organizations to connect and use their own external or locally hosted Large Language Models within the platform. Teams can add organization-specific models alongside existing supported providers and use them across evaluation, annotation, response comparison, synthetic task generation, and external prompt workflows.

Custom LLMs can be configured directly within the platform using options such as **Authentication Scripts**, **Custom Credentials**, **Temperature**, and **Maximum Tokens**.

![Custom LLM integration via Integration Page](/assets/images/annotation_lab/8.1.0/1.gif)
*<center>Users can configure and connect custom external or self-hosted LLM providers directly within Generative AI Lab, enabling organization-specific models to be integrated into annotation and evaluation workflows.</center>*

![Custom LLM selection during project configuration](/assets/images/annotation_lab/8.1.0/2.gif)
*<center>Custom LLM providers can be selected alongside supported providers during project setup, allowing teams to include organization-specific models in evaluation and response comparison workflows.</center>*

### Technical Details

**Custom LLM Configuration:** 
A new **Add Custom LLM** option is available within the **Integration** and **Project Settings** sections, allowing users to configure custom LLM endpoints directly from the UI.

**Supported Configuration Fields:** 
Users can configure:
-   Model Name
-   Base URL / Endpoint
-   API Key or Authentication Token
-   Optional parameters such as Temperature and Maximum Tokens

**Proxy-Based Routing & Connection Validation:** 
All LLM requests are routed through a centralized proxy server to ensure secure and standardized communication across providers. The proxy server is responsible for authentication handling, API key management, request logging, rate limiting, and request/response normalization.
Before saving the configuration, the system validates connectivity through the proxy server. If an endpoint is invalid or authentication fails, users are shown clear error messages to help identify and resolve connection issues quickly.

**Project- and User-Level Scope:** Custom LLMs can be configured at either the project or user level

**Permissions & Access Control:** Only users with **Admin** or **Supervisor** roles can add, edit, or delete Custom LLM configurations. Regular users can use approved models within projects but cannot modify configurations.

**Multi-Model Support:** Projects can reference multiple LLMs simultaneously, including both default integrated providers and organization-specific custom models.

**Supported Workflows:** 
Custom LLMs are available alongside existing integrated providers in:
-   LLM Evaluation
-   Response Comparison
-   Annotation Workflows
-   Synthetic Task Generation
-   External Prompt Workflows


![Generating response using Custom LLM for LLM Evaluation](/assets/images/annotation_lab/8.1.0/3.gif)
*<center>Custom LLMs can generate responses directly within LLM evaluation workflows, enabling side-by-side comparison between private models and integrated providers.</center>*

![Custom LLM used in External prompt](/assets/images/annotation_lab/8.1.0/4.gif)
*<center>External prompt workflows support custom LLM providers, allowing teams to generate and evaluate responses using organization-specific models within the same interface.</center>*


### User Benefits

**Bring Your Own Models:** Use organization-specific, private, or self-hosted LLMs directly within Generative AI Lab alongside existing supported providers.

**Centralized & Secure Management:** Configure and manage external LLM connections from a single interface while securely handling credentials and model communication through centralized proxy routing.

**Flexible Multi-Model Workflows:** Use multiple custom and integrated LLMs across evaluation, annotation, comparison, synthetic task generation, and response generation workflows within the same project.

**Reduced Operational Overhead:** Simplify external LLM integration and management without requiring additional infrastructure configuration or disconnected tooling.
  
### Example Use Case
An enterprise AI team wants to evaluate responses generated from an internally hosted healthcare LLM alongside OpenAI and Claude models.

A Project Admin adds the organization’s private LLM endpoint through the **Add Custom LLM** configuration page, validates the connection, and enables the model for the project. Annotators and reviewers can then use the custom model alongside other providers during evaluation and comparison workflows without requiring direct access to external infrastructure or credentials.


## Improvements

### Zero-Shot Prompt Support for Visual NER De-Identification
**What's Improved**
Visual NER De-Identification projects now support **Zero-Shot prompts** during project configuration and pre-annotation workflows. Previously, users were unable to use Zero-Shot prompts within the Visual NER De-Identification flow, limiting prompt-based entity detection capabilities for visual documents.

This improvement enables users to configure and use JSL-based Zero-Shot prompts seamlessly alongside Visual NER De-Identification pipelines for images and PDFs.

![Zero-shot prompt support for Visual NER de-identification projects](/assets/images/annotation_lab/8.1.0/14.gif)
*<center>Visual NER De-Identification projects now support Zero-Shot prompts during configuration and pre-annotation workflows for image and PDF-based tasks.</center>*

**Technical Details**
-   Enabled compatibility with **Zero Shot Prompt** during project configuration and pre-annotation.
-   Zero-Shot prompts can now be used with both **image** and **PDF-based** Visual NER De-Identification projects.
-   Improved validation and workflow handling to support prompt-based entity extraction within the Visual NER pipeline.

**User Benefits**
-   **Expanded Prompt Support** – Users can now use Zero-Shot prompts in Visual NER De-Identification projects.
-   **Improved Flexibility** – Supports prompt-based entity detection alongside existing de-identification workflows.
-   **Better Workflow Consistency** – Aligns Visual NER De-Identification capabilities with other supported NER workflows.

**Example Use Case**
A healthcare team creates a Visual NER De-Identification project for scanned medical documents and configures a Zero-Shot prompt to identify patient names. During pre-annotation, the system successfully applies the prompt and detects sensitive entities directly from images and PDFs.


### Performance Gains for Annotation and Visual NER Workflows
**What's Improved**
Generative AI Lab introduces performance improvements for terminology lookup and Visual NER annotation workflows. Initial terminology lookup during manual annotation is now significantly faster, and Visual NER projects now handle repeated zoom interactions more reliably without freezing or hiding task content.

These enhancements provide a smoother and more responsive annotation experience, especially for healthcare and document-heavy workflows.

![Faster terminology lookup during annotation](/assets/images/annotation_lab/8.1.0/19.gif)
*<center>Terminology datasets are now preloaded during deployment, significantly improving the speed of initial manual terminology lookup actions.</center>*

**Technical Details**
-   Lookup datasets are preloaded during **Terminology Server deployment** based on project configuration.
-   Improved initialization handling reduces delays during the first manual lookup action.
-   Enhanced zoom handling and rendering stability in Visual NER projects and fixed issues causing task content to disappear or the annotation page to freeze during repeated zoom actions.

**User Benefits**
-   **Faster terminology lookup** during annotation.
-   **More stable Visual NER interaction** during zoom operations.
-   **Improved responsiveness** for image and document-based annotation workflows.

**Example Use Case**
A healthcare annotator reviewing a Visual NER task can quickly perform terminology lookups while repeatedly zooming into document regions without experiencing startup delays, UI freezes, or disappearing task content.


### Smart UI Components for Improved Annotation Workspace
**What's Improved**
Generative AI Lab introduces multiple UI improvements to create a more responsive and efficient annotation workspace. The Meta section on the right-side panel now dynamically adjusts when users resize the Annotation widget, while the Regions and Relations side panel now supports expandable and collapsible views for smaller screens.

Previously, resizing annotation panels could leave excessive blank space in the Meta section, and only a limited number of relations were visible on smaller displays. These enhancements improve layout consistency, space utilization, and navigation when working with large annotation and relation sets.

![Expandable Regions and Relations side panel](/assets/images/annotation_lab/8.1.0/15.gif)
*<center>The Regions and Relations side panel now supports expandable and collapsible views, improving visibility and navigation for large annotation sets.</center>*


![Dynamic Meta section resizing during annotation](/assets/images/annotation_lab/8.1.0/16.gif)
*<center>The Meta section dynamically adjusts based on annotation panel resizing, improving layout balance and reducing unused screen space.</center>*

**Technical Details**
-   Added dynamic resizing behavior for the **Meta** section based on Annotation widget size changes.
-   Automatically adjusts Meta section height and positioning to reduce unused blank space.
-   Added expand and collapse functionality for the **Regions and Relations** side panel.
-   Expanded view supports scrolling through large relation and region lists on smaller screens.
-   Improved overall layout responsiveness and usability for annotation projects with large numbers of annotations and relations.

**User Benefits**
-   **Improved Layout Consistency** – Maintains a cleaner and more balanced annotation interface.
-   **Better Space Utilization** – Dynamically uses available screen space more efficiently.
-   **Enhanced Visibility** – Allows users to view more relations and regions on smaller screens.
-   **Improved Navigation** – Easier scrolling and review of large annotation and relation lists.
-   **Responsive Annotation Workspace** – Provides a more responsive and efficient annotation experience across complex annotation workflows.

**Example Use Case**

A reviewer working on a laptop expands the Annotation panel while reviewing a task with multiple entity relations. The Meta section automatically resizes to fit the available space, while the expandable Relations panel allows the reviewer to scroll through longer relation lists without affecting the main annotation area.


### Bulk Management for Relations
**What's Improved**
Generative AI Lab introduces new bulk management controls for Relations, making it easier to review and manage large relation sets during annotation workflows. Users can now delete all relations in a single action or hide specific relations individually for a cleaner and more focused review experience.

Previously, relations had to be deleted one by one, and users could only hide all relations at once. These improvements reduce manual cleanup effort and provide more granular visibility control when working with large or overlapping relation sets.

![Bulk relation deletion workflow](/assets/images/annotation_lab/8.1.0/17.gif)
*<center>Users can now remove all relations in a single action, simplifying cleanup of incorrect or unnecessary relation sets.</center>*

![Individual relation visibility controls](/assets/images/annotation_lab/8.1.0/18.gif)
*<center>Specific relations can now be hidden individually, allowing annotators to focus on relevant connections without hiding the entire relation set.</center>*



**Technical Details**
-   Added a **Delete All Relations** action with confirmation before deletion.
-   Added an individual **Hide** option for each relation. Users can now hide selected relations without affecting other visible relations.
-   Existing **Hide All** functionality remains supported.

**User Benefits**
-   **Faster cleanup** of incorrect or unnecessary relations.
-   **Improved visibility control** during relation review.
-   **More efficient annotation workflow** when working with large relation sets.

**Example Use Case**
An annotator reviewing a task with many overlapping relations can quickly remove all incorrect relations or hide only selected ones to focus on the most relevant connections.


### Medical Terminology Workflow Improvements

**What's Improved**

Version 8.1 introduces several usability improvements for Medical Terminology configuration and management workflows.

* **Terminology UX:** Added proper display names for Medical Terminology databases across the Project Configuration and Medical Terminology pages, replacing previously displayed raw database identifiers for improved readability and usability.

![Improved Medical Terminology display names](/assets/images/annotation_lab/8.1.0/20.png)
*<center>Medical Terminology databases now display user-friendly names across configuration and terminology management workflows.</center>*

* **Delete Confirmation for Medical Terminologies:** Added a confirmation pop-up when deleting Medical Terminologies to help prevent accidental deletions. Users are now prompted to confirm or cancel the delete action before the terminology is removed.

![Delete confirmation dialog for Medical Terminologies](/assets/images/annotation_lab/8.1.0/21.png)
*<center>A confirmation dialog is now displayed before deleting Medical Terminologies, helping prevent accidental removal of terminology resources.</center>*


## Bug Fixes
### Critical Bug Fixes & Stability

- **Users Redirected to “Something Went Wrong” Page During Login**

  Login attempts could unexpectedly redirect users to the “Something Went Wrong” page, preventing successful authentication and access to the platform. Login workflow handling has been stabilized, and users can now authenticate successfully without unexpected redirects or error pages.

- **PDF Text Extraction Corrupts Table Structure**

  PDF text extraction could corrupt table formatting during ingestion workflows, causing values to appear in incorrect columns, numeric values to be omitted, and structured table layouts to become unusable. Table extraction handling has been improved to preserve original structure, alignment, and numeric content more accurately during PDF processing.

- **Annotation Page Freezes After Aggressive Zooming in Visual NER Projects**

  Repeated or aggressive zoom interactions in Visual NER projects could cause annotation pages to freeze or task content to disappear, requiring a manual page refresh to recover. Zoom handling and rendering stability have been improved, allowing Visual NER annotation pages to remain responsive during repeated zoom operations.

- **Error on Labeling Page for Annotator and Reviewer Users**

  Annotator and Reviewer users could encounter unexpected errors when opening tasks on the labeling page, interrupting annotation and review workflows. Access and labeling page handling for these roles has been corrected, and tasks now open successfully without labeling page errors.

- **Internal Server Error When Deleting Downloaded Embeddings**

  Deleting downloaded embeddings could trigger an internal server error because embedding usage validation was not properly handled before deletion.
  Embedding deletion workflows now validate active usage before removal:
  
  - If the embedding is currently in use, a clear validation message is displayed.
  - If the embedding is unused, deletion completes successfully.

- **Unable to Generate Augmented Tasks with OpenAI After External Service Integration**

  Augmented task generation with OpenAI could fail even after a valid External Service Provider was properly configured and integrated into the platform. Integration and generation workflows have been corrected, and augmented task generation now functions successfully with supported OpenAI integrations.
  
### Core Functional Improvements

- **Unable to Export External Prompts While Zero-Shot Prompts Export Successfully**

  External prompt export workflows could fail even though zero-shot prompts exported correctly, creating inconsistent behavior between supported prompt types. Export and import functionality for external prompts has been corrected, allowing teams to manage all prompt types consistently across projects.

- **“License in Use” Error When Deploying TS While HC Model Is Already Deployed**

  Deploying a Terminology Server (TS) could incorrectly trigger a “License in use” error when a Healthcare (HC) model or NER model was already deployed using the same floating or universal license credits, even when sufficient credits were available.
  
  License validation logic has been updated to correctly support shared usage scenarios, allowing:
  - Parallel deployment of model servers and Terminology Servers using the same available credits
  - Deployment of NER models in one project while deploying Terminology Server independently in another project

- **Annotator Role Unable to Access Medical Terminology in Self-Created Projects**

  Annotator users could encounter access restrictions when attempting to use Medical Terminology functionality inside projects they created themselves. Permission handling has been corrected, and Annotator users can now access Medical Terminology features as expected within self-created projects.

- **Deployed External Prompts Missing from Configuration**

  Previously deployed external prompts were not always displayed in the Configuration section on the Cluster page after deployment. Visibility of deployed prompts has been corrected, ensuring deployed external prompts now appear consistently within Configuration workflows.

- **Selecting Medical Terminology Redirects User to AI Resolver Model Tab**

  Selecting the Medical Terminology section during configuration workflows could incorrectly redirect users to the AI Resolver Model tab, interrupting navigation flow. Navigation behavior has been corrected so users now remain within the Medical Terminology workflow as expected.

- **Model Download Status Does Not Refresh Automatically**

  Downloaded models could remain stuck in the “Downloading” state until the page was manually refreshed, even after downloads completed successfully. Status synchronization has been improved so model states now update automatically to “Downloaded” immediately after completion.

- **Incorrect Data Displayed in “Average Number of Edits per Task” Analytics Chart**

  The “Average Number of Edits Per Task” analytics chart could display inaccurate values because calculations were incorrectly based on time metrics instead of edit counts. Chart calculations have been corrected, and the visualization now accurately reflects the number of edits performed per task.

### UI/UX & Visual Enhancements

- **Relations Between Annotations Overlap in UI**

  Relation lines between annotations could overlap with each other and surrounding interface elements, reducing readability during annotation and review workflows. Relation rendering has been improved to provide clearer visual separation and better usability when working with complex relation sets.

- **Inconsistent Breadcrumb Styling Across Pages**

  Breadcrumb styling could appear inconsistent across different pages due to variations in font size, separators, and notation styles. Breadcrumb components have been standardized across the application, improving visual consistency and navigation clarity throughout the platform.

---
## Versions

</div>

<ul class="pagination owl-carousel pagination_big">
    <li><a href="annotation_labs_releases/release_notes_8_1_3">8.1.3</a></li>
    <li><a href="annotation_labs_releases/release_notes_8_1_2">8.1.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_8_1_1">8.1.1</a></li>
    <li class="active"><a href="annotation_labs_releases/release_notes_8_1_0">8.1.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_8_0_1">8.0.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_8_0_0">8.0.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_8_2">7.8.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_8_1">7.8.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_8">7.8</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_7">7.7</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_6_0">7.6.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_5_1">7.5.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_5_0">7.5.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_7_4_0">7.4.0</a></li>
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