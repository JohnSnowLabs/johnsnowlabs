---
layout: model
title: Pipeline for Logical Observation Identifiers Names and Codes (LOINC-Numeric) (sbiobert_base_cased_mli_onnx embeddings)
author: John Snow Labs
name: sbiobertresolve_loinc_numeric_pipeline_2_83
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

This pipeline extracts `TEST` entities and maps them to their corresponding Logical Observation Identifiers Names and Codes (LOINC) codes using `sbiobert_base_cased_mli` sentence embeddings.

Trained on the official LOINC 2.83 dataset, scoped to numeric LOINC codes, without the inclusion of LOINC "Document Ontology" codes starting with the letter "L".

If you also need LOINC's non-numeric auxiliary codes (e.g. Part codes prefixed "LP"), use `sbiobertresolve_loinc_pipeline_2_83` instead.

It also provides the official resolution of the codes within the brackets.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_loinc_numeric_pipeline_2_83_en_6.4.1_3.4_1788740225697.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_loinc_numeric_pipeline_2_83_en_6.4.1_3.4_1788740225697.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

loinc_pipeline = PretrainedPipeline("sbiobertresolve_loinc_numeric_pipeline_2_83", "en", "clinical/models")

data = spark.createDataFrame([["The patient's glucose and hemoglobin A1c levels were checked, along with a basic metabolic panel including sodium and potassium, and a complete blood count."]]).toDF("text")
result = loinc_pipeline.transform(data)

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

loinc_pipeline = nlp.PretrainedPipeline("sbiobertresolve_loinc_numeric_pipeline_2_83", "en", "clinical/models")

data = spark.createDataFrame([["The patient's glucose and hemoglobin A1c levels were checked, along with a basic metabolic panel including sodium and potassium, and a complete blood count."]]).toDF("text")
result = loinc_pipeline.transform(data)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val loinc_pipeline = PretrainedPipeline("sbiobertresolve_loinc_numeric_pipeline_2_83", "en", "clinical/models")

val data = Seq("The patient's glucose and hemoglobin A1c levels were checked, along with a basic metabolic panel including sodium and potassium, and a complete blood count.").toDF("text")
val result = loinc_pipeline.transform(data)

