---
layout: model
title: Detect Problems, Tests and Treatments (ner_clinical_large_v2)
author: John Snow Labs
name: ner_clinical_large_v2
date: 2025-12-28
tags: [ner, clinical, licensed, en]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_EVENTS_CLINICAL/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_large_v2_en_6.2.0_3.4_1766922434100.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_large_v2_en_6.2.0_3.4_1766922434100.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_clinical_large_v2", "en", "clinical/models") \
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

text = """
Mr. ABC is a 60-year-old gentleman who had stress test earlier today in my office with severe chest pain after 5 minutes of exercise on the standard Bruce with horizontal ST depressions and moderate apical ischemia on stress imaging only. 
He required 3 sublingual nitroglycerin in total. 
The patient underwent cardiac catheterization with myself today which showed mild-to-moderate left main distal disease of 30%, a severe mid-LAD lesion of 99%, and a mid-left circumflex lesion of 80% with normal LV function and some mild luminal irregularities in the right coronary artery with some moderate stenosis seen in the mid to distal right PDA.
"""

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

word_embeddings =  nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = medical.NerModel.pretrained("ner_clinical_large_v2", "en", "clinical/models") \
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

text = """
Mr. ABC is a 60-year-old gentleman who had stress test earlier today in my office with severe chest pain after 5 minutes of exercise on the standard Bruce with horizontal ST depressions and moderate apical ischemia on stress imaging only. 
He required 3 sublingual nitroglycerin in total. 
The patient underwent cardiac catheterization with myself today which showed mild-to-moderate left main distal disease of 30%, a severe mid-LAD lesion of 99%, and a mid-left circumflex lesion of 80% with normal LV function and some mild luminal irregularities in the right coronary artery with some moderate stenosis seen in the mid to distal right PDA.
"""

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

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_clinical_large_v2", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")


val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter
))

val data = Seq("""
Mr. ABC is a 60-year-old gentleman who had stress test earlier today in my office with severe chest pain after 5 minutes of exercise on the standard Bruce with horizontal ST depressions and moderate apical ischemia on stress imaging only. 
He required 3 sublingual nitroglycerin in total. 
The patient underwent cardiac catheterization with myself today which showed mild-to-moderate left main distal disease of 30%, a severe mid-LAD lesion of 99%, and a mid-left circumflex lesion of 80% with normal LV function and some mild luminal irregularities in the right coronary artery with some moderate stenosis seen in the mid to distal right PDA.
""").toDF("text")

val results = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
|chunk                      |begin|end|ner_label|
|--------------------------:|:----|:--|:--------|
|stress test                |44   |54 |TEST     |
|chest pain                 |95   |104|PROBLEM  |
|ST depressions             |172  |185|PROBLEM  |
|ischemia                   |207  |214|PROBLEM  |
|stress imaging             |219  |232|TEST     |
|cardiac catheterization    |313  |335|TEST     |
|disease                    |402  |408|PROBLEM  |
|severe mid-LAD lesion      |420  |440|PROBLEM  |
|mild luminal irregularities|523  |549|PROBLEM  |
|moderate stenosis          |590  |606|PROBLEM  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical_large_v2|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.5 MB|

## References

Trained on merged ner oncology, ner posology and ner clinical datasets.

## Benchmarking

```bash
| Label          | Precision | Recall | F1-Score | Support |
|----------------|-----------|--------|----------|---------|
| B-PROBLEM      | 0.8871    | 0.8788 | 0.8829   | 17,793  |
| B-TEST         | 0.8488    | 0.8439 | 0.8464   | 8,433   |
| B-TREATMENT    | 0.8787    | 0.8589 | 0.8687   | 10,841  |
| I-PROBLEM      | 0.8410    | 0.8500 | 0.8455   | 10,730  |
| I-TEST         | 0.7968    | 0.8301 | 0.8131   | 5,773   |
| I-TREATMENT    | 0.8191    | 0.8170 | 0.8181   | 4,967   |
| O              | 0.9908    | 0.9910 | 0.9909   | 506,113 |
| Accuracy       |           |        | 0.9769   | 564,650 |
| Macro Avg      | 0.8661    | 0.8671 | 0.8665   | 564,650 |
| Weighted Avg   | 0.9769    | 0.9769 | 0.9769   | 564,650 |
```