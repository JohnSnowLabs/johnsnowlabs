---
layout: docs
header: true
seotitle: Medical LLMs | John Snow Labs
title: Release Notes
permalink: /docs/en/LLMs/releases/release_notes
key: docs-medical-llm
modify_date: "2026-07-23"
show_nav: true
sidebar:
    nav: medical-llm
---

<div class="h3-box" markdown="1">

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

