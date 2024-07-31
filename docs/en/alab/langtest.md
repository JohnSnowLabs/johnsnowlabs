---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: LangTest
permalink: /docs/en/alab/langtest
key: docs-training
modify_date: "2024-06-12"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

## Test Suite Management
A Test Suite represents a collection of tests designed to evaluate your trained model across different scenarios. LangTest is a comprehensive framework for assessing AI language models in the Generative AI Lab, focusing on dimensions such as robustness, representation, and fairness. The framework subjects the models to a series of tests to evaluate their performance in these areas. Through iterative training cycles, the models are continuously improved until they achieve satisfactory results in these tests. This iterative process ensures that the models are well-equipped to handle diverse scenarios and meet essential requirements for reliable and effective language processing.

### Test Suites HUB
The new **"Test Suites HUB"** option under the Hub parent node, is the place where existing Test Suites are saved and managed. Clicking on Test Suites Hub takes the user to the **"Test Suite"** page, where all existing Test Suites he/she has access to are listed.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/1.png)


### Create, Update, and Delete Test Suites
Managing a Test Suite is easy: a Test Suite can be created using the **"Test"** page under a parent project and can be fully managed in the **"Test Suite"** page within the **"Test Suites HUB"** option where users can create, update, and delete test suites.

#### Test Suite Creation
Creating a new Test Suite from the **"Test Suite"** page is straightforward:

1.  In the Test Suite page, click on the **"New"** button to open the **"Add Test Suite"** form.
2.  Provide a name (mandatory) and a description (optional) for the test suite.
3.  Under **"TESTS"**, select the desired category and click on it to expand and view all available test types within that category. (Category samples - **Robustness**, **Bias**,etc.). 
4.  Choose the desired test types by selecting the checkboxes for the relevant categories.
5.  Provide or modify the necessary details for each selected test type.
6.  Apply the steps above for any number of different categories you require to configure the test suite.
7.  Save your work, when configuration is complete by clicking on the **"Save"** button.

**Note**: The Model type is set to "NER" and cannot be changed, as Generative AI Lab supports only testing NER models in this version.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/2.gif)

### Supported Test Categories
The following are the currently supported categories for NER models within the Generative AI Lab application, available through the LangTest framework:

**1. ACCURACY**
The goal of the Accuracy is to give users real, useful insights into how accurate the model is. It’s all about helping the user make smart choices on when and where to use the model in real-life situations. Accuracy tests evaluate the correctness of a model's predictions. This category comprises six test types, three of which - **"Min F1 Score"**, **"Min Precision Score"** and **"Min Recall Score"** - require the user to provide model labels. The user can add labels in the "Add Model Labels" section, which becomes active immediately after selecting the corresponding checkbox for the test. Labels can be added or removed as shown below:

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/3.gif)
 
