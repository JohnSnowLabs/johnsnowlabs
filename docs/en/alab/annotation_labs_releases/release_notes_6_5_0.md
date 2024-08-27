---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab Release Notes 6.5.0
permalink: /docs/en/alab/annotation_labs_releases/release_notes_6_5_0
key: docs-licensed-release-notes
modify_date: 2024-08-25
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 6.5.0

Release date: **08-26-2024**

## Create Augmented Tasks for NER Models, Set up your project using a Visual Menu Builder, and leverage Entity Resolver models, rules, and zero-shot prompts in Generative AI Lab 6.5.
The release of Generative AI Lab version 6.5 introduces several new features designed to enhance user experience and improve platform efficiency.

One of the key updates is the ability to generate augmented data based on the existing tasks. This feature enhances model performance by generating additional data, seamlessly fitting into the Generative AI Lab workflow to support various test types and improve their models without having to create dataset from scratch. 

Additionally, users can now use an entity resolver by combining it with rules and John Snow Labs' zero-shot prompts, offering a more streamlined approach to entity recognition. 

Lastly, the new menu builder allows users to visually configure every setting for the annotation project setups, improving the ability for product creators to streamline the workflow for their agents at the project level.

Here are the highlights of this release:

## Data Augmentation for more Robust Model Training
Instead of having to manually create new tasks or documents to enhance model performance and evaluate it against different test types, when the project manager reviews the LangTest report, they can then take steps to improve the model using newly introduced data augmentation techniques. With the release of the Data Augmentation feature in Generative AI Lab 6.5, users can now automatically generate new data for different test types from the existing dataset. This feature streamlines the model improvement process by creating augmented tasks, retraining the model, and testing it against a wider range of scenarios. Users can simply click the "**Improve Test Results**" button to generate augmented tasks for the test types that failed.

The new tab called "**Generate Augmented Data**" on the import page will make it easier for you to create augmented tasks. By clicking on the "**Improve Test Results**" option, you'll be redirected to the "**Generate Augmented Data**" page. Here, the lang-test framework automatically selects the test types you have run and failed, along with the corresponding values of the max_proportion for each test type under "**Proportional Augmentation**".

![genAI650](/assets/images/annotation_lab/6.5.0/1.gif)

####  Proportional Augmentaiton

This method enhances data quality by using various testing techniques to generate new data based on an existing dataset. Proportional Augmentation is particularly effective in improving model performance by addressing specific weaknesses, such as the inability to recognize lowercase text, uppercase text, typos, and more. It is especially beneficial for bias and robustness testing, ensuring that the model produces high-quality and accurate results for machine learning, predictive modeling, and decision-making tasks. After setting the test types and max_proportion, click on "**Generate Results**" to create augmented tasks. Based on your configuration, data augmentation will enhance the existing tasks and generate new ones.

![genAI650](/assets/images/annotation_lab/6.5.0/2.gif)

Another way to generate augmented tasks is through "**Templatic augmentation**".

####  Templatic Augementation
Templatic Augmentation creates new data by using templates or patterns that are similar in structure and context to the original input. This method depends a lot on the templates provided by the user. There are two options for using this approach:
 
 **A. Manually Add Templates**
 Users can manually choose templates along with the available labels. They can choose how many results to generate for each template using a scroll bar, which can be set from 1 to 50.

![genAI650](/assets/images/annotation_lab/6.5.0/3.gif)

 **B. Generate Templates with OpenAI**

 Users can create more templates using OpenAI, which must be integrated into the project for this feature to work. After choosing how many extra templates to generate for each existing one (from 1 to 10), users can select how many results they want for each template by adjusting a scroll bar from 1 to 50. The total expected number of results will also be shown.

![genAI650](/assets/images/annotation_lab/6.5.0/4.gif)

**Note:** **Automatic tags in import augmented tasks** 
After the augmented tasks are generated, the user can import the tasks. The augmented tasks are imported with the "**Augmented**" default tag.

![genAI650](/assets/images/annotation_lab/6.5.0/5.gif)

Users can then re-train the model with the newly augmented tasks and run model testing, which will improve the model's performance under the augmented conditions.


## Configure project using Visual Menu Builder

This version of Generative AI Lab introduces a new way for configuring your projects, removing the need for manual XML configuration. With the Visual Menu Builder, users can easily create, edit, and manage project configurations through a user-friendly interface. This makes the configuration process much more straightforward, especially for those unfamiliar with XML syntax, while also reducing the risk of errors associated with manual coding.

