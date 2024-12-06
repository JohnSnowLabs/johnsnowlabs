---
layout: model
title: Named Entity Recognition Profiling (Biobert)
author: John Snow Labs
name: ner_profiling_biobert
date: 2021-09-23
tags: [ner, ner_profiling, clinical, licensed, en]
task: Pipeline Healthcare
language: en
nav_key: models
edition: Healthcare NLP 3.2.3
spark_version: 2.4
supported: true
annotator: PipelineModel
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to explore all the available pretrained NER models at once. When you run this pipeline over your text, you will end up with the predictions coming out of each pretrained clinical NER model trained with `biobert_pubmed_base_cased`. 

Here are the NER models that this pretrained pipeline includes: `ner_jsl_enriched_biobert`, `ner_clinical_biobert`, `ner_chemprot_biobert`, `ner_jsl_greedy_biobert`, `ner_bionlp_biobert`, `ner_human_phenotype_go_biobert`, `jsl_rd_ner_wip_greedy_biobert`, `ner_posology_large_biobert`, `ner_risk_factors_biobert`, `ner_anatomy_coarse_biobert`, `ner_deid_enriched_biobert`, `ner_human_phenotype_gene_biobert`, `ner_jsl_biobert`, `ner_events_biobert`, `ner_deid_biobert`, `ner_posology_biobert`, `ner_diseases_biobert`, `jsl_ner_wip_greedy_biobert`, `ner_ade_biobert`, `ner_anatomy_biobert`, `ner_cellular_biobert`.

## Predicted Entities

