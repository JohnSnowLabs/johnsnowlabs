---
layout: model
title: Detect PHI (Deidentification)(clinical_large)
author: John Snow Labs
name: ner_deid_large_emb_clinical_large
date: 2023-04-12
tags: [ner, licensed, clinical, phi, deidentification, english, en]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Description : Deidentification NER (Large) is a Named Entity Recognition model that annotates text to find protected health information that may need to be deidentified. The entities it annotates are Age, Contact, Date, Id, Location, Name, and Profession. This model is trained with the 'embeddings_clinical_large' word embeddings model, so be sure to use the same embeddings in the pipeline.

We sticked to official annotation guideline (AG) for 2014 i2b2 Deid challenge while annotating new datasets for this model. All the details regarding the nuances and explanations for AG can be found here https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4978170/

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_DEMOGRAPHICS/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_DEMOGRAPHICS.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_large_emb_clinical_large_en_4.3.2_3.0_1681321107196.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_large_emb_clinical_large_en_4.3.2_3.0_1681321107196.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence") 

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_large", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

deid_ner = MedicalNerModel.load( "ner_deid_large_emb_clinical_large", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("deid_ner")
    
deid_ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "deid_ner"]) \
    .setOutputCol("deid_ner_chunk")

deid_ner_pipeline = Pipeline(stages=[
    documentAssembler, 
    sentenceDetector,
    tokenizer,
    word_embeddings,
    deid_ner,
    deid_ner_converter])

empty_data = spark.createDataFrame([[""]]).toDF("text")

deid_ner_model = deid_ner_pipeline.fit(empty_data)

results = deid_ner_model.transform(spark.createDataFrame([["""HISTORY OF PRESENT ILLNESS: Mr. Smith is a 60-year-old white male veteran with multiple comorbidities, who has a history of bladder cancer diagnosed approximately two years ago by the VA Hospital. He underwent a resection there. He was to be admitted to the Day Hospital for cystectomy. He was seen in Urology Clinic and Radiology Clinic on 02/04/2003.	HOSPITAL COURSE: Mr. Smith presented to the Day Hospital in anticipation for Urology surgery. On evaluation, EKG, echocardiogram was abnormal, a Cardiology consult was obtained. A cardiac adenosine stress MRI was then proceeded, same was positive for inducible ischemia, mild-to-moderate inferolateral subendocardial infarction with peri-infarct ischemia. In addition, inducible ischemia seen in the inferior lateral septum. Mr. Smith underwent a left heart catheterization, which revealed two vessel coronary artery disease. The RCA, proximal was 95% stenosed and the distal 80% stenosed. The mid LAD was 85% stenosed and the distal LAD was 85% stenosed. There was four Multi-Link Vision bare metal stents placed to decrease all four lesions to 0%. Following intervention, Mr. Smith was admitted to 7 Ardmore Tower under Cardiology Service under the direction of Dr. Hart. Mr. Smith had a noncomplicated post-intervention hospital course. He was stable for discharge home on 02/07/2003 with instructions to take Plavix daily for one month and Urology is aware of the same."""]]).toDF("text"))
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
    
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_large", "en", "clinical/models")\
    .setInputCols(Array("sentence", "token"))\
    .setOutputCol("embeddings")

val deid_ner_model = BertForTokenClassification.pretrained('ner_deid_large_emb_clinical_large' "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("deid_ner")

val deid_ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("deid_ner_chunk")

val deid_pipeline = new PipelineModel().setStages(Array(document_assembler, 
                                                   sentence_detector,
                                                   tokenizer,
                                                   word_embeddings,
                                                   deid_ner_model,
                                                   deid_ner_converter))

val data = Seq(""" """HISTORY OF PRESENT ILLNESS: Mr. Smith is a 60-year-old white male veteran with multiple comorbidities, who has a history of bladder cancer diagnosed approximately two years ago by the VA Hospital. He underwent a resection there. He was to be admitted to the Day Hospital for cystectomy. He was seen in Urology Clinic and Radiology Clinic on 02/04/2003.	HOSPITAL COURSE: Mr. Smith presented to the Day Hospital in anticipation for Urology surgery. On evaluation, EKG, echocardiogram was abnormal, a Cardiology consult was obtained. A cardiac adenosine stress MRI was then proceeded, same was positive for inducible ischemia, mild-to-moderate inferolateral subendocardial infarction with peri-infarct ischemia. In addition, inducible ischemia seen in the inferior lateral septum. Mr. Smith underwent a left heart catheterization, which revealed two vessel coronary artery disease. The RCA, proximal was 95% stenosed and the distal 80% stenosed. The mid LAD was 85% stenosed and the distal LAD was 85% stenosed. There was four Multi-Link Vision bare metal stents placed to decrease all four lesions to 0%. Following intervention, Mr. Smith was admitted to 7 Ardmore Tower under Cardiology Service under the direction of Dr. Hart. Mr. Smith had a noncomplicated post-intervention hospital course. He was stable for discharge home on 02/07/2003 with instructions to take Plavix daily for one month and Urology is aware of the same."""""").toDS.toDF("text")

val result = model.fit(data).transform(data)
```
</div>

## Results

```bash
|    | chunks          |   begin |   end | entities   |
|---:|:----------------|--------:|------:|:-----------|
|  0 | Smith           |      32 |    36 | NAME       |
|  1 | VA Hospital     |     184 |   194 | LOCATION   |
|  2 | Day Hospital    |     258 |   269 | LOCATION   |
|  3 | 02/04/2003      |     341 |   350 | DATE       |
|  4 | Smith           |     374 |   378 | NAME       |
|  5 | Day Hospital    |     397 |   408 | LOCATION   |
|  6 | Smith           |     782 |   786 | NAME       |
|  7 | Smith           |    1131 |  1135 | NAME       |
|  8 | 7 Ardmore Tower |    1153 |  1167 | LOCATION   |
|  9 | Hart            |    1221 |  1224 | NAME       |
| 10 | Smith           |    1231 |  1235 | NAME       |
| 11 | 02/07/2003      |    1329 |  1338 | DATE       |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_large_emb_clinical_large|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|2.8 MB|

## Benchmarking

```bash
                  precision recall    f1-score  support
     CONTACT       0.92      0.98      0.95       126
        DATE       0.99      0.99      0.99      2631
        NAME       0.98      0.98      0.98      2594
         AGE       0.99      0.94      0.97       284
    LOCATION       0.97      0.94      0.95      1511
          ID       0.91      0.96      0.94       213
  PROFESSION       0.81      0.84      0.83       160
   micro avg       0.97      0.97      0.97      7519
   macro avg       0.94      0.95      0.94      7519
weighted avg       0.97      0.97      0.97      7519
```
