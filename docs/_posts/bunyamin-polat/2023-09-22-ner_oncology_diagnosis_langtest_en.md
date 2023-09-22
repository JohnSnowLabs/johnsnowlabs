---
layout: model
title: Detect Entities Related to Cancer Diagnosis (LangTest)
author: John Snow Labs
name: ner_oncology_diagnosis_langtest
date: 2023-09-22
tags: [en, ner, clinical, licensed, oncology, diagnosis, langtest]
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

This model extracts entities related to cancer diagnosis, such as Metastasis, Histological_Type, or Invasion. It is the version of [ner_oncology_diagnosis](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_diagnosis_en.html) model augmented with `langtest` library.

Definitions of Predicted Entities:

- `Adenopathy`: Mentions of pathological findings of the lymph nodes.
- `Cancer_Dx`: Mentions of cancer diagnoses (such as "breast cancer") or pathological types that are usually used as synonyms for "cancer" (e.g. "carcinoma"). When anatomical references are present, they are included in the Cancer_Dx extraction.
- `Cancer_Score`: Clinical or imaging scores that are specific for cancer settings (e.g. "BI-RADS" or "Allred score").
- `Grade`: All pathological grading of tumors (e.g. "grade 1") or degrees of cellular differentiation (e.g. "well-differentiated")
- `Histological_Type`: Histological variants or cancer subtypes, such as "papillary", "clear cell" or "medullary". 
- `Invasion`: Mentions that refer to tumor invasion, such as "invasion" or "involvement". Metastases or lymph node involvement are excluded from this category.
- `Metastasis`: Terms that indicate a metastatic disease. Anatomical references are not included in these extractions.
- `Pathology_Result`: The findings of a biopsy from the pathology report that is not covered by another entity (e.g. "malignant ductal cells").
- `Performance_Status`: Mentions of performance status scores, such as ECOG and Karnofsky. The name of the score is extracted together with the result (e.g. "ECOG performance status of 4").
- `Staging`: Mentions of cancer stage such as "stage 2b" or "T2N1M0". It also includes words such as "in situ", "early-stage" or "advanced".
- `Tumor_Finding`: All nonspecific terms that may be related to tumors, either malignant or benign (for example: "mass", "tumor", "lesion", or "neoplasm").
- `Tumor_Size`: Size of the tumor, including numerical value and unit of measurement (e.g. "3 cm").

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_punctuation**  | 4                     | 3                    | 183                   | 184                  | 60%                   | 98%                  | 98%                 |
| **swap_entities**    | 272                   | 276                  | 1241                  | 1252                 | 60%                   | 82%                  | 82%                 |
| **titlecase**        | 910                   | 834                  | 3592                  | 3668                 | 80%                   | 80%                  | 81%                 |
| **uppercase**        | 1768                  | 606                  | 2747                  | 3909                 | 80%                   | 61%                  | 87%                 |
| **weighted average** | **2954**              | **1719**             | **7763**              | **9013**             | **70%**               | **72.44%**           | **83.98%**          |

## Predicted Entities

`Adenopathy`, `Cancer_Dx`, `Cancer_Score`, `Grade`, `Histological_Type`, `Invasion`, `Metastasis`, `Pathology_Result`, `Performance_Status`, `Staging`, `Tumor_Finding`, `Tumor_Size`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_diagnosis_langtest_en_5.1.0_3.0_1695393811887.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_diagnosis_langtest_en_5.1.0_3.0_1695393811887.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_oncology_diagnosis_langtest", "en", "clinical/models") \
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

data = spark.createDataFrame([["Two years ago, the patient presented with a tumor in her left breast and adenopathies. She was diagnosed with invasive ductal carcinoma. Last week she was also found to have a lung metastasis."]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
    
val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")
    
val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")
    
val word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                
    
val ner = MedicalNerModel.pretrained("ner_oncology_diagnosis_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")
    
val ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

        
val pipeline = new Pipeline().setStages(Array(document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter))    

val data = Seq("Two years ago, the patient presented with a tumor in her left breast and adenopathies. She was diagnosed with invasive ductal carcinoma. Last week she was also found to have a lung metastasis.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------+-----------------+
|chunk       |ner_label        |
+------------+-----------------+
|tumor       |Tumor_Finding    |
|adenopathies|Adenopathy       |
|invasive    |Histological_Type|
|ductal      |Histological_Type|
|carcinoma   |Cancer_Dx        |
|metastasis  |Metastasis       |
+------------+-----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_diagnosis_langtest|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.8 MB|

## References

In-house annotated oncology case reports.

## Benchmarking

```bash
label               precision  recall  f1-score  support 
Adenopathy          0.65       0.82    0.73      34      
Cancer_Dx           0.85       0.95    0.90      721     
Cancer_Score        0.86       0.64    0.73      28      
Grade               0.57       0.73    0.64      82      
Histological_Type   0.73       0.87    0.79      242     
Invasion            0.79       0.94    0.86      172     
Metastasis          0.82       0.98    0.89      321     
Pathology_Result    0.44       0.70    0.54      348     
Performance_Status  0.33       0.94    0.49      31      
Staging             0.90       0.94    0.92      123     
Tumor_Finding       0.87       0.94    0.90      1018    
Tumor_Size          0.68       0.93    0.78      216     
micro-avg           0.75       0.91    0.82      3336    
macro-avg           0.71       0.87    0.77      3336    
weighted-avg        0.77       0.91    0.83      3336    
```