---
layout: model
title: Named Entity Recognition Profiling (Biobert)
author: John Snow Labs
name: ner_profiling_biobert
date: 2022-01-18
tags: [ner_profiling, ner, clinical, biobert, en, licensed]
task: Pipeline Healthcare
language: en
nav_key: models
edition: Healthcare NLP 3.3.1
spark_version: 2.4
supported: true
annotator: PipelineModel
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to explore all the available pretrained NER models at once. When you run this pipeline over your text, you will end up with the predictions coming out of each pretrained clinical NER model trained with `biobert_pubmed_base_cased`. It has been updated by adding NER model outputs to the previous version.

Here are the NER models that this pretrained pipeline includes: `ner_jsl_enriched_biobert`, `ner_clinical_biobert`, `ner_chemprot_biobert`, `ner_jsl_greedy_biobert`, `ner_bionlp_biobert`, `ner_human_phenotype_go_biobert`, `jsl_rd_ner_wip_greedy_biobert`, `ner_posology_large_biobert`, `ner_risk_factors_biobert`, `ner_anatomy_coarse_biobert`, `ner_deid_enriched_biobert`, `ner_human_phenotype_gene_biobert`, `ner_jsl_biobert`, `ner_events_biobert`, `ner_deid_biobert`, `ner_posology_biobert`, `ner_diseases_biobert`, `jsl_ner_wip_greedy_biobert`, `ner_ade_biobert`, `ner_anatomy_biobert`, `ner_cellular_biobert` .

## Predicted Entities

`ADE`, `ADMISSION`, `AGE`, `Admission_Discharge`, `Age`, `Alcohol`, `Allergen`, `Allergenic_substance`, `Amino_acid`, `Anatomical_system`, `Anatomy`, `BIOID`, `BMI`, `Birth_Entity`, `Blood_Pressure`, `BodyPart`, `CAD`, `CHEMICAL`, `CITY`, `CLINICAL_DEPT`, `CONTACT`, `COUNTRY`, `Cancer`, `Cancer_Modifier`, `Causative_Agents_(Virus_and_Bacteria)`, `Cell`, `Cellular_component`, `Cerebrovascular_Disease`, `Clinical_Dept`, `Communicable_Disease`, `DATE`, `DEVICE`, `DIABETES`, `DISCHARGE`, `DNA`, `DOCTOR`, `DOSAGE`, `DRUG`, `DURATION`, `Date`, `Death_Entity`, `Developing_anatomical_structure`, `Diabetes`, `Diagnosis`, `Diet`, `Direction`, `Disease`, `Disease_Syndrome_Disorder`, `Dosage`, `Drug`, `Drug_BrandName`, `Drug_Ingredient`, `Drug_Name`, `Duration`, `EKG_Findings`, `EMAIL`, `EVIDENTIAL`, `Employment`, `External_body_part_or_region`, `FAMILY_HIST`, `FAX`, `FORM`, `FREQUENCY`, `Family_History_Header`, `Female_Reproductive_Status`, `Fetus_NewBorn`, `Form`, `Frequency`, `GENE`, `GENE-N`, `GENE-Y`, `GO`, `Gender`, `Gene_or_gene_product`, `HDL`, `HEALTHPLAN`, `HOSPITAL`, `HP`, `HUMAN`, `HYPERLIPIDEMIA`, `HYPERTENSION`, `Heart_Disease`, `Height`, `Hyperlipidemia`, `Hypertension`, `ID`, `IDNUM`, `ImagingFindings`, `ImagingTest`, `Imaging_Technique`, `Immaterial_anatomical_entity`, `Injury_or_Poisoning`, `Internal_organ_or_component`, `Kidney_Disease`, `LDL`, `LOCATION`, `LOCATION-OTHER`, `Lab_Name`, `Lab_Result`, `Labour_Delivery`, `MEDICALRECORD`, `MEDICATION`, `ManualFix`, `Maybe`, `Measurements`, `Medical_Device`, `Medical_History_Header`, `Metastasis`, `Modifier`, `Multi-tissue_structure`, `NAME`, `Name`, `Negation`, `O2_Saturation`, `OBESE`, `OCCURRENCE`, `ORGANIZATION`, `Obesity`, `Oncological`, `Oncology_Therapy`, `Organ`, `Organism`, `Organism_subdivision`, `Organism_substance`, `OtherFindings`, `Overweight`, `Oxygen_Therapy`, `PATIENT`, `PHI`, `PHONE`, `PROBLEM`, `PROFESSION`, `Pathological_formation`, `Performance_Status`, `Pregnancy`, `Pregnancy_Delivery_Puerperium`, `Procedure`, `Procedure_Name`, `Psychological_Condition`, `Puerperium`, `Pulse`, `Pulse_Rate`, `RNA`, `ROUTE`, `Race_Ethnicity`, `Relationship_Status`, `RelativeDate`, `RelativeTime`, `Respiration`, `Respiratory_Rate`, `Route`, `SMOKER`, `SPECIES`, `STATE`, `STREET`, `STRENGTH`, `Score`, `Section_Header`, `Section_Name`, `Sexually_Active_or_Sexual_Orientation`, `Simple_chemical`, `Smoking`, `Social_History_Header`, `Staging`, `Strength`, `Substance`, `Substance_Name`, `Substance_Quantity`, `Symptom`, `Symptom_Name`, `TEST`, `TIME`, `TREATMENT`, `Temperature`, `Test`, `Test_Result`, `Time`, `Tissue`, `Total_Cholesterol`, `Treatment`, `Triglycerides`, `Tumor_Finding`, `URL`, `USERNAME`, `Units`, `VS_Finding`, `Vaccine`, `Vital_Signs_Header`, `Weight`, `ZIP`, `cell_line`, `cell_type`, `protein`


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.2.Pretrained_NER_Profiling_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_profiling_biobert_en_3.3.1_2.4_1642535810700.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_profiling_biobert_en_3.3.1_2.4_1642535810700.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_profiling_pipeline = PretrainedPipeline('ner_profiling_biobert', 'en', 'clinical/models')

