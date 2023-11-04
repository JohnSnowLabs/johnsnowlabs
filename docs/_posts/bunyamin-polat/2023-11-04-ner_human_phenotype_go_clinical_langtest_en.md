---
layout: model
title: Detect Normalized Genes and Human Phenotypes (LangTest)
author: John Snow Labs
name: ner_human_phenotype_go_clinical_langtest
date: 2023-11-04
tags: [en, ner, clinical, licensed, langtest, human, phenotype]
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

This model can be used to detect normalized mentions of genes (go) and human phenotypes (hp) in medical text. It is the version of [ner_human_phenotype_go_clinical](https://nlp.johnsnowlabs.com/2021/03/31/ner_human_phenotype_go_clinical_en.html) model augmented with `langtest` library.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_abbreviation** | 116                   | 53                   | 475                   | 538                  | 85%                   | 80%                  | 91%                 |
| **add_ocr_typo**     | 517                   | 93                   | 192                   | 616                  | 70%                   | 27%                  | 87%                 |
| **add_typo**         | 201                   | 92                   | 480                   | 594                  | 75%                   | 70%                  | 87%                 |
| **lowercase**        | 71                    | 44                   | 622                   | 649                  | 90%                   | 90%                  | 94%                 |
| **titlecase**        | 701                   | 123                  | 8                     | 586                  | 70%                   | 1%                   | 83%                 |
| **uppercase**        | 707                   | 186                  | 2                     | 523                  | 70%                   | 0%                   | 74%                 |
| **weighted average** | **2313**              | **591**              | **1779**              | **3506**             | **77%**               | **43.48%**           | **85.57%**          |

## Predicted Entities

`GO`, `HP`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_human_phenotype_go_clinical_langtest_en_5.1.1_3.0_1699113634845.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_human_phenotype_go_clinical_langtest_en_5.1.1_3.0_1699113634845.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
	
```python
document_assembler = DocumentAssembler()\
	.setInputCol("text")\
	.setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
	.setInputCols(["document"]) \
	.setOutputCol("sentence")

tokenizer = Tokenizer()\
	.setInputCols(["sentence"])\
	.setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
	.setInputCols(["sentence", "token"])\
	.setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_human_phenotype_go_clinical_langtest", "en", "clinical/models") \
	.setInputCols(["sentence", "token", "embeddings"]) \
	.setOutputCol("ner")

ner_converter = NerConverter() \
	.setInputCols(["sentence", "token", "ner"]) \
	.setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            clinical_ner,
                            ner_converter])

data = spark.createDataFrame([["""Another disease that shares two of the tumor components of CT, namely GIST and the tricarboxylic acid cycle is the Carney-Stratakis syndrome (CSS) or dyad."""]]).toDF("text")

result = pipeline.fit(data).transform(data)
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

val ner = MedicalNerModel.pretrained("ner_human_phenotype_go_clinical_langtest", "en", "clinical/models")
	.setInputCols(Array("sentence", "token", "embeddings"))
	.setOutputCol("ner")

val ner_converter = new NerConverter()
	.setInputCols(Array("sentence", "token", "ner"))
	.setOutputCol("entities")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, ner, ner_converter))

val data = Seq("Another disease that shares two of the tumor components of CT, namely GIST and tricarboxylic acid cycle is the Carney-Stratakis syndrome (CSS) or dyad.").toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------------+---------+
|chunk                   |ner_label|
+------------------------+---------+
|tumor                   |HP       |
|tricarboxylic acid cycle|GO       |
+------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_human_phenotype_go_clinical_langtest|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.6 MB|

## Benchmarking

```bash
label         precision  recall  f1-score  support 
GO            0.89       0.81    0.85      1363    
HP            0.84       0.85    0.85      762     
micro-avg     0.87       0.82    0.85      2125    
macro-avg     0.86       0.83    0.85      2125    
weighted-avg  0.87       0.82    0.85      2125    
```
