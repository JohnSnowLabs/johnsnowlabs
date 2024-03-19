---
layout: model
title: Explain Clinical Document - Public Health
author: John Snow Labs
name: explain_clinical_doc_public_health
date: 2024-03-19
tags: [licensed, en, public_health, pipeline, ner, assertion, relation_extraction]
task: [Named Entity Recognition, Assertion Status, Relation Extraction, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This specialized public health pipeline can;

- extract public health related entities,

- assign assertion status to the extracted entities,

- establish relations between the extracted entities from the clinical documents.

In this pipeline, five NER, one assertion and one relation extraction model were used to achieve those tasks.



- **Entity Labels:** `Access_To_Care`, `Community_Safety`, `Overweight`, `Pregnancy`, `Environmental_Condition`, `Employment`, `Financial_Status`, `Food_Insecurity`, `Geographic_Entity`, `Healthcare_Institution`, `Obesity` ,`Race_Ethnicity`, `Population_Group`,  `Insurance_Status`, `Legal_Issues`, `Mental_Health`, `Smoking`, `Quality_Of_Life`, `Social_Exclusion`, `Social_Support`, `Spiritual_Beliefs`, `Substance`, `Violence_Or_Abuse`, `Education`, `Housing`, `Alcohol`, `Disease_Syndrome_Disorder`, `Diet`,`Relationship_Status`, `Drug`, `Alcohol`, `Psychological_Condition`, `Employment`, `Disease_Syndrome_Disorder`, `Substance`, `Substance_Quantity`, `Sexually_Active_or_Sexual_Orientation`, `Injury_or_Poisoning`, `Obesity`, `BMI`, `Blood_pressure`, `HDL`, `Smoking`

- **Assertion Status Labels:**  `Hypothetical_Or_Absent`, `Present_Or_Past`, `SomeoneElse`

- **Relation Extraction Labels:** Given Relation Pairs : `Disease_Syndrome_Disorder-Drug`, `Drug-Disease_Syndrome_Disorder`, `Drug-Mental_Healt`,`Mental_Health-Drug`, `Allergen-Drug`, `Drug-Allergen`,  `Psychological_Condition-Drug`, `Drug-Psychological_Condition`, `BMI-Obesity`, `Obesity-BMI` , `Alcohol-Substance_Quantity`, `Substance_Quantity-Alcohol`, `Smoking-Substance_Quantity`, `Substance_Quantity-Smoking`, `Substance-Substance_Quantity`, `Substance_Quantity-Substance`])

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_public_health_en_5.3.0_3.2_1710864403939.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_public_health_en_5.3.0_3.2_1710864403939.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

resolver_pipeline = PretrainedPipeline("explain_clinical_doc_public_health", "en", "clinical/models")

result = resolver_pipeline.annotate(""" Social History: Patient is a 38 year old Chinese man, construction worker, often exposed to dust, fumes. He is a former smoker, having quit it 10 years ago after smoking a pack a day for 15 years. He occasionally consumes alcohol on weekends . He reports struggles with maintaining a healthy diet due to time constraints and limited access to fresh foods in his neighborhood. Obesity: BMI 32; struggles with weight management. 
Public Health Related Factors: John's occupation as a construction worker exposes him to various occupational hazards, including dust, which may contribute to his respiratory symptoms. While John quit smoking a decade ago, his previous smoking habit puts him at an increased risk for respiratory.
Socioeconomic Factors: John's socioeconomic status, characterized by his occupation as a construction worker and residing in an area with limited access to healthy foods, may impact his ability to maintain a healthy lifestyle and access healthcare services. By addressing John's medical concerns within the context of his occupational and social history, we can provide comprehensive care that not only treats his current symptoms but also promotes his long-term health and well-being. 
Medications: Lisinopril (ACE inhibitor) for hypertension.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val resolver_pipeline = PretrainedPipeline("explain_clinical_doc_public_health", "en", "clinical/models")

val result = resolver_pipeline.annotate(""" Social History: Patient is a 38 year old Chinese man, construction worker, often exposed to dust, fumes. He is a former smoker, having quit it 10 years ago after smoking a pack a day for 15 years. He occasionally consumes alcohol on weekends . He reports struggles with maintaining a healthy diet due to time constraints and limited access to fresh foods in his neighborhood. Obesity: BMI 32; struggles with weight management. 
Public Health Related Factors: John's occupation as a construction worker exposes him to various occupational hazards, including dust, which may contribute to his respiratory symptoms. While John quit smoking a decade ago, his previous smoking habit puts him at an increased risk for respiratory.
Socioeconomic Factors: John's socioeconomic status, characterized by his occupation as a construction worker and residing in an area with limited access to healthy foods, may impact his ability to maintain a healthy lifestyle and access healthcare services. By addressing John's medical concerns within the context of his occupational and social history, we can provide comprehensive care that not only treats his current symptoms but also promotes his long-term health and well-being. 
Medications: Lisinopril (ACE inhibitor) for hypertension.
""")

```
</div>

## Results

```bash


# NER Result

|    |   sentence_id | chunks                     |   begin |   end | entities                  |
|---:|--------------:|:---------------------------|--------:|------:|:--------------------------|
|  0 |             0 | Chinese                    |      42 |    48 | Race_Ethnicity            |
|  1 |             0 | construction worker        |      55 |    73 | Employment                |
|  2 |             1 | smoker                     |     121 |   126 | Smoking                   |
|  3 |             1 | smoking                    |     163 |   169 | Smoking                   |
|  4 |             1 | a pack                     |     171 |   176 | Substance_Quantity        |
|  5 |             2 | alcohol                    |     223 |   229 | Alcohol                   |
|  6 |             3 | healthy diet               |     285 |   296 | Diet                      |
|  7 |             3 | fresh foods                |     344 |   354 | Food_Insecurity           |
|  8 |             4 | Obesity                    |     377 |   383 | Obesity                   |
|  9 |             4 | BMI 32                     |     386 |   391 | BMI                       |
| 10 |             5 | construction worker        |     483 |   501 | Employment                |
| 11 |             6 | smoking                    |     630 |   636 | Smoking                   |
| 12 |             6 | smoking                    |     665 |   671 | Smoking                   |
| 13 |             7 | construction worker        |     815 |   833 | Employment                |
| 14 |             7 | healthy foods              |     882 |   894 | Food_Insecurity           |
| 15 |             7 | access healthcare services |     956 |   981 | Access_To_Care            |
| 16 |             8 | comprehensive care         |    1096 |  1113 | Access_To_Care            |
| 17 |             8 | well-being                 |    1200 |  1209 | Quality_Of_Life           |
| 18 |             9 | Lisinopril                 |    1226 |  1235 | Drug                      |
| 19 |             9 | ACE inhibitor              |    1238 |  1250 | Drug                      |
| 20 |             9 | hypertension               |    1257 |  1268 | Disease_Syndrome_Disorder |

# Assertion Result

|    |   sentence_id | chunks                     |   begin |   end | entities                  | assertion              |
|---:|--------------:|:---------------------------|--------:|------:|:--------------------------|:-----------------------|
|  0 |             0 | construction worker        |      55 |    73 | Employment                | Present_Or_Past        |
|  1 |             1 | smoker                     |     121 |   126 | Smoking                   | Present_Or_Past        |
|  2 |             1 | smoking                    |     163 |   169 | Smoking                   | Present_Or_Past        |
|  3 |             2 | alcohol                    |     223 |   229 | Alcohol                   | Hypothetical_Or_Absent |
|  4 |             3 | healthy diet               |     285 |   296 | Diet                      | Hypothetical_Or_Absent |
|  5 |             3 | fresh foods                |     344 |   354 | Food_Insecurity           | Present_Or_Past        |
|  6 |             4 | Obesity                    |     377 |   383 | Obesity                   | Hypothetical_Or_Absent |
|  7 |             4 | BMI 32                     |     386 |   391 | Obesity                   | Present_Or_Past        |
|  8 |             5 | construction worker        |     483 |   501 | Employment                | Present_Or_Past        |
|  9 |             6 | smoking                    |     630 |   636 | Smoking                   | Present_Or_Past        |
| 10 |             6 | smoking                    |     665 |   671 | Smoking                   | Present_Or_Past        |
| 11 |             7 | construction worker        |     815 |   833 | Employment                | Present_Or_Past        |
| 12 |             7 | healthy foods              |     882 |   894 | Food_Insecurity           | Present_Or_Past        |
| 13 |             7 | access healthcare services |     956 |   981 | Access_To_Care            | Hypothetical_Or_Absent |
| 14 |             8 | comprehensive care         |    1096 |  1113 | Access_To_Care            | Present_Or_Past        |
| 15 |             8 | well-being                 |    1200 |  1209 | Quality_Of_Life           | Present_Or_Past        |
| 16 |             9 | hypertension               |    1257 |  1268 | Disease_Syndrome_Disorder | Hypothetical_Or_Absent |

# Relation Extraction Result

|    |   sentence |   entity1_begin |   entity1_end | chunk1        | entity1   |   entity2_begin |   entity2_end | chunk2       | entity2                   | relation                       |   confidence |
|---:|-----------:|----------------:|--------------:|:--------------|:----------|----------------:|--------------:|:-------------|:--------------------------|:-------------------------------|-------------:|
|  0 |          1 |             121 |           126 | smoker        | Smoking   |             171 |           176 | a pack       | Substance_Quantity        | Smoking-Substance_Quantity     |            1 |
|  1 |          1 |             163 |           169 | smoking       | Smoking   |             171 |           176 | a pack       | Substance_Quantity        | Smoking-Substance_Quantity     |            1 |
|  2 |          4 |             377 |           383 | Obesity       | Obesity   |             386 |           391 | BMI 32       | BMI                       | Obesity-BMI                    |            1 |
|  3 |          9 |            1226 |          1235 | Lisinopril    | Drug      |            1257 |          1268 | hypertension | Disease_Syndrome_Disorder | Drug-Disease_Syndrome_Disorder |            1 |
|  4 |          9 |            1238 |          1250 | ACE inhibitor | Drug      |            1257 |          1268 | hypertension | Disease_Syndrome_Disorder | Drug-Disease_Syndrome_Disorder |            1 |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_public_health|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- ChunkMergeModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- GenericREModel