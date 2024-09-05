---
layout: model
title: Detect Adverse Drug Events
author: John Snow Labs
name: ner_ade_clinical_v2
date: 2024-09-05
tags: [en, licensed, clinical, ner, ade]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Detect adverse reactions of drugs, and problem in reviews, tweets, and medical text using pretrained NER model.

## Predicted Entities

`DRUG`, `ADE`, `PROBLEM`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ADE/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/16.Adverse_Drug_Event_ADE_NER_and_Classifier.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_ade_clinical_v2_en_5.4.1_3.0_1725553595853.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_ade_clinical_v2_en_5.4.1_3.0_1725553595853.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained("ner_ade_clinical_v2", "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
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

model = pipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

result = model.transform(spark.createDataFrame([["""I have an allergic reaction to vancomycin so I have itchy skin, sore throat/burning/itching, numbness of tongue and gums.
I would not recommend this drug to anyone, especially since I have never had such an adverse reaction to any other medication."""]]).toDF("text"))
```
```scala
val document_assembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")
	
val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")
	.setInputCols(Array("document"))
	.setOutputCol("sentence")
	
val tokenizer = new Tokenizer()
	.setInputCols(Array("sentence"))
	.setOutputCol("token")
	
val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
	.setInputCols(Array("sentence","token"))
	.setOutputCol("embeddings")
	
val ner_model = MedicalNerModel.pretrained("ner_ade_clinical_v2", "en", "clinical/models")
	.setInputCols(Array("sentence","token","embeddings"))
	.setOutputCol("ner")
	
val ner_converter = new NerConverterInternal()
	.setInputCols(Array("sentence","token","ner"))
	.setOutputCol("ner_chunk")
	
val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter))
	
val model = pipeline.fit(Seq("").toDF("text"))
	
val result = model.transform(Seq("""I have an allergic reaction to vancomycin so I have itchy skin, sore throat/burning/itching, numbness of tongue and gums.
I would not recommend this drug to anyone, especially since I have never had such an adverse reaction to any other medication.""").toDF("text"))
```
</div>

## Results

```bash
+---------------------------+-----+---+---------+
|chunk                      |begin|end|ner_label|
+---------------------------+-----+---+---------+
|allergic reaction          |10   |26 |ADE      |
|vancomycin                 |31   |40 |DRUG     |
|itchy skin                 |52   |61 |ADE      |
|sore throat/burning/itching|64   |90 |ADE      |
|numbness of tongue and gums|93   |119|ADE      |
|an adverse reaction        |204  |222|PROBLEM  |
+---------------------------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_ade_clinical_v2|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|2.8 MB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
         ADE       0.84      0.81      0.82      7966
        DRUG       0.94      0.91      0.93     17519
     PROBLEM       0.91      0.86      0.88     33301
   micro-avg       0.91      0.87      0.89     58786
   macro-avg       0.89      0.86      0.88     58786
weighted-avg       0.91      0.87      0.89     58786
```