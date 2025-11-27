---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 7.6
permalink: /docs/en/alab/annotation_labs_releases/release_notes_7_6_0
key: docs-licensed-release-notes
modify_date: 2025-11-27
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">


## Generative AI Lab 7.6: Multi Model Blind Evaluation and Advanced NER Training
Generative AI Lab 7.6.0 delivers one of the most significant upgrades to the evaluation and training workflow to date, introducing powerful new capabilities for multi-model benchmarking, advanced NER training, and deeper analytics insights.

This release focuses on enabling teams to perform unbiased, large-scale LLM comparisons, streamline annotation workflows, and improve both the usability and clarity of analytics across the platform. With the introduction of Blind LLM Response Comparison, a new BertForTokenClassifier training option, and a wide range of UI/UX refinements and stability improvements, 7.6.0 enhances accuracy, transparency, and efficiency across every stage of the AI development lifecycle.

Whether you're evaluating multiple foundation models, training high-performance NER pipelines, or managing complex annotation teams, this release provides the tools needed to build regulatory-grade, auditable, and scalable human-in-the-loop workflows.

## Unbiased Multi-Model Assessment with Blind LLM Response Comparison
Generative AI Lab **7.6.0** introduces a major capability designed for teams comparing the performance of several large language models: **Blind LLM Response Comparison**. This new project type enables the evaluation responses from **two or more LLMs** without revealing which model produced each answer, allowing fair, unbiased assessment at scale.

This feature supports a broad range of evaluation workflows from automated response generation to uploading outputs from external systems while providing a redesigned review interface tailored for multi-model comparisons.

### **Technical Details**

- **New Project Type: Blind LLM Response Comparison**

  A dedicated configuration flow enables users to select **any number of connected LLM endpoints**, removing the former limitation of comparing only two models. Popular LLMs, along with responses generated from Custom and organization-specific LLM services, are fully supported for evaluation.

![760image](/assets/images/annotation_lab/7.6.0/1.gif)

- **Flexible Prompt Importing**

  Prompts or questions can be imported individually or in bulk using `.json` or `.txt` formats.
  Example JSON prompt:
  `{ "text": "What are some of the symptoms seen in a person suffering from sepsis?" }`
  The system accepts a variable number of responses for each prompt, whether generated within Generative AI Lab or responses that are imported in GenAI Lab.

![760image](/assets/images/annotation_lab/7.6.0/2.gif)

- **Support for External Responses**

  Imported datasets may include model outputs produced outside Generative AI Lab, as long as they follow the supported JSON structure. During import, the system validates the format and correctly associates each response with its corresponding prompt, enabling flexible, mixed-source evaluation workflows.

- **Blind & Randomized Response Display**

  Responses appear in **random order** and each response is labeled with generic identifiers (e.g., “Response A”, “Response B”).
  Model identities remain hidden from annotators. Internally, a secure mapping is stored and can be viewed by project managers while accessing analytics, but never exposed during labeling.

![760image](/assets/images/annotation_lab/7.6.0/3.gif)

- **Enhanced Annotation Interface**

  To accommodate multiple LLM answers, the annotation screen uses **scrollable panes**, **collapsible response sections**, and **fullscreen view**, making it easier to navigate and compare more than two answers without clutter. Annotators can expand or hide responses based on their review style.

![760image](/assets/images/annotation_lab/7.6.0/4.gif)

- **Expanded Analytics for Multi-Model Comparison**

  The Analytics dashboard now supports detailed comparisons across two or more LLMs, enabling teams to analyze performance differences with greater precision. Enhanced filtering options allow users to narrow the view to specific models, model combinations, or evaluation criteria, making it easier to uncover strengths, weaknesses, and behavioral patterns across LLMs.

  Users can interactively refine the displayed data by **toggling LLM names directly from the bar-graph legend** or by **selecting specific LLMs from the dropdown filter**. This allows focused analysis on individual models or direct comparisons between selected LLMs, rather than viewing the entire dataset at once.

![760image](/assets/images/annotation_lab/7.6.0/5.gif)

