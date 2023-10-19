---
layout: model
title: Detect PHI for Deidentification (LangTest - Generic - Augmented)
author: John Snow Labs
name: ner_deid_generic_augmented_langtest
date: 2023-09-26
tags: [en, ner, clinical, deid, licensed, langtest]
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

Named Entity recognition annotator allows for a generic model to be trained by utilizing a deep learning algorithm (Char CNNs - BiLSTM - CRF - word embeddings) inspired by a former state-of-the-art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM, CNN. Deidentification NER (Generic-Augmented) is a Named Entity Recognition model that annotates text to find protected health information that may need to be de-identified. It detects 7 entities. This ner model is trained with a combination of the i2b2 train set and an augmented version of the i2b2 train set.  It is the version of [ner_deid_generic_augmented](https://nlp.johnsnowlabs.com/2021/06/01/ner_deid_generic_augmented_en.html) model augmented with `langtest` library.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**     | 376                   | 369                  | 11927                 | 11934                | 95%                   | 97%                  | 97%                 |
| **lowercase**        | 1008                  | 350                  | 15138                 | 15796                | 95%                   | 94%                  | 98%                 |
| **swap_entities**    | 394                   | 350                  | 3687                  | 3733                 | 95%                   | 90%                  | 91%                 |
| **titlecase**        | 437                   | 352                  | 16970                 | 17055                | 95%                   | 97%                  | 98%                 |
| **uppercase**        | 1085                  | 506                  | 16198                 | 16777                | 95%                   | 94%                  | 97%                 |
| **weighted average** | **3300**              | **1927**             | **63920**             | **65295**            | **95%**               | **95.09%**           | 97.13%              |

We stuck to the official annotation guideline (AG) for the 2014 i2b2 Deid challenge while annotating new datasets for this model. All the details regarding the nuances and explanations for AG can be found here [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4978170/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4978170/)

## Predicted Entities

`DATE`, `NAME`, `LOCATION`, `PROFESSION`, `CONTACT`, `AGE`, `ID`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_augmented_langtest_en_5.1.0_3.0_1695730996506.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_augmented_langtest_en_5.1.0_3.0_1695730996506.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

deid_ner = MedicalNerModel.pretrained("ner_deid_generic_augmented_langtest", "en", "clinical/models") \
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

results = model.transform(spark.createDataFrame(pd.DataFrame({"text": ["""A. Record date : 2093-01-13, David Hale, M.D., Name : Hendrickson, Ora MR. # 7194334 Date : 01/13/93 PCP : Oliveira, 25 -year-old, Record date : 1-11-2000. Cocke County Baptist Hospital. 0295 Keats Street. Phone : (302) 786-5227."""]})))
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

val deid_ner = MedicalNerModel.pretrained("ner_deid_generic_augmented_langtest", "en", "clinical/models")
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

val data = Seq("""A. Record date : 2093-01-13, David Hale, M.D., Name : Hendrickson, Ora MR. # 7194334 Date : 01/13/93 PCP : Oliveira, 25 -year-old, Record date : 1-11-2000. Cocke County Baptist Hospital. 0295 Keats Street. Phone : (302) 786-5227.""").toDS.toDF("text")

val result = nlpPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------------+---------+
|chunk                        |ner_label|
+-----------------------------+---------+
|2093-01-13                   |DATE     |
|David Hale                   |NAME     |
|Hendrickson, Ora             |NAME     |
|7194334                      |ID       |
|01/13/93                     |DATE     |
|Oliveira                     |NAME     |
|25                           |AGE      |
|1-11-2000                    |DATE     |
|Cocke County Baptist Hospital|LOCATION |
|0295 Keats Street            |LOCATION |
|(302) 786-5227               |CONTACT  |
+-----------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_generic_augmented_langtest|
|Compatibility:|Healthcare NLP 5.1.0+|
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
AGE           0.96       0.95    0.96      395     
CONTACT       0.89       0.85    0.87      100     
DATE          0.98       0.98    0.98      2355    
ID            0.83       0.84    0.83      325     
LOCATION      0.85       0.87    0.86      756     
NAME          0.94       0.95    0.95      1314    
PROFESSION    0.55       0.69    0.61      113     
micro-avg     0.93       0.94    0.94      5358    
macro-avg     0.86       0.88    0.87      5358    
weighted-avg  0.93       0.94    0.94      5358    
```
