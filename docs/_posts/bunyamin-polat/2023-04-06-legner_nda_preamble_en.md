---
layout: model
title: Legal NER for NDA (Preamble Clause)
author: John Snow Labs
name: legner_nda_preamble
date: 2023-04-06
tags: [en, licensed, legal, ner, nda, preamble, purpose]
task: Named Entity Recognition
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
annotator: LegalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a NER model, aimed to be run **only** after detecting the `PREAMBLE` clause with a proper classifier (use legmulticlf_mnda_sections_paragraph_other for that purpose). It will extract the following entities: `PURPOSE`, and `PURPOSE_OBJECT`.

## Predicted Entities

`PURPOSE`, `PURPOSE_OBJECT`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_nda_preamble_en_1.0.0_3.0_1680791988031.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_nda_preamble_en_1.0.0_3.0_1680791988031.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
        .setInputCol("text")\
        .setOutputCol("document")
        
sentence_detector = nlp.SentenceDetector()\
        .setInputCols(["document"])\
        .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
        .setInputCols(["sentence"])\
        .setOutputCol("token")

embeddings = nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en") \
        .setInputCols(["sentence", "token"]) \
        .setOutputCol("embeddings")\
        .setMaxSentenceLength(512)\
        .setCaseSensitive(True)

ner_model = legal.NerModel.pretrained("legner_nda_preamble", "en", "legal/models")\
        .setInputCols(["sentence", "token", "embeddings"])\
        .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
        .setInputCols(["sentence", "token", "ner"])\
        .setOutputCol("ner_chunk")

nlpPipeline = nlp.Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        embeddings,
        ner_model,
        ner_converter])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

text = ["""In order to facilitate the consideration and negotiation of a possible transaction involving Chordiant and Pegasystems ( referred to collectively as the "Parties" and individually as a "Party"), each Party has requested access to certain non-public information regarding the other Party and the other Party’s subsidiaries."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+-------------+--------------+
|chunk        |ner_label     |
+-------------+--------------+
|consideration|PURPOSE       |
|negotiation  |PURPOSE       |
|transaction  |PURPOSE_OBJECT|
+-------------+--------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_nda_preamble|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|16.3 MB|

## References

In-house annotations on the Non-disclosure Agreements

## Benchmarking

```bash
label             precision  recall  f1-score  support 
B-PURPOSE         1.00       0.93    0.97      15      
B-PURPOSE_OBJECT  0.90       0.82    0.86      11      
I-PURPOSE_OBJECT  1.00       0.80    0.89      5       
micro-avg         0.96       0.87    0.92      31      
macro-avg         0.97       0.85    0.90      31      
weighted-avg      0.96       0.87    0.91      31  
```