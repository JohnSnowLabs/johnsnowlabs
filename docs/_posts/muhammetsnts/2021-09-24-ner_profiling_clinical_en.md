---
layout: model
title: Named Entity Recognition Profiling (Clinical)
author: John Snow Labs
name: ner_profiling_clinical
date: 2021-09-24
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

This pipeline can be used to explore all the available pretrained NER models at once. When you run this pipeline over your text, you will end up with the predictions coming out of each pretrained clinical NER model trained with `embeddings_clinical`.

Here are the NER models that this pretrained pipeline includes: `ner_ade_clinical_chunks`, `ner_posology_greedy_chunks`, `ner_risk_factors_chunks`, `jsl_ner_wip_clinical_chunks`, `ner_human_phenotype_gene_clinical_chunks`, `jsl_ner_wip_greedy_clinical_chunks`, `ner_cellular_chunks`, `ner_cancer_genetics_chunks`, `jsl_ner_wip_modifier_clinical_chunks`, `ner_drugs_greedy_chunks`, `ner_deid_sd_large_chunks`, `ner_diseases_chunks`, `nerdl_tumour_demo_chunks`, `ner_deid_subentity_augmented_chunks`, `ner_jsl_enriched_chunks`, `ner_genetic_variants_chunks`, `ner_bionlp_chunks`, `ner_measurements_clinical_chunks`, `ner_diseases_large_chunks`, `ner_radiology_chunks`, `ner_deid_augmented_chunks`, `ner_anatomy_chunks`, `ner_chemprot_clinical_chunks`, `ner_posology_experimental_chunks`, `ner_drugs_chunks`, `ner_deid_sd_chunks`, `ner_posology_large_chunks`, `ner_deid_large_chunks`, `ner_posology_chunks`, `ner_deidentify_dl_chunks`, `ner_deid_enriched_chunks`, `ner_bacterial_species_chunks`, `ner_drugs_large_chunks`, `ner_clinical_large_chunks`, `jsl_rd_ner_wip_greedy_clinical_chunks`, `ner_medmentions_coarse_chunks`, `ner_radiology_wip_clinical_chunks`, `ner_clinical_chunks`, `ner_chemicals_chunks`, `ner_deid_synthetic_chunks`, `ner_events_clinical_chunks`, `ner_posology_small_chunks`, `ner_anatomy_coarse_chunks`, `ner_human_phenotype_go_clinical_chunks`, `ner_jsl_slim_chunks`, `ner_jsl_chunks`, `ner_jsl_greedy_chunks`, `ner_events_admission_clinical_chunks` .

## Predicted Entities

