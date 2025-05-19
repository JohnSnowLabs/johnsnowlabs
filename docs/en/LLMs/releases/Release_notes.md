---
layout: docs
header: true
seotitle: Medical LLMs | John Snow Labs
title: Release Notes
permalink: /docs/en/LLMs/releases/release_notes
key: docs-medical-llm
modify_date: "2025-05-19"
show_nav: true
sidebar:
    nav: medical-llm
---

<div class="h3-box" markdown="1">

## 05-19-2025

We are excited to announce the addition of two new powerful models to our Medical LLM lineup.

- **Medical-VLM-24B**: A 24B parameter vision-language model that combines medical expertise with visual comprehension capabilities. This model excels at processing both medical images (X-rays, MRIs, pathology slides) and text, enabling comprehensive analysis of visual and textual medical data.

- **Spanish-Medical-LLM-24B**: A specialized 24B parameter model designed for Spanish-speaking healthcare environments, offering native processing of Spanish medical terminology and clinical documentation. The model maintains high precision in Spanish medical language understanding without requiring translation.

#### Specifications

| **Model Name**             | **Parameters** | **Recommended GPU Memory** | **Max Sequence Length** | **Model Size** | **Max KV-Cache** | **Tensor Parallel Sizes** |
|---------------------------|--------------|------------------|-------------------|-------------|----------------|------------------------|
| Medical-VLM-24B           | 24B         | ~145 GB          | 128K              | 45 GB       | 100 GB         | 2, 4, 8               |
| Spanish-Medical-LLM-24B   | 24B         | ~145 GB          | 128K              | 45 GB       | 100 GB         | 2, 4, 8               |

## 04-06-2025

**Welcome to John Snow Labs Medicall LLMs on premise deployments Documentation and Updates Hub!**

We are excited to announce the launch of the on premise deplyment of our Medical LLM models page, a centralized repository for all the latest features, enhancements, and resolutions of known issues within the. This dedicated space is designed to keep users informed of the most recent developments, enabling seamless testing and facilitating the provision of valuable feedback. Our commitment is to ensure that users have immediate access to the latest information, empowering them to leverage the full capabilities of out Medical LLM models effectively. Stay updated with us as we continue to improve and expand the functionalities of our Medical LLMs to meet and exceed your expectations.

### Supported Medical LLM Models

| **Model Name** | **Parameters** | **Recommended GPU Memory** | **Max Sequence Length** | **Model Size** | **Max KV-Cache** | **Tensor Parallel Sizes** |
|----------------------------|------------|--------------|---------------------|------------|--------------|----------------------|
| Medical-LLM-7B             | 7B         | ~25 GB       | 16K                 | 14 GB      | 11 GB        | 1, 2, 4              |
| Medical-LLM-10B            | 10B        | ~35 GB       | 32K                 | 19 GB      | 15 GB        | 1, 2, 4              |
| Medical-LLM-14B            | 14B        | ~40 GB       | 16K                 | 27 GB      | 13 GB        | 1, 2                 |
| Medical-LLM-24B            | 24B        | ~69 GB       | 32K                 | 44 GB      | 25 GB        | 1, 2, 4, 8           |
| Medical-LLM-Small          | 14B        | ~58 GB       | 32K                 | 28 GB      | 30 GB        | 1, 2, 4, 8           |
| Medical-LLM-Medium         | 70B        | ~452 GB      | 128K                | 131 GB     | 320 GB       | 4, 8                 |
| Medical-Reasoning-LLM-14B  | 14B        | ~58 GB       | 32K                 | 28 GB      | 30 GB        | 1, 2, 4, 8           |
| Medical-Reasoning-LLM-32B  | 32B        | ~222 GB      | 128K                | 61 GB      | 160 GB       | 2, 4, 8              |

</div>
