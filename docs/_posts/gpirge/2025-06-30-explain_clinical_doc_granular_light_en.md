---
layout: model
title: Explain Clinical Document Granular - Light
author: John Snow Labs
name: explain_clinical_doc_granular_light
date: 2025-06-30
tags: [licensed, en, clinical, pipeline, ner, relations]
task: [Pipeline Healthcare, Named Entity Recognition, Relation Extraction]
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to extract clinical entities and establish relations between the extracted entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_granular_light_en_6.0.2_3.4_1751293267057.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_granular_light_en_6.0.2_3.4_1751293267057.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_granular_light", "en", "clinical/models")

result = ner_pipeline.annotate("""The patient admitted for gastrointestinal pathology, under working treatment.
History of prior heart murmur with echocardiogram findings as above on March 1998.
According to the last echocardiogram, basically reveals normal left ventricular function, and left atrial enlargement .
Based on the above findings, we will treat her medically with ACE inhibitors 10 mg, p.o, daily. Also we will give Furosemide 40 mg, p.o later and see how she fares. """)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_granular_light", "en", "clinical/models")

val result = ner_pipeline.annotate("""The patient admitted for gastrointestinal pathology, under working treatment.
History of prior heart murmur with echocardiogram findings as above on March 1998.
According to the last echocardiogram, basically reveals normal left ventricular function, and left atrial enlargement .
Based on the above findings, we will treat her medically with ACE inhibitors 10 mg, p.o, daily. Also we will give Furosemide 40 mg, p.o later and see how she fares. """)

```
</div>

## Results

```bash

# ner_chunk

+-----------+-----+---+--------------------------+-------------------+
|sentence_id|begin|end|entity                    |label              |
+-----------+-----+---+--------------------------+-------------------+
|0          |13   |20 |admitted                  |Admission_Discharge|
|0          |26   |51 |gastrointestinal pathology|Clinical_Dept      |
|1          |96   |107|heart murmur              |Heart_Disease      |
|1          |114  |127|echocardiogram            |Test               |
|1          |150  |159|March 1998                |Date               |
|2          |162  |175|Echocardiogram            |Test               |
|2          |182  |186|today                     |RelativeDate       |
|2          |198  |222|left ventricular function |Test               |
|2          |227  |232|normal                    |Test_Result        |
|2          |238  |260|left atrial enlargement   |Heart_Disease      |
|3          |306  |308|her                       |Gender             |
|3          |325  |338|ACE inhibitors            |Drug_Ingredient    |
|3          |340  |344|10 mg                     |Strength           |
|3          |347  |349|p.o                       |Route              |
|3          |352  |356|daily                     |Frequency          |
|4          |377  |386|Furosemide                |Drug_Ingredient    |
|4          |388  |392|40 mg                     |Strength           |
|4          |395  |397|p.o                       |Route              |
|4          |417  |419|she                       |Gender             |
+-----------+-----+---+--------------------------+-------------------+

# relation