To see the structure of a project configuration XML file and the definitions of the supported tag types and various parameters and variables, and to better understand how Visual Menu Builder maps and creates these elements when configuring your project, see [Project Configuration Overview](https://nlp.johnsnowlabs.com/docs/en/alab/tags_overview).

**Key Features:**

**Add New Element**

The new menu user interface allows users to easily add new elements to their project configurations. Users can click on the plus icon ("+") within the Visual Menu Builder interface to add a new element. Once the element is added, users can further customize it by configuring additional parameters directly in the interface. This might include setting attributes, defining properties, or linking to other project components.

![genAI650](/assets/images/annotation_lab/6.5.0/6.gif)

**Edit an Element**

Users can modify the properties and configurations of existing elements within the project. By clicking on the edit icon (a pencil icon), users can access the settings for an existing element. This opens an editable interface where users can adjust the element's parameters to suit the evolving needs of the project.

![genAI650](/assets/images/annotation_lab/6.5.0/7.gif)

**Delete an Element**

Users can remove unwanted elements from the project configuration. Users can click on the cross button ("x") associated with a specific element to remove it from the project. This feature helps in keeping the project configuration clean and relevant by allowing users to easily remove elements that are no longer needed.

![genAI650](/assets/images/annotation_lab/6.5.0/8.gif)

**Drag and Move Element**

The new visual menu builder allows users to easily rearrange elements within the project configuration using a drag-and-drop interface. To move an element, users can click and hold on the "Handle" icon, which is represented by a set of six dots (three parallel dots in two vertical rows) next to the element. After clicking on the Handle, users can drag the element to the desired position within the project configuration. Release the mouse button to drop the element in its new location. This feature provides flexibility in organizing the project structure, allowing users to quickly and intuitively reorder elements.

![genAI650](/assets/images/annotation_lab/6.5.0/9.gif)

**Show Element Boundaries**

The **Show element Boundaries** button in the visual menu builder highlights the borders of each element within the project configuration, making it easier to visualize and distinguish the different components. By clicking on the "**Show element Boundaries**" button, users can toggle the visibility of the boundaries for all elements in the configuration. When enabled, a visible border will appear around each element, clearly outlining its scope and separation from other elements. This feature is particularly helpful when working with complex configurations where multiple elements are closely positioned. By showing the boundaries, users can easily identify and select the correct element they want to edit, move, or delete.

![genAI650](/assets/images/annotation_lab/6.5.0/10.gif)

**Show Parent Action Buttons on Hover**

The **Show parent action buttons on hover** button in the Visual Menu Builder allows users to quickly access action buttons (such as edit, delete, or add) for parent elements by hovering over them. By hiding the action buttons until needed, it reduces visual clutter and allows users to concentrate on their current tasks. The ability to quickly access these buttons by hovering ensures that they remain easily accessible without overwhelming the interface.

![genAI650](/assets/images/annotation_lab/6.5.0/11.gif)

**Fullscreen Mode**

The "**Fullscreen**" button in the visual menu builder allows users to expand the workspace to occupy the entire screen, providing a larger and more focused view of the project configuration. Clicking on the "**Fullscreen**" button maximizes the Visual Menu Builder, hiding other UI elements so the entire screen is dedicated to the project configuration. To exit fullscreen mode, users can click the "**Fullscreen**" button again or use the Esc key to return to the normal view with all standard UI elements visible.

![genAI650](/assets/images/annotation_lab/6.5.0/12.gif)

## Pair Entity resolver models with rules and zero-shot prompts
Version 6.5.0 introduces expanded support for using Entity Resolution (ER) models, now allowing their use alongside rules and zero-shot prompts. ER models were previously limited to use with Named Entity Recognition (NER) models only. Users can now leverage ER models not only with NER models but also in conjunction with rules and zero-shot prompts. This enhancement offers greater flexibility and efficiency in annotation workflows.

**How to Use**:
  - **Step 1**: Add a rule or prompt from the Re-use Resource page.
  - **Step 2**: Edit the label in the Customize Labels page and select the appropriate ER model to associate with the labels.
  - **Step 3**: Import tasks and Pre-annotate the task.
    
![genAI650](/assets/images/annotation_lab/6.5.0/13.gif)

This update broadens the capabilities of ER models, making them more versatile in annotation projects.

### Improvements
### By default "synthetic" tag is added for imported synthetic tasks
In previous versions, users had to manually add tags to synthetically generated tasks or else tasks imported into the task page lacked any associated tags. Starting with version 6.5.0, when tasks are imported, they now come with synthetic tags already associated with them during import in the task page.

![genAI650](/assets/images/annotation_lab/6.5.0/14.gif)

This improvement saves time by eliminating the need for manual tag assignment and ensures that imported tasks are accurately tagged from the start, improving organization and searchability. Also, this enhancement streamlines the workflow for managing and organizing synthetic tasks, making it easier to work with large datasets as well.

### Enhanced task filtering

With this version, users can combine multiple filters simultaneously to refine their task search, significantly enhancing the control and flexibility in task management.

![genAI650](/assets/images/annotation_lab/6.5.0/15.gif)

### Enhanced visibility - Annotator's Instructions 
The instruction section in Version 6.5.0 has been enhanced for better visibility. Now displayed with a faded blue background and an icon, the instructions stand out clearly, making them easily identifiable by annotators.

![genAI650](/assets/images/annotation_lab/6.5.0/16.png)

### View instructions on the tasks page for "compact view"
View the instructions directly on the task page itself when using the compact view in Classification Project type. 

![genAI650](/assets/images/annotation_lab/6.5.0/17.png)

### Bulk test suite deletion API
Delete multiple test suites in bulk using the API. This streamlines the process of managing test suites, the new bulk deletion API can be accessed and tested directly from the API Integration page within the application as well. 

![genAI650](/assets/images/annotation_lab/6.5.0/18.png)

### Pyspark version displayed on "About" page
This information is useful when training models or when using specific PySpark features, ensuring compatibility. 

![genAI650](/assets/images/annotation_lab/6.5.0/19.png)

### Bug Fixes
- **Bugs Fixes for Testing** 

	Test cases were occasionally failing even when the expected and actual results were identical, tests passing despite a mismatch between expected and actual results, tests incorrectly passing even when expected results were empty and actual results were present. These issues have been resolved in version 6.5.0, ensuring accurate test results and consistent behavior across test cases.
	
	**Not able to change the Units on the Speed Test:**
    This issue has been fixed, allowing users to change the unit of the speed test.
    
    **Test Suite Import Failure:**
    Importing test suites encountered issues and was not functioning as expected. This problem has been resolved in version 6.5.0, and users can now import test suites without any issues.

- **"Emotion Classifier" cannot be deployed in both playground and preannotation server**

    There was an issue with using the model named "Emotional Classifier" after online download. Users must download and use the updated and supported version classifierdl_use_emotion from the Online Models page.
	
- **Duplication check for prompt name should be case-insensitive**

	The prompt name validation has been enhanced to be case insensitive, ensuring that creating duplicate prompt names is no longer possible. 
	
- **Error while Importing Tasks in JSON Format using URL**

    The issue has been fixed, allowing users to import JSON tasks directly from a URL without any errors.
	
- **State of the Previously Opened Project is still Available when Opening a New Project**

    When navigating to a different project, the state of the previously opened project was still retained, causing issues. This issue has been resolved, the state of the previously opened project is no longer saved.
	
- **Improved Pre-Annotation in case of Failure**

	Pre-annotation would fail for non pre-annotated tasks after pre-annotating incomplete tasks. In version 6.5.0, the entire pre-annotation process was improved and the issue above, fixed. 
	
- **Tasks cannot be imported for HTML Dialogues and Conversation project type**

This issue has been fixed, allowing the import of tasks for these project types.
	
- **Empty pre-annotation results when testing Classification models in Playground**

Text classification did not function correctly when classification models were tested in the playground. This issue has been fixed, classification models can be tested successfully with pre-annotation results in the Playground.
	
- **Annotators can view the unsaved completions of other annotators when "Allow Annotators to view Completion from Reviewers" is enabled**

In the previous versions, when the "Allow Annotators to View Completions from Reviewers" option was enabled, annotators could view not only their completions but also the unsaved completions by other annotators. This issue has been resolved in version 6.5.0. Now, annotators can only view their completions and the submitted completions from reviewers, specifically if a reviewer has cloned and submitted one of their completions.


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}