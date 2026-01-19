---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: LLM Evaluation & Comparison
permalink: /docs/en/alab/llm_eval
key: docs-training
modify_date: "2025-11-27"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

## LLM Evaluation Project Types with Multi-Provider Integration

Generative AI Lab provides specialized project types for evaluating and comparing responses from large language models (LLMs):

- **LLM Evaluation** – assess responses from a single LLM based on defined criteria  
- **LLM Comparison** – compare side-by-side responses from two or more LLMs for the same prompt

These projects enable structured model assessment, supporting both qualitative and quantitative scoring within the same collaborative annotation environment.

## Blind LLM Response Comparison

Blind LLM Response Comparison is used when you want reviewers to compare multiple responses without seeing which provider or model generated each response.

In blind comparison projects:

- Responses are displayed using neutral identifiers (for example, Response A, Response B, Response C)
- The ordering of responses is shuffled per task
- Provider and model identity is hidden during review

Depending on project configuration, reviewers may also be asked to **rank** responses (best to worst). Ranking can be required or optional based on how the project is configured.

### Supported LLM Providers

Generative AI Lab integrates with multiple leading LLM providers:

- **OpenAI**
- **Azure OpenAI**
- **Amazon SageMaker**
- **Anthropic Claude**

You can configure one or more providers globally from **System Settings → Integration**, where credentials for each service can be securely added.  
The procedure is consistent across providers: enter the required API keys or access tokens, validate, and save.  
Once configured, these providers are available for selection when creating LLM Evaluation or LLM Comparison projects.

![720image](/assets/images/annotation_lab/7.2.0/1.gif)

### Creating an LLM Evaluation Project

1. Navigate to the Projects page and click **New**.
2. After filling in the project details and assigning to the project team, proceed to the Configuration page.
3. Under the **Text** tab in step 1 (Content Type), select **LLM Evaluation** task and click **Next**.
4. On the **Select LLM Providers** page, you can either:
   - Click **Add** to create an external provider specific to the project (this provider will only be used within this project), or
   - Click **Go to External Service Page** to be redirected to the Integration page, associate the project with one of the supported external LLM providers, and return to **Project → Configuration → Select LLM Response Provider**
5. Choose the provider you want to use, save the configuration, and click **Next**.
6. Customize labels and choices as needed in the **Customize Labels** section, and save the configuration.

![720image](/assets/images/annotation_lab/7.2.0/2.gif)

For **LLM Comparison** projects, follow the same steps, but associate the project with **two or more** different external providers and select them on the **LLM Response Provider** page.

### Importing Prompts for LLM Evaluation (No Pre-Filled Responses)

To start working with prompts:

1. Go to the **Tasks** page and click **Import**.
2. Upload your prompts in either `.json` or `.zip` format using the structure below.

### Sample JSON for LLM Evaluation Project

```json
{
  "data": {
    "prompt": "Give me a diet plan for a diabetic 35 year old with reference links",
    "response1": "",
    "title": "DietPlan"
  }
}
```

### Sample JSON for LLM Comparison Project

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

### Importing Prompts and LLM Responses for Evaluation

Users can also import prompts and LLM-generated responses using a structured JSON format. This feature supports both LLM Evaluation and LLM Comparison project types and is useful when responses are generated outside Generative AI Lab.

Below are example JSON formats:

- **LLM Evaluation:** includes a prompt and one LLM response mapped to a provider
- **LLM Comparison:** supports multiple LLM responses to the same prompt

### Sample JSON for LLM Evaluation Project with Response

```json
{
  "data": {
    "prompt": "Give me a diet plan for a diabetic 35 year old with reference links",
    "response1": "Prompt Response 1 Here",
    "llm_details": [
      { "synthetic_tasks_service_provider_id": 1, "response_key": "response1" }
    ],
    "title": "DietPlan"
  }
}
```

### Sample JSON for LLM Comparison Project with Responses

```json
{
  "data": {
    "prompt": "Give me a diet plan for a diabetic 35 year old with reference links",
    "response1": "Prompt Response1 Here",
    "response2": "Prompt Response2 Here",
    "llm_details": [
      { "synthetic_tasks_service_provider_id": 1, "response_key": "response1" },
      { "synthetic_tasks_service_provider_id": 2, "response_key": "response2" }
    ],
    "title": "DietPlan"
  }
}
```

When used in blind comparison projects, imported responses are anonymized during review.

### Analytics Dashboard for LLM Evaluation Projects

A dedicated analytics tab provides quantitative insights for LLM evaluation projects:

- Bar graphs for each evaluation label and choice option
- Statistical summaries derived from submitted completions
- Multi-annotator scenarios prioritize submissions from highest-priority users
- Analytics calculations exclude draft completions (submitted tasks only)

![720image](/assets/images/annotation_lab/7.2.0/4.gif)

The general workflow for these projects aligns with the existing annotation flow in Generative AI Lab. The key difference lies in the integration with external LLM providers and the ability to generate model responses directly within the application for evaluation.

These project types provide teams with a structured approach to assess and compare LLM outputs efficiently, whether for performance tuning, QA validation, or human-in-the-loop benchmarking.
