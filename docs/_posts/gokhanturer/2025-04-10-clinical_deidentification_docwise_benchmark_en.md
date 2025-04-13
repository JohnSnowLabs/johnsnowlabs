---
layout: model
title: Clinical Deidentification Pipeline (Document Wise - Benchmark)
author: John Snow Labs
name: clinical_deidentification_docwise_benchmark
date: 2025-04-10
tags: [licensed, en, deidentification, deid, pipeline, clinical, docwise, benchmark]
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

This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. The pipeline can mask and obfuscate `NAME`, `IDNUM`, `CONTACT`, `LOCATION`, `AGE`, `DATE` entities.
**This pipeline is prepared for benchmarking with cloud providers.**

## Predicted Entities

`NAME`, `IDNUM`, `CONTACT`, `LOCATION`, `AGE`, `DATE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_docwise_benchmark_en_5.5.3_3.0_1744313407180.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_docwise_benchmark_en_5.5.3_3.0_1744313407180.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_docwise_benchmark", "en", "clinical/models")               

deid_result = deid_pipeline.fullAnnotate("""Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B.
Phone (302) 786-5227, Keats Street, San Francisco, E-MAIL: smith@gmail.com.""")

print(''.join([i.result for i in deid_result['mask_entity']]))
print(''.join([i.result for i in deid_result['obfuscated']]))

```

{:.jsl-block}
```python

deid_pipeline = nlp.PretrainedPipeline("clinical_deidentification_docwise_benchmark", "en", "clinical/models")               

deid_result = deid_pipeline.fullAnnotate("""Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B.
Phone (302) 786-5227, Keats Street, San Francisco, E-MAIL: smith@gmail.com.""")

print(''.join([i.result for i in deid_result['mask_entity']]))
print(''.join([i.result for i in deid_result['obfuscated']]))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_docwise_benchmark", "en", "clinical/models")               

val deid_result = deid_pipeline.fullAnnotate("""Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B.
Phone (302) 786-5227, Keats Street, San Francisco, E-MAIL: smith@gmail.com.""")

println(deid_result("mask_entity").map(_("result").toString).mkString(""))
println(deid_result("obfuscated").map(_("result").toString).mkString(""))

```
</div>

## Results

```bash

Masked with entity labels
------------------------------
Name : <NAME>, Record date: <DATE>, # <IDNUM>.
Dr. <NAME>, ID: <IDNUM>, IP <IDNUM>.
He is a <AGE> male was admitted to the <LOCATION> for cystectomy on <DATE>.
Patient's VIN : <IDNUM>, SSN <IDNUM>, Driver's license <IDNUM>.
Phone <CONTACT>, <LOCATION>, <LOCATION>, E-MAIL: <CONTACT>.


Obfuscated
------------------------------
Name : Lawson Prey, Record date: 2093-02-13, # 931857.
Dr. May Sparks, ID: 6986066538, IP 089.708.009.79.
He is a 70-year-old male was admitted to the 2190 Hwy 85 N for cystectomy on 02/13/93.
Patient's VIN : 9LWRL49JVQN907286, SSN #222-55-7777, Driver's license YZ:Z447766W.
Phone (091) 475-2114, 506 Lenox Avenue, 13111 N Port Washington Rd, E-MAIL: KYUPT@EYCUX.AWY.

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_docwise_benchmark|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.5 GB|

## Included Models

- DocumentAssembler
- InternalDocumentSplitter
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- MedicalNerModel
- MedicalNerModel
- NerConverterInternalModel
- NerConverterInternalModel
- NerConverterInternalModel
- PretrainedZeroShotNER
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ContextualEntityRuler
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
- ContextualParserModel
- RegexMatcherInternalModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- ChunkMergeModel
- ChunkMergeModel
- ContextualEntityRuler
- ChunkMergeModel
- LightDeIdentification
- LightDeIdentification