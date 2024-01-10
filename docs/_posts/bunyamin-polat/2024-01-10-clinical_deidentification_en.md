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

val deid_pipeline = PretrainedPipeline("clinical_deidentification", "en", "clinical/models")

val result = deid_pipeline.annotate("""Record date : 2093-01-13, Name : Hendrickson, ORA, 25 years-old, #719435. IP: 203.120.223.13, the driver's license no:A334455B. The SSN:324598674 and e-mail: hale@gmail.com. Patient's VIN : 1HGBH41JXMN109286. Date : 01/13/93, PCP : David Hale.""")

```
</div>

## Results

```bash


sample = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR #719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

result4 = deid_pipeline3.annotate(sample)

print("\nMasked with entity labels")
print("-"*30)

output

Masked with entity labels
------------------------------
Name : <PATIENT>, Record date: <DATE>, MR <MEDICALRECORD>.
Dr. <DOCTOR>, ID<IDNUM>, IP <IPADDR>.
He is a <AGE>-year-old male was admitted to the <LOCATION> for cystectomy on <DATE>.
Patient's VIN : <VIN>, SSN <SSN>, Driver's license no: <DLN>.
Phone <PHONE>, <STREET>, <CITY>, E-MAIL: <EMAIL>.

Masked with chars
------------------------------
Name : [**************], Record date: [********], MR [*****].
Dr. [********], ID[**********], IP [************].
He is a **-year-old male was admitted to the [**********] for cystectomy on [******].
Patient's VIN : [***************], SSN [**********], Driver's license no: [******].
Phone [************], [***************], [***********], E-MAIL: [*************].

Masked with fixed length chars
------------------------------
Name : ****, Record date: ****, MR ****.
Dr. ****, ID****, IP ****.
He is a ****-year-old male was admitted to the **** for cystectomy on ****.
Patient's VIN : ****, SSN ****, Driver's license no: ****.
Phone ****, ****, ****, E-MAIL: ****.

Obfuscated
------------------------------
Name : Beatrice Lecher, Record date: 2093-01-24, MR #194174.
Dr. Margarette Canada, ID: 0814481856, IP 001.001.001.001.
He is a 77-year-old male was admitted to the South Megan for cystectomy on 01/24/93.
Patient's VIN : 3JSHF02OVZC588502, SSN #774-12-8786, Driver's license no: V672094B.
Phone (096) 283-6629, Timothyborough, Ocala, E-MAIL: Lemuel@yahoo.com.

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
