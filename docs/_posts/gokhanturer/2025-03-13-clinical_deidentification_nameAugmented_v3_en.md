---
layout: model
title: Clinical Deidentification Pipeline (Sentence Wise)
author: John Snow Labs
name: clinical_deidentification_nameAugmented_v3
date: 2025-03-13
tags: [deidentification, deid, en, licensed, clinical, pipeline, name]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.5.3
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text.
The pipeline can mask and obfuscate `ACCOUNT`, `AGE`, `BIOID`, `CITY`, `CONTACT`, `COUNTRY`, `DATE`, `DEVICE`, `DLN`, `EMAIL`, `FAX`, `HEALTHPLAN`, `IDNUM`, `IP`, `LICENSE`,
`LOCATION`, `MEDICALRECORD`, `NAME`, `ORGANIZATION`, `PHONE`, `PLATE`, `PROFESSION`, `SSN`, `STATE`, `STREET`, `VIN`, `ZIP` entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_nameAugmented_v3_en_5.5.3_3.0_1741880764602.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_nameAugmented_v3_en_5.5.3_3.0_1741880764602.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_nameAugmented_v3", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline2.fullAnnotate(text)[0]

print(''.join([i.metadata['masked'] for i in deid_result['obfuscated']]))
print(''.join([i.result for i in deid_result['obfuscated']]))

```

{:.jsl-block}
```python

deid_pipeline = nlp.PretrainedPipeline("clinical_deidentification_nameAugmented_v3", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)[0]

print(''.join([i.metadata['masked'] for i in deid_result['obfuscated']]))
print(''.join([i.result for i in deid_result['obfuscated']]))


```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_nameAugmented_v3", "en", "clinical/models")

val text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 ."""

val deid_result = deid_pipeline.fullAnnotate(text)[0]

println(deid_result("obfuscated").map(_("metadata")("masked").toString).mkString(""))
println(deid_result("obfuscated").map(_("result").toString).mkString(""))

```
</div>

## Results

```bash

Masked with entity labels
------------------------------
Dr. <NAME>, from <LOCATION> in <CITY>,  attended to the patient on <DATE>.
The patient’s medical record number is <MEDICALRECORD>.
The patient, <NAME>, is <AGE> years old,  her Contact number: <PHONE> .

Obfuscated
------------------------------
Dr. Rhodia Cera, from 252 Mchenry St in UNTERLAND,  attended to the patient on 18/06/2024.
The patient’s medical record number is 16109604.
The patient, Eulice Hickory, is 44 years old,  her Contact number: 540-981-1914 .

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_nameAugmented_v3|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.9 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- NerDLModel
- NerConverterInternalModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
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
- TextMatcherInternalModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- ContextualParserModel
- RegexMatcherInternalModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- TextMatcherInternalModel
- ChunkMergeModel
- ChunkMergeModel
- DeIdentificationModel