- **Mandatory Classifications Across LLM Evaluation Templates**

  LLM evaluation project templates now enforce mandatory classification selections to maintain consistency and prevent incomplete task submissions. A response cannot be submitted until at least one choice option is selected, ensuring evaluators always provide a definitive classification. This requirement applies not only to **Blind LLM Response Comparison** but also to other evaluation-oriented templates, including **LLM Evaluation** and **LLM Response Comparison** for both **Text** and **HTML** project types.

  This functionality is enabled by the `required="true"` attribute automatically included in all `<Choice>` elements within the default XML templates. Administrators may modify the XML configuration if optional selections are preferred for their workflow.

### **User Benefits**

- **Unbiased Model Assessment** – Blind review ensures annotations and judgments are not influenced by model vendor or expectations.
- **Scalable Multi-Model Evaluation** – Supports multiple LLM endpoints, accommodating internal, external, or custom models.
- **Flexible Data Handling** – Works seamlessly with system-generated responses and externally produced outputs.
- **Improved Usability** – A modernized annotation view makes multi-model comparison practical, even with large sets of responses.
- **Deeper Insights** – Enhanced analytics help teams pinpoint which models perform best under specific prompts or criteria.

### **Example Use Case**

A research team wants to evaluate five LLMs, one hosted on SageMaker, and different models offered by OpenAI, Azure OpenAI, and Claude. They import a set of prompts, upload external responses for some models, generate responses for others, and begin review. 

Annotators see randomized, anonymized answers, while project managers access full analytics showing how each model performed across accuracy, completeness, and other criteria. The Blind LLM Response Comparison workflow ensures evaluation results remain fair, structured, and scalable.

## NER Training Approach – Support for BertForTokenClassifier Training
A new NER Training Approach option has been introduced, enabling users to train NER models using the BertForTokenClassifier pipeline. This enhancement leverages the licensed model training architecture and offers greater flexibility and accuracy for advanced NER tasks.

**What’s New**

Users can now choose between MedicalNER (existing approach) and the new BertForTokenClassifier method when training NER models. This unlocks the ability to train transformer-based token classification models directly within the platform, with optimized defaults and GPU support for faster processing.

![760image](/assets/images/annotation_lab/7.6.0/6.png)

**Technical Details**

- **New Training Parameter Added:**  
  `NER Training Approach` with two options:  
  - **MedicalNER** (default / existing)  
  - **BertForTokenClassifier** (new)

- **Visible for Healthcare License Types:**  
  The new parameter appears only for customers using a **Healthcare** license, as it leverages the licensed training pipeline.

- **Automatic Learning Rate Adjustment:**  
  When **BertForTokenClassifier** is selected, the system automatically reduces the learning rate from:  
  - **0.001 → 0.00002**

- **No Embeddings Required:**  
  The BertForTokenClassifier pipeline **does not use embeddings**.  
  - If users switch back to **MedicalNER** or **Open-Source NER**, they must **re-select the appropriate embeddings**.

- **GPU Support Enabled for NER Training:**  
  Training with BertForTokenClassifier is more compute-intensive than MedicalNER.  
  - **GPU execution is now supported and recommended** for this training approach.  
  - Previously, GPU usage was only available for Visual NER projects.

**User Benefits**

- **Greater Flexibility:**  
  Choose between fast MedicalNER training or the more powerful BertForTokenClassifier approach.

- **Higher Accuracy for Complex Tasks:**  
  Transformer-based models improve performance on advanced NER workloads.

- **Optimized Training Defaults:**  
  Automatic learning rate tuning reduces configuration steps.

- **GPU-Accelerated Training:**  
  Enables significantly faster training for larger datasets.

- **Smooth Workflow:**  
  Clear switching between approaches with guidance for embedding requirements.

**Example Use Case**

A data scientist wants to improve accuracy for clinical NER tasks involving complex entity boundaries. They select **BertForTokenClassifier** under the NER Training Approach. The system configures the optimized learning rate automatically, and training is performed efficiently on a GPU instance.  
Later, if they revert to MedicalNER, they simply re-select the suitable embeddings for the model.

---

## Improvements

### Analytics Charts Updates: 

#### Minimize the Need for Annotator Selection in Inter-Annotator Charts
**What’s Improved:**  
The Inter-Annotator Charts page now offers a more streamlined workflow by reducing repetitive annotator selections. Previously, every chart required users to manually pick one or two annotators, making the process time-consuming. Especially when reviewing multiple charts in sequence.
With this enhancement, annotators' selection is now centralized and intelligently retained across all IAA charts, ensuring a smoother and more consistent analysis experience. Individual charts also load their data when available.

**Technical Details:**
-   A **global annotators selector** has been introduced at the top of the Inter-Annotator Charts page.
-   The **global selection automatically applies to all IAA charts**, minimizing repeated manual input for IAA charts. 
-   A **default annotator** is pre-selected to simplify initial chart loading.
-   The selected annotator(s) are **retained across navigation and refresh**, improving continuity during analysis.

![Pre-selected initial chart loading](/assets/images/annotation_lab/7.6.0/7.gif)

**User Benefits:**
- **Consistent interactions:** Annotator selections persist across the entire IAA charts.
- **Greater efficiency** — default pre-selection speeds up chart loading.
- **Flexibility** – All charts can still be individually customized when needed.
- **Smoother workflow:** Ideal for reviewing multiple charts quickly and efficiently.

**Example Use Case:**  
A project manager reviewing multiple Inter-Annotator charts selects Annotator A and Annotator B once using the new global selector, and all charts automatically update with this choice. The selection persists across all IAA charts, allowing fast and consistent comparison without repeated manual input.

![Global selection automatically applies to IAA all charts](/assets/images/annotation_lab/7.6.0/8.gif)

#### Improved Context Visibility in Prediction vs Ground Truth Comparison
**What’s Improved:**  
The Prediction vs Ground Truth comparison table now provides sentence-level context to make review and error analysis clearer and more intuitive. Previously, predictions and annotations were shown without surrounding text, making it harder for reviewers to understand where each token or label appeared in the original content.

With this enhancement, a new **Context** column has been added to the comparison view, offering meaningful context for every prediction–ground truth pair.

**Technical Details:**
-   A new **Context** column is displayed in the _Prediction vs Ground Truth_ table.    
-   When sentence boundaries are unavailable, the system automatically extracts a **±20-token context window** around the token.
-   The context column is available **both in the UI** and **in exported reports**, ensuring consistent review clarity across platforms.

![760image](/assets/images/annotation_lab/7.6.0/9.gif)

**User Benefits**
-   **Better Readability:** Reviewers can immediately understand the text surrounding a token or label. 
-   **Faster Error Analysis:** Context helps identify why certain prediction mismatches occurred.

**Example Use Case:**  
A reviewer checking mismatches can now see the sentence around each token, making it easier to understand whether the model’s prediction makes sense in context.

#### More Meaningful Metrics
**What’s Improved:** 
The Analytics charts have been updated to deliver clearer, cleaner, and more user-friendly visualizations. Previously, charts showed floating-point values even when they weren’t meaningful, and some charts displayed auto-generated labels like _bar1_ or _chart2_, which created visual clutter.

**Technical Details:**
-   Floating-point values now appear **only** on charts that display average-based metrics.
-   Unnecessary autogenerated labels such as _bar1_ and _chart2_ have been removed.
-   Units (e.g., **seconds, labels**) are now included in both the **tooltip** and **y-axis**, improving readability and context.

![760image](/assets/images/annotation_lab/7.6.0/10.gif)

**User Benefits**
-   **Cleaner charts:** Users can interpret visual data more quickly without distracting labels.
-   **Better consistency:** Only relevant charts show decimal values, reducing confusion.
-   **Improved clarity:** Units added to tooltips and axes make chart values more understandable at a glance.

**Example Use Case:**

A user reviewing project performance opens the _Task Completion Time_ chart. Previously, the chart showed long decimal values and confusing labels like _chart2_, making it harder to interpret. Now, the chart displays clean whole numbers with **“seconds”** clearly shown on the y-axis and tooltip, allowing the user to quickly understand the timing data without distractions.

#### Choices Chart Now Shows Actual Provider Names
**What’s Improved:**  
The Choices chart in Blind Evaluation Analytics now displays the **actual provider names** instead of generic labels like _Response 1, Response 2_, making it much easier for users to interpret which provider’s output was selected during evaluation.

**Technical Details:**
-   The chart now maps each choice directly to its **corresponding provider**, removing ambiguity.
-   Users no longer need to manually cross-reference response numbers with providers.

![760image](/assets/images/annotation_lab/7.6.0/11.png)

**User Benefits**
-   **Clearer Insights:** Users can instantly identify which provider was preferred.   
-   **Better Comparisons:** Makes evaluation patterns more meaningful and easier to analyze.

**Example Use Case:**  
A reviewer analyzing provider performance can now look at the Choices chart and immediately see that “OpenAI” or “Claude” was selected most often, instead of trying to decode which response number mapped to which provider. This makes evaluating provider quality faster and more accurate.

### Support for Multiple Pie Charts Outside the Evaluation Block
**What’s Improved:**  
Previously, analytics could only render a single pie chart for elements placed outside the **Evaluation Block**, causing missing or incomplete visualizations in projects with custom configurations. This limitation made it difficult for users to analyze additional classification fields when positioned outside the evaluation structure.

**Technical Details:**
-   The system now supports **multiple pie charts** even when they are defined outside the Evaluation Block.  
-   All classification elements placed outside the block are now correctly visualized as individual charts.    
-   Projects with custom analytics layouts can display all relevant charts without restriction.

![760image](/assets/images/annotation_lab/7.6.0/12.gif)

**User Benefits**
-   **Greater Flexibility:** Custom project configurations now work seamlessly with analytics.   
-   **More Complete Insights:** Users can view every classification chart without elements being skipped or overwritten.
  
**Example Use Case:**  
A project using custom fields that are outside the Evaluation Block can now display a separate pie chart for each field. This allows reviewers to analyze all classification metrics without losing visibility due to previous single-chart limitations.

--- 

### Clearer, More Clickable Role Options in Team Member Settings
**What’s Improved:**  
The Team Member page has been updated to make role options—**Annotator**, **Reviewer**, and **Manager**—clearly appear selectable. Previously, the light text styling made these roles look disabled or non-interactive, which created confusion for users assigning team roles.

**Technical Details:**
-   Role options now use a **darker, more prominent text style**, making them clearly visible and intuitively clickable.
-   When a user is selected, the corresponding role text becomes even more distinct, giving immediate visual confirmation of selection.

![760image](/assets/images/annotation_lab/7.6.0/13.gif)

#### **User Benefits**
-   **Better Usability:** Users can now confidently identify which roles are interactive.
-   **Reduced Confusion:** The updated styling eliminates the impression that role checkboxes are disabled.

### Credential Visibility Toggle Added for S3 and Azure Imports
**What’s Improved:**  
Users can now toggle the visibility of their S3 and Azure credentials during task import, making it easier to verify input values and avoid errors. Previously, credentials were always masked, which often led to mistakes that were difficult to detect.

**Technical Details:**
-   An **eye icon** has been added to the S3 and Azure credential fields.
-   Users can **switch between hidden and visible text**, ensuring credentials are entered correctly.
-   Enhances clarity and reduces back-and-forth corrections during configuration.

![760image](/assets/images/annotation_lab/7.6.0/14.gif)
    
**User Benefits**
-   **Improved Usability:** Users can confirm the accuracy of credentials instantly.
-   **Fewer Input Errors:** Mis-typed keys are now easy to spot before submission.

**Example Use Case:**  
A user configuring task import for an S3 bucket can click the eye icon to briefly reveal the access key and confirm it’s typed correctly, preventing import failures caused by hidden credential typos.

### Custom LLM Names Are Now Automatically Made Unique
**What’s Improved:**  
Users were previously able to create multiple custom LLMs with the same name, leading to confusion in the “Select LLM Response Providers” tab, where identical labels made it hard to tell providers apart.

**Technical Details:**
-   The platform automatically assigns a unique sequential Custom name for every Custom LLM created(e.g., _Custom_1, Custom_2, Custom_3_).  
-   The system now checks for existing custom LLM names when a new one is created.

![760image](/assets/images/annotation_lab/7.6.0/15.gif)

**User Benefits**
-   **Improved Clarity:** Users can easily identify each custom LLM without encountering duplicate names.  
-   **Smoother Setup:** Reduces mistakes and confusion during project configuration.

**Example Use Case:** 

A user creating multiple custom LLMs now has a unique name automatically applied, making it easy to distinguish them in the Select LLM Response Providers tab. 

### Prevent Multiple Sample Task Actions During Import

