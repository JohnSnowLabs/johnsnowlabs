---
layout: docs
header: true
seotitle: Medical LLMs| John Snow Labs
title: Deploy LLMs as Private Databricks Endpoints
permalink: /docs/en/LLMs/on_databricks
key: docs-medical-llm
modify_date: "2025-12-30"
show_nav: true
sidebar:
    nav: medical-llm
---

<div class="h3-box" markdown="1">

The LLMs listed below are available on Databricks Marketplace as Model Serving Endpoints.

[Medical-LLM-Medium](https://marketplace.databricks.com/details/6955d25d-2dda-4517-8a26-5dc3239e6995/John-Snow-Labs_MedicalLLMMedium)

[Medical LLM - Small](https://marketplace.databricks.com/details/2d3cabaf-e93e-45e0-a954-82202000afd8/John-Snow-Labs_Medical-LLM-Small)

[Vision OCR LLM](https://marketplace.databricks.com/details/c90c05de-8957-443d-8e1d-b73358d82b67/John-Snow-Labs_Vision-OCR-LLM)

[Vision OCR Structured LLM](https://marketplace.databricks.com/details/e5063101-57bb-4523-baa0-48da9cf6d4ab/John-Snow-Labs_Vision-OCR-Structured)

</div><div class="h3-box" markdown="1">

## Deployment Instructions

1. Click **Get access** on the model listing page in Databricks Marketplace.

2. Once access is granted, click the **Open** button to view the model and available versions.

3. Select the model version with the **production** alias (recommended for stable deployments) and click **Serve this model**.

4. In the **Create serving endpoint** configuration:
   
   - **Compute type**: Select the appropriate compute type based on your workload requirements. Refer to the [memory requirements table](https://nlp.johnsnowlabs.com/docs/en/LLMs/medical_llm#medical-llms-offering) to determine the approximate memory needed for your selected model.
   
   - **Environment variables**: Add the following required environment variable:
     ```
     SPARK_NLP_LICENSE="your-license-key"
     ```

5. Complete the serving endpoint configuration and click **Create**.

6. Wait for the endpoint to become active.

**Note**: Each model listing includes a detailed notebook with comprehensive instructions for creating serving endpoints using the Databricks API, along with inference examples and supported formats.

</div>
