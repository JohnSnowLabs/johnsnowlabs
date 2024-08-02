---
layout: model
title: Detect Problems, Tests and Treatments (ner_clinical) in Vietnamese
author: John Snow Labs
name: ner_clinical
date: 2023-09-20
tags: [ner, vi, clinical, licensed]
task: Named Entity Recognition
language: vi
edition: Healthcare NLP 5.1.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms in Vietnamese. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CLINICAL_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_vi_5.1.0_3.0_1695240145908.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_vi_5.1.0_3.0_1695240145908.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","vi") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "vi", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
    ])

sample_df = spark.createDataFrame([["""A/P : Nam , 48 tuổi, có tiền sử HCV, rối loạn lưỡng cực , có nỗ lực tự tử, dùng Inderal, Klonopin, Geodon, nhập viện tại Jackson với ống thông khí để bảo vệ đường thở, có câu hỏi về xâm nhập phía sau tim bên trái, hiện tại đang ổn định. một cuộc quét MRI cổ chỉ ra sự thoái hóa đĩa ấn tượng rất ở C5-C6, ít hơn ở C4-C5, với sự nén tủy rõ ràng, đặc biệt là ở phía bên phải C5-C6."""]]).toDF("text")

result = pipeline.fit(sample_df).transform(sample_df)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","vi")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_clinical", "vi", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter))

val sample_data = Seq("""A/P : Nam , 48 tuổi, có tiền sử HCV, rối loạn lưỡng cực , có nỗ lực tự tử, dùng Inderal, Klonopin, Geodon, nhập viện tại Jackson với ống thông khí để bảo vệ đường thở, có câu hỏi về xâm nhập phía sau tim bên trái, hiện tại đang ổn định. một cuộc quét MRI cổ chỉ ra sự thoái hóa đĩa ấn tượng rất ở C5-C6, ít hơn ở C4-C5, với sự nén tủy rõ ràng, đặc biệt là ở phía bên phải C5-C6.""").toDS.toDF("text")

val result = pipeline.fit(sample_data).transform(sample_data)
```
</div>

## Results

```bash
+------------------------------+-----+---+---------+
|chunk                         |begin|end|ner_label|
+------------------------------+-----+---+---------+
|HCV                           |32   |34 |PROBLEM  |
|rối loạn lưỡng cực            |37   |54 |PROBLEM  |
|tự tử                         |68   |72 |PROBLEM  |
|Inderal                       |80   |86 |TREATMENT|
|Klonopin                      |89   |96 |TREATMENT|
|Geodon                        |99   |104|TREATMENT|
|ống thông khí                 |133  |145|TREATMENT|
|bảo vệ đường thở              |150  |165|TREATMENT|
|xâm nhập phía sau tim bên trái|182  |211|PROBLEM  |
|một cuộc quét MRI cổ          |237  |256|TEST     |
|sự nén tủy rõ ràng            |324  |341|PROBLEM  |
+------------------------------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|vi|
|Size:|2.9 MB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
   TREATMENT       0.68      0.75      0.71       554
        TEST       0.86      0.75      0.80       357
     PROBLEM       0.78      0.78      0.78      1373
   micro-avg       0.76      0.77      0.77      2284
   macro-avg       0.77      0.76      0.77      2284
weighted-avg       0.77      0.77      0.77      2284
```
