---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: LLM Evaluation & Comparison
permalink: /docs/en/alab/llm_eval
key: docs-training
modify_date: "2025-07-28"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

## LLM Evaluation Project Types with Multi-Provider Integration


You can now systematically evaluate and compare the outputs of large language models (LLMs) using two specialized project types in Generative AI Lab:
- **LLM Evaluation:**  Assess responses from a single LLM based on custom criteria.
- **LLM Evaluation Comparison:** Compare side-by-side outputs from two different LLMs for the same prompt.

These project types support integration with major LLM providers:
- **OpenAI**
- **Azure OpenAI**
- **Amazon SageMaker**

### Setting Up LLM Provider Integration
1. Navigate to **Settings → System Settings → Integration**.
2. Click **Add**, enter your provider credentials, and save the configuration..

![720image](/assets/images/annotation_lab/7.2.0/1.gif)

### Creating an LLM Evaluation Project

1. Navigate to the Projects page and click New.
2. After filling in the project details and assigning to the project team, proceed to the Configuration page.
3. Under the Text tab on step 1 - Content Type, select LLM Evaluation task and click on Next.
4. On the Select LLM Providers page, you can either:
   - Click Add button to create an external provider specific to the project (this provider will only be used within this project), or
   - Click Go to External Service Page to be redirected to Integration page, associate the project with one of the supported external LLM providers, and return to Project → Configuration → Select LLM Response Provider
5. Choose the provider you want to use, save the configuration and click on Next.
6. Customize labels and choices as needed in the Customize Labels section, and save the configuration.

![720image](/assets/images/annotation_lab/7.2.0/2.gif)

For **LLM Evaluation Comparison** projects, follow the same steps, but associate the project with **two** different external providers and select both on the **LLM Response Provider** page.

### Importing Prompts for LLM Evaluation (No Pre-Filled Responses)

To start working with prompts:

1. Go to the **Tasks** page and click **Import**.

2. Upload your prompts in either .json or .zip format using the structure below. 

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
3. Once the prompts are imported as tasks, click the **Generate Response** button to fetch LLM responses directly from the configured providers.

![720image](/assets/images/annotation_lab/7.2.0/3.gif)

After the responses are generated, users can begin evaluating them directly within the task interface.

### Importing Promtps and LLM Responses for Evaluation
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
