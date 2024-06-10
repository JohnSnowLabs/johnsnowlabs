---
layout: model
title: Detect Assertion Status for Radiology
author: John Snow Labs
name: assertion_dl_radiology
date: 2024-06-10
tags: [assertion, radiology, clinical, en, licensed]
task: Assertion Status
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.0
supported: true
annotator: AssertionDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Assign assertion status to clinical entities extracted by Radiology NER based on their context in the text.

## Predicted Entities

`Confirmed`, `Suspected`, `Negative`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_dl_radiology_en_5.3.3_3.0_1718021696198.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_dl_radiology_en_5.3.3_3.0_1718021696198.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

Extract radiology entities using the radiology NER model in the pipeline and assign assertion status for them with assertion_dl_radiology pretrained model. Note: Example for demo purpose taken from: https://www.mtsamples.com/site/pages/sample.asp?Type=95-Radiology&Sample=1391-Chest%20PA%20&%20Lateral

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

radiology_ner = MedicalNerModel.pretrained("ner_radiology", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")\
    .setWhiteList(["ImagingFindings"])

radiology_assertion = AssertionDLModel.pretrained("assertion_dl_radiology", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")

nlpPipeline = Pipeline(stages=[documentAssembler, sentenceDetector, tokenizer, word_embeddings, radiology_ner, ner_converter, radiology_assertion])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = LightPipeline(nlpPipeline.fit(empty_data))

text = """
INTERPRETATION: There has been interval development of a moderate left-sided pneumothorax with near complete collapse of the left upper lobe. The lower lobe appears aerated. There is stable, diffuse, bilateral interstitial thickening with no definite acute air space consolidation. The heart and pulmonary vascularity are within normal limits. Left-sided port is seen with Groshong tip at the SVC/RA junction. No evidence for acute fracture, malalignment, or dislocation."""

result = model.fullAnnotate(text)
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val radiology_ner = MedicalNerModel.pretrained("ner_radiology", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = NerConverter() 
    .setInputCols(Array("sentence", "token", "ner")) 
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("ImagingFindings"))

val radiology_assertion = AssertionDLModel.pretrained("assertion_dl_radiology", "en", "clinical/models")
    .setInputCols(Array("sentence", "ner_chunk", "embeddings"))
    .setOutputCol("assertion")

val nlpPipeline = new Pipeline().setStages(Array(documentAssembler,  sentenceDetector, tokenizer, word_embeddings, radiology_ner, ner_converter, radiology_assertion))

text = """
INTERPRETATION: There has been interval development of a moderate left-sided pneumothorax with near complete collapse of the left upper lobe. The lower lobe appears aerated. There is stable, diffuse, bilateral interstitial thickening with no definite acute air space consolidation. The heart and pulmonary vascularity are within normal limits. Left-sided port is seen with Groshong tip at the SVC/RA junction. No evidence for acute fracture, malalignment, or dislocation."""

val data = Seq("text").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
 |    |                ner_chunk | begin | end |       ner_label | assertion | assertion confidence |
 |---:|:-------------------------|:------|:----|:----------------|:----------|:---------------------|
 | 0  |               left-sided |    66 |  75 |       Direction | Confirmed |               0.9964 |
 | 1  |             pneumothorax |    77 |  88 | ImagingFindings | Confirmed |               0.9963 |
 | 2  |        complete collapse |   100 | 116 | ImagingFindings | Confirmed |               0.9977 |
 | 3  |               left upper |   125 | 134 |       Direction | Confirmed |               0.9962 |
 | 4  |                     lobe |   136 | 139 |        BodyPart | Confirmed |               0.9913 |
 | 5  |                    lower |   146 | 150 |       Direction | Confirmed |               0.7678 |
 | 6  |                     lobe |   152 | 155 |        BodyPart | Confirmed |               0.8673 |
 | 7  |                  aerated |   165 | 171 | ImagingFindings | Confirmed |               0.5755 |
 | 8  |                bilateral |   200 | 208 |       Direction | Confirmed |               0.9966 |
 | 9  |             interstitial |   210 | 221 |        BodyPart | Confirmed |               0.9944 |
 | 10 |               thickening |   223 | 232 | ImagingFindings | Confirmed |               0.9954 |
 | 11 |  air space consolidation |   257 | 279 | ImagingFindings |  Negative |               0.9434 |
 | 12 |                    heart |   286 | 290 |        BodyPart | Confirmed |               0.9941 |
 | 13 |    pulmonary vascularity |   296 | 316 |        BodyPart | Confirmed |               0.9986 |
 | 14 |     within normal limits |   322 | 341 | ImagingFindings | Confirmed |               0.9999 |
 | 15 |               Left-sided |   344 | 353 |       Direction | Confirmed |               0.9782 |
 | 16 |                     port |   355 | 358 |  Medical_Device | Confirmed |               0.9838 |
 | 17 |          SVC/RA junction |   393 | 407 |        BodyPart | Confirmed |               0.9998 |
 | 18 |           acute fracture |   426 | 439 | ImagingFindings |  Negative |               0.9995 |
 | 19 |             malalignment |   442 | 453 | ImagingFindings |  Negative |               0.9964 |
 | 20 |              dislocation |   459 | 469 | ImagingFindings |  Negative |               0.9864 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_dl_radiology|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, ner_chunk, embeddings]|
|Output Labels:|[assertion_pred]|
|Language:|en|
|Size:|2.5 MB|

## References

Custom internal labeled radiology dataset.

## Benchmarking

```bash
       label  precision    recall  f1-score   support
   Confirmed       0.95      0.92      0.94      3511
    Negative       0.95      0.95      0.95       615
   Suspected       0.79      0.87      0.82      1106
    accuracy       -         -         0.91      5232
   macro-avg       0.90      0.91      0.90      5232
weighted-avg       0.92      0.91      0.92      5232
```
