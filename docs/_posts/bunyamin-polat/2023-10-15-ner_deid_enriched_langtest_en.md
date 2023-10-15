---
layout: model
title: Detect PHI for Deidentification (Enriched - LangTest)
author: John Snow Labs
name: ner_deid_enriched_langtest
date: 2023-10-15
tags: [en, ner, licensed, clinical, deid, langtest]
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

Deidentification NER (Enriched) is a Named Entity Recognition model that annotates text to find protected health information that may need to be de-identified. The entities it annotates are Age, City, Country, Date, Doctor, Hospital, Idnum, Medicalrecord, Organization, Patient, Phone, Profession, State, Street, Username, and Zip. Clinical NER is trained with the 'embeddings_clinical' word embeddings model, so be sure to use the same embeddings in the pipeline. This is the version of [ner_deid_enriched](https://nlp.johnsnowlabs.com/2021/03/31/ner_deid_enriched_en.html) model augmented with `langtest` library.

We stuck to the official annotation guideline (AG) for the 2014 i2b2 Deid challenge while annotating new datasets for this model. All the details regarding the nuances and explanations for AG can be found here [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4978170/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4978170/)

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **lowercase**        | 903                   | 272                  | 11541                 | 12172                | 95%                   | 93%                  | 98%                 |
| **swap_entities**    | 268                   | 249                  | 2481                  | 2482                 | 95%                   | 90%                  | 91%                 |
| **titlecase**        | 339                   | 192                  | 13088                 | 13235                | 95%                   | 97%                  | 99%                 |
| **uppercase**        | 683                   | 343                  | 12670                 | 13010                | 95%                   | 95%                  | 97%                 |
| **weighted average** | **2193**              | **1056**             | **39780**             | **40899**            | **95%**               | **94.78%**           | **97.48%**          |

## Predicted Entities

`AGE`, `CITY`, `COUNTRY`, `DATE`, `DOCTOR`, `HOSPITAL`, `IDNUM`, `MEDICALRECORD`, `ORGANIZATION`, `PATIENT`, `PHONE`, `PROFESSION`, `STATE`, `STREET`, `USERNAME`, `ZIP`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_enriched_langtest_en_5.1.1_3.0_1697388253227.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_enriched_langtest_en_5.1.1_3.0_1697388253227.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_deid_enriched_langtest", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverter()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")
    
nlpPipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector, 
    tokenizer, 
    word_embeddings, 
    ner, 
    ner_converter])

model = nlpPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

results = model.transform(spark.createDataFrame([['HISTORY OF PRESENT ILLNESS: Mr. Smith is a 60-year-old white male veteran with multiple comorbidities, who has a history of bladder cancer diagnosed approximately two years ago by the VA Hospital. He underwent a resection there. He was seen in Urology Clinic and Radiology Clinic on 02/04/2003. HOSPITAL COURSE: Mr. Smith presented to the Day Hospital in anticipation for Urology surgery. On evaluation, EKG, and echocardiogram were abnormal, a Cardiology consult was obtained. A cardiac adenosine stress MRI was then proceeded, and same was positive for inducible ischemia, mild-to-moderate inferolateral subendocardial infarction with peri-infarct ischemia. In addition, inducible ischemia seen in the inferior lateral septum. Mr. Smith underwent a left heart catheterization, which revealed two-vessel coronary artery disease. The RCA, proximal was 95% stenosed and the distal 80% stenosed. The mid LAD was 85% stenosed and the distal LAD was 85% stenosed. There were four Multi-Link Vision bare metal stents placed to decrease all four lesions to 0%. Following the intervention, Mr. Smith was admitted to 7 Ardmore Tower under the Cardiology Service under the direction of Dr. Hart. Mr. Smith had a noncomplicated post-intervention hospital course. He was stable for discharge home on 02/07/2003 with instructions to take Plavix daily for one month and Urology is aware of the same.']], ["text"]))
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

val ner = MedicalNerModel.pretrained("ner_deid_enriched_langtest", "en", "clinical/models")
	.setInputCols("sentence", "token", "embeddings")
	.setOutputCol("ner")

val ner_converter = new NerConverter()
 	.setInputCols(Array("sentence", "token", "ner"))
 	.setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector, 
    tokenizer, 
    word_embeddings, 
    ner, 
    ner_converter))

val data = Seq("""HISTORY OF PRESENT ILLNESS: Mr. Smith is a 60-year-old white male veteran with multiple comorbidities, who has a history of bladder cancer diagnosed approximately two years ago by the VA Hospital. He underwent a resection there. He was seen in Urology Clinic and Radiology Clinic on 02/04/2003. HOSPITAL COURSE: Mr. Smith presented to the Day Hospital in anticipation for Urology surgery. On evaluation, EKG, and echocardiogram were abnormal, a Cardiology consult was obtained. A cardiac adenosine stress MRI was then proceeded, and same was positive for inducible ischemia, mild-to-moderate inferolateral subendocardial infarction with peri-infarct ischemia. In addition, inducible ischemia seen in the inferior lateral septum. Mr. Smith underwent a left heart catheterization, which revealed two-vessel coronary artery disease. The RCA, proximal was 95% stenosed and the distal 80% stenosed. The mid LAD was 85% stenosed and the distal LAD was 85% stenosed. There were four Multi-Link Vision bare metal stents placed to decrease all four lesions to 0%. Following the intervention, Mr. Smith was admitted to 7 Ardmore Tower under the Cardiology Service under the direction of Dr. Hart. Mr. Smith had a noncomplicated post-intervention hospital course. He was stable for discharge home on 02/07/2003 with instructions to take Plavix daily for one month and Urology is aware of the same.""").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---------------+---------+
|chunk          |ner_label|
+---------------+---------+
|Smith          |PATIENT  |
|VA Hospital    |HOSPITAL |
|02/04/2003     |DATE     |
|Smith          |PATIENT  |
|Smith          |PATIENT  |
|Smith          |PATIENT  |
|7 Ardmore Tower|HOSPITAL |
|Hart           |DOCTOR   |
|Smith          |PATIENT  |
|02/07/2003     |DATE     |
+---------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_enriched_langtest|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.9 MB|

## References

Trained on JSL enriched n2c2 2014: De-identification and Heart Disease Risk Factors Challenge [datasets](https://portal.dbmi.hms.harvard.edu/projects/n2c2-2014/) with `embeddings_clinical`

## Benchmarking

```bash
label           precision  recall  f1-score  support 
AGE             0.96       0.95    0.95      198     
CITY            0.72       0.68    0.70      80      
COUNTRY         0.71       0.77    0.74      26      
DATE            0.98       0.98    0.98      1560    
DEVICE          1.00       0.50    0.67      2       
DOCTOR          0.92       0.92    0.92      600     
HEALTHPLAN      0.00       0.00    0.00      1       
HOSPITAL        0.91       0.90    0.90      292     
IDNUM           0.82       0.62    0.70      50      
LOCATION-OTHER  1.00       0.44    0.62      9       
MEDICALRECORD   0.90       0.95    0.93      106     
ORGANIZATION    0.45       0.28    0.35      32      
PATIENT         0.86       0.91    0.89      280     
PHONE           0.91       0.96    0.94      53      
PROFESSION      0.74       0.68    0.71      50      
STATE           0.94       0.79    0.85      56      
STREET          0.94       0.89    0.91      54      
USERNAME        1.00       0.81    0.90      32      
ZIP             0.95       0.86    0.90      43      
micro-avg       0.93       0.92    0.93      3524    
macro-avg       0.83       0.73    0.77      3524    
weighted-avg    0.93       0.92    0.93      3524    
```