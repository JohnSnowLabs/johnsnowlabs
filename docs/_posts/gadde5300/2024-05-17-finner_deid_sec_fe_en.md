---
layout: model
title: Generic Deidentification NER (Finance)
author: John Snow Labs
name: finner_deid_sec_fe
date: 2024-05-17
tags: [deid, deidentification, anonymization, en, licensed]
task: Named Entity Recognition
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
recommended: true
annotator: FinanceNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a NER model trained using custom finance embeddings which allows you to detect some generic entities that may require to be masked or obfuscated to be compliant with different regulations, as GDPR and CCPA. This is just an NER model, make sure you try the full De-identification pipelines available in Models Hub.

## Predicted Entities

`AGE`, `CITY`, `COUNTRY`, `DATE`, `EMAIL`, `LOCATION-OTHER`, `FAX`, `ORG`, `PERSON`, `PHONE`, `PROFESSION`, `STATE`, `STREET`, `URL`, `ZIP`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finner_deid_sec_fe_en_1.0.0_3.0_1715953927003.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finner_deid_sec_fe_en_1.0.0_3.0_1715953927003.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = nlp.WordEmbeddingsModel.pretrained("finance_word_embeddings", "en", "finance/models")\
            .setInputCols(["sentence","token"])\
            .setOutputCol("embeddings")

ner_model =finance.NerModel.pretrained("finner_deid_sec_fe", "en", "finance/models")\
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

text = [""" This LICENSE AND DEVELOPMENT AGREEMENT (this Agreement) is entered into effective as of Nov. 02, 2019 (the Effective Date) by and between Bioeq IP AG, having its principal place of business at 333 Twin Dolphin Drive, Suite 600, Redwood City, CA, 94065, USA (Licensee). """]

res = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+----------------------+------+
|chunk                 |label |
+----------------------+------+
|Nov. 02, 2019         |DATE  |
|333 Twin Dolphin Drive|STREET|
|Redwood City          |CITY  |
|CA                    |STATE |
|94065                 |ZIP   |
+----------------------+------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finner_deid_sec_fe|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.6 MB|

## References

In-house annotated documents with protected information

## Benchmarking

```bash
                precision    recall  f1-score   support
           AGE       0.97      0.95      0.96       266
          CITY       0.86      0.80      0.83       120
       COUNTRY       0.86      0.63      0.73        38
          DATE       0.98      0.98      0.98      2206
         EMAIL       1.00      1.00      1.00         1
           FAX       0.00      0.00      0.00         2
LOCATION-OTHER       1.00      0.33      0.50         6
           ORG       0.82      0.55      0.66        42
        PERSON       0.95      0.95      0.95      1295
         PHONE       0.89      0.89      0.89        62
    PROFESSION       0.75      0.55      0.64        76
         STATE       0.90      0.92      0.91        90
        STREET       0.92      0.89      0.91        81
           URL       0.00      0.00      0.00         1
           ZIP       0.97      0.94      0.95        67
     micro-avg       0.96      0.94      0.95      4353
     macro-avg       0.79      0.69      0.73      4353
  weighted-avg       0.96      0.94      0.95      4353
```
