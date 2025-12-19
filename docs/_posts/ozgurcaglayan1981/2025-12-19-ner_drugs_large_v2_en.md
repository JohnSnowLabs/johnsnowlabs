---
layout: model
title: Detect Drug Entities
author: John Snow Labs
name: ner_drugs_large_v2
date: 2025-12-19
tags: [ner, clinical, licensed, en]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.2.2
spark_version: 3.4
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for Drugs. The model combines dosage, strength, form, and route into a single entity: Drug. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`DRUG`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_drugs_large_v2_en_6.2.2_3.4_1766177214051.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_drugs_large_v2_en_6.2.2_3.4_1766177214051.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_large", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_drugs_large_v2", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

nlpPipeline = Pipeline(stages=[
                  document_assembler,
                  sentence_detector,
                  tokenizer,
                  word_embeddings,
                  clinical_ner,
                  ner_converter])

model = nlpPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

text = '''
The patient is a 40-year-old white male who presents with a chief complaint of 'chest pain'.
The patient is diabetic and has a prior history of coronary artery disease.
The patient presents today stating that his chest pain started yesterday evening and has been somewhat intermittent.
He has been advised Aspirin 81 milligrams QDay.
Humulin N. insulin 50 units in a.m.
HCTZ 50 mg QDay. Nitroglycerin 1/150 sublingually PRN chest pain.
'''

results = model.transform(spark.createDataFrame([[text]]).toDF("text"))

```

{:.jsl-block}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings =  nlp.WordEmbeddingsModel.pretrained("embeddings_clinical_large", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = medical.NerModel.pretrained("ner_drugs_large_v2", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

nlpPipeline = nlp.Pipeline(stages=[
                  document_assembler,
                  sentence_detector,
                  tokenizer,
                  word_embeddings,
                  clinical_ner,
                  ner_converter])

model = nlpPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

text = '''
The patient is a 40-year-old white male who presents with a chief complaint of 'chest pain'.
The patient is diabetic and has a prior history of coronary artery disease.
The patient presents today stating that his chest pain started yesterday evening and has been somewhat intermittent.
He has been advised Aspirin 81 milligrams QDay.
Humulin N. insulin 50 units in a.m.
HCTZ 50 mg QDay. Nitroglycerin 1/150 sublingually PRN chest pain.
'''

results = model.transform(spark.createDataFrame([[text]]).toDF("text"))
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_ner = MedicalNerModel.pretrained("ner_drugs_large_v2", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")


val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    clinical_ner,
    ner_converter
))

val data = Seq('''
The patient is a 40-year-old white male who presents with a chief complaint of 'chest pain'.
The patient is diabetic and has a prior history of coronary artery disease.
The patient presents today stating that his chest pain started yesterday evening and has been somewhat intermittent.
He has been advised Aspirin 81 milligrams QDay.
Humulin N. insulin 50 units in a.m.
HCTZ 50 mg QDay. Nitroglycerin 1/150 sublingually PRN chest pain.
''').toDF("text")

val results = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------+-----+---+---------+
|chunk        |begin|end|ner_label|
+-------------+-----+---+---------+
|Aspirin      |307  |313|DRUG     |
|Humulin N    |335  |343|DRUG     |
|insulin      |346  |352|DRUG     |
|HCTZ         |371  |374|DRUG     |
|Nitroglycerin|388  |400|DRUG     |
+-------------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_drugs_large_v2|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.5 MB|

## References

Trained on merged ner_posology, ner_ade, ner_drugs datasets.

## Benchmarking

```bash
| Entity        | Precision | Recall   | F1-score | Support |
|---------------|----------:|-------  :|---------:|--------:|
| DRUG          | 0.939819  | 0.951195 | 0.945473 | 46,676  |
| Micro_Avg     | 0.939819  | 0.951195 | 0.945473 | 46,676  |
| Macro_Avg     | 0.939819  | 0.951195 | 0.945473 | 46,676  |
| Weighted_Avg  | 0.939819  | 0.951195 | 0.945473 | 46,676  |
```
