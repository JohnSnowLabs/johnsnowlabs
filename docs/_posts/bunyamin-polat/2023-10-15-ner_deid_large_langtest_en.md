---
layout: model
title: Detect PHI for Deidentification (Large - LangTest)
author: John Snow Labs
name: ner_deid_large_langtest
date: 2023-10-15
tags: [en, ner, clinical, licensed, deid, langtest]
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

Deidentification NER (Large) is a Named Entity Recognition model that annotates text to find protected health information that may need to be de-identified. The entities it annotates are Age, Contact, Date, ID, Location, Name, and Profession. This is the version of [ner_deid_large](https://nlp.johnsnowlabs.com/2021/03/31/ner_deid_large_en.html) model augmented with `langtest` library.

We stuck to the official annotation guideline (AG) for the 2014 i2b2 Deid challenge while annotating new datasets for this model. All the details regarding the nuances and explanations for AG can be found here [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4978170/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4978170/)

| **test_type**             | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|---------------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**          | 238                   | 92                   | 1662                  | 1808                 | 95%                   | 87%                  | 95%                 |
| **add_typo**              | 133                   | 124                  | 3407                  | 3437                 | 95%                   | 96%                  | 97%                 |
| **lowercase**             | 810                   | 142                  | 2840                  | 3508                 | 95%                   | 78%                  | 96%                 |
| **strip_all_punctuation** | 346                   | 262                  | 2934                  | 3018                 | 95%                   | 89%                  | 92%                 |
| **titlecase**             | 278                   | 86                   | 2802                  | 2994                 | 95%                   | 91%                  | 97%                 |
| **uppercase**             | 642                   | 194                  | 2705                  | 3153                 | 95%                   | 81%                  | 94%                 |
| **weighted average**      | **2447**              | **900**              | **16350**             | **17918**            | **95%**               | **86.98%**           | **95.22%**          |

## Predicted Entities

`AGE`, `CONTACT`, `DATE`, `ID`, `LOCATION`, `NAME`, `PROFESSION`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_large_langtest_en_5.1.1_3.0_1697391879893.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_large_langtest_en_5.1.1_3.0_1697391879893.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols("sentence") \
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner = MedicalNerModel.pretrained("ner_deid_large_langtest", "en", "clinical/models") \
    .setInputCols("sentence", "token", "embeddings") \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("entities")

nlp_pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector, 
    tokenizer, 
    word_embeddings, 
    ner, 
    ner_converter]) 

data = spark.createDataFrame([["""HISTORY OF PRESENT ILLNESS: Mr. Smith is a 60-year-old white male veteran with multiple comorbidities, who has a history of bladder cancer diagnosed approximately two years ago by the VA Hospital. He underwent a resection there. He was to be admitted to the Day Hospital for cystectomy. He was seen in Urology Clinic and Radiology Clinic on 02/04/2003.	HOSPITAL COURSE: Mr. Smith presented to the Day Hospital in anticipation for Urology surgery. On evaluation, EKG, echocardiogram was abnormal, a Cardiology consult was obtained. A cardiac adenosine stress MRI was then proceeded, same was positive for inducible ischemia, mild-to-moderate inferolateral subendocardial infarction with peri-infarct ischemia. In addition, inducible ischemia seen in the inferior lateral septum. Mr. Smith underwent a left heart catheterization, which revealed two vessel coronary artery disease. The RCA, proximal was 95% stenosed and the distal 80% stenosed. The mid LAD was 85% stenosed and the distal LAD was 85% stenosed. There was four Multi-Link Vision bare metal stents placed to decrease all four lesions to 0%. Following intervention, Mr. Smith was admitted to 7 Ardmore Tower under Cardiology Service under the direction of Dr. Hart. Mr. Smith had a noncomplicated post-intervention hospital course. He was stable for discharge home on 02/07/2003 with instructions to take Plavix daily for one month and Urology is aware of the same."""]]).toDF("text")

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

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_deid_large_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("entities")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector, 
    tokenizer, 
    word_embeddings, 
    ner, 
    ner_converter))

val data = Seq("HISTORY OF PRESENT ILLNESS: Mr. Smith is a 60-year-old white male veteran with multiple comorbidities, who has a history of bladder cancer diagnosed approximately two years ago by the VA Hospital. He underwent a resection there. He was to be admitted to the Day Hospital for cystectomy. He was seen in Urology Clinic and Radiology Clinic on 02/04/2003. HOSPITAL COURSE: Mr. Smith presented to the Day Hospital in anticipation for Urology surgery. On evaluation, EKG, echocardiogram was abnormal, and a Cardiology consult was obtained. A cardiac adenosine stress MRI was then proceeded, same was positive for inducible ischemia, mild-to-moderate inferolateral subendocardial infarction with peri-infarct ischemia. In addition, inducible ischemia seen in the inferior lateral septum. Mr. Smith underwent a left heart catheterization, which revealed two vessel coronary artery disease. The RCA, proximal was 95% stenosed and the distal 80% stenosed. The mid LAD was 85% stenosed and the distal LAD was 85% stenosed. There was four Multi-Link Vision bare metal stents placed to decrease all four lesions to 0%. Following intervention, Mr. Smith was admitted to 7 Ardmore Tower under Cardiology Service under the direction of Dr. Hart. Mr. Smith had a noncomplicated post-intervention hospital course. He was stable for discharge home on 02/07/2003 with instructions to take Plavix daily for one month and Urology is aware of the same.").toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---------------+---------+
|chunk          |ner_label|
+---------------+---------+
|Smith          |NAME     |
|VA Hospital    |LOCATION |
|Day Hospital   |LOCATION |
|02/04/2003     |DATE     |
|Smith          |NAME     |
|Day Hospital   |LOCATION |
|Smith          |NAME     |
|Smith          |NAME     |
|7 Ardmore Tower|LOCATION |
|Hart           |NAME     |
|Smith          |NAME     |
|02/07/2003     |DATE     |
+---------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_large_langtest|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.7 MB|

## References

Trained on JSL enriched n2c2 2014: De-identification and Heart Disease Risk Factors Challenge [datasets](https://portal.dbmi.hms.harvard.edu/projects/n2c2-2014/) with `embeddings_clinical`

## Benchmarking

```bash
label         precision  recall  f1-score  support 
B-AGE         0.98       1.00    0.99      233     
B-CONTACT     0.97       0.99    0.98      67      
B-DATE        1.00       1.00    1.00      2151    
B-ID          0.99       0.97    0.98      194     
B-LOCATION    0.98       0.96    0.97      753     
B-NAME        0.99       0.99    0.99      1316    
B-PROFESSION  0.92       0.91    0.91      76      
I-AGE         1.00       0.75    0.86      4       
I-CONTACT     1.00       0.95    0.97      55      
I-DATE        0.99       1.00    1.00      376     
I-ID          1.00       0.77    0.87      26      
I-LOCATION    0.98       0.97    0.97      628     
I-NAME        0.99       0.99    0.99      1151    
I-PROFESSION  0.94       0.85    0.89      59      
micro-avg     0.99       0.98    0.99      7089    
macro-avg     0.98       0.93    0.95      7089    
weighted-avg  0.99       0.98    0.99      7089   
```
