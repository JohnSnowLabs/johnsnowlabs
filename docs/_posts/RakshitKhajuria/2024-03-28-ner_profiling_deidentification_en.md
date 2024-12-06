---
layout: model
title: Named Entity Recognition Profiling (De-Identification)
author: John Snow Labs
name: ner_profiling_deidentification
date: 2024-03-28
tags: [licensed, en, clinical, profiling, ner_profiling, ner, deid, de_identification]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed for deidentification in clinical texts, leveraging a range of pretrained NER models tailored for extracting and anonymizing sensitive information. By integrating these models, the pipeline provides a comprehensive solution for protecting patient privacy and complying with data protection regulations.

The pipeline employs `embeddings_clinical` for contextual understanding and includes the following specialized NER models for deidentification:

`ner_deid_augmented`, `ner_deid_enriched`, `ner_deid_generic_augmented`, `ner_deid_name_multilingual_clinical`, `ner_deid_sd`, `ner_deid_subentity_augmented`, `ner_deid_subentity_augmented_i2b2`, `ner_deid_synthetic`, `ner_jsl`, `ner_jsl_enriched`

Each model addresses a unique aspect of deidentification, making this pipeline an all-encompassing tool for securing clinical narratives.

## Predicted Entities

`AGE`, `Age`, `BIOID`, `CITY`, `CONTACT`, `COUNTRY`, `DATE`, `DEVICE`, `DOCTOR`, `Date`, `Dosage`, `EMAIL`, `FAX`, `HEALTHPLAN`, `HOSPITAL`, `ID`, `IDNUM`, `LOCATION`, `LOCATION-OTHER`, `MEDICALRECORD`, `NAME`, `NN`, `ORGANIZATION`, `PATIENT`, `PHONE`, `PROFESSION`, `RelativeDate`, `STATE`, `STREET`, `URL`, `USERNAME`, `ZIP`


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_profiling_deidentification_en_5.3.1_3.0_1711633188135.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_profiling_deidentification_en_5.3.1_3.0_1711633188135.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_profiling_pipeline = PretrainedPipeline("ner_profiling_deidentification", 'en', 'clinical/models')

