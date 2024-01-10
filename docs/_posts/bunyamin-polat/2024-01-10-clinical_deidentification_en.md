---
layout: model
title: Clinical Deidentification Pipeline (English)
author: John Snow Labs
name: clinical_deidentification
date: 2024-01-10
tags: [deidentification, deid, en, licensed, clinical, pipeline]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. The pipeline can mask and obfuscate `AGE`, `CONTACT`, `DATE`, `LOCATION`, `NAME`, `PROFESSION`, `CITY`, `COUNTRY`, `DOCTOR`, `HOSPITAL`, `IDNUM`, `MEDICALRECORD`, `ORGANIZATION`, `PATIENT`, `PHONE`, `STREET`, `USERNAME`, `ZIP`, `ACCOUNT`, `LICENSE`, `VIN`, `SSN`, `DLN`, `PLATE`, `IPADDR` entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_en_5.2.0_3.0_1704910057316.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_en_5.2.0_3.0_1704910057316.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification", "en", "clinical/models")

deid_pipeline.fullAnnotate("""Record date : 2093-01-13, Name : Hendrickson, ORA, 25 years-old, #719435. IP: 203.120.223.13, the driver's license no:A334455B. The SSN:324598674 and e-mail: hale@gmail.com. Patient's VIN : 1HGBH41JXMN109286. Date : 01/13/93, PCP : David Hale.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_profiling_pipeline = PretrainedPipeline("clinical_deidentification", "en", "clinical/models")

val result = deid_pipeline.annotate("""Record date : 2093-01-13, Name : Hendrickson, ORA, 25 years-old, #719435. IP: 203.120.223.13, the driver's license no:A334455B. The SSN:324598674 and e-mail: hale@gmail.com. Patient's VIN : 1HGBH41JXMN109286. Date : 01/13/93, PCP : David Hale.""")

```
</div>

## Results

```bash

Masked with entity labels
------------------------------
Record date : <DATE>, <DOCTOR>, M.D. <NAME> <IPADDR>, the driver's license no: <DLN>.
the SSN: <SSN> and e-mail: <EMAIL>.
Name : <PATIENT> MR. <AGE> years-old # <MEDICALRECORD> Date : <DATE>.
Signed by <DOCTOR>, .
Patient's VIN : <VIN>.

Masked with chars
------------------------------
Record date : [********], [********], M.D. ** [************], the driver's license no: [******].
the SSN: [*******] and e-mail: [************].
Name : [**************] MR. ** years-old # [****] Date : [******].
Signed by [*************], .
Patient's VIN : [***************].

Masked with fixed length chars
------------------------------
Record date : ****, ****, M.D. **** ****, the driver's license no: ****.
the SSN: **** and e-mail: ****.
Name : **** MR. **** years-old # **** Date : ****.
Signed by ****, .
Patient's VIN : ****.

Obfuscated
------------------------------
Record date : 2093-01-24, Bethel Born, M.D. Amie Critchley 001.001.001.001, the driver's license no: I347425Z.
the SSN: 563875643 and e-mail: Damocles@yahoo.com.
Name : Beatrice Lecher MR. 32 years-old # 329518 Date : 01/24/93.
Signed by Barbara Cower, .
Patient's VIN : 8CZYS06TKZS010932.

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.0+|
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
- MedicalNerModel
- NerConverter
- ChunkMergeModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- TextMatcherModel
- ContextualParserModel
- RegexMatcherModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ChunkMergeModel
- ChunkMergeModel
- DeIdentificationModel
- DeIdentificationModel
- DeIdentificationModel
- DeIdentificationModel
- Finisher