---
layout: model
title: Explain Document Oncology
author: John Snow Labs
name: explain_document_oncology
date: 2024-01-16
tags: [licensed, en, oncology, pipeline, ner, assertion, relation_extraction]
task: [Named Entity Recognition, Assertion Status, Relation Extraction, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to

- extract all clinical/medical entities from text,

- assign assertion status to the extracted entities,

- establish relations between the extracted entities.

7 NER models, one assertion model and two relation extraction model were used in order to achieve those tasks.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_document_oncology_en_5.2.0_3.0_1705423109442.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_document_oncology_en_5.2.0_3.0_1705423109442.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_document_oncology", "en", "clinical/models")

result = ner_pipeline.annotate("""The Patient underwent a computed tomography (CT) scan of the abdomen and pelvis, which showed a complex ovarian mass. A Pap smear performed one month later was positive for atypical glandular cells suspicious for adenocarcinoma. The pathologic specimen showed extension of the tumor throughout the fallopian tubes, appendix, omentum, and 5 out of 5 enlarged lymph nodes. The final pathologic diagnosis of the tumor was stage IIIC papillary serous ovarian adenocarcinoma. Two months later, the patient was diagnosed with lung metastases.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_document_oncology", "en", "clinical/models")

val result = ner_pipeline.annotate("""The Patient underwent a computed tomography (CT) scan of the abdomen and pelvis, which showed a complex ovarian mass. A Pap smear performed one month later was positive for atypical glandular cells suspicious for adenocarcinoma. The pathologic specimen showed extension of the tumor throughout the fallopian tubes, appendix, omentum, and 5 out of 5 enlarged lymph nodes. The final pathologic diagnosis of the tumor was stage IIIC papillary serous ovarian adenocarcinoma. Two months later, the patient was diagnosed with lung metastases.""")

```
</div>

## Results

```bash


|    | sentence_id | chunks                                  | begin | end | entities             |
|----|-------------|-----------------------------------------|-------|-----|----------------------|
| 0  | 0           | computed tomography                     | 24    | 42  | Imaging_Test         |
| 1  | 0           | CT                                      | 45    | 46  | Imaging_Test         |
| 2  | 0           | abdomen                                 | 61    | 67  | Site_Other_Body_Part |
| 3  | 0           | pelvis                                  | 73    | 78  | Site_Other_Body_Part |
| 4  | 0           | ovarian                                 | 104   | 110 | Site_Other_Body_Part |
| 5  | 0           | mass                                    | 112   | 115 | Tumor_Finding        |
| 6  | 1           | Pap smear                               | 120   | 128 | Pathology_Test       |
| 7  | 1           | one month later                         | 140   | 154 | Relative_Date        |
| 8  | 1           | atypical glandular cells                | 173   | 196 | Pathology_Result     |
| 9  | 1           | adenocarcinoma                          | 213   | 226 | Cancer_Dx            |
| 10 | 2           | pathologic specimen                     | 233   | 251 | Pathology_Test       |
| 11 | 2           | extension                               | 260   | 268 | Invasion             |
| 12 | 2           | tumor                                   | 277   | 281 | Tumor_Finding        |
| 13 | 2           | fallopian tubes                         | 298   | 312 | Site_Other_Body_Part |
| 14 | 2           | appendix                                | 315   | 322 | Site_Other_Body_Part |
| 15 | 2           | omentum                                 | 325   | 331 | Site_Other_Body_Part |
| 16 | 2           | enlarged                                | 349   | 356 | Lymph_Node_Modifier  |
| 17 | 2           | lymph nodes                             | 358   | 368 | Site_Lymph_Node      |
| 18 | 3           | tumor                                   | 409   | 413 | Tumor_Finding        |
| 19 | 3           | stage IIIC                              | 419   | 428 | Staging              |
| 20 | 3           | papillary serous ovarian adenocarcinoma | 430   | 468 | Oncological          |
| 21 | 4           | Two months later                        | 471   | 486 | Relative_Date        |
| 22 | 4           | lung metastases                         | 520   | 534 | Oncological          |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_document_oncology|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.9 GB|

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
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- ChunkMergeModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel
- RelationExtractionModel
- AnnotationMerger