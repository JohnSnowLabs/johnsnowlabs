---
layout: docs
comment: no
header: true
seotitle: Release Notes | John Snow Labs
title: Release Notes
permalink: /docs/en/alab/release_notes
key: docs-training
modify_date: "2024-03-15"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## NLP Lab 5.9 – Entity Resolution and Pre-annotation using Resolvers for NER, Pre-annotation using Prompts and Rules for Visual NER, Import and Export projects to S3 and Azure Blob

NLP Lab 5.9 introduces significant updates aimed at enriching and expanding the capabilities of your NLP workflows. This release represents a major step forward, offering support for Entity Resolution for standard taxonomies like ICD-10, RxNorm, SNOMED, LOINC, UMLS, MeSH, CPT for both annotations and pre-annotations activities. Furthermore, the inclusion of Rules and Prompts in Visual NER projects enables improved pre-annotation results without the need for trained models. The introduction of the Supervisor role offers enhanced authority compared to the Annotator role. Additionally, the ability to Import and Export projects in S3/Blob further enhances NLP Lab 5.9 for easier project backup and sharing capabilities. These advancements, coupled with our ongoing commitment to performance enhancements and user experience improvements, underscore our dedication to meeting the evolving needs of the NLP community. Discover the limitless possibilities with NLP Lab 5.9 and elevate your NLP projects to new levels of excellence.

## Support for Entity Resolution
### Lookup code/terms in Labeling page
NLP Lab version 5.9.0 introduces support for Entity Resolution, allowing users to enhance their annotations by adding lookup datasets. By allowing users to enrich labeled text with additional information, NLP Lab provides the way for improving the context and accuracy of annotations. Lookup functionality is currently supported exclusively by text based NER projects.

### Configuring Lookup
Configuring lookup datasets is straightforward: use the well-known Customize Labels page during project configuration and follow the steps below:
1. Click on the specific label for which you want to add lookup data.
2. Select the desired lookup dataset from the dropdown list.
3. Navigate to the task page and add lookup information to labeled texts.

![LookUpConfiguration](/assets/images/annotation_lab/5.9.0/1.gif)

### Identifying Entities with Lookup Data:
Once setup is done, it is easy to identify entities eligible for lookup by a small ⌄ icon displayed next to them. This icon signifies that lookup data can be added to those entities, providing users with clear guidance on annotation possibilities.

![ViewingIfLookupIsAvailable](/assets/images/annotation_lab/5.9.0/2.png)

### Adding/Viewing and Updating Lookup Data:
**Adding Lookup Data in Labeling Page:** Users can select the available lookup data from the list available for a particular label.

![AddLookup](/assets/images/annotation_lab/5.9.0/3.gif)

**Viewing Lookup Dataset:** Users can view the lookup data or metadata by clicking the gear icon in the labeling page and enabling the "Show Meta in Regions" setting.

![ShowhideMeta](/assets/images/annotation_lab/5.9.0/4.gif)

**Updating Lookup Dataset:** If users wish to change or edit the lookup data, they can simply right-click on the particular entity and choose the new lookup data.

![UpdateLookup](/assets/images/annotation_lab/5.9.0/5.gif)

This new feature enhances the annotation capabilities of NLP Lab, allowing users to enrich their annotations with relevant contextual information from lookup datasets. We're excited to see how this feature empowers users to create more accurate and comprehensive annotations in their projects.

## Pre-annotate metadata using Resolvers 

- NLP Lab 5.9 introduces a pivotal enhancement that expands pre-annotation capabilities with the use of Healthcare resolvers. These resolvers are now conveniently accessible and discoverable on the NLP Models Hub page. Simply apply the "Entity Resolution" filter to view the comprehensive list.

![Resolution_prediction](/assets/images/annotation_lab/5.9.0/6.png)

- For any selected resolver to be used in the pre-annotation process it is required to incorporate the named entity recognition (NER) model as part of the configuration project during setup.

- To seamlessly integrate the resolver with the NER models, navigate to the "Reuse Resources" page within the project configuration. Subsequently, proceed to the "Customize Labels" section. Here, individually select each label and designate the appropriate resolver from the drop-down menu of Entity Resolution Models.

