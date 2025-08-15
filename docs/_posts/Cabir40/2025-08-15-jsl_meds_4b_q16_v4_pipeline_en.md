---
layout: model
title: Pipeline to JSL_MedS_v4 (LLM - 4B - q16)
author: John Snow Labs
name: jsl_meds_4b_q16_v4_pipeline
date: 2025-08-15
tags: [licensed, en, clinical, meds, llm, ner, qa, summarization]
task: [Summarization, Named Entity Recognition, Question Answering]
language: en
edition: Healthcare NLP 6.1.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [jsl_meds_4b_q16_v4](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_4b_q16_v4_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_4b_q16_v4_pipeline_en_6.1.0_3.0_1755260906819.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_4b_q16_v4_pipeline_en_6.1.0_3.0_1755260906819.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("jsl_meds_4b_q16_v4_pipeline", "en", "clinical/models")

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

pipeline = nlp.PretrainedPipeline("jsl_meds_4b_q16_v4_pipeline", "en", "clinical/models")

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

val pipeline = new PretrainedPipeline("jsl_meds_4b_q16_v4_pipeline", "en", "clinical/models")

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

The best treatment for this patient is:

**E: Nitrofurantoin**

### Rationale:
- The patient is a pregnant woman at 22 weeks gestation presenting with symptoms of a urinary tract infection (UTI) (burning upon urination).
- The symptoms have worsened despite increased fluid intake and cranberry extract.
- The physical examination is otherwise normal, with no costovertebral angle tenderness.
- The patient's vital signs are stable.

**Nitrofurantoin** is considered a safe and effective first-line antibiotic for treating uncomplicated UTIs in pregnant women. It has a favorable safety profile during pregnancy and is not associated with significant teratogenic effects.

**Why not the other options?**
- **Ampicillin (A)**: While it can be used in pregnancy, it is not the first-line treatment for UTIs.
- **Ceftriaxone (B)**: This is a broad-spectrum antibiotic that is not typically used for uncomplicated UTIs in pregnancy.
- **Ciprofloxacin (C)**: This is contraindicated in pregnancy due to potential risks to the fetus.
- **Doxycycline (D)**: This is contraindicated in pregnancy, especially in the first trimester, and is not recommended for use during pregnancy.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_4b_q16_v4_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.1.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|6.4 GB|

## Included Models

- DocumentAssembler
- MedicalLLM
