---
layout: model
title: Pipeline to Detect Medication Entities, Assign Assertion Status and Find Relations
author: John Snow Labs
name: explain_clinical_doc_medication
date: 2024-06-19
tags: [licensed, en, clinical, ner, medication, posology, assertion, relation_extraction, pipeline]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

A pipeline for detecting posology entities with the `ner_posology_large` NER model, assigning their assertion status with `assertion_jsl` model, and extracting relations between posology-related terminology with `posology_re` relation extraction model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_medication_en_5.3.0_3.4_1718782308964.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_medication_en_5.3.0_3.4_1718782308964.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_medication", "en", "clinical/models")

result = ner_pipeline.annotate("""The patient is a 30-year-old female with an insulin dependent diabetes, type 2. She received a course of Bactrim for 14 days for UTI. She was prescribed 5000 units of Fragmin  subcutaneously daily, and along with Lantus 40 units subcutaneously at bedtime.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_medication", "en", "clinical/models")

val result = ner_pipeline.annotate("""The patient is a 30-year-old female with an insulin dependent diabetes, type 2. She received a course of Bactrim for 14 days for UTI. She was prescribed 5000 units of Fragmin  subcutaneously daily, and along with Lantus 40 units subcutaneously at bedtime.""")

```
</div>

## Results

```bash

# ner_chunk

+--------------+-----+---+---------+
|     ner_chunk|begin|end|ner_label|
+--------------+-----+---+---------+
|       insulin|   44| 50|     DRUG|
|       Bactrim|  105|111|     DRUG|
|   for 14 days|  113|123| DURATION|
|    5000 units|  153|162|   DOSAGE|
|       Fragmin|  167|173|     DRUG|
|subcutaneously|  176|189|    ROUTE|
|         daily|  191|195|FREQUENCY|
|        Lantus|  213|218|     DRUG|
|      40 units|  220|227|   DOSAGE|
|subcutaneously|  229|242|    ROUTE|
|    at bedtime|  244|253|FREQUENCY|
+--------------+-----+---+---------+

# assertion

+-------+-----+---+--------+---------+-----------+
| chunks|begin|end|entities|assertion|confidence)|
+-------+-----+---+--------+---------+-----------+
|insulin|   44| 50|    DRUG|  Present|      0.999|
|Bactrim|  105|111|    DRUG|     Past|     0.9324|
|Fragmin|  167|173|    DRUG|  Present|       0.74|
| Lantus|  213|218|    DRUG|     Past|     0.5094|
+-------+-----+---+--------+---------+-----------+

# relation

+--------+--------------+----------+-------+--------------+---------+----------+
|sentence|      relation|    chunk1|entity1|        chunk2|  entity2|confidence|
+--------+--------------+----------+-------+--------------+---------+----------+
|       1| DRUG-DURATION|   Bactrim|   DRUG|   for 14 days| DURATION|       1.0|
|       2|   DOSAGE-DRUG|5000 units| DOSAGE|       Fragmin|     DRUG|       1.0|
|       2|    DRUG-ROUTE|   Fragmin|   DRUG|subcutaneously|    ROUTE|       1.0|
|       2|DRUG-FREQUENCY|   Fragmin|   DRUG|         daily|FREQUENCY|       1.0|
|       2|   DRUG-DOSAGE|    Lantus|   DRUG|      40 units|   DOSAGE|       1.0|
|       2|    DRUG-ROUTE|    Lantus|   DRUG|subcutaneously|    ROUTE|       1.0|
|       2|DRUG-FREQUENCY|    Lantus|   DRUG|    at bedtime|FREQUENCY|       1.0|
+--------+--------------+----------+-------+--------------+---------+----------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_medication|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.0+|
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
- NerConverter
- NerConverterInternalModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- PosologyREModel