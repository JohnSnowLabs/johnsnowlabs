---
layout: model
title: Named Entity Recognition Profiling (De-Identification)
author: John Snow Labs
name: ner_profiling_deidentification
date: 2025-06-16
tags: [licensed, en, clinical, profiling, ner_profiling, ner, deid, de_identification]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.0.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed for profiling and benchmarking various de-identification models applied to clinical texts. It integrates multiple NER models and rule-based components that are commonly used for detecting and anonymizing protected health information (PHI). The pipeline includes models trained with embeddings_clinical, zero-shot NER models, regex matchers, text matchers, and contextual parsers. By consolidating these diverse approaches, it allows comprehensive evaluation and comparison of different de-identification strategies across clinical datasets.

The following models are included in this pipeline:
`ner_deid_aipii`, `ner_deid_augmented`, `ner_deid_enriched`, `ner_deid_enriched_langtest`, `ner_deid_generic_augmented`, `ner_deid_generic_augmented_allUpperCased_langtest`, `ner_deid_generic_augmented_langtest`, `ner_deid_generic_docwise`, `ner_deid_large`, `ner_deid_large_langtest`, `ner_deid_sd`, `ner_deid_sd_large`, `ner_deid_subentity_augmented`, `ner_deid_subentity_augmented_docwise`, `ner_deid_subentity_augmented_i2b2`, `ner_deid_subentity_augmented_langtest`, `ner_deid_subentity_augmented_v2`, `ner_deid_subentity_docwise`, `ner_deid_synthetic`, `ner_deidentify_dl`, `zeroshot_ner_deid_subentity_merged_medium`

## Predicted Entities

`ACCOUNT`, `AGE`, `BIOID`, `CITY`, `CONTACT`, `COUNTRY`, `DATE`, `DEVICE`, `DLN`, `DOCTOR`, `EMAIL`, `FAX`, `HEALTHPLAN`, `HOSPITAL`, `ID`, `IDNUM`, `LICENSE`, `LOCATION`, `LOCATION_OTHER`, `MEDICALRECORD`, `NAME`, `ORGANIZATION`, `PATIENT`, `PHONE`, `PROFESSION`, `SSN`, `STATE`, `STREET`, `URL`, `USERNAME`, `ZIP`.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_profiling_deidentification_en_6.0.0_3.2_1750048147795.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_profiling_deidentification_en_6.0.0_3.2_1750048147795.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_profiling_pipeline = PretrainedPipeline("ner_profiling_deidentification", "en", "clinical/models")

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, Age: 25, # 719435. Dr. John Green, ID: 1231511863, IP 203.120.223.13. He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93. Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B. Phone (302) 786-5227, 0295 Keats Street, San Francisco."""

ner_profiling_pipeline_result = ner_profiling_pipeline.fullAnnotate(text)[0]


```

{:.jsl-block}
```python

ner_profiling_pipeline = nlp.PretrainedPipeline("ner_profiling_deidentification", "en", "clinical/models")

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, Age: 25, # 719435. Dr. John Green, ID: 1231511863, IP 203.120.223.13. He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93. Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B. Phone (302) 786-5227, 0295 Keats Street, San Francisco."""

ner_profiling_pipeline_result = ner_profiling_pipeline.fullAnnotate(text)[0]



```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_profiling_pipeline = PretrainedPipeline("ner_profiling_deidentification", "en", "clinical/models")

val text = """Name : Hendrickson, Ora, Record date: 2093-01-13, Age: 25, # 719435. Dr. John Green, ID: 1231511863, IP 203.120.223.13. He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93. Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B. Phone (302) 786-5227, 0295 Keats Street, San Francisco."""

val ner_profiling_pipeline_result = ner_profiling_pipeline.fullAnnotate(text)[0]


```
</div>

## Results

