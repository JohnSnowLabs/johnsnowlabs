---
layout: model
title: Clinical Deidentification Pipeline (English)
author: John Snow Labs
name: clinical_deidentification_nameAugmented_v2
date: 2024-10-02
tags: [deidentification, deid, en, licensed, clinical, pipeline, sent_wise]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. The pipeline can mask and obfuscate `ACCOUNT`, `AGE`, `BIOID`, `CITY`, `CONTACT`, `COUNTRY`, `DATE`, `DEVICE`, `DLN`, `DOCTOR`, `EMAIL`, `FAX`, `HEALTHPLAN`, `HOSPITAL`, `ID`, `IPADDR`, `LICENSE`, `LOCATION`, `MEDICALRECORD`, `NAME`, `ORGANIZATION`, `PATIENT`, `PHONE`, `PLATE`, `PROFESSION`, `SREET`, `SSN`, `STATE`, `STREET`, `URL`, `USERNAME`, `VIN`, `ZIP` entities.

## Predicted Entities

`ACCOUNT`, `AGE`, `BIOID`, `CITY`, `CONTACT`, `COUNTRY`, `City`, `Country`, `DATE`, `DEVICE`, `DLN`, `EMAIL`, `FAX`, `HEALTHPLAN`, `HOSPITAL`, `ID`, `IDNUM`, `IP`, `LICENSE`, `LOCATION`, `LOCATION-OTHER`, `LOCATION_OTHER`, `MEDICALRECORD`, `NAME`, `ORGANIZATION`, `PHONE`, `PLATE`, `PROFESSION`, `SSN`, `STATE`, `STREET`, `URL`, `VIN`, `ZIP`


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_nameAugmented_v2_en_5.4.1_3.4_1727897157489.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_nameAugmented_v2_en_5.4.1_3.4_1727897157489.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_nameAugmented_v2", "en", "clinical/models")

text = """Dr. John Taylor, a cardiologist at St. Mary's Hospital in Boston, was contacted on 05/10/2023 regarding a 45-year-old male patient."""

deid_result = deid_pipeline.fullAnnotate(text)

print(''.join([i.metadata['masked'] for i in deid_result[0]['obfuscated']]))
print(''.join([i.result for i in deid_result[0]['obfuscated']]))
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_nameAugmented_v2", "en", "clinical/models")

val text = """Dr. John Taylor, a cardiologist at St. Mary's Hospital in Boston, was contacted on 05/10/2023 regarding a 45-year-old male patient."""

val deid_result = deid_pipeline.fullAnnotate(text)

println(deid_result(0)("obfuscated").map(_("metadata")("masked").toString).mkString(""))
println(deid_result(0)("obfuscated").map(_("result").toString).mkString(""))
```
</div>

## Results

```bash
Masked with entity labels
------------------------------
Dr. <NAME>, a <PROFESSION> at <HOSPITAL> in <CITY>, was contacted on <DATE> regarding a <AGE>-year-old male patient.

Obfuscated
------------------------------
Dr. Rolande Cleverly, a Fish farm manager at NORTH COUNTRY HOSPITAL & HEALTH CENTER in BARMOLLOCH, was contacted on 16/10/2023 regarding a 48-year-old male patient.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_nameAugmented_v2|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.0+|
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
- RegexMatcherInternalModel
- ContextualParserModel
- ContextualParserModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- ContextualParserModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- ChunkMergeModel
- ChunkMergeModel
- DeIdentificationModel
- Finisher
