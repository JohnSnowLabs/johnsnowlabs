---
layout: model
title: Resolve Tickers to Company Names
author: John Snow Labs
name: finel_tickers2names_fe
date: 2024-06-12
tags: [nasdaq, companies, finance, licensed, en]
task: Entity Resolution
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
recommended: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is an Entity Resolution / Entity Linking model, which is able to provide Company Names given their Ticker / Trading Symbols. You can use any NER which extracts Tickersto then send the output to this Entity Linking model and get the Company Name.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finel_tickers2names_fe_en_1.0.0_3.0_1718189884813.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finel_tickers2names_fe_en_1.0.0_3.0_1718189884813.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

resolver = finance.SentenceEntityResolverModel.pretrained("finel_tickers2names_fe", "en", "finance/models") \
      .setInputCols(["ner_chunk", "sentence_embeddings"]) \
      .setOutputCol("name")\
      .setDistanceFunction("EUCLIDEAN")

pipelineModel = nlp.Pipeline(
      stages = [
          documentAssembler,
          embeddings,
          resolver])

lp = LightPipeline(pipelineModel)

lp.fullAnnotate("HP")
```

</div>

## Results

```bash
['HP Inc. Common Stock']
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finel_tickers2names_fe|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[normalized]|
|Language:|en|
|Size:|115.7 MB|
|Case sensitive:|false|

## References

https://data.world/johnsnowlabs/list-of-companies-in-nasdaq-exchanges