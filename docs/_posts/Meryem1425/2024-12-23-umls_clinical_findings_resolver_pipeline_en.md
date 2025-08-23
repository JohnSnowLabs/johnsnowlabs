---
layout: model
title: Clinical Findings to UMLS Code Pipeline
author: John Snow Labs
name: umls_clinical_findings_resolver_pipeline
date: 2024-12-23
tags: [licensed, en, resolver, clinical, umls, pipeline]
task: [Pipeline Healthcare, Chunk Mapping]
language: en
edition: Healthcare NLP 5.5.1
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline maps entities (Clinical Findings) with their corresponding UMLS CUI codes. You’ll just feed your text and it will return the corresponding UMLS codes.

## Predicted Entities

`PROBLEM`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_clinical_findings_resolver_pipeline_en_5.5.1_3.2_1734986382021.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_clinical_findings_resolver_pipeline_en_5.5.1_3.2_1734986382021.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

resolver_pipeline = PretrainedPipeline("umls_clinical_findings_resolver_pipeline", "en", "clinical/models")

result = resolver_pipeline.annotate("""HTG-induced pancreatitis associated with an acute hepatitis, and obesity""")

```

{:.jsl-block}
```python

resolver_pipeline = nlp.PretrainedPipeline("umls_clinical_findings_resolver_pipeline", "en", "clinical/models")

result = resolver_pipeline.annotate("""HTG-induced pancreatitis associated with an acute hepatitis, and obesity""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val resolver_pipeline = PretrainedPipeline("umls_clinical_findings_resolver_pipeline", "en", "clinical/models")

val result = resolver_pipeline.annotate("""HTG-induced pancreatitis associated with an acute hepatitis, and obesity""")

```
</div>

## Results

```bash

+------------------------+---------+---------+
|chunk                   |ner_label|umls_code|
+------------------------+---------+---------+
|HTG-induced pancreatitis|PROBLEM  |C3808945 |
|an acute hepatitis      |PROBLEM  |C4750596 |
|obesity                 |PROBLEM  |C4759928 |
+------------------------+---------+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_clinical_findings_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|4.4 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- ChunkMapperModel
- ChunkMapperFilterer
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
- ResolverMerger
