---
layout: model
title: Pipeline to JSL_MedS_v4 (LLM - 8B - q8)
author: John Snow Labs
name: jsl_meds_8b_q8_v4_pipeline
date: 2025-08-16
tags: [licensed, en, clinical, meds, llm, ner, qa, summarization]
task: [Summarization, Named Entity Recognition, Question Answering]
language: en
edition: Healthcare NLP 6.1.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [jsl_meds_8b_q8_v4](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_8b_q8_v4_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_8b_q8_v4_pipeline_en_6.1.0_3.4_1755311112918.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_8b_q8_v4_pipeline_en_6.1.0_3.4_1755311112918.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("jsl_meds_8b_q8_v4_pipeline", "en", "clinical/models")

text = """<no_think></no_think>
A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus.
Which of the following is the best treatment for this patient?
A: Ampicillin
B: Ceftriaxone
C: Ciprofloxacin
D: Doxycycline
E: Nitrofurantoin
"""

result = pipeline.fullAnnotate(text)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("jsl_meds_8b_q8_v4_pipeline", "en", "clinical/models")

text = """<no_think></no_think>
A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus.
Which of the following is the best treatment for this patient?
A: Ampicillin
B: Ceftriaxone
C: Ciprofloxacin
D: Doxycycline
E: Nitrofurantoin
"""

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("jsl_meds_8b_q8_v4_pipeline", "en", "clinical/models")

val text = """<no_think></no_think>
A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus.
Which of the following is the best treatment for this patient?
A: Ampicillin
B: Ceftriaxone
C: Ciprofloxacin
D: Doxycycline
E: Nitrofurantoin
"""

val result = pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
<think>

</think>

The best treatment for this 23-year-old pregnant woman at 22 weeks gestation with **burning upon urination** (likely **urinary tract infection**, or UTI) is:

**E: Nitrofurantoin**

---

### Rationale:

- **Clinical presentation**: Burning upon urination, worsening despite increased fluid intake and cranberry extract, suggests a **urinary tract infection (UTI)**.
- **Pregnancy**: At 22 weeks gestation, the patient is in the second trimester.
- **UTI in pregnancy** is a common condition that requires prompt treatment to prevent complications such as pyelonephritis, preterm labor, or low birth weight.

### Why Nitrofurantoin is the best choice:

- **Nitrofurantoin** is **safe and effective** for treating uncomplicated UTIs in pregnancy, particularly in the **second and third trimesters**.
- It is **well-tolerated** and has **good urinary concentration**.
- It is **not associated with fetal malformations** when used appropriately.

### Why other options are less ideal:

- **Ampicillin (A)**: May be used in early pregnancy, but is **less effective** than nitrofurantoin for UTIs and may be **less preferred** due to potential resistance.
- **Ceftriaxone (B)**: A third-generation cephalosporin. While effective, it is **not typically first-line** for uncomplicated UTIs in pregnancy and may be **overused**.
- **Ciprofloxacin (C)**: **Contraindicated** in pregnancy due to potential risk of cartilage damage in the developing fetus.
- **Doxycycline (D)**: **Contraindicated** in pregnancy due to risk of **fetal tooth discoloration** and **bone development issues**.

---

### Conclusion:

**Nitrofurantoin (E)** is the best treatment option for this patient with a UTI at 22 weeks gestation.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_8b_q8_v4_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.1.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|8.4 GB|

## Included Models

- DocumentAssembler
- MedicalLLM