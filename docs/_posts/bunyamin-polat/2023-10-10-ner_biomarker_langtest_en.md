---
layout: model
title: Extraction of Biomarker Information (LangTest)
author: John Snow Labs
name: ner_biomarker_langtest
date: 2023-10-10
tags: [en, ner, licensed, clinical, biomarker, langtest]
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

This model is trained to extract biomarkers, therapies, oncological, and other general concepts from text. It is the version of [ner_biomarker](https://nlp.johnsnowlabs.com/2021/11/26/ner_biomarker_en.html) model augmented with `langtest` library.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**     | 1409                  | 589                  | 2209                  | 3029                 | 70%                   | 61%                  | 84%                 |
| **add_typo**         | 698                   | 647                  | 2937                  | 2966                 | 70%                   | 81%                  | 82%                 |
| **lowercase**        | 1913                  | 606                  | 1791                  | 3098                 | 70%                   | 48%                  | 84%                 |
| **titlecase**        | 2541                  | 953                  | 1227                  | 2815                 | 70%                   | 33%                  | 75%                 |
| **uppercase**        | 3515                  | 1111                 | 245                   | 2649                 | 70%                   | 7%                   | 70%                 |
| **weighted average** | **10076**             | **3906**             | **8409**              | **14557**            | **70%**               | **45.49%**           | **78.84%**          |

## Predicted Entities

`Oncogenes`, `Tumor_Finding`, `UnspecificTherapy`, `Ethnicity`, `Age`, `ResponseToTreatment`, `Biomarker`, `HormonalTherapy`, `Staging`, `Drug`, `CancerDx`, `Radiotherapy`, `CancerSurgery`, `TargetedTherapy`, `PerformanceStatus`, `CancerModifier`, `Radiological_Test_Result`, `Biomarker_Measurement`, `Metastasis`, `Radiological_Test`, `Chemotherapy`, `Test`, `Dosage`, `Test_Result`, `Immunotherapy`, `Date`, `Gender`, `Prognostic_Biomarkers`, `Duration`, `Predictive_Biomarkers`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_biomarker_langtest_en_5.1.1_3.0_1696945067061.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_biomarker_langtest_en_5.1.1_3.0_1696945067061.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings_clinical = WordEmbeddingsModel.pretrained('embeddings_clinical', 'en', 'clinical/models') \
    .setInputCols(['sentence', 'token']) \
    .setOutputCol('embeddings')

clinical_ner = MedicalNerModel.pretrained("ner_biomarker_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter()\
 	  .setInputCols(["sentence", "token", "ner"])\
 	  .setOutputCol("ner_chunk")
    
nlpPipeline = Pipeline(stages=[document_assembler, sentence_detector, tokenizer, embeddings_clinical,  clinical_ner, ner_converter])

model = nlpPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

result = model.transform(spark.createDataFrame([["Immunohistochemistry (IHC) showed that the primary metaplastic SCC was ER negative, PR negative, HER-2 positive (3+), EGFR (1+), CK5/6 (2+), 34βE12 (2+), P63 positive (the P63 positive cells were located around the cancer nest), P53 negative, SMMHC positive (1+), E-cadherin (2+), and Ki-67 was positive in 95% tumor cells."]], ["text"]))
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

val embeddings_clinical = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_biomarker_langtest", "en", "clinical/models") 
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
 	.setInputCols(Array("sentence", "token", "ner"))
 	.setOutputCol("ner_chunk")
    
val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, embeddings_clinical, ner, ner_converter))

val data = Seq("""Immunohistochemistry (IHC) showed that the primary metaplastic SCC was ER negative, PR negative, HER-2 positive (3+), EGFR (1+), CK5/6 (2+), 34βE12 (2+), P63 positive (the P63 positive cells were located around the cancer nest), P53 negative, SMMHC positive (1+), E-cadherin (2+), and Ki-67 was positive in 95% tumor cells.""").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------------+---------------------+
|chunk               |ner_label            |
+--------------------+---------------------+
|Immunohistochemistry|Test                 |
|IHC                 |Test                 |
|metaplastic         |CancerModifier       |
|SCC                 |CancerDx             |
|ER                  |Biomarker            |
|negative            |Biomarker_Measurement|
|PR                  |Biomarker            |
|negative            |Biomarker_Measurement|
|HER-2               |Biomarker            |
|positive            |Biomarker_Measurement|
|3+                  |Biomarker_Measurement|
|EGFR                |Oncogenes            |
|1+                  |Biomarker_Measurement|
|CK5/6               |Biomarker            |
|2+                  |Biomarker_Measurement|
|34βE12              |Biomarker            |
|2+                  |Biomarker_Measurement|
|P63                 |Biomarker            |
|positive            |Biomarker_Measurement|
|P63                 |Biomarker            |
|positive            |Biomarker_Measurement|
|cancer              |CancerDx             |
|P53                 |Biomarker            |
|negative            |Biomarker_Measurement|
|SMMHC               |Biomarker            |
|positive            |Biomarker_Measurement|
|1+                  |Biomarker_Measurement|
|E-cadherin          |Biomarker            |
|2+                  |Biomarker_Measurement|
|Ki-67               |Biomarker            |
|positive            |Biomarker_Measurement|
|95%                 |Biomarker_Measurement|
|tumor               |Tumor_Finding        |
+--------------------+---------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_biomarker_langtest|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.8 MB|

## References

Trained on data sampled from Mimic-III, and annotated in-house.

## Benchmarking

```bash
label                     precision  recall  f1-score  support 
Age                       0.81       0.93    0.87      46      
Biomarker                 0.80       0.84    0.82      3491    
Biomarker_Measurement     0.77       0.76    0.76      733     
CancerDx                  0.92       0.93    0.93      2873    
CancerModifier            0.77       0.84    0.80      1065    
CancerSurgery             0.84       0.88    0.86      282     
Chemotherapy              0.93       0.93    0.93      665     
Date                      0.86       0.74    0.80      136     
Dosage                    0.62       0.40    0.48      133     
Drug                      0.69       0.65    0.67      37      
Duration                  0.49       0.35    0.41      66      
Ethnicity                 0.67       1.00    0.80      6       
Gender                    0.76       0.86    0.80      84      
HormonalTherapy           0.84       0.84    0.84      135     
Immunotherapy             0.91       0.91    0.91      317     
Metastasis                0.93       0.91    0.92      568     
Oncogenes                 0.66       0.56    0.60      670     
PerformanceStatus         0.50       0.43    0.46      7       
Predictive_Biomarkers     0.00       0.00    0.00      1       
Prognostic_Biomarkers     0.41       0.20    0.27      64      
Radiological_Test         0.65       0.64    0.65      101     
Radiological_Test_Result  0.14       0.08    0.10      13      
Radiotherapy              0.93       0.93    0.93      177     
ResponseToTreatment       0.71       0.14    0.23      36      
Staging                   0.65       0.66    0.65      82      
TargetedTherapy           0.90       0.89    0.89      765     
Test                      0.68       0.68    0.68      445     
Test_Result               0.31       0.13    0.18      31      
Tumor_Finding             0.73       0.83    0.78      728     
UnspecificTherapy         0.69       0.82    0.75      79      
micro-avg                 0.82       0.83    0.83      13836   
macro-avg                 0.68       0.66    0.66      13836   
weighted-avg              0.82       0.83    0.82      13836   
```