+-----------+-------------------------+---------------------+-------------------------+---------------------+-------------------------+--------------------------+----------------------------------+---------------------------------+----------------------------------+---------------------------------+-------------------------+--------------------------+-------------------------+--------------------------+-------------------------+
|sentence_id|all_relations            |all_relations_entity1|all_relations_chunk1     |all_relations_entity2|all_relations_chunk2     |test_result_date_relations|test_result_date_relations_entity1|test_result_date_relations_chunk1|test_result_date_relations_entity2|test_result_date_relations_chunk2|posology_relations       |posology_relations_entity1|posology_relations_chunk1|posology_relations_entity2|posology_relations_chunk2|
+-----------+-------------------------+---------------------+-------------------------+---------------------+-------------------------+--------------------------+----------------------------------+---------------------------------+----------------------------------+---------------------------------+-------------------------+--------------------------+-------------------------+--------------------------+-------------------------+
|1          |is_finding_of            |Heart_Disease        |heart murmur             |Test                 |echocardiogram           |is_finding_of             |Heart_Disease                     |heart murmur                     |Test                              |echocardiogram                   |Drug_Ingredient-Strength |Drug_Ingredient           |ACE inhibitors           |Strength                  |10 mg                    |
|1          |is_date_of               |Heart_Disease        |heart murmur             |Date                 |March 1998               |is_date_of                |Heart_Disease                     |heart murmur                     |Date                              |March 1998                       |Drug_Ingredient-Route    |Drug_Ingredient           |ACE inhibitors           |Route                     |p.o                      |
|1          |is_date_of               |Test                 |echocardiogram           |Date                 |March 1998               |is_date_of                |Test                              |echocardiogram                   |Date                              |March 1998                       |Drug_Ingredient-Frequency|Drug_Ingredient           |ACE inhibitors           |Frequency                 |daily                    |
|2          |is_date_of               |Test                 |Echocardiogram           |RelativeDate         |today                    |is_date_of                |Test                              |Echocardiogram                   |RelativeDate                      |today                            |Drug_Ingredient-Strength |Drug_Ingredient           |Furosemide               |Strength                  |40 mg                    |
|2          |is_finding_of            |Test                 |Echocardiogram           |Heart_Disease        |left atrial enlargement  |is_finding_of             |Test                              |Echocardiogram                   |Heart_Disease                     |left atrial enlargement          |null                     |null                      |null                     |null                      |null                     |
|2          |is_date_of               |RelativeDate         |today                    |Test                 |left ventricular function|is_date_of                |RelativeDate                      |today                            |Test                              |left ventricular function        |null                     |null                      |null                     |null                      |null                     |
|2          |is_date_of               |RelativeDate         |today                    |Test_Result          |normal                   |is_date_of                |RelativeDate                      |today                            |Test_Result                       |normal                           |null                     |null                      |null                     |null                      |null                     |
|2          |is_date_of               |RelativeDate         |today                    |Heart_Disease        |left atrial enlargement  |is_date_of                |RelativeDate                      |today                            |Heart_Disease                     |left atrial enlargement          |null                     |null                      |null                     |null                      |null                     |
|2          |is_result_of             |Test                 |left ventricular function|Test_Result          |normal                   |is_result_of              |Test                              |left ventricular function        |Test_Result                       |normal                           |null                     |null                      |null                     |null                      |null                     |
|2          |is_finding_of            |Test                 |left ventricular function|Heart_Disease        |left atrial enlargement  |is_finding_of             |Test                              |left ventricular function        |Heart_Disease                     |left atrial enlargement          |null                     |null                      |null                     |null                      |null                     |
|3          |Drug_Ingredient-Strength |Drug_Ingredient      |ACE inhibitors           |Strength             |10 mg                    |null                      |null                              |null                             |null                              |null                             |null                     |null                      |null                     |null                      |null                     |
|3          |Drug_Ingredient-Route    |Drug_Ingredient      |ACE inhibitors           |Route                |p.o                      |null                      |null                              |null                             |null                              |null                             |null                     |null                      |null                     |null                      |null                     |
|3          |Drug_Ingredient-Frequency|Drug_Ingredient      |ACE inhibitors           |Frequency            |daily                    |null                      |null                              |null                             |null                              |null                             |null                     |null                      |null                     |null                      |null                     |
|4          |Drug_Ingredient-Strength |Drug_Ingredient      |Furosemide               |Strength             |40 mg                    |null                      |null                              |null                             |null                              |null                             |null                     |null                      |null                     |null                      |null                     |
|4          |Drug_Ingredient-Route    |Drug_Ingredient      |Furosemide               |Route                |p.o                      |null                      |null                              |null                             |null                              |null                             |null                     |null                      |null                     |null                      |null                     |
+-----------+-------------------------+---------------------+-------------------------+---------------------+-------------------------+--------------------------+----------------------------------+---------------------------------+----------------------------------+---------------------------------+-------------------------+--------------------------+-------------------------+--------------------------+-------------------------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_granular_light|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel
- PosologyREModel
