---
layout: model
title: Clinical Deidentification Pipeline - Multi Mode Output (English)
author: John Snow Labs
name: clinical_deidentification_multi_mode_output
date: 2025-01-03
tags: [deidentification, deid, en, licensed, clinical, pipeline]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.5.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to de-identify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. The pipeline can mask and obfuscate `ACCOUNT`, `AGE`, `CITY`, `CONTACT`, `COUNTRY`, `DATE`, `DEVICE`, `DLN`, `DOCTOR`, `EMAIL`, `FAX`, `HEALTHPLAN`, `HOSPITAL`, `ID`, `IPADDR`, `LICENSE`, `LOCATION`, `MEDICALRECORD`, `NAME`, `ORGANIZATION`, `PATIENT`, `PHONE`, `PLATE`, `PROFESSION`, `SREET`, `SSN`, `STATE`, `STREET`, `URL`, `USERNAME`, `VIN`, `ZIP`, `CITY` entities.

This pipeline simultaneously produces masked with entity labels, fixed-length char, same-length char and obfuscated version of the text.

## Predicted Entities

`ACCOUNT`, `AGE`, `CITY`, `CONTACT`, `COUNTRY`, `DATE`, `DEVICE`, `DLN`, `DOCTOR`, `EMAIL`, `FAX`, `HEALTHPLAN`, `HOSPITAL`, `ID`, `IPADDR`, `LICENSE`, `LOCATION`, `MEDICALRECORD`, `NAME`, `ORGANIZATION`, `PATIENT`, `PHONE`, `PLATE`, `PROFESSION`, `SREET`, `SSN`, `STATE`, `STREET`, `URL`, `USERNAME`, `VIN`, `ZIP`, `CITY`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_multi_mode_output_en_5.5.1_3.0_1735932330478.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_multi_mode_output_en_5.5.1_3.0_1735932330478.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_multi_mode_output", "en", "clinical/models")

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR # 719435.
Dr. John Green, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, CA 94131, E-MAIL: smith@gmail.com."""

result = deid_pipeline.annotate(text)


```

{:.jsl-block}
```python

deid_pipeline = nlp.PretrainedPipeline("clinical_deidentification_multi_mode_output", "en", "clinical/models")

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR # 719435.
Dr. John Green, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, CA 94131, E-MAIL: smith@gmail.com."""

result = deid_pipeline.annotate(text)


```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_multi_mode_output", "en", "clinical/models")

val text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR # 719435.
Dr. John Green, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, CA 94131, E-MAIL: smith@gmail.com."""

val result = deid_pipeline.annotate(text)

```
</div>

## Results

```bash

print("\nMasked with entity labels")
print("-"*30)
print("\n".join(result['masked']))
print("\nMasked with chars")
print("-"*30)
print("\n".join(result['masked_with_chars']))
print("\nMasked with fixed length chars")
print("-"*30)
print("\n".join(result['masked_fixed_length_chars']))
print("\nObfuscated")
print("-"*30)
print("\n".join(result['obfuscated']))

Masked with entity labels
------------------------------
Name : <PATIENT>, Record date: <DATE>, MR # <MEDICALRECORD>.
Dr. <DOCTOR>, IP <IPADDR>.
He is a <AGE>-year-old male was admitted to the <HOSPITAL> for cystectomy on <DATE>.
Patient's VIN : <VIN>, SSN <SSN>, Driver's license no: <DLN>.
Phone <PHONE>, <STREET>, <CITY>, <STATE> <ZIP>, E-MAIL: <EMAIL>.

Masked with chars
------------------------------
Name : [**************], Record date: [********], MR # [****].
Dr. [********], IP [************].
He is a **-year-old male was admitted to the [**********] for cystectomy on [******].
Patient's VIN : [***************], SSN [**********], Driver's license no: [******].
Phone [************], [***************], [***********], ** [***], E-MAIL: [*************].

Masked with fixed length chars
------------------------------
Name : ****, Record date: ****, MR # ****.
Dr. ****, IP ****.
He is a ****-year-old male was admitted to the **** for cystectomy on ****.
Patient's VIN : ****, SSN ****, Driver's license no: ****.
Phone ****, ****, ****, **** ****, E-MAIL: ****.

Obfuscated
------------------------------
Name : Dallis Dues, Record date: 2093-03-10, MR # 071219.
Dr. Emilie Harden, IP 001.001.001.001.
He is a 73-year-old male was admitted to the SOMERSET HOSPITAL for cystectomy on 03/10/93.
Patient's VIN : 7JOIT25QDIY641583, SSN #094-07-6808, Driver's license no: U110315X.
Phone (458) 592-9244, 100 Hospital Drive, NUNGATTA, Louisiana 62863, E-MAIL: Adelais@google.com.

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_multi_mode_output|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.1+|
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
- ChunkMergeModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcherInternalModel
- ContextualParserModel
- ContextualParserModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- ContextualParserModel
- RegexMatcherInternalModel
- TextMatcherInternalModel
- ChunkMergeModel
- ChunkMergeModel
- DeIdentificationModel
- DeIdentificationModel
- DeIdentificationModel
- DeIdentificationModel
- Finisher
