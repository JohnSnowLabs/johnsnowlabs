---
layout: docs
header: true
seotitle: Medical LLMs | John Snow Labs
title: Release Notes
permalink: /docs/en/LLMs/releases/release_notes
key: docs-medical-llm
modify_date: "2026-09-14"
show_nav: true
sidebar:
    nav: medical-llm
---

<div class="h3-box" markdown="1">

## 09-14-2026

### Model Updates

We're excited to announce an updated version of our Medical-LLM-Medium model, delivering enhanced structured medical reasoning and multimodal capabilities.

- **Medical-LLM-Medium**: This version of the Medical-LLM-Medium improves the overall OpenMed benchmark average from **94.5% to 95.5%**. The largest comparable gain is in **Anatomy (+2.0 points)**, followed by **anchoring-bias resistance (+1.33 points)** and **safety & reliability (+1.2 points)**. Clinical knowledge comprehension and racial bias detection each improve by 1 point, while already strong performance in medical genetics, professional medicine, PubMedQA, and name bias remains unchanged.

#### Specifications

| **Model Name**             | **Parameters** | **Recommended GPU Memory** | **Max Sequence Length** | **Model Size** | **Max KV-Cache** | **Tensor Parallel Sizes** |
|---------------------------|----------------|----------------------------|-------------------------|----------------|------------------|--------------------------|
| Medical-LLM-Medium | 27B            | ~67 GB                     | 262K                    | 51 GB          | 16 GB            | 2, 4, 8                  |

#### Benchmark Performance – Medical-LLM-Medium

Side by side comparison with previous version

{:.table-model-big}
| **Metric** | **Previous (07-23-2026)** | **New (09-14-2026)** | **Absolute Change** | **Relative Change** |
|---|---|---|---|---|
| **OpenMed average** | 94.5% | 95.5% | **+1.0 pt** | **+1.06%** |
| Medical genetics | 99% | 99% | No change | 0% |
| Professional medicine | 98% | 98% | No change | 0% |
| Clinical knowledge comprehension | 95% | 96% | **+1.0 pt** | **+1.05%** |
| Anatomy | 93% | 95% | **+2.0 pts** | **+2.15%** |
| PubMedQA | 84% | 84% | No change | 0% |
| Safety & reliability | 95.5% | 96.7% | **+1.2 pts** | **+1.26%** |
| Name bias | 98% | 98% | No change | 0% |
| Racial bias detection | 94% | 95% | **+1.0 pt** | **+1.06%** |
| Anchoring-bias resistance | 94.67% | 96% | **+1.33 pts** | **+1.40%** |


## 07-23-2026

### Model Updates

We're excited to announce a major new version of our Medical-Medium-LLM model, representing a significant advancement in AI-powered clinical decision support with enhanced structured medical reasoning capabilities.

- **Medical Medium LLM**: The new model demonstrates <b>broader and more balanced performance improvements</b>, increasing the overall OpenMed benchmark average from <b>93.0% to 94.5%</b>. The most significant gains are in <b>PubMedQA (+6 points)</b> and <b>anchoring-bias resistance (+3 points)</b>, indicating better clinical reasoning and improved robustness against cognitive bias. Safety also improved, while maintaining industry-leading scores in medical genetics and professional medicine.



Side by side comparison with previous version


{:.table-model-big}
| **Metric**             | **Old** | **New** | **Absolute Change** | **Relative Change** |
|---------------------------|----------------|----------------------------|-------------------------|--------------------------|
| **OpenMed average** | 93.0% | 94.5% | **+1.5 pts** |**+1.61%**  |
| Medical genetics | 99% | 99% | No change | 0%  |
| Professional medicine| 98% | 98%| No change| 0%  |
| Clinical knowledge comprehension | 94% | 95% | +1.0 pt| **+1.06%**|
| Anatomy | 92% | 93% | **+1.0 pt**| **+1.09%**|
| MedQA | 93.5% | 94.7% | **+1.2 pts**| **+1.28%**|
| PubMedQA | 78% | 84% | **+6.0 pts**| **+7.69%**|
| Safety & reliability| 94.5% | 95.5% | **+1.0 pt**| **+1.06%**|
| Name bias | 98% | 98%  | No change|  0%  |
| Racial bias | 93% | 94% | **+1.0 pt**| **+1.08%**|
| Anchoring-bias resistance | 91.67% | 94.67% | **+3.0 pts**| **+3.27%**|

##### Summary of improvements

**Major improvements**

- PubMedQA: +6.0 percentage points (7.7% relative improvement)  

- Anchoring-bias resistance: +3.0 percentage points  

- OpenMed overall average: +1.5 percentage points  

**General improvements**

- Clinical knowledge comprehension: +1.0 point  

- Anatomy: +1.0 point  

- MedQA: +1.2 points  

- Safety & reliability: +1.0 point  

- Racial bias detection: +1.0 point

