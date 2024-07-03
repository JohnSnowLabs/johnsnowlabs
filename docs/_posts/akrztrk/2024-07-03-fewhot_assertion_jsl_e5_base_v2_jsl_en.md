---
layout: model
title: Few-Shot Assertion Model ( JSL )
author: John Snow Labs
name: fewhot_assertion_jsl_e5_base_v2_jsl
date: 2024-07-03
tags: [assertion, en, licensed, clinical, e5, medical, jsl, fewshot]
task: Assertion Status
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.0
supported: true
annotator: FewShotAssertionClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Assign assertion status to clinical entities extracted by NER based on their context in the text. Also this model is trained on a list of clinical and biomedical datasets curated in-house

## Predicted Entities

`Present`, `Absent`, `Possible`, `Planned`, `Past`, `Family`, `Hypotetical`, `SomeoneElse`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/fewhot_assertion_jsl_e5_base_v2_jsl_en_5.3.3_3.0_1720033675839.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/fewhot_assertion_jsl_e5_base_v2_jsl_en_5.3.3_3.0_1720033675839.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")\
    .setSplitChars(["-", "\/"])

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

# ner_jsl
clinical_ner = MedicalNerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_jsl_chunk")\
    .setBlackList(["RelativeDate", "Gender"])

few_shot_assertion_converter = FewShotAssertionSentenceConverter()\
    .setInputCols(["sentence","token", "ner_jsl_chunk"])\
    .setOutputCol("assertion_sentence")

e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_jsl", "en", "clinical/models")\
    .setInputCols(["assertion_sentence"])\
    .setOutputCol("assertion_embedding")

few_shot_assertion_classifier = FewShotAssertionClassifierModel()\
    .pretrained("fewhot_assertion_jsl_e5_base_v2_jsl", "en", "clinical/models")\
    .setInputCols(["assertion_embedding"])\
    .setOutputCol("assertion")

assertion_pipeline = Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    few_shot_assertion_converter,
    e5_embeddings,
    few_shot_assertion_classifier
])

data = spark.createDataFrame([["""Patient had a headache for the last 2 weeks, and appears anxious when she walks fast. No alopecia noted. She denies pain. Her father is paralyzed and it is a stressor for her. She was bullied by her boss and got antidepressant. We prescribed sleeping pills for her current insomnia."""]]).toDF("text")

result = assertion_pipeline.fit(data).transform(data)

```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")
    .setSplitChars(Array("-", "\/"))

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings")

// ner_jsl
val clinical_ner = MedicalNerModel.pretrained("ner_jsl","en","clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_jsl_chunk")
    .setBlackList(["RelativeDate", "Gender"])

val few_shot_assertion_converter = new FewShotAssertionSentenceConverter()
    .setInputCols(Array("sentence","token", "ner_jsl_chunk"))
    .setOutputCol("assertion_sentence")

val e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_jsl", "en", "clinical/models")
    .setInputCols(Array("assertion_sentence"))
    .setOutputCol("assertion_embedding")

val few_shot_assertion_classifier = FewShotAssertionClassifierModel()
    .pretrained("fewhot_assertion_jsl_e5_base_v2_jsl", "en", "clinical/models")
    .setInputCols(Array("assertion_embedding"))
    .setOutputCol("assertion")

val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    few_shot_assertion_converter,
    e5_embeddings,
    few_shot_assertion_classifier))

val data = Seq(Array("""Patient had a headache for the last 2 weeks, and appears anxious when she walks fast. No alopecia noted. She denies pain. Her father is paralyzed and it is a stressor for her. She was bullied by her boss and got antidepressant. We prescribed sleeping pills for her current insomnia.""")).toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
|    | chunks               |   begin |   end | entities        | assertion   |   confidence |
|---:|:---------------------|--------:|------:|:----------------|:------------|-------------:|
|  0 | headache             |      14 |    21 | Symptom         | Past        |     0.905649 |
|  1 | for the last 2 weeks |      23 |    42 | Duration        | Past        |     0.904228 |
|  2 | anxious              |      57 |    63 | Symptom         | Possible    |     0.872409 |
|  3 | alopecia             |      89 |    96 | Symptom         | Absent      |     0.907129 |
|  4 | pain                 |     116 |   119 | Symptom         | Absent      |     0.907316 |
|  5 | paralyzed            |     136 |   144 | Symptom         | Family      |     0.889557 |
|  6 | stressor             |     158 |   165 | Symptom         | Family      |     0.890123 |
|  7 | bullied by her boss  |     184 |   202 | Symptom         | Past        |     0.870923 |
|  8 | antidepressant       |     212 |   225 | Drug_Ingredient | Present     |     0.89228  |
|  9 | sleeping pills       |     242 |   255 | Drug_Ingredient | Planned     |     0.849468 |
| 10 | insomnia             |     273 |   280 | Symptom         | Planned     |     0.818986 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|fewhot_assertion_jsl_e5_base_v2_jsl|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[assertion_embedding]|
|Output Labels:|[assertion]|
|Language:|en|
|Size:|32.1 KB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
      Absent       0.97      0.96      0.97       707
      Family       0.92      0.91      0.92       283
Hypothetical       0.88      0.83      0.85       386
        Past       0.91      0.90      0.91       717
     Planned       0.75      0.91      0.82       159
    Possible       0.77      0.93      0.84       289
     Present       0.94      0.89      0.92      1058
 SomeoneElse       0.84      0.87      0.85       148
    accuracy          -         -      0.90      3747
   macro-avg       0.87      0.90      0.88      3747
weighted-avg       0.91      0.90      0.91      3747
```
