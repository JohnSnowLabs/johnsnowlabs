---
layout: model
title: Detect Problems, Tests and Treatments (LangTest)
author: John Snow Labs
name: ner_clinical_langtest
date: 2023-09-26
tags: [en, ner, clinical, licensed, langtest]
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

Pretrained named entity recognition deep learning model for clinical terms. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state-of-the-art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN. It is the version of [ner_clinical](https://nlp.johnsnowlabs.com/2020/01/30/ner_clinical_en.html) model augmented with `langtest` library.

| **test_type**         | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|-----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**      | 470                   | 154                  | 635                   | 951                  | 80%                   | 57%                  | 86%                 |
| **lowercase**         | 174                   | 150                  | 1308                  | 1332                 | 80%                   | 88%                  | 90%                 |
| **strip_punctuation** | 49                    | 32                   | 1190                  | 1207                 | 80%                   | 96%                  | 97%                 |
| **titlecase**         | 421                   | 297                  | 1012                  | 1136                 | 70%                   | 71%                  | 79%                 |
| **uppercase**         | 763                   | 379                  | 615                   | 999                  | 70%                   | 45%                  | 72%                 |
| **weighted average**  | **1877**              | **1012**             | **4760**              | **5625**             | **76%**               | **71.72%**           | **84.75%**          |

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_langtest_en_5.1.0_3.0_1695735000637.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_langtest_en_5.1.0_3.0_1695735000637.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\ 
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner = MedicalNerModel.pretrained("ner_clinical_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter])

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, and associated with an acute hepatitis, presented with a one-week history of polyuria, poor appetite, and vomiting. She was on metformin, glipizide, and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG. She had been on dapagliflozin for six months at the time of presentation. Physical examination on presentation was significant for dry oral mucosa ; significantly , her abdominal examination was benign with no tenderness, guarding, or rigidity. Pertinent laboratory findings on admission were: serum glucose 111 mg/dl,  creatinine 0.4 mg/dL, triglycerides 508 mg/dL, total cholesterol 122 mg/dL, and venous pH 7.27."""]]).toDF("text")

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

val ner = MedicalNerModel.pretrained("ner_clinical_langtest", "en", "clinical/models")
        .setInputCols(Array("sentence", "token", "embeddings"))
        .setOutputCol("ner")

val ner_converter = new NerConverter()
   	    .setInputCols(Array("sentence", "token", "ner"))
   	    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, ner, ner_converter))

val data = Seq("""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, and associated with an acute hepatitis, presented with a one-week history of polyuria, poor appetite, and vomiting. She was on metformin, glipizide, and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG. She had been on dapagliflozin for six months at the time of presentation. Physical examination on presentation was significant for dry oral mucosa ; significantly , her abdominal examination was benign with no tenderness, guarding, or rigidity. Pertinent laboratory findings on admission were: serum glucose 111 mg/dl,  creatinine 0.4 mg/dL, triglycerides 508 mg/dL, total cholesterol 122 mg/dL, and venous pH 7.27.""").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------------------------+---------+
|chunk                               |ner_label|
+------------------------------------+---------+
|gestational diabetes mellitus       |PROBLEM  |
|type two diabetes mellitus          |PROBLEM  |
|T2DM                                |PROBLEM  |
|HTG-induced pancreatitis            |PROBLEM  |
|an acute hepatitis                  |PROBLEM  |
|polyuria                            |PROBLEM  |
|poor appetite                       |PROBLEM  |
|vomiting                            |PROBLEM  |
|metformin                           |TREATMENT|
|glipizide                           |TREATMENT|
|dapagliflozin                       |TREATMENT|
|T2DM                                |PROBLEM  |
|atorvastatin                        |TREATMENT|
|gemfibrozil                         |TREATMENT|
|HTG                                 |PROBLEM  |
|dapagliflozin                       |TREATMENT|
|Physical examination on presentation|TEST     |
|dry oral mucosa                     |PROBLEM  |
|her abdominal examination           |TEST     |
|tenderness                          |PROBLEM  |
|guarding                            |PROBLEM  |
|rigidity                            |PROBLEM  |
|serum glucose                       |TEST     |
|creatinine                          |TEST     |
|triglycerides                       |TEST     |
|total cholesterol                   |TEST     |
|venous pH                           |TEST     |
+------------------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical_langtest|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.5 MB|

## References

Trained on augmented version of 2010 [i2b2](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/) challenge data with ‘embeddings_clinical’. https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/

## Benchmarking

```bash
label         precision  recall  f1-score  support 
PROBLEM       0.85       0.86    0.86      1085    
TEST          0.89       0.87    0.88      717     
TREATMENT     0.87       0.85    0.86      667     
micro-avg     0.87       0.86    0.86      2469    
macro-avg     0.87       0.86    0.86      2469    
weighted-avg  0.87       0.86    0.86      2469    
```