`ADE`, `ADMISSION`, `AGE`, `Admission_Discharge`, `Age`, `Alcohol`, `Allergen`, `Allergenic_substance`, `Amino_acid`, `Anatomical_system`, `Anatomy`, `BIOID`, `BMI`, `Birth_Entity`, `Blood_Pressure`, `BodyPart`, `CAD`, `CHEMICAL`, `CITY`, `CLINICAL_DEPT`, `CONTACT`, `COUNTRY`, `Cancer`, `Cancer_Modifier`, `Causative_Agents_(Virus_and_Bacteria)`, `Cell`, `Cellular_component`, `Cerebrovascular_Disease`, `Clinical_Dept`, `Communicable_Disease`, `DATE`, `DEVICE`, `DIABETES`, `DISCHARGE`, `DNA`, `DOCTOR`, `DOSAGE`, `DRUG`, `DURATION`, `Date`, `Death_Entity`, `Developing_anatomical_structure`, `Diabetes`, `Diagnosis`, `Diet`, `Direction`, `Disease`, `Disease_Syndrome_Disorder`, `Dosage`, `Drug`, `Drug_BrandName`, `Drug_Ingredient`, `Drug_Name`, `Duration`, `EKG_Findings`, `EMAIL`, `EVIDENTIAL`, `Employment`, `External_body_part_or_region`, `FAMILY_HIST`, `FAX`, `FORM`, `FREQUENCY`, `Family_History_Header`, `Female_Reproductive_Status`, `Fetus_NewBorn`, `Form`, `Frequency`, `GENE`, `GENE-N`, `GENE-Y`, `GO`, `Gender`, `Gene_or_gene_product`, `HDL`, `HEALTHPLAN`, `HOSPITAL`, `HP`, `HUMAN`, `HYPERLIPIDEMIA`, `HYPERTENSION`, `Heart_Disease`, `Height`, `Hyperlipidemia`, `Hypertension`, `ID`, `IDNUM`, `ImagingFindings`, `ImagingTest`, `Imaging_Technique`, `Immaterial_anatomical_entity`, `Injury_or_Poisoning`, `Internal_organ_or_component`, `Kidney_Disease`, `LDL`, `LOCATION`, `LOCATION-OTHER`, `Lab_Name`, `Lab_Result`, `Labour_Delivery`, `MEDICALRECORD`, `MEDICATION`, `ManualFix`, `Maybe`, `Measurements`, `Medical_Device`, `Medical_History_Header`, `Metastasis`, `Modifier`, `Multi-tissue_structure`, `NAME`, `Name`, `Negation`, `O2_Saturation`, `OBESE`, `OCCURRENCE`, `ORGANIZATION`, `Obesity`, `Oncological`, `Oncology_Therapy`, `Organ`, `Organism`, `Organism_subdivision`, `Organism_substance`, `OtherFindings`, `Overweight`, `Oxygen_Therapy`, `PATIENT`, `PHI`, `PHONE`, `PROBLEM`, `PROFESSION`, `Pathological_formation`, `Performance_Status`, `Pregnancy`, `Pregnancy_Delivery_Puerperium`, `Procedure`, `Procedure_Name`, `Psychological_Condition`, `Puerperium`, `Pulse`, `Pulse_Rate`, `RNA`, `ROUTE`, `Race_Ethnicity`, `Relationship_Status`, `RelativeDate`, `RelativeTime`, `Respiration`, `Respiratory_Rate`, `Route`, `SMOKER`, `SPECIES`, `STATE`, `STREET`, `STRENGTH`, `Score`, `Section_Header`, `Section_Name`, `Sexually_Active_or_Sexual_Orientation`, `Simple_chemical`, `Smoking`, `Social_History_Header`, `Staging`, `Strength`, `Substance`, `Substance_Name`, `Substance_Quantity`, `Symptom`, `Symptom_Name`, `TEST`, `TIME`, `TREATMENT`, `Temperature`, `Test`, `Test_Result`, `Time`, `Tissue`, `Total_Cholesterol`, `Treatment`, `Triglycerides`, `Tumor_Finding`, `URL`, `USERNAME`, `Units`, `VS_Finding`, `Vaccine`, `Vital_Signs_Header`, `Weight`, `ZIP`, `cell_line`, `cell_type`, `protein`


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.2.Pretrained_NER_Profiling_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_profiling_biobert_en_3.2.3_2.4_1632427360617.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_profiling_biobert_en_3.2.3_2.4_1632427360617.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
ner_cellular_biobert_chunks :  []
ner_diseases_biobert_chunks :  ['gestational diabetes mellitus', 'type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'hepatitis', 'obesity', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_events_biobert_chunks :  ['gestational diabetes mellitus', 'eight years', 'presentation', 'type two diabetes mellitus ( T2DM', 'HTG-induced pancreatitis', 'three years', 'presentation', 'an acute hepatitis', 'obesity', 'a body mass index', 'BMI', 'presented', 'a one-week', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_bionlp_biobert_chunks :  []
ner_jsl_greedy_biobert_chunks :  ['28-year-old', 'female', 'gestational diabetes mellitus', 'eight years prior', 'type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'three years prior', 'acute hepatitis', 'obesity', 'body mass index', 'BMI ) of 33.5 kg/m2', 'one-week', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_jsl_biobert_chunks :  ['28-year-old', 'female', 'gestational diabetes mellitus', 'eight years prior', 'type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'three years prior', 'acute', 'hepatitis', 'obesity', 'body mass index', 'BMI ) of 33.5 kg/m2', 'one-week', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_anatomy_biobert_chunks :  ['body']
ner_jsl_enriched_biobert_chunks :  ['28-year-old', 'female', 'gestational diabetes mellitus', 'type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'acute', 'hepatitis', 'obesity', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_human_phenotype_go_biobert_chunks :  ['obesity', 'polyuria', 'polydipsia']
ner_deid_biobert_chunks :  ['eight years', 'three years']
ner_deid_enriched_biobert_chunks :  []
token :  ['A', '28-year-old', 'female', 'with', 'a', 'history', 'of', 'gestational', 'diabetes', 'mellitus', 'diagnosed', 'eight', 'years', 'prior', 'to', 'presentation', 'and', 'subsequent', 'type', 'two', 'diabetes', 'mellitus', '(', 'T2DM', '),', 'one', 'prior', 'episode', 'of', 'HTG-induced', 'pancreatitis', 'three', 'years', 'prior', 'to', 'presentation', ',', 'associated', 'with', 'an', 'acute', 'hepatitis', ',', 'and', 'obesity', 'with', 'a', 'body', 'mass', 'index', '(', 'BMI', ')', 'of', '33.5', 'kg/m2', ',', 'presented', 'with', 'a', 'one-week', 'history', 'of', 'polyuria', ',', 'polydipsia', ',', 'poor', 'appetite', ',', 'and', 'vomiting', '.']
ner_clinical_biobert_chunks :  ['gestational diabetes mellitus', 'subsequent type two diabetes mellitus ( T2DM', 'HTG-induced pancreatitis', 'an acute hepatitis', 'obesity', 'a body mass index ( BMI )', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_anatomy_coarse_biobert_chunks :  ['body']
ner_human_phenotype_gene_biobert_chunks :  ['obesity', 'mass', 'polyuria', 'polydipsia', 'vomiting']
ner_posology_large_biobert_chunks :  []
jsl_rd_ner_wip_greedy_biobert_chunks :  ['gestational diabetes mellitus', 'type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'acute hepatitis', 'obesity', 'body mass index', '33.5', 'kg/m2', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_posology_biobert_chunks :  []
jsl_ner_wip_greedy_biobert_chunks :  ['28-year-old', 'female', 'gestational diabetes mellitus', 'eight years prior', 'type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'three years prior', 'acute hepatitis', 'obesity', 'body mass index', 'BMI ) of 33.5 kg/m2', 'one-week', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_chemprot_biobert_chunks :  []
ner_ade_biobert_chunks :  ['pancreatitis', 'acute hepatitis', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_risk_factors_biobert_chunks :  ['diabetes mellitus', 'subsequent type two diabetes mellitus', 'obesity']
sentence :  ['A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis three years prior to presentation , associated with an acute hepatitis , and obesity with a body mass index ( BMI ) of 33.5 kg/m2 , presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .']
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_profiling_biobert|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 3.2.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- BertEmbeddings
- MedicalNerModel (x21)
- NerConverter (x21)
- Finisher
