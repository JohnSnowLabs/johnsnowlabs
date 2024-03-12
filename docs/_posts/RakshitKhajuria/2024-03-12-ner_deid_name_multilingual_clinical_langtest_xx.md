---
layout: model
title: Detect Name for Deidentification Multilingual (LangTest)
author: John Snow Labs
name: ner_deid_name_multilingual_clinical_langtest
date: 2024-03-12
tags: [licensed, ner, clinical, langtest, multilingual, deid, name, xx]
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

This model detects name entities in clinical documents. It is the version of  [ner_deid_name_multilingual_clinical](https://nlp.johnsnowlabs.com/2024/02/12/ner_deid_name_multilingual_clinical_xx.html) model augmented with `langtest` library. 

| **test_type**             | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|---------------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**          | 165                   | 139                  | 2337                  | 2363                 | 95%                   | 93%                  | 94%                 |
| **lowercase**             | 3282                  | 1135                 | 1762                  | 3909                 | 95%                   | 35%                  | 77%                 |
| **titlecase**             | 1799                  | 840                  | 3165                  | 4124                 | 95%                   | 64%                  | 83%                 |
| **add_abbreviation**      | 74                    | 73                   | 1343                  | 1344                 | 95%                   | 95%                  | 95%                 |
| **strip_all_punctuation** | 654                   | 655                  | 4320                  | 4319                 | 95%                   | 87%                  | 87%                 |
| **uppercase**             | 2481                  | 1252                 | 2488                  | 3717                 | 95%                   | 50%                  | 75%                 |

## Predicted Entities

`NAME`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_name_multilingual_clinical_langtest_xx_5.2.1_3.0_1710268198235.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_name_multilingual_clinical_langtest_xx_5.2.1_3.0_1710268198235.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols("sentence","token")\
    .setOutputCol("embeddings")

ner = MedicalNerModel.pretrained(''ner_deid_name_multilingual_clinical_langtest", "xx", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverterInternal() \
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

text_list = ["""Record date: 2093-01-13, David Hale, M.D., Name: Hendrickson, Ora MR. # 7194334 Date: 01/13/93 PCP: Oliveira, 25 years old, Record date: 1-11-2000. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 (302) 786-5227. The patient's complaints first surfaced when he started working for Brothers Coal-Mine.""",
             
"""J'ai vu en consultation Michel Martinez (49 ans) adressé au Centre Hospitalier De Plaisir pour un diabète mal contrôlé avec des symptômes datant de Mars 2015.""",
             
"""Michael Berger wird am Morgen des 12 Dezember 2018 ins St. Elisabeth-Krankenhaus in Bad Kissingen eingeliefert. Herr Berger ist 76 Jahre alt und hat zu viel Wasser in den Beinen.""",

"""Ho visto Gastone Montanariello (49 anni) riferito all' Ospedale San Camillo per diabete mal controllato con sintomi risalenti a marzo 2015.""",

"""Antonio Miguel Martínez, un varón de 35 años de edad, de profesión auxiliar de enfermería y nacido en Cadiz, España. Aún no estaba vacunado, se infectó con Covid-19 el dia 14 de Marzo y tuvo que ir al Hospital. Fue tratado con anticuerpos monoclonales en la Clinica San Carlos.""",
    
"""
Detalhes do paciente:
Nome do paciente: Pedro Gonçalves NHC: 2569870 Endereço: Rua Das Flores 23. Cidade/ Província: Porto Código Postal: 21754-987 Dados de cuidados Data de nascimento: 10/10/1963 Idade: 53 anos Data de admissão: 17/06/2016 Doutora: Maria Santos""",

"""Spitalul Pentru Ochi de Deal, Drumul Oprea Nr. 972 Vaslui, 737405 România Tel: +40(235)413773 Data setului de analize: 25 May 2022 15:36:00 Nume&Prenume: BUREAN MARIA, Varsta: 77 CNP: 2450502264401"""
]

data = spark.createDataFrame(pd.DataFrame({"text": text_list}))

result = model.transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer() 
    .setInputCols("sentence") 
    .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_deid_name_multilingual_clinical_langtest", "xx", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings")) 
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal() 
    .setInputCols(Array("sentence", "token", "ner")) 
    .setOutputCol("ner_chunk")
    
val pipeline = new Pipeline().setStages(Array(document_assembler,
                            sentence_detector,
                            tokenizer,
                            embeddings,
                            ner,
                            ner_converter))

val text_list = Seq(
"""Record date: 2093-01-13, David Hale, M.D., Name: Hendrickson, Ora MR. # 7194334 Date: 01/13/93 PCP: Oliveira, 25 years old, Record date: 1-11-2000. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 (302) 786-5227. The patient's complaints first surfaced when he started working for Brothers Coal-Mine.""",
             
"""J'ai vu en consultation Michel Martinez (49 ans) adressé au Centre Hospitalier De Plaisir pour un diabète mal contrôlé avec des symptômes datant de Mars 2015.""",
             
"""Michael Berger wird am Morgen des 12 Dezember 2018 ins St. Elisabeth-Krankenhaus in Bad Kissingen eingeliefert. Herr Berger ist 76 Jahre alt und hat zu viel Wasser in den Beinen.""",

"""Ho visto Gastone Montanariello (49 anni) riferito all' Ospedale San Camillo per diabete mal controllato con sintomi risalenti a marzo 2015.""",

"""Antonio Miguel Martínez, un varón de 35 años de edad, de profesión auxiliar de enfermería y nacido en Cadiz, España. Aún no estaba vacunado, se infectó con Covid-19 el dia 14 de Marzo y tuvo que ir al Hospital. Fue tratado con anticuerpos monoclonales en la Clinica San Carlos.""",
    
"""
Detalhes do paciente:
Nome do paciente: Pedro Gonçalves NHC: 2569870 Endereço: Rua Das Flores 23. Cidade/ Província: Porto Código Postal: 21754-987 Dados de cuidados Data de nascimento: 10/10/1963 Idade: 53 anos Data de admissão: 17/06/2016 Doutora: Maria Santos""",

"""Spitalul Pentru Ochi de Deal, Drumul Oprea Nr. 972 Vaslui, 737405 România Tel: +40(235)413773 Data setului de analize: 25 May 2022 15:36:00 Nume&Prenume: BUREAN MARIA, Varsta: 77 CNP: 2450502264401"""
)

val data = Seq(text_list).toDF("text")

val result = model.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------+-----+---+---------+
|              ner_chunk|begin|end|ner_label|
+-----------------------+-----+---+---------+
|             David Hale|   25| 34|     NAME|
|       Hendrickson, Ora|   49| 64|     NAME|
|     Brothers Coal-Mine|  291|308|     NAME|
|        Michel Martinez|   24| 38|     NAME|
|         Michael Berger|    0| 13|     NAME|
|                 Berger|  117|122|     NAME|
|  Gastone Montanariello|    9| 29|     NAME|
|Antonio Miguel Martínez|    0| 22|     NAME|
|        Pedro Gonçalves|   41| 55|     NAME|
|           Maria Santos|  251|262|     NAME|
|           BUREAN MARIA|  154|165|     NAME|
+-----------------------+-----+---+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_name_multilingual_clinical_langtest|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|xx|
|Size:|14.8 MB|

## Benchmarking

```bash
       label    precision     recall  f1-score   support 
      B-NAME         0.90       0.90      0.90      4986    
      I-NAME         0.91       0.93      0.92      4059    
   micro-avg         0.90       0.92      0.91      9045    
   macro-avg         0.91       0.92      0.91      9045    
weighted-avg         0.90       0.92      0.91      9045    
```