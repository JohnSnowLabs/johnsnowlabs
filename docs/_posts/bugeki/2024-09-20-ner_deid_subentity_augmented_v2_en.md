---
layout: model
title: Detect PHI for Deidentification (Subentity- Augmented)
author: John Snow Labs
name: ner_deid_subentity_augmented_v2
date: 2024-09-20
tags: [licensed, en, ner, deid]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Named Entity recognition annotator allows for a generic model to be trained by utilizing a deep learning algorithm (Char CNNs - BiLSTM - CRF - word embeddings)
inspired on a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM, CNN. Deidentification NER is a Named Entity Recognition model
that annotates text to find protected health information that may need to be deidentified. Model detects 18 entities.

## Predicted Entities

`ZIP`, `ORGANIZATION`, `COUNTRY`, `PATIENT`, `PROFESSION`, `STATE`, `IDNUM`, `PHONE`, `STREET`, `HOSPITAL`, `LOCATION_OTHER`, `AGE`, `DOCTOR`, `CITY`, `MEDICALRECORD`, `DEVICE`, `DATE`, `USERNAME`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_augmented_v2_en_5.4.1_3.0_1726822472566.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_augmented_v2_en_5.4.1_3.0_1726822472566.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

deid_ner = MedicalNerModel.pretrained("ner_deid_subentity_augmented_v2", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk_subentity")

nlpPipeline = Pipeline(stages=[
                    document_assembler,
                    sentence_detector,
                    tokenizer,
                    word_embeddings,
                    deid_ner,
                    ner_converter])

model = nlpPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

text = "A. Record date : 2093-01-13, David Hale, M.D., Name : Hendrickson, Ora MR. # 7194334 Date : 01/13/93 PCP : Oliveira, 25 year old, Record date : 1-11-2000. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 302 786-5227. Patient's complaints first surfaced when he started working for Brothers Coal-Mine."

data = spark.createDataFrame([[text]]).toDF("text")

results = model.transform(data)
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

val deid_ner = MedicalNerModel.pretrained("ner_deid_subentity_augmented_v2", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk_subentity")

val nlpPipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    deid_ner,
    ner_converter))

val data = Seq("A. Record date : 2093-01-13, David Hale, M.D., Name : Hendrickson, Ora MR. # 7194334 Date : 01/13/93 PCP : Oliveira, 25 year old, Record date : 1-11-2000. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 302 786-5227. Patient's complaints first surfaced when he started working for Brothers Coal-Mine.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---+-----------------------------+-----+---+-------------+----------+
|   |ner_chunk                    |begin|end|ner_label    |confidence|
+---+-----------------------------+-----+---+-------------+----------+
| 0 |2093-01-13                   |17   |26 |DATE         |1.0       |
| 1 |David Hale                   |29   |38 |DOCTOR       |0.9998    |
| 2 |Hendrickson, Ora             |54   |69 |PATIENT      |0.8085334 |
| 3 |7194334                      |77   |83 |MEDICALRECORD|0.9971    |
| 4 |01/13/93                     |92   |99 |DATE         |1.0       |
| 5 |Oliveira                     |107  |114|DOCTOR       |1.0       |
| 6 |25                           |117  |118|AGE          |0.9995    |
| 7 |1-11-2000                    |144  |152|DATE         |0.9998    |
| 8 |Cocke County Baptist Hospital|155  |183|HOSPITAL     |0.84585   |
| 9 |0295 Keats Street            |186  |202|STREET       |0.99956673|
| 10|302 786 5227                 |215  |226|PHONE        |0.9714    |
| 11|Brothers Coal-Mine           |293  |310|ORGANIZATION |0.9285    |
+---+-----------------------------+-----+---+-------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_subentity_augmented_v2|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|34.8 MB|

## Benchmarking

```bash
         label      tp     fp     fn   total  precision  recall      f1
           AGE   727.0   46.0   35.0   762.0     0.9405  0.9541  0.9472
          CITY   269.0   45.0   72.0   341.0     0.8567  0.7889  0.8214
       COUNTRY    96.0   35.0   32.0   128.0     0.7328  0.75    0.7413
          DATE  5531.0   69.0  111.0  5642.0     0.9877  0.9803  0.984
        DEVICE    10.0    0.0    0.0    10.0     1.0     1.0     1.0
        DOCTOR  3368.0  231.0  179.0  3547.0     0.9358  0.9495  0.9426
      HOSPITAL  1377.0   69.0  207.0  1584.0     0.9523  0.8693  0.9089
         IDNUM   161.0   36.0   49.0   210.0     0.8173  0.7667  0.7912
LOCATION_OTHER    19.0    3.0    2.0    21.0     0.8636  0.9048  0.8837
 MEDICALRECORD   412.0   20.0   32.0   444.0     0.9537  0.9279  0.9406
  ORGANIZATION   101.0   36.0   37.0   138.0     0.7372  0.7319  0.7345
       PATIENT  1468.0  101.0  159.0  1627.0     0.9356  0.9023  0.9186
         PHONE   346.0   32.0    8.0   354.0     0.9153  0.9774  0.9454
    PROFESSION   271.0   72.0   65.0   336.0     0.7901  0.8065  0.7982
         STATE   178.0   28.0   27.0   205.0     0.8641  0.8683  0.8662
        STREET   408.0   22.0    7.0   415.0     0.9488  0.9831  0.9657
      USERNAME    87.0    4.0   14.0   101.0     0.956   0.8614  0.9063
           ZIP   129.0    3.0   10.0   139.0     0.9773  0.9281  0.952
         macro     -       -      -      -         -        -    0.8916
         micro     -       -      -      -         -        -    0.94
```
