---
layout: model
title: Detect Problems, Tests, and Treatments (French)
author: John Snow Labs
name: ner_clinical
date: 2023-08-30
tags: [licensed, clinical, ner, fr]
task: Named Entity Recognition
language: fr
edition: Healthcare NLP 5.0.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms in French. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state-of-the-art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/){:.button.button-orange}
[Open in Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CLINICAL_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_fr_5.0.1_3.0_1693411313384.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_fr_5.0.1_3.0_1693411313384.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","fr") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "fr", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
    ])

sample_text = """Le KCNJ9 humain (Kir 3.3, GIRK3) is a member of the famille des canaux potassiques rectifiants activés par les protéines G (GIRK). Ici, nous décrivons l'organisation génomique du locus KCNJ9 sur le chromosome 1q21-23 en tant que gène candidat pour le diabète sucré de type II dans la population indienne Pima. Le gène s'étend sur environ 7,6 kb et contient un exon non codant et deux exons codants séparés respectivement par des introns d'environ 2,2 et environ 2,6 kb. Nous avons identifié 14 polymorphismes d'un seul nucléotide (SNP), dont un qui prédit une substitution Val366Ala, ainsi qu'une insertion/deletion de 8 paires de bases (bp). Nos études d'expression ont révélé la présence du transcrit dans divers tissus humains, notamment le pancréas et deux tissus importants réagissant à l'insuline : la graisse et le muscle squelettique. La caractérisation du gène KCNJ9 devrait faciliter d'autres études sur la fonction de la protéine KCNJ9 et permettre d'évaluer le rôle potentiel du locus dans le diabète de type II. CONTEXTE : À l'heure actuelle, l'un des aspects les plus importants pour le traitement du cancer du sein est le développement de la thérapie standard pour les patients précédemment traités avec des anthracyclines et des taxanes."""


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

val embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","fr")
    .setInputCols(Array("document", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_clinical", "fr", "clinical/models")
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
    ])

val sample_data = Seq("""Le KCNJ9 humain (Kir 3.3, GIRK3) is a member of the famille des canaux potassiques rectifiants activés par les protéines G (GIRK). Ici, nous décrivons l'organisation génomique du locus KCNJ9 sur le chromosome 1q21-23 en tant que gène candidat pour le diabète sucré de type II dans la population indienne Pima. Le gène s'étend sur environ 7,6 kb et contient un exon non codant et deux exons codants séparés respectivement par des introns d'environ 2,2 et environ 2,6 kb. Nous avons identifié 14 polymorphismes d'un seul nucléotide (SNP), dont un qui prédit une substitution Val366Ala, ainsi qu'une insertion/deletion de 8 paires de bases (bp). Nos études d'expression ont révélé la présence du transcrit dans divers tissus humains, notamment le pancréas et deux tissus importants réagissant à l'insuline : la graisse et le muscle squelettique. La caractérisation du gène KCNJ9 devrait faciliter d'autres études sur la fonction de la protéine KCNJ9 et permettre d'évaluer le rôle potentiel du locus dans le diabète de type II. CONTEXTE : À l'heure actuelle, l'un des aspects les plus importants pour le traitement du cancer du sein est le développement de la thérapie standard pour les patients précédemment traités avec des anthracyclines et des taxanes.""").toDS.toDF("text")

val result = pipeline.fit(sample_data).transform(sample_data)
```
</div>

## Results

```bash
+---------------------------------------------------------+-----+----+---------+
|chunk                                                    |begin|end |ner_label|
+---------------------------------------------------------+-----+----+---------+
|GIRK3                                                    |26   |30  |TREATMENT|
|canaux potassiques                                       |64   |81  |TREATMENT|
|protéines G                                              |111  |121 |TREATMENT|
|locus KCNJ9                                              |179  |189 |PROBLEM  |
|gène                                                     |229  |232 |PROBLEM  |
|diabète sucré de type II dans la population indienne Pima|251  |307 |PROBLEM  |
|Le gène                                                  |310  |316 |TEST     |
|un exon non codant                                       |357  |374 |PROBLEM  |
|exons codants                                            |384  |396 |TEST     |
|introns d'environ                                        |429  |445 |TREATMENT|
|polymorphismes                                           |494  |507 |TEST     |
|SNP                                                      |531  |533 |TEST     |
|substitution Val366Ala                                   |560  |581 |TEST     |
|insertion/deletion                                       |597  |614 |PROBLEM  |
|Nos études d'expression                                  |643  |665 |TEST     |
|transcrit dans divers tissus                             |693  |720 |PROBLEM  |
|graisse                                                  |808  |814 |PROBLEM  |
|muscle squelettique                                      |822  |840 |PROBLEM  |
|caractérisation du gène KCNJ9                            |846  |874 |TEST     |
|locus                                                    |991  |995 |PROBLEM  |
|diabète de type II                                       |1005 |1022|PROBLEM  |
|thérapie standard                                        |1157 |1173|TREATMENT|
|anthracyclines                                           |1223 |1236|TREATMENT|
|taxanes                                                  |1245 |1251|TREATMENT|
+---------------------------------------------------------+-----+----+---------+
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
|Language:|fr|
|Size:|2.9 MB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
        TEST       0.92      0.80      0.85       288
     PROBLEM       0.80      0.79      0.80       529
   TREATMENT       0.70      0.66      0.68       310
   micro-avg       0.80      0.76      0.78      1127
   macro-avg       0.81      0.75      0.78      1127
weighted-avg       0.80      0.76      0.78      1127
```
