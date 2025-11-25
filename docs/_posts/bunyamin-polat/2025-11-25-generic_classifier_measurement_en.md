---
layout: model
title: Generic Classifier for Measurement
author: John Snow Labs
name: generic_classifier_measurement
date: 2025-11-25
tags: [en, classification, measurement, licensed]
task: Text Classification
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.0
supported: true
annotator: GenericClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a binary classification model that determines whether clinical sentences
include quantitative measurement terms and values.

Classes:
- `MEASUREMENT`: Contains numerical health measurements, vital signs, lab results, or test values
- `OTHER`: Doesn't contain quantitative measurement information

## Predicted Entities

`MEASUREMENT`, `OTHER`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/generic_classifier_measurement_en_6.2.0_3.0_1764094101445.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/generic_classifier_measurement_en_6.2.0_3.0_1764094101445.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols("document")\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("word_embeddings")

sentence_embeddings = SentenceEmbeddings()\
    .setInputCols(["document", "word_embeddings"])\
    .setOutputCol("sentence_embeddings")\
    .setPoolingStrategy("AVERAGE")

features_asm = FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

generic_classifier = GenericClassifierModel.pretrained("generic_classifier_measurement", "en", "clinical/models")\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

clf_pipeline = Pipeline(
  stages=[
    document_assembler,
    tokenizer,
    word_embeddings,
    sentence_embeddings,
    features_asm,
    generic_classifier])

sample_texts = [
    ["This is a 58-year-old male who started out having a toothache in the left lower side of the mouth that is now radiating into his jaw and towards his left ear. Triage nurse reported that he does not believe it is his tooth because he has regular dental appointments, but has not seen a dentist since this new toothache began. The patient denies any facial swelling."],
    ["The database was available at this point of time. WBC count is elevated at 19,000 with the left shift, hemoglobin of 17.7, and hematocrit of 55.8 consistent with severe dehydration."],
    ["Temperature max is 99, heart rate was 133 to 177, blood pressure is 114/43 (while moving), respiratory rate was 28 to 56 with O2 saturations 97 to 100% on room air. Weight was 4.1 kg."],
    ["I will see her back in followup in 3 months, at which time she will be recovering from a shoulder surgery and we will see if she needs any further intervention with regard to the cervical spine.I will also be in touch with Dr. Y to let him know this information prior to the surgery in several weeks."]
]

data = spark.createDataFrame(sample_texts).toDF("text")

result = clf_pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols("document")\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("word_embeddings")

sentence_embeddings = nlp.SentenceEmbeddings()\
    .setInputCols(["document", "word_embeddings"])\
    .setOutputCol("sentence_embeddings")\
    .setPoolingStrategy("AVERAGE")

features_asm = medical.FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

generic_classifier = medical.GenericClassifierModel.pretrained("generic_classifier_measurement", "en", "clinical/models")\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

clf_Pipeline = nlp.Pipeline(
  stages=[
    document_assembler,
    tokenizer,
    word_embeddings,
    sentence_embeddings,
    features_asm,
    generic_classifier])

sample_texts = [
    ["This is a 58-year-old male who started out having a toothache in the left lower side of the mouth that is now radiating into his jaw and towards his left ear. Triage nurse reported that he does not believe it is his tooth because he has regular dental appointments, but has not seen a dentist since this new toothache began. The patient denies any facial swelling."],
    ["The database was available at this point of time. WBC count is elevated at 19,000 with the left shift, hemoglobin of 17.7, and hematocrit of 55.8 consistent with severe dehydration."],
    ["Temperature max is 99, heart rate was 133 to 177, blood pressure is 114/43 (while moving), respiratory rate was 28 to 56 with O2 saturations 97 to 100% on room air. Weight was 4.1 kg."],
    ["I will see her back in followup in 3 months, at which time she will be recovering from a shoulder surgery and we will see if she needs any further intervention with regard to the cervical spine.I will also be in touch with Dr. Y to let him know this information prior to the surgery in several weeks."]
]

data = spark.createDataFrame(sample_texts).toDF("text")

result = clf_Pipeline.fit(data).transform(data)
```
```scala

val document_assembler = new DocumentAssembler()
  .setInputCol(Array("text"))
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols(Array("document"))
  .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("document", "token"))
  .setOutputCol("word_embeddings")

val sentence_embeddings = new SentenceEmbeddings()
  .setInputCols(Array("document", "word_embeddings"))
  .setOutputCol("sentence_embeddings")
  .setPoolingStrategy("AVERAGE")

val features_asm = new FeaturesAssembler()
  .setInputCols(Array("sentence_embeddings"))
  .setOutputCol("features")

val generic_classifier = GenericClassifierModel.pretrained("generic_classifier_measurement", "en", "clinical/models")
  .setInputCols(Array("features"))
  .setOutputCol("prediction")

val clf_pipeline = new Pipeline().setStages(Array(
  document_assembler,
  tokenizer,
  word_embeddings,
  sentence_embeddings,
  features_asm,
  generic_classifier
))


val data = Seq([
  ["This is a 58-year-old male who started out having a toothache in the left lower side of the mouth that is now radiating into his jaw and towards his left ear. Triage nurse reported that he does not believe it is his tooth because he has regular dental appointments, but has not seen a dentist since this new toothache began. The patient denies any facial swelling."],
    ["The database was available at this point of time. WBC count is elevated at 19,000 with the left shift, hemoglobin of 17.7, and hematocrit of 55.8 consistent with severe dehydration."],
    ["Temperature max is 99, heart rate was 133 to 177, blood pressure is 114/43 (while moving), respiratory rate was 28 to 56 with O2 saturations 97 to 100% on room air. Weight was 4.1 kg."],
    ["I will see her back in followup in 3 months, at which time she will be recovering from a shoulder surgery and we will see if she needs any further intervention with regard to the cervical spine.I will also be in touch with Dr. Y to let him know this information prior to the surgery in several weeks."]
]]).toDF("text")

val result = clf_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+-------------+
|                                                                                                text|       result|
+----------------------------------------------------------------------------------------------------+-------------+
|This is a 58-year-old male who started out having a toothache in the left lower side of the mouth t...|      [OTHER]|
|The database was available at this point of time. WBC count is elevated at 19,0...|[MEASUREMENT]|
|Temperature max is 99, heart rate was 133 to 177, blood pressure is 114/43 (while moving)...|[MEASUREMENT]|
|I will see her back in follow-up in 3 months, at which time she will be recovering from a shoulder...|      [OTHER]|
+----------------------------------------------------------------------------------------------------+-------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|generic_classifier_measurement|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[features]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|1.5 MB|

## Benchmarking

```bash
| label        | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| MEASUREMENT  | 0.90      | 0.90   | 0.90     | 374     |
| OTHER        | 0.91      | 0.91   | 0.91     | 400     |
| accuracy     | -         | -      | 0.91     | 774     |
| macro-avg    | 0.91      | 0.91   | 0.91     | 774     |
| weighted-avg | 0.91      | 0.91   | 0.91     | 774     |
```