---
layout: model
title: Detect PHI for Generic Deidentification(multilingual)
author: John Snow Labs
name: ner_deid_multilingual
date: 2024-02-12
tags: [ner, licensed, deid, multilingual, xx, roberta]
task: Named Entity Recognition
language: xx
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Deidentification NER is a Named Entity Recognition model that annotates English, German, French, Italian, Spanish, Portuguese, and Romanian text to find protected health information (PHI) that may need to be de-identified. It has been trained with in-house annotated datasets using `xlm-roberta-base` multilingual embeddings.

## Predicted Entities

`AGE`, `CONTACT`, `DATE`, `ID`, `LOCATION`, `NAME`, `PROFESSION`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_multilingual_xx_5.2.1_3.0_1707781448758.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_multilingual_xx_5.2.1_3.0_1707781448758.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

embeddings = XlmRoBertaEmbeddings.pretrained("xlm_roberta_base", "xx") \
    .setInputCols("sentence", "token") \
    .setOutputCol("embeddings")\
    .setMaxSentenceLength(512)\

ner = MedicalNerModel.pretrained("ner_deid_multilingual", "xx", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

nlpPipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            embeddings,
                            ner,
                            ner_converter])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

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

result = model.transform(data)


```
```scala
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val embeddings = XlmRoBertaEmbeddings.pretrained("xlm_roberta_base", "xx")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")
  .setMaxSentenceLength(512)

val ner = MedicalNerModel.pretrained("ner_deid_multilingual", "xx", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")

val nerConverter = new NerConverter()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")

val nlpPipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  ner,
  nerConverter))

val text_list = Seq(
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
)

val data = Seq(text_list).toDS.toDF("text")

val result = nlpPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------------+----------+
|chunk                        |ner_label |
+-----------------------------+----------+
|2093-01-13                   |DATE      |
|David Hale                   |NAME      |
|Hendrickson                  |NAME      |
|7194334                      |ID        |
|01/13/93                     |DATE      |
|Oliveira                     |NAME      |
|25                           |AGE       |
|1-11-2000                    |DATE      |
|Cocke County Baptist Hospital|LOCATION  |
|0295 Keats Street            |LOCATION  |
|(302) 786-5227               |CONTACT   |
|Brothers Coal-Mine           |LOCATION  |
|Michel Martinez              |NAME      |
|49 ans                       |AGE       |
|Centre Hospitalier De Plaisir|LOCATION  |
|Mars 2015                    |DATE      |
|Michael Berger               |NAME      |
|Bad Kissingen                |LOCATION  |
|Berger                       |NAME      |
|76                           |AGE       |
|Gastone Montanariello        |NAME      |
|49                           |AGE       |
|Ospedale San Camillo         |LOCATION  |
|marzo 2015                   |DATE      |
|Antonio Miguel Martínez      |NAME      |
|35                           |AGE       |
|auxiliar de enfermería       |PROFESSION|
|Cadiz                        |LOCATION  |
|España                       |LOCATION  |
|14 de Marzo                  |DATE      |
|Clinica San Carlos           |LOCATION  |
|Pedro Gonçalves              |NAME      |
|2569870                      |ID        |
|Rua Das Flores               |NAME      |
|Porto                        |LOCATION  |
|21754-987                    |ID        |
|10/10/1963                   |DATE      |
|53                           |AGE       |
|17/06/2016                   |DATE      |
|Maria Santos                 |NAME      |
|Spitalul Pentru Ochi de Deal |LOCATION  |
|Drumul Oprea Nr              |LOCATION  |
|972                          |LOCATION  |
|Vaslui                       |LOCATION  |
|737405                       |LOCATION  |
|România                      |LOCATION  |
|+40(235)413773               |CONTACT   |
|25 May 2022                  |DATE      |
|BUREAN MARIA                 |NAME      |
|77                           |AGE       |
|Agota Evelyn Tımar           |NAME      |
|2450502264401                |ID        |
+-----------------------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_multilingual|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|xx|
|Size:|3.2 MB|

## References

In-house annotated datasets

## Benchmarking

```bash
label         precision  recall  f1-score  support 
AGE           0.96       0.97    0.97      2815    
CONTACT       0.96       0.94    0.95      835     
DATE          0.94       0.90    0.92      1255    
ID            0.92       0.92    0.92      857     
LOCATION      0.82       0.81    0.81      3144    
NAME          0.91       0.86    0.88      2769    
PROFESSION    0.90       0.79    0.84      1414    
micro-avg     0.90       0.88    0.89      13089   
macro-avg     0.92       0.88    0.90      13089   
weighted-avg  0.90       0.88    0.89      13089   
```