```
</div>

## Results

```bash
| chunk                 | label   | loinc_code   | resolution                                                      | all_codes                                                                                                                                                                                                 | all_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:----------------------|:--------|:-------------|:----------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| glucose               | Test    | 2345-7       | glucose [Glucose [Mass/volume] in Serum or Plasma]              | 2345-7:::74790-7:::51419-0:::81637-1:::47621-8:::104638-2:::50016-5:::72648-9:::27353-2:::6248-9:::41653-7:::4269-7:::95720-9:::41896-2:::26682-5:::50667-5:::97506-0:::80093-8:::20643-3                 | glucose [Glucose [Mass/volume] in Serum or Plasma]:::Glucose HBT [Glucose challenge (hydrogen breath test) panel - Exhaled gas]:::Glucose cor [Sodium [Moles/volume] corrected for glucose in Serum or Plasma]:::Glucose correlation [Glucose meter to reference method correlation [Ratio] in Serum, Plasma or Blood by calculation]:::glucose.iv [Glucose.IV [Mass] of Dose]:::Glucose SD [Glucose standard deviation/Glucose mean in Reporting Period Interstitial fluid by calculation]:::sugar [Sugar [Type] of Dose]:::glucose gradient [Glucose in serum - glucose in synovial fluid [Molar concentration difference]]:::Glucose mean value [Glucose mean value [Mass/volume] in Blood Estimated from glycated hemoglobin]:::Gly [Soybean IgE Ab [Units/volume] in Serum]:::Glucomtr [Glucose [Mass/volume] in Capillary blood by Glucometer]:::glucose.po [Glucose.PO [Mass] of Dose]:::GlyR [Glycine receptor Ab [Titer] in Serum or Plasma by Immunoassay]:::Glucose Mtr Dev [Type of Glucose meter device]:::glycolate [Glycolate [Presence] in Urine]:::glucose tolerance [Glucose tolerance [Interpretation] in Serum or Plasma Narrative]:::Glucose management indicator [Glucose management indicator]:::glucosamine [Glucosamine [Moles/volume] in Serum or Plasma]:::Gln [Glutamine [Moles/volume] in Serum or Plasma]                                                                                                                                                                                                                                                                                                                                                                                                                       |
| hemoglobin A1c levels | Test    | 41995-2      | hemoglobin a1c [Hemoglobin A1c [Mass/volume] in Blood]          | 41995-2:::43150-2:::4548-4:::10486-9:::21687-9:::112870-1:::51196-4:::10346-5:::50319-3:::17871-5:::4593-0:::50385-4:::6864-3:::72914-5:::14563-1:::96595-4:::2030-5:::2865-4:::62854-5:::96496-5         | hemoglobin a1c [Hemoglobin A1c [Mass/volume] in Blood]:::Hemoglobin A1c measurement device panel [Hemoglobin A1c measurement device panel]:::hemoglobin a1c/hemoglobin.total [Hemoglobin A1c/Hemoglobin.total in Blood]:::hemoglobin ag [Hemoglobin Ag [Presence] in Tissue by Immune stain]:::Hemoglobin, alpha 1 [HBA1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal]:::hemoglobin a1c & estimated average glucose panel [Hemoglobin A1c and estimated average glucose panel - Blood]:::hemoglobin a1/hemoglobin.total [Hemoglobin A1/Hemoglobin.total in Blood by Electrophoresis]:::hemoglobin a [Hemoglobin A [Units/volume] in Blood by Electrophoresis]:::hbme-1 ag [HBME-1 Ag [Presence] in Tissue by Immune stain]:::hemoglobin h [Hemoglobin H [Presence] in Blood by Heat denaturation]:::hemoglobin i [Hemoglobin I [Presence] in Blood by Electrophoresis acid (pH 6.3)]:::A1 Microglob [Alpha-1-Microglobulin.placental [Presence] in Vaginal fluid]:::hemoglobin s [Hemoglobin S [Presence] in Blood by Solubility test]:::hna 1c ab [HNA 1c Ab [Presence] in Serum by Immunoassay]:::hemoglobin^1st specimen [Hemoglobin [Presence] in Stool from gastrointestinal --1st specimen]:::Hemoglobin A1c/Hemoglobin.total in DBS [Hemoglobin A1c/Hemoglobin.total in DBS]:::CO Hemoglobin [Carboxyhemoglobin/Hemoglobin.total in Arterial blood]:::alpha 1 globulin [Alpha 1 globulin [Mass/volume] in Serum or Plasma by Electrophoresis]:::Glycosylated hemoglobin assay [PhenX - glycosylated hemoglobin assay reflecting long-term glucose concentration protocol 140901]:::GlyRa-1 Ab [Glycine receptor alpha-1 subunit IgG Ab [Presence] in Serum by Cell binding immunofluorescent assay] |
| basic metabolic panel | Test    | 51990-0      | basic metabolic panel [Basic metabolic panel - Blood]           | 51990-0:::101655-9:::89044-2:::9350-0:::50042-1:::79531-0:::43147-8:::24321-2:::79529-4:::104076-5:::79530-2:::112034-4:::81578-7:::1547-9:::107464-0:::41966-3                                           | basic metabolic panel [Basic metabolic panel - Blood]:::basic metabolic & hematocrit panel [Basic metabolic and hematocrit panel - Blood]:::basic metabolic & albumin panel [Basic metabolic and albumin panel - Serum or Plasma]:::Metabolic screen [Sulfhydryls [Presence] in Urine]:::Basal metabolic rate index [Basal metabolic rate index]:::basic mobility items [Basic mobility items number [Activity Measure for Post-Acute Care]]:::Metabolism measurement device panel [Metabolism measurement device panel]:::basic metabolic 2000 panel [Basic metabolic 2000 panel - Serum or Plasma]:::basic mobility score [Basic mobility score [AM-PAC]]:::basic metabolic & hemoglobin & hematocrit panel [Basic metabolic with hemoglobin and hematocrit panel - Blood]:::Basic mobility score SE [Basic mobility score standard error [AM-PAC]]:::Basic information [Basic information]:::PT Brain metabolic [PT Brain metabolic]:::glucose^baseline [Glucose [Mass/volume] in Serum or Plasma --baseline]:::metabolic disease screening [Metabolic disease screening Newborn]:::Name of Metabolism measurement device [Name of Metabolism measurement device]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| sodium                | Test    | 2951-2       | sodium [Sodium [Moles/volume] in Serum or Plasma]               | 2951-2:::81011-9:::9086-0:::16527-4:::9087-8:::2957-9:::43423-3:::87451-1:::50912-5:::87452-9:::14055-8:::28003-2:::74993-7:::51205-3:::23611-7:::2954-6:::2950-4:::32340-2:::43223-7:::49135-7:::54437-9 | sodium [Sodium [Moles/volume] in Serum or Plasma]:::sodium intake [Sodium intake 24 hour Estimated]:::Sodium intake Est [Sodium intake Estimated]:::calcium/sodium [Calcium/Sodium [Mass Ratio] in Serum or Plasma]:::Sodium intake Measured [Sodium intake Measured]:::sodium renal clearance [Sodium renal clearance in 24 hour Urine and Serum or Plasma]:::sodium urate [Sodium urate [Saturation Fraction] in 24 hour Urine]:::Sodium [Mass/volume] in Specimen [Sodium [Mass/volume] in Specimen]:::Sodium Hair-sCnt [Sodium [Moles/mass] in Hair]:::Sodium [Mass/mass] in Specimen [Sodium [Mass/mass] in Specimen]:::Sodium Stl-sCnt [Sodium [Moles/mass] in Stool]:::sodium/potassium [Sodium/Potassium [Molar ratio] in Serum or Plasma]:::Chloride+sodium Pnl [Chloride and sodium panel [Moles/volume] - Sweat]:::Sodium Hair-mCnt [Sodium [Mass/mass] in Hair]:::Nemasol sodium [Para aminosalicylate [Susceptibility] by Method for Slow-growing mycobacteria]:::Sodium Sweat-sCnc [Sodium [Moles/volume] in Sweat]:::Sodium [Moles/volume] in Body fluid [Sodium [Moles/volume] in Body fluid]:::Sodium Spec-sCnc [Sodium [Moles/volume] in Specimen]:::Sodium/Creat Ur-Rto [Sodium/Creatinine [Ratio] in Urine]:::fractional excretion of sodium [Fractional excretion of sodium [Ratio] in Urine and Serum or Plasma]:::sodium urate/total [Sodium urate/Total in Stone by Infrared spectroscopy]                                                                                                                                                                                                                                                                                                                                            |
| potassium             | Test    | 2823-3       | potassium [Potassium [Moles/volume] in Serum or Plasma]         | 2823-3:::10322-6:::9073-8:::28003-2:::2830-8:::59733-6:::9074-6:::25506-7:::87455-2:::50902-6:::32336-0:::49788-3:::59010-9:::32713-0:::79710-0:::87454-5:::9482-1:::12814-0:::2828-2:::34548-8:::6940-1  | potassium [Potassium [Moles/volume] in Serum or Plasma]:::potassium intake [Potassium intake 24 hour]:::Potassium intake Est [Potassium intake Estimated]:::sodium/potassium [Sodium/Potassium [Molar ratio] in Serum or Plasma]:::potassium renal clearance [Potassium renal clearance in 24 hour Urine and Serum or Plasma]:::Potassium Tiss-mCnt [Potassium [Mass/mass] in Tissue]:::Potassium intake Measured [Potassium intake Measured]:::Potassium Stl-sCnt [Potassium [Moles/mass] in Stool]:::Potassium Spec-mCnt [Potassium [Mass/mass] in Specimen]:::Potassium Hair-sCnt [Potassium [Moles/mass] in Hair]:::Potassium Spec-sCnc [Potassium [Moles/volume] in Specimen]:::Potassium Amn-sCnc [Potassium [Moles/volume] in Amniotic fluid]:::fractional excretion of potassium [Fractional excretion of potassium [Ratio] in Urine and Serum or Plasma collected for unspecified duration]:::Potassium BldA-sCnc [Potassium [Moles/volume] in Arterial blood]:::Potassium Hair-mCnt [Potassium [Mass/mass] in Hair]:::Potassium [Mass/volume] in Specimen [Potassium [Mass/volume] in Specimen]:::Potassium Wat-mCnc [Potassium [Mass/volume] in Water]:::Potassium Vitf-sCnc [Potassium [Moles/volume] in Vitreous fluid]:::Potassium Ur-sCnc [Potassium [Moles/volume] in Urine]:::Sodium + Potassium Pnl [Sodium and Potassium panel [Moles/volume] - Serum or Plasma]:::Potassium ?Tm Stl-sRate [Potassium [Moles/time] in unspecified time Stool]                                                                                                                                                                                                                                                                                              |
| complete blood count  | Test    | 24358-4      | Complete Blood Count [Hemogram without Platelets panel - Blood] | 24358-4:::58410-2:::74412-8:::47288-6:::1335-9:::789-8:::51876-1:::786-4:::777-3:::39227-4:::41986-1:::57022-6:::57021-8:::51637-7:::53963-5:::111533-6:::34556-1:::24360-0:::91604-9:::43113-0           | Complete Blood Count [Hemogram without Platelets panel - Blood]:::complete blood count panel [CBC panel - Blood by Automated count]:::complete blood count w differential panel [CBC W Differential panel - Cord blood]:::complete blood count wo differential panel [CBC WO Differential panel - Cord blood]:::whole blood given [Whole blood given [Volume]]:::Whole blood [Erythrocytes [#/volume] in Blood by Automated count]:::whole blood units given [Whole blood units given [#]]:::HEMATOLOGY/CELL COUNTS [MCHC [Entitic Mass/volume] in Red Blood Cells by Automated count]:::Platelet count [Platelets [#/volume] in Blood by Automated count]:::hematocrit test status [Hematocrit test status CPHS]:::Hematocrit Test Status/Results [Hematocrit test status/results Set CPHS]:::complete blood count w reflex manual differential panel [CBC W Reflex Manual Differential panel - Blood]:::complete blood count w auto differential panel [CBC W Auto Differential panel - Blood]:::plateletocrit [Plateletcrit [Volume Fraction] in Blood]:::blood [Blood [Presence] in Urine by Visual]:::specimen count [Specimen Count [#] by calculation]:::Cell count panel - Body fluid [Cell count panel - Body fluid]:::hemoglobin & hematocrit panel [Hemoglobin and Hematocrit panel - Blood]:::Device count [Device count]:::hemoglobin panel [Hemoglobin electrophoresis panel in Blood]                                                                                                                                                                                                                                                                                                                                                          |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_loinc_numeric_pipeline_2_83|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.0 GB|

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