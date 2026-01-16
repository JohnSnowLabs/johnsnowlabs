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
- ner_jsl_langtest: Extracts 60+ medical entity types (symptoms, diseases, vitals, procedures, etc.)
- ner_posology_greedy: Extracts drug-related entities (DRUG, DOSAGE, FREQUENCY, ROUTE, etc.)
- ner_deid_subentity_augmented_v2: Extracts PATIENT, DOCTOR, and HOSPITAL names

**Text Matchers:**
- procedure_matcher, drug_matcher, cancer_diagnosis_matcher, symptom_matcher

**Contextual Parsers:**
- age_parser: Extracts age mentions
- date_matcher + DateNormalizer: Extracts and normalizes dates

**Assertion Models:**
- 9 Assertion models: family, someoneelse, absent, past, planned, conditional, hypothetical, possible

**Output:** Merged entities with assertion status (present, absent, past, family, planned, possible, conditional, hypothetical, someoneelse).
Additionally, in the output, you will see entities that are not related to the assertion status as `no_assertion`.

## Predicted Entities

`TEST`, `HOSPITAL`, `PATIENT`, `DOCTOR`, `ADMISSION_DISCHARGE`, `AGE`, `ALCOHOL`, `ALLERGEN`, `BIRTH_ENTITY`, `CEREBROVASCULAR_DISEASE`, `CLINICAL_DEPT`, `COMMUNICABLE_DISEASE`, `DEATH_ENTITY`, `DIABETES`, `DIET`, `DIRECTION`, `DISEASE_SYNDROME_DISORDER`, `EMPLOYMENT`, `EXTERNAL_BODY_PART_OR_REGION`, `FAMILY_HISTORY_HEADER`, `FETUS_NEWBORN`, `GENDER`, `HEART_DISEASE`, `HYPERLIPIDEMIA`, `HYPERTENSION`, `INJURY_OR_POISONING`, `INTERNAL_ORGAN_OR_COMPONENT`, `KIDNEY_DISEASE`, `LABOUR_DELIVERY`, `MEDICAL_DEVICE`, `MEDICAL_HISTORY_HEADER`, `MODIFIER`, `OBESITY`, `ONCOLOGICAL`, `OVERWEIGHT`, `OXYGEN_THERAPY`, `PREGNANCY`, `PROCEDURE`, `PSYCHOLOGICAL_CONDITION`, `RACE_ETHNICITY`, `RELATIONSHIP_STATUS`, `SECTION_HEADER`, `SEXUALLY_ACTIVE_OR_SEXUAL_ORIENTATION`, `SMOKING`, `SOCIAL_HISTORY_HEADER`, `SUBSTANCE`, `SUBSTANCE_QUANTITY`, `SYMPTOM`, `TREATMENT`, `VACCINE`, `VACCINE_NAME`, `VITAL_SIGNS_HEADER`, `TEST_RESULT`, `BLOOD_PRESSURE`, `PULSE`, `RESPIRATION`, `O2_SATURATION`, `TEMPERATURE`, `VS_FINDING`, `HEIGHT`, `WEIGHT`, `BMI`, `EKG_FINDINGS`, `IMAGINGFINDINGS`, `LDL`, `HDL`, `TRIGLYCERIDES`, `TOTAL_CHOLESTEROL`, `IMAGING_TECHNIQUE`, `DATE`, `RELATIVEDATE`, `RELATIVETIME`, `TIME`, `DRUG`, `STRENGTH`, `DURATION`, `FREQUENCY`, `FORM`, `DOSAGE`, `ROUTE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/omop_ner_assertion_pipeline_en_6.2.0_3.4_1768521482967.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/omop_ner_assertion_pipeline_en_6.2.0_3.4_1768521482967.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("omop_ner_assertion_pipeline", "en", "clinical/models")

text = """GENERAL: He is an elderly gentleman in no acute distress. He is sitting up in bed eating his breakfast. He is alert and oriented and answering questions appropriately.
HEENT: Sclerae showed mild arcus senilis in the right. Left was clear. Pupils are equally round and reactive to light. Extraocular movements are intact. Oropharynx is clear.
NECK: Supple. Trachea is midline. No jugular venous pressure distention is noted. No adenopathy in the cervical, supraclavicular, or axillary areas.
ABDOMEN: Soft and not tender. There may be some fullness in the left upper quadrant, although I do not appreciate a true spleen with inspiration.
EXTREMITIES: There is some edema, but no cyanosis and clubbing .
IMPRESSION: There are no sign or symptom of blood loss and the previous esophagogastroduodenoscopy was negative. His creatinine was 1.
  My impression at this time is that he probably has an underlying myelodysplastic syndrome or bone marrow failure. His creatinine on this hospitalization was up slightly to 1.6 and this may contribute to his anemia.
  At this time, my recommendation for the patient is that he should undergo a bone marrow aspiration.
  I have discussed the procedure in detail which the patient. I have discussed the risks, benefits, and successes of that treatment and usefulness of the bone marrow and predicting his cause of refractory anemia and further therapeutic interventions, which might be beneficial to him.
  He is willing to proceed with the studies I have described to him. We will order an ultrasound of his abdomen because of the possible fullness of the spleen."""

result = pipeline.fullAnnotate(text)

```

