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
- **Anthropic Claude**

### Setting Up LLM Provider Integration
1. Navigate to **Settings → System Settings → Integration**.
2. Click **Add**, enter your provider credentials, and save the configuration..
3. If a provider is added by a non-admin user, an admin must approve it before it can be used to generate responses.

![720image](/assets/images/annotation_lab/7.2.0/1.gif)

### Creating an LLM Evaluation Project

1. Navigate to the Projects page and click New.
2. After filling in the project details and assigning to the project team, proceed to the Configuration page.
3. Under the Text tab on step 1 - Content Type, select LLM Evaluation task and click on Next.
4. On the Select LLM Providers page, you can either:
   - Click Add button to create an external provider specific to the project (this provider will only be used within this project), or
   - Click Go to External Service Page to be redirected to Integration page, associate the project with one of the supported external LLM providers, and return to Project → Configuration → Select LLM Response Provider
5. Choose the provider you want to use, save the configuration and click on Next.
6. You can proceed without connecting an external provider by using a custom LLM configuration.
7. Customize labels and choices as needed in the Customize Labels section, and save the configuration.

![720image](/assets/images/annotation_lab/7.2.0/2.gif)

For **LLM Evaluation Comparison** projects, follow the same steps, but associate the project with **two** different external providers and select both on the **LLM Response Provider** page.

### Importing Prompts for LLM Evaluation (No Pre-Filled Responses)

## What to do

1. **Find the block that starts with** `To start working with prompts:` and ends right before the next heading.
2. **Replace that whole block** with the two subsections below.

---

### Importing prompts for LLM Evaluation or Comparison

To import prompts:

1. Go to the **Tasks** page and click **Import**.
2. Upload prompts in **JSON** or **CSV**.

**JSON format**
Provide an array of objects with a `text` field:

```json
[
  {"text": "Give me a diet plan for a diabetic 35 year old with reference links"},
  {"text": "Summarize the following discharge note and list medications separately"}
]
```

**CSV format**
Provide a CSV file with a single `text` column, one prompt per row.

After import, open a task and click **Generate Response** to fetch model outputs from the configured provider.

![720image](/assets/images/annotation_lab/7.2.0/3.gif)

After the responses are generated, users can evaluate them in the task interface.


### Importing prompts together with prefilled responses

Use this method when you already have one or more model responses that you want to include at import time.

**Sample JSON for LLM Evaluation Project**

```json
{
  "data": {
    "prompt": "Give me a diet plan for a diabetic 35 year old with reference links",
    "response1": "Model A response text here",
    "title": "DietPlan"
  }
}
```

**Sample JSON for LLM Evaluation Comparison Project**

```json
{
  "data": {
    "prompt": "Give me a diet plan for a diabetic 35 year old with reference links",
    "response1": "Model A response text here",
    "response2": "Model B response text here",
    "title": "DietPlan"
  }
}
```

You can add additional response fields if the project configuration expects them. The responses will appear in the task for side by side review.


### Annotation Comments

Each annotation in an LLM Evaluation or Comparison project can include a long-form comment for detailed explanations. Reviewers can add a comment to any highlighted selection, or example to explain why a passage is marked as a hallucination. These comments are separate from metadata fields and are saved with the annotation. Comments are visible in the annotation interface when you open a selection, and they are included in exported JSON.

### Importing Prompts and LLM Responses for Evaluation
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
- Multiple rating sections in one evaluation are supported.
- HyperTextLabels and choice fields are fully represented in the charts.


![720image](/assets/images/annotation_lab/7.2.0/4.gif)

The general workflow for these projects aligns with the existing annotation flow in Generative AI Lab. The key difference lies in the integration with external LLM providers and the ability to generate model responses directly within the application for evaluation.

These new project types provide teams with a structured approach to assess and compare LLM outputs efficiently, whether for performance tuning, QA validation, or human-in-the-loop benchmarking.
