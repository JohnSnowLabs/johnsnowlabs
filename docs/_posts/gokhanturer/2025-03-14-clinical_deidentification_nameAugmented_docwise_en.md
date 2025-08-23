---
layout: model
title: Clinical Deidentification Pipeline (Document Wise)
author: John Snow Labs
name: clinical_deidentification_nameAugmented_docwise
date: 2025-03-14
tags: [deidentification, deid, en, licensed, clinical, pipeline, docwise]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.5.3
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text.
The pipeline can mask and obfuscate `ACCOUNT`, `AGE`, `BIOID`, `CITY`, `CONTACT`, `COUNTRY`, `DATE`, `DEVICE`, `DLN`, `EMAIL`, `FAX`, `HEALTHPLAN`, `IDNUM`, `IP`,
`LICENSE`, `LOCATION`, `MEDICALRECORD`, `NAME`, `PHONE`, `PLATE`, `PROFESSION`, `SSN`, `STATE`, `STREET`, `URL`, `VIN`, `ZIP` entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_nameAugmented_docwise_en_5.5.3_3.2_1741966261404.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_nameAugmented_docwise_en_5.5.3_3.2_1741966261404.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_nameAugmented_docwise", "en", "clinical/models")

text = """Record date : 2093-01-13, Name : Hendrickson ORA. 25 years-old, MRN #719435.
IP: 203.120.223.13, the driver's license no:A334455B. The SSN: 324598674 and e-mail: hale@gmail.com.
Patient's VIN : 1HGBH41JXMN109286. Date : 01/13/93, PCP : David Hale."""

deid_result = deid_pipeline.fullAnnotate(text)[0]

print(''.join([i.result for i in deid_result['mask_entity']]))
print(''.join([i.result for i in deid_result['obfuscated']]))


```

{:.jsl-block}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = nlp.PretrainedPipeline("clinical_deidentification_nameAugmented_docwise", "en", "clinical/models")

text = """Record date : 2093-01-13, Name : Hendrickson ORA. 25 years-old, MRN #719435.
IP: 203.120.223.13, the driver's license no:A334455B. The SSN: 324598674 and e-mail: hale@gmail.com.
Patient's VIN : 1HGBH41JXMN109286. Date : 01/13/93, PCP : David Hale."""

deid_result = deid_pipeline.fullAnnotate(text)[0]

print(''.join([i.result for i in deid_result['mask_entity']]))
print(''.join([i.result for i in deid_result['obfuscated']]))


```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_nameAugmented_docwise", "en", "clinical/models")

val text = """Record date : 2093-01-13, Name : Hendrickson ORA. 25 years-old, MRN #719435.
IP: 203.120.223.13, the driver's license no:A334455B. The SSN: 324598674 and e-mail: hale@gmail.com.
Patient's VIN : 1HGBH41JXMN109286. Date : 01/13/93, PCP : David Hale."""

val deid_result = deid_pipeline.fullAnnotate(text)[0]

println(deid_result("mask_entity").map(_("result").toString).mkString(""))
println(deid_result("obfuscated").map(_("result").toString).mkString(""))


```
</div>

## Results

```bash

Masked with entity labels
------------------------------
Record date : <DATE>, Name : <NAME>. <AGE> years-old, MRN <MEDICALRECORD>.
IP: <IP>, the driver's license <DLN>. The SSN: <SSN> and e-mail: <EMAIL>.
Patient's VIN : <VIN>. Date : <DATE>, PCP : <NAME>.

Obfuscated
------------------------------
Record date : 2093-03-04, Name : Ronalee Cocking. 33 years-old, MRN #153079.
IP: 177.192.38.52, the driver's license FG:G114433D. The SSN: 891045321 and e-mail: Andi@google.com.
Patient's VIN : 5ZKFZ05XJEB563842. Date : 03/04/93, PCP : Solmon Dupont.

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_nameAugmented_docwise|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.9 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- InternalDocumentSplitter
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
- LightDeIdentification
- LightDeIdentification