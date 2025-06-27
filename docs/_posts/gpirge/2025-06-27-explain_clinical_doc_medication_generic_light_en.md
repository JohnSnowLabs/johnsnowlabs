---
layout: model
title: Explain Clinical Document Generic Medications - Light
author: John Snow Labs
name: explain_clinical_doc_medication_generic_light
date: 2025-06-27
tags: [licensed, en, clinical, pipeline, ner, medication]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to extract medication entities in generic form from texts.

2 NER models and a text matcher are used to extract the medication entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_medication_generic_light_en_6.0.2_3.4_1751048341279.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_medication_generic_light_en_6.0.2_3.4_1751048341279.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_medication_generic_light", "en", "clinical/models")

result = ner_pipeline.annotate("""In response, his doctor prescribed a regimen tailored to his conditions:
Thiamine 100 mg q.day , Folic acid 1 mg q.day , multivitamins q.day , Calcium carbonate plus Vitamin D 250 mg t.i.d. , Heparin 5000 units subcutaneously b.i.d. , Prilosec 20 mg q.day , Senna two tabs qhs.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_medication_generic_light", "en", "clinical/models")

val result = ner_pipeline.annotate("""In response, his doctor prescribed a regimen tailored to his conditions:
Thiamine 100 mg q.day , Folic acid 1 mg q.day , multivitamins q.day , Calcium carbonate plus Vitamin D 250 mg t.i.d. , Heparin 5000 units subcutaneously b.i.d. , Prilosec 20 mg q.day , Senna two tabs qhs.""")

```
</div>

## Results

```bash
|    | chunks                            |   begin |   end | entities   |
|---:|:----------------------------------|--------:|------:|:-----------|
|  0 | Thiamine 100 mg                   |      73 |    87 | DRUG       |
|  1 | q.day                             |      89 |    93 | FREQUENCY  |
|  2 | Folic acid 1 mg                   |      97 |   111 | DRUG       |
|  3 | q.day                             |     113 |   117 | FREQUENCY  |
|  4 | multivitamins                     |     121 |   133 | DRUG       |
|  5 | q.day                             |     135 |   139 | FREQUENCY  |
|  6 | Calcium carbonate                 |     143 |   159 | DRUG       |
|  7 | Vitamin D 250 mg                  |     166 |   181 | DRUG       |
|  8 | t.i.d                             |     183 |   187 | FREQUENCY  |
|  9 | Heparin 5000 units subcutaneously |     192 |   224 | DRUG       |
| 10 | b.i.d                             |     226 |   230 | FREQUENCY  |
| 11 | Prilosec 20 mg                    |     235 |   248 | DRUG       |
| 12 | q.day                             |     250 |   254 | FREQUENCY  |
| 13 | Senna two tabs                    |     258 |   271 | DRUG       |
| 14 | qhs                               |     273 |   275 | FREQUENCY  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_medication_generic_light|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
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
- MedicalNerModel
- NerConverterInternalModel
- TextMatcherInternalModel
- ChunkMergeModel