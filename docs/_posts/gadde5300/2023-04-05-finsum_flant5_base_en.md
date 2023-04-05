---
layout: model
title: Financial FLAN-T5 Summarization (Base)
author: John Snow Labs
name: finsum_flant5_base
date: 2023-04-05
tags: [finance, en, flant5, t5, summarization, licensed, tensorflow]
task: Summarization
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: FinanceSummarizer
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

FLAN-T5 is a state-of-the-art language model developed by Facebook AI that utilizes the T5 architecture for text summarization tasks. It is trained on a large dataset of diverse texts and can generate high-quality summaries of articles, documents, and other text-based inputs.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finsum_flant5_base_en_1.0.0_3.0_1680700696220.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finsum_flant5_base_en_1.0.0_3.0_1680700696220.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("documents")

flant5 = finance.Summarizer().pretrained('finsum_flant5_base','en','finance/models')\
    .setInputCols(["documents"])\
    .setOutputCol("flan_t5_output")

pipeline = nlp.Pipeline(stages=[document_assembler, flant5])

data = spark.createDataFrame([
  [1, "Based on the financial data provided, it appears that the company has experienced steady growth in revenue over the past few years. However, this growth has been offset by increasing expenses, particularly in the areas of research and development, and marketing and advertising. As a result, the company's profit margins have remained relatively stable, but have not shown significant improvement."]
]).toDF('id', 'text')

results = pipeline.fit(data).transform(data)

results.select("flan_t5_output.result").show(truncate=False)
```

</div>

## Results

```bash
+------------------------------------------------------------------------------------------------------------+
|result                                                                                                      |
+------------------------------------------------------------------------------------------------------------+
|[The company's revenue has been growing but the company's expenses have been offset by increasing revenues.]|
+------------------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finsum_flant5_base|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|920.9 MB|
