---
layout: model
title: Extract Cancer Therapies and Granular Posology Information (langtest)
author: John Snow Labs
name: ner_oncology_posology_langtest
date: 2023-09-04
tags: [en, ner, licensed, clinical, oncology, posology, langtest]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.0.2
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts cancer therapies (Cancer_Surgery, Radiotherapy, and Cancer_Therapy) and posology information at a granular level. It is the version of [ner_oncology_posology](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_posology_en.html) model augmented with `langtest` library.

Definitions of Predicted Entities:

- `Cancer_Surgery`: Terms that indicate surgery as a form of cancer treatment.
- `Cancer_Therapy`: Any cancer treatment mentioned in text, excluding surgeries and radiotherapy.
- `Cycle_Count`: The total number of cycles being administered of an oncological therapy (e.g. "5 cycles"). 
- `Cycle_Day`: References to the day of the cycle of oncological therapy (e.g. "day 5").
- `Cycle_Number`: The number of the cycle of an oncological therapy that is being applied (e.g. "third cycle").
- `Dosage`: The quantity prescribed by the physician for an active ingredient.
- `Duration`: Words indicating the duration of a treatment (e.g. "for 2 weeks").
- `Frequency`: Words indicating the frequency of treatment administration (e.g. "daily" or "bid").
- `Radiotherapy`: Terms that indicate the use of Radiotherapy.
- `Radiation_Dose`: Dose used in radiotherapy.
- `Route`: Words indicating the type of administration route (such as "PO" or "transdermal").

## Predicted Entities

`Cancer_Surgery`, `Cancer_Therapy`, `Cycle_Count`, `Cycle_Day`, `Cycle_Number`, `Dosage`, `Duration`, `Frequency`, `Radiotherapy`, `Radiation_Dose`, `Route`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_posology_langtest_en_5.0.2_3.0_1693828527870.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_posology_langtest_en_5.0.2_3.0_1693828527870.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")                

ner = MedicalNerModel.pretrained("ner_oncology_posology_langtest", "en", "clinical/models") \
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

data = spark.createDataFrame([["The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses. She is currently receiving his second cycle of chemotherapy and is in good overall condition."]]).toDF("text")

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
    
val word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                
    
val ner = MedicalNerModel.pretrained("ner_oncology_posology_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
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

val data = Seq("The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses. She is currently receiving his second cycle of chemotherapy and is in good overall condition.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------+--------------+
|chunk           |ner_label     |
+----------------+--------------+
|adriamycin      |Cancer_Therapy|
|60 mg/m2        |Dosage        |
|cyclophosphamide|Cancer_Therapy|
|600 mg/m2       |Dosage        |
|six courses     |Cycle_Count   |
|second cycle    |Cycle_Number  |
|chemotherapy    |Cancer_Therapy|
+----------------+--------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_posology_langtest|
|Compatibility:|Healthcare NLP 5.0.2+|
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
label             precision  recall  f1-score  support 
B-Cancer_Therapy  0.93       0.96    0.94      1185    
B-Dosage          0.90       0.88    0.89      258     
I-Dosage          0.90       0.94    0.92      752     
B-Frequency       0.92       0.92    0.92      157     
I-Frequency       0.92       0.86    0.89      218     
B-Cancer_Surgery  0.83       0.85    0.84      517     
I-Cancer_Therapy  0.81       0.86    0.83      507     
B-Radiotherapy    0.91       0.86    0.89      170     
I-Radiotherapy    0.91       0.75    0.82      120     
B-Duration        0.87       0.79    0.83      280     
I-Duration        0.89       0.85    0.87      537     
I-Cancer_Surgery  0.75       0.78    0.77      370     
B-Cycle_Number    0.89       0.61    0.72      41      
I-Cycle_Number    0.89       0.61    0.72      41      
B-Cycle_Count     0.82       0.87    0.84      128     
I-Cycle_Count     0.83       0.88    0.86      115     
I-Radiation_Dose  0.93       0.86    0.89      77      
B-Cycle_Day       0.85       0.85    0.85      124     
B-Route           0.91       0.92    0.92      114     
I-Cycle_Day       0.87       0.77    0.82      177     
I-Route           0.81       0.72    0.76      29      
B-Radiation_Dose  0.93       0.95    0.94      43      
micro-avg         0.88       0.88    0.88      5960    
macro-avg         0.88       0.83    0.85      5960    
weighted-avg      0.88       0.88    0.88      5960    
```