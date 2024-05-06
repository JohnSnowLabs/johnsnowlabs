---
layout: model
title: Explain Clinical Document - Granular
author: John Snow Labs
name: explain_clinical_doc_granular
date: 2024-05-06
tags: [licensed, en, entity_resolution, relation_extraction, assertion_status, clinical, pipeline, granular]
task: [Pipeline Healthcare, Named Entity Recognition, Assertion Status, Relation Extraction]
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to:

- extract clinical entities
- assign assertion status to the extracted entities
- establish relations between the extracted entities

from clinical texts. In this pipeline, [ner_jsl]() NER model, [assertion_jsl]() assertion model, [re_test_result_date](), and posology_re()[https://nlp.johnsnowlabs.com/2020/09/01/posology_re.html] relation extraction model were used to achieve those tasks. Here are the NER, assertion, and relation extraction labels this pipeline can extract.

- Clinical Entity Labels:
`Admission_Discharge`
`Age`
`Alcohol`
`Allergen`
`BMI`
`Birth_Entity`
`Blood_Pressure`
`Cerebrovascular_Disease`
`Clinical_Dept`
`Communicable_Disease`
`Date`
`Death_Entity`
`Diabetes`
`Diet`
`Direction`
`Disease_Syndrome_Disorder`
`Dosage`
`Drug_BrandName`
`Drug_Ingredient`
`Duration`
`EKG_Findings`
`Employment`
`External_body_part_or_region`
`Family_History_Header`
`Fetus_NewBorn`
`Form`
`Frequency`
`Gender`
`HDL`
`Heart_Disease`
`Height`
`Hyperlipidemia`
`Hypertension`
`ImagingFindings`
`Imaging_Technique`
`Injury_or_Poisoning`
`Internal_organ_or_component`
`Kidney_Disease`
`LDL`
`Labour_Delivery`
`Medical_Device`
`Medical_History_Header`
`Modifier`
`O2_Saturation`
`Obesity`
`Oncological`
`Overweight`
`Oxygen_Therapy`
`Pregnancy`
`Procedure`
`Psychological_Condition`
`Pulse`
`Race_Ethnicity`
`Relationship_Status`
`RelativeDate`
`RelativeTime`
`Respiration`
`Route`
`Section_Header`
`Sexually_Active_or_Sexual_Orientation`
`Smoking`
`Social_History_Header`
`Strength`
`Substance`
`Substance_Quantity`
`Symptom`
`Temperature`
`Test`
`Test_Result`
`Time`
`Total_Cholesterol`
`Treatment`
`Triglycerides`
`VS_Finding`
`Vaccine`
`Vaccine_Name`
`Vital_Signs_Header`
`Weight`

- Assertion Status Labels: `Hypothetical`, `Someoneelse`, `Past`, `Absent`, `Family`, `Planned`, `Possible`, `Present`

- Relation Extraction Labels: `is_finding_of`, `is_date_of`, `is_result_of`, `O`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_granular_en_5.3.1_3.0_1714994735262.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_granular_en_5.3.1_3.0_1714994735262.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_granular", "en", "clinical/models")

result = ner_pipeline.annotate("""The patient admitted for gastrointestinal pathology, under working treatment.
History of prior heart murmur with echocardiogram findings as above on March 1998.
According to the latest echocardiogram, basically revealed normal left ventricular function with left atrial enlargement .
Based on the above findings, we will treat her medically with ACE inhibitors and diuretics and see how she fares.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_granular", "en", "clinical/models")

val result = ner_pipeline.annotate("""The patient admitted for gastrointestinal pathology, under working treatment.
History of prior heart murmur with echocardiogram findings as above on March 1998.
According to the latest echocardiogram, basically revealed normal left ventricular function with left atrial enlargement .
Based on the above findings, we will treat her medically with ACE inhibitors and diuretics and see how she fares.""")

```
</div>

## Results

```bash


# ner
+-----------+-----+---+--------------------------+-------------------+
|sentence_id|begin|end|entity                    |label              |
+-----------+-----+---+--------------------------+-------------------+
|0          |12   |19 |admitted                  |Admission_Discharge|
|0          |25   |50 |gastrointestinal pathology|Clinical_Dept      |
|1          |95   |106|heart murmur              |Heart_Disease      |
|1          |113  |126|echocardiogram            |Test               |
|1          |149  |158|March 1998                |Date               |
|2          |185  |198|echocardiogram            |Test               |
|2          |220  |225|normal                    |Test_Result        |
|2          |227  |251|left ventricular function |Test               |
|2          |258  |280|left atrial enlargement   |Heart_Disease      |
|3          |327  |329|her                       |Gender             |
|3          |346  |359|ACE inhibitors            |Drug_Ingredient    |
|3          |365  |373|diuretics                 |Drug_Ingredient    |
|3          |387  |389|she                       |Gender             |
+-----------+-----+---+--------------------------+-------------------+

# assertion

+-----------+-----+---+-------------------------+---------------+----------------+
|sentence_id|begin|end|entity                   |label          |assertion_status|
+-----------+-----+---+-------------------------+---------------+----------------+
|1          |95   |106|heart murmur             |Heart_Disease  |Past            |
|1          |113  |126|echocardiogram           |Test           |Past            |
|2          |185  |198|echocardiogram           |Test           |Present         |
|2          |220  |225|normal                   |Test_Result    |Present         |
|2          |227  |251|left ventricular function|Test           |Present         |
|2          |258  |280|left atrial enlargement  |Heart_Disease  |Present         |
|3          |346  |359|ACE inhibitors           |Drug_Ingredient|Planned         |
|3          |365  |373|diuretics                |Drug_Ingredient|Planned         |
+-----------+-----+---+-------------------------+---------------+----------------+

# relation

+-----------+-------------+-----------------+-------------------------+-----------------+-------------------------+
|sentence_id|relations    |relations_entity1|relations_chunk1         |relations_entity2|relations_chunk2         |
+-----------+-------------+-----------------+-------------------------+-----------------+-------------------------+
|1          |is_finding_of|Heart_Disease    |heart murmur             |Test             |echocardiogram           |
|1          |is_date_of   |Heart_Disease    |heart murmur             |Date             |March 1998               |
|1          |is_date_of   |Test             |echocardiogram           |Date             |March 1998               |
|2          |is_finding_of|Test             |echocardiogram           |Heart_Disease    |left atrial enlargement  |
|2          |is_result_of |Test_Result      |normal                   |Test             |left ventricular function|
|2          |is_finding_of|Test             |left ventricular function|Heart_Disease    |left atrial enlargement  |
+-----------+-------------+-----------------+-------------------------+-----------------+-------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_granular|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.1+|
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
- NerConverterInternalModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel
- PosologyREModel
- AnnotationMerger