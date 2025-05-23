---
layout: model
title: Pipeline to Extract Entities Related to TNM Staging
author: John Snow Labs
name: ner_oncology_tnm_pipeline
date: 2023-03-09
tags: [licensed, en, clinical, oncology, ner]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.3.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_oncology_tnm](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_tnm_en.html) model.

## Predicted Entities

`Cancer_Dx`, `Lymph_Node`, `Metastasis`, `Tumor_Description`, `Staging`, `Tumor`, `Lymph_Node_Modifier`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_tnm_pipeline_en_4.3.0_3.2_1678352273944.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_tnm_pipeline_en_4.3.0_3.2_1678352273944.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_oncology_tnm_pipeline", "en", "clinical/models")

text = '''The final diagnosis was metastatic breast carcinoma, and it was classified as T2N1M1 stage IV. The histological grade of this 4 cm tumor was grade 2.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("ner_oncology_tnm_pipeline", "en", "clinical/models")

val text = "The final diagnosis was metastatic breast carcinoma, and it was classified as T2N1M1 stage IV. The histological grade of this 4 cm tumor was grade 2."

val result = pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | ner_chunks       |   begin |   end | ner_label         |   confidence |
|---:|:-----------------|--------:|------:|:------------------|-------------:|
|  0 | metastatic       |      24 |    33 | Metastasis        |     0.9999   |
|  1 | breast carcinoma |      35 |    50 | Cancer_Dx         |     0.9972   |
|  2 | T2N1M1 stage IV  |      78 |    92 | Staging           |     0.905267 |
|  3 | 4 cm             |     126 |   129 | Tumor_Description |     0.85105  |
|  4 | tumor            |     131 |   135 | Tumor             |     0.9926   |
|  5 | grade 2          |     141 |   147 | Tumor_Description |     0.89705  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_tnm_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel