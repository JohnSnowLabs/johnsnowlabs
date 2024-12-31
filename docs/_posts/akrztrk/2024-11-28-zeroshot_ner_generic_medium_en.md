---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_generic_medium)
author: John Snow Labs
name: zeroshot_ner_generic_medium
date: 2024-11-28
tags: [licensed, en, ner, oncology, zeroshot, clinical, generic]
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

Zero-shot Named Entity Recognition (NER) enables the identification of entities in text with minimal effort. By leveraging pre-trained language models and contextual understanding, zero-shot NER extends entity recognition capabilities to new domains and languages. While the model card includes default labels as examples, it is important to highlight that users are not limited to these labels. 

**The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. For best results, it is recommended to use labels that are conceptually similar to the provided defaults.**

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_generic_medium_en_5.5.1_3.0_1732833761762.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_generic_medium_en_5.5.1_3.0_1732833761762.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

labels = ['AGE','DATE','DISEASE','DISORDER','DRUG','LOCATION','NAME','PHONE','RESULT','SYMPTOM','SYNDROME','TEST','TREATMENT']

pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_generic_medium", "en", "clinical/models")\
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

data = spark.createDataFrame([["""Record date: 2093-01-13, Age: 25, # 719435. Dr. John Green,  Phone (302) 786-5227, 0295 Keats Street, San Francisco.
Jennifer Smith is 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), 
one prior episode of HTG-induced pancreatitis three years prior to presentation, and associated with an acute hepatitis, presented with a one-week history of polyuria, poor appetite, and vomiting."""]]).toDF("text")

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

labels = ['AGE','DATE','DISEASE','DISORDER','DRUG','LOCATION','NAME','PHONE','RESULT','SYMPTOM','SYNDROME','TEST','TREATMENT']

pretrained_zero_shot_ner = medical.PretrainedZeroShotNER().pretrained("zeroshot_ner_generic_medium", "en", "clinical/models")\
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

data = spark.createDataFrame([["""Record date: 2093-01-13, Age: 25, # 719435. Dr. John Green,  Phone (302) 786-5227, 0295 Keats Street, San Francisco.
Jennifer Smith is 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), 
one prior episode of HTG-induced pancreatitis three years prior to presentation, and associated with an acute hepatitis, presented with a one-week history of polyuria, poor appetite, and vomiting."""]]).toDF("text")

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

val labels = Array('AGE','DATE','DISEASE','DISORDER','DRUG','LOCATION','NAME','PHONE','RESULT','SYMPTOM','SYNDROME','TEST','TREATMENT')

val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_generic_medium", "en", "clinical/models")
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

val data = Seq("""Record date: 2093-01-13, Age: 25, # 719435. Dr. John Green,  Phone (302) 786-5227, 0295 Keats Street, San Francisco.
Jennifer Smith is 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), 
one prior episode of HTG-induced pancreatitis three years prior to presentation, and associated with an acute hepatitis, presented with a one-week history of polyuria, poor appetite, and vomiting.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-----------------------------+-----+---+---------+----------+
|chunk                        |begin|end|ner_label|confidence|
+-----------------------------+-----+---+---------+----------+
|2093-01-13                   |14   |23 |DATE     |0.7226501 |
|25                           |31   |32 |AGE      |0.73603666|
|Dr. John Green               |45   |58 |NAME     |0.85545534|
|Phone (302) 786-5227         |62   |81 |PHONE    |0.57981455|
|0295 Keats Street            |84   |100|LOCATION |0.8096688 |
|San Francisco                |103  |115|LOCATION |0.93522215|
|Jennifer Smith               |118  |131|NAME     |0.8787616 |
|28-year-old                  |136  |146|AGE      |0.5765038 |
|gestational diabetes mellitus|173  |201|DISEASE  |0.55128574|
|HTG-induced pancreatitis     |319  |342|DISEASE  |0.5173685 |
|acute hepatitis              |402  |416|DISEASE  |0.50674236|
|polyuria                     |456  |463|SYMPTOM  |0.80963147|
|poor appetite                |466  |478|SYMPTOM  |0.84152484|
|vomiting                     |485  |492|SYMPTOM  |0.86616516|
+-----------------------------+-----+---+---------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_generic_medium|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|710.4 MB|