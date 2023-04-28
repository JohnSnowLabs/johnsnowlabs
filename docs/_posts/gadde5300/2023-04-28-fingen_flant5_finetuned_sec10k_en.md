---
layout: model
title: Financial Finetuned FLAN-T5 Text Generation ( SEC 10k Filings )
author: John Snow Labs
name: fingen_flant5_finetuned_sec10k
date: 2023-04-28
tags: [en, licensed, text_generation, tensorflow]
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

This Text Generation Mode has been fine-tuned on FLANT5 Using SEC filings data. FLAN-T5 is a state-of-the-art language model developed by Facebook AI that utilizes the T5 architecture for text generation tasks.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/fingen_flant5_finetuned_sec10k_en_1.0.0_3.0_1682669039071.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/fingen_flant5_finetuned_sec10k_en_1.0.0_3.0_1682669039071.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("question")

flant5 = finance.TextGenerator.pretrained('fingen_flant5_finetuned_sec10k','en','finance/models')\
    .setInputCols(["question"])\
    .setOutputCol("generated_text")
    .setMaxNewTokens(150)\
    .setStopAtEos(True)
  
pipeline = nlp.Pipeline(stages=[document_assembler, flant5])
data = spark.createDataFrame([
  [1, """Deferred revenue primarily consists of customer billings or payments received in advance of revenues being recognized from the company’s subscription and services contracts"""]
]).toDF('id', 'text')
results = pipeline.fit(data).transform(data)
results.select("generated_text.result").show(truncate=False)
```

</div>

## Results

```bash
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[The company’s deferred revenue is recognized ratably over the term of the contract, which is generally one year or less, based on the estimated useful lives of the customer and the expected life of the customer’s subscription or services contract, and the estimated useful lives of the customer’s subscription or services contract, if any, if the company determines that the estimated useful lives of the customer’s subscription or services contract are less than the estimated useful lives of the customer’s subscription or services contract, the company recognizes revenue ratably over the term of the contract, which is generally one year or less, based on the estimated useful lives of the customer’s subscription or services contract]|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|fingen_flant5_finetuned_sec10k|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|

## References

In house annotated dataset
