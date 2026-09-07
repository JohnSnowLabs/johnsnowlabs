---
layout: model
title: Pipeline for Logical Observation Identifiers Names and Codes (LOINC-Numeric) (sbiobert_base_cased_mli_onnx embeddings)
author: John Snow Labs
name: sbiobertresolve_loinc_numeric_augmented_pipeline_2_83
date: 2026-09-07
tags: [en, entity_resolution, licensed, clinical, loinc, pipeline, sbiobert]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline extracts `TEST` entities and maps them to their corresponding Logical Observation Identifiers Names and Codes (LOINC) codes using `sbiobert_base_cased_mli` sentence embeddings. It is trained on the augmented version of the LOINC 2.83 dataset (LOINC 2.83 official data plus an in-house curated dataset), scoped to numeric LOINC codes, without the inclusion of LOINC's non-numeric Part, Answer, Panel, Survey, and other auxiliary/document codes.

If you also need LOINC's non-numeric auxiliary codes, use `sbiobertresolve_loinc_augmented_pipeline_2_83` instead.

It also provides the official resolution of the codes within the brackets.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_loinc_numeric_augmented_pipeline_2_83_en_6.4.1_3.4_1788739819841.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_loinc_numeric_augmented_pipeline_2_83_en_6.4.1_3.4_1788739819841.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

loinc_pipeline = PretrainedPipeline("sbiobertresolve_loinc_numeric_augmented_pipeline_2_83", "en", "clinical/models")

data = spark.createDataFrame([["The patient's glucose and hemoglobin A1c levels were checked, along with a basic metabolic panel including sodium and potassium, and a complete blood count."]]).toDF("text")
result = loinc_pipeline.transform(data)

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

loinc_pipeline = nlp.PretrainedPipeline("sbiobertresolve_loinc_numeric_augmented_pipeline_2_83", "en", "clinical/models")

data = spark.createDataFrame([["The patient's glucose and hemoglobin A1c levels were checked, along with a basic metabolic panel including sodium and potassium, and a complete blood count."]]).toDF("text")
result = loinc_pipeline.transform(data)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val loinc_pipeline = PretrainedPipeline("sbiobertresolve_loinc_numeric_augmented_pipeline_2_83", "en", "clinical/models")

val data = Seq("The patient's glucose and hemoglobin A1c levels were checked, along with a basic metabolic panel including sodium and potassium, and a complete blood count.").toDF("text")
val result = loinc_pipeline.transform(data)