For more details about Accuracy tests, visit the [LangTest Accuracy Documentation](https://langtest.org/docs/pages/tests/accuracy).

**Note:** Tests using custom labels require tasks with ground truth data.

**2. BIAS**
Model bias tests aim to gauge how well a model aligns its predictions with actual outcomes. Detecting and mitigating model bias is essential to prevent negative consequences such as perpetuating stereotypes or discrimination. This testing explores the impact of replacing documents with different genders, ethnicities, religions, or countries on the model’s predictions compared to the original training set, helping identify and rectify potential biases
LangTest framework provides support for more than 20 distinct test types for the Bias category. 

For detailed information on Bias category, supported tests and samples, please refer to the [LangTest Bias Documentation](https://langtest.org/docs/pages/docs/test_categories#bias-tests).

**3. FAIRNESS**
Fairness testing is essential to evaluate a model’s performance without bias, particularly concerning specific groups. The goal is to ensure unbiased results across all groups, avoiding favoritism or discrimination. Various tests, including those focused on attributes like gender, contribute to this evaluation, promoting fairness and equality in model outcomes.

This category comprises two test types: **"Max Gender F1 Score"** and **"Min Gender F1 Score"**. 

Further information on Fairness tests can be accessed through the [LangTest Fairness Documentation](https://langtest.org/docs/pages/docs/test_categories#fairness-tests).

**4. PERFORMANCE**
Performance tests gauge the efficiency and speed of a language model's predictions. This category consists of one test type: **"speed"** which evaluates the execution speed of the model based on tokens.

Further information on Performance test can be accessed through the [LangTest Performance Documentation](https://langtest.org/docs/pages/tutorials/test_specific_notebooks/performance).

**5. REPRESENTATION**
Representation testing assesses whether a dataset accurately represents a specific population. It aims to identify potential biases within the dataset that could impact the results of any analysis, ensuring that the data used for training and testing is representative and unbiased. 

For additional details on Representation tests, please visit the [LangTest Representation Documentation](https://langtest.org/docs/pages/tests/representation).

**6. ROBUSTNESS**
Model robustness tests evaluate a model’s ability to maintain consistent performance when subjected to perturbations in the data it predicts. For tasks like Named Entity Recognition (NER), these tests assess how variations in input data, such as documents with typos or fully uppercased sentences, impact the model’s prediction performance. This provides insights into the model’s stability and reliability.

More information on Robustness tests is available in the [LangTest Robustness Documentation](https://langtest.org/docs/pages/docs/test_categories#robustness-tests).

#### **Managing Test Suites**
To edit an existing Test Suite, navigate to the **"Test Suites"** page and follow these steps:

1. Click on the three dots at the top-right corner of the test suite card to display the three options available: **"Export"**, **"Edit"**, and **"Delete"**.
2.  Selecting "Edit" takes you to the "Edit Test Suite" page. 
3. Modify the description as necessary.
4.  Under **"LIST OF TESTS"**, view all previously configured test categories and test types. Use the filter functionality to faster lookup the test category you need to edit.
Selecting a test category will display its associated test types and corresponding pre-configured values. Clicking on the three dots next to a test type will present two options: **"Edit"** and **"Delete"**. Choosing **"Delete"** will deselect the test type, while selecting **"Edit"** will redirect you to the corresponding test type under **TESTS**, where you can modify the test type values. You can directly edit each test type within the **TESTS** section of the test suite.
5. Click the **"Save"** button to apply the changes.

**Note**: Name and Model Type of a test suite cannot be modified.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/4.gif)
 
 **Full-screen Mode and Search**
To boost productivity, you can create or edit a test suite using full-screen mode and the search functionality to quickly locate specific tests within the **"TESTS"** section.
 
 ![GenaiImage](/assets/images/annotation_lab/6.2.0/5.gif)

 **Test Suite Deletion**

To delete a test suite from the **"Test Suite"** page, follow these steps:

1. Locate the test suite you wish to delete and click on the three dots next to it. This will reveal three options: **"Export"**, **"Edit"**, and **"Delete"**.
2. Select the **"Delete"** option.
3. A pop-up box will be shown. Click the **"Yes"** option.
4. The test suite will be deleted, and a deletion message will confirm the action.

**Note**: a test suite used within at least one project in your enterprise cannot be deleted.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/6.gif)

### Importing and Exporting Test Suites
Users can export and import test suites using the **"Test Suites HUB"**. To export a test suite from the **"Test Suite"** page, follow these simple steps:

1. Click on the ellipsis symbol located next to the test suite you wish to export. This will present three options: **"Export"**, **"Edit"**, and **"Delete"**.
2. Click on the **"Export"**.
3. Upon selecting **"Export"**, the test suite will be saved as **<test_suite_name>.json**, and a confirmation message indicating successful export will appear.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/7.gif)

Users can import a test suite into the **"Test Suites HUB"** by following these few steps:

1. Navigate to the **"Test Suite"** page and click on the **"Import"** button to open the **"Import Test Suite"** page.
2.  Either drag and drop the test suite file into the designated area or click to import the test suite file from your local file system.
3. Upon successful import, a confirmation message will be displayed.
4. You can then view the imported test suite on the **"Test Suite"** page.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/8.gif)
 
### Searching for a specific Test Suite
Use the search feature on the **"Test Suite"** page, the **"SEARCH TEST SUITES ..."** search bar to find the desired Test Suite, by matching it’s name.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/9.gif)
 
### New "Test" page under Project Menu
A new entry, **"Test"** has been added under the project menu in the left navigation bar for NER projects. Clicking on the **"Test"** node in the left navigation bar will take the user to the **"Test"** page, where they can manage tests and execute model testing.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/10.png)
 
On this page, project managers can configure tests settings and corresponding parameters, create and edit test cases, start and stop model testing, review test logs, and review, download, or delete test results. 

**Note**: The functionality available on the Test page is exclusively available to users with project manager roles.

#### Test - setup and configuration**

Navigating to the **"Test”** page under a specific project, allows the user to specify what tests will be used to assess the quality of the project’s model.

There are two mandatory sections that need to be filled:

**1. Select Model:**
Select the NER model pretrained/trained that is used to predict annotations for the tasks/documents in the current project. The user can choose a NER model from the dropdown. All available models configured within the project are listed in this dropdown menu for selection.

**2. Select Test Suite:**
The test suite comprises a collection of tests designed to evaluate your trained model in various scenarios.

The user can choose an existing test suite from the dropdown menu or create a new one by clicking on "+ Create New Test Suite" within the dropdown menu. 

**Note**: The option to create a new test suite is available only to supervisor and admin users with the manager role.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/11.gif)
 
There are two configuration options available in the "Test Parameters" section; they are optional:

**1. Filter completions by:**

This option enables users to narrow down their analysis by selecting tasks based on their completion status.
The available options are:

