---
layout: model
title: Detect Clinical Events (langtest)
author: John Snow Labs
name: ner_events_clinical_langtest
date: 2023-08-31
tags: [en, ner, clinical, licensed, langtest]
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

This model can be used to detect clinical events in medical text. It is the version of [ner_events_clinical](https://nlp.johnsnowlabs.com/2021/03/31/ner_events_clinical_en.html) model augmented with `langtest` library

## Predicted Entities

`DATE`, `TIME`, `PROBLEM`, `TEST`, `TREATMENT`, `OCCURENCE`, `CLINICAL_DEPT`, `EVIDENTIAL`, `DURATION`, `FREQUENCY`, `ADMISSION`, `DISCHARGE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_events_clinical_langtest_en_5.0.2_3.0_1693508325179.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_events_clinical_langtest_en_5.0.2_3.0_1693508325179.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_events_clinical_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter()\
     .setInputCols(["sentence", "token", "ner"])\
     .setOutputCol("ner_chunk")

nlp_pipeline = Pipeline(stages=[document_assembler, 
                                                        sentence_detector, 
                                                        tokenizer, 
                                                        word_embeddings,  
                                                        clinical_ner, 
                                                        ner_converter])

model = nlp_pipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

result = model.transform(spark.createDataFrame([["The patient presented to the emergency room last evening"]], ["text"]))
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
         
val sentence_detector = sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_events_clinical_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, ner, ner_converter))

val data = Seq("""The patient presented to the emergency room last evening""").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------+-------------+
|chunk             |ner_label    |
+------------------+-------------+
|presented         |EVIDENTIAL   |
|the emergency room|CLINICAL_DEPT|
|last evening      |DATE         |
+------------------+-------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_events_clinical_langtest|
|Compatibility:|Healthcare NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.7 MB|

## References

Trained on augmented version of i2b2 dataset with `clinical_embeddings`.

## Benchmarking

```bash
label            precision  recall  f1-score  support 
B-TREATMENT      0.84       0.85    0.84      3280    
I-TREATMENT      0.84       0.82    0.83      3115    
B-DATE           0.82       0.84    0.83      985     
I-DATE           0.74       0.83    0.78      1117    
B-TEST           0.85       0.84    0.85      2171    
B-DURATION       0.63       0.67    0.65      341     
I-DURATION       0.64       0.75    0.69      465     
B-PROBLEM        0.84       0.86    0.85      4309    
I-PROBLEM        0.82       0.85    0.84      6063    
B-OCCURRENCE     0.69       0.60    0.64      2493    
I-OCCURRENCE     0.50       0.38    0.43      1612    
B-DISCHARGE      0.00       0.00    0.00      117     
B-EVIDENTIAL     0.76       0.70    0.73      595     
I-EVIDENTIAL     0.00       0.00    0.00      18      
I-TEST           0.86       0.83    0.85      2665    
B-CLINICAL_DEPT  0.79       0.81    0.80      732     
I-CLINICAL_DEPT  0.86       0.87    0.87      1410    
B-ADMISSION      0.00       0.00    0.00      120     
B-FREQUENCY      0.85       0.61    0.71      197     
I-FREQUENCY      0.74       0.40    0.52      161     
B-TIME           0.68       0.38    0.49      60      
I-TIME           0.90       0.37    0.53      127     
micro-avg        0.80       0.78    0.79      32153   
macro-avg        0.67       0.60    0.62      32153   
weighted-avg     0.79       0.78    0.79      32153   
```