![Resolver_configuration](/assets/images/annotation_lab/5.9.0/7.gif)

- The role of these resolvers is to transform pre-annotated labels into both code and descriptive representations. To access this functionality, ensure that the "Show Meta in Regions" option is enabled within the task settings.
  
![Resolution_prediction](/assets/images/annotation_lab/5.9.0/8.gif)

- Meta-information associated with a label is stored in a key-value pair format, facilitating easy retrieval and interpretation.

![Resolution_prediction](/assets/images/annotation_lab/5.9.0/9.png)

- While it's possible to copy and modify completions, it's important to note that the resolved code and descriptions cannot be directly edited. In such cases, deletion of the existing content or addition of new key-value pairs is necessary. In instances where no prediction is available, manual annotation of tasks can be performed using lookup codes/terms, provided that a lookup table has been configured.
![Resolver_copy_and_renames](/assets/images/annotation_lab/5.9.0/10.gif)

## Pre-annotation using Prompts in Visual NER project
NLP Lab 5.9.0 expands pre-annotation capabilities for Visual NER projects with added support for pre-annotation using Prompts. Users can now pre-annotate tasks in Visual NER projects using zero-shot prompts, significantly enhancing the scope for pre-annotation along with efficiency and accuracy.

In previous versions, the use of prompts was limited to only in text-based projects. With this version, the scope has been expanded, allowing users to leverage prompts for pre-annotation in their PDF and image-based projects as well.

By incorporating zero-shot prompts, users can achieve efficient and accurate pre-annotation without the need for manual intervention.

### Configure and Pre-annotate tasks using Prompts:
- Create a Visual NER Project
- Navigate to Reuse-Resource Page and add desired zero shot prompts (relation prompts and external prompts are not supported, currently)
- Once project configuration is saved, pre-annotate the tasks using the prompt.

![PromptInVisner](/assets/images/annotation_lab/5.9.0/11.gif)

This new feature streamlines the pre-annotation process and extends the benefits of prompts to Visual NER projects, empowering users to annotate tasks more effectively across various document types.


## Pre-annotation using and Rules Visual NER project
Version 5.9.0 introduces support for using Rules for pre-annotation capabilities of Visual NER projects. Users can now pre-annotate tasks in Visual NER projects using rules, extending the benefits of automated pre-annotation to a wider range of document types.

Previously, rules were only available for use in text-based projects. However, with this version, the scope has been expanded to include Visual NER projects. Users can now leverage rules for pre-annotation in PDF and image-based projects, providing greater flexibility and efficiency in annotation workflows, allowing users to utilize rules to automatically annotate tasks in Visual NER projects.

### Configure and Pre-annotate tasks using Rules:
- Create a Visual NER Project
- Navigate to Reuse-Resource Page and add desired rules.
- Once project configuration is saved, pre-annotate the tasks using the rules.

  ![RulesInVisner](/assets/images/annotation_lab/5.9.0/12.gif)

## New Supervisor Role for Users
In this version of NLP Lab, we're excited to introduce a new user role: Supervisor. The Supervisor role offers enhanced authority compared to the Annotator role while maintaining restrictions, similar to the Admin role.

### Role Authority:
A user with the Supervisor role has access to almost all functionalities available to the Admin role, with a few exceptions:
- **Users Page Access:** Supervisors cannot access the Users page, limiting their ability to create and edit users within the system.
- **External Service Providers:** They do not have access to external service providers and cannot use prompts created by other users via external service providers.
- **Limited Access to System Settings:** Supervisors have read-only access to Analytics Requests page, License page, Infrastructure Settings, and Export Project Settings in the System Settings page.
- **No Access to Backup Page:** The Backup page is inaccessible to users with the Supervisor role.

![SupervisorAuthority](/assets/images/annotation_lab/5.9.0/13.gif)

### Creating a user with Supervisor Role
The process of creating a user with the new role is just like creating any other users. As an admin user, navigate to the “Users” page under “Settings” menu item, then Add a new user, assign Supervisor role and save it.