result = ner_profiling_pipeline.annotate("""Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_profiling_pipeline = PretrainedPipeline("ner_profiling_deidentification", "en", "clinical/models")

val result = ner_profiling_pipeline.annotate("""Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .""")

```
</div>

## Results

```bash
 
******************** ner_deid_name_multilingual_clinical Model Results ******************** 

('David Hale', 'NAME') ('Hendrickson Ora', 'NAME') ('Oliveira', 'NAME')

******************** ner_deid_subentity_augmented_i2b2 Model Results ******************** 

('2093-01-13', 'DATE') ('David Hale', 'DOCTOR') ('Hendrickson Ora', 'PATIENT') ('7194334', 'MEDICALRECORD') ('01/13/93', 'DATE') ('Oliveira', 'PATIENT') ('25', 'AGE') ('2079-11-09', 'DATE') ('Cocke County Baptist Hospital', 'HOSPITAL') ('0295 Keats Street', 'STREET') ('55-555-5555', 'PHONE')

******************** ner_deid_large Model Results ******************** 

('2093-01-13', 'DATE') ('David Hale', 'NAME') ('Hendrickson Ora', 'NAME') ('7194334', 'ID') ('01/13/93', 'DATE') ('Oliveira', 'NAME') ('25', 'AGE') ('2079-11-09', 'DATE') ('Cocke County Baptist Hospital', 'LOCATION') ('0295 Keats Street', 'LOCATION') ('55-555-5555', 'CONTACT')

******************** ner_jsl_enriched Model Results ******************** 

('01/13/93', 'Date') ('25 years-old', 'Age') ('2079-11-09', 'Date')

******************** ner_deid_sd_large Model Results ******************** 

('2093-01-13', 'DATE') ('David Hale', 'NAME') ('Hendrickson Ora', 'NAME') ('7194334', 'ID') ('01/13/93', 'DATE') ('Oliveira', 'NAME') ('2079-11-09', 'DATE') ('Cocke County Baptist Hospital', 'LOCATION') ('0295 Keats Street', 'LOCATION') ('55-555-5555', 'CONTACT')

******************** ner_deid_generic_augmented Model Results ******************** 

('2093-01-13', 'DATE') ('David Hale', 'NAME') ('Hendrickson Ora', 'NAME') ('7194334', 'ID') ('01/13/93', 'DATE') ('Oliveira', 'NAME') ('25', 'AGE') ('2079-11-09', 'DATE') ('Cocke County Baptist Hospital', 'LOCATION') ('0295 Keats Street', 'LOCATION') ('55-555-5555', 'CONTACT')

******************** ner_deid_name_multilingual_clinical_langtest Model Results ******************** 

('David Hale', 'NAME') ('Hendrickson Ora', 'NAME') ('Oliveira', 'NAME')

******************** ner_deid_generic_augmented_langtest Model Results ******************** 

('2093-01-13', 'DATE') ('David Hale', 'NAME') ('Hendrickson Ora', 'NAME') ('7194334', 'ID') ('01/13/93', 'DATE') ('Oliveira', 'NAME') ('25', 'AGE') ('2079-11-09', 'DATE') ('Cocke County Baptist Hospital', 'LOCATION') ('0295 Keats Street', 'LOCATION') ('55-555-5555', 'CONTACT')

******************** ner_deid_sd Model Results ******************** 

('2093-01-13', 'DATE') ('David Hale', 'NAME') ('Hendrickson Ora', 'NAME') ('7194334', 'ID') ('01/13/93', 'DATE') ('Oliveira', 'NAME') ('25', 'AGE') ('2079-11-09', 'DATE') ('Cocke County Baptist Hospital', 'LOCATION') ('0295 Keats Street', 'LOCATION')

******************** ner_deid_subentity_augmented  Model Results ******************** 

('2093-01-13', 'DATE') ('David Hale', 'DOCTOR') ('Hendrickson Ora', 'PATIENT') ('7194334', 'MEDICALRECORD') ('01/13/93', 'DATE') ('Oliveira', 'DOCTOR') ('25', 'AGE') ('2079-11-09', 'DATE') ('Cocke County Baptist Hospital', 'HOSPITAL') ('0295 Keats Street', 'STREET') ('55-555-5555', 'PHONE')

******************** ner_deid_large_langtest Model Results ******************** 

('2093-01-13', 'DATE') ('David Hale', 'NAME') ('Hendrickson Ora', 'NAME') ('7194334', 'ID') ('01/13/93', 'DATE') ('Oliveira', 'NAME') ('25', 'AGE') ('2079-11-09', 'DATE') ('Cocke County Baptist Hospital', 'LOCATION') ('0295 Keats Street', 'LOCATION') ('55-555-5555', 'CONTACT')

******************** ner_jsl Model Results ******************** 

('01/13/93', 'DATE') ('25 years-old', 'AGE')

******************** ner_deid_synthetic Model Results ******************** 

('2093-01-13', 'DATE') ('David Hale', 'NAME') ('Hendrickson Ora', 'NAME') ('7194334', 'ID') ('01/13/93', 'DATE') ('Oliveira', 'NAME') ('25', 'AGE') ('2079-11-09', 'DATE') ('Cocke County Baptist Hospital', 'LOCATION') ('0295 Keats Street', 'LOCATION') ('55-555-5555', 'CONTACT')

******************** ner_deid_augmented Model Results ******************** 

('2093-01-13', 'DATE') ('David Hale', 'NAME') ('Hendrickson Ora', 'NAME') ('7194334', 'ID') ('01/13/93', 'DATE') ('Oliveira', 'NAME') ('25', 'AGE') ('2079-11-09', 'DATE') ('Cocke County Baptist Hospital', 'LOCATION') ('Keats Street', 'LOCATION')

******************** ner_deid_generic_augmented_allUpperCased_langtest Model Results ******************** 

('2093-01-13', 'DATE') ('David Hale', 'NAME') ('Hendrickson Ora', 'NAME') ('7194334', 'ID') ('01/13/93', 'DATE') ('Oliveira', 'NAME') ('25', 'AGE') ('2079-11-09', 'DATE') ('Cocke County Baptist Hospital', 'LOCATION') ('0295 Keats Street', 'LOCATION') ('55-555-5555', 'CONTACT')

******************** ner_deid_enriched_langtest Model Results ******************** 

('2093-01-13', 'DATE') ('David Hale', 'DOCTOR') ('Hendrickson Ora', 'DOCTOR') ('7194334', 'MEDICALRECORD') ('01/13/93', 'DATE') ('Oliveira', 'DOCTOR') ('25', 'AGE') ('2079-11-09', 'DATE') ('Cocke County Baptist Hospital', 'HOSPITAL') ('0295 Keats Street', 'STREET') ('55-555-5555', 'PHONE')

******************** ner_deid_subentity_augmented_langtest Model Results ******************** 

('2093-01-13', 'DATE') ('David Hale', 'DOCTOR') ('Hendrickson Ora', 'DOCTOR') ('7194334', 'MEDICALRECORD') ('01/13/93', 'DATE') ('Oliveira', 'DOCTOR') ('25', 'AGE') ('2079-11-09', 'DATE') ('Cocke County Baptist Hospital', 'HOSPITAL') ('0295 Keats Street', 'STREET') ('55-555-5555', 'PHONE')

******************** ner_deid_enriched Model Results ******************** 

('2093-01-13', 'DATE') ('David Hale', 'DOCTOR') ('Hendrickson Ora', 'DOCTOR') ('7194334', 'MEDICALRECORD') ('01/13/93', 'DATE') ('Oliveira', 'DOCTOR') ('25', 'AGE') ('2079-11-09', 'DATE') ('Cocke County Baptist Hospital', 'HOSPITAL') ('0295 Keats Street', 'STREET') ('55-555-5555', 'PHONE')


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_profiling_deidentification|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.0 GB|


## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel x 14
- NerConverterInternalModel x 14

