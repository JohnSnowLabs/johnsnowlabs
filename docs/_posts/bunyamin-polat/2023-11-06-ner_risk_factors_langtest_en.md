---
layout: model
title: Detect Risk Factors (LangTest)
author: John Snow Labs
name: ner_risk_factors_langtest
date: 2023-11-06
tags: [en, ner, clinical, licensed, langtest]
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

Pretrained named entity recognition deep learning model for Heart Disease Risk Factors and Personal Health Information. It is the version of [ner_risk_factors](https://nlp.johnsnowlabs.com/2021/03/31/ner_risk_factors_en.html) model augmented with `langtest` library.

## Predicted Entities

`CAD`, `DIABETES`, `FAMILY_HIST`, `HYPERLIPIDEMIA`, `HYPERTENSION`, `MEDICATION`, `OBESE`, `PHI`, `SMOKER`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_risk_factors_langtest_en_5.1.1_3.0_1699259077185.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_risk_factors_langtest_en_5.1.1_3.0_1699259077185.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

clinical_ner = MedicalNerModel.pretrained("ner_risk_factors_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter()\
 	.setInputCols(["sentence", "token", "ner"])\
 	.setOutputCol("ner_chunk")

nlp_pipeline = Pipeline(stages=[document_assembler, sentence_detector, tokenizer, word_embeddings, clinical_ner, ner_converter])

model = nlp_pipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

result = model.transform(spark.createDataFrame([["""PAST SURGICAL HISTORY: She has also had a hysterectomy, salpingoophorectomy, appendectomy, tonsillectomy, two carpal tunnel releases. She also has had a parathyroidectomy but still has had some borderline elevated calcium. Also, hypertension, hyperlipidemia, as well as diabetes. She also has osteoporosis.

SOCIAL HISTORY: The patient still smokes about a third of a pack a day, also drinks only occasional alcoholic drinks. The patient is married. She has three grown sons, all of which are very successful in professional positions. One son is a gastroenterologist in San Diego, California.

MEDICATIONS: Nifedipine-XR 90 mg daily, furosemide 20 mg half tablet b.i.d., lisinopril 20 mg daily, gemfibrozil 600 mg b.i.d., Synthroid 0.1 mg daily, Miacalcin one spray in alternate nostrils daily, Ogen 0.625 mg daily, Daypro 600 mg t.i.d., also Lortab 7.5 two or three a day, also Flexeril occasionally, also other vitamin.

ALLERGIES: She had some adverse reactions to penicillin, sulfa, perhaps contrast medium, and some mycins."""]], ["text"]))
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

val ner = MedicalNerModel.pretrained("ner_risk_factors_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
 	.setInputCols(Array("sentence", "token", "ner"))
 	.setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, ner, ner_converter))

val data = Seq("""PAST SURGICAL HISTORY: She has also had a hysterectomy, salpingoophorectomy, appendectomy, tonsillectomy, two carpal tunnel releases. She also has had a parathyroidectomy but still has had some borderline elevated calcium. Also, hypertension, hyperlipidemia, as well as diabetes. She also has osteoporosis.

SOCIAL HISTORY: The patient still smokes about a third of a pack a day, also drinks only occasional alcoholic drinks. The patient is married. She has three grown sons, all of which are very successful in professional positions. One son is a gastroenterologist in San Diego, California.

MEDICATIONS: Nifedipine-XR 90 mg daily, furosemide 20 mg half tablet b.i.d., lisinopril 20 mg daily, gemfibrozil 600 mg b.i.d., Synthroid 0.1 mg daily, Miacalcin one spray in alternate nostrils daily, Ogen 0.625 mg daily, Daypro 600 mg t.i.d., also Lortab 7.5 two or three a day, also Flexeril occasionally, also other vitamin.

ALLERGIES: She had some adverse reactions to penicillin, sulfa, perhaps contrast medium, and some mycins.""").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------------------------------+--------------+
|chunk                                     |ner_label     |
+------------------------------------------+--------------+
|hypertension                              |HYPERTENSION  |
|hyperlipidemia                            |HYPERLIPIDEMIA|
|diabetes                                  |DIABETES      |
|still smokes about a third of a pack a day|SMOKER        |
|San Diego                                 |PHI           |
|California                                |PHI           |
|lisinopril                                |MEDICATION    |
|gemfibrozil                               |MEDICATION    |
+------------------------------------------+--------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_risk_factors_langtest|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.7 MB|

## References

Trained on plain n2c2 2014: De-identification and Heart Disease Risk Factors Challenge datasets with `embeddings_clinical`. https://portal.dbmi.hms.harvard.edu/projects/n2c2-2014/

## Benchmarking

```bash
label             precision  recall  f1-score  support 
B-CAD             0.55       0.48    0.51      183     
B-DIABETES        0.74       0.80    0.77      246     
B-FAMILY_HIST     0.00       0.00    0.00      3       
B-HYPERLIPIDEMIA  0.85       0.89    0.87      95      
B-HYPERTENSION    0.73       0.81    0.77      233     
B-MEDICATION      0.84       0.85    0.84      894     
B-OBESE           0.69       0.82    0.75      49      
B-PHI             0.81       0.80    0.81      2106    
B-SMOKER          0.66       0.19    0.30      118     
I-CAD             0.38       0.36    0.37      476     
I-DIABETES        0.59       0.59    0.59      214     
I-FAMILY_HIST     0.83       0.29    0.43      17      
I-HYPERLIPIDEMIA  0.55       0.35    0.43      17      
I-HYPERTENSION    0.24       0.31    0.27      108     
I-MEDICATION      0.73       0.20    0.31      347     
I-OBESE           0.23       0.43    0.30      7       
I-PHI             0.79       0.72    0.75      618     
I-SMOKER          0.74       0.30    0.43      220     
micro-avg         0.73       0.67    0.70      5951    
macro-avg         0.61       0.51    0.53      5951    
weighted-avg      0.73       0.67    0.69      5951   
```