```
</div>

## Results

```bash
| chunk                 | label   | loinc_code   | resolution                                                      | all_codes                                                                                                                                                                                              | all_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:----------------------|:--------|:-------------|:----------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| glucose               | Test    | 2345-7       | glucose [Glucose [Mass/volume] in Serum or Plasma]              | 2345-7:::74790-7:::51419-0:::81637-1:::47621-8:::32318-8:::104638-2:::50016-5:::72648-9:::27353-2:::6248-9:::41653-7:::4269-7:::95720-9:::41896-2:::26682-5:::50667-5:::97506-0:::80093-8:::20643-3    | glucose [Glucose [Mass/volume] in Serum or Plasma]:::Glucose HBT [Glucose challenge (hydrogen breath test) panel - Exhaled gas]:::Glucose cor [Sodium [Moles/volume] corrected for glucose in Serum or Plasma]:::Glucose correlation [Glucose meter to reference method correlation [Ratio] in Serum, Plasma or Blood by calculation]:::glucose.iv [Glucose.IV [Mass] of Dose]:::Glucose, Specimen [Glucose [Moles/volume] in Specimen]:::Glucose SD [Glucose standard deviation/Glucose mean in Reporting Period Interstitial fluid by calculation]:::sugar [Sugar [Type] of Dose]:::glucose gradient [Glucose in serum - glucose in synovial fluid [Molar concentration difference]]:::Glucose mean value [Glucose mean value [Mass/volume] in Blood Estimated from glycated hemoglobin]:::Gly [Soybean IgE Ab [Units/volume] in Serum]:::Glucomtr [Glucose [Mass/volume] in Capillary blood by Glucometer]:::glucose.po [Glucose.PO [Mass] of Dose]:::GlyR [Glycine receptor Ab [Titer] in Serum or Plasma by Immunoassay]:::Glucose Mtr Dev [Type of Glucose meter device]:::glycolate [Glycolate [Presence] in Urine]:::glucose tolerance [Glucose tolerance [Interpretation] in Serum or Plasma Narrative]:::Glucose management indicator [Glucose management indicator]:::glucosamine [Glucosamine [Moles/volume] in Serum or Plasma]:::Gln [Glutamine [Moles/volume] in Serum or Plasma]                                                                                                               |
| hemoglobin A1c levels | Test    | 41995-2      | hemoglobin a1c [Hemoglobin A1c [Mass/volume] in Blood]          | 41995-2:::43150-2:::4548-4:::10486-9:::21687-9:::112870-1:::51196-4:::4593-0:::10346-5:::50319-3:::17871-5:::50385-4:::6864-3:::72914-5:::14563-1:::96595-4:::2030-5:::2865-4                          | hemoglobin a1c [Hemoglobin A1c [Mass/volume] in Blood]:::Hemoglobin A1c measurement device panel [Hemoglobin A1c measurement device panel]:::hemoglobin a1c/hemoglobin.total [Hemoglobin A1c/Hemoglobin.total in Blood]:::hemoglobin ag [Hemoglobin Ag [Presence] in Tissue by Immune stain]:::Hemoglobin, alpha 1 [HBA1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal]:::hemoglobin a1c & estimated average glucose panel [Hemoglobin A1c and estimated average glucose panel - Blood]:::hemoglobin a1/hemoglobin.total [Hemoglobin A1/Hemoglobin.total in Blood by Electrophoresis]:::Hemoglobin I, Blood [Hemoglobin I [Presence] in Blood by Electrophoresis acid (pH 6.3)]:::hemoglobin a [Hemoglobin A [Units/volume] in Blood by Electrophoresis]:::hbme-1 ag [HBME-1 Ag [Presence] in Tissue by Immune stain]:::hemoglobin h [Hemoglobin H [Presence] in Blood by Heat denaturation]:::A1 Microglob [Alpha-1-Microglobulin.placental [Presence] in Vaginal fluid]:::hemoglobin s [Hemoglobin S [Presence] in Blood by Solubility test]:::hna 1c ab [HNA 1c Ab [Presence] in Serum by Immunoassay]:::hemoglobin^1st specimen [Hemoglobin [Presence] in Stool from gastrointestinal --1st specimen]:::Hemoglobin A1c/Hemoglobin.total in DBS [Hemoglobin A1c/Hemoglobin.total in DBS]:::CO Hemoglobin [Carboxyhemoglobin/Hemoglobin.total in Arterial blood]:::alpha 1 globulin [Alpha 1 globulin [Mass/volume] in Serum or Plasma by Electrophoresis] |
| basic metabolic panel | Test    | 51990-0      | basic metabolic panel [Basic metabolic panel - Blood]           | 51990-0:::101655-9:::89044-2:::9350-0:::50042-1:::79531-0:::43147-8:::24321-2:::79529-4:::104076-5:::79530-2:::112034-4:::81578-7:::1547-9:::107464-0:::41966-3                                        | basic metabolic panel [Basic metabolic panel - Blood]:::basic metabolic & hematocrit panel [Basic metabolic and hematocrit panel - Blood]:::basic metabolic & albumin panel [Basic metabolic and albumin panel - Serum or Plasma]:::Metabolic screen [Sulfhydryls [Presence] in Urine]:::Basal metabolic rate index [Basal metabolic rate index]:::basic mobility items [Basic mobility items number [Activity Measure for Post-Acute Care]]:::Metabolism measurement device panel [Metabolism measurement device panel]:::basic metabolic 2000 panel [Basic metabolic 2000 panel - Serum or Plasma]:::basic mobility score [Basic mobility score [AM-PAC]]:::basic metabolic & hemoglobin & hematocrit panel [Basic metabolic with hemoglobin and hematocrit panel - Blood]:::Basic mobility score SE [Basic mobility score standard error [AM-PAC]]:::Basic information [Basic information]:::PT Brain metabolic [PT Brain metabolic]:::glucose^baseline [Glucose [Mass/volume] in Serum or Plasma --baseline]:::metabolic disease screening [Metabolic disease screening Newborn]:::Name of Metabolism measurement device [Name of Metabolism measurement device]                                                                                                                                                                                                                                                                                                                                           |
| sodium                | Test    | 2951-2       | sodium [Sodium [Moles/volume] in Serum or Plasma]               | 2951-2:::32340-2:::50912-5:::81011-9:::9086-0:::16527-4:::2950-4:::9087-8:::2954-6:::9485-4:::2957-9:::43423-3:::87451-1:::2955-3:::87452-9:::56979-8:::14055-8:::17796-4:::2948-8:::28003-2:::74993-7 | sodium [Sodium [Moles/volume] in Serum or Plasma]:::Sodium, Specimen [Sodium [Moles/volume] in Specimen]:::Sodium, Hair [Sodium [Moles/mass] in Hair]:::sodium intake [Sodium intake 24 hour Estimated]:::Sodium intake Est [Sodium intake Estimated]:::calcium/sodium [Calcium/Sodium [Mass Ratio] in Serum or Plasma]:::Sodium, Body fluid [Sodium [Moles/volume] in Body fluid]:::Sodium intake Measured [Sodium intake Measured]:::Sodium, Sweat [Sodium [Moles/volume] in Sweat]:::Sodium, Water [Sodium [Mass/volume] in Water]:::sodium renal clearance [Sodium renal clearance in 24 hour Urine and Serum or Plasma]:::sodium urate [Sodium urate [Saturation Fraction] in 24 hour Urine]:::Sodium [Mass/volume] in Specimen [Sodium [Mass/volume] in Specimen]:::Sodium, Urine [Sodium [Moles/volume] in Urine]:::Sodium [Mass/mass] in Specimen [Sodium [Mass/mass] in Specimen]:::Sodium, Saliva [Sodium [Moles/volume] in Saliva (oral fluid)]:::Sodium Stl-sCnt [Sodium [Moles/mass] in Stool]:::Sodium, Hyperal solution [Sodium [Moles/volume] in Hyperal solution]:::Sodium, Spinal fluid [Sodium [Moles/volume] in Cerebral spinal fluid]:::sodium/potassium [Sodium/Potassium [Molar ratio] in Serum or Plasma]:::Chloride+sodium Pnl [Chloride and sodium panel [Moles/volume] - Sweat]                                                                                                                                                                                                     |
| potassium             | Test    | 2823-3       | potassium [Potassium [Moles/volume] in Serum or Plasma]         | 2823-3:::10322-6:::32336-0:::59733-6:::9073-8:::28003-2:::2821-7:::50902-6:::2830-8:::9074-6:::25506-7:::9482-1:::87455-2:::2819-1:::49788-3:::2827-4:::2828-2:::59010-9:::32713-0                     | potassium [Potassium [Moles/volume] in Serum or Plasma]:::potassium intake [Potassium intake 24 hour]:::Potassium, Specimen [Potassium [Moles/volume] in Specimen]:::Potassium, Tissue [Potassium [Mass/mass] in Tissue]:::Potassium intake Est [Potassium intake Estimated]:::sodium/potassium [Sodium/Potassium [Molar ratio] in Serum or Plasma]:::Potassium, Body fluid [Potassium [Moles/volume] in Body fluid]:::Potassium, Hair [Potassium [Moles/mass] in Hair]:::potassium renal clearance [Potassium renal clearance in 24 hour Urine and Serum or Plasma]:::Potassium intake Measured [Potassium intake Measured]:::Potassium Stl-sCnt [Potassium [Moles/mass] in Stool]:::Potassium, Water [Potassium [Mass/volume] in Water]:::Potassium Spec-mCnt [Potassium [Mass/mass] in Specimen]:::Potassium, Spinal fluid [Potassium [Moles/volume] in Cerebral spinal fluid]:::Potassium Amn-sCnc [Potassium [Moles/volume] in Amniotic fluid]:::Potassium, Sweat [Potassium [Moles/volume] in Sweat]:::Potassium, Urine [Potassium [Moles/volume] in Urine]:::fractional excretion of potassium [Fractional excretion of potassium [Ratio] in Urine and Serum or Plasma collected for unspecified duration]:::Potassium BldA-sCnc [Potassium [Moles/volume] in Arterial blood]                                                                                                                                                                                                                           |
| complete blood count  | Test    | 24358-4      | Complete Blood Count [Hemogram without Platelets panel - Blood] | 24358-4:::58410-2:::74412-8:::47288-6:::1335-9:::789-8:::51876-1:::786-4:::777-3:::39227-4:::41986-1:::111539-3:::55781-9:::57022-6:::57021-8:::51637-7:::4544-3:::53963-5:::50774-9:::111533-6        | Complete Blood Count [Hemogram without Platelets panel - Blood]:::complete blood count panel [CBC panel - Blood by Automated count]:::complete blood count w differential panel [CBC W Differential panel - Cord blood]:::complete blood count wo differential panel [CBC WO Differential panel - Cord blood]:::whole blood given [Whole blood given [Volume]]:::Whole blood [Erythrocytes [#/volume] in Blood by Automated count]:::whole blood units given [Whole blood units given [#]]:::HEMATOLOGY/CELL COUNTS [MCHC [Entitic Mass/volume] in Red Blood Cells by Automated count]:::Platelet count [Platelets [#/volume] in Blood by Automated count]:::hematocrit test status [Hematocrit test status CPHS]:::Hematocrit Test Status/Results [Hematocrit test status/results Set CPHS]:::Hematocrit [Hematocrit [Volume Fraction] adjusted to ideal blood volume by calculation]:::Hematocrit, Bone marrow [Hematocrit [Volume Fraction] of Bone marrow by calculation]:::complete blood count w reflex manual differential panel [CBC W Reflex Manual Differential panel - Blood]:::complete blood count w auto differential panel [CBC W Auto Differential panel - Blood]:::plateletocrit [Plateletcrit [Volume Fraction] in Blood]:::Hematocrit, Blood [Hematocrit [Volume Fraction] of Blood by Automated count]:::blood [Blood [Presence] in Urine by Visual]:::Nucleated cells, Blood [Nucleated cells [#/volume] in Blood]:::specimen count [Specimen Count [#] by calculation]                   |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_loinc_numeric_augmented_pipeline_2_83|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.1 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel