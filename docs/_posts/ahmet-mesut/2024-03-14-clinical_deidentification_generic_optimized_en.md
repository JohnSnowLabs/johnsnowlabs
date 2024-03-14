---
layout: model
title: Clinical Deidentification Pipeline Optimized Version (English - Generic)
author: John Snow Labs
name: clinical_deidentification_generic_optimized
date: 2024-03-14
tags: [deidentification, optimized, en, licensed, clinical, pipeline, obfuscation, mask]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be obfuscated in the resulting text and also masked with entitiy labels in the metadata. The pipeline can obfuscate and mask `AGE`, `CONTACT`, `DATE`, `LOCATION`, `NAME`, `PROFESSION`, `CITY`, `COUNTRY`, `DOCTOR`, `HOSPITAL`, `IDNUM`, `MEDICALRECORD`, `ORGANIZATION`, `PATIENT`, `PHONE`, `STREET`, `USERNAME`, `ZIP`, `ACCOUNT`, `LICENSE`, `VIN`, `SSN`, `DLN`, `PLATE`, `IPADDR` entities. This pipeline is built using the `ner_deid_generic_augmented` model as well as `ContextualParser`, `RegexMatcher`, and `TextMatcher` and a single `Deidentification` stage for optimization.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_generic_optimized_en_5.3.0_3.2_1710409456868.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_generic_optimized_en_5.3.0_3.2_1710409456868.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_generic_optimized", "en", "clinical/models")

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR #719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

result = deid_pipeline.fullAnnotate(text)


```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_generic_optimized", "en", "clinical/models")

val text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR #719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

val result = deid_pipeline.fullAnnotate(text)

```
</div>

## Results

```bash

|index|Sentence|Masked|Obfuscated|
|---|---|---|---|
|0|Name : Hendrickson, Ora, Record date: 2093-01-13, MR \#719435\.|Name : \<NAME\>, Record date: \<DATE\>, MR \<ID\>\.|Name : Chesley Noon, Record date: 2093-02-18, MR \#536644\.|
|1|Dr\. John Green, ID: 1231511863, IP 203\.120\.223\.13\.|Dr\. \<NAME\>, ID: \<ID\>, IP \<IPADDR\>\.|Dr\. Su Grand, ID: 0347425956, IP 333\.333\.333\.333\.|
|2|He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93\.|He is a \<AGE\>-year-old male was admitted to the \<LOCATION\> for cystectomy on \<DATE\>\.|He is a 79-year-old male was admitted to the 1000 Trancas Street for cystectomy on 02/18/93\.|
|3|Patient's VIN : 1HGBH41JXMN109286, SSN \#333-44-6666, Driver's license no: A334455B\.|Patient's VIN : \<VIN\>, SSN \<SSN\>, Driver's license no: \<DLN\>\.|Patient's VIN : 3OVFI43PIRJ188416, SSN \#606-30-1601, Driver's license no: U932355D\.|
|4|Phone \(302\) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail\.com\.|Phone \<PHONE\>, \<LOCATION\>, \<LOCATION\>, E-MAIL: \<EMAIL\>\.|Phone \(322\) 025-4270, 1301 S Main Street, 1514 Vernon Road, E-MAIL: Toto@hotmail\.com\.|

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_generic_optimized|
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
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- TextMatcherInternalModel
- ContextualParserModel
- RegexMatcherModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ChunkMergeModel
- ChunkMergeModel
- DeIdentificationModel
- Finisher