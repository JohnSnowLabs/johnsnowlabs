---
layout: model
title: Explain Clinical Document Generic
author: John Snow Labs
name: explain_clinical_doc_generic
date: 2024-01-17
tags: [licensed, clinical, en, doc, pipeline, ner, assertion, relation_extraction, generic]
task: [Named Entity Recognition, Assertion Status, Relation Extraction, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to:

    - extract all clinical/medical entities from text,

    - assign assertion status to the extracted entities,

    - establish relations between the extracted entities.

4 NER models, one assertion model and one relation extraction model were used in order to achieve those tasks.

Clinical Entity Labels: `PROBLEM`, `TEST`, `TREATMENT`

Assertion Status Labels: `Present`, `Absent`, `Possible`, `Planned`, `Past`, `Family`, `Hypotetical`, `SomeoneElse`

Relation Extraction Labels: `TrAP`, `TeRP`, `TrIP`, `TrWP`, `TrCP`, `TrAP`, `TrNAP`, `TeCP`, `PIP`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_generic_en_5.2.1_3.2_1705509431473.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_generic_en_5.2.1_3.2_1705509431473.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_generic", "en", "clinical/models")

result = ner_pipeline.annotate("""Patient with severe fever and sore throat.
He shows no stomach pain. He maintained on an epidural and PCA for pain control.
After CT, lung tumor located at the right lower lobe. Father with Alzheimer.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_generic", "en", "clinical/models")

val result = ner_pipeline.annotate("""Patient with severe fever and sore throat.
He shows no stomach pain. He maintained on an epidural and PCA for pain control.
After CT, lung tumor located at the right lower lobe. Father with Alzheimer.""")

```
</div>

## Results

```bash
|    | chunks       | entities   | assertion    |
|---:|:-------------|:-----------|:-------------|
|  0 | severe fever | PROBLEM    | Present      |
|  1 | sore throat  | PROBLEM    | Present      |
|  2 | stomach pain | PROBLEM    | Absent       |
|  3 | an epidural  | TREATMENT  | Past         |
|  4 | PCA          | TREATMENT  | Past         |
|  5 | pain         | PROBLEM    | Hypothetical |
|  6 | CT           | TEST       | Past         |
|  7 | lung tumor   | PROBLEM    | Present      |
|  8 | Alzheimer    | PROBLEM    | Family       |
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