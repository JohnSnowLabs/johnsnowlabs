---
layout: model
title: Legal NER on Subpoenas (Small)
author: John Snow Labs
name: legner_subpoenas_sm
date: 2024-06-28
tags: [legal, subpoenas, licensed, en]
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

This is a Legal NER model which is trained using custom legal embeddings and is aimed to extract 19 entities from subpoenas. This is called a small version because it has been trained on more generic labels. The larger versions of this model will be available on models hub.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_subpoenas_sm_en_1.0.0_3.0_1719594943623.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_subpoenas_sm_en_1.0.0_3.0_1719594943623.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = nlp.DocumentAssembler()\
        .setInputCol("text")\
        .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
        .setInputCols(["document"])\
        .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
        .setInputCols(["sentence"])\
        .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("legal_word_embeddings", "en", "legal/models")\
            .setInputCols(["sentence","token"])\
            .setOutputCol("embeddings")

ner_model = legal.NerModel.pretrained("legner_bert_subpoenas_sm_le", "en", "legal/models")\
        .setInputCols(["sentence", "token", "embeddings"])\
        .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
        .setInputCols(["sentence","token","ner"])\
        .setOutputCol("ner_chunk")

nlpPipeline = nlp.Pipeline(stages=[
        documentAssembler,
        sentenceDetector,
        tokenizer,
        embeddings,
        ner_model,
        ner_converter])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)
```

</div>

## Results

```bash
+-------------------+-------------+
|chunk              |label        |
+-------------------+-------------+
|summary disposition|DOCUMENT_TYPE|
+-------------------+-------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_subpoenas_sm|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.7 MB|

## References

In House annotated dataset

## Benchmarking

```bash
                    precision    recall  f1-score   support
           ADDRESS       0.82      0.88      0.85        42
  APPOINTMENT_DATE       0.50      1.00      0.67         3
  APPOINTMENT_HOUR       1.00      1.00      1.00         2
              CASE       0.74      0.89      0.81        19
            COUNTY       0.33      0.50      0.40         2
             COURT       0.44      0.40      0.42        10
     DEADLINE_DATE       0.50      1.00      0.67         2
DOCUMENT_DATE_FROM       0.67      0.86      0.75         7
  DOCUMENT_DATE_TO       0.71      0.83      0.77         6
DOCUMENT_DATE_YEAR       0.50      0.50      0.50         4
   DOCUMENT_PERSON       0.82      0.79      0.81      1307
    DOCUMENT_TOPIC       0.63      0.62      0.62        94
     DOCUMENT_TYPE       0.87      0.89      0.88       783
            MATTER       0.92      0.86      0.89        94
         MATTER_VS       0.93      0.78      0.85        54
          RECEIVER       0.50      0.30      0.37        20
            SIGNER       0.62      0.65      0.63        20
             STATE       0.60      0.86      0.71        14
     SUBPOENA_DATE       0.24      0.57      0.33         7
         micro-avg       0.82      0.81      0.82      2490
         macro-avg       0.65      0.75      0.68      2490
      weighted-avg       0.82      0.81      0.82      2490
```