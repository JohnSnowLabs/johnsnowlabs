---
layout: model
title: Detect Genes and Human Phenotypes (LangTest)
author: John Snow Labs
name: ner_human_phenotype_gene_clinical_langtest
date: 2023-11-04
tags: [en, ner, clinical, licensed, langtest, human, phenotype, gene]
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

This model detects mentions of genes and human phenotypes (hp) in medical text. It is the version of [ner_human_phenotype_gene_clinical](https://nlp.johnsnowlabs.com/2021/03/31/ner_human_phenotype_gene_clinical_en.html) model augmented with `langtest` library.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**     | 175                   | 120                  | 606                   | 661                  | 85%                   | 78%                  | 85%                 |
| **lowercase**        | 262                   | 110                  | 521                   | 673                  | 85%                   | 67%                  | 86%                 |
| **swap_entities**    | 123                   | 112                  | 600                   | 614                  | 80%                   | 83%                  | 85%                 |
| **titlecase**        | 704                   | 155                  | 79                    | 628                  | 75%                   | 10%                  | 80%                 |
| **uppercase**        | 709                   | 174                  | 74                    | 609                  | 75%                   | 9%                   | 78%                 |
| **weighted average** | **1973**              | **671**              | **1880**              | **3185**             | **80%**               | **48.79%**           | **82.60%**          |

## Predicted Entities

`GENE`, `HP`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_human_phenotype_gene_clinical_langtest_en_5.1.1_3.0_1699104573201.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_human_phenotype_gene_clinical_langtest_en_5.1.1_3.0_1699104573201.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_human_phenotype_gene_clinical_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")
    
nlp_pipeline = Pipeline(stages=[document_assembler, sentence_detector, tokenizer, word_embeddings, clinical_ner, ner_converter])

model = nlp_pipeline.fit(spark.createDataFrame([['']]).toDF("text"))

result = model.transform(spark.createDataFrame([["Here we presented a case (BS type) of a 17 years old female presented with polyhydramnios, polyuria, nephrocalcinosis, and hypokalemia, which was alleviated after treatment with celecoxib and vitamin D(3)."]]).toDF("text"))
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols("document") 
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_human_phenotype_gene_clinical_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, ner, ner_converter))

val data = Seq("""Here we presented a case (BS type) of a 17 years old female presented with polyhydramnios, polyuria, nephrocalcinosis, and hypokalemia, which was alleviated after treatment with celecoxib and vitamin D(3).""").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------------------+---------+
|chunk                     |ner_label|
+--------------------------+---------+
|CHN1                      |GENE     |
|MDH1                      |GENE     |
|PCP4                      |GENE     |
|RTN1                      |GENE     |
|SLC14A1                   |GENE     |
|SNAP25                    |GENE     |
|VSNL1                     |GENE     |
|neurodegenerative diseases|HP       |
+--------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_human_phenotype_gene_clinical_langtest|
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
GENE          0.85       0.89    0.87      1082    
HP            0.89       0.88    0.88      878     
micro-avg     0.87       0.88    0.87      1960    
macro-avg     0.87       0.88    0.87      1960    
weighted-avg  0.87       0.88    0.87      1960    
```
