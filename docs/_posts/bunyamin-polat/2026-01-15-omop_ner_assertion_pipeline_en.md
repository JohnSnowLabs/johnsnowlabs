---
layout: model
title: Complete OMOP Pipeline for Entity Extraction and Assertion Status
author: John Snow Labs
name: omop_ner_assertion_pipeline
date: 2026-01-15
tags: [licensed, en, clinical, pipeline, ner, assertion, omop]
task: [Named Entity Recognition, Assertion Status, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

A comprehensive medical NLP pipeline designed for clinical entity extraction and assertion status detection from medical text.

**NER Models:**
- ner_clinical_large_langtest: Extracts PROBLEM and TEST entities
- ner_jsl_langtest: Extracts 60+ medical entity types (symptoms, diseases, vitals, procedures, etc.)
- ner_posology_greedy: Extracts drug-related entities (DRUG, DOSAGE, FREQUENCY, ROUTE, etc.)
- ner_deid_subentity_augmented_v2: Extracts PATIENT, DOCTOR, and HOSPITAL names

**Text Matchers:**
- procedure_matcher, drug_matcher, cancer_diagnosis_matcher, symptom_matcher

**Contextual Parsers:**
- age_parser: Extracts age mentions
- test_result_parser: Extracts test results with values
- date_matcher + DateNormalizer: Extracts and normalizes dates

**Assertion Models:**
- 9 Assertion models: family, someoneelse, absent, past, planned, conditional, hypothetical, possible

**Output:** Merged entities with assertion status (present, absent, past, family, planned, possible, conditional, hypothetical, someoneelse)

## Predicted Entities

`PROBLEM`, `TEST`, `HOSPITAL`, `PATIENT`, `DOCTOR`, `ADMISSION_DISCHARGE`, `AGE`, `ALCOHOL`, `ALLERGEN`, `BIRTH_ENTITY`, `CEREBROVASCULAR_DISEASE`, `CLINICAL_DEPT`, `COMMUNICABLE_DISEASE`, `DEATH_ENTITY`, `DIABETES`, `DIET`, `DIRECTION`, `DISEASE_SYNDROME_DISORDER`, `EMPLOYMENT`, `EXTERNAL_BODY_PART_OR_REGION`, `FAMILY_HISTORY_HEADER`, `FETUS_NEWBORN`, `GENDER`, `HEART_DISEASE`, `HYPERLIPIDEMIA`, `HYPERTENSION`, `INJURY_OR_POISONING`, `INTERNAL_ORGAN_OR_COMPONENT`, `KIDNEY_DISEASE`, `LABOUR_DELIVERY`, `MEDICAL_DEVICE`, `MEDICAL_HISTORY_HEADER`, `MODIFIER`, `OBESITY`, `ONCOLOGICAL`, `OVERWEIGHT`, `OXYGEN_THERAPY`, `PREGNANCY`, `PROCEDURE`, `PSYCHOLOGICAL_CONDITION`, `RACE_ETHNICITY`, `RELATIONSHIP_STATUS`, `SECTION_HEADER`, `SEXUALLY_ACTIVE_OR_SEXUAL_ORIENTATION`, `SMOKING`, `SOCIAL_HISTORY_HEADER`, `SUBSTANCE`, `SUBSTANCE_QUANTITY`, `SYMPTOM`, `TREATMENT`, `VACCINE`, `VACCINE_NAME`, `VITAL_SIGNS_HEADER`, `TEST_RESULT`, `BLOOD_PRESSURE`, `PULSE`, `RESPIRATION`, `O2_SATURATION`, `TEMPERATURE`, `VS_FINDING`, `HEIGHT`, `WEIGHT`, `BMI`, `EKG_FINDINGS`, `IMAGINGFINDINGS`, `LDL`, `HDL`, `TRIGLYCERIDES`, `TOTAL_CHOLESTEROL`, `IMAGING_TECHNIQUE`, `DATE`, `RELATIVEDATE`, `RELATIVETIME`, `TIME`, `DRUG`, `STRENGTH`, `DURATION`, `FREQUENCY`, `FORM`, `DOSAGE`, `ROUTE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/omop_ner_assertion_pipeline_en_6.2.0_3.4_1768437857603.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/omop_ner_assertion_pipeline_en_6.2.0_3.4_1768437857603.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("omop_ner_assertion_pipeline", "en", "clinical/models")

text = """Patient had a headache for the last 2 weeks and appears anxious when walking fast. No alopecia noted. She denies any pain. Her father is paralyzed which is a stressor for her. She was given an antidepressant. We prescribed sleeping pills for her current insomnia."""

result = pipeline.fullAnnotate(text)

```

{:.jsl-block}
```python

pipeline = nlp.PretrainedPipeline("omop_ner_assertion_pipeline", "en", "clinical/models")

text = """Patient had a headache for the last 2 weeks and appears anxious when walking fast. No alopecia noted. She denies any pain. Her father is paralyzed which is a stressor for her. She was given an antidepressant. We prescribed sleeping pills for her current insomnia."""

result = pipeline.fullAnnotate(text)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("omop_ner_assertion_pipeline", "en", "clinical/models")

val text = """Patient had a headache for the last 2 weeks and appears anxious when walking fast. No alopecia noted. She denies any pain. Her father is paralyzed which is a stressor for her. She was given an antidepressant. We prescribed sleeping pills for her current insomnia."""

val result = pipeline.fullAnnotate(text)

```
</div>

## Results

```bash

+---------------------------+-------+-----+-------------+-----------+------+
|chunk_text                |begin |end |entity_type |assertion |
+---------------------------+-------+-----+-------------+-----------+------+
|a headache                |12    |21  |PROBLEM     |past      |
|anxious when walking fast |56    |80  |SYMPTOM     |possible  |
|alopecia                  |86    |93  |PROBLEM     |absent    |
|any pain                  |113   |120 |PROBLEM     |absent    |
|paralyzed                 |137   |145 |SYMPTOM     |family    |
|stressor                  |158   |165 |SYMPTOM     |present   |
|antidepressant            |193   |206 |DRUG        |present   |
|her current insomnia      |242   |261 |PROBLEM     |present   |
+---------------------------+-------+-----+-------------+-----------+------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|omop_ner_assertion_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- WordEmbeddingsModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- RegexMatcherInternalModel
- NerConverterInternalModel
- ChunkMergeModel
- DateNormalizer
- ContextualParserModel
- ChunkConverter
- ContextualParserModel
- ChunkConverter
- ChunkMergeModel
- ChunkMergeModel
- ContextualAssertion
- ContextualAssertion
- ContextualAssertion
- ContextualAssertion
- ContextualAssertion
- ContextualAssertion
- ContextualAssertion
- ContextualAssertion
- AssertionDLModel
- AssertionMerger