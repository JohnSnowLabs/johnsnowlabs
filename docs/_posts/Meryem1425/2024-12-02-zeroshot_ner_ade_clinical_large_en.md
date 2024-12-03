---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_ade_clinical_large)
author: John Snow Labs
name: zeroshot_ner_ade_clinical_large
date: 2024-12-02
tags: [licensed, en, ner, ade, zeroshot, clinical]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.5.1
spark_version: 3.0
supported: true
annotator: PretrainedZeroShotNER
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Zero-shot Named Entity Recognition (NER) enables the identification of entities in text with minimal effort. By leveraging pre-trained language models and contextual understanding, zero-shot NER extends entity recognition capabilities to new domains and languages.
While the model card includes default labels as examples, it is important to highlight that users are not limited to these labels. The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. For best results, it is recommended to use labels that are conceptually similar to the provided defaults.

## Predicted Entities
`DRUG`, `ADE`,`PROBLEM`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_ade_clinical_large_en_5.5.1_3.0_1733148964132.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_ade_clinical_large_en_5.5.1_3.0_1733148964132.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

labels = ['DRUG', 'ADE','PROBLEM'] # You can change the entities
pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_ade_clinical_large", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("ner")\
    .setPredictionThreshold(0.5)\
    .setLabels(labels)

ner_converter = NerConverterInternal()\
    .setInputCols("sentence", "token", "ner")\
    .setOutputCol("ner_chunk")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
])

data = spark.createDataFrame([["""To alleviate severe seasonal allergies that included symptoms such as sneezing, watery eyes, and nasal congestion, the doctor recommended a combination of antihistamines and nasal corticosteroids, which collectively provided the patient with substantial symptomatic relief and improved quality of life. However, the patient reported experiencing side effects such as drowsiness from the antihistamines and occasional nosebleeds due to the nasal corticosteroids."""]]).toDF("text")

result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
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

labels = ['DRUG', 'ADE','PROBLEM']
pretrained_zero_shot_ner = medical.PretrainedZeroShotNER().pretrained("zeroshot_ner_ade_clinical_large", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("ner")\
    .setPredictionThreshold(0.5)\
    .setLabels(labels)

ner_converter = medical.NerConverterInternal()\
    .setInputCols("sentence", "token", "ner")\
    .setOutputCol("ner_chunk")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
])

data = spark.createDataFrame([["""To alleviate severe seasonal allergies that included symptoms such as sneezing, watery eyes, and nasal congestion, the doctor recommended a combination of antihistamines and nasal corticosteroids, which collectively provided the patient with substantial symptomatic relief and improved quality of life. However, the patient reported experiencing side effects such as drowsiness from the antihistamines and occasional nosebleeds due to the nasal corticosteroids."""]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

labels = Array("DRUG", "ADE","PROBLEM") // You can change the entities
val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_ade_clinical_large", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("ner")
    .setPredictionThreshold(0.5)
    .setLabels(labels)

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
))

val data = Seq(("""To alleviate severe seasonal allergies that included symptoms such as sneezing, watery eyes, and nasal congestion, the doctor recommended a combination of antihistamines and nasal corticosteroids, which collectively provided the patient with substantial symptomatic relief and improved quality of life. However, the patient reported experiencing side effects such as drowsiness from the antihistamines and occasional nosebleeds due to the nasal corticosteroids.""")).toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+----------------------+-----+---+---------+----------+
|chunk                 |begin|end|ner_label|confidence|
+----------------------+-----+---+---------+----------+
|seasonal allergies    |21   |38 |PROBLEM  |0.7983188 |
|symptoms              |54   |61 |PROBLEM  |0.72892165|
|sneezing              |71   |78 |PROBLEM  |0.99215865|
|watery eyes           |81   |91 |PROBLEM  |0.98562455|
|nasal congestion      |98   |113|PROBLEM  |0.9831299 |
|antihistamines        |156  |169|DRUG     |0.99360174|
|nasal corticosteroids |175  |195|DRUG     |0.81538504|
|side effects          |347  |358|PROBLEM  |0.77464384|
|drowsiness            |368  |377|ADE      |0.99594826|
|antihistamines        |388  |401|DRUG     |0.9916972 |
|nosebleeds            |418  |427|ADE      |0.98120177|
|nasal corticosteroids.|440  |461|DRUG     |0.52606887|
+----------------------+-----+---+---------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_ade_clinical_large|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|



## Benchmarking

```bash
       label  precision    recall  f1-score   support
       B-ADE      0.817     0.717     0.764      3551
      B-DRUG      0.878     0.894     0.886      7551
   B-PROBLEM      0.868     0.787     0.826     18238
       I-ADE      0.818     0.648     0.723      4296
      I-DRUG      0.883     0.757     0.815     10488
   I-PROBLEM      0.862     0.636     0.732     15925
    accuracy        -         -       0.942    347624
   macro-avg      0.869     0.775     0.816    347624
weighted-avg      0.940     0.942     0.940    347624
```
