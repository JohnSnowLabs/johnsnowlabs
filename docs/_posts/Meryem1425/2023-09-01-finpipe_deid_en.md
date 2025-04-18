---
layout: model
title: Financial Deidentification Pipeline
author: John Snow Labs
name: finpipe_deid
date: 2023-09-01
tags: [licensed, en, finance, deid, deidentification, anonymization]
task: Pipeline Finance
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a Pretrained Pipeline aimed to deidentify legal and financial documents to be compliant with data privacy regulations as GDPR and CCPA. Since the models used in this pipeline are statistical, make sure you use this model in a human-in-the-loop process to guarantee a 100% accuracy.

You can carry out both masking and obfuscation with this pipeline, on the following entities:
`ALIAS`, `EMAIL`, `PHONE`, `PROFESSION`, `ORG`, `DATE`, `PERSON`, `ADDRESS`, `STREET`, `CITY`, `STATE`, `ZIP`, `COUNTRY`, `TITLE_CLASS`, `TICKER`, `STOCK_EXCHANGE`, `CFN`, `IRS`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finpipe_deid_en_1.0.0_3.0_1693599372226.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finpipe_deid_en_1.0.0_3.0_1693599372226.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("finpipe_deid", "en", "finance/models")

result = deid_pipeline.annotate("""CARGILL, INCORPORATED

By:     Pirkko Suominen



Name: Pirkko Suominen Title: Director, Bio Technology Development  Center,  Date:   10/19/2011

BIOAMBER, SAS

By:     Jean-François Huc



Name: Jean-François Huc  Title: President Date:   October 15, 2011

email : jeanfran@gmail.com
phone : 18087339090 """)

```

</div>

## Results

```bash
Masked with entity labels
------------------------------
<PARTY>, <PARTY>
By:     <SIGNING_PERSON>
Name: <PARTY>: <SIGNING_TITLE>,  Date:   <EFFDATE>
<PARTY>, <PARTY>
By:     <SIGNING_PERSON>
Name: <PARTY>: <SIGNING_TITLE>Date:   <EFFDATE>

email : <EMAIL>
phone : <PHONE>

Masked with chars
------------------------------
[*****], [**********]
By:     [*************]
Name: [*******************]: [**********************************]  Center,  Date:   [********]
[******], [*]
By:     [***************]
Name: [**********************]: [*******]Date:   [**************]

email : [****************]
phone : [********]

Masked with fixed length chars
------------------------------
****, ****
By:     ****
Name: ****: ****,  Date:   ****
****, ****
By:     ****
Name: ****: ****Date:   ****

email : ****
phone : ****

Obfuscated
------------------------------
MGT Trust Company, LLC., Clarus llc.
By:     Benjamin Dean
Name: John Snow Labs Inc: Sales Manager,  Date:   03/08/2025
Clarus llc., SESA CO.
By:     JAMES TURNER
Name: MGT Trust Company, LLC.: Business ManagerDate:   11/7/2016

email : Tyrus@google.com
phone : 78 834 854

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finpipe_deid|
|Type:|pipeline|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|471.8 MB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- BertEmbeddings
- FinanceNerModel
- NerConverterInternalModel
- FinanceNerModel
- NerConverterInternalModel
- FinanceNerModel
- NerConverterInternalModel
- FinanceNerModel
- NerConverterInternalModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ChunkMergeModel
- DeIdentificationModel
- DeIdentificationModel
- DeIdentificationModel
- DeIdentificationModel