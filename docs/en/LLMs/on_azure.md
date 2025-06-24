---
layout: docs
header: true
seotitle: Medical LLMs| John Snow Labs
title: Deploy LLMs as Private Azure Endpoints
permalink: /docs/en/LLMs/on_azure
key: docs-medical-llm
modify_date: "2025-03-31"
show_nav: true
sidebar:
    nav: medical-llm
---

The LLMs listed below are available on Azure.

**All LLMs on AWS Sagemaker are Open AI compatible.**

[Medical LLM Medium]()

[Medical LLM Small]()

[Medical LLM - 14B]()

[Medical LLM - 10B]()

[Medical LLM- 7B]()

[Medical Reasoning LLM - 14B]()

[Medical Reasoning LLM - 32B]()


## Deployment Instructions

1. Subscribe to the Product from the models listing page using the `Get It Now` button.
![azure_subscribe](/assets/images/med_llms/azure_subscribe.png)

2. Create a virtual machine of the product. Make sure port 80 is open for inbound requests.

    ***Optional**, open port 3000 for Open Web UI interface.*
    ![launch_azure_product](/assets/images/med_llms/azure_launch.png)
3. Wait for the services to be active. This might take few minutes for the initial boot.
<br/>
    To check the status, login to the instance and run this command
<br/>
`sudo systemctl status med-llm.service`
4. Once all the status is active, access the model api docs from http://INSTANCE_IP/docs


## Model Interactions
Once deployed, the container exposes a RESTful API for model interactions.

### Chat Completions
Use this endpoint for multi-turn conversational interactions (e.g., clinical assistants).

- **Endpoint**: `/v1/chat/completions`
- **Method**: POST
- **Example Request**:

```python
payload = {
    "model": "Medical-LLM-7B",
    "messages": [
        {"role": "system", "content": "You are a professional medical assistant"},
        {"role": "user", "content": "Explain symptoms of chronic fatigue syndrome"}
    ],
    "temperature": 0.7,
    "max_tokens": 1024
}
```

### Text Completions
Use this endpoint for single-turn prompts or generating long-form medical text.

- **Endpoint**: `/v1/completions`
- **Method**: POST
- **Example Request**:
```python
payload = {
    "model": "Medical-LLM-7B",
    "prompt": "Provide a detailed explanation of rheumatoid arthritis treatment",
    "temperature": 0.7,
    "max_tokens": 4096
}
