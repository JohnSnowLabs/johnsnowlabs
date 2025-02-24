---
layout: model
title: Pipeline to Detect Medication Entities, Assign Assertion Status and Find Relations
author: John Snow Labs
name: explain_clinical_doc_medication
date: 2023-06-17
tags: [licensed, clinical, ner, en, assertion, relation_extraction, posology, medication]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

A pipeline for detecting posology entities with the `ner_posology_large` NER model, assigning their assertion status with `assertion_jsl` model, and extracting relations between posology-related terminology with `posology_re` relation extraction model.

## Predicted Entities

`DRUG`, `DOSAGE`, `DURATION`, `FORM`, `FREQUENCY`, `ROUTE`, `STRENGTH`



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_medication_en_4.4.4_3.0_1686989820905.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_medication_en_4.4.4_3.0_1686989820905.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("explain_clinical_doc_medication", "en", "clinical/models")

text = '''The patient is a 30-year-old female with an insulin dependent diabetes, type 2. She received a course of Bactrim for 14 days for UTI. She was prescribed 5000 units of Fragmin  subcutaneously daily, and along with Lantus 40 units subcutaneously at bedtime.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("explain_clinical_doc_medication", "en", "clinical/models")

val text = "The patient is a 30-year-old female with an insulin dependent diabetes, type 2. She received a course of Bactrim for 14 days for UTI. She was prescribed 5000 units of Fragmin  subcutaneously daily, and along with Lantus 40 units subcutaneously at bedtime."

val result = pipeline.fullAnnotate(text)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.explain_dco.clinical_medication.pipeline").predict("""The patient is a 30-year-old female with an insulin dependent diabetes, type 2. She received a course of Bactrim for 14 days for UTI. She was prescribed 5000 units of Fragmin  subcutaneously daily, and along with Lantus 40 units subcutaneously at bedtime.""")
```

</div>



## Results

```bash
# ner_chunk

|    |      ner_chunk | begin | end | ner_label |
|---:|---------------:|------:|----:|----------:|
|  0 |        insulin |    44 |  50 |      DRUG |
|  1 |        Bactrim |   105 | 111 |      DRUG |
|  2 |    for 14 days |   113 | 123 |  DURATION |
|  3 |     5000 units |   153 | 162 |    DOSAGE |
|  4 |        Fragmin |   167 | 173 |      DRUG |
|  5 | subcutaneously |   176 | 189 |     ROUTE |
|  6 |          daily |   191 | 195 | FREQUENCY |
|  7 |         Lantus |   213 | 218 |      DRUG |
|  8 |       40 units |   220 | 227 |    DOSAGE |
|  9 | subcutaneously |   229 | 242 |     ROUTE |
| 10 |     at bedtime |   244 | 253 | FREQUENCY |

# assertion

|   |  chunks | entities | assertion |
|--:|--------:|---------:|----------:|
| 0 | insulin |     DRUG |   Present |
| 1 | Bactrim |     DRUG |      Past |
| 2 | Fragmin |     DRUG |   Planned |
| 3 |  Lantus |     DRUG |      Past |

# relation

|   |       relation | entity1 |     chunk1 |   entity2 |         chunk2 |
|--:|---------------:|--------:|-----------:|----------:|---------------:|
| 0 |  DRUG-DURATION |    DRUG |    Bactrim |  DURATION |    for 14 days |
| 1 |    DOSAGE-DRUG |  DOSAGE | 5000 units |      DRUG |        Fragmin |
| 2 |     DRUG-ROUTE |    DRUG |    Fragmin |     ROUTE | subcutaneously |
| 3 | DRUG-FREQUENCY |    DRUG |    Fragmin | FREQUENCY |          daily |
| 4 |    DRUG-DOSAGE |    DRUG |     Lantus |    DOSAGE |       40 units |
| 5 |     DRUG-ROUTE |    DRUG |     Lantus |     ROUTE | subcutaneously |
| 6 | DRUG-FREQUENCY |    DRUG |     Lantus | FREQUENCY |     at bedtime |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_medication|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
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
- NerConverterInternalModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- PosologyREModel