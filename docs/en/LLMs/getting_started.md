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


## On Premise Deployment

Prerequisites: A JSL License and Docker installed on your machine.

You can use our docker image to deploy the Medical LLM on your own infrastructure. The image is available on [Docker Hub](https://hub.docker.com/r/johnsnowlabs/jsl-llms) and can be pulled using the following command:

```bash
docker pull johnsnowlabs/jsl-llms:latest
```

Once you have the image, you can run it using the following command:

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


### Model Interactions

#### Chat Completions
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

#### Text Completions
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




### Supported Medical LLM Models

| **Model Name** | **Parameters** | **Recommended GPU Memory** |  **Max Sequence Length** | **Model Size** | **Max KV-Cache** |**Tensor Parallel Sizes**|
| Medical-LLM-7B | 7B | ~25GB | 32K | 14GB |10.50 GB | 1,2,4 |
| Medical-LLM-10B | 10B | ~35GB | 32K | 19GB |15.00 GB| 1,2,4 |
| Medical-LLM-14B | 14B | ~40FB | 16K | 28GB | 12.50GB | 1,2 |
| Medical-LLM-24B | 24B | ~70GB | 32K | 44GB | 25GB | 1,2,4,8  |
| Medical-LLM-Small | 14B | ~58GB | 32K | 28GB | 30GB | 1,2,4,8 |
| Medical-LLM-Medium | 70B | 452GB | 128K | 132GB | 320GB | 4, 8 |


*Memory Note: All memory calculations are based on half-precision (fp16/bf16) weights. Recommended GPU Memory considers the model size and the maximum key-value cache at the model's maximum sequence length. These calculations follow the guidelines from [DJL's LMI Deployment Guide.](https://docs.djl.ai/master/docs/serving/serving/docs/lmi/deployment_guide/instance-type-selection.html)*

#### Memory Optimization Tips

- Use smaller sequence lengths to reduce KV-cache memory
- Leverage tensor parallelism for large models
- Select an appropriate model based on your GPU resources

