---
layout: docs
header: true
seotitle: Medical LLMs | John Snow Labs
title: Getting Started
permalink: /docs/en/LLMs/getting_started
key: docs-medical-llm
modify_date: "2024-03-31"
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

Use the command below to start the container. Replace <path_to_jsl_license> with the absolute path to your license file on the host machine; replace the <model> with the name of the LLM model you want to deploy (Medical-LLM-7B, Medical-LLM-10B, Medical-LLM-14B, Medical-LLM-24B, Medical-LLM-Small, Medical-LLM-Medium): 

```bash
docker run -d \
--gpus all \
-v "<path_to_jsl_license>:/app/license.json" \
-p 8080:8080 \
--ipc=host \
johnsnowlabs/jsl-llms \
--model Medical-LLM-7B \
--port 8080
```

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
```




## Medical LLMs Offering

| **Model Name** | **Parameters** | **Recommended GPU Memory** |  **Max Sequence Length** | **Model Size** | **Max KV-Cache** |**Tensor Parallel Sizes**|
| Medical-LLM-7B | 7B | ~25GB | 32K | 14GB |10.50 GB | 1,2,4 |
| Medical-LLM-10B | 10B | ~35GB | 32K | 19GB |15.00 GB| 1,2,4 |
| Medical-LLM-14B | 14B | ~40FB | 16K | 28GB | 12.50GB | 1,2 |
| Medical-LLM-24B | 24B | ~70GB | 32K | 44GB | 25GB | 1,2,4,8  |
| Medical-LLM-Small | 14B | ~58GB | 32K | 28GB | 30GB | 1,2,4,8 |
| Medical-LLM-Medium | 70B | 452GB | 128K | 132GB | 320GB | 4, 8 |


*Note: All memory calculations are based on half-precision (fp16/bf16) weights. Recommended GPU Memory considers the model size and the maximum key-value cache at the model's maximum sequence length. These calculations follow the guidelines from [DJL's LMI Deployment Guide.](https://docs.djl.ai/master/docs/serving/serving/docs/lmi/deployment_guide/instance-type-selection.html)*


