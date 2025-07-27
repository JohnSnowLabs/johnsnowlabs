---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: LLM Evaluation & Comparison
permalink: /docs/en/alab/llm_eval
key: docs-training
modify_date: "2025-07-24"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

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

![720image](/assets/images/annotation_lab/7.2.0/1.gif)

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

![720image](/assets/images/annotation_lab/7.2.0/2.gif)

For **LLM Evaluation Comparison** projects, follow the same steps, but associate the project with **two** different external providers and select both on the **LLM Response Provider** page.

### Sample Import Format for LLM Evaluation

To start working with prompts:

1.Go to the **Tasks** page and click **Import**.

2.Upload your prompts in either .json or .zip format. Following is a Sample JSON Format to import prompt:

**Sample JSON for LLM Evaluation Project**
```json
{
  "data": {
    "prompt": "Give me a diet plan for a diabetic 35 year old with reference links",
    "response1": "",
    "title": "DietPlan"
  }
}
```
**Sample JSON for LLM Evaluation Comparison Project**
```json
{
  "data": {
    "prompt": "Give me a diet plan for a diabetic 35 year old with reference links",
    "response1": "",
    "response2": "",
    "title": "DietPlan"
  }
}
```
3.Once the prompts are imported as tasks, click the **Generate Response** button to generate LLM responses.

![720image](/assets/images/annotation_lab/7.2.0/3.gif)

After responses are generated, users can begin evaluating them directly within the task interface.

### Sample Import Format for LLM Evaluation with Response
Users can also import prompts and LLM-generated responses using a structured JSON format. This feature supports both LLM Evaluation and LLM Evaluation Comparison project types.

Below are example JSON formats:

- **LLM Evaluation:** Includes a prompt and one LLM response mapped to a provider.
- **LLM Evaluation Comparison:** Supports multiple LLM responses to the same prompt, allowing side-by-side evaluation.

**Sample JSON for LLM Evaluation Project with Response**

```json
{
  "data": {
    "prompt": "Give me a diet plan for a diabetic 35 year old with reference links",
    "response1": "Prompt Respons1 Here",
    "llm_details": [
      { "synthetic_tasks_service_provider_id": 1, "response_key": "response1" }
    ],
    "title": "DietPlan"
  }
}
```
**Sample JSON for LLM Evaluation Comparision Project with Response**
```json
{
  "data": {
    "prompt": "Give me a diet plan for a diabetic 35 year old with reference links",
    "response1": "Prompt Respons1 Here",
    "response2": "Prompt Respons2 Here",
    "llm_details": [
      { "synthetic_tasks_service_provider_id": 1, "response_key": "response1" },
       { "synthetic_tasks_service_provider_id": 2, "response_key": "response2" }
    ],
    "title": "DietPlan"
  }
}
```


### Analytics Dashboard for LLM Evaluation Projects

A dedicated analytics tab provides quantitative insights for LLM evaluation projects:

- Bar graphs for each evaluation label and choice option
- Statistical summaries derived from submitted completions
- Multi-annotator scenarios prioritize submissions from highest-priority users
- Analytics calculations exclude draft completions (submitted tasks only)

![720image](/assets/images/annotation_lab/7.2.0/4.gif)

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

![720image](/assets/images/annotation_lab/7.2.0/5.png)

## Improvements
## Redesigned Annotation Interface for NER Projects
The annotation widget interface has been streamlined for Text and Visual NER project types. This update focuses on enhancing clarity, reducing visual clutter, and improving overall usability, without altering the core workflow. All previously available data remains intact in the exported JSON, even if not shown in the UI. 

### Enhancements in Name Entity Recognition and Visual NER Labeling Project Types
- Removed redundant or non-essential data from the annotation view.
- Grouped the Meta section visually to distinguish it clearly and associate the delete button specifically with metadata entries.
- Default confidence scores display (1.00) with green highlighting.
   Hover functionality on labeled text reveals text ID.

![720image](/assets/images/annotation_lab/7.2.0/6.png)