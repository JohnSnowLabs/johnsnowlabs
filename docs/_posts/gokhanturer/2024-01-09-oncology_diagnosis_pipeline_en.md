---
layout: model
title: Oncology Pipeline for Diagnosis Entities
author: John Snow Labs
name: oncology_diagnosis_pipeline
date: 2024-01-09
tags: [licensed, en, oncology, pipeline, ner, assertion, re]
task: [Named Entity Recognition, Pipeline Healthcare, Assertion Status, Relation Extraction]
language: en
edition: Healthcare NLP 5.2.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline includes Named-Entity Recognition, Assertion Status, Relation Extraction and Entity Resolution models to extract information from oncology texts. This pipeline focuses on entities related to oncological diagnosis.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/oncology_diagnosis_pipeline_en_5.2.0_3.2_1704824993066.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/oncology_diagnosis_pipeline_en_5.2.0_3.2_1704824993066.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("oncology_diagnosis_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""Two years ago, the patient presented with a 4-cm tumor in her left breast. She was diagnosed with ductal carcinoma.
According to her last CT, she has no lung metastases.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("oncology_diagnosis_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""Two years ago, the patient presented with a 4-cm tumor in her left breast. She was diagnosed with ductal carcinoma.
According to her last CT, she has no lung metastases.""")

```
</div>

## Results

```bash
# ner_oncology_chunk
+----------+-----+---+-----------------+
|chunk     |begin|end|ner_label        |
+----------+-----+---+-----------------+
|4-cm      |44   |47 |Tumor_Size       |
|tumor     |49   |53 |Tumor_Finding    |
|left      |62   |65 |Direction        |
|breast    |67   |72 |Site_Breast      |
|ductal    |98   |103|Histological_Type|
|carcinoma |105  |113|Cancer_Dx        |
|lung      |153  |156|Site_Lung        |
|metastases|158  |167|Metastasis       |
+----------+-----+---+-----------------+

# ner_oncology_diagnosis
+----------+-----+---+-----------------+
|chunk     |begin|end|ner_label        |
+----------+-----+---+-----------------+
|4-cm      |44   |47 |Tumor_Size       |
|tumor     |49   |53 |Tumor_Finding    |
|ductal    |98   |103|Histological_Type|
|carcinoma |105  |113|Cancer_Dx        |
|metastases|158  |167|Metastasis       |
+----------+-----+---+-----------------+

# ner_oncology_tnm_chunk
+----------+-----+---+-----------------+
|chunk     |begin|end|ner_label        |
+----------+-----+---+-----------------+
|4-cm      |44   |47 |Tumor_Description|
|tumor     |49   |53 |Tumor            |
|ductal    |98   |103|Tumor_Description|
|carcinoma |105  |113|Cancer_Dx        |
|metastases|158  |167|Metastasis       |
+----------+-----+---+-----------------+

# assertion_oncology_wip
+----------+-----+---+-----------------+---------+
|chunk     |begin|end|ner_label        |assertion|
+----------+-----+---+-----------------+---------+
|tumor     |49   |53 |Tumor_Finding    |Present  |
|ductal    |98   |103|Histological_Type|Present  |
|carcinoma |105  |113|Cancer_Dx        |Present  |
|metastases|158  |167|Metastasis       |Absent   |
+----------+-----+---+-----------------+---------+

# assertion_oncology_problem_wip
+----------+-----+---+-----------------+----------------------+
|chunk     |begin|end|ner_label        |assertion             |
+----------+-----+---+-----------------+----------------------+
|tumor     |49   |53 |Tumor_Finding    |Medical_History       |
|ductal    |98   |103|Histological_Type|Medical_History       |
|carcinoma |105  |113|Cancer_Dx        |Medical_History       |
|metastases|158  |167|Metastasis       |Hypothetical_Or_Absent|
+----------+-----+---+-----------------+----------------------+

# re_oncology_wip
| chunk1 | entity1 |        chunk2 |    entity2 |      relation |               |
|-------:|--------:|--------------:|-----------:|--------------:|---------------|
|    0   |    4-cm |    Tumor_Size |      tumor | Tumor_Finding | is_related_to |
|    1   |    4-cm |    Tumor_Size |  carcinoma |     Cancer_Dx |             O |
|    2   |   tumor | Tumor_Finding |     breast |   Site_Breast | is_related_to |
|    3   |  breast |   Site_Breast |  carcinoma |     Cancer_Dx |             O |
|    4   |    lung |     Site_Lung | metastases |    Metastasis | is_related_to |

# re_oncology_granular_wip
|   | chunk1 |       entity1 |     chunk2 |       entity2 |       relation |
|--:|-------:|--------------:|-----------:|--------------:|---------------:|
| 0 |   4-cm |    Tumor_Size |      tumor | Tumor_Finding |     is_size_of |
| 1 |   4-cm |    Tumor_Size |  carcinoma |     Cancer_Dx |              O |
| 2 |  tumor | Tumor_Finding |     breast |   Site_Breast | is_location_of |
| 3 | breast |   Site_Breast |  carcinoma |     Cancer_Dx |              O |
| 4 |   lung |     Site_Lung | metastases |    Metastasis | is_location_of |

# re_oncology_size_wip
|   | chunk1 |    entity1 |    chunk2 |       entity2 |   relation |
|--:|-------:|-----------:|----------:|--------------:|-----------:|
| 0 |   4-cm | Tumor_Size |     tumor | Tumor_Finding | is_size_of |
| 1 |   4-cm | Tumor_Size | carcinoma |     Cancer_Dx |          O |

# ICD-O resolver
+----------+-----+---+-----------------+------+-----------------+
|chunk     |begin|end|ner_label        |code  |normalized_term  |
+----------+-----+---+-----------------+------+-----------------+
|tumor     |49   |53 |Tumor_Finding    |8000/1|tumor            |
|breast    |67   |72 |Site_Breast      |C50   |breast           |
|ductal    |98   |103|Histological_Type|8500/2|dcis             |
|carcinoma |105  |113|Cancer_Dx        |8010/3|carcinoma        |
|lung      |153  |156|Site_Lung        |C34.9 |lung             |
|metastases|158  |167|Metastasis       |8000/6|tumor, metastatic|
+----------+-----+---+-----------------+------+-----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|oncology_diagnosis_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.4 GB|

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
- ChunkMergeModel
- ChunkMergeModel
- AssertionDLModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel
- RelationExtractionModel
- RelationExtractionModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
