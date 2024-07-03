---
layout: model
title: Few-Shot Assertion Model ( Radiology )
author: John Snow Labs
name: fewhot_assertion_radiology_e5_base_v2_radiology
date: 2024-07-03
tags: [assertion, en, licensed, clinical, e5, medical, radiology, fewshot]
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

`Confirmed`, `Negative`, `Suspected`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/fewhot_assertion_radiology_e5_base_v2_radiology_en_5.3.3_3.0_1720036334397.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/fewhot_assertion_radiology_e5_base_v2_radiology_en_5.3.3_3.0_1720036334397.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

# ner_radiology
clinical_ner = MedicalNerModel.pretrained("ner_radiology","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_radiology_chunk")\
    .setWhiteList(["ImagingFindings"])

few_shot_assertion_converter = FewShotAssertionSentenceConverter()\
    .setInputCols(["sentence","token", "ner_radiology_chunk"])\
    .setOutputCol("assertion_sentence")

e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_radiology", "en", "clinical/models")\
    .setInputCols(["assertion_sentence"])\
    .setOutputCol("assertion_embedding")

few_shot_assertion_classifier = FewShotAssertionClassifierModel()\
    .pretrained("fewhot_assertion_radiology_e5_base_v2_radiology", "en", "clinical/models")\
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

data = spark.createDataFrame([["""No right-sided pleural effusion or pneumothorax is definitively seen and there are mildly displaced fractures of the left lateral 8th and likely 9th ribs."""]]).toDF("text")

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

// ner_radiology
val clinical_ner = MedicalNerModel.pretrained("ner_radiology","en","clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_radiology_chunk")
    .setWhiteList(Array("ImagingFindings"))

val few_shot_assertion_converter = new FewShotAssertionSentenceConverter()
    .setInputCols(Array("sentence","token", "ner_radiology_chunk"))
    .setOutputCol("assertion_sentence")

val e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_radiology", "en", "clinical/models")
    .setInputCols(Array("assertion_sentence"))
    .setOutputCol("assertion_embedding")

val few_shot_assertion_classifier = FewShotAssertionClassifierModel()
    .pretrained("fewhot_assertion_radiology_e5_base_v2_radiology", "en", "clinical/models")
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

val data = Seq(Array("""No right-sided pleural effusion or pneumothorax is definitively seen and there are mildly displaced fractures of the left lateral 8th and likely 9th ribs.""")).toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
|    | chunks              |   begin |   end | entities        | assertion   |   confidence |
|---:|:--------------------|--------:|------:|:----------------|:------------|-------------:|
|  0 | effusion            |      23 |    30 | ImagingFindings | Negative    |     0.94988  |
|  1 | pneumothorax        |      35 |    46 | ImagingFindings | Negative    |     0.94994  |
|  2 | displaced fractures |      90 |   108 | ImagingFindings | Confirmed   |     0.969101 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|fewhot_assertion_radiology_e5_base_v2_radiology|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[assertion_embedding]|
|Output Labels:|[assertion]|
|Language:|en|
|Size:|15.2 KB|

## Benchmarking

```bash
      label   precision    recall  f1-score   support
   Confirmed       0.97      0.93      0.95      2323
    Negative       0.94      0.97      0.96       403
   Suspected       0.82      0.91      0.86       779
    accuracy          -         -      0.93      3505
   macro-avg       0.91      0.94      0.92      3505
weighted-avg       0.93      0.93      0.93      3505
```
