---
layout: model
title: "Extracts Age, Age Groups, ADE, MedDRA codes, Laboratory Tests and Results, Medical History, and Administory information.

Pipeline Description: 
This pipeline is designed to process clinical text and extract a variety of entities, including:
- Age and Age Groups: Identifies mentions of patient age and categorizes them into age groups.
- ADE (Adverse Drug Events): Extracts mentions of adverse drug events.
- MedDRA Codes: Maps extracted medical terms to MedDRA (Medical Dictionary for Regulatory Activities) Lowest Level Terms (LLTs).
- Posology: Extracts information related to drug dosage, frequency, route, strength, and duration.
- Laboratory Test and Result: Identifies laboratory tests and their corresponding results.
- Medical History: Extracts information about the patient's medical history.
- Administory: Extracts administrative information.

The pipeline utilizes a combination of rule-based and deep learning models for robust entity recognition and mapping."
author: John Snow Labs
name: ner_ade_age_meddra_test_pipeline
date: 2025-06-29
tags: [licensed, clinical, en, pipeline, ner, ade, drug, age, meddra, test]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.0.3
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Extracts Age Groups, ADE, MedDRA, Tests, Medical History

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_ade_age_meddra_test_pipeline_en_6.0.3_3.4_1751219502637.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_ade_age_meddra_test_pipeline_en_6.0.3_3.4_1751219502637.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_ade_age_meddra_test_pipeline", "en", "clinical/models")

text = """A 75-year-old female presented with complaints of itching, sore/burning throat, and numbness of the tongue and gums shortly after initiating intravenous Vancomycin therapy. The symptoms were consistent with an allergic-type reaction. The medication was discontinued, and symptoms gradually resolved.
Subsequently, the patient reported taking Atorvastatin (Lipitor), presumably for hypercholesterolemia. After several days, they developed acute-onset, intermittent epigastric and flank pain radiating to the back. The abdominal pain persisted for a week, with episodes severe enough to cause sleep disturbance. The patient also experienced intermittent urinary urgency without dysuria or fever and had recently recovered from a urinary tract infection (UTI), which was considered unrelated due to symptom variation.
Upon self-discontinuation of Atorvastatin, the patient reported immediate relief from both gastrointestinal discomfort and urinary urgency. Additionally, they noted improvement in energy levels, which had been attributed to stress but were retrospectively linked to the medication.
"""

result = ner_pipeline.fullAnnotate(text)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

ner_pipeline = nlp.PretrainedPipeline("ner_ade_age_meddra_test_pipeline", "en", "clinical/models")

text = """A 75-year-old female presented with complaints of itching, sore/burning throat, and numbness of the tongue and gums shortly after initiating intravenous Vancomycin therapy. The symptoms were consistent with an allergic-type reaction. The medication was discontinued, and symptoms gradually resolved.
Subsequently, the patient reported taking Atorvastatin (Lipitor), presumably for hypercholesterolemia. After several days, they developed acute-onset, intermittent epigastric and flank pain radiating to the back. The abdominal pain persisted for a week, with episodes severe enough to cause sleep disturbance. The patient also experienced intermittent urinary urgency without dysuria or fever and had recently recovered from a urinary tract infection (UTI), which was considered unrelated due to symptom variation.
Upon self-discontinuation of Atorvastatin, the patient reported immediate relief from both gastrointestinal discomfort and urinary urgency. Additionally, they noted improvement in energy levels, which had been attributed to stress but were retrospectively linked to the medication.
"""

result = ner_pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_ade_age_meddra_test_pipeline", "en", "clinical/models")

val text = """A 75-year-old female presented with complaints of itching, sore/burning throat, and numbness of the tongue and gums shortly after initiating intravenous Vancomycin therapy. The symptoms were consistent with an allergic-type reaction. The medication was discontinued, and symptoms gradually resolved.
Subsequently, the patient reported taking Atorvastatin (Lipitor), presumably for hypercholesterolemia. After several days, they developed acute-onset, intermittent epigastric and flank pain radiating to the back. The abdominal pain persisted for a week, with episodes severe enough to cause sleep disturbance. The patient also experienced intermittent urinary urgency without dysuria or fever and had recently recovered from a urinary tract infection (UTI), which was considered unrelated due to symptom variation.
Upon self-discontinuation of Atorvastatin, the patient reported immediate relief from both gastrointestinal discomfort and urinary urgency. Additionally, they noted improvement in energy levels, which had been attributed to stress but were retrospectively linked to the medication.
"""

val result = ner_pipeline.fullAnnotate(text)
```
</div>

## Results

```bash

