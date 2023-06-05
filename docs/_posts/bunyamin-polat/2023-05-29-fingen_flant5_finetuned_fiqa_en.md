---
layout: model
title: Financial Finetuned FLAN-T5 Text Generation (FIQA dataset)
author: John Snow Labs
name: fingen_flant5_finetuned_fiqa
date: 2023-05-29
tags: [en, finance, generation, licensed, flant5, fiqa, tensorflow]
task: Text Generation
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: FinanceTextGenerator
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The `fingen_flant5_finetuned_fiqa` model is the Text Generation model that has been fine-tuned on FLAN-T5 using FIQA dataset. FLAN-T5 is a state-of-the-art language model developed by Google AI that utilizes the T5 architecture for text-generation tasks.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/fingen_flant5_finetuned_fiqa_en_1.0.0_3.0_1685363340017.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/fingen_flant5_finetuned_fiqa_en_1.0.0_3.0_1685363340017.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

flant5 = finance.TextGenerator.pretrained("fingen_flant5_finetuned_fiqa", "en", "finance/models")\
    .setInputCols(["document"])\
    .setOutputCol("generated")\
    .setMaxNewTokens(256)\
    .setStopAtEos(True)\
    .setDoSample(True)\
    .setTopK(3)

pipeline = nlp.Pipeline(stages=[document_assembler, flant5])
 
data = spark.createDataFrame([
   [1, "How to have a small capital investment in US if I am out of the country?"]]).toDF('id', 'text')

results = pipeline.fit(data).transform(data)

results.select("generated.result").show(truncate=False)

```

</div>

## Results

```bash

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[I would suggest a local broker. They have diversified funds that are diversified and have the same fees as the US market. They also offer diversified portfolios that have the lowest risk.]|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|fingen_flant5_finetuned_fiqa|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|

## References

The dataset is available [here](https://huggingface.co/datasets/BeIR/fiqa)
