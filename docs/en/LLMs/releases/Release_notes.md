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

- **Medical-LLM-Medium**: This model is an advanced clinical decision-support system built for structured medical reasoning rather than simple knowledge retrieval. It analyzes symptoms, diagnostics, and longitudinal patient histories to guide complex diagnostic and treatment decisions in line with established clinical guidelines. With multimodal vision capabilities, it can also interpret medical images and visual documents alongside text, broadening the range of clinical inputs it can reason over. Now grounded in curated, specialty-specific medical knowledge bases, it anchors conclusions to vetted clinical evidence for greater factual reliability. It delivers transparent, step-aware reasoning, weighs competing hypotheses, and communicates uncertainty to support risk-aware clinical judgment.

#### Specifications

| **Model Name**             | **Parameters** | **Recommended GPU Memory** | **Max Sequence Length** | **Model Size** | **Max KV-Cache** | **Tensor Parallel Sizes** |
|---------------------------|----------------|----------------------------|-------------------------|----------------|------------------|--------------------------|
| Medical-LLM-Medium | 27B            | ~67 GB                     | 262K                    | 51 GB          | 16 GB            | 2, 4, 8                  |

#### Benchmark Performance – Medical-LLM-Medium

- Achieves 95.5% average across OpenMed benchmarks
- Medical genetics: 99%; Professional medicine: 98%
- Clinical knowledge comprehension: 96%; College biology mastery: 98%
- RaceBias: 96%; Anatomy: 95%
- Achieves 76% on Medec and 84% on PubMedQA
- Safety & reliability: 96.7% on hallucination detection, inappropriate-content avoidance, and refusal of unethical or illegal requests
- Fairness & bias: 98% pass rate on name bias, 95% on racial bias detection, and 96% on anchoring-bias resistance

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