![CreatingSupervissor](/assets/images/annotation_lab/5.9.0/14.gif)

The introduction of the Supervisor role enhances user management capabilities while maintaining necessary restrictions to ensure data security and system integrity. This role provides users with the appropriate level of authority to oversee projects and workflows effectively within NLP Lab.

## Import and Export project in S3 and Blob
Version 5.9 of NLP Lab allows you to effortlessly import and export projects using S3 and Azure Blob.

**Steps to import a project from S3:**
- Navigate to "Import Project"
- Choose "AWS S3"
- Input the path to the S3 file as s3://bucket/folder/file.zip
- Provide S3 Access Key, S3 Secret Key, and Session Token (Required for MFA Accounts)
- Click "Import"
  ![S3_import](/assets/images/annotation_lab/5.9.0/15.gif)


**Steps to import a project from Azure Bbob:**
- Go to "Import Project"
- Select "Azure Blob"
- Enter the path to the Azure Blob file as Container/file.zip
- Input Azure Account Name and Azure Account Secret Key
- Click "Import"
  ![Import_azure](/assets/images/annotation_lab/5.9.0/16.gif)


**Steps to export a project to S3:**
- Navigate to "Projects"
- Choose the desired project and Click "Export Project"
- Select "Cloud Export"
- Click "AWS S3"
- Input S3 Access Key and S3 Secret Key 
- Specify the S3 path for export (e.g., s3://bucket/folder/)
- Optionally, provide Session Token for MFA Account
- You click on Save Credentils as well for the future use
- Optionally, save credentials for future use
- Click "EXPORT"
![s3_export](/assets/images/annotation_lab/5.9.0/17.gif)

**Steps to export a project to Azure Bbob:**
- Navigate to "Projects"
- Select the project and Click "Export Project"
- Choose "Cloud Export"
- Select "Azure Blob"
- Enter Account Name, Account Key, and Container Name
- Optionally, save credentials for future use
- Click "EXPORT"
![azure_export](/assets/images/annotation_lab/5.9.0/18.gif)

## Improvements
### Delete user from the user edit page
A delete button has been incorporated into the user edit page, whereas previously, users could only be deleted from the user list page via the three-dot menu. Now, administrators have the option to delete users directly from the user edit page. Additionally, a supplementary delete button has been placed beside the save button at the bottom of the user edit page.

### Configurable button layout for Login page
In previous versions, the "Sign in with OIDC" button appeared directly below the regular "Sign in" button. With NLP 5.9, administrators have the flexibility to configure the positioning of these buttons. By appending an asterisk (*) to the end of the Display Name of Identity Providers in Keycloak authentication, the "Sign in with OIDC" button can be set as the primary option, eliminating any confusion and reducing room for errors.

![OIDC_button_flip](/assets/images/annotation_lab/5.9.0/19.gif)

### The "Next" button is enabled after selected users are added to the project in "Team Member" Page
On the project team member page, bulk selection and role assignment of accounts is now available. Once user accounts are selected, it is now possible to assign "annotator," "reviewer," and "manager" roles in bulk. However, there's a common issue where users occasionally forget to click the "Add to team" button after assigning roles. Consequently, when users attempt to proceed to the project configuration page by clicking the next button, the selected users and their roles are lost in this case. 

To address this situation, the "Next" button is left disabled until the selected users along with their roles are added to the team, ensuring that changes are saved. Only after this process is complete does the "Next" button become enabled, allowing users to proceed without losing any data.

### Meta in Labels should support HTML tags and escape sequences
In previous versions of NLP Lab, metadata in labels had limitations regarding support for special characters, HTML tags, and new lines. With version 5.9.0, meta support in labels has been significantly enhanced to include special characters, new lines, and HTML tags (such as \n, \s).

![MetaSupportSpecialCharacter](/assets/images/annotation_lab/5.9.0/20.gif)

Users can leverage the enhanced meta support to provide additional context and information within labeled entities. Whether including special characters for specific annotations, utilizing HTML tags for formatting, or adding new lines for clarity, users have greater flexibility in annotating text data.

### Add shortcut for pagination in the task labeling page
In version 5.9.0, we are excited to introduce an improvement to the labeling page that enhances user navigation for large tasks. Users can now utilize keyboard shortcuts to quickly navigate to the next and previous pages within tasks, improving efficiency and workflow.

**Keyboard Shortcuts:**
- **Navigate to Previous Page:** Users can press “Alt/Option + Left" to navigate to the previous page within a task.
- **Navigate to Next Page:** Pressing “Alt/Option + Right" allows users to navigate to the next page within a task.

![PaginationTest](/assets/images/annotation_lab/5.9.0/21.gif)

These keyboard shortcuts provide users with a convenient way to navigate through large tasks more efficiently, particularly when annotating large text data tasks. By streamlining navigation, users can stay focused on annotation task itself, maintaining productivity within NLP Lab.

### Bug Fixes
- **Labels and Choices in a Vertical Layout fail to occupy the entire vertical space**

	Previously, when the project was set up to display labels or choices in a vertical layout, the options did not optimally use the page space and only occupy a small portion of the vertical space. This resulted in cluttered options, and when annotators scrolled through long tasks, these options would often go unnoticed. The fix addresses the issue and the entire vertical space is utilized to list the annotation options.
	
- **Model evaluation can be triggered for trained model**

	Model evaluation is exclusively supported for pre-trained models. An issue arose where users attempted to evaluate trained models, resulting in an error message: 'Evaluation Failed! NER/Classification pretrained model not found in project configuration.' Thus, if a user adds a trained model and attempts evaluation, this error will be displayed.
	
- **For label names with spaces, when trained, the prediction entity name is truncated after spaces**

	In new projects, the NLP lab restricts NER label names from including spaces. If a project owner or manager attempts to add a label name with spaces, an error message will appear. However, in existing projects where label names contain spaces, this error will not occur. Nevertheless, during model training in these projects, entity names with spaces will be truncated after the space in prediction outputs.
	
- **Team members are not displayed in the project card for imported project**

	Previously, when a user imported a project containing multiple users, the project would be created, but the icons of added users were not displayed on the project card in the home page.
	
- **SBA: "Filter Pre-annotation acc. to latest completion" does not show the predicted labels for newly added sections created after the Pre-annotation**

	Previously, the 'Filter Pre-annotation according to latest completion' feature did not display predicted labels for newly added sections created after pre-annotation. The fix corrects how labels are now displayed and preserved for manually created or deleted sections.

The 'Filter by latest completions' feature now accurately displays predicted labels based on pre-annotation for all sections, including manually created ones. Additionally, pre-annotation predictions are removed from sections not present in the latest draft or completion of the current user.
	
- **System Settings is hidden by the "Help" Button in the Side Menu**

	The System Settings, previously hidden under the Help Button in the Side Menu, were inaccessible even with the scroll bar. Now, the System Settings are no longer hidden by the Help button. They are readily accessible and can be scrolled down within the Side Menu to reach the page.
	
- **When user Deletes a user and then transfers the project to another user, the project are not transferred**

	Previously, when the admin user deleted a user and attempted to transfer the project to another user, the project was not successfully transferred. Additionally, a "bad request" error was encountered in the UI.

Now, after deleting a user, the projects are automatically transferred to another user as intended.
	
- **Import fails for cloud task import when mixed image type documents are imported**

	For cases when the user tries to import mixed image type documents from cloud storage, the users will now receive an error message.
	
- **Annotations are not copied when copying completion in a Visual NER Project with SBA**

	Previously, Annotations were not copied when duplicating completions in a Visual NER Project with SBA.
	
- **Search text box in Project page doesn't reset/refresh the page when texts are removed**

	Previously, the search text box on the Project page did not reset or refresh the page when the text was removed. Now, after clearing the search box, all projects are listed as expected.
	
- **While uploading a model, the user need to type every prediction entity**

	Previously, when uploading a model, users had to manually type each prediction entity. This has now been rectified; users can simply copy and paste a comma-separated list of prediction entities for the models.
	
- **Completions are not created when textarea tag is without "toName" attribute**

	Previously, there was an issue where completions were not saved when the textarea tag lacked the "toName" attribute. Now, if such a configuration exists, the config validation will throw an error before the user can save the config, specifically when the XML config includes a `<TextArea/>` node without the toName attribute. After adding the toName attribute, completions are successfully created.
	
- **Relation lines for two entities are not displayed when they are in different lines**

	The issue has been resolved, and now the relation lines remain visible even when scrolling through the task. This fix will across various scenarios including single-page tasks with short texts, as well as multi-page tasks with large texts for both manual annotation and pre-annotation.
	
- **Users are not able to view benchmarking data for pre-trained model**

	The issue has been resolved, and now both admin and supervisors can view benchmarking results for pre-trained models, provided they are available.
	
- **NER model not added" error is shown even when relation model is not added to the project configuration**

	Now, the error message 'NER model not added' no longer appears when RE configuration is added without an RE model. However, if an RE model is added without the inclusion of the NER model, the error message will be displayed.


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

<ul class="pagination owl-carousel pagination_big">
    <li><a href="annotation_labs_releases/release_notes_5_9_1">5.9.1</a></li>
    <li class="active"><a href="annotation_labs_releases/release_notes_5_9_0">5.9.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_8_1">5.8.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_8_0">5.8.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_7_1">5.7.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_7_0">5.7.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_6_2">5.6.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_6_1">5.6.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_6_0">5.6.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_5_3">5.5.3</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_5_2">5.5.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_5_1">5.5.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_5_0">5.5.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_4_1">5.4.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_3_2">5.3.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_2_3">5.2.3</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_2_2">5.2.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_5_1_1">5.1.1</a></li> 
    <li><a href="annotation_labs_releases/release_notes_5_1_0">5.1.0</a></li> 
    <li><a href="annotation_labs_releases/release_notes_4_10_1">4.10.1</a></li> 
    <li><a href="annotation_labs_releases/release_notes_4_10_0">4.10.0</a></li> 
    <li><a href="annotation_labs_releases/release_notes_4_9_2">4.9.2</a></li> 
    <li><a href="annotation_labs_releases/release_notes_4_8_4">4.8.4</a></li> 
    <li><a href="annotation_labs_releases/release_notes_4_8_3">4.8.3</a></li> 
    <li><a href="annotation_labs_releases/release_notes_4_8_2">4.8.2</a></li> 
    <li><a href="annotation_labs_releases/release_notes_4_8_1">4.8.1</a></li> 
    <li><a href="annotation_labs_releases/release_notes_4_7_4">4.7.4</a></li>   
    <li><a href="annotation_labs_releases/release_notes_4_7_1">4.7.1</a></li>        
    <li><a href="annotation_labs_releases/release_notes_4_6_5">4.6.5</a></li>    
    <li><a href="annotation_labs_releases/release_notes_4_6_3">4.6.3</a></li>
    <li><a href="annotation_labs_releases/release_notes_4_6_2">4.6.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_4_5_1">4.5.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_4_5_0">4.5.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_4_4_1">4.4.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_4_4_0">4.4.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_4_3_0">4.3.0</a></li>
	<li><a href="annotation_labs_releases/release_notes_4_2_0">4.2.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_4_1_0">4.1.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_5_0">3.5.0</a></li>
	<li><a href="annotation_labs_releases/release_notes_3_4_1">3.4.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_4_0">3.4.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_3_1">3.3.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_3_0">3.3.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_2_0">3.2.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_1_1">3.1.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_1_0">3.1.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_0_1">3.0.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_3_0_0">3.0.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_8_0">2.8.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_7_2">2.7.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_7_1">2.7.1</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_7_0">2.7.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_6_0">2.6.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_5_0">2.5.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_4_0">2.4.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_3_0">2.3.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_2_2">2.2.2</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_1_0">2.1.0</a></li>
    <li><a href="annotation_labs_releases/release_notes_2_0_1">2.0.1</a></li>
</ul>
