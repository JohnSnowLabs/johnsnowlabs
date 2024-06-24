---
layout: model
title: Pipeline to Detect Medication Entities, Assign Assertion Status and Find Relations
author: John Snow Labs
name: explain_clinical_doc_medication
date: 2024-06-19
tags: [licensed, en, clinical, ner, medication, posology, assertion, relation_extraction, pipeline]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

A pipeline for detecting posology entities with the `ner_posology_large` NER model, assigning their assertion status with `assertion_oncology_wip` model, and extracting relations between posology-related terminology with `posology_re` relation extraction model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_medication_en_5.3.3_3.0_1718825386195.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_medication_en_5.3.3_3.0_1718825386195.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_medication", "en", "clinical/models")

result = ner_pipeline.annotate("""The patient is a 30-year-old female with diabetes mellitus type 2. She received a course of Bactrim for 14 days for UTI. 
She was prescribed 5000 units of Fragmin subcutaneously daily. She was also prescribed 40 units of Lantus subcutaneously at night.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_medication", "en", "clinical/models")

val result = ner_pipeline.annotate("""The patient is a 30-year-old female with diabetes mellitus type 2. She received a course of Bactrim for 14 days for UTI. 
She was prescribed 5000 units of Fragmin subcutaneously daily. She was also prescribed 40 units of Lantus subcutaneously at night.""")

```
</div>

## Results

```bash

# ner_chunk

+--------------+-----+---+---------+
|     ner_chunk|begin|end|ner_label|
+--------------+-----+---+---------+
|       Bactrim|   92| 98|     DRUG|
|   for 14 days|  100|110| DURATION|
|    5000 units|  141|150|   DOSAGE|
|       Fragmin|  155|161|     DRUG|
|subcutaneously|  163|176|    ROUTE|
|         daily|  178|182|FREQUENCY|
|      40 units|  209|216|   DOSAGE|
|        Lantus|  221|226|     DRUG|
|subcutaneously|  228|241|    ROUTE|
|      at night|  243|250|FREQUENCY|
+--------------+-----+---+---------+

# assertion

+-------+-----+---+--------+---------+-----------+
| chunks|begin|end|entities|assertion|confidence)|
+-------+-----+---+--------+---------+-----------+
|Bactrim|   92| 98|    DRUG|     Past|     0.9324|
|Fragmin|  155|161|    DRUG|  Present|     0.7456|
| Lantus|  190|195|    DRUG|  Present|     0.4984|
+-------+-----+---+--------+---------+-----------+

# relation

+--------+--------------+---------+----------+-------+--------------+---------+----------+
|sentence|      relation|direction|    chunk1|entity1|        chunk2|  entity2|confidence|
+--------+--------------+---------+----------+-------+--------------+---------+----------+
|       1| DRUG-DURATION|     both|   Bactrim|   DRUG|   for 14 days| DURATION|       1.0|
|       2|   DOSAGE-DRUG|     both|5000 units| DOSAGE|       Fragmin|     DRUG|       1.0|
|       2|    DRUG-ROUTE|     both|   Fragmin|   DRUG|subcutaneously|    ROUTE|       1.0|
|       2|DRUG-FREQUENCY|     both|   Fragmin|   DRUG|         daily|FREQUENCY|       1.0|
|       3|   DOSAGE-DRUG|     both|  40 units| DOSAGE|        Lantus|     DRUG|       1.0|
|       3|    DRUG-ROUTE|     both|    Lantus|   DRUG|subcutaneously|    ROUTE|       1.0|
|       3|DRUG-FREQUENCY|     both|    Lantus|   DRUG|      at night|FREQUENCY|       1.0|
+--------+--------------+---------+----------+-------+--------------+---------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_medication|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.3+|
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
