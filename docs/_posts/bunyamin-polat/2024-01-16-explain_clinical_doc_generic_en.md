---
layout: model
title: Explain Clinical Document Generic
author: John Snow Labs
name: explain_clinical_doc_generic
date: 2024-01-16
tags: [licensed, clinical, en, doc, pipeline, ner, assertion, relation_extraction, generic]
task: [Named Entity Recognition, Assertion Status, Relation Extraction, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to:

    - extract all clinical/medical entities

    - assign assertion status to the extracted entities

    - establish relations between the extracted entities

from clinical texts. In this pipeline, 4 NER models, one assertion model, and one relation extraction model were used to achieve those tasks. Here are the NER, assertion, and relation extraction labels this pipeline can extract.

- Clinical Entity Labels: `PROBLEM`, `TEST`, `TREATMENT` 

- Assertion Status Labels: `Present`, `Absent`, `Possible`, `Planned`, `Past`, `Family`, `Hypotetical`, `SomeoneElse`

- Relation Extraction Labels: `TrAP`, `TeRP`, `TrIP`, `TrWP`, `TrCP`, `TrAP`, `TrNAP`, `TeCP`, `PIP`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_generic_en_5.2.1_3.0_1705427189860.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_generic_en_5.2.1_3.0_1705427189860.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_generic", "en", "clinical/models")

result = ner_pipeline.annotate("""
GENERAL: He is an elderly gentleman in no acute distress. He is sitting up in bed eating his breakfast. He is alert and oriented and answering questions appropriately.
HEENT: Sclerae showed mild arcus senilis in the right. Left was clear. Pupils are equally round and reactive to light. Extraocular movements are intact. Oropharynx is clear.
NECK: Supple. Trachea is midline. No jugular venous pressure distention is noted. No adenopathy in the cervical, supraclavicular, or axillary areas.
ABDOMEN: Soft and not tender. There may be some fullness in the left upper quadrant, although I do not appreciate a true spleen with inspiration.
EXTREMITIES: There is some edema, but no cyanosis and clubbing .
IMPRESSION: At this time is refractory anemia, which is transfusion dependent. He is on B12, iron, folic acid, and Procrit. There are no sign or symptom of blood loss and the previous esophagogastroduodenoscopy was negative. His creatinine was 1.
  My impression at this time is that he probably has an underlying myelodysplastic syndrome or bone marrow failure. His creatinine on this hospitalization was up slightly to 1.6 and this may contribute to his anemia.
  At this time, my recommendation for the patient is that he should undergo a bone marrow aspiration.
  I have discussed the procedure in detail which the patient. I have discussed the risks, benefits, and successes of that treatment and usefulness of the bone marrow and predicting his cause of refractory anemia and further therapeutic interventions, which might be beneficial to him.
  He is willing to proceed with the studies I have described to him. We will order an ultrasound of his abdomen because of the possible fullness of the spleen.
  As always, we greatly appreciate being able to participate in the care of your patient. We appreciate the consultation of the patient.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_generic", "en", "clinical/models")

val result = ner_pipeline.annotate("""
GENERAL: He is an elderly gentleman in no acute distress. He is sitting up in bed eating his breakfast. He is alert and oriented and answering questions appropriately.
HEENT: Sclerae showed mild arcus senilis in the right. Left was clear. Pupils are equally round and reactive to light. Extraocular movements are intact. Oropharynx is clear.
NECK: Supple. Trachea is midline. No jugular venous pressure distention is noted. No adenopathy in the cervical, supraclavicular, or axillary areas.
ABDOMEN: Soft and not tender. There may be some fullness in the left upper quadrant, although I do not appreciate a true spleen with inspiration.
EXTREMITIES: There is some edema, but no clubbing.
IMPRESSION: At this time is refractory anemia, which is transfusion dependent. He is on B12, iron, folic acid, and Procrit. There are no sign or symptom of blood loss and the previous esophagogastroduodenoscopy was negative. His creatinine was 1.
  My impression at this time is that he probably has an underlying myelodysplastic syndrome or bone marrow failure. His creatinine on this hospitalization was up slightly to 1.6 and this may contribute to his anemia.
  At this time, my recommendation for the patient is that he should undergo a bone marrow aspiration.
  I have discussed the procedure in detail which the patient. I have discussed the risks, benefits, and successes of that treatment and usefulness of the bone marrow and predicting his cause of refractory anemia and further therapeutic interventions, which might be beneficial to him.
  He is willing to proceed with the studies I have described to him. We will order an ultrasound of his abdomen because of the possible fullness of the spleen.
  As always, we greatly appreciate being able to participate in the care of your patient. We appreciate the consultation of the patient.
""")

```
</div>

## Results

```bash
# NER and Assertion Result
|    | chunks                                   | entities   | assertion    |
|---:|:-----------------------------------------|:-----------|:-------------|
|  0 | acute distress                           | PROBLEM    | Absent       |
|  1 | mild arcus senilis in the right          | PROBLEM    | Present      |
|  2 | jugular venous pressure distention       | PROBLEM    | Absent       |
|  3 | adenopathy                               | PROBLEM    | Absent       |
|  4 | tender                                   | PROBLEM    | Absent       |
|  5 | some fullness in the left upper quadrant | PROBLEM    | Possible     |
|  6 | some edema                               | PROBLEM    | Present      |
|  7 | clubbing                                 | PROBLEM    | Absent       |
|  8 | refractory anemia                        | PROBLEM    | Present      |
|  9 | transfusion                              | TREATMENT  | Present      |
| 10 | B12                                      | TREATMENT  | Planned      |
| 11 | iron                                     | TREATMENT  | Planned      |
| 12 | folic acid                               | TREATMENT  | Possible     |
| 13 | Procrit                                  | TREATMENT  | Planned      |
| 14 | blood loss                               | PROBLEM    | Absent       |
| 15 | the previous esophagogastroduodenoscopy  | TEST       | Past         |
| 16 | His creatinine                           | TEST       | Past         |
| 17 | an underlying myelodysplastic syndrome   | PROBLEM    | Possible     |
| 18 | bone marrow failure                      | PROBLEM    | Possible     |
| 19 | His creatinine                           | TEST       | Absent       |
| 20 | his anemia                               | PROBLEM    | Present      |
| 21 | a bone marrow aspiration                 | PROBLEM    | Hypothetical |
| 22 | the procedure                            | TREATMENT  | Hypothetical |
| 23 | usefulness of the bone marrow            | TEST       | Hypothetical |
| 24 | refractory anemia                        | PROBLEM    | Present      |
| 25 | therapeutic interventions                | TREATMENT  | Hypothetical |
| 26 | the studies                              | TEST       | Planned      |
| 27 | an ultrasound of his abdomen             | TEST       | Planned      |
| 28 | fullness of the spleen                   | PROBLEM    | Possible     |

# Relation Extraction Result
|    |   sentence |   entity1_begin |   entity1_end | chunk1                        | entity1   |   entity2_begin |   entity2_end | chunk2                                  | entity2   | relation   |   confidence |
|---:|-----------:|----------------:|--------------:|:------------------------------|:----------|----------------:|--------------:|:----------------------------------------|:----------|:-----------|-------------:|
|  1 |         14 |             731 |           747 | refractory anemia             | PROBLEM   |             759 |           769 | transfusion                             | TREATMENT | O          |     0.999496 |
|  2 |         15 |             791 |           793 | B12                           | TREATMENT |             802 |           811 | folic acid                              | TREATMENT | O          |     0.961106 |
|  3 |         15 |             791 |           793 | B12                           | TREATMENT |             818 |           824 | Procrit                                 | TREATMENT | O          |     1        |
|  4 |         15 |             796 |           799 | iron                          | TREATMENT |             802 |           811 | folic acid                              | TREATMENT | O          |     0.999855 |
|  5 |         15 |             796 |           799 | iron                          | TREATMENT |             818 |           824 | Procrit                                 | TREATMENT | O          |     0.999987 |
|  6 |         15 |             802 |           811 | folic acid                    | TREATMENT |             818 |           824 | Procrit                                 | TREATMENT | O          |     0.994239 |
|  7 |         16 |             859 |           868 | blood loss                    | PROBLEM   |             874 |           912 | the previous esophagogastroduodenoscopy | TEST      | TeRP       |     1        |
|  8 |         19 |            1066 |          1079 | His creatinine                | TEST      |            1155 |          1164 | his anemia                              | PROBLEM   | TeRP       |     1        |
|  9 |         22 |            1405 |          1433 | usefulness of the bone marrow | TEST      |            1463 |          1479 | refractory anemia                       | PROBLEM   | TeRP       |     1        |
| 10 |         24 |            1637 |          1664 | an ultrasound of his abdomen  | TEST      |            1690 |          1711 | fullness of the spleen                  | PROBLEM   | TeRP       |     1        |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_generic|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel
