---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 7.5
permalink: /docs/en/alab/annotation_labs_releases/release_notes_7_5_0
key: docs-licensed-release-notes
modify_date: 2025-10-22
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">

## Generative AI Lab 7.5: Smarter, Safer, and Seamlessly Connected
Generative AI Lab 7.5.0 takes productivity and security to the next level with smarter automation, seamless integrations, and a smoother user experience. This release empowers teams with credential-free S3 access via EC2 roles, incremental imports for faster data syncs, and real-time admin notifications for better collaboration. With enhanced LLM controls, refined confidence filtering, and polished UI interactions, version 7.5.0 makes managing, annotating, and optimizing AI projects more effortless than ever.

### Support for EC2 Instance Role-Based Access to S3 for Import and Export

**What's New**: Generative AI Lab **7.5.0** introduces seamless and secure integration with **AWS S3** through **EC2 instance-level IAM roles**. Until now, users had to manually enter their S3 credentials each time they imported or exported data, a process that was repetitive, error-prone, and posed security risks.

With this update, the application can access designated S3 buckets directly using the IAM role assigned to the hosting EC2 instance, removing the need for user-provided credentials entirely.

**Technical Details:**
- The **import** and **export** logic has been enhanced to automatically use the **instance's IAM role** when interacting with S3.
- User-entered credentials are no longer required for S3 operations.
- The system securely accesses designated S3 buckets configured under **AWS IAM policies**.
- Implementation follows **AWS security best practices**, including the **least-privilege principle**, ensuring only necessary permissions are granted.
- The workflow for importing or exporting data remains unchanged; users simply select the S3 bucket, and the platform handles authentication automatically.

  ![IAMImport](/assets/images/annotation_lab/7.5.0/1.gif)

**User Benefits:**
- **Simplified workflow** - eliminates the need to repeatedly enter and manage S3 credentials.
- **Enhanced security** - reduces the risk of exposed or misconfigured credentials.
- **AWS-native integration** - leverages IAM roles for secure and scalable access management.
- **Improved reliability** - minimizes import/export errors related to credential handling.
- **Reduced support overhead** - fewer configuration and troubleshooting steps for teams.

**Example Use Case:**
An organization hosts Generative AI Lab on an **EC2 instance** configured with an **IAM role** that grants read/write permissions to specific **S3 buckets**.

When users import datasets or export annotated projects, the platform seamlessly accesses the corresponding S3 buckets using the IAM role, with no manual credential entry needed.

This ensures a faster, safer, and more consistent data management experience.

### Support Incremental Imports from S3 Buckets (Avoid Re-importing Existing Files)

**What's New:** Generative AI Lab **7.5.0** introduces a major enhancement to the **S3 import workflow**: incremental imports.
Previously, every time users imported data from an S3 bucket, **all files** in the bucket were re-imported, even if they had already been added to the project. This led to **duplicate tasks**, redundant processing, and longer import times.

With this update, Generative AI Lab now intelligently identifies which files are **new** and only imports those, while skipping files that already exist in the project. This ensures faster imports, cleaner task management, and a more efficient workflow.

**Technical Details:**
- The import process now compares **file names** against existing task names within the project.
- Files already imported are **skipped automatically**, preventing duplicates.
- The **import summary message** clearly indicates how many new files were imported and how many were skipped.
- The enhancement is fully **backward compatible**, existing projects and import configurations continue to function without any changes.
- No modification is required on the user's part; the system handles this logic seamlessly.

![IncrementalImport](/assets/images/annotation_lab/7.5.0/2.gif)

**User Benefits:**
- **Eliminates duplication** - prevents re-importing files that are already part of the project.
- **Faster imports** - only new or updated files are processed.
- **Clear feedback** - users receive precise information on how many files were imported and skipped.
- **Improved efficiency** - reduces unnecessary computation and improves project organization.
- **Hassle-free transition** - no additional setup or configuration needed for existing projects.

### **Example Use Case:**
A user initially imports **10 documents** from an S3 bucket. Later, **5 more documents** are added to the same bucket. When re-importing, Generative AI Lab automatically detects the existing 10 files and imports only the **5 new ones**.

This process saves time, prevents redundancy, and keeps project data clean and consistent.

> **Note:** Incremental import applies only when **Saved Credentials** are used.
> If the saved credentials or import path are modified, all files in the bucket will be re-imported as a new batch.

## Admin Notifications for Analytics and LLM Requests

**What's New:**  

Generative AI Lab **7.5.0** introduces a new feature that automatically **notifies administrators** whenever users create **Analytics** or **LLM requests**.

In the past, admins were not **automatically notified** of the requests, so users had to **inform admins directly**. This usually resulted in slow response and complicated the tracking of running activities by the admins.

With this update, **the new Analytics and LLM requests** are automatically notified to the admin users in **real-time** to allow them to coordinate faster and have a better view of the operations.


**Technical Details:**
-   Implemented **automated notification triggers** for Analytics and LLM requests.
-   Notifications are sent **only to admin users** for better control and clarity.
-   Notifications are delivered **in real time**, ensuring immediate awareness of new requests.  
-	Enables **faster coordination** between users and admins without any manual steps.


  ![750image](/assets/images/annotation_lab/7.5.0/3.png)

**User Benefits:**
-   **Automatic notifications** - No need for users to manually inform admins about new requests. 
-   **Improved visibility** - Admins stay up to date on all Analytics and LLM activities.
-   **Faster coordination** - Enables quicker reviews, approvals, and responses. 
-   **Operational transparency** - Keeps teams aligned and informed.

**Example Use Case:**  
A user submits a new **Analytics request** to generate insights for their project. The assigned **admins are instantly notified**, allowing them to review and manage the request promptly.

  ![IAMImport](/assets/images/annotation_lab/7.5.0/4.gif)

### Improvements

### Accurate Relation Filtering Based on Confidence Score

**What's New:**  

Generative AI Lab **7.5.0** enhances the **confidence score filtering** mechanism to ensure that **relations are filtered consistently** with their associated labels.

Previously, when users filtered annotations by confidence score, related entities with lower confidence values were not correctly filtered out, leading to mismatched or incomplete views of prediction results.

With this improvement, relations are now automatically filtered according to the **confidence score range** applied, ensuring precise and consistent annotation visibility.

**Technical Details:**

-   Updated the filtering logic to include **relation confidence scores** alongside labels.    
-   Relations below the selected confidence threshold are now **excluded** from the task view.    
-   Ensures **real-time synchronization** between label and relation filtering.   
-   Improves **annotation accuracy and UI consistency** during review.

  ![IAMImport](/assets/images/annotation_lab/7.5.0/5.gif)

**User Benefits:**

-   **Consistent filtering** - Relations now align with label confidence score filters. 
-   **Improved clarity** - Reduces confusion caused by partially filtered results. 
-   **Better accuracy** - Only relevant relations remain visible during high-confidence analysis.

**Example Use Case:**  

A user filters annotations by a **confidence range of 0.9-1.0**.  
Previously, relations with confidence scores below this range (e.g., **0.88**) would still appear.  
Now, such relations are automatically **excluded**, providing a cleaner and more accurate view of confident predictions.

### Configurable Temperature and Token Settings for All Supported LLMs

**What's New:**  

Generative AI Lab **7.5.0** introduces new options in the UI to **define temperature and token limits** for all supported LLM providers - **OpenAI**, **Claude**, **Azure OpenAI**, and **Amazon SageMaker**.

Previously, these parameters were fixed or required backend configuration, limiting flexibility.  
With this improvement, users can now easily adjust **generation behavior and output length** directly from the interface, ensuring greater control over model responses.

**Technical Details:**
-   Added **Temperature** and **Max Token** input fields to the UI for all supported LLMs.  
-   Applied across key features, including **Task Generation** and **External Prompts**.   
-   Configurations are **stored and applied dynamically** during request execution.  
-   Supports all providers: **OpenAI**, **Claude**, **Azure**, and **SageMaker**.

  ![IAMImport](/assets/images/annotation_lab/7.5.0/6.gif)

**User Benefits:**
-   **Fine-tuned control** - Users can customize creativity (temperature) and the response length (tokens).   
-   **Unified experience** - Same configuration options available across all LLM providers.   
-   **Enhanced flexibility** - Easily adapt model behavior for diverse project needs.

**Example Use Case:**  
A user generating tasks using **Azure OpenAI** can now set a **temperature of 0.7** for balanced creativity and a **max token limit of 512** to control response length.  
These parameters can be adjusted, helping teams optimize output quality and consistency across different LLMs.

***Note:***
*-   The **temperature** value ranges from **0 to 1**.*
*-   If a user sets the value to **0**, the system automatically applies a **default temperature of 0.7** to maintain optimal model performance.*

### Dropdown to Select Predefined LLM Response Names in LLM Comparison Projects

**What's New:**  
Generative AI Lab **7.5.0** now allows users to **select predefined LLM response names from a dropdown** in LLM Comparison projects.

Previously, users had to manually enter response names, which increased the risk of typos and inconsistencies. With this update, selecting names is faster, easier, and error-free.

**Technical Details:**
-   Added a **dropdown menu** listing all predefined LLM response names.  
-   Users can now select a response name directly from the dropdown instead of typing it manually.  
-   Fully integrated into LLM Comparison projects for seamless workflow.

  ![IAMImport](/assets/images/annotation_lab/7.5.0/7.gif)

**User Benefits:**
-   **Simplified workflow** - Quickly select response names without typing.  
-   **Reduced errors** - Eliminates typos and mismatched entries.  
-   **Faster setup** - Speeds up project configuration and comparison tasks.
-   **Improved consistency** - Maintains uniform naming across projects.

**Example Use Case:**  
A user creating a **LLM Comparison project**, can now select from a list of predefined response names, using the dropdown. This ensures uniformity across multiple comparisons and reduces manual input errors, saving time and improving project accuracy.

### Updated Pop-up Messaging Before Submission

**What's New:**  
Generative AI Lab **7.5.0** updates the **submission confirmation pop-up** to provide clearer guidance to users.

Previously, the message could be misleading, especially for first-time users, implying that **no further modifications** are possible after submission. In reality, changes can still be made by creating a **new completion**.

With this update, the pop-up text now accurately reflects the process, reducing confusion and improving the user experience.

**Technical Details:**
-   Updated the **confirmation pop-up message** before submission.
-   Clarifies that **submitted completions cannot be edited**, but new completions can be created for changes.
-   Added a **"Don't show again"** checkbox for user preference. 
-   Applied across all relevant task types in the platform for consistency.

  ![IAMImport](/assets/images/annotation_lab/7.5.0/8.png)

**User Benefits:**

-   **Clear guidance** - Users understand the correct workflow for editing and creating completions.   
-   **Reduced confusion** - Eliminates misunderstandings about submission and editing limitations. 
-   **Improved UX** - Supports smoother task completion and reduces support queries.   
-   **Optional reminder** - Users can disable the pop-up if preferred.

**Example Use Case:**

A first-time annotator submits a completion. The updated pop-up now states:  
_"Submitting this completion means it cannot be edited further. To make changes, please create a new completion. Are you sure you want to continue?"_

### Improved OCR Server Connection Feedback for NER Projects

Enhance user experience with clear visual indicators when connecting to an existing OCR server, reducing confusion and preventing duplicate deployment attempts.

**What's New:**
Generative AI Lab 7.5.0 introduces an improved loading experience for OCR-enabled NER projects. When the Import page is refreshed and an OCR server is already deployed, users now see a **loading spinner** indicating that the OCR server is connecting.  

Additionally, the **"Add Sample Task"** button now displays a **loading state** after being clicked, letting users know the process is in progress.

**Technical Details:**

-   Added a **loading spinner** on the Import page during OCR server connection for NER projects.
-   Disabled the **"Add Sample Task"** button while the OCR server is busy.   
-   Implemented a **loading animation** on the button after user interaction. 
-   Prevents duplicate OCR deployment attempts by clearly showing connection progress.

  ![750Image](/assets/images/annotation_lab/7.5.0/9.gif)
    
**User Benefits:**

-   **Clarity:** Users immediately see when the OCR server is connecting.  
-   **Efficiency:** Avoids redundant deployment attempts due to unclear server state.    
-   **Feedback:** Loading indicators provide better understanding of ongoing operations.

### Bug Fixes
- **Confidence Score Shown in HTML Projects Even When Labeling Options Are Disabled**

  Fixed an issue where confidence scores were displayed in HTML projects even when the corresponding labeling option was disabled. The confidence score now only appears when explicitly enabled in project settings, ensuring consistent UI behavior.
  
- **Import Status Shows Failure When ZIP Contains a PDF File**

  The import status now correctly reflects the outcome when a ZIP contains both .txt and .pdf files. All valid .txt tasks are imported successfully, while the .pdf file is skipped and listed as a failed task, with the final status showing correct status.

- **Pre-Annotation Server Deploys Successfully Even When Model Is Unavailable**

  Fixed an issue where the pre-annotation server deployment succeeded even when no model was available. The deployment process now validates model availability before proceeding, preventing false-positive success notifications.

- **Assertion Models Cannot Be Deployed Alongside NER Models for Pre-Annotation**

  Addressed an issue where assertion models could not be deployed together with NER models for pre-annotation. The system now supports joint deployment of both models, enabling richer pre-annotation capabilities.

- **"Something Went Wrong" Error Appears When Using Delete All Tasks Button**

  Fixed a bug that triggered a generic "Something Went Wrong" error when using the Delete All Tasks button. The action now completes successfully, and appropriate success or error messages are displayed.

- **Credentials Not Saved or Masked During Synthetic Task Generation**

  Resolved an issue where credentials used for synthetic task generation were not saved or masked. Credentials are now securely stored, masked in the UI, and reused across sessions to enhance usability and security.

- **Coordinates aren't visible in Bbox Detection project types**

  Fixed an issue where bounding box coordinates were not visible in detection-type projects. Coordinates are now displayed correctly, improving annotation visibility and accuracy.

- **Credentials aren't saved for external providers in "Generate Synthetic Tasks"**

  Addressed an issue where credentials for external data providers in Generate Synthetic Tasks were not being saved. Credentials are now persisted securely and reused without requiring re-entry.

- **User is not automatically redirected to logout page after session timeout**

  Fixed an issue where users were not redirected to the logout page after session timeout. The system now automatically logs out inactive users and redirects them to the login screen, ensuring session integrity.

- **No Validation Required for Response Name in Labeling config in LLM Response Comparison**

  Validation now correctly enforces that the element name must match the response name (response1 or response2) for LLM Response Comparison in HTML project type in visual project configuration mode. Incorrect names are blocked since there is now a drop-down of the response names for these fields.
  
- **Reviewer Dropdown Fails to Populate After Page Refresh When Assigning Reviewers**

  Addressed an issue where the reviewer dropdown failed to populate after refreshing the page during reviewer assignment. Reviewer lists now load correctly after refresh, improving task management flow.

- **Project Owner Missing in Member Order API After Import**

  Fixed an issue where the project owner was missing from the Member Order API response after project import. The API now includes the owner field as expected.

- **"Only Assigned" checkbox is not visible when Prediction section is selected**

  Resolved a UI issue where the Only Assigned checkbox disappeared when the Prediction section was selected. The checkbox now remains visible and functional across all relevant views.

- **Confirmation dialog box overlapped by Labels section in labelling page while submitting tasks**

  Fixed a UI layering issue causing the confirmation dialog box to be overlapped by the labels section during task submission. Dialogs now appear in the correct visual hierarchy.

- **Labeling page flickers when user compares between completions**

  Resolved a visual glitch where the labeling page flickered while switching between completions. Completion view is now smooth and stable.

- **User cannot deploy OCR Server if no models are configured in a Project**

  Fixed an issue where users were unable to deploy the OCR server if no models were configured in the project. Users can now successfully deploy the OCR server in a Visual NER project even when no models are configured.

- **Internal Server Error When Viewing Newly Uploaded PDF and Image Tasks**

  Addressed an issue that caused an internal server error when opening newly uploaded PDF or image tasks. These tasks now render correctly in the viewer without errors.

- **Error during Bulk import of JSON text**

  Fixed an issue where bulk importing JSON text resulted in errors. JSON imports are now processed reliably, with improved validation and error handling.

-  **User are not able to generate Augmented Task**

   Fixed an issue preventing users from generating augmented tasks. Task augmentation executes successfully and reflects the generated results without error.


## Versions

</div>

{%- include docs-annotation-pagination.html -%}