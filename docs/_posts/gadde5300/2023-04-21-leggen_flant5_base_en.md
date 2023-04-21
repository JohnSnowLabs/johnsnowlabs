---
layout: model
title: Legal FLAN-T5 Text Generation (Base)
author: John Snow Labs
name: leggen_flant5_base
date: 2023-04-21
tags: [en, licensed, legal, flan_t5, generation, tensorflow]
task: Text Generation
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: LegalTextGenerator
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

FLAN-T5 is an enhanced version of the original T5 model and is designed to produce better quality and more coherent text generation. It is trained on a large dataset of diverse texts and can generate high-quality summaries of articles, documents, and other text-based inputs.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/leggen_flant5_base_en_1.0.0_3.0_1682073962277.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/leggen_flant5_base_en_1.0.0_3.0_1682073962277.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("question")

flant5 = legal.TextGenerator.pretrained('leggen_flant5_base','en','legal/models')\
    .setInputCols(["question"])\
    .setOutputCol("summary")
    .setMaxNewTokens(150)\
    .setStopAtEos(True)
  
pipeline = nlp.Pipeline(stages=[document_assembler, flant5])
data = spark.createDataFrame([
  [1, "What is a NDA?"]
]).toDF('id', 'text')
results = pipeline.fit(data).transform(data)
results.select("summary.result").show(truncate=False)
```

</div>

## Results

```bash
+----------------------------+
|result                      |
+----------------------------+
|[a non-disclosure agreement]|
+----------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|leggen_flant5_base|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|920.9 MB|