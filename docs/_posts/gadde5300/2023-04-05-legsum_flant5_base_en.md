---
layout: model
title: Legal FLAN-T5 Summarization (Base)
author: John Snow Labs
name: legsum_flant5_base
date: 2023-04-05
tags: [en, legal, flant5, t5, summarization, licensed, tensorflow]
task: Summarization
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: LegalSummarizer
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legsum_flant5_base_en_1.0.0_3.0_1680709193886.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legsum_flant5_base_en_1.0.0_3.0_1680709193886.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("documents")

flant5 = legal.Summarizer().pretrained('legsum_flant5_base','en','legal/models')\
    .setInputCols(["documents"])\
    .setOutputCol("summary")

pipeline = nlp.Pipeline(stages=[document_assembler, flant5])

data = spark.createDataFrame([
  [1, "The defendant was found guilty of first-degree murder and sentenced to life in prison without the possibility of parole."]
]).toDF('id', 'text')

results = pipeline.fit(data).transform(data)

results.select("summary.result").show(truncate=False)
```

</div>

## Results

```bash
+------------------------------------------------------------------------------------------------------------+
|result                                                                                                      |
+------------------------------------------------------------------------------------------------------------+
|[A man has been sentenced to life in prison without parole after being found guilty of first-degree murder.]|
+------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legsum_flant5_base|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|920.9 MB|
