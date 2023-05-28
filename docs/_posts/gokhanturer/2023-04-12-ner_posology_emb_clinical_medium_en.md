---
layout: model
title: Detect Posology concepts (clinical_medium)
author: John Snow Labs
name: ner_posology_emb_clinical_medium
date: 2023-04-12
tags: [ner, licensed, english, clinical, posology, en]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model detects Drug, Dosage, and administration instructions in text using pretrained NER model.

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_POSOLOGY/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_POSOLOGY.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_posology_emb_clinical_medium_en_4.3.2_3.0_1681315841950.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_posology_emb_clinical_medium_en_4.3.2_3.0_1681315841950.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence") 

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_medium", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

posology_ner = MedicalNerModel.pretrained('ner_posology_emb_clinical_medium' , "en",  "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("posology_ner")
    
posology_ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "posology_ner"]) \
    .setOutputCol("posology_ner_chunk")

posology_ner_pipeline = Pipeline(stages=[
    documentAssembler, 
    sentenceDetector,
    tokenizer,
    word_embeddings,
    posology_ner,
    posology_ner_converter])

empty_data = spark.createDataFrame([[""]]).toDF("text")

posology_ner_model = posology_ner_pipeline.fit(empty_data)

results = posology_ner_model.transform(spark.createDataFrame([["The patient has been advised Aspirin 81 milligrams QDay. insulin 50 units in a.m. HCTZ 50 mg QDay. Nitroglycerin 1/150 sublingually."]]).toDF("text"))
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")
    
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_medium", "en", "clinical/models")\
    .setInputCols(Array("sentence", "token"))\
    .setOutputCol("embeddings")

val posology_ner_model = MedicalNerModel.pretrained('ner_posology_emb_clinical_large' "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("posology_ner")

val posology_ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("posology_ner_chunk")

val posology_pipeline = new PipelineModel().setStages(Array(document_assembler, 
                                                   sentence_detector,
                                                   tokenizer,
                                                   word_embeddings,
                                                   posology_ner_model,
                                                   posology_ner_converter))

val data = Seq(""" The patient has been advised Aspirin 81 milligrams QDay. insulin 50 units in a.m. HCTZ 50 mg QDay. Nitroglycerin 1/150 sublingually.""").toDS.toDF("text")

val result = model.fit(data).transform(data)
```
</div>

## Results

```bash
|    | chunks        |   begin |   end | entities   |
|---:|:--------------|--------:|------:|:-----------|
|  0 | Aspirin       |      29 |    35 | DRUG       |
|  1 | 81 milligrams |      37 |    49 | STRENGTH   |
|  2 | QDay          |      51 |    54 | FREQUENCY  |
|  3 | insulin       |      57 |    63 | DRUG       |
|  4 | 50 units      |      65 |    72 | STRENGTH   |
|  5 | HCTZ          |      82 |    85 | DRUG       |
|  6 | 50 mg         |      87 |    91 | STRENGTH   |
|  7 | QDay          |      93 |    96 | FREQUENCY  |
|  8 | Nitroglycerin |      99 |   111 | DRUG       |
|  9 | 1/150         |     113 |   117 | STRENGTH   |
| 10 | sublingually  |     119 |   130 | ROUTE      |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_posology_emb_clinical_medium|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|2.8 MB|

## Benchmarking

```bash
                  precision  recall   f1-score  support
        DRUG       0.91      0.91      0.91      2252
    STRENGTH       0.88      0.93      0.91      2290
   FREQUENCY       0.90      0.94      0.92      1782
    DURATION       0.78      0.84      0.81       463
      DOSAGE       0.66      0.63      0.65       476
       ROUTE       0.89      0.89      0.89       394
        FORM       0.86      0.76      0.81       773
   micro avg       0.87      0.89      0.88      8430
   macro avg       0.84      0.84      0.84      8430
weighted avg       0.87      0.89      0.88      8430
```
