---
layout: model
title: Explain Clinical Document Generic
author: John Snow Labs
name: explain_clinical_doc_generic
date: 2024-04-27
tags: [licensed, clinical, en, doc, ner, pipeline, assertion, relation_extraction, generic]
task: [Pipeline Healthcare, Named Entity Recognition, Assertion Status, Relation Extraction]
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
                      - extract clinical/medical entities
                      - assign assertion status to the extracted entities
                      - establish relations between the extracted entities
from clinical texts. In this pipeline, 4 NER models, one assertion model, and one relation extraction model were used to achieve those tasks. Here are the NER, assertion, and relation extraction labels this pipeline can extract.
                      - Clinical Entity Labels: `PROBLEM`, `TEST`, `TREATMENT`
                      - Assertion Status Labels: `Present`, `Absent`, `Possible`, `Planned`, `Past`, `Family`, `Hypotetical`, `SomeoneElse`
                      - Relation Extraction Labels: `TrAP`, `TeRP`, `TrIP`, `TrWP`, `TrCP`, `TrAP`, `TrNAP`, `TeCP`, `PIP`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_generic_en_5.2.1_3.0_1714248373884.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_generic_en_5.2.1_3.0_1714248373884.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_generic", "en", "clinical/models")

result = ner_pipeline.annotate("""Patient with severe fever and sore throat. He shows no stomach pain. He maintained on the epidural and PCA for pain control.
After CT, lung tumor located at the right lower lobe. Father with Alzheimer.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_generic", "en", "clinical/models")

val result = ner_pipeline.annotate("""Patient with severe fever and sore throat. He shows no stomach pain. He maintained on the epidural and PCA for pain control.
After CT, lung tumor located at the right lower lobe. Father with Alzheimer.""")

```
</div>

## Results

```bash

# NER and Assertion Result

+------------+---------+------------+
|merged_chunk|entities |assertion   |
+------------+---------+------------+
|severe fever|PROBLEM  |Present     |
|sore throat |PROBLEM  |Present     |
|stomach pain|PROBLEM  |Absent      |
|the epidural|TREATMENT|Present     |
|PCA         |TREATMENT|Past        |
|pain        |PROBLEM  |Hypothetical|
|CT          |PROBLEM  |Past        |
|lung tumor  |PROBLEM  |Present     |
|Alzheimer   |PROBLEM  |Family      |
+------------+---------+------------+

# Relation Extraction Result

+--------+-------------+-----------+------------+---------+-------------+-----------+-----------+-------+--------+----------+
|sentence|entity1_begin|entity1_end|      chunk1|  entity1|entity2_begin|entity2_end|     chunk2|entity2|relation|confidence|
+--------+-------------+-----------+------------+---------+-------------+-----------+-----------+-------+--------+----------+
|       0|           13|         24|severe fever|  PROBLEM|           30|         40|sore throat|PROBLEM|     PIP| 0.9999982|
|       2|           86|         97|the epidural|TREATMENT|          111|        114|       pain|PROBLEM|    TrAP|0.81723267|
|       2|          103|        105|         PCA|TREATMENT|          111|        114|       pain|PROBLEM|    TrAP|0.99933213|
|       3|          131|        132|          CT|  PROBLEM|          135|        144| lung tumor|PROBLEM|     PIP|  0.999998|
+--------+-------------+-----------+------------+---------+-------------+-----------+-----------+-------+--------+----------+

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
