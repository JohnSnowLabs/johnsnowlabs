---
layout: model
title: Resolver Company Names to Tickers
author: John Snow Labs
name: finel_names2tickers_fe
date: 2024-06-11
tags: [finance, companies, ticker, nasdaq, licensed, en]
task: Entity Resolution
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is an Entity Resolution / Entity Linking model, which is able to provide Ticker / Trading Symbols using a Company Name as an input. You can use any NER which extracts Organizations / Companies / Parties to then send the output to this Entity Linking model and get the Ticker / Trading Symbol (given the company has one).

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finel_names2tickers_fe_en_1.0.0_3.0_1718110711125.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finel_names2tickers_fe_en_1.0.0_3.0_1718110711125.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("ner_chunk")

embeddings = nlp.BGEEmbeddings.pretrained("finance_bge_base_embeddings", "en", "finance/models")\ 
      .setInputCols("ner_chunk") \
      .setOutputCol("sentence_embeddings")
    
resolver = finance.SentenceEntityResolverModel.pretrained("finel_names2tickers_fe", "en", "finance/models") \
      .setInputCols(["ner_chunk", "sentence_embeddings"]) \
      .setOutputCol("name")\
      .setDistanceFunction("EUCLIDEAN")

pipelineModel = nlp.Pipeline(
      stages = [
          documentAssembler,
          embeddings,
          resolver])

lp = LightPipeline(pipelineModel)

lp.fullAnnotate("Tesla")
```

</div>

## Results

```bash
['TSLA']
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finel_names2tickers_fe|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[normalized]|
|Language:|en|
|Size:|115.6 MB|
|Case sensitive:|false|

## References

https://data.world/johnsnowlabs/list-of-companies-in-nasdaq-exchanges