**What’s Improved:**  
The **Add Sample Task** button in Visual NER projects is now disabled while tasks are being imported. Previously, users could click the button repeatedly, affecting the application’s performance. A dialog box now alerts users that the task import is in progress.

**Technical Details:**
-   The Add Sample Task button is disabled during task import.
-   A dialog box informs the user that tasks are being imported.    
-   The button is re-enabled once the import completes.

![760image](/assets/images/annotation_lab/7.6.0/16.gif)

**User Benefits:**
-   **Improved Stability:** Prevents repeated clicks from affecting the application.
-   **Clear Feedback:** Users are informed that the import is in progress.

**Example Use Case:**  
A user importing tasks into a Visual NER project can no longer click the Add Sample Task button multiple times. The dialog box confirms the import is in progress, preventing errors and confusion.

### Enable Left Navigation Bar Expansion on Hover
**What’s Improved:**  
The left navigation bar now expands automatically when users hover over it, making navigation faster and more intuitive. Previously, users had to click to open the menu, which added unnecessary steps during frequent navigation.

**Technical Details:**
-   The navigation bar expands instantly when the cursor hovers over it and collapses smoothly when the cursor moves away.
-   No clicks are required, creating a more fluid and responsive interaction.
-   A subtle animation is applied to ensure a clean and polished transition.

![760image](/assets/images/annotation_lab/7.6.0/17.gif)

#### **User Benefits**
-   **Faster Navigation:** Users can access menu items more quickly, especially during repetitive workflows.
-   **Better Usability:** The UI feels more responsive and reduces extra clicks.

**Note:**  
This functionality applies **only to the Customize Labels page and the Labelling page**.

### Bug Fixes

#### Labeling Page Issues
- **Long Project Names Overlap in Breadcrumb Navigation**

 Fixed an issue where long project names caused breadcrumb links to overlap or spill into adjacent navigation elements. Breadcrumbs now dynamically adjust and truncate appropriately, ensuring clean and readable navigation across all project types.

- **Pixelated Label Names in Visual NER Annotations**

 Resolved an issue where annotated label names in Visual NER tasks appeared blurry or pixelated. The annotation window now renders labels sharply, improving clarity and overall annotation accuracy.

- **“Annotation Guidelines” Shown for Projects Without Labels**

 Previously, the Annotation Guidelines toggle appeared for all project types, including those without label definitions. The toggle is now shown only when at least one label includes annotation instructions, ensuring a cleaner and more relevant user interface.

- **Gestures Allowed Zooming Into Blank Spaces**

 Fixed an issue where gesture-based zooming allowed users to zoom into empty or whitespace areas, particularly in PDF and image-based projects. The zoom behavior now correctly focuses only on valid content regions across all project types.

- **Discrepancy in Visual NER After Labeling Multiline Tokens**

 Addressed a discrepancy where multiline token annotations displayed or behaved inconsistently in Visual NER projects. Multiline annotations now render and behave as expected across all scenarios.

- **Annotation Guidelines Hidden on Smaller Screens**

 Resolved a layout issue where the Annotation Guidelines section was clipped or hidden on smaller screens. The section now responds appropriately to screen size and remains fully visible.

- **UI Error When Interchanging Labels and Regions in Side-by-Side Projects**

Fixed a UI error that occurred when users interchanged labels and regions on the labeling page for side-by-side projects. The page now renders correctly and supports smooth interaction with no functional disruptions.

- **Deleting the First Annotation Removes Overlapping Annotations in HTML Projects**

 Fixed an issue in HTML projects where deleting an annotation inadvertently would remove overlapping annotations. Additional issues were also addressed: Users can now annotate across multiple paragraphs, and they can simultaneously annotate text and HTML tags.

- **Annotation Guidelines Button Hidden When Multiple Annotations Are Listed**

 Fixed an issue where the Annotation Guidelines button became hidden when a long list of annotations was present. The button now remains consistently visible regardless of the number of annotations.

- **Unable to Configure Zoom Tag for B-Box Projects**

 Resolved an issue preventing users from configuring the `<zoom>` tag in B-Box (Bounding Box) project types. The zoom configuration now works correctly across B-Box and other supported project types, enabling proper zoom functionality during annotation.

