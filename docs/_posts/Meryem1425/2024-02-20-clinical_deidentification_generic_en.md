---
layout: model
title: Clinical Deidentification Pipeline (English - Generic)
author: John Snow Labs
name: clinical_deidentification_generic
date: 2024-02-20
tags: [deidentification, deid, en, licensed, clinical, pipeline]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to de-identify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. The pipeline can mask and obfuscate `AGE`, `CONTACT`, `DATE`, `LOCATION`, `COUNTRY`, `NAME`, `PROFESSION`, `ID`, `MEDICALRECORD`, `PHONE`, `ZIP`, `ACCOUNT`, `LICENSE`, `VIN`, `SSN`, `DLN`, `PLATE` entities. This pipeline is built using the `ner_deid_generic` model as well as ContextualParser, RegexMatcher, and TextMatcher.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_generic_en_5.2.1_3.2_1708467513464.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_generic_en_5.2.1_3.2_1708467513464.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_generic", "en", "clinical/models")

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

result = deid_pipeline.annotate(text)


```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_generic", "en", "clinical/models")

val text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the hospital for cystectomy on 01/13/93.
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
Name : <NAME>, Record date: <DATE>, MR <MEDICALRECORD>.
Dr. <NAME>, ID: <ID>, IP <IPADDR>.
He is a <AGE>-year-old male was admitted to the hospital for cystectomy on <DATE>.
Patient's VIN : <VIN>, SSN <SSN>, Driver's license no: <DLN>.
Phone <PHONE>, <LOCATION>, <LOCATION>, E-MAIL: <EMAIL>.

Masked with chars
------------------------------
Name : [**************], Record date: [********], MR [****].
Dr. [********], ID: [********], IP [************].
He is a **-year-old male was admitted to the hospital for cystectomy on [******].
Patient's VIN : [***************], SSN [**********], Driver's license no: [******].
Phone [************], [***************], [***********], E-MAIL: [*************].

Masked with fixed length chars
------------------------------
Name : ****, Record date: ****, MR ****.
Dr. ****, ID: ****, IP ****.
He is a ****-year-old male was admitted to the hospital for cystectomy on ****.
Patient's VIN : ****, SSN ****, Driver's license no: ****.
Phone ****, ****, ****, E-MAIL: ****.

Obfuscated
------------------------------
Name : Vonzell Schlatter, Record date: 2093-02-07, MR 182993.
Dr. Dartha Lodge, ID: 7169678938, IP 444.444.444.444.
He is a 63-year-old male was admitted to the hospital for cystectomy on 02/07/93.
Patient's VIN : 1OFBP10CHEN277824, SSN #235-36-1443, Driver's license no: X540086P.
Phone (619) 509-3267, 31700 Temecula Pkwy, 1215 Franciscan Dr, E-MAIL: Savannah@google.com.

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_generic|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
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
