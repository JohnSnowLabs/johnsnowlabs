---
layout: model
title: Clinical Deidentification Pipeline (Document Wise)
author: John Snow Labs
name: ner_deid_nameAugmented_docwise_pipeline
date: 2025-03-25
tags: [deidentification, deid, en, licensed, clinical, pipeline, docwise]
task: Pipeline Healthcare
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_nameAugmented_docwise_pipeline_en_5.5.3_3.2_1742877971410.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_nameAugmented_docwise_pipeline_en_5.5.3_3.2_1742877971410.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("ner_deid_nameAugmented_docwise_pipeline", "en", "clinical/models")

text = """Record date : 2093-01-13, Name : Hendrickson ORA. 25 years-old, MRN #719435.
IP: 203.120.223.13, the driver's license no:A334455B. The SSN: 324598674 and e-mail: hale@gmail.com.
Patient's VIN : 1HGBH41JXMN109286. Date : 01/13/93, PCP : David Hale."""

deid_result = deid_pipeline.fullAnnotate(text)[0]


```

{:.jsl-block}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = nlp.PretrainedPipeline("ner_deid_nameAugmented_docwise_pipeline", "en", "clinical/models")

text = """Record date : 2093-01-13, Name : Hendrickson ORA. 25 years-old, MRN #719435.
IP: 203.120.223.13, the driver's license no:A334455B. The SSN: 324598674 and e-mail: hale@gmail.com.
Patient's VIN : 1HGBH41JXMN109286. Date : 01/13/93, PCP : David Hale."""

deid_result = deid_pipeline.fullAnnotate(text)[0]


```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("ner_deid_nameAugmented_docwise_pipeline", "en", "clinical/models")

val text = """Record date : 2093-01-13, Name : Hendrickson ORA. 25 years-old, MRN #719435.
IP: 203.120.223.13, the driver's license no:A334455B. The SSN: 324598674 and e-mail: hale@gmail.com.
Patient's VIN : 1HGBH41JXMN109286. Date : 01/13/93, PCP : David Hale."""

val deid_result = deid_pipeline.fullAnnotate(text)[0]



```
</div>

## Results

```bash

+-----------------+-----+---+-------------+
|result           |begin|end|entity       |
+-----------------+-----+---+-------------+
|2093-01-13       |14   |23 |DATE         |
|Hendrickson ORA  |33   |47 |NAME         |
|25               |50   |51 |AGE          |
|#719435          |68   |74 |MEDICALRECORD|
|203.120.223.13   |81   |94 |IP           |
|no:A334455B      |118  |128|DLN          |
|324598674        |140  |148|SSN          |
|hale@gmail.com   |162  |175|EMAIL        |
|1HGBH41JXMN109286|194  |210|VIN          |
|01/13/93         |220  |227|DATE         |
|David Hale       |236  |245|NAME         |
+-----------------+-----+---+-------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_nameAugmented_docwise_pipeline|
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
