---
layout: model
title: Few-Shot Assertion Model ( Smoking )
author: John Snow Labs
name: fewhot_assertion_smoking_e5_base_v2_smoking
date: 2024-07-03
tags: [assertion, en, licensed, clinical, e5, medical, smoking, fewshot]
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

`Present`, `Absent`,  `Past`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/fewhot_assertion_smoking_e5_base_v2_smoking_en_5.3.3_3.0_1720021478167.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/fewhot_assertion_smoking_e5_base_v2_smoking_en_5.3.3_3.0_1720021478167.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

# ner_sdoh
ner_smoking = MedicalNerModel.pretrained("ner_sdoh","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_smoking")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner_smoking"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["smoking"])

few_shot_assertion_converter = FewShotAssertionSentenceConverter()\
    .setInputCols(["sentence","token","ner_chunk"])\
    .setOutputCol("assertion_sentence")

e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_smoking", "en", "clinical/models")\
    .setInputCols(["assertion_sentence"])\
    .setOutputCol("assertion_embedding")

few_shot_assertion_classifier = FewShotAssertionClassifierModel()\
    .pretrained("fewhot_assertion_smoking_e5_base_v2_smoking", "en", "clinical/models")\
    .setInputCols(["assertion_embedding"])\
    .setOutputCol("assertion")

assertion_pipeline = Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_smoking,
    ner_converter,
    few_shot_assertion_converter,
    e5_embeddings,
    few_shot_assertion_classifier
])

data = spark.createDataFrame([["""The patient, a 50-year-old man, came to the clinic due to worsening shortness of breath, productive cough, and wheezing. He has a history of heavy smoking, having smoked a pack of cigarettes daily for 20 years. He quit smoking five years ago after recurrent respiratory infections and worsening breathing problems. Despite quitting, he frequently experiences exacerbations of chronic bronchitis, particularly in the winter. Over the past week, his symptoms have intensified, with increased sputum production and dyspnea on exertion."""]]).toDF("text")

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

// ner_sdoh
val ner_smoking = MedicalNerModel.pretrained("ner_sdoh","en","clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner_smoking")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence","token","ner_smoking"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("smoking"))

val few_shot_assertion_converter = new FewShotAssertionSentenceConverter()
    .setInputCols(Array("sentence","token","ner_chunk"))
    .setOutputCol("assertion_sentence")

val e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_smoking", "en", "clinical/models")
    .setInputCols(Array("assertion_sentence"))
    .setOutputCol("assertion_embedding")

val few_shot_assertion_classifier = FewShotAssertionClassifierModel()
    .pretrained("fewhot_assertion_smoking_e5_base_v2_smoking", "en", "clinical/models")
    .setInputCols(Array("assertion_embedding"))
    .setOutputCol("assertion")

val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_smoking,
    ner_converter,
    few_shot_assertion_converter,
    e5_embeddings,
    few_shot_assertion_classifier))

val data = Seq(Array("""The patient, a 50-year-old man, came to the clinic due to worsening shortness of breath, productive cough, and wheezing. He has a history of heavy smoking, having smoked a pack of cigarettes daily for 20 years. He quit smoking five years ago after recurrent respiratory infections and worsening breathing problems. Despite quitting, he frequently experiences exacerbations of chronic bronchitis, particularly in the winter. Over the past week, his symptoms have intensified, with increased sputum production and dyspnea on exertion.""")).toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
|    | chunks     |   begin |   end | entities   | assertion   |   confidence |
|---:|:-----------|--------:|------:|:-----------|:------------|-------------:|
|  0 | smoking    |     147 |   153 | Smoking    | Past        |     0.936773 |
|  1 | smoked     |     163 |   168 | Smoking    | Past        |     0.936713 |
|  2 | cigarettes |     180 |   189 | Smoking    | Past        |     0.936727 |
|  3 | smoking    |     219 |   225 | Smoking    | Past        |     0.936954 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|fewhot_assertion_smoking_e5_base_v2_smoking|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[assertion_embedding]|
|Output Labels:|[assertion]|
|Language:|en|
|Size:|15.2 KB|


## Benchmarking

```bash
       label  precision    recall  f1-score   support
      Absent       0.95      1.00      0.97        19
        Past       0.94      0.89      0.91        18
     Present       0.92      0.92      0.92        13
    accuracy          -         -      0.94        50
   macro-avg       0.94      0.94      0.94        50
weighted-avg       0.94      0.94      0.94        50
```