{:.jsl-block}
```python

pipeline = nlp.PretrainedPipeline("omop_ner_assertion_pipeline", "en", "clinical/models")

text = """GENERAL: He is an elderly gentleman in no acute distress. He is sitting up in bed eating his breakfast. He is alert and oriented and answering questions appropriately.
HEENT: Sclerae showed mild arcus senilis in the right. Left was clear. Pupils are equally round and reactive to light. Extraocular movements are intact. Oropharynx is clear.
NECK: Supple. Trachea is midline. No jugular venous pressure distention is noted. No adenopathy in the cervical, supraclavicular, or axillary areas.
ABDOMEN: Soft and not tender. There may be some fullness in the left upper quadrant, although I do not appreciate a true spleen with inspiration.
EXTREMITIES: There is some edema, but no cyanosis and clubbing .
IMPRESSION: There are no sign or symptom of blood loss and the previous esophagogastroduodenoscopy was negative. His creatinine was 1.
  My impression at this time is that he probably has an underlying myelodysplastic syndrome or bone marrow failure. His creatinine on this hospitalization was up slightly to 1.6 and this may contribute to his anemia.
  At this time, my recommendation for the patient is that he should undergo a bone marrow aspiration.
  I have discussed the procedure in detail which the patient. I have discussed the risks, benefits, and successes of that treatment and usefulness of the bone marrow and predicting his cause of refractory anemia and further therapeutic interventions, which might be beneficial to him.
  He is willing to proceed with the studies I have described to him. We will order an ultrasound of his abdomen because of the possible fullness of the spleen."""

result = pipeline.fullAnnotate(text)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("omop_ner_assertion_pipeline", "en", "clinical/models")

val text = """GENERAL: He is an elderly gentleman in no acute distress. He is sitting up in bed eating his breakfast. He is alert and oriented and answering questions appropriately.
HEENT: Sclerae showed mild arcus senilis in the right. Left was clear. Pupils are equally round and reactive to light. Extraocular movements are intact. Oropharynx is clear.
NECK: Supple. Trachea is midline. No jugular venous pressure distention is noted. No adenopathy in the cervical, supraclavicular, or axillary areas.
ABDOMEN: Soft and not tender. There may be some fullness in the left upper quadrant, although I do not appreciate a true spleen with inspiration.
EXTREMITIES: There is some edema, but no cyanosis and clubbing .
IMPRESSION: There are no sign or symptom of blood loss and the previous esophagogastroduodenoscopy was negative. His creatinine was 1.
  My impression at this time is that he probably has an underlying myelodysplastic syndrome or bone marrow failure. His creatinine on this hospitalization was up slightly to 1.6 and this may contribute to his anemia.
  At this time, my recommendation for the patient is that he should undergo a bone marrow aspiration.
  I have discussed the procedure in detail which the patient. I have discussed the risks, benefits, and successes of that treatment and usefulness of the bone marrow and predicting his cause of refractory anemia and further therapeutic interventions, which might be beneficial to him.
  He is willing to proceed with the studies I have described to him. We will order an ultrasound of his abdomen because of the possible fullness of the spleen."""

val result = pipeline.fullAnnotate(text)

```
</div>

## Results