# NER Result
|    | ner_chunk                                           |   begin |   end | pred_label     | ner_source         |   confidence |
|---:|:----------------------------------------------------|--------:|------:|:---------------|:-------------------|-------------:|
|  0 | 75                                                  |       3 |     4 | AGE            | entity_age         |     0.5      |
|  1 | female                                              |      15 |    20 | GENDER         | ner_jsl_chunk      |     0.9998   |
|  2 | itching                                             |      51 |    57 | ADE            | ner_ade_chunk      |     0.7943   |
|  3 | sore/burning throat                                 |      60 |    78 | ADE            | ner_ade_chunk      |     0.92495  |
|  4 | numbness of the tongue and gums                     |      85 |   115 | ADE            | ner_ade_chunk      |     0.818517 |
|  5 | intravenous                                         |     142 |   152 | ROUTE          | ner_posology_chunk |     0.9994   |
|  6 | Vancomycin                                          |     154 |   163 | DRUG           | ner_posology_chunk |     0.9997   |
|  7 | Atorvastatin                                        |     344 |   355 | DRUG           | ner_posology_chunk |     0.9987   |
|  8 | Lipitor                                             |     358 |   364 | DRUG_BRANDNAME | ner_jsl_chunk      |     0.9985   |
|  9 | After several days                                  |     405 |   422 | RELATIVEDATE   | ner_jsl_chunk      |     0.5753   |
| 10 | acute-onset, intermittent epigastric and flank pain |     440 |   490 | ADE            | ner_ade_chunk      |     0.742243 |
| 11 | abdominal pain                                      |     519 |   532 | ADE            | ner_ade_chunk      |     0.71365  |
| 12 | for a week                                          |     544 |   553 | DURATION       | ner_jsl_chunk      |     0.724033 |
| 13 | sleep disturbance                                   |     593 |   609 | ADE            | ner_ade_chunk      |     0.67975  |
| 14 | Atorvastatin                                        |     847 |   858 | DRUG           | ner_posology_chunk |     0.9999   |
| 15 | gastrointestinal discomfort                         |     909 |   935 | ADE            | ner_ade_chunk      |     0.90105  |
| 16 | urinary urgency                                     |     941 |   955 | ADE            | ner_ade_chunk      |     0.91545  |



# Age Group Classifier
|    | sentence                                                                                                                                                                       | pred_chunk | begin | end |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|:------|:----|
|  0 | 'A 75-year-old female presented with complaints of itching, sore/burning throat, and numbness of the tongue and gums shortly after initiating intravenous Vancomycin therapy.' | 'Adult'    | 0     | 171 |
# MedDRA Codes

|    | ner_chunk                                           |begin |  end | entity                       |meddra_llt_code | resolution                  | all_k_results                  | all_k_resolutions                   |
|---:|:----------------------------------------------------|-----:|-----:|:-----------------------------|---------------:|:----------------------------|:-------------------------------|:------------------------------------|
|  0 | itching                                             |   51 |   57 | ADE                          |       10023084 | itching                     | 10023084:::10062437:::10023082 | itching:::generalized itching:::... |
|  1 | sore/burning throat                                 |   60 |   78 | ADE                          |       10041367 | sore throat                 | 10041367:::10086056:::10043524 | sore throat:::scratchy throat:::... |
|  2 | numbness of the tongue and gums                     |   85 |  115 | ADE                          |       10029852 | numbness of tongue          | 10029852:::10043989:::10049387 | numbness of tongue:::tongue tip ... |
|  3 | allergic-type reaction                              |  211 |  232 | SYMPTOM                      |       10001718 | allergic reaction           | 10001718:::10001729:::10001717 | allergic reaction:::allergic ski... |
|  4 | hypercholesterolemia                                |  383 |  402 | HYPERLIPIDEMIA               |       10020604 | hypercholesterolemia        | 10020604:::10020603:::10020602 | hypercholesterolemia:::hyperchol... |
|  5 | acute-onset, intermittent epigastric and flank pain |  440 |  490 | ADE                          |       10066562 | chronic epigastric pain     | 10066562:::10015026:::10000058 | chronic epigastric pain:::epigas... |
|  6 | back                                                |  509 |  512 | EXTERNAL_BODY_PART_OR_REGION |       10018203 | gerd                        | 10018203:::10037832:::10014544 | gerd:::rale:::emg:::bun:::bph:::... |
|  7 | abdominal pain                                      |  519 |  532 | ADE                          |       10000081 | abdominal pain              | 10000081:::10046272:::10087945 | abdominal pain:::upper abdominal... |
|  8 | sleep disturbance                                   |  593 |  609 | ADE                          |       10040995 | sleep disturbance           | 10040995:::10041005:::10080881 | sleep disturbance:::sleep proble... |
|  9 | urinary urgency                                     |  654 |  668 | DISEASE_SYNDROME_DISORDER    |       10046593 | urinary urgency             | 10046593:::10046604:::10046497 | urinary urgency:::urination urge... |
| 10 | dysuria                                             |  678 |  684 | SYMPTOM                      |       10013990 | dysuria                     | 10013990:::10037195:::10054791 | dysuria:::psychogenic dysuria:::... |
| 11 | fever                                               |  689 |  693 | VS_FINDING                   |       10016558 | fever                       | 10016558:::10058698:::10073718 | fever:::intermittent fever:::fev... |
| 12 | urinary tract infection                             |  729 |  751 | DISEASE_SYNDROME_DISORDER    |       10046571 | urinary tract infection     | 10046571:::10046544:::10080628 | urinary tract infection:::urinar... |
| 13 | UTI                                                 |  754 |  756 | DISEASE_SYNDROME_DISORDER    |       10046848 | uti                         | 10046848:::10023111:::10024411 | uti:::ivu:::lh:::als:::uibc:::ih... |
| 14 | gastrointestinal discomfort                         |  909 |  935 | ADE                          |       10054209 | gastrointestinal discomfort | 10054209:::10017999:::10030973 | gastrointestinal discomfort:::ga... |
| 15 | urinary urgency                                     |  941 |  955 | ADE                          |       10046593 | urinary urgency             | 10046593:::10046604:::10046497 | urinary urgency:::urination urge... |
| 16 | stress                                              | 1042 | 1047 | SYMPTOM                      |       10042209 | stress                      | 10042209:::10042218:::10043889 | stress:::stress symptoms:::tired... |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_ade_age_meddra_test_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- RegexTokenizer
- ContextualParserModel
- DocumentFiltererByNER
- LargeFewShotClassifierModel
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
- MedicalNerModel
- NerConverterInternalModel
- NerConverterInternalModel
- ChunkMergeModel
- ChunkFilterer
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
- ChunkMergeModel