`10_Dysarthria`, `11_ExtinctionInattention`, `1a_LOC`, `1b_LOCQuestions`, `1c_LOCCommands`, `2_BestGaze`, `3_Visual`, `4_FacialPalsy`, `5_Motor`, `5a_LeftArm`, `5b_RightArm`, `6_Motor`, `6a_LeftLeg`, `6b_RightLeg`, `7_LimbAtaxia`, `8_Sensory`, `9_BestLanguage`, `ABBR`, `ABBREVIATION`, `ADE`, `ADMISSION`, `AGE`, `ANAT`, `Abstractconcept`, `Access_To_Care`, `Adenopathy`, `Administration`, `AdmissionDischarge`, `Admission_Discharge`, `Age`, `Alcohol`, `Alcohol_Type`, `Alergen`, `Allergen`, `Allergies_header`, `AllocationRatio`, `Alzheimer`, `Amino_Acid,_Peptide,_or_Protein`, `Amino_acid`, `Aminoacid`, `Aminoacidpeptide`, `Anatomical_Site`, `Anatomical_Structure`, `Anatomical_system`, `Anatomicalpart`, `Anatomy`, `Antidepressants`, `Atom`, `Author`, `BENEFIT`, `BIOID`, `BMI`, `BioAndMedicalUnit`, `Biologic_Function`, `Biological_molecules`, `Biologicalprocess`, `Biomarker`, `Biomarker_Measurement`, `Biomarker_Result`, `Biomedical_or_Dental_Material`, `Birth_Entity`, `Blood_Pressure`, `BodyPart`, `Body_Location_or_Region`, `Body_Part`, `Body_Part,_Organ,_or_Organ_Component`, `Body_Substance`, `Body_System`, `Bodypart`, `CAD`, `CHEM`, `CHEMICAL`, `CITY`, `CLINICAL_DEPT`, `CONDITION`, `CONTACT`, `COUNTRY`, `CTAnalysisApproach`, `CTDesign`, `Cancer`, `CancerDx`, `CancerModifier`, `CancerSurgery`, `Cancer_Dx`, `Cancer_Modifier`, `Cancer_Score`, `Cancer_Surgery`, `Cancer_Therapy`, `Cardiovascular_Issues`, `Cell`, `Cell_Component`, `Cell_Type`, `Cellcomponent`, `Cells`, `Cellular_component`, `Cerebrovascular_Disease`, `Cerebrovascular_disease`, `Cessation_Treatment`, `Chemical`, `Chemotherapy`, `Chidhood_Event`, `Chief_complaint_header`, `Childhood_Event`, `Chromosome`, `Citation`, `ClinicalDept`, `Clinical_Attribute`, `Clinical_Dept`, `Clinical_history_header`, `Communicable_Disease`, `Community_Safety`, `Confidence`, `Country`, `Cycle_Count`, `Cycle_Day`, `Cycle_Number`, `Cyclecount`, `Cycleday`, `Cyclelength`, `Cyclenumber`, `DATE`, `DEVICE`, `DIABETES`, `DISCHARGE`, `DNA`, `DNAMutation`, `DOCTOR`, `DOSAGE`, `DRUG`, `DURATION`, `Daily_or_Recreational_Activity`, `Date`, `DateTime`, `Date_Time`, `Death_Entity`, `Demographics`, `Developing_anatomical_structure`, `Diabetes`, `Diagnosis_header`, `Diagnostic_Procedure`, `Diet`, `Direction`, `Disability`, `Disease`, `Disease_Syndrome_Disorder`, `Disease_or_Syndrome`, `DisorderOrSyndrome`, `Dosage`, `DoseValue`, `Dr`, `Drinking_Status`, `Drug`, `DrugChem`, `DrugTime`, `Drug_BrandName`, `Drug_Ingredient`, `Duration`, `EKG_Findings`, `EMAIL`, `EVIDENTIAL`, `Eating_Disorder`, `Education`, `Employment`, `Environmental_Condition`, `Environmentalfactor`, `Ethnicity`, `Eukaryote`, `Exercise`, `Experimentalfactor`, `External_body_part_or_region`, `FAMILY`, `FAMILY_HIST`, `FAX`, `FORM`, `FORMULA`, `FREQUENCY`, `Facility`, `Family_History_Header`, `Family_Member`, `Female_Reproductive_Status`, `Fetus_NewBorn`, `Financial_Status`, `Food`, `Food_Insecurity`, `Form`, `Fracture`, `Frequency`, `Fungus`, `G`, `GENE`, `GENE-N`, `GENE-Y`, `GENE_AND_CHEMICAL`, `GENE_PROTEIN`, `GO`, `GUT_Issues`, `G_P`, `Gen`, `Gender`, `Gene`, `Gene_or_Genome`, `Gene_or_gene_product`, `Geneorprotein`, `Geneorproteingroup`, `Genetic_Function`, `Geographic_Area`, `Geographic_Entity`, `Geographicallocation`, `Geographiclocation`, `Geographicnotproper`, `Gp`, `Grade`, `Grading`, `Group`, `Groupofpeople`, `Gynecological_Disease`, `Gynecological_Symptom`, `HDL`, `HEALTHPLAN`, `HOSPITAL`, `HP`, `HUMAN`, `HYPERLIPIDEMIA`, `HYPERTENSION`, `Header`, `HealthStatus`, `Health_Care_Activity`, `Healthcare_Institution`, `Heart_Disease`, `Heart_disease`, `Height`, `Histological_Type`, `History_pres_ilness_header`, `HormonalTherapy`, `Hormonal_Therapy`, `Hormone_Replacement_Therapy`, `Hormone_Testing`, `Housing`, `Hyperlipidemia`, `Hypertension`, `ID`, `IDENTIFIER`, `IDNUM`, `ImagingFindings`, `ImagingTest`, `Imaging_Technique`, `Imaging_Test`, `Imaging_header`, `Immaterial_anatomical_entity`, `Immunotherapy`, `Income`, `Indicator,_Reagent,_or_Diagnostic_Aid`, `Infectious_disease`, `InjuryOrPoisoning`, `Injury_or_Poisoning`, `Institution`, `Insurance_Status`, `Intellectualproduct`, `Internal_organ_or_component`, `Invasion`, `Ion`, `Irregular_Menstruation`, `Journal`, `Kidney_Disease`, `Kidney_disease`, `LDL`, `LOCATION`, `LOCATION-OTHER`, `Lab_results_header`, `Laboratory_Procedure`, `Laboratoryexperimentalfactor`, `Labour_Delivery`, `Language`, `Laterality`, `Legal_Issues`, `Lifestyle`, `Line_Of_Therapy`, `Localization`, `Lymph_Node`, `Lymph_Node_Modifier`, `MEDICALRECORD`, `MEDICATION`, `MULTIPLE`, `Machineactivity`, `Mammal`, `ManualFix`, `Manufactured_Object`, `Marital_Status`, `Meas`, `Measurement`, `Measurements`, `MedicalCondition`, `MedicalDevice`, `Medical_Device`, `Medical_History_Header`, `Medical_history_header`, `Medicaldevice`, `Medicalfinding`, `Medicalprocedure`, `Medicalprocedureordevice`, `Medications_header`, `Medicine`, `Menopause`, `Mental_Health`, `Mental_Process`, `Mental_disorder`, `Mental_or_Behavioral_Dysfunction`, `Mentalprocess`, `Metastasis`, `Modifier`, `Molecular_Biology_Research_Technique`, `Molecular_Function`, `Molecularprocess`, `Molecule`, `Multi-tissue_structure`, `N`, `NAME`, `NIHSS`, `NN`, `N_Patients`, `Namedentity`, `Neoplastic_Process`, `Nonproteinornucleicacidchemical`, `Nucleic_Acid,_Nucleoside,_or_Nucleotide`, `Nucleicacid`, `Nucleicacidsubstance`, `Nucleotide_Sequence`, `NumberPatients`, `O2_Saturation`, `OBESE`, `OBS`, `OCCURRENCE`, `ORGANIZATION`, `Obesity`, `Oncogene`, `Oncogenes`, `Oncological`, `Oncological_disease`, `Oncology_Therapy`, `Organ`, `Organic_Chemical`, `Organism`, `Organism_Attribute`, `Organism_subdivision`, `Organism_substance`, `Organismpart`, `Organization`, `Osteoporosis`, `Osteporosis_Therapy`, `OtherFindings`, `Other_Disease`, `Other_Health_Issues`, `Other_SDoH_Keywords`, `Other_Symptom`, `Overweight`, `Oxygen_Therapy`, `P`, `PATIENT`, `PHI`, `PHONE`, `PMID`, `PROBLEM`, `PROFESSION`, `PValue`, `Partofprotein`, `Pathogen`, `Pathologic_Function`, `Pathological_formation`, `Pathology_Result`, `Pathology_Test`, `Patient_info_header`, `PercentagePatients`, `PerformanceStatus`, `Performance_Status`, `Perimenopause`, `Person`, `Persongroup`, `Pharmacologic_Substance`, `Physical_Measurement`, `Physicalphenomenon`, `Physiological_reaction`, `Plant`, `Population_Group`, `Posology_Information`, `Predictive_Biomarkers`, `Pregnancy`, `Pregnancy_Delivery_Puerperium`, `Pregnancy_Newborn`, `Problem`, `Procedure`, `Process`, `Professional_or_Occupational_Group`, `Prognostic_Biomarkers`, `Prokaryote`, `Propernamedgeographicallocation`, `Protein`, `ProteinMutation`, `PsychologicalCondition`, `Psychological_Condition`, `Psychoneurologic_Issue`, `PublicationYear`, `Publicationorcitation`, `Publishedsourceofinformation`, `Puerperium`, `Pulse`, `Qualitative_Concept`, `Quality_Of_Life`, `Quantitative_Concept`, `Quantity`, `Quantityormeasure`, `Quantityormeasurement`, `R`, `RNA`, `ROUTE`, `RaceEthnicity`, `Race_Ethnicity`, `Radiation_Dose`, `Radiological_Test`, `Radiological_Test_Result`, `Radiotherapy`, `Relationship`, `RelationshipStatus`, `Relationship_Status`, `Relationshipphrase`, `RelativeDate`, `RelativeTime`, `Relative_Date`, `Research_Activity`, `Researchactivity`, `Researchactivty`, `Respiration`, `Respiratory_Issues`, `Respiratory_disease`, `ResponseToTreatment`, `Response_To_Treatment`, `Route`, `SMOKER`, `SNP`, `SPECIES`, `STATE`, `STREET`, `STRENGTH`, `SYSTEMATIC`, `Score`, `Section_Header`, `Severity`, `Sexual_Activity`, `Sexual_Orientation`, `Sexually_Active_or_Sexual_Orientation`, `Sign_or_Symptom`, `Simple_chemical`, `Site_Bone`, `Site_Brain`, `Site_Breast`, `Site_Liver`, `Site_Lung`, `Site_Lymph_Node`, `Site_Other_Body_Part`, `Size`, `Size_Trend`, `Smallmolecule`, `Smoking`, `Smoking_Status`, `Smoking_Type`, `Social_Exclusion`, `Social_History_Header`, `Social_Support`, `Spatial_Concept`, `Spiritual_Beliefs`, `Stage`, `Staging`, `Statistical_Indicator`, `Strength`, `Substance`, `SubstanceQuantity`, `Substance_Duration`, `Substance_Frequency`, `Substance_Quantity`, `Substance_Use`, `Symptom`, `TEST`, `TIME`, `TREATMENT`, `TRIVIAL`, `TargetedTherapy`, `Targeted_Therapy`, `Temperature`, `Test`, `TestResult`, `Test_Result`, `Therapeutic_or_Preventive_Procedure`, `Thing`, `Time`, `TimePoint`, `Timepoint`, `Tissue`, `Total_Cholesterol`, `Transportation`, `Treatment`, `Treatment_plan_header`, `Trial_Design`, `Trial_Phase`, `Triglycerides`, `Tumor`, `Tumor_Description`, `Tumor_Finding`, `Tumor_Size`, `URL`, `USERNAME`, `Unconjugated`, `Unit`, `Units`, `Unpropernamedgeographicallocation`, `UnspecificTherapy`, `Unspecific_Therapy`, `VS_Finding`, `Vaccine`, `Vaccine_Name`, `Vaginal_Swab`, `Value`, `Violence_Or_Abuse`, `Viral_components`, `Virus`, `VitalTest`, `Vital_Sign`, `Vital_Signs_Header`, `Warfarin`, `Weight`, `Withdrawal_Treatment`, `X`, `ZIP`, `alcohol_use`, `antidote`, `behavior_alcohol`, `behavior_drug`, `behavior_tobacco`, `bodypart`, `cell_line`, `cell_type`, `clinical_condition`, `clinical_event`, `communicable_disease`, `date_time`, `drug_duration`, `drug_form`, `drug_frequency`, `drug_quantity`, `drug_route`, `drug_strength`, `employment`, `general_symptoms`, `legal_issue`, `marital_status`, `opioid_drug`, `other_disease`, `other_drug`, `patient`, `protein`, `psychiatric_issue`, `sdoh_community`, `sdoh_economics`, `sdoh_education`, `sdoh_environment`, `sexual_orientation`, `snomed_term`, `substance_use_disorder`, `test`, `test_result`, `units_measurements`, `violence`


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.2.Pretrained_NER_Profiling_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_profiling_clinical_en_3.2.3_2.4_1632491778580.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_profiling_clinical_en_3.2.3_2.4_1632491778580.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_profiling_pipeline = PretrainedPipeline('ner_profiling_clinical', 'en', 'clinical/models')