result = ner_profiling_pipeline.annotate("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis three years prior to presentation , associated with an acute hepatitis , and obesity with a body mass index ( BMI ) of 33.5 kg/m2 , presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_profiling_pipeline = PretrainedPipeline('ner_profiling_biobert', 'en', 'clinical/models')

val result = ner_profiling_pipeline.annotate("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis three years prior to presentation , associated with an acute hepatitis , and obesity with a body mass index ( BMI ) of 33.5 kg/m2 , presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .")
```


{:.nlu-block}
```python
import nlu
nlu.load("en.med_ner.profiling_biobert").predict("""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis three years prior to presentation , associated with an acute hepatitis , and obesity with a body mass index ( BMI ) of 33.5 kg/m2 , presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .""")
```

</div>

## Results

```bash
******************** ner_diseases_biobert Model Results ******************** 

[('gestational diabetes mellitus', 'Disease'), ('type two diabetes mellitus', 'Disease'), ('T2DM', 'Disease'), ('HTG-induced pancreatitis', 'Disease'), ('hepatitis', 'Disease'), ('obesity', 'Disease'), ('polyuria', 'Disease'), ('polydipsia', 'Disease'), ('poor appetite', 'Disease'), ('vomiting', 'Disease')]


******************** ner_events_biobert Model Results ******************** 

[('gestational diabetes mellitus', 'PROBLEM'), ('eight years', 'DURATION'), ('presentation', 'OCCURRENCE'), ('type two diabetes mellitus ( T2DM', 'PROBLEM'), ('HTG-induced pancreatitis', 'PROBLEM'), ('three years', 'DURATION'), ('presentation', 'OCCURRENCE'), ('an acute hepatitis', 'PROBLEM'), ('obesity', 'PROBLEM'), ('a body mass index', 'TEST'), ('BMI', 'TEST'), ('presented', 'OCCURRENCE'), ('a one-week', 'DURATION'), ('polyuria', 'PROBLEM'), ('polydipsia', 'PROBLEM'), ('poor appetite', 'PROBLEM'), ('vomiting', 'PROBLEM')]


******************** ner_jsl_biobert Model Results ******************** 

[('28-year-old', 'Age'), ('female', 'Gender'), ('gestational diabetes mellitus', 'Diabetes'), ('eight years prior', 'RelativeDate'), ('type two diabetes mellitus', 'Diabetes'), ('T2DM', 'Disease_Syndrome_Disorder'), ('HTG-induced pancreatitis', 'Disease_Syndrome_Disorder'), ('three years prior', 'RelativeDate'), ('acute', 'Modifier'), ('hepatitis', 'Disease_Syndrome_Disorder'), ('obesity', 'Obesity'), ('body mass index', 'BMI'), ('BMI ) of 33.5 kg/m2', 'BMI'), ('one-week', 'Duration'), ('polyuria', 'Symptom'), ('polydipsia', 'Symptom'), ('poor appetite', 'Symptom'), ('vomiting', 'Symptom')]


******************** ner_clinical_biobert Model Results ******************** 

[('gestational diabetes mellitus', 'PROBLEM'), ('subsequent type two diabetes mellitus ( T2DM', 'PROBLEM'), ('HTG-induced pancreatitis', 'PROBLEM'), ('an acute hepatitis', 'PROBLEM'), ('obesity', 'PROBLEM'), ('a body mass index ( BMI )', 'TEST'), ('polyuria', 'PROBLEM'), ('polydipsia', 'PROBLEM'), ('poor appetite', 'PROBLEM'), ('vomiting', 'PROBLEM')]


******************** ner_risk_factors_biobert Model Results ******************** 

[('diabetes mellitus', 'DIABETES'), ('subsequent type two diabetes mellitus', 'DIABETES'), ('obesity', 'OBESE')]

...
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_profiling_biobert|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 3.3.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|750.1 MB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- BertEmbeddings
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- Finisher