```bash
******************** ner_deid_augmented Model Results ********************

[('Hendrickson , Ora', 'NAME'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'CONTACT'), ('John Green', 'NAME'), ('1231511863', 'ID'), ('IP 203.120.223.13', 'CONTACT'), ('Day Hospital', 'LOCATION'), ('01/13/93', 'DATE'), ('1HGBH41JXMN109286', 'ID'), ('( 302 ) 786-5227', 'CONTACT'), ('0295 Keats Street', 'LOCATION'), ('San Francisco', 'LOCATION')]

******************** ner_deid_subentity_augmented_i2b2 Model Results ********************

[('Hendrickson , Ora', 'PATIENT'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'ZIP'), ('John Green', 'DOCTOR'), (': 1231511863', 'IDNUM'), ('203.120.223.13', 'PHONE'), ('01/13/93', 'DATE'), ('1HGBH41JXMN109286', 'IDNUM'), ('#333-44-6666', 'PHONE'), ('no:A334455B', 'IDNUM'), ('( 302 ) 786-5227', 'PHONE'), ('0295 Keats Street', 'STREET'), ('San Francisco', 'CITY')]

******************** ner_deidentify_dl Model Results ********************

[('Hendrickson , Ora', 'PATIENT'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'PHONE'), ('John Green', 'DOCTOR'), ('1231511863', 'IDNUM'), ('Day Hospital', 'HOSPITAL'), ('01/13/93', 'DATE'), ('no:A334455B', 'IDNUM'), ('( 302 ) 786-5227', 'PHONE'), ('0295 Keats Street', 'STREET'), ('San Francisco .', 'CITY')]

******************** ner_deid_subentity_augmented_langtest Model Results ********************

[('Hendrickson , Ora', 'PATIENT'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'PHONE'), ('John Green', 'DOCTOR'), ('1231511863', 'IDNUM'), ('203.120.223.13', 'PHONE'), ('60-year-old', 'AGE'), ('Day Hospital', 'HOSPITAL'), ('01/13/93', 'DATE'), ('1HGBH41JXMN109286', 'IDNUM'), ('#333-44-6666', 'PHONE'), ('no:A334455B', 'IDNUM'), ('( 302 ) 786-5227', 'PHONE'), ('0295 Keats Street', 'STREET'), ('San Francisco', 'CITY')]

******************** ner_deid_synthetic Model Results ********************

[('Hendrickson , Ora', 'NAME'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'ID'), ('John Green', 'NAME'), ('1231511863', 'ID'), ('Day Hospital', 'LOCATION'), ('01/13/93', 'DATE'), ('1HGBH41JXMN109286', 'ID'), ('( 302', 'CONTACT'), ('786-5227', 'CONTACT'), ('0295 Keats Street', 'LOCATION'), ('San Francisco', 'LOCATION')]

******************** ner_deid_aipii Model Results ********************

[('Hendrickson', 'NAME'), ('2093-01-13', 'SSN'), ('John Green', 'STREET'), ('1231511863', 'IDNUM'), ('203.120.223.13', 'SSN'), ('( 302 ) 786-5227', 'PHONE'), ('0295 Keats Street', 'STREET'), ('San Francisco', 'CITY')]

******************** ner_deid_large_langtest Model Results ********************

[('Hendrickson , Ora', 'NAME'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'CONTACT'), ('John Green', 'NAME'), ('1231511863', 'ID'), ('Day Hospital', 'LOCATION'), ('01/13/93', 'DATE'), ('1HGBH41JXMN109286', 'ID'), ('no:A334455B', 'ID'), ('( 302 ) 786-5227', 'CONTACT'), ('0295 Keats Street', 'LOCATION'), ('San Francisco', 'LOCATION')]

******************** ner_deid_large Model Results ********************

[('Hendrickson , Ora', 'NAME'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'CONTACT'), ('John Green', 'NAME'), ('1231511863', 'ID'), ('Day Hospital', 'LOCATION'), ('01/13/93', 'DATE'), ('1HGBH41JXMN109286', 'ID'), ('( 302 ) 786-5227', 'CONTACT'), ('0295 Keats Street', 'LOCATION'), ('San Francisco', 'LOCATION')]

******************** ner_deid_subentity_docwise Model Results ********************

[('Hendrickson , Ora', 'PATIENT'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'DEVICE'), ('John Green', 'DOCTOR'), ('1231511863', 'IDNUM'), ('203.120.223.13', 'DATE'), ('60-year-old', 'AGE'), ('01/13/93', 'DATE'), ('1HGBH41JXMN109286', 'IDNUM'), ('no:A334455B', 'IDNUM'), ('( 302 ) 786-5227', 'PHONE'), ('0295 Keats Street', 'STREET'), ('San Francisco', 'CITY')]

******************** ner_deid_subentity_augmented_v2 Model Results ********************

[('Hendrickson , Ora', 'PATIENT'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'PHONE'), ('John Green', 'DOCTOR'), ('1231511863', 'IDNUM'), ('203.120.223.13', 'USERNAME'), ('60-year-old', 'AGE'), ('Day Hospital', 'HOSPITAL'), ('01/13/93', 'DATE'), ('1HGBH41JXMN109286', 'IDNUM'), ('#333-44-6666', 'IDNUM'), ('no:A334455B', 'PHONE'), ('( 302 ) 786-5227', 'PHONE'), ('0295 Keats Street', 'STREET'), ('San Francisco', 'STATE')]

******************** ner_deid_subentity_augmented_docwise Model Results ********************

[('Hendrickson , Ora', 'PATIENT'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'PHONE'), ('John Green', 'DOCTOR'), ('1231511863', 'IDNUM'), ('203.120.223.13', 'PHONE'), ('60-year-old', 'AGE'), ('Day Hospital', 'HOSPITAL'), ('01/13/93', 'DATE'), ('1HGBH41JXMN109286', 'IDNUM'), ('#333-44-6666', 'IDNUM'), ('no:A334455B', 'PHONE'), ('( 302 ) 786-5227', 'PHONE'), ('0295 Keats Street , San Francisco', 'LOCATION')]

******************** zeroshot_ner_deid_subentity_merged_medium Model Results ********************

[('Hendrickson , Ora', 'PATIENT'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'IDNUM'), ('John Green', 'DOCTOR'), ('1231511863', 'IDNUM'), ('60-year-old', 'AGE'), ('Day Hospital', 'HOSPITAL'), ('01/13/93', 'DATE'), ('1HGBH41JXMN109286', 'IDNUM'), ('( 302 ) 786-5227', 'PHONE'), ('0295 Keats Street', 'STREET'), ('San Francisco', 'CITY')]

******************** ner_deid_sd_large Model Results ********************

[('Hendrickson , Ora', 'NAME'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'ID'), ('John Green', 'NAME'), ('1231511863', 'ID'), ('Day Hospital', 'LOCATION'), ('01/13/93', 'DATE'), ('786-5227', 'CONTACT'), ('0295 Keats Street', 'LOCATION'), ('San Francisco', 'LOCATION')]

******************** ner_deid_enriched_langtest Model Results ********************

[('Hendrickson , Ora', 'PATIENT'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'PHONE'), ('John Green', 'DOCTOR'), ('1231511863', 'IDNUM'), ('01/13/93', 'DATE'), ('1HGBH41JXMN109286', 'IDNUM'), ('( 302 ) 786-5227', 'PHONE'), ('0295 Keats Street', 'STREET'), ('San Francisco', 'CITY')]

******************** ner_deid_sd Model Results ********************

[('Hendrickson , Ora', 'NAME'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'CONTACT'), ('John Green', 'NAME'), ('1231511863', 'ID'), ('203.120.223.13', 'CONTACT'), ('01/13/93', 'DATE'), ('( 302 ) 786-5227', 'CONTACT'), ('0295 Keats Street', 'LOCATION'), ('San Francisco', 'LOCATION')]

******************** ner_deid_generic_augmented Model Results ********************

[('Hendrickson , Ora', 'NAME'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'CONTACT'), ('John Green', 'NAME'), ('1231511863', 'ID'), ('60-year-old', 'AGE'), ('Day Hospital', 'LOCATION'), ('01/13/93', 'DATE'), ('1HGBH41JXMN109286', 'ID'), ('#333-44-6666', 'ID'), ('no:A334455B', 'ID'), ('( 302 ) 786-5227', 'CONTACT'), ('0295 Keats Street', 'LOCATION'), ('San Francisco', 'LOCATION')]

******************** ner_deid_enriched Model Results ********************

[('Hendrickson , Ora', 'PATIENT'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'PHONE'), ('John Green', 'DOCTOR'), ('01/13/93', 'DATE'), ('( 302 ) 786-5227', 'PHONE'), ('0295 Keats Street', 'STREET'), ('San Francisco', 'CITY')]

******************** ner_deid_generic_augmented_langtest Model Results ********************

[('Hendrickson , Ora', 'NAME'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'CONTACT'), ('John Green', 'NAME'), ('1231511863', 'ID'), ('60-year-old', 'AGE'), ('01/13/93', 'DATE'), ('( 302 ) 786-5227', 'CONTACT'), ('0295 Keats Street', 'LOCATION'), ('San Francisco', 'LOCATION')]

******************** ner_deid_subentity_augmented Model Results ********************

[('Hendrickson , Ora', 'PATIENT'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'PHONE'), ('John Green', 'DOCTOR'), ('1231511863', 'DEVICE'), ('60-year-old', 'AGE'), ('Day Hospital', 'HOSPITAL'), ('01/13/93', 'DATE'), ('no:A334455B', 'IDNUM'), ('( 302 ) 786-5227', 'PHONE'), ('0295 Keats Street', 'STREET'), ('San Francisco', 'STATE')]

******************** ner_deid_generic_docwise Model Results ********************

[('Hendrickson , Ora', 'NAME'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'CONTACT'), ('John Green', 'NAME'), ('1231511863', 'ID'), ('IP', 'NAME'), ('203.120.223.13', 'DATE'), ('60-year-old', 'AGE'), ('01/13/93', 'DATE'), ('1HGBH41JXMN109286', 'ID'), ('#333-44-6666', 'ID'), ('no:A334455B', 'ID'), ('( 302 ) 786-5227 , 0295', 'CONTACT'), ('Keats Street', 'LOCATION'), ('San Francisco', 'LOCATION')]

******************** ner_deid_generic_augmented_allUpperCased_langtest Model Results ********************

[('Hendrickson , Ora', 'NAME'), ('2093-01-13', 'DATE'), ('25', 'AGE'), ('719435', 'ID'), ('John Green', 'NAME'), ('1231511863', 'ID'), ('60-year-old', 'AGE'), ('01/13/93', 'DATE'), ('1HGBH41JXMN109286 , SSN', 'NAME'), ('#333-44-6666', 'ID'), ('no:A334455B', 'ID'), ('( 302 ) 786-5227', 'CONTACT'), ('0295 Keats Street', 'LOCATION'), ('San Francisco', 'LOCATION')]
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_profiling_deidentification|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- TextMatcherInternalModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- TextMatcherInternalModel
- PretrainedZeroShotNER
- NerConverterInternalModel
- Finisher