- **Clear "Filter completions by"**: Removes selected completion filters.
- **Submitted completions**: Select only tasks with submitted completions for analysis.
- **Reviewed completions**: Select only tasks with reviewed completions for analysis.

**2. Filter test by tag:**

This functionality enables users to refine their analysis by selecting only project tasks associated with specific tags. 
By default, the dropdown includes all default tags such as "Validated", "Test", "Corrections Needed", and "Train", as well as any custom tags created within the project. 

Users can select tags to focus the model testing execution on the specific tagged tasks; if no tags are selected, all tasks will be considered for analysis.

Users have two methods to select Test Settings and Test Parameters:

**1. Direct Selection Method (Without Wizard Mode):**
 - Go to the **"Test"** page.
 - In the Test Settings section, choose a model from the **"Select Model"** dropdown.
 - Within the Testing Parameters section, pick completions from the **"Filter completions by"** dropdown.
 - Also within Testing Parameters, select tags from the **"Filter test by tag for testing"** dropdown.
 - Click the **"Save"** button to confirm your selections and save the configuration.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/12.gif)
 
**2. Wizard Mode (Guided Setup):**

 - Click the **"Wizard"** button to initiate Wizard mode. This will reveal the **"Test Setting"** tab, offering detailed information about Model Selection and Test Suite.
 - From the **"Select Model"** dropdown, choose a model.
 - Select a test suite from the dropdown or create a new one by clicking on **"+ Create New Test Suite"**.
 - Click "Next" to proceed to the **"Test Parameters"** tab, where you'll see detailed information about **"Filter completions by"** and **"Tags"**.
 - Within the **"Filter completions by"** dropdown, select the appropriate option.
 - Choose one or more tags, or none, from the **"Filter test by tag for testing"** dropdown.
 - Click **"Next"** to save the Test Settings and Parameters.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/13.gif)
 
To modify the Test Settings and Parameters, simply click on the **"Edit"** icon.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/14.png)

####  Generating Test Cases
After saving the Test Settings and Parameters, the following options become available: **"Generate Test Cases"**, **"Start Testing"**, and **"Edit"**. 
Users must generate test cases and conduct testing independently. 

Clicking on **"Generate Test Cases"** will produce test cases based on the saved Test Settings and Parameters. The generated test cases will appear under the "Test Cases" tab.

**Note**: 
Only Bias and Robustness test cases can be edited and updated; other test cases are not editable.

Modifying Test Settings or Parameters and generating new test cases will discard any existing ones. If no relevant tasks or data are available, no test cases will be generated.


 ![GenaiImage](/assets/images/annotation_lab/6.2.0/15.gif)

#### Start Model Testing
When **"Start Testing"** is clicked, model testing commences based on the generated test cases and the configured test settings. To view the test logs, click on **"Show Logs"**. The testing process can be halted by clicking on **"Stop Testing"**. If no test cases have been generated, the **"Start Testing"** option will be disabled, preventing the user from initiating testing.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/16.gif)

If any changes are made to the Test Settings that differ from those used to generate the test cases, clicking on "Start Testing" will trigger a pop-up notification informing the user of the configuration change. The user must either ensure that the Test Settings and Parameters match those used for test case generation or create new test cases based on the updated configuration to proceed with model testing.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/17.png)

#### View and Delete Test Results 
Once the execution of model testing is complete, users can access the test results via the **"Test Results History"** section in the **"Test Results"** tab. 

Under this tab, the application displays all the “test runs” and corresponding results, for every test previously conducted for the project.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/18.png)

Clicking on **"Show Results"** will display the results for the selected test execution run. The test results consist of two reports:

**1. Result Metrics:**

This section of the results provides a summary of all tests performed, including their status. It includes details such as **"Number"**, **"Category"**, **"Test Type"**, **"Fail Count"**, **"Pass Count"**, **"Pass Rate"**, **"Minimum Pass Rate"** and **"Status"**.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/19.png)

**2. Detailed Report:**

The detailed report contains information about each test case within the selected tests. It includes **"Number"**, **"Category"**, **"Test Type"**, **"Original"**,**"Test Case"**, **"Expected Results"**, **"Actual Results"** and **"Status"**.

In this context, **"Expected Results"** refer to the prediction output by the testing model on the **"Original"** data, while **"Actual Results"** indicate the prediction output by the testing model on the **"Test Case"** data generated. A test is considered passed if the **"Expected Results"** match the **"Actual Results"**; otherwise, it is deemed failed.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/20.png)

Users have the option to simultaneously download both reports in CSV format by selecting the download button.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/21.png)

For a detailed report, users can enter full-screen mode by clicking the full-screen button.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/22.gif)

Furthermore, users can delete test results from the **"Test Results History"** by selecting the three dots followed by the **"Delete"** button.

 ![GenaiImage](/assets/images/annotation_lab/6.2.0/23.gif)