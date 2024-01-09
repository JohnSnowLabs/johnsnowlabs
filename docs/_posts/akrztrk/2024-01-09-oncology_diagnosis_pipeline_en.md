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
spark_version: 3.4
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/oncology_diagnosis_pipeline_en_5.2.0_3.4_1704825991977.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/oncology_diagnosis_pipeline_en_5.2.0_3.4_1704825991977.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
|    | chunks     |   begin |   end | entities          |
|---:|:-----------|--------:|------:|:------------------|
|  0 | 4-cm       |      44 |    47 | Tumor_Size        |
|  1 | tumor      |      49 |    53 | Tumor_Finding     |
|  2 | left       |      62 |    65 | Direction         |
|  3 | breast     |      67 |    72 | Site_Breast       |
|  4 | ductal     |      98 |   103 | Histological_Type |
|  5 | carcinoma  |     105 |   113 | Cancer_Dx         |
|  6 | lung       |     153 |   156 | Site_Lung         |
|  7 | metastases |     158 |   167 | Metastasis        |
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