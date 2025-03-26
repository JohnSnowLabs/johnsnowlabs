---
layout: model
title: Financial Assertion of Aspect-Based Sentiment (md, Medium)
author: John Snow Labs
name: finassertion_aspect_based_sentiment_md_fe
date: 2024-06-21
tags: [assertion, licensed, en, finance]
task: Assertion Status
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
recommended: true
annotator: AssertionDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This assertion model classifies financial entities into an aspect-based sentiment. It is designed to be used together with the associated NER model.

## Predicted Entities

`POSITIVE`, `NEGITIVE`, `NEUTRAL`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finassertion_aspect_based_sentiment_md_fe_en_1.0.0_3.0_1718963493988.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finassertion_aspect_based_sentiment_md_fe_en_1.0.0_3.0_1718963493988.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

# Sentence Detector annotator, processes various sentences per line
sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

# Tokenizer splits words in a relevant format for NLP
tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("finance_word_embeddings", "en", "finance/models")\
            .setInputCols(["sentence","token"])\
            .setOutputCol("embeddings")

ner_model =finance.NerModel.pretrained("finner_aspect_based_sentiment_fe", "en", "finance/models")\
      .setInputCols(["sentence", "token", "embeddings"])\
      .setOutputCol("ner")

ner_converter = finance.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

assertion_model = finance.AssertionDLModel.pretrained("finassertion_aspect_based_sentiment_md", "en", "finance/models")\
    .setInputCols(["sentence", "ner_chunk", "embeddings"])\
    .setOutputCol("assertion")


nlpPipeline = nlp.Pipeline(
    stages=[documentAssembler,
            sentenceDetector,
            tokenizer,
            embeddings,
            ner_model,
            ner_converter,
            assertion_model])


empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

text = "Equity and earnings of affiliates in Latin America increased to $4.8 million in the quarter from $2.2 million in the prior year as the commodity markets in Latin America remain strong through the end of the quarter."

light_model = nlp.LightPipeline(model)

light_result = light_model.fullAnnotate(text)[0]

print(text)

chunks=[]
entities=[]
status=[]
confidence=[]

for n,m in zip(light_result['ner_chunk'],light_result['assertion']):

    chunks.append(n.result)
    entities.append(n.metadata['entity'])
    status.append(m.result)
    confidence.append(m.metadata['confidence'])

df = pd.DataFrame({'chunks':chunks, 'entities':entities, 'assertion':status, 'confidence':confidence})
```

</div>

## Results

```bash
| chunks   | entities  | assertion | confidence |
|----------|-----------|-----------|------------|
| 0        | Equity    | GAINS     | POSITIVE   | 0.9463     |
| 1        | earnings  | PROFIT    | POSITIVE   | 0.9144     |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finassertion_aspect_based_sentiment_md_fe|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, chunk, embeddings]|
|Output Labels:|[assertion]|
|Language:|en|
|Size:|1.2 MB|