---
layout: model
title: Detect Diseases (LangTest)
author: John Snow Labs
name: ner_diseases_langtest
date: 2023-10-15
tags: [en, ner, clinical, licensed, diseases, langtest]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.1.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts mentions of different types of disease in medical text. It is the version of [ner_diseases](https://nlp.johnsnowlabs.com/2021/03/31/ner_diseases_en.html) model augmented with `langtest` library.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**     | 266                   | 55                   | 541                   | 752                  | 70%                   | 67%                  | 93%                 |
| **lowercase**        | 152                   | 107                  | 665                   | 710                  | 70%                   | 81%                  | 87%                 |
| **swap_entities**    | 120                   | 118                  | 686                   | 688                  | 70%                   | 85%                  | 85%                 |
| **titlecase**        | 320                   | 113                  | 497                   | 704                  | 70%                   | 61%                  | 86%                 |
| **uppercase**        | 768                   | 175                  | 51                    | 644                  | 70%                   | 6%                   | 79%                 |
| **weighted average** | **1626**              | **568**              | **2440**              | **3498**             | **70%**               | **60.01%**           | **86.03%**          |

## Predicted Entities

`Disease`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_diseases_langtest_en_5.1.1_3.0_1697407071834.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_diseases_langtest_en_5.1.1_3.0_1697407071834.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

clinical_ner = MedicalNerModel.pretrained("ner_diseases_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

nlpPipeline = Pipeline(stages=[document_assembler, sentence_detector, tokenizer, embeddings_clinical, clinical_ner, ner_converter])

model = nlpPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

result = model.transform(spark.createDataFrame([["""POSTOPERATIVE DIAGNOSES:
1. Epidural fibrosis with nerve root entrapment.
OPERATION PERFORMED:
Left L4-L5 transforaminal neuroplasty with nerve root decompression and lysis of adherence followed by epidural steroid injection."""]], ["text"]))
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

val embeddings_clinical = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_diseases_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, embeddings_clinical, ner, ner_converter))

val data = Seq("""POSTOPERATIVE DIAGNOSES:
1. Epidural fibrosis with nerve root entrapment.
OPERATION PERFORMED:
Left L4-L5 transforaminal neuroplasty with nerve root decompression and lysis of adherence followed by epidural steroid injection.""").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------------+---------+
|chunk                   |ner_label|
+------------------------+---------+
|fibrosis                |Disease  |
|nerve root decompression|Disease  |
+------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_diseases_langtest|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.5 MB|

## References

Trained with an augmented version of the [i2b2 dataset](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/) with `embeddings_clinical`.

## Benchmarking

```bash
label         precision  recall  f1-score  support 
Disease       0.91       0.93    0.92      1348    
micro-avg     0.91       0.93    0.92      1348    
macro-avg     0.91       0.93    0.92      1348    
weighted-avg  0.91       0.93    0.92      1348    
```
