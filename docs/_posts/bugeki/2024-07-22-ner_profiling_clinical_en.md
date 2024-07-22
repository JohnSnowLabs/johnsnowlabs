---
layout: model
title: Named Entity Recognition Profiling (Clinical)
author: John Snow Labs
name: ner_profiling_clinical
date: 2024-07-22
tags: [licensed, en, clinical, profiling, ner_profiling, ner]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to explore all the available pretrained NER models at once. When you run this pipeline over your text, you will end up with the predictions of each pretrained clinical NER model trained with `embeddings_clinical`.

It has been updated by adding new clinical NER models and NER model outputs to the previous version. In this version, there are 151 clinical NER models.

Here are the NER models that this pretrained pipeline includes:

`jsl_ner_wip_clinical`, `jsl_ner_wip_greedy_clinical`, `jsl_ner_wip_modifier_clinical`, `jsl_rd_ner_wip_greedy_clinical`, `ner_abbreviation_clinical`, `ner_ade_binary`, `ner_ade_clinical`,
`ner_ade_clinical_langtest`, `ner_alcohol_smoking`, `ner_anatomy`, `ner_anatomy_coarse`,  `ner_bacterial_species`, `ner_bacterial_species_langtest`, `ner_biomarker`, `ner_biomarker_langtest`, `ner_biomedical_bc2gm`, `ner_bionlp`, `ner_bionlp_langtest`, `ner_cancer_genetics`, `ner_cellular`, `ner_cellular_langtest`, `ner_chemd_clinical`, `ner_chemicals`, `ner_chemprot_clinical`, `ner_chemprot_clinical_langtest`, `ner_chexpert`, `ner_clinical`, `ner_clinical_abbreviation_langtest`, `ner_clinical_langtest`, `ner_clinical_large`, `ner_clinical_large_langtest`, `ner_clinical_trials_abstracts`, `ner_covid_trials`, `ner_deid_augmented`, `ner_deid_enriched`, `ner_deid_enriched_langtest`, `ner_deid_generic_augmented`, `ner_deid_generic_augmented_allUpperCased_langtest`, `ner_deid_generic_augmented_langtest`, `ner_deid_large`, `ner_deid_large_langtest`, `ner_deid_sd`, `ner_deid_sd_large`, `ner_deid_subentity_augmented`, `ner_deid_subentity_augmented_i2b2`, `ner_deid_subentity_augmented_langtest`, `ner_deid_synthetic`, `ner_deidentify_dl`, `ner_diseases`, `ner_diseases_langtest`, `ner_diseases_large`, `ner_drugprot_clinical`, `ner_drugs`, `ner_drugs_greedy`, `ner_drugs_large`, `ner_eu_clinical_case`, `ner_eu_clinical_condition`, `ner_eu_clinical_condition_langtest`, `ner_events_admission_clinical`, `ner_events_clinical`, `ner_events_clinical_langtest`, `ner_genetic_variants`, `ner_human_phenotype_gene_clinical`, `ner_human_phenotype_gene_clinical_langtest`, `ner_human_phenotype_go_clinical`, `ner_human_phenotype_go_clinical_langtest`, `ner_jsl`, `ner_jsl_enriched`, `ner_jsl_greedy`, `ner_jsl_langtest`, `ner_jsl_limited_80p_for_benchmarks`, `ner_jsl_slim`, `ner_living_species`, `ner_living_species_langtest`, `ner_measurements_clinical`, `ner_medmentions_coarse`, `ner_menopause_core`, `ner_nature_nero_clinical`, `ner_nihss`, `ner_oncology`, `ner_oncology_anatomy_general`, `ner_oncology_anatomy_general_langtest`, `ner_oncology_anatomy_granular`, `ner_oncology_anatomy_granular_langtest`, `ner_oncology_biomarker`, `ner_oncology_biomarker_langtest`, `ner_oncology_demographics`, `ner_oncology_demographics_langtest`, `ner_oncology_diagnosis`, `ner_oncology_diagnosis_langtest`, `ner_oncology_langtest`, `ner_oncology_limited_80p_for_benchmarks`, `ner_oncology_posology`, `ner_oncology_posology_langtest`, `ner_oncology_response_to_treatment`, `ner_oncology_response_to_treatment_langtest`, `ner_oncology_test`, `ner_oncology_test_langtest`, `ner_oncology_therapy`, `ner_oncology_therapy_langtest`, `ner_oncology_tnm`, `ner_oncology_tnm_langtest`, `ner_oncology_unspecific_posology`, `ner_oncology_unspecific_posology_langtest`, `ner_opioid`, `ner_pathogen`, `ner_posology`, `ner_posology_small`, `ner_posology_experimental`, `ner_posology_greedy`, `ner_posology_large`,  `ner_posology_langtest`, `ner_radiology`, `ner_radiology_wip_clinical`, `ner_risk_factors`, `ner_risk_factors_langtest`, `ner_sdoh`, `ner_sdoh_access_to_healthcare`, `ner_sdoh_community_condition`, `ner_sdoh_core`, `ner_sdoh_demographics`, `ner_sdoh_health_behaviours_problems`, `ner_sdoh_income_social_status`, `ner_sdoh_langtest`, `ner_sdoh_mentions`,
`ner_sdoh_mentions_test`, `ner_sdoh_social_environment`, `ner_sdoh_substance_usage`, `ner_section_header_diagnosis`, `ner_snomed_term`, `ner_supplement_clinical`,
`ner_vop`, `ner_vop_anatomy`, `ner_vop_anatomy_langtest`, `ner_vop_clinical_dept`, `ner_vop_clinical_dept_langtest`, `ner_vop_demographic`, `ner_vop_demographic_langtest`,
`ner_vop_langtest`, `ner_vop_problem`, `ner_vop_problem_langtest`, `ner_vop_problem_reduced`, `ner_vop_problem_reduced_langtest`,`ner_vop_temporal`, `ner_vop_temporal_langtest`,
`ner_vop_test`, `ner_vop_test_langtest`, `ner_vop_treatment`, `ner_vop_treatment_langtest`, `ner_vop_v2`, `nerdl_tumour_demo`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_profiling_clinical_en_5.4.0_3.0_1721644427291.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_profiling_clinical_en_5.4.0_3.0_1721644427291.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use


