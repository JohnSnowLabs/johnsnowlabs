---
layout: model
title: Generic Deidentification NER (Legal)
author: John Snow Labs
name: legner_deid_le
date: 2024-05-21
tags: [en, legal, ner, deid, deidentification, licensed]
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

This is a Legal NER model trained using custom legal embeddings which allows you to detect some generic entities that may require to be masked or obfuscated to be compliant with different regulations, as GDPR and CCPA. This is just an NER model, make sure you try the full De-identification pipelines available in Models Hub.

## Predicted Entities

`AGE`, `CITY`, `COUNTRY`, `DATE`, `EMAIL`, `FAX`, `LOCATION-OTHER`, `ORG`, `PERSON`, `PHONE`, `PROFESSION`, `STATE`, `STREET`, `URL`, `ZIP`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_deid_le_en_1.0.0_3.0_1716291298762.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_deid_le_en_1.0.0_3.0_1716291298762.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model =legal.NerModel.pretrained("legner_deid_le", "en", "legal/models")\
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
+----------------------+------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_deid_le|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.8 MB|

## References

In-house annotated documents with protected information

## Benchmarking

```bash
                 precision    recall  f1-score   support
AGE                  0.97      0.97      0.97       266
CITY                 0.85      0.76      0.80       120
COUNTRY              0.89      0.63      0.74        38
DATE                 0.98      0.98      0.98      2206
EMAIL                1.00      1.00      1.00         1
FAX                  0.00      0.00      0.00         2
LOCATION-OTHER       1.00      0.50      0.67         6
ORG                  0.69      0.48      0.56        42
PERSON               0.96      0.96      0.96      1295
PHONE                0.84      0.85      0.85        62
PROFESSION           0.80      0.54      0.65        76
STATE                0.94      0.93      0.94        90
STREET               0.95      0.90      0.92        81
URL                  0.00      0.00      0.00         1
ZIP                  0.97      0.96      0.96        67
micro-avg            0.96      0.95      0.95      4353
macro-avg            0.79      0.70      0.73      4353
weighted-avg         0.96      0.95      0.95      4353

```