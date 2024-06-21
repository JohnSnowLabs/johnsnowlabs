---
layout: model
title: Financial NER on EDGAR Documents
author: John Snow Labs
name: finner_sec_edgar_fe
date: 2024-05-17
tags: [en, licensed, finance, ner, sec]
task: Named Entity Recognition
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
annotator: LegalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Financial NER model extracts ORG, INST, LAW, COURT, PER, LOC, MISC, ALIAS, and TICKER entities from the US SEC EDGAR documents, was trained using custom finance word embeddings.

## Predicted Entities

`ORG`, `INST`, `LAW`, `COURT`, `PER`, `LOC`, `MISC`, `ALIAS`, `TICKER`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finner_sec_edgar_fe_en_1.0.0_3.0_1715948751469.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finner_sec_edgar_fe_en_1.0.0_3.0_1715948751469.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")
        
sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
      .setInputCols(["document"])\
      .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
      .setInputCols(["sentence"])\
      .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("finance_word_embeddings", "en", "finance/models")\
            .setInputCols(["sentence","token"])\
            .setOutputCol("embeddings")

ner_model = finance.NerModel.pretrained("finner_sec_edgar_fe", "en", "finance/models")\
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

text = ["""In our opinion, the accompanying consolidated balance sheets and the related consolidated statements of operations, of changes in stockholders' equity, and of cash flows present fairly, in all material respects, the financial position of SunGard Capital Corp. II and its subsidiaries ( SCC II ) at December 31, 2010, and 2009, and the results of their operations and their cash flows for each of the three years in the period ended December 31, 2010, in conformity with accounting principles generally accepted in the United States of America."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+----------------------------------------+-----+
|chunk                                   |label|
+----------------------------------------+-----+
|SunGard Capital Corp                    |ORG  |
|SCC II                                  |ALIAS|
|accounting principles generally accepted|LAW  |
|United States of America                |LOC  |
+----------------------------------------+-----+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finner_sec_edgar_fe|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|2.2 MB|

## References

In-house annotations

## Benchmarking

```bash
          precision    recall  f1-score   support
ALIAS         0.91      0.80      0.85        84
COURT         1.00      1.00      1.00         6
INST          0.92      0.76      0.83        76
LAW           0.89      0.86      0.87       166
LOC           0.87      0.87      0.87       140
MISC          0.86      0.75      0.80       226
ORG           0.88      0.91      0.89       430
PER           0.89      0.88      0.89        66
TICKER        1.00      0.86      0.92         7
micro-avg     0.88      0.85      0.87      1201
macro-avg     0.91      0.85      0.88      1201
weighted-avg  0.88      0.85      0.86      1201
```