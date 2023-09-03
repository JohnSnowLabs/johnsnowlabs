---
layout: model
title: Detect Problems, Tests, and Treatments (Italian)
author: John Snow Labs
name: ner_clinical
date: 2023-08-30
tags: [licensed, clinical, ner, it]
task: Named Entity Recognition
language: it
edition: Healthcare NLP 5.0.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms in Italian. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state-of-the-art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/){:.button.button-orange}
[Open in Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CLINICAL_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_it_5.0.1_3.0_1693369013548.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_it_5.0.1_3.0_1693369013548.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","it") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "it", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(['sentence', 'token', 'ner'])\
    .setOutputCol('ner_chunk')

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
    ])

sample_text = """Il KCNJ9 umano (Kir 3.3, GIRK3) è un membro della famiglia dei canali di potassio rettificanti internamente attivati da proteine G (GIRK). Qui descriviamo l'organizzazione genomica del locus KCNJ9 sul cromosoma 1q21-23 come gene candidato per il diabete mellito di tipo II nella popolazione indiana Pima. Il gene si estende per circa 7,6 kb e contiene un esone non codificante e due esoni codificanti separati rispettivamente da introni di circa 2,2 e circa 2,6 kb. Abbiamo identificato 14 polimorfismi a singolo nucleotide (SNP), tra cui uno che prevede una sostituzione Val366Ala, e un'insertione/delezione di 8 paia di basi (bp). I nostri studi sull'espressione hanno rivelato la presenza del trascritto in vari tessuti umani, tra cui il pancreas e due importanti tessuti insulinoresponsivi: il grasso e il muscolo scheletrico. La caratterizzazione del gene KCNJ9 dovrebbe agevolare ulteriori studi sulla funzione della proteina KCNJ9 e consentire di valutare il potenziale ruolo del locus nel diabete di tipo II. CONTESTO: Attualmente, uno degli aspetti più importanti per il trattamento del cancro al seno è lo sviluppo della terapia standard per i pazienti precedentemente trattati con antracicline e taxani."""


data = spark.createDataFrame([[sample_text]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","it")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_clinical", "it", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
))

sample_data = Seq("""Il KCNJ9 umano (Kir 3.3, GIRK3) è un membro della famiglia dei canali di potassio rettificanti internamente attivati da proteine G (GIRK). Qui descriviamo l'organizzazione genomica del locus KCNJ9 sul cromosoma 1q21-23 come gene candidato per il diabete mellito di tipo II nella popolazione indiana Pima. Il gene si estende per circa 7,6 kb e contiene un esone non codificante e due esoni codificanti separati rispettivamente da introni di circa 2,2 e circa 2,6 kb. Abbiamo identificato 14 polimorfismi a singolo nucleotide (SNP), tra cui uno che prevede una sostituzione Val366Ala, e un'insertione/delezione di 8 paia di basi (bp). I nostri studi sull'espressione hanno rivelato la presenza del trascritto in vari tessuti umani, tra cui il pancreas e due importanti tessuti insulinoresponsivi: il grasso e il muscolo scheletrico. La caratterizzazione del gene KCNJ9 dovrebbe agevolare ulteriori studi sulla funzione della proteina KCNJ9 e consentire di valutare il potenziale ruolo del locus nel diabete di tipo II. CONTESTO: Attualmente, uno degli aspetti più importanti per il trattamento del cancro al seno è lo sviluppo della terapia standard per i pazienti precedentemente trattati con antracicline e taxani.""").toDS.toDF("text")


val result = pipeline.fit(sample_data).transform(sample_data)
```
</div>

## Results

```bash
+----------------------------------------------------+-----+----+---------+
|chunk                                               |begin|end |ner_label|
+----------------------------------------------------+-----+----+---------+
|potassio rettificanti                               |73   |93  |TREATMENT|
|proteine G                                          |120  |129 |TREATMENT|
|l'organizzazione genomica del locus KCNJ9           |155  |195 |TEST     |
|diabete mellito di tipo II nella popolazione indiana|246  |297 |PROBLEM  |
|kb                                                  |338  |339 |PROBLEM  |
|un esone non codificante                            |352  |375 |PROBLEM  |
|introni                                             |429  |435 |TEST     |
|kb                                                  |462  |463 |PROBLEM  |
|polimorfismi                                        |490  |501 |TEST     |
|SNP                                                 |525  |527 |PROBLEM  |
|sostituzione Val366Ala                              |559  |580 |TREATMENT|
|un'insertione/delezione di                          |585  |610 |TREATMENT|
|I nostri studi                                      |633  |646 |TEST     |
|tessuti umani                                       |715  |727 |PROBLEM  |
|il pancreas                                         |738  |748 |PROBLEM  |
|due importanti tessuti insulinoresponsivi           |752  |792 |PROBLEM  |
|il grasso                                           |795  |803 |PROBLEM  |
|il muscolo scheletrico                              |807  |828 |PROBLEM  |
|La caratterizzazione del gene                       |831  |859 |PROBLEM  |
|ulteriori studi sulla funzione della proteina       |886  |930 |TEST     |
|diabete di tipo II                                  |997  |1014|PROBLEM  |
|uno degli aspetti più importanti                    |1040 |1071|PROBLEM  |
|trattamento del cancro al seno                      |1080 |1109|PROBLEM  |
|terapia standard                                    |1131 |1146|TREATMENT|
|antracicline                                        |1192 |1203|TREATMENT|
|taxani                                              |1207 |1212|TREATMENT|
+----------------------------------------------------+-----+----+---------+

​
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical|
|Compatibility:|Healthcare NLP 5.0.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|it|
|Size:|2.9 MB|

## Benchmarking

```bash
       label      precision    recall  f1-score   support
   TREATMENT           0.69      0.78      0.73       296
     PROBLEM           0.87      0.70      0.78       698
        TEST           0.90      0.81      0.85       401
   micro-avg           0.83      0.75      0.79      1395
   macro-avg           0.82      0.76      0.79      1395
weighted-avg           0.84      0.75      0.79      1395
```
