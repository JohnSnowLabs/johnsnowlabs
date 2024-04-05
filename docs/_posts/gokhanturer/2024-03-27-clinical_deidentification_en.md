---
layout: model
title: Clinical Deidentification Pipeline (English)
author: John Snow Labs
name: clinical_deidentification
date: 2024-03-27
tags: [deidentification, deid, licensed, en, clinical, pipeline]
task: De-identification
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. The pipeline can mask and obfuscate `AGE`, `CONTACT`, `DATE`, `LOCATION`, `NAME`, `PROFESSION`, `CITY`, `COUNTRY`, `DOCTOR`, `HOSPITAL`, `IDNUM`, `MEDICALRECORD`, `ORGANIZATION`, `PATIENT`, `PHONE`, `STREET`, `USERNAME`, `ZIP`, `ACCOUNT`, `LICENSE`, `VIN`, `SSN`, `DLN`, `PLATE`, `IPADDR` entities.

This pipeline is the optimized version of the previous `clinical_deidentification` pipelines, resulting in significantly improved speed. It returns obfuscated version of the texts as the result and its masked with entity labels version in the metadata.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_en_5.3.1_3.4_1711540321304.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_en_5.3.1_3.4_1711540321304.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification", "en", "clinical/models")

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR #719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

result = deid_pipeline.fullAnnotate(text)

print('\n'.join([i.metadata['masked'] for i in deid_result[0]['obfuscated']]))
print('\n'.join([i.result for i in deid_result[0]['obfuscated']])))
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification", "en", "clinical/models")

val text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR #719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

val result = deid_pipeline.fullAnnotate(text)

println(deid_result(0)("obfuscated").map(_("metadata")("masked").toString).mkString("\n"))
println(deid_result(0)("obfuscated").map(_("result").toString).mkString("\n"))
```
</div>

## Results

```bash
Masked with entity labels
------------------------------
Name : <PATIENT>, Record date: <DATE>, MR <ID>.
Dr. <DOCTOR>, ID: <DEVICE>, IP <IPADDR>.
He is a <AGE>-year-old male was admitted to the <HOSPITAL> for cystectomy on <DATE>.
Patient's VIN : <VIN>, SSN <SSN>, Driver's license no: <DLN>.
Phone <PHONE>, <STREET>, <CITY>, E-MAIL: <EMAIL>.

Obfuscated
------------------------------
Name : Lucretia Kern, Record date: 2093-02-16, MR #169678.
Dr. Ramon Dredge, ID: U4680041, IP 005.005.005.005.
He is a 79-year-old male was admitted to the ST. JOSEPH REGIONAL MEDICAL CENTER for cystectomy on 02/16/93.
Patient's VIN : 9FYBO17PZWC585277, SSN #824-23-5361, Driver's license no: W431540G.
Phone (867) 619-5093, 800 Share Drive, Wilburton, E-MAIL: Rufus@google.com.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification|
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
