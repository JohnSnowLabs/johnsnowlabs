---
layout: model
title: Financial Suspicious Activity Reports Pipeline
author: John Snow Labs
name: finpipe_suspicious_activity_reports
date: 2023-04-27
tags: [finance, en, licensed, pipeline]
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

This is a finance Pretrained pipeline aimed to extract entities from suspicious activity reports that are filed by financial institutions, and those associated with their business, with the Financial Crimes Enforcement Network.

## Predicted Entities

`ORG`, `ADDRESS`, `ROLE`, `DATE`,`SUSPICIOUS_ITEMS`, `PERSON_NAME`, `SUSPICIOUS_ACTION`, `SUSPICIOUS_KEYWORD`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finpipe_suspicious_activity_reports_en_1.0.0_3.0_1682595607527.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finpipe_suspicious_activity_reports_en_1.0.0_3.0_1682595607527.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from johnsnowlabs import PretrainedPipeline

sar_pipeline = PretrainedPipeline("finpipe_suspicious_activity_reports", "en", "finance/models")
```

</div>

## Results

```bash
+-------------------------+------------------+
|chunk                    |ner_label         |
+-------------------------+------------------+
|SUSPICIOUS               |SUSPICIOUS_KEYWORD|
|April 25, 2023           |DATE              |
|John Doe                 |PERSON_NAME       |
|Senior Compliance Officer|ROLE              |
|SUSPICIOUS_ACTION        |SUSPICIOUS_KEYWORD|
|Unusual                  |SUSPICIOUS_KEYWORD|
|SUSPICIOUS_KEYWORD       |SUSPICIOUS_KEYWORD|
|Money Laundering         |SUSPICIOUS_ACTION |
|SUSPICIOUS_ITEMS         |SUSPICIOUS_KEYWORD|
|deposits                 |SUSPICIOUS_ITEMS  |
|cash                     |SUSPICIOUS_ITEMS  |
|Currency                 |SUSPICIOUS_ITEMS  |
|sums of money            |SUSPICIOUS_ITEMS  |
|bank accounts            |SUSPICIOUS_ITEMS  |
|tax                      |SUSPICIOUS_ITEMS  |
|April 24, 2023           |DATE              |
|XYZ Bank                 |ORG               |
+-------------------------+------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finpipe_suspicious_activity_reports|
|Type:|pipeline|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.2 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- TokenizerModel
- BertEmbeddings
- BertEmbeddings
- FinanceNerModel
- FinanceNerModel
- FinanceBertForTokenClassification
- NerConverterInternalModel
- NerConverterInternalModel
- NerConverterInternalModel
- ContextualParserModel
- ChunkMergeModel
