---
layout: model
title: Detect Adverse Drug Events
author: John Snow Labs
name: ner_ade_clinical
date: 2021-04-01
tags: [ner, clinical, licensed, en]
task: Named Entity Recognition
language: en
nav_key: models
edition: Healthcare NLP 3.0.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Detect adverse reactions of drugs in reviews, tweets, and medical text using pretrained NER model.

## Predicted Entities

`DRUG`, `ADE`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ADE/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/16.Adverse_Drug_Event_ADE_NER_and_Classifier.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_ade_clinical_en_3.0.0_3.0_1617260622471.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_ade_clinical_en_3.0.0_3.0_1617260622471.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings_clinical = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_ade_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverter()\
 	  .setInputCols(["sentence", "token", "ner"])\
 	  .setOutputCol("ner_chunk")

nlpPipeline = Pipeline(stages=[document_assembler,
                               sentence_detector,
                               tokenizer,
                               embeddings_clinical,
                               clinical_ner,
                               ner_converter])

model = nlpPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

result = model.transform(spark.createDataFrame([["Hypersensitivity to aspirin can be manifested as acute asthma, urticaria and/or angioedema, or a systemic anaphylactoid reaction."]]).toDF("text"))
```
```scala
val document_assembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")
	
val sentence_detector = new SentenceDetector()
	.setInputCols(Array("document"))
	.setOutputCol("sentence")
	
val tokenizer = new Tokenizer()
	.setInputCols(Array("sentence"))
	.setOutputCol("token")
	
val embeddings_clinical = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
	.setInputCols(Array("sentence","token"))
	.setOutputCol("embeddings")
	
val clinical_ner = MedicalNerModel.pretrained("ner_ade_clinical","en","clinical/models")
	.setInputCols(Array("sentence","token","embeddings"))
	.setOutputCol("ner")
	
val ner_converter = new NerConverter()
	.setInputCols(Array("sentence","token","ner"))
	.setOutputCol("ner_chunk")
	
val nlpPipeline = new Pipeline().setStages(Array(
		 document_assembler, 
		 sentence_detector, 
		 tokenizer, 
		 embeddings_clinical, 
		 clinical_ner, 
		 ner_converter))
	
val model = nlpPipeline.fit(Seq("").toDF("text"))
	
val result = model.transform(Seq("Hypersensitivity to aspirin can be manifested as acute asthma, urticaria and/or angioedema, or a systemic anaphylactoid reaction.").toDF("text"))
```


{:.nlu-block}
```python
import nlu
nlu.load("en.med_ner.ade.clinical").predict("""Hypersensitivity to aspirin can be manifested as acute asthma, urticaria and/or angioedema, or a systemic anaphylactoid reaction.""")
```

## Results

```bash
+-------------------------------+-----+---+---------+
|                          chunk|begin|end|ner_label|
+-------------------------------+-----+---+---------+
|                        aspirin|   20| 26|     DRUG|
|                   acute asthma|   49| 60|      ADE|
|                      urticaria|   63| 71|      ADE|
|                     angioedema|   80| 89|      ADE|
|systemic anaphylactoid reaction|   97|127|      ADE|
+-------------------------------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_ade_clinical|
|Compatibility:|Healthcare NLP 3.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|

## Benchmarking

```bash
+------+-------+------+------+-------+---------+------+------+
|entity|     tp|    fp|    fn|  total|precision|recall|    f1|
+------+-------+------+------+-------+---------+------+------+
|  DRUG|17470.0|1436.0|1951.0|19421.0|    0.924|0.8995|0.9116|
|   ADE| 6010.0|1244.0|1886.0| 7896.0|   0.8285|0.7611|0.7934|
+------+-------+------+------+-------+---------+------+------+

+------------------+
|             macro|
+------------------+
|0.8525141088742945|
+------------------+

+------------------+
|             micro|
+------------------+
|0.8774545383517981|
+------------------+
```