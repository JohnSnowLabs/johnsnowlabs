---
layout: model
title: Clinical Deidentification Pipeline (English - Subentity - Name Augmented)
author: John Snow Labs
name: clinical_deidentification_subentity_nameAugmented
date: 2024-03-14
tags: [deidentification, deid, en, licensed, clinical, pipeline]
task: [De-identification, Pipeline Healthcare]
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

This pipeline can be used to deidentify PHI information from medical texts.
The PHI information will be masked and obfuscated in the resulting text.
The pipeline can mask and obfuscate `AGE`, `DATE`, `PROFESSION`, `CITY`, `COUNTRY`, `DOCTOR`, `HOSPITAL`, `IDNUM`, `MEDICALRECORD`, `ORGANIZATION`, `PATIENT`,
`PHONE`, `STREET`, `USERNAME`, `EMAIL`, `ZIP`, `ACCOUNT`, `LICENSE`, `VIN`, `SSN`, `DLN`, `PLATE`, `IPADDR` entities.
This pipeline is built using the `ner_deid_subentity_augmented` model as well as ContextualParser, RegexMatcher, and TextMatcher.
It is augmented with `ner_deid_name_multilingual_clinical` model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_subentity_nameAugmented_en_5.3.0_3.4_1710413718741.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_subentity_nameAugmented_en_5.3.0_3.4_1710413718741.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_nameAugmented", "en", "clinical/models")

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR #719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

result = deid_pipeline.annotate(text)


```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_nameAugmented", "en", "clinical/models")

val text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR #719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

val result = deid_pipeline.annotate(text)

```
</div>

## Results

```bash

print("
Masked with entity labels")
print("-"*30)
print("
".join(result['masked']))
print("
Masked with chars")
print("-"*30)
print("
".join(result['masked_with_chars']))
print("
Masked with fixed length chars")
print("-"*30)
print("
".join(result['masked_fixed_length_chars']))
print("
Obfuscated")
print("-"*30)
print("
".join(result['obfuscated']))

Masked with entity labels
------------------------------
Name : <PATIENT>, Record date: <DATE>, MR <MEDICALRECORD>.
Dr. <DOCTOR>, ID: <DEVICE>, IP <IPADDR>.
He is a <AGE>-year-old male was admitted to the <HOSPITAL> for cystectomy on <DATE>.
Patient's VIN : <VIN>, SSN <SSN>, Driver's license no: <DLN>.
Phone <PHONE>, <STREET>, <CITY>, E-MAIL: <EMAIL>.

Masked with chars
------------------------------
Name : [**************], Record date: [********], MR [****].
Dr. [********], ID: [********], IP [************].
He is a **-year-old male was admitted to the [**********] for cystectomy on [******].
Patient's VIN : [***************], SSN [**********], Driver's license no: [******].
Phone [************], [***************], [***********], E-MAIL: [*************].

Masked with fixed length chars
------------------------------
Name : ****, Record date: ****, MR ****.
Dr. ****, ID: ****, IP ****.
He is a ****-year-old male was admitted to the **** for cystectomy on ****.
Patient's VIN : ****, SSN ****, Driver's license no: ****.
Phone ****, ****, ****, E-MAIL: ****.

Obfuscated
------------------------------
Name : Campbell Lerner, Record date: 2093-01-22, MR 301601.
Dr. Ivar Drape, ID: O1478969, IP 004.004.004.004.
He is a 74-year-old male was admitted to the DELAWARE COUNTY MEMORIAL HOSPITAL for cystectomy on 01/22/93.
Patient's VIN : 0XNAT55DDUK025427, SSN #062-37-6283, Driver's license no: T517616W.
Phone (737) 106-2694, 1120 Pine St, Durham, E-MAIL: Joseline@hotmail.com.

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_subentity_nameAugmented|
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