```bash

+------------------------------------+-------+------+------------------------------+--------------+------+
|chunk_text                         |begin |end  |entity_type                  |assertion    |
+------------------------------------+-------+------+------------------------------+--------------+------+
|GENERAL:                           |0     |7    |VITAL_SIGNS_HEADER           |no_assertion |
|He                                 |9     |10   |GENDER                       |no_assertion |
|elderly                            |18    |24   |AGE                          |no_assertion |
|gentleman                          |26    |34   |GENDER                       |no_assertion |
|no acute distress                  |39    |55   |SYMPTOM                      |absent       |
|He                                 |58    |59   |GENDER                       |no_assertion |
|his                                |89    |91   |GENDER                       |no_assertion |
|He                                 |104   |105  |GENDER                       |no_assertion |
|Sclerae                            |175   |181  |INTERNAL_ORGAN_OR_COMPONENT  |no_assertion |
|mild                               |190   |193  |MODIFIER                     |no_assertion |
|arcus senilis                      |195   |207  |SYMPTOM                      |present      |
|right                              |216   |220  |DIRECTION                    |no_assertion |
|Left                               |223   |226  |DIRECTION                    |no_assertion |
|Pupils                             |239   |244  |EXTERNAL_BODY_PART_OR_REGION |no_assertion |
|Oropharynx                         |321   |330  |INTERNAL_ORGAN_OR_COMPONENT  |no_assertion |
|Trachea                            |356   |362  |INTERNAL_ORGAN_OR_COMPONENT  |no_assertion |
|midline                            |367   |373  |DIRECTION                    |no_assertion |
|jugular venous pressure distention |379   |412  |SYMPTOM                      |absent       |
|adenopathy                         |427   |436  |SYMPTOM                      |absent       |
|cervical                           |445   |452  |EXTERNAL_BODY_PART_OR_REGION |no_assertion |
|supraclavicular                    |455   |469  |EXTERNAL_BODY_PART_OR_REGION |no_assertion |
|axillary areas                     |475   |488  |EXTERNAL_BODY_PART_OR_REGION |no_assertion |
|tender                             |513   |518  |SYMPTOM                      |absent       |
|fullness                           |539   |546  |SYMPTOM                      |possible     |
|left                               |555   |558  |DIRECTION                    |no_assertion |
|upper quadrant                     |560   |573  |EXTERNAL_BODY_PART_OR_REGION |no_assertion |
|true spleen with inspiration       |607   |634  |SYMPTOM                      |absent       |
|edema                              |664   |668  |SYMPTOM                      |present      |
|cyanosis                           |678   |685  |SYMPTOM                      |absent       |
|clubbing                           |691   |698  |SYMPTOM                      |absent       |
|IMPRESSION:                        |702   |712  |SECTION_HEADER               |no_assertion |
|blood loss                         |746   |755  |SYMPTOM                      |absent       |
|esophagogastroduodenoscopy         |774   |799  |PROCEDURE                    |past         |
|negative                           |805   |812  |TEST_RESULT                  |past         |
|His                                |815   |817  |GENDER                       |no_assertion |
|creatinine                         |819   |828  |TEST                         |present      |
|he                                 |874   |875  |GENDER                       |no_assertion |
|underlying                         |893   |902  |MODIFIER                     |no_assertion |
|myelodysplastic syndrome           |904   |927  |Cancer_dx                    |possible     |
|bone marrow failure                |932   |950  |DISEASE_SYNDROME_DISORDER    |possible     |
|His                                |953   |955  |GENDER                       |no_assertion |
|creatinine                         |957   |966  |TEST                         |present      |
|hospitalization                    |976   |990  |ADMISSION_DISCHARGE          |no_assertion |
|1.6                                |1011  |1013 |TEST_RESULT                  |present      |
|his                                |1042  |1044 |GENDER                       |no_assertion |
|anemia                             |1046  |1051 |DISEASE_SYNDROME_DISORDER    |possible     |
|he                                 |1112  |1113 |GENDER                       |no_assertion |
|bone marrow aspiration             |1132  |1153 |PROCEDURE                    |hypothetical |
|procedure                          |1179  |1187 |PROCEDURE                    |planned      |
|bone marrow                        |1310  |1320 |INTERNAL_ORGAN_OR_COMPONENT  |no_assertion |
|his                                |1337  |1339 |GENDER                       |no_assertion |
|refractory                         |1350  |1359 |MODIFIER                     |no_assertion |
|anemia                             |1361  |1366 |DISEASE_SYNDROME_DISORDER    |present      |
|him                                |1436  |1438 |GENDER                       |no_assertion |
|He                                 |1443  |1444 |GENDER                       |no_assertion |
|him                                |1505  |1507 |GENDER                       |no_assertion |
|ultrasound                         |1527  |1536 |PROCEDURE                    |planned      |
|fullness                           |1577  |1584 |SYMPTOM                      |possible     |
+------------------------------------+-------+------+------------------------------+--------------+------+

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
- RegexMatcherInternalModel
- NerConverterInternalModel
- ChunkMergeModel
- DateNormalizer
- ContextualParserModel
- ChunkConverter
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
- AnnotationConverter
- AssertionMerger