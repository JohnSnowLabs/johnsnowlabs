---
layout: model
title: Clinical Deidentification Pipeline Optimized Version (English - Subentity)
author: John Snow Labs
name: clinical_deidentification_subentity_optimized
date: 2024-03-14
tags: [deidentification, optimized, en, licensed, clinical, pipeline, obfuscation, mask]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be obfuscated in the resulting text and also masked with entitiy labels in the metadata. The pipeline can obfuscate and mask `AGE`, `DATE`, `PROFESSION`, `CITY`, `COUNTRY`, `DOCTOR`, `HOSPITAL`, `IDNUM`, `MEDICALRECORD`, `ORGANIZATION`, `PATIENT`, `PHONE`, `STREET`, `USERNAME`, `EMAIL`, `ZIP`, `ACCOUNT`, `LICENSE`, `VIN`, `SSN`, `DLN`, `PLATE`, `IPADDR` entities. This pipeline is built using the `ner_deid_subentity_augmented` model as well as `ContextualParser`, `RegexMatcher`, and `TextMatcher` and a single `Deidentification` stage for optimization.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_subentity_optimized_en_5.3.0_3.0_1710417564670.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_subentity_optimized_en_5.3.0_3.0_1710417564670.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_generic_optimized", "en", "clinical/models")

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR: 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Cocke Baptist Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

deid_result = deid_pipeline.fullAnnotate(text)

print('
'.join([i.metadata['masked'] for i in deid_result[0]['obfuscated']]))
print('
'.join([i.result for i in deid_result[0]['obfuscated']]))
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_generic_optimized", "en", "clinical/models")

val text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR: 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Cocke Baptist Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

val result = deid_pipeline.fullAnnotate(text)

println(deid_result(0)("obfuscated").map(_("metadata")("masked").toString).mkString("
"))
println(deid_result(0)("obfuscated").map(_("result").toString).mkString("
"))
```
</div>

## Results

```bash
Masked with entity labels
------------------------------
Name : <PATIENT>, Record date: <DATE>, MR: <MEDICALRECORD>.
Dr. <DOCTOR>, ID<IDNUM>, IP <IPADDR>.
He is a <AGE>-year-old male was admitted to the <HOSPITAL> for cystectomy on <DATE>.
Patient's VIN : <VIN>, SSN <SSN>, Driver's license no: <DLN>.
Phone <PHONE>, <STREET>, <CITY>, E-MAIL: <EMAIL>.

Obfuscated
------------------------------
Name : Lenor Coffin, Record date: 2093-03-13, MR: 427062.
Dr. Otila Kluver, ID: 3762831517, IP 444.444.444.444.
He is a 78-year-old male was admitted to the NOLAND HOSPITAL ANNISTON for cystectomy on 03/13/93.
Patient's VIN : 6HYWV37TGGY694854, SSN #627-03-5009, Driver's license no: F818299B.
Phone (716) 967-8938, 615 Ridge Rd, Edinburg, E-MAIL: Ascanius@yahoo.com.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_subentity_optimized|
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
