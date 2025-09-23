---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_deid_generic_multi_large)
author: John Snow Labs
name: zeroshot_ner_deid_generic_multi_large
date: 2024-12-21
tags: [licensed, ner, multilingual, xx, deidentification, zeroshot, clinical]
task: Named Entity Recognition
language: xx
edition: Healthcare NLP 5.5.1
spark_version: 3.0
supported: true
annotator: PretrainedZeroShotNER
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Zero-shot Named Entity Recognition (NER) enables the identification of entities in text with minimal effort. By leveraging pre-trained language models and contextual understanding, zero-shot NER extends entity recognition capabilities to new domains and languages. While the model card includes default labels as examples, it is important to highlight that users are not limited to these labels.

**The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. For best results, it is recommended to use labels that are conceptually similar to the provided defaults.**

## Predicted Entities

`AGE`, `CONTACT`, `DATE`, `ID`, `LOCATION`, `NAME`, `PROFESSION`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/01.4.ZeroShot_Clinical_NER.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_generic_multi_large_xx_5.5.1_3.0_1734800769281.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_generic_multi_large_xx_5.5.1_3.0_1734800769281.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

labels = ['AGE', 'CONTACT', 'DATE', 'ID', 'LOCATION', 'NAME', 'PROFESSION'] # You can change the entities
pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_generic_multi_large", "xx", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("ner")\
    .setPredictionThreshold(0.5)\
    .setLabels(labels)

ner_converter = NerConverterInternal()\
    .setInputCols("sentence", "token", "ner")\
    .setOutputCol("ner_chunk")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
])

text_list = [
"""Record date : 2093-01-13, David Hale, M.D., Name : Hendrickson, Ora MR. # 7194334 Date : 01/13/93 PCP : Oliveira, 25 years old, Record date : 1-11-2000. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 (302) 786-5227. Patient's complaints first surfaced when he started working for Brothers Coal-Mine.""",

"""J'ai vu en consultation Michel Martinez (49 ans) adressé au Centre Hospitalier De Plaisir pour un diabète mal contrôlé avec des symptômes datant de Mars 2015.""",

"""Michael Berger wird am Morgen des 12 Dezember 2018 ins St. Elisabeth-Krankenhaus in Bad Kissingen eingeliefert. Herr Berger ist 76 Jahre alt und hat zu viel Wasser in den Beinen.""",

"""Ho visto Gastone Montanariello (49 anni) riferito all' Ospedale San Camillo per diabete mal controllato con sintomi risalenti a marzo 2015.""",

"""Antonio Miguel Martínez, un varón de 35 años de edad, de profesión auxiliar de enfermería y nacido en Cadiz, España. Aún no estaba vacunado, se infectó con Covid-19 el dia 14 de Marzo y tuvo que ir al Hospital. Fue tratado con anticuerpos monoclonales en la Clinica San Carlos.""",

"""Detalhes do paciente.
Nome do paciente:  Pedro Gonçalves
NHC: 2569870.
Endereço: Rua Das Flores 23.
Cidade/ Província: Porto.
Código Postal: 21754-987.
Dados de cuidados.
Data de nascimento: 10/10/1963.
Idade: 53 anos Sexo: Homen
Data de admissão: 17/06/2016.
Doutora: Maria Santos""",

"""Spitalul Pentru Ochi de Deal, Drumul Oprea Nr. 972 Vaslui, 737405 România
Tel: +40(235)413773
Data setului de analize: 25 May 2022 15:36:00
Nume si Prenume : BUREAN MARIA, Varsta: 77
Medic : Agota Evelyn Tımar
C.N.P : 2450502264401"""
]

data = spark.createDataFrame(pd.DataFrame({"text": text_list}))

result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

labels = ['AGE', 'CONTACT', 'DATE', 'ID', 'LOCATION', 'NAME', 'PROFESSION'] # You can change the entities
pretrained_zero_shot_ner = medical.PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_generic_multi_large", "xx", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("ner")\
    .setPredictionThreshold(0.5)\
    .setLabels(labels)

ner_converter = medical.NerConverterInternal()\
    .setInputCols("sentence", "token", "ner")\
    .setOutputCol("ner_chunk")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
])

text_list = [
"""Record date : 2093-01-13, David Hale, M.D., Name : Hendrickson, Ora MR. # 7194334 Date : 01/13/93 PCP : Oliveira, 25 years old, Record date : 1-11-2000. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 (302) 786-5227. Patient's complaints first surfaced when he started working for Brothers Coal-Mine.""",

"""J'ai vu en consultation Michel Martinez (49 ans) adressé au Centre Hospitalier De Plaisir pour un diabète mal contrôlé avec des symptômes datant de Mars 2015.""",

"""Michael Berger wird am Morgen des 12 Dezember 2018 ins St. Elisabeth-Krankenhaus in Bad Kissingen eingeliefert. Herr Berger ist 76 Jahre alt und hat zu viel Wasser in den Beinen.""",

"""Ho visto Gastone Montanariello (49 anni) riferito all' Ospedale San Camillo per diabete mal controllato con sintomi risalenti a marzo 2015.""",

"""Antonio Miguel Martínez, un varón de 35 años de edad, de profesión auxiliar de enfermería y nacido en Cadiz, España. Aún no estaba vacunado, se infectó con Covid-19 el dia 14 de Marzo y tuvo que ir al Hospital. Fue tratado con anticuerpos monoclonales en la Clinica San Carlos.""",

"""Detalhes do paciente.
Nome do paciente:  Pedro Gonçalves
NHC: 2569870.
Endereço: Rua Das Flores 23.
Cidade/ Província: Porto.
Código Postal: 21754-987.
Dados de cuidados.
Data de nascimento: 10/10/1963.
Idade: 53 anos Sexo: Homen
Data de admissão: 17/06/2016.
Doutora: Maria Santos""",

"""Spitalul Pentru Ochi de Deal, Drumul Oprea Nr. 972 Vaslui, 737405 România
Tel: +40(235)413773
Data setului de analize: 25 May 2022 15:36:00
Nume si Prenume : BUREAN MARIA, Varsta: 77
Medic : Agota Evelyn Tımar
C.N.P : 2450502264401"""
]

data = spark.createDataFrame(pd.DataFrame({"text": text_list}))

result = pipeline.fit(data).transform(data)

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

labels = ("AGE", "CONTACT", "DATE", "ID", "LOCATION", "NAME", "PROFESSION") # You can change the entities
val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_generic_multi_large", "xx", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("ner")
    .setPredictionThreshold(0.5)
    .setLabels(labels)

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
))

val text_list = Seq(Array(
"""Record date : 2093-01-13, David Hale, M.D., Name : Hendrickson, Ora MR. # 7194334 Date : 01/13/93 PCP : Oliveira, 25 years old, Record date : 1-11-2000. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 (302) 786-5227. Patient's complaints first surfaced when he started working for Brothers Coal-Mine.""",

"""J'ai vu en consultation Michel Martinez (49 ans) adressé au Centre Hospitalier De Plaisir pour un diabète mal contrôlé avec des symptômes datant de Mars 2015.""",

"""Michael Berger wird am Morgen des 12 Dezember 2018 ins St. Elisabeth-Krankenhaus in Bad Kissingen eingeliefert. Herr Berger ist 76 Jahre alt und hat zu viel Wasser in den Beinen.""",

"""Ho visto Gastone Montanariello (49 anni) riferito all' Ospedale San Camillo per diabete mal controllato con sintomi risalenti a marzo 2015.""",

"""Antonio Miguel Martínez, un varón de 35 años de edad, de profesión auxiliar de enfermería y nacido en Cadiz, España. Aún no estaba vacunado, se infectó con Covid-19 el dia 14 de Marzo y tuvo que ir al Hospital. Fue tratado con anticuerpos monoclonales en la Clinica San Carlos.""",

"""Detalhes do paciente.
Nome do paciente:  Pedro Gonçalves
NHC: 2569870.
Endereço: Rua Das Flores 23.
Cidade/ Província: Porto.
Código Postal: 21754-987.
Dados de cuidados.
Data de nascimento: 10/10/1963.
Idade: 53 anos Sexo: Homen
Data de admissão: 17/06/2016.
Doutora: Maria Santos""",

"""Spitalul Pentru Ochi de Deal, Drumul Oprea Nr. 972 Vaslui, 737405 România
Tel: +40(235)413773
Data setului de analize: 25 May 2022 15:36:00
Nume si Prenume : BUREAN MARIA, Varsta: 77
Medic : Agota Evelyn Tımar
C.N.P : 2450502264401"""
))

