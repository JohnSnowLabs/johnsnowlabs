---
layout: model
title: Few-Shot Assertion Model ( SDOH )
author: John Snow Labs
name: fewhot_assertion_sdoh_e5_base_v2_sdoh
date: 2024-07-04
tags: [assertion, en, licensed, clinical, e5, medical, sdoh, fewshot]
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

`Absent`, `Past`, `Present`, `Someone_Else`, `Hypothetical`, `Possible`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/fewhot_assertion_sdoh_e5_base_v2_sdoh_en_5.3.3_3.0_1720084864692.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/fewhot_assertion_sdoh_e5_base_v2_sdoh_en_5.3.3_3.0_1720084864692.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
clinical_ner = MedicalNerModel.pretrained("ner_sdoh","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_sdoh_chunk")\
    .setBlackList(['Age','Gender','Language','HEALTHCARE_INSTITUTION']) 

few_shot_assertion_converter = FewShotAssertionSentenceConverter()\
    .setInputCols(["sentence","token", "ner_sdoh_chunk"])\
    .setOutputCol("assertion_sentence")

e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_sdoh", "en", "clinical/models")\
    .setInputCols(["assertion_sentence"])\
    .setOutputCol("assertion_embedding")

few_shot_assertion_classifier = FewShotAssertionClassifierModel()\
    .pretrained("fewhot_assertion_sdoh_e5_base_v2_sdoh", "en", "clinical/models")\
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

data = spark.createDataFrame([["""Smith works as a cleaning assistant and does not have access to health insurance or paid sick leave.
But she has generally housing problems. She lives in a apartment now.  She has long history of EtOH abuse, beginning in her teens.
She is aware she needs to attend Rehab Programs. She had DUI back in April and was due to be in court this week.
Her partner is an alcoholic and a drug abuser for the last 5 years.
She also mentioned feeling socially isolated and lack of a strong support system."""]]).toDF("text")

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
val clinical_ner = MedicalNerModel.pretrained("ner_sdoh","en","clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_sdoh_chunk")
    .setBlackList(Array('Age','Gender','Language','HEALTHCARE_INSTITUTION')) 

val few_shot_assertion_converter = new FewShotAssertionSentenceConverter()
    .setInputCols(Array("sentence","token", "ner_sdoh_chunk"))
    .setOutputCol("assertion_sentence")

val e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_sdoh", "en", "clinical/models")
    .setInputCols(Array("assertion_sentence"))
    .setOutputCol("assertion_embedding")

val few_shot_assertion_classifier = FewShotAssertionClassifierModel()
    .pretrained("fewhot_assertion_sdoh_e5_base_v2_sdoh", "en", "clinical/models")
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

val data = Seq(Array("""Smith works as a cleaning assistant and does not have access to health insurance or paid sick leave.
But she has generally housing problems. She lives in a apartment now.  She has long history of EtOH abuse, beginning in her teens.
She is aware she needs to attend Rehab Programs. She had DUI back in April and was due to be in court this week.
Her partner is an alcoholic and a drug abuser for the last 5 years.
She also mentioned feeling socially isolated and lack of a strong support system.""")).toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
|    | chunks             |   begin |   end | entities           | assertion    |   confidence |
|---:|:-------------------|--------:|------:|:-------------------|:-------------|-------------:|
|  0 | cleaning assistant |      17 |    34 | Employment         | present      |     0.956549 |
|  1 | health insurance   |      64 |    79 | Insurance_Status   | Absent       |     0.930705 |
|  2 | apartment          |     156 |   164 | Housing            | present      |     0.953653 |
|  3 | EtOH abuse         |     196 |   205 | Alcohol            | Past         |     0.855614 |
|  4 | Rehab Programs     |     265 |   278 | Access_To_Care     | Hypothetical |     0.871034 |
|  5 | DUI                |     289 |   291 | Legal_Issues       | Past         |     0.853602 |
|  6 | alcoholic          |     363 |   371 | Alcohol            | Someone_Else |     0.895126 |
|  7 | drug abuser        |     379 |   389 | Substance_Use      | Someone_Else |     0.89584  |
|  8 | last 5 years       |     399 |   410 | Substance_Duration | present      |     0.95608  |
|  9 | socially isolated  |     440 |   456 | Social_Exclusion   | present      |     0.956841 |
| 10 | strong support     |     472 |   485 | Social_Support     | Absent       |     0.93079  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|fewhot_assertion_sdoh_e5_base_v2_sdoh|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[assertion_embedding]|
|Output Labels:|[assertion]|
|Language:|en|
|Size:|25.4 KB|