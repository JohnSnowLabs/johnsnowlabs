---
layout: model
title: Clinical Deidentification Pipeline (English)
author: John Snow Labs
name: clinical_deidentification_docwise_wip
date: 2024-09-25
tags: [deidentification, en, deid, licensed, clinical, pipeline, sent_wise]
task: Pipeline Healthcare
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

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_docwise_wip_en_5.4.1_3.4_1727248183384.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_docwise_wip_en_5.4.1_3.4_1727248183384.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_docwise_wip", "en", "clinical/models")

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR: 87719435.
ID: #12315112, Dr. John Green, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco,  CA 94108. E-MAIL: smith@gmail.com."""

deid_result = deid_pipeline.fullAnnotate(text)

print(''.join([i.metadata['masked'] for i in deid_result[0]['obfuscated']]))
print(''.join([i.result for i in deid_result[0]['obfuscated']]))
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_docwise_wip", "en", "clinical/models")

val text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR: 87719435.
ID: #12315112, Dr. John Green, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco,  CA 94108. E-MAIL: smith@gmail.com."""

val deid_result = deid_pipeline.fullAnnotate(text)

println(deid_result(0)("obfuscated").map(_("metadata")("masked").toString).mkString(""))
println(deid_result(0)("obfuscated").map(_("result").toString).mkString(""))
```
</div>

## Results

```bash
Masked with entity labels
------------------------------
Name : <PATIENT>, Record date: <DATE>, MR: <MEDICALRECORD>.
ID: <IDNUM>, Dr. <DOCTOR>, IP <IPADDR>.
He is a <AGE>-year-old male was admitted to the <HOSPITAL> for cystectomy on <DATE>.
Patient's VIN : <VIN>, SSN <SSN>, Driver's license no: <DLN>.
Phone <PHONE>, <STREET>, <CITY>,  <STATE> <ZIP>.
E-MAIL: <EMAIL>.

Obfuscated
------------------------------
Name : Axel Bohr, Record date: 2093-02-01, MR: 61443154.
ID: #00867619, Dr. Rickard Charles, IP 002.002.002.002.
He is a 73-year-old male was admitted to the LOMA LINDA UNIVERSITY MEDICAL CENTER-MURRIETA for cystectomy on 02/01/93.
Patient's VIN : 5KDTO67TIWP809983, SSN #382-50-5397, Driver's license no: Q734193X.
Phone (902) 409-7353, 1555 Long Pond Road, Pomeroy,  Maryland 29924.
 E-MAIL: Halit@google.com.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_docwise_wip|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DocumentAssembler
- InternalDocumentSplitter
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- MedicalNerModel
- MedicalNerModel
- NerConverterInternalModel
- NerConverterInternalModel
- NerConverterInternalModel
- ChunkMergeModel
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
- LightDeIdentification
- LightDeIdentification