val data = Seq(text_list).toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-----------------------------+-----+---+----------+----------+
|chunk                        |begin|end|ner_label |confidence|
+-----------------------------+-----+---+----------+----------+
|2093-01-13                   |14   |23 |DATE      |0.99943763|
|David Hale                   |26   |35 |NAME      |0.99969995|
|Hendrickson, Ora             |51   |66 |NAME      |0.99995136|
|7194334                      |74   |80 |ID        |0.9970041 |
|01/13/93                     |89   |96 |DATE      |0.999616  |
|Oliveira                     |104  |111|NAME      |0.99986875|
|25                           |114  |115|AGE       |0.9996654 |
|1-11-2000                    |142  |150|DATE      |0.9997458 |
|Cocke County Baptist Hospital|153  |181|LOCATION  |0.99486864|
|0295 Keats Street            |184  |200|LOCATION  |0.99688274|
|+1 (302) 786-5227            |209  |225|CONTACT   |0.998147  |
|Brothers Coal-Mine           |292  |309|LOCATION  |0.9962675 |
|Michel Martinez              |24   |38 |NAME      |0.999997  |
|49 ans                       |41   |46 |AGE       |0.8242508 |
|Centre Hospitalier De Plaisir|60   |88 |LOCATION  |0.9999776 |
|Mars 2015                    |148  |156|DATE      |0.99994504|
|Michael Berger               |0    |13 |NAME      |0.9999294 |
|12 Dezember 2018             |34   |49 |DATE      |0.99977356|
|St. Elisabeth-Krankenhaus    |55   |79 |LOCATION  |0.9921251 |
|Bad Kissingen                |84   |96 |LOCATION  |0.99577075|
|Berger                       |117  |122|NAME      |0.9913891 |
|76                           |128  |129|AGE       |0.9999888 |
|Gastone Montanariello        |9    |29 |NAME      |0.99999213|
|49                           |32   |33 |AGE       |0.9999839 |
|Ospedale San Camillo         |55   |74 |LOCATION  |0.9998891 |
|marzo 2015                   |128  |137|DATE      |0.9996381 |
|Antonio Miguel Martínez      |0    |22 |NAME      |0.9998452 |
|35                           |37   |38 |AGE       |0.9997782 |
|auxiliar de enfermería       |67   |88 |PROFESSION|0.9999606 |
|Cadiz                        |102  |106|LOCATION  |0.9994766 |
|España                       |109  |114|LOCATION  |0.9972957 |
|14 de Marzo                  |172  |182|DATE      |0.85703737|
|Hospital                     |201  |208|LOCATION  |0.9773244 |
|Clinica San Carlos           |258  |275|LOCATION  |0.99843866|
|Pedro Gonçalves              |41   |55 |NAME      |0.9999325 |
|2569870                      |62   |68 |ID        |0.99984646|
|Rua Das Flores 23            |81   |97 |LOCATION  |0.99988925|
|Porto                        |119  |123|LOCATION  |0.9989887 |
|21754-987                    |141  |149|CONTACT   |0.9996555 |
|10/10/1963                   |191  |200|DATE      |0.9999933 |
|53                           |210  |211|AGE       |0.9870047 |
|17/06/2016                   |248  |257|DATE      |0.9999876 |
|Maria Santos                 |269  |280|NAME      |0.9999502 |
|Spitalul Pentru Ochi de Deal |0    |27 |LOCATION  |0.9976414 |
|Drumul Oprea Nr. 972         |30   |49 |LOCATION  |0.9992417 |
|Vaslui                       |51   |56 |LOCATION  |0.9988475 |
|737405                       |59   |64 |LOCATION  |0.99923706|
|România                      |66   |72 |LOCATION  |0.9871066 |
|+40(235)413773               |79   |92 |CONTACT   |0.9994785 |
|25 May 2022                  |119  |129|DATE      |0.9999304 |
|BUREAN MARIA                 |158  |169|NAME      |0.99993825|
|77                           |180  |181|AGE       |0.9999943 |
|Agota Evelyn Tımar           |191  |208|NAME      |0.80123115|
|2450502264401                |218  |230|CONTACT   |0.9868976 |
+-----------------------------+-----+---+----------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_deid_generic_multi_large|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|xx|
|Size:|1.6 GB|

## Benchmarking

```bash

       label  precision    recall  f1-score   support
         AGE       0.97      0.98      0.97      3355
     CONTACT       0.95      0.86      0.90      1444
        DATE       0.85      0.97      0.91      2272
          ID       0.85      0.88      0.87       967
    LOCATION       0.91      0.92      0.92      7470
        NAME       0.95      0.95      0.95      5375
  PROFESSION       0.91      0.93      0.92      2698
    accuracy          -         -      0.98    140265
   macro avg       0.92      0.93      0.93    140265
weighted avg       0.98      0.98      0.98    140265

```
