---
layout: model
title: Detect PHI for Deidentification (LangTest - Generic Augmented - UpperCased)
author: John Snow Labs
name: ner_deid_generic_augmented_allUpperCased_langtest
date: 2023-10-16
tags: [en, ner, clinical, licensed, deid, uppercase, langtest]
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

The `ner_deid_generic_augmented_allUpperCased_langtest` model is a Named Entity Recognition model that annotates text to find protected health information that may need to be de-identified. This NER model is trained and augmented with the "langtest" library. The dataset is an uppercased version of the i2b2 train set and augmented i2b2 train set.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**     | 426                   | 399                  | 11877                 | 11904                | 95%                   | 97%                  | 97%                 |
| **add_typo**         | 246                   | 244                  | 17400                 | 17426                | 95%                   | 99%                  | 99%                 |
| **lowercase**        | 1508                  | 352                  | 17150                 | 18306                | 95%                   | 92%                  | 98%                 |
| **swap_entities**    | 394                   | 381                  | 3688                  | 3708                 | 95%                   | 90%                  | 91%                 |
| **titlecase**        | 1181                  | 334                  | 17346                 | 18193                | 95%                   | 94%                  | 98%                 |
| **weighted average** | **3755**              | **1710**             | **67461**             | **69537**            | **95%**               | **94.73%**           | **97.60%**          |

## Predicted Entities

`DATE`, `NAME`, `LOCATION`, `PROFESSION`, `CONTACT`, `AGE`, `ID`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_augmented_allUpperCased_langtest_en_5.1.1_3.0_1697454771302.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_augmented_allUpperCased_langtest_en_5.1.1_3.0_1697454771302.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

deid_ner = MedicalNerModel.pretrained("ner_deid_generic_augmented_allUpperCased_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk_generic")

nlpPipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector, 
    tokenizer, 
    word_embeddings, 
    deid_ner, 
    ner_converter])

model = nlpPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

results = model.transform(spark.createDataFrame(pd.DataFrame({"text": ["""A. RECORD DATE : 2093-01-13, DAVID HALE, M.D., NAME : HENDRICKSON, ORA MR. # 7194334 DATE : 01/13/93 PCP : OLIVEIRA, 25 -YEAR-OLD, RECORD DATE : 1-11-2000. COCKE COUNTY BAPTIST HOSPITAL. 0295 KEATS STREET. PHONE : (302) 786-5227.""]})))
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

val deid_ner = MedicalNerModel.pretrained("ner_deid_generic_augmented_allUpperCased_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk_generic")

val nlpPipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector, 
    tokenizer, 
    word_embeddings, 
    deid_ner, 
    ner_converter))

val data = Seq("""A. RECORD DATE : 2093-01-13, DAVID HALE, M.D., NAME : HENDRICKSON, ORA MR. # 7194334 DATE : 01/13/93 PCP : OLIVEIRA, 25 -YEAR-OLD, RECORD DATE : 1-11-2000. COCKE COUNTY BAPTIST HOSPITAL. 0295 KEATS STREET. PHONE : (302) 786-5227.""").toDS.toDF("text")

val result = nlpPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------------+---------+
|chunk                        |ner_label|
+-----------------------------+---------+
|2093-01-13                   |DATE     |
|DAVID HALE                   |NAME     |
|HENDRICKSON, ORA             |NAME     |
|7194334                      |ID       |
|01/13/93                     |DATE     |
|OLIVEIRA                     |NAME     |
|25                           |AGE      |
|1-11-2000                    |DATE     |
|COCKE COUNTY BAPTIST HOSPITAL|LOCATION |
|0295 KEATS STREET            |LOCATION |
|(302) 786-5227               |CONTACT  |
+-----------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_generic_augmented_allUpperCased_langtest|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.7 MB|

## References

A custom data set which is created from the i2b2-PHI train and the augmented version of the i2b2-PHI train set is used.

## Benchmarking

```bash
label         precision  recall  f1-score  support 
AGE           0.95       0.95    0.95      395     
CONTACT       0.93       0.86    0.90      100     
DATE          0.98       0.98    0.98      2355    
ID            0.84       0.80    0.82      325     
LOCATION      0.85       0.82    0.84      756     
NAME          0.93       0.94    0.94      1314    
PROFESSION    0.62       0.53    0.57      113     
micro-avg     0.93       0.93    0.93      5358    
macro-avg     0.87       0.84    0.86      5358    
weighted-avg  0.93       0.93    0.93      5358    
```