<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_profiling_clinical", "en", "clinical/models")

result = ner_pipeline.annotate("""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM ),
one prior episode of HTG-induced pancreatitis three years prior to presentation , associated with an acute hepatitis , and obesity with a body mass index ( BMI ) of 33.5 kg/m2 ,
presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_profiling_clinical", "en", "clinical/models")

val result = ner_pipeline.annotate("""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM ),
one prior episode of HTG-induced pancreatitis three years prior to presentation , associated with an acute hepatitis , and obesity with a body mass index ( BMI ) of 33.5 kg/m2 ,
presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .""")

```
</div>

## Results

```bash

******************** ner_jsl Model Results ********************

[('28-year-old', 'Age'), ('female', 'Gender'), ('gestational diabetes mellitus', 'Diabetes'), ('eight years prior', 'RelativeDate'), ('type two diabetes mellitus', 'Diabetes'), ('T2DM', 'Diabetes'), ('HTG-induced pancreatitis', 'Disease_Syndrome_Disorder'), ('three years prior', 'RelativeDate'), ('acute', 'Modifier'), ('hepatitis', 'Disease_Syndrome_Disorder'), ('obesity', 'Obesity'), ('body mass index', 'BMI'), ('BMI', 'BMI'), ('33.5 kg/m2', 'BMI'), ('one-week', 'Duration'), ('polyuria', 'Symptom'), ('polydipsia', 'Symptom'), ('poor appetite', 'Symptom'), ('vomiting', 'Symptom')]


******************** ner_diseases_large Model Results ********************

[('gestational diabetes mellitus', 'Disease'), ('diabetes mellitus', 'Disease'), ('T2DM', 'Disease'), ('pancreatitis', 'Disease'), ('hepatitis', 'Disease'), ('obesity', 'Disease'), ('polyuria', 'Disease'), ('polydipsia', 'Disease'), ('vomiting', 'Disease')]


******************** ner_radiology Model Results ********************

[('gestational diabetes mellitus', 'Disease_Syndrome_Disorder'), ('type two diabetes mellitus', 'Disease_Syndrome_Disorder'), ('T2DM', 'Disease_Syndrome_Disorder'), ('HTG-induced pancreatitis', 'Disease_Syndrome_Disorder'), ('acute hepatitis', 'Disease_Syndrome_Disorder'), ('obesity', 'Disease_Syndrome_Disorder'), ('body', 'BodyPart'), ('mass index', 'Symptom'), ('BMI', 'Test'), ('33.5', 'Measurements'), ('kg/m2', 'Units'), ('polyuria', 'Symptom'), ('polydipsia', 'Symptom'), ('poor appetite', 'Symptom'), ('vomiting', 'Symptom')]


******************** ner_clinical Model Results ********************

[('gestational diabetes mellitus', 'PROBLEM'), ('subsequent type two diabetes mellitus', 'PROBLEM'), ('T2DM', 'PROBLEM'), ('HTG-induced pancreatitis', 'PROBLEM'), ('an acute hepatitis', 'PROBLEM'), ('obesity', 'PROBLEM'), ('a body mass index', 'PROBLEM'), ('BMI', 'TEST'), ('polyuria', 'PROBLEM'), ('polydipsia', 'PROBLEM'), ('poor appetite', 'PROBLEM'), ('vomiting', 'PROBLEM')]
Model: ner_clinical


******************** ner_medmentions_coarse Model Results ********************

[('female', 'Organism_Attribute'), ('diabetes mellitus', 'Disease_or_Syndrome'), ('diabetes mellitus', 'Disease_or_Syndrome'), ('T2DM', 'Disease_or_Syndrome'), ('HTG-induced pancreatitis', 'Disease_or_Syndrome'), ('associated with', 'Qualitative_Concept'), ('acute hepatitis', 'Disease_or_Syndrome'), ('obesity', 'Disease_or_Syndrome'), ('body mass index', 'Clinical_Attribute'), ('BMI', 'Clinical_Attribute'), ('polyuria', 'Sign_or_Symptom'), ('polydipsia', 'Sign_or_Symptom'), ('poor appetite', 'Sign_or_Symptom'), ('vomiting', 'Sign_or_Symptom')]

...

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_profiling_clinical|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
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
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- Finisher
