---
layout: model
title: Clinical Deidentification Pipeline - Multi Mode Output (English)
author: John Snow Labs
name: clinical_deidentification_multi_mode_output
date: 2024-03-27
tags: [deidentification, deid, clinical, pipeline, en, licensed]
task: De-identification
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"

deploy:
  sagemaker_link: https://aws.amazon.com/marketplace/pp/prodview-ept2dbql5slue
  snowflake_link: 
  databricks_link: https://marketplace.databricks.com/details/facfaf55-00f6-496c-a8db-a395631130ec/John-Snow-Labs_Clinical-Deidentification

---

## Description

This pipeline can be used to de-identify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. The pipeline can mask and obfuscate `LOCATION`, `CONTACT`, `PROFESSION`, `NAME`, `DATE`, `ID`, `AGE`, `MEDICALRECORD`, `ORGANIZATION`, `HEALTHPLAN`, `DOCTOR`, `USERNAME`, `URL`, `DEVICE`, `CITY`, `ZIP`, `STATE`, `PATIENT`, `COUNTRY`, `STREET`, `PHONE`, `HOSPITAL`, `EMAIL`, `IDNUM`, `BIOID`, `FAX`, `SSN`, `ACCOUNT`, `DLN`, `PLATE`, `VIN`, `LICENSE` entities.
 
This pipeline simultaneously produces masked with entity labels, fixed-length char, same-length char and obfuscated version of the text.

## Predicted Entities

`LOCATION`, `CONTACT`, `PROFESSION`, `NAME`, `DATE`, `ID`, `AGE`, `MEDICALRECORD`, `ORGANIZATION`, `HEALTHPLAN`, `DOCTOR`, `USERNAME`, `URL`, `DEVICE`, `CITY`, `ZIP`, `STATE`, `PATIENT`, `COUNTRY`, `STREET`, `PHONE`, `HOSPITAL`, `EMAIL`, `IDNUM`, `BIOID`, `FAX`, `SSN`, `ACCOUNT`, `DLN`, `PLATE`, `VIN`, `LICENSE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_multi_mode_output_en_5.3.1_3.4_1711532922696.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_multi_mode_output_en_5.3.1_3.4_1711532922696.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}


{% if page.deploy %}
## Available as Private API Endpoint

{:.tac}
{% include display_platform_information.html %}
{% endif %}


## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_multi_mode_output", "en", "clinical/models")

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

result = deid_pipeline.annotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_multi_mode_output", "en", "clinical/models")

val text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

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
Dr. <DOCTOR>, ID: <DEVICE>, IP <IPADDR>.
He is a <AGE>-year-old male was admitted to the <HOSPITAL> for cystectomy on <DATE>.
Patient's VIN : <VIN>, SSN <SSN>, Driver's license no: <DLN>.
Phone <PHONE>, <STREET>, <CITY>, E-MAIL: <EMAIL>.

Masked with chars
------------------------------
Name : [**************], Record date: [********], MR # [****].
Dr. [********], ID: [********], IP [************].
He is a **-year-old male was admitted to the [**********] for cystectomy on [******].
Patient's VIN : [***************], SSN [**********], Driver's license no: [******].
Phone [************], [***************], [***********], E-MAIL: [*************].

Masked with fixed length chars
------------------------------
Name : ****, Record date: ****, MR # ****.
Dr. ****, ID: ****, IP ****.
He is a ****-year-old male was admitted to the **** for cystectomy on ****.
Patient's VIN : ****, SSN ****, Driver's license no: ****.
Phone ****, ****, ****, E-MAIL: ****.

Obfuscated
------------------------------
Name : Marlana Salvage, Record date: 2093-02-23, MR # 824235.
Dr. Vic Blackbird, ID: X2814358, IP 001.001.001.001.
He is a 68-year-old male was admitted to the PRAIRIE SAINT JOHN'S for cystectomy on 02/23/93.
Patient's VIN : 3IRWE31VQMG867619, SSN #509-32-6712, Driver's license no: W580998P.
Phone (382) 505-3976, 521 Adams St, Port Shannon, E-MAIL: Dasha@yahoo.com.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_multi_mode_output|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.1+|
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
