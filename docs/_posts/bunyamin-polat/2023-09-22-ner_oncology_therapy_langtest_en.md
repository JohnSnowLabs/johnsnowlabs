---
layout: model
title: Detect Entities Related to Cancer Therapies (LangTest)
author: John Snow Labs
name: ner_oncology_therapy_langtest
date: 2023-09-22
tags: [en, ner, clinical, licensed, oncology, therapy, langtest]
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

This model extracts entities related to oncology therapies using granular labels, including mentions of treatments, posology information, and line of therapy. It is the version of [ner_oncology_therapy](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_therapy_en.html) model augmented with `langtest` library.

Definitions of Predicted Entities:

- `Cancer_Surgery`: Terms that indicate surgery as a form of cancer treatment.
- `Chemotherapy`: Mentions of chemotherapy drugs, or unspecific words such as "chemotherapy".
- `Cycle_Count`: The total number of cycles being administered of an oncological therapy (e.g. "5 cycles"). 
- `Cycle_Day`: References to the day of the cycle of oncological therapy (e.g. "day 5").
- `Cycle_Number`: The number of the cycle of an oncological therapy that is being applied (e.g. "third cycle").
- `Dosage`: The quantity prescribed by the physician for an active ingredient.
- `Duration`: Words indicating the duration of a treatment (e.g. "for 2 weeks").
- `Frequency`: Words indicating the frequency of treatment administration (e.g. "daily" or "bid").
- `Hormonal_Therapy`: Mentions of hormonal drugs used to treat cancer, or unspecific words such as "hormonal therapy".
- `Immunotherapy`: Mentions of immunotherapy drugs, or unspecific words such as "immunotherapy".
- `Line_Of_Therapy`: Explicit references to the line of therapy of an oncological therapy (e.g. "first-line treatment").
- `Radiotherapy`: Terms that indicate the use of Radiotherapy.
- `Radiation_Dose`: Dose used in radiotherapy.
- `Response_To_Treatment`: Terms related to the clinical progress of the patient related to cancer treatment, including "recurrence", "bad response" or "improvement".
- `Route`: Words indicating the type of administration route (such as "PO" or "transdermal").
- `Targeted_Therapy`: Mentions of targeted therapy drugs, or unspecific words such as "targeted therapy".
- `Unspecific_Therapy`: Terms that indicate a known cancer therapy but that is not specific to any other therapy entity (e.g. "chemoradiotherapy" or "adjuvant therapy").

| **test_type**             | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|---------------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**          | 725                   | 279                  | 617                   | 1063                 | 70%                   | 46%                  | 79%                 |
| **add_typo**              | 248                   | 152                  | 1066                  | 1169                 | 70%                   | 81%                  | 88%                 |
| **lowercase**             | 214                   | 152                  | 1152                  | 1214                 | 70%                   | 84%                  | 89%                 |
| **strip_all_punctuation** | 223                   | 228                  | 1128                  | 1123                 | 70%                   | 83%                  | 83%                 |
| **strip_punctuation**     | 50                    | 37                   | 1270                  | 1283                 | 70%                   | 96%                  | 97%                 |
| **titlecase**             | 764                   | 288                  | 603                   | 1079                 | 70%                   | 44%                  | 79%                 |
| **uppercase**             | 1320                  | 233                  | 48                    | 1135                 | 70%                   | 4%                   | 83%                 |
| **weighted average**      | **2571**              | **938**              | **4201**              | **5834**             | **70%**               | **62.03%**           | **86.15%**          |

## Predicted Entities

`Cancer_Surgery`, `Chemotherapy`, `Cycle_Count`, `Cycle_Day`, `Cycle_Number`, `Dosage`, `Duration`, `Frequency`, `Hormonal_Therapy`, `Immunotherapy`, `Line_Of_Therapy`, `Radiotherapy`, `Radiation_Dose`, `Response_To_Treatment`, `Route`, `Targeted_Therapy`, `Unspecific_Therapy`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_therapy_langtest_en_5.1.0_3.0_1695389309847.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_therapy_langtest_en_5.1.0_3.0_1695389309847.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_oncology_therapy_langtest", "en", "clinical/models") \
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

data = spark.createDataFrame([["The had previously undergone a left mastectomy and an axillary lymph node dissection for a left breast cancer twenty years ago.
The tumor was positive for ER and PR. Postoperatively, radiotherapy was administered to her breast.
The cancer recurred as a right lung metastasis 13 years later. The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses, as first line therapy."]]).toDF("text")

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
    
val ner = MedicalNerModel.pretrained("ner_oncology_therapy_langtest", "en", "clinical/models")
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

val data = Seq("The had previously undergone a left mastectomy and an axillary lymph node dissection for a left breast cancer twenty years ago.
The tumor was positive for ER and PR. Postoperatively, radiotherapy was administered to her breast.
The cancer recurred as a right lung metastasis 13 years later. The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses, as first line therapy.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------------------+---------------------+
|chunk                         |ner_label            |
+------------------------------+---------------------+
|mastectomy                    |Cancer_Surgery       |
|axillary lymph node dissection|Cancer_Surgery       |
|PR                            |Response_To_Treatment|
|radiotherapy                  |Radiotherapy         |
|recurred                      |Response_To_Treatment|
|adriamycin                    |Chemotherapy         |
|60 mg/m2                      |Chemotherapy         |
|cyclophosphamide              |Chemotherapy         |
|600 mg/m2                     |Chemotherapy         |
|six courses                   |Cycle_Count          |
|first line                    |Line_Of_Therapy      |
+------------------------------+---------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_therapy_langtest|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.7 MB|

## References

In-house annotated oncology case reports.

## Benchmarking

```bash
label                  precision  recall  f1-score  support 
Cancer_Surgery         0.85       0.85    0.85      490     
Chemotherapy           0.92       0.93    0.92      637     
Cycle_Count            0.78       0.85    0.82      128     
Cycle_Day              0.66       0.71    0.68      68      
Cycle_Number           0.75       0.58    0.65      52      
Dosage                 0.91       0.91    0.91      311     
Duration               0.80       0.74    0.77      221     
Frequency              0.86       0.89    0.88      162     
Hormonal_Therapy       0.91       0.90    0.91      92      
Immunotherapy          0.82       0.79    0.81      63      
Line_Of_Therapy        0.78       0.78    0.78      46      
Radiation_Dose         0.88       0.88    0.88      48      
Radiotherapy           0.83       0.88    0.85      154     
Response_To_Treatment  0.71       0.68    0.69      377     
Route                  0.94       0.85    0.89      92      
Targeted_Therapy       0.90       0.89    0.89      166     
Unspecific_Therapy     0.74       0.79    0.77      150     
micro-avg              0.84       0.84    0.84      3257    
macro-avg              0.83       0.82    0.82      3257    
weighted-avg           0.84       0.84    0.84      3257    
```