result = ner_profiling_pipeline.annotate("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis three years prior to presentation , associated with an acute hepatitis , and obesity with a body mass index ( BMI ) of 33.5 kg/m2 , presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_profiling_pipeline = PretrainedPipeline('ner_profiling_clinical', 'en', 'clinical/models')

val result = ner_profiling_pipeline.annotate("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis three years prior to presentation , associated with an acute hepatitis , and obesity with a body mass index ( BMI ) of 33.5 kg/m2 , presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .")
```


{:.nlu-block}
```python
import nlu
nlu.load("en.med_ner.profiling_clinical").predict("""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis three years prior to presentation , associated with an acute hepatitis , and obesity with a body mass index ( BMI ) of 33.5 kg/m2 , presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .""")
```

</div>

## Results

```bash
ner_ade_clinical_chunks :  ['polydipsia', 'poor appetite', 'vomiting']
ner_posology_greedy_chunks :  []
ner_risk_factors_chunks :  ['diabetes mellitus', 'type two diabetes mellitus', 'obesity']
jsl_ner_wip_clinical_chunks :  ['28-year-old', 'female', 'gestational diabetes mellitus', 'eight years prior', 'subsequent', 'type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'three years prior', 'acute', 'hepatitis', 'obesity', 'body mass index', '33.5 kg/m2', 'one-week', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_human_phenotype_gene_clinical_chunks :  ['type', 'obesity', 'mass', 'polyuria', 'polydipsia']
jsl_ner_wip_greedy_clinical_chunks :  ['28-year-old', 'female', 'gestational diabetes mellitus', 'eight years prior', 'type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'three years prior', 'acute hepatitis', 'obesity', 'body mass', 'BMI ) of 33.5 kg/m2', 'one-week', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_cellular_chunks :  []
ner_cancer_genetics_chunks :  []
jsl_ner_wip_modifier_clinical_chunks :  ['28-year-old', 'female', 'gestational diabetes mellitus', 'eight years prior', 'type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'three years prior', 'acute hepatitis', 'obesity', 'body mass', 'BMI ) of 33.5 kg/m2', 'one-week', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_drugs_greedy_chunks :  []
ner_deid_sd_large_chunks :  []
ner_diseases_chunks :  ['gestational diabetes mellitus', 'diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'hepatitis', 'obesity', 'BMI', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
nerdl_tumour_demo_chunks :  []
ner_deid_subentity_augmented_chunks :  ['28-year-old']
ner_jsl_enriched_chunks :  ['28-year-old', 'female', 'gestational diabetes mellitus', 'diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'acute', 'hepatitis', 'obesity', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_genetic_variants_chunks :  []
ner_bionlp_chunks :  ['female', 'hepatitis']
ner_measurements_clinical_chunks :  ['33.5', 'kg/m2']
ner_diseases_large_chunks :  ['gestational diabetes mellitus', 'diabetes mellitus', 'T2DM', 'pancreatitis', 'hepatitis', 'obesity', 'polyuria', 'polydipsia', 'vomiting']
ner_radiology_chunks :  ['gestational diabetes mellitus', 'type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'acute hepatitis', 'obesity', 'body', 'mass index', 'BMI', '33.5', 'kg/m2', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_deid_augmented_chunks :  []
ner_anatomy_chunks :  ['body']
ner_chemprot_clinical_chunks :  []
ner_posology_experimental_chunks :  []
ner_drugs_chunks :  []
ner_deid_sd_chunks :  []
ner_posology_large_chunks :  []
ner_deid_large_chunks :  []
ner_posology_chunks :  []
ner_deidentify_dl_chunks :  []
ner_deid_enriched_chunks :  []
ner_bacterial_species_chunks :  []
ner_drugs_large_chunks :  []
ner_clinical_large_chunks :  ['gestational diabetes mellitus', 'subsequent type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'an acute hepatitis', 'obesity', 'a body mass index', 'BMI', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
token :  ['A', '28-year-old', 'female', 'with', 'a', 'history', 'of', 'gestational', 'diabetes', 'mellitus', 'diagnosed', 'eight', 'years', 'prior', 'to', 'presentation', 'and', 'subsequent', 'type', 'two', 'diabetes', 'mellitus', '(', 'T2DM', '),', 'one', 'prior', 'episode', 'of', 'HTG-induced', 'pancreatitis', 'three', 'years', 'prior', 'to', 'presentation', ',', 'associated', 'with', 'an', 'acute', 'hepatitis', ',', 'and', 'obesity', 'with', 'a', 'body', 'mass', 'index', '(', 'BMI', ')', 'of', '33.5', 'kg/m2', ',', 'presented', 'with', 'a', 'one-week', 'history', 'of', 'polyuria', ',', 'polydipsia', ',', 'poor', 'appetite', ',', 'and', 'vomiting', '.']
jsl_rd_ner_wip_greedy_clinical_chunks :  ['28-year-old', 'female', 'gestational diabetes mellitus', 'eight years prior', 'subsequent type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'three years prior', 'acute hepatitis', 'obesity', 'body mass index ( BMI', '33.5 kg/m2', 'one-week', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_medmentions_coarse_chunks :  ['female', 'diabetes mellitus', 'diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'associated with', 'acute hepatitis', 'obesity', 'body mass index', 'BMI', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_radiology_wip_clinical_chunks :  ['gestational diabetes mellitus', 'type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'acute hepatitis', 'obesity', 'body', 'mass index', '33.5', 'kg/m2', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_clinical_chunks :  ['gestational diabetes mellitus', 'subsequent type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'an acute hepatitis', 'obesity', 'a body mass index', 'BMI', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_chemicals_chunks :  []
ner_deid_synthetic_chunks :  []
ner_events_clinical_chunks :  ['gestational diabetes mellitus', 'eight years', 'presentation', 'subsequent type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'three years', 'presentation', 'an acute hepatitis', 'obesity', 'a body mass index ( BMI', 'presented', 'a one-week', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_posology_small_chunks :  []
ner_anatomy_coarse_chunks :  ['body']
ner_human_phenotype_go_clinical_chunks :  ['obesity', 'polydipsia', 'vomiting']
ner_jsl_slim_chunks :  ['28-year-old', 'female', 'gestational diabetes mellitus', 'eight years prior', 'type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'three years prior', 'acute hepatitis', 'obesity', 'body mass index', 'BMI ) of 33.5 kg/m2', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_jsl_chunks :  ['28-year-old', 'female', 'gestational diabetes mellitus', 'eight years prior', 'subsequent', 'type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'three years prior', 'acute', 'hepatitis', 'obesity', 'body mass index', '33.5 kg/m2', 'one-week', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
ner_jsl_greedy_chunks :  ['28-year-old', 'female', 'gestational diabetes mellitus', 'eight years prior', 'type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'three years prior', 'acute hepatitis', 'obesity', 'body mass', 'BMI ) of 33.5 kg/m2', 'one-week', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
sentence :  ['A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis three years prior to presentation , associated with an acute hepatitis , and obesity with a body mass index ( BMI ) of 33.5 kg/m2 , presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .']
ner_events_admission_clinical_chunks :  ['gestational diabetes mellitus', 'eight years', 'presentation', 'subsequent type two diabetes mellitus', 'T2DM', 'HTG-induced pancreatitis', 'three years', 'presentation', 'an acute hepatitis', 'obesity', 'a body mass index', 'BMI', 'kg/m2', 'presented', 'a one-week', 'polyuria', 'polydipsia', 'poor appetite', 'vomiting']
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_profiling_clinical|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 3.2.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel (x48)
- NerConverter (x48)
- Finisher