- **Search Not Working in Visual NER Task Labeling Page**

 The search function on the Visual NER task labeling page was not returning results. The issue has been fixed, and users can now successfully search for text within Visual NER tasks.

- **Unable to Modify Token Labels Without Deleting Them in Blind Evaluation Projects**

Fixed an issue where users could not modify labels on tokens without deleting them first in Blind Evaluation projects. Token labels can now be updated directly, improving annotation efficiency and usability.

#### UI Issues
- **Tasks per Page Field Overflows with Large Input**

 Fixed an issue where entering large values (e.g., over 9 digits) in the Tasks per Page field caused overflow, unexpected UI behavior, and pagination instability. The input is now capped at a maximum value of 200, preventing overflow, UI freezing, and maintaining smooth pagination performance.

- **Unable to Erase First Character in Input Field for Custom LLM due to Space Validator**

 Resolved an issue where users were prevented from deleting the first character in custom LLM input fields because the space validator misinterpreted the action as invalid. Users can now freely delete or modify the first character without restrictions.

- **Labels Selection Triggers by Hotkeys While Entering Custom Value in Characters per Page**

 Addressed an issue where label-selection hotkeys were unintentionally triggered while typing inside the Characters per Page field. Hotkeys are now automatically disabled during input, preventing accidental label selection.

- **Benchmark Button Active When No Benchmark Data Is Available**

Previously, the Benchmark button remained enabled even when no benchmark data existed, leading to errors when clicked. The Benchmark button is now hidden when benchmark data is unavailable, preventing invalid interactions and ensuring a clean user experience.

- **“Something Went Wrong” Error When Generating Templatic Augmentation Using OpenAI**

 Fixed an issue where generating templatic augmentation tasks with the OpenAI model redirected users to a generic error page. Users can now generate templatic augmentation tasks successfully without encountering the error page.

- **Unable to Import Augmented Tasks**

Resolved a backend validation error that prevented users from importing augmented tasks, resulting in an error toast message during the import process.
Augmented tasks now import correctly with no errors or interruptions.

- **“Tasks Uploaded Successfully” Dialog Not Shown During Subsequent Cloud Import**

 Fixed an issue where the success dialog failed to appear during repeated cloud imports. The confirmation dialog now appears reliably for every import attempt, and validation messages correctly display when credentials are missing.

- **Missing Error Message When Generating Templatic Augmentation Without Annotations**

 Previously, no pop-up message was shown when users attempted to generate templatic augmentation tasks without any annotated labels. The system now displays a clear and informative error message, ensuring users understand why the action cannot proceed.
 
#### System Errors

- **Admin User Unable to Disable an Existing User Account**

 Fixed an issue where admin users were unable to disable an existing user account due to an error being thrown during the action. Admins can now successfully disable user accounts, and disabled users are correctly prevented from accessing the application.

- **Missing Success Popup After LLM Integration**

 Previously, no confirmation pop-up appeared after successfully integrating an LLM, leaving users unsure whether the process was completed correctly. But now, after a successful LLM integration, a validation pop-up stating “New service provider added” is displayed, confirming successful integration.

- **Error When Creating New Section-Based Rules**

 Users were redirected to a “Something went wrong” error page when attempting to create new rules under Relevant Sections in project configuration. The issue has been resolved, and users can now create section-based rules without any errors.

- **Blank Page When Modifying Member Order in a Project**

 Fixed an issue where users were redirected to a blank page after altering the order of members in a project's team settings. Users can now reorder project members successfully, and changes are saved correctly without triggering any UI or API errors.

- **“License in Use” Message Not Displayed for Floating License Conflicts**

 The “License in use” message was not shown when floating licenses were used across multiple instances, covering scenarios such as: De-identification pipeline used with Visual Classification or OCR/Visual NER models; NER model used with Visual Classification or OCR/Visual NER models. This behavior has now been fixed. The UI correctly displays the “License in use” message in all relevant scenarios, ensuring users are informed of licensing conflicts.

- **Notification Indicator Visible for Supervisor Even When No Requests Are Pending**

 Fixed an issue where the notification indicator in the Request Center remained active for Supervisor users despite having no pending requests. Since the Request Center is read-only for Supervisor roles, the notification indicator is now correctly hidden, ensuring the UI reflects the actual request status.


## Versions

</div>

{%- include docs-annotation-pagination.html -%}