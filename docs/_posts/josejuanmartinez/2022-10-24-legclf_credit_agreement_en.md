---
layout: model
title: Legal Credit agreement Document Classifier (Longformer)
author: John Snow Labs
name: legclf_credit_agreement
date: 2022-10-24
tags: [en, legal, classification, document, agreement, contract, licensed]
task: Text Classification
language: en
nav_key: models
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
annotator: LegalClassifierDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The `legclf_credit_agreement` model is a Legal Longformer Document Classifier to classify if the document belongs to the class credit-agreement or not (Binary Classification).

Longformers have a restriction on 4096 tokens, so only the first 4096 tokens will be taken into account. We have realised that for the big majority of the documents in legal corpora, if they are clean and only contain the legal document without any extra information before, 4096 is enough to perform Document Classification.

If not, let us know and we can carry out another approach for you: getting chunks of 4096 tokens and average the embeddings, training with the averaged version, what means all document will be taken into account. But this theoretically should not be required.

## Predicted Entities

`other`, `credit-agreement`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/legal/CLASSIFY_LEGAL_DOCUMENTS/){:.button.button-orange}
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_credit_agreement_en_1.0.0_3.0_1666620886293.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_credit_agreement_en_1.0.0_3.0_1666620886293.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = nlp.DocumentAssembler() \
     .setInputCol("text") \
     .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
     .setInputCols(["document"])\
     .setOutputCol("token")

embeddings = nlp.LongformerEmbeddings.pretrained("legal_longformer_base", "en")\
    .setInputCols("document", "token") \
    .setOutputCol("embeddings")

sembeddings = nlp.SentenceEmbeddings()\
    .setInputCols(["document", "embeddings"]) \
    .setOutputCol("sentence_embeddings") \
    .setPoolingStrategy("AVERAGE")

docClassifier = nlp.ClassifierDLModel.pretrained("legclf_credit_agreement", "en", "legal/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("category")
    
nlpPipeline = nlp.Pipeline(stages=[
    documentAssembler, 
    tokenizer,
    embeddings,
    sembeddings,
    docClassifier])
 
df = spark.createDataFrame([["YOUR TEXT HERE"]]).toDF("text")
model = nlpPipeline.fit(df)
result = model.transform(df)
```

</div>

## Results

```bash
+-------+
| result|
+-------+
|[credit-agreement]|
|[other]|
|[other]|
|[credit-agreement]|

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legclf_credit_agreement|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|en|
|Size:|21.5 MB|

## References

Legal documents, scrapped from the Internet, and classified in-house + SEC documents 

## Benchmarking

```bash
           label   precision    recall  f1-score   support
credit-agreement       0.94      0.94      0.94        36
           other       0.97      0.97      0.97        62
        accuracy          -         -      0.96        98
       macro-avg       0.96      0.96      0.96        98
    weighted-avg       0.96      0.96      0.96        98
```