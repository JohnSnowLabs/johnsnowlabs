---
layout: model
title: Financial FLAN-T5 Text Generation (Base)
author: John Snow Labs
name: fingen_flant5_base
date: 2023-04-21
tags: [en, licensed, generation, flan_t5, finance, tensorflow]
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

FLAN-T5 is an enhanced version of the original T5 model and is designed to produce better quality and more coherent text generation. It is trained on a large dataset of diverse texts and can generate high-quality summaries of articles, documents, and other text-based inputs. The model can also be utilized to generate financial text.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/fingen_flant5_base_en_1.0.0_3.0_1682073956957.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/fingen_flant5_base_en_1.0.0_3.0_1682073956957.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("question")

flant5 = finance.TextGenerator.pretrained('fingen_flant5_base','en','finance/models')\
    .setInputCols(["question"])\
    .setOutputCol("generated_text")
    .setMaxNewTokens(150)\
    .setStopAtEos(True)
  

pipeline = nlp.Pipeline(stages=[document_assembler, flant5])

data = spark.createDataFrame([
  [1, "Explain what is Sec 10-k filing "]
]).toDF('id', 'text')

results = pipeline.fit(data).transform(data)

results.select("generated_text.result").show(truncate=False)
```

</div>

## Results

```bash
+--------------------------------------------------------------------------------------------------------------------+
|result                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------+
|[Sec 10k filing is a form of tax filing that requires a party to file jointly or several entities for tax purposes.]|
+--------------------------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|fingen_flant5_base|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|920.9 MB|
