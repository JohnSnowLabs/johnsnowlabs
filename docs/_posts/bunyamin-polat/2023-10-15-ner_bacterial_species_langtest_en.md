---
layout: model
title: Detect Bacterial Species (LangTest)
author: John Snow Labs
name: ner_bacterial_species_langtest
date: 2023-10-15
tags: [en, ner, clinical, licensed, species, langtest]
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

This model detects different types of species of bacteria in clinical texts. It is the version of [er_bacterial_species](https://nlp.johnsnowlabs.com/2021/04/01/ner_bacterial_species_en.html) model augmented with `langtest` library.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **lowercase**        | 200                   | 43                   | 864                   | 1021                 | 90%                   | 81%                  | 96%                 |
| **swap_entities**    | 66                    | 56                   | 264                   | 268                  | 75%                   | 80%                  | 83%                 |
| **titlecase**        | 273                   | 116                  | 791                   | 948                  | 85%                   | 74%                  | 89%                 |
| **uppercase**        | 305                   | 114                  | 760                   | 951                  | 90%                   | 71%                  | 89%                 |
| **weighted average** | **844**               | **329**              | **2679**              | **3188**             | **83%**               | **76.04%**           | **90.65%**          |

## Predicted Entities

`SPECIES`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_bacterial_species_langtest_en_5.1.1_3.0_1697377871284.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_bacterial_species_langtest_en_5.1.1_3.0_1697377871284.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

clinical_ner = MedicalNerModel.pretrained("ner_bacterial_species_langtest", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverter()\
 	.setInputCols(["sentence", "token", "ner"])\
 	.setOutputCol("ner_chunk")

nlpPipeline = Pipeline(stages=[document_assembler, sentence_detector, tokenizer, embeddings_clinical, clinical_ner, ner_converter])

model = nlpPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

result = model.transform(spark.createDataFrame([[""""The PRP8 intein, the most widespread among fungi, occurs in important pathogens such as Histoplasma capsulatum and Paracoccidioides brasiliensis, from the Ajellomycetaceae family.""""]], ["text"]))
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

val ner = MedicalNerModel.pretrained("ner_bacterial_species_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
 	.setInputCols(Array("sentence", "token", "ner"))
 	.setOutputCol("ner_chunk")
    
val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, embeddings_clinical, ner, ner_converter))

val data = Seq("""The PRP8 intein, the most widespread among fungi, occurs in important pathogens such as Histoplasma capsulatum and Paracoccidioides brasiliensis, from the Ajellomycetaceae family.""").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------------+---------+
|chunk                        |ner_label|
+-----------------------------+---------+
|Histoplasma capsulatum       |SPECIES  |
|Paracoccidioides brasiliensis|SPECIES  |
+-----------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_bacterial_species_langtest|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.7 MB|

## Benchmarking

```bash
label         precision  recall  f1-score  support 
SPECIES       0.84       0.90    0.87      521     
micro-avg     0.84       0.90    0.87      521     
macro-avg     0.84       0.90    0.87      521     
weighted-avg  0.84       0.90    0.87      521     
```