---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_deid_generic_nonMedical_medium)
author: John Snow Labs
name: zeroshot_ner_deid_generic_nonMedical_medium
date: 2025-12-28
tags: [licensed, en, ner, deid, zeroshot, clinical, generic]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.2.2
spark_version: 3.4
supported: true
engine: onnx
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_generic_nonMedical_medium_en_6.2.2_3.4_1766880864914.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_generic_nonMedical_medium_en_6.2.2_3.4_1766880864914.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

labels = ["NAME", "AGE", "DATE", "LOCATION", "ID", "CONTACT", "PROFESSION"]

pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_generic_nonMedical_medium", "en", "clinical/models")\
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

data = spark.createDataFrame([["""Mr. James Wilson is a 65-year-old male who presented to the emergency department at Boston General Hospital on 10/25/2023. 
He lives at 123 Oak Street, Springfield, IL 62704. He can be contacted at 555-0199. His SocialSecurityNumber is 999-001-1234. Dr. Gregory House is the attending physician."""]]).toDF("text")

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

labels = ["NAME", "AGE", "DATE", "LOCATION", "ID", "CONTACT", "PROFESSION"]

pretrained_zero_shot_ner = medical.PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_generic_nonMedical_medium", "en", "clinical/models")\
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

data = spark.createDataFrame([["""Mr. James Wilson is a 65-year-old male who presented to the emergency department at Boston General Hospital on 10/25/2023. 
He lives at 123 Oak Street, Springfield, IL 62704. He can be contacted at 555-0199. His SocialSecurityNumber is 999-001-1234. Dr. Gregory House is the attending physician."""]]).toDF("text")

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

val labels = Array("NAME", "AGE", "DATE", "LOCATION", "ID", "CONTACT", "PROFESSION")

val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_generic_nonMedical_medium", "en", "clinical/models")
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

val data = Seq("""Mr. James Wilson is a 65-year-old male who presented to the emergency department at Boston General Hospital on 10/25/2023. 
He lives at 123 Oak Street, Springfield, IL 62704. He can be contacted at 555-0199. His SocialSecurityNumber is 999-001-1234. Dr. Gregory House is the attending physician.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-----------------------+-----+---+---------+----------+
|chunk                  |begin|end|ner_label|confidence|
+-----------------------+-----+---+---------+----------+
|James Wilson           |4    |15 |NAME     |0.9993062 |
|65-year-old            |22   |32 |AGE      |0.9988632 |
|Boston General Hospital|84   |106|LOCATION |0.9958438 |
|10/25/2023             |111  |120|DATE     |0.9923149 |
|123 Oak Street         |136  |149|LOCATION |0.9757991 |
|Springfield            |152  |162|LOCATION |0.9798024 |
|IL                     |165  |166|LOCATION |0.9987602 |
|62704                  |168  |172|LOCATION |0.9594395 |
|555-0199               |198  |205|CONTACT  |0.9907244 |
|999-001-1234           |236  |247|ID       |0.9978492 |
|Gregory House          |254  |266|NAME     |0.9979722 |
+-----------------------+-----+---+---------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_deid_generic_nonMedical_medium|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|789.8 MB|
