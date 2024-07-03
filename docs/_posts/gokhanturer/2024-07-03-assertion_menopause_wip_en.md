---
layout: model
title: Detect Assertion Status from Menopause Entities
author: John Snow Labs
name: assertion_menopause_wip
date: 2024-07-03
tags: [en, licensed, clinical, menopause, assertion]
task: Assertion Status
language: en
edition: Healthcare NLP 5.3.2
spark_version: 3.0
supported: true
annotator: AssertionDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model detects the assertion status of menopause-related entities.

## Predicted Entities

`Present`, `Absent`, `Possible`, `Past`, `Hypothetical`, `Planned`, `Family`, `Menarche_Age`, `Menopause_Age`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_menopause_wip_en_5.3.2_3.0_1720021324244.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_menopause_wip_en_5.3.2_3.0_1720021324244.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_menopause_core", "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

assertion = AssertionDLModel.pretrained("assertion_menopause_wip", "en", "clinical/models")\
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter,
    assertion
    ])

sample_texts = ["""A 50-year-old woman, G2P1, presents with symptoms of perimenopause including night sweats, irregular menstruation, and fatigue.She has previously been diagnosed with hypertension. She is taking hormone replacement therapy with estradiol and norethindrone acetate. Recent tests included a bone density scan, which confirmed osteoporosis and showed elevated FSH levels. She also underwent a vaginal swab test for routine screening. Her mother has a history of breast cancer. Her menarche age was 11."""]


data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_menopause_core", "en", "clinical/models")
    .setInputCols(Array("sentence", "token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val assertion = AssertionDLModel.pretrained("assertion_menopause_wip", "en", "clinical/models")
    .setInputCols(Array("sentence", "ner_chunk", "embeddings"))
    .setOutputCol("assertion")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter,
    assertion
))

val sample_texts = Seq("""A 50-year-old woman, G2P1, presents with symptoms of perimenopause including night sweats, irregular menstruation, and fatigue.She has previously been diagnosed with hypertension. She is taking hormone replacement therapy with estradiol and norethindrone acetate. Recent tests included a bone density scan, which confirmed osteoporosis and showed elevated FSH levels. She also underwent a vaginal swab test for routine screening. Her mother has a history of breast cancer. Her menarche age was 11.""").toDF("text")


val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

## Results

```bash
+---------------------------+-----+---+---------------------------+------------+----------+
|chunk                      |begin|end|ner_label                  |assertion   |confidence|
+---------------------------+-----+---+---------------------------+------------+----------+
|G2P1                       |21   |24 |G_P                        |Present     |0.9999    |
|perimenopause              |53   |65 |Perimenopause              |Present     |0.9999    |
|night sweats               |77   |88 |Other_Symptom              |Present     |0.9997    |
|irregular menstruation     |91   |112|Irregular_Menstruation     |Present     |0.9997    |
|fatigue                    |119  |125|Other_Symptom              |Present     |0.9954    |
|hypertension               |166  |177|Hypertension               |Past        |0.9916    |
|hormone replacement therapy|194  |220|Hormone_Replacement_Therapy|Present     |0.9988    |
|estradiol                  |227  |235|Hormone_Replacement_Therapy|Present     |0.9696    |
|norethindrone acetate      |241  |261|Hormone_Replacement_Therapy|Present     |0.9984    |
|osteoporosis               |323  |334|Osteoporosis               |Present     |1.0       |
|elevated                   |347  |354|Test_Result                |Present     |1.0       |
|FSH                        |356  |358|Hormone_Testing            |Present     |0.9999    |
|vaginal swab               |389  |400|Vaginal_Swab               |Present     |1.0       |
|breast cancer              |458  |470|Oncological                |Family      |0.9843    |
|11                         |494  |495|Age                        |Menarche_Age|0.9891    |
+---------------------------+-----+---+---------------------------+------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_menopause_wip|
|Compatibility:|Healthcare NLP 5.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, ner_chunk, embeddings]|
|Output Labels:|[assertion_pred]|
|Language:|en|
|Size:|2.5 MB|

## References

The datasets employed in training this model were meticulously curated and annotated using our in-house capabilities.

## Benchmarking

```bash
        label  precision    recall  f1-score   support
       Absent       0.83      0.84      0.84       177
       Family       0.47      0.73      0.57        11
 Hypothetical       0.80      0.71      0.75       413
 Menarche_Age       1.00      1.00      1.00         5
Menopause_Age       0.85      0.94      0.89        18
         Past       0.46      0.41      0.43        44
      Planned       0.80      0.67      0.73         6
     Possible       0.59      0.46      0.52        28
      Present       0.89      0.92      0.90      1558
     accuracy         -         -       0.86      2260
    macro-avg       0.74      0.74      0.74      2260
 weighted-avg       0.86      0.86      0.86      2260
```