---
layout: model
title: Detect PHI for Deidentification (LangTest - Subentity - Augmented)
author: John Snow Labs
name: ner_deid_subentity_augmented_langtest
date: 2023-09-26
tags: [en, ner, clinical, deid, langtest, licensed]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.1.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Named Entity recognition annotator allows for a generic model to be trained by utilizing a deep learning algorithm (Char CNNs - BiLSTM - CRF - word embeddings) inspired by a former state-of-the-art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM, CNN. Deidentification NER is a Named Entity Recognition model that annotates text to find protected health information that may need to be de-identified. It detects 23 entities. This ner model is trained with a combination of the i2b2 train set and a re-augmented version of the i2b2 train set. It is the version of [ner_deid_subentity_augmented](https://nlp.johnsnowlabs.com/2021/09/03/ner_deid_subentity_augmented_en.html) model augmented with `langtest` library.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_typo**         | 306                   | 256                  | 17377                 | 17416                | 95%                   | 98%                  | 99%                 |
| **lowercase**        | 910                   | 336                  | 15226                 | 15800                | 95%                   | 94%                  | 98%                 |
| **swap_entities**    | 358                   | 322                  | 3688                  | 3734                 | 95%                   | 91%                  | 92%                 |
| **titlecase**        | 396                   | 237                  | 17014                 | 17173                | 95%                   | 98%                  | 99%                 |
| **uppercase**        | 1096                  | 500                  | 16262                 | 16858                | 95%                   | 94%                  | 97%                 |
| **weighted average** | **3066**              | **1651**             | **69567**             | **70981**            | **95%**               | **95.78%**           | **97.73%**          |

We stuck to the official annotation guideline (AG) for the 2014 i2b2 Deid challenge while annotating new datasets for this model. All the details regarding the nuances and explanations for AG can be found here [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4978170/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4978170/)

## Predicted Entities

`MEDICALRECORD`, `ORGANIZATION`, `DOCTOR`, `USERNAME`, `PROFESSION`, `HEALTHPLAN`, `URL`, `CITY`, `DATE`, `LOCATION-OTHER`, `STATE`, `PATIENT`, `DEVICE`, `COUNTRY`, `ZIP`, `PHONE`, `HOSPITAL`, `EMAIL`, `IDNUM`, `STREET`, `BIOID`, `FAX`, `AGE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_augmented_langtest_en_5.1.0_3.0_1695732332957.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_augmented_langtest_en_5.1.0_3.0_1695732332957.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

deid_ner = MedicalNerModel.pretrained("ner_deid_subentity_augmented_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk_subentity")

nlpPipeline = Pipeline(stages=[
                    document_assembler, 
                    sentence_detector, 
                    tokenizer, 
                    word_embeddings, 
                    deid_ner, 
                    ner_converter])

model = nlpPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

results = model.transform(spark.createDataFrame(pd.DataFrame({"text": ["""A. Record date : 2093-01-13, David Hale, M.D., Name : Hendrickson, Ora MR. # 7194334 Date : 01/13/93 PCP : Oliveira, 25-year-old, Record date : 1-11-2000. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 (302) 786-5227. Patient's complaints first surfaced when he started working for Brothers Coal-Mine."""]})))
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

val deid_ner = MedicalNerModel.pretrained("ner_deid_subentity_augmented_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk_subentity")

val nlpPipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector, 
    tokenizer, 
    word_embeddings, 
    deid_ner, 
    ner_converter))

val data = Seq("""A. Record date : 2093-01-13, David Hale, M.D., Name : Hendrickson, Ora MR. # 7194334 Date : 01/13/93 PCP : Oliveira, 25-year-old, Record date : 1-11-2000. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 (302) 786-5227. Patient's complaints first surfaced when he started working for Brothers Coal-Mine.""").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------------+-------------+
|chunk                        |ner_label    |
+-----------------------------+-------------+
|2093-01-13                   |DATE         |
|David Hale                   |DOCTOR       |
|Hendrickson, Ora             |PATIENT      |
|7194334                      |MEDICALRECORD|
|01/13/93                     |DATE         |
|Oliveira                     |DOCTOR       |
|25-year-old                  |AGE          |
|1-11-2000                    |DATE         |
|Cocke County Baptist Hospital|HOSPITAL     |
|0295 Keats Street            |STREET       |
|(302) 786-5227               |PHONE        |
|Brothers Coal-Mine           |ORGANIZATION |
+-----------------------------+-------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_subentity_augmented_langtest|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.8 MB|

## References

A custom data set which is created from the i2b2-PHI train and the re-augmented version of the i2b2-PHI train set is used.

## Benchmarking

```bash
label           precision  recall  f1-score  support 
AGE             0.96       0.93    0.94      377     
BIOID           0.00       0.00    0.00      1       
CITY            0.89       0.82    0.85      104     
COUNTRY         0.88       0.86    0.87      57      
DATE            0.98       0.99    0.99      2375    
DEVICE          0.83       0.71    0.77      7       
DOCTOR          0.96       0.91    0.93      918     
FAX             0.00       0.00    0.00      2       
HOSPITAL        0.90       0.91    0.90      410     
IDNUM           0.83       0.66    0.74      83      
LOCATION-OTHER  0.50       0.75    0.60      8       
MEDICALRECORD   0.91       0.97    0.94      164     
ORGANIZATION    0.78       0.63    0.70      57      
PATIENT         0.85       0.92    0.89      408     
PHONE           0.93       0.88    0.91      112     
PROFESSION      0.84       0.80    0.82      97      
STATE           0.94       0.92    0.93      73      
STREET          0.87       0.95    0.91      77      
USERNAME        0.96       0.90    0.93      52      
ZIP             0.96       1.00    0.98      45      
micro-avg       0.94       0.94    0.94      5427    
macro-avg       0.79       0.78    0.78      5427    
weighted-avg    0.94       0.94    0.94      5427    
```
