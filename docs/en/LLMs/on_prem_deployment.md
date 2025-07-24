---
layout: docs
header: true
seotitle: Medical LLMs | John Snow Labs
title: On-premise Deployment
permalink: /docs/en/LLMs/on_prem_deploy
key: docs-medical-llm
modify_date: "2025-07-17"
show_nav: true
sidebar:
    nav: medical-llm
---

<div class="h3-box" markdown="1">


## On Premise Deployment of John Snow Labs Medical LLMs

Deploying Medical LLMs within your infrastructure ensures complete control over your data and compliance with local security policies. This guide walks you through the steps to deploy a Medical LLM using Docker on your server.

**Prerequisites**: 
Before you begin, make sure the following are in place:
- John Snow Labs License: You need a valid John Snow Labs license file (license.json). Contact your account manager if you don’t have one.
- Docker Installed: Ensure Docker is installed and running on your machine. You can verify by running:

```bash
docker --version

```
*Note: For GPU acceleration, your system must have compatible NVIDIA GPUs with the NVIDIA Container Toolkit installed.*

John Snow Labs provides a ready-to-use Docker image for deploying the Medical LLMs on your own infrastructure. The image is available on [Docker Hub](https://hub.docker.com/r/johnsnowlabs/jsl-llms) and can be pulled using the following command:

```bash
docker pull johnsnowlabs/jsl-llms:latest
```

Use the command below to start the container. Replace <path_to_jsl_license> with the absolute path to your license file on the host machine; replace the <model> with the name of the LLM model you want to deploy (Medical-LLM-Small, Medical-LLM-Medium, etc. see the complete list in the table below): 

```bash
docker run -d \
--gpus all \
-v "<path_to_jsl_license>:/app/license.json" \
-p 8080:8080 \
--ipc=host \
johnsnowlabs/jsl-llms \
--model Medical-LLM-10B \
--port 8080
```

The following models are currently available for on-premise deployments:

| **Model Name** | **Parameters** | **Recommended GPU Memory** | **Max Sequence Length** | **Model Size** | **Max KV-Cache** | **Tensor Parallel Sizes** |
|----------------------------|------------|--------------|---------------------|------------|--------------|----------------------|
| Medical-LLM-8B             | 8B         | ~38 GB       | 40K                 | 15 GB      | 23 GB        | 1, 2, 4, 8           |
| Medical-LLM-10B            | 10B        | ~35 GB       | 32K                 | 19 GB      | 15 GB        | 1, 2, 4              |
| Medical-LLM-14B            | 14B        | ~40 GB       | 16K                 | 27 GB      | 13 GB        | 1, 2                 |
| Medical-LLM-24B            | 24B        | ~69 GB       | 32K                 | 44 GB      | 25 GB        | 1, 2, 4, 8           |
| Medical-LLM-Small          | 14B        | ~59 GB       | 40K                 | 28 GB      | 31 GB        | 1, 2, 4, 8           |
| Medical-LLM-Medium         | 70B        | ~452 GB      | 128K                | 131 GB     | 320 GB       | 4, 8                 |
| Medical-Reasoning-LLM-14B  | 14B        | ~58 GB       | 32K                 | 28 GB      | 30 GB        | 1, 2, 4, 8           |
| Medical-Reasoning-LLM-32B  | 32B        | ~111 GB      | 40K                 | 61 GB      | 50 GB        | 2, 4, 8              |
| Medical-VLM-24B            | 24B        | ~145 GB      | 128K                | 45 GB      | 100 GB       | 2, 4, 8              |
| Spanish-Medical-LLM-24B    | 24B        | ~145 GB      | 128K                | 45 GB      | 100 GB       | 2, 4, 8              |


> **Important Notes**
> 
> **Memory Calculations:** All memory calculations are based on half-precision (fp16/bf16) weights. Recommended GPU Memory considers the model size and the maximum key-value cache at the model's maximum sequence length. These calculations follow the guidelines from [DJL's LMI Deployment Guide.](https://docs.djl.ai/master/docs/serving/serving/docs/lmi/deployment_guide/instance-type-selection.html)
> 
> **Vision Language Model Limitations:** Medical-VLM-24B and Spanish-Medical-LLM-24B currently **only support text inference** for on-premise deployment. For full vision-language capabilities (both text and image processing), please use these models through [AWS SageMaker Marketplace](/docs/en/LLMs/on_aws) where these models support complete multimodal functionality.

</div>

### 🪄 Memory Optimization Tips

- Use smaller sequence lengths to reduce KV-cache memory
- Leverage tensor parallelism for large models
- Select an appropriate model based on your GPU resources


## Model Interactions
Once deployed, the container exposes a RESTful API for model interactions.

### Chat Completions
Use this endpoint for multi-turn conversational interactions (e.g., clinical assistants).

- **Endpoint**: `/v1/chat/completions`
- **Method**: POST
- **Example Request**:

```python
payload = {
    "model": "Medical-LLM-10B",
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
    "model": "Medical-LLM-10B",
    "prompt": "Provide a detailed explanation of rheumatoid arthritis treatment",
    "temperature": 0.7,
    "max_tokens": 4096
}
```






