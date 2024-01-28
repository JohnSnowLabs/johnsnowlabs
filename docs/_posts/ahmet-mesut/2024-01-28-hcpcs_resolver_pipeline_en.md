---
layout: model
title: Pipeline for HCPCS Codes
author: John Snow Labs
name: hcpcs_resolver_pipeline
date: 2024-01-28
tags: [licensed, en, clinical, hcpcs, pipeline, resolver]
task: [Entity Resolution, Pipeline Healthcare]
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

This pipeline extracts `Procedure` and `TREATMENT` entities and maps them to their corresponding [Healthcare Common Procedure Coding System (HCPCS)](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/current/HCPCS/index.html)
codes using 'sbiobert_base_cased_mli' sentence embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hcpcs_resolver_pipeline_en_5.2.1_3.2_1706400927432.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hcpcs_resolver_pipeline_en_5.2.1_3.2_1706400927432.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

hcpcs_pipeline = PretrainedPipeline("hcpcs_resolver_pipeline", "en", "clinical/models")

text = """Mary received a mechanical prosthetic heart valve in June 2020, and the results were successful. Diabetes screening test performed, revealing abnormal result. She  uses infusion pump for diabetes and a CPAP machine for sleep apnea. In 2021, She received a breast prosthesis implant. Mary also received home healthcare services for post-surgery."""

result = hcpcs_pipeline.fullAnnotate(text)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val hcpcs_pipeline = PretrainedPipeline("hcpcs_resolver_pipeline", "en", "clinical/models")

val text = """Mary received a mechanical prosthetic heart valve in June 2020, and the results were successful. Diabetes screening test performed, revealing abnormal result. She  uses infusion pump for diabetes and a CPAP machine for sleep apnea. In 2021, She received a breast prosthesis implant. Mary also received home healthcare services for post-surgery."""

val result = hcpcs_pipeline.fullAnnotate(text)

```
</div>

## Results

```bash

+-----------------------------------+-----+---+-----+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+
|                             chunks|begin|end| code|                                                        all_codes|                                                      resolutions|                                                    all_distances|
+-----------------------------------+-----+---+-----+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+
|a mechanical prosthetic heart valve|   14| 48|G0043|[G0043, C1824, L8698, Q0508, C1764, C1883,    AV, V5095, L8699...|[Patients with mechanical prosthetic heart valve, Generator, c...|[0.0384, 0.2283, 0.2375, 0.2393, 0.2434, 0.2587, 0.2515, 0.262...|
|                      infusion pump|  169|181|C1772|[C1772,    JA, C1754, A4220,    SH, B9004, S9007, B9002, C1887...|[Infusion pump, programmable (implantable), Administered intra...|[0.1408, 0.1777, 0.1990, 0.2107, 0.2175, 0.2166, 0.2214, 0.221...|
|                     a CPAP machine|  200|213|E0601|[E0601, Q4246, E0570, E0860, E0942, E0457, C1880, L0972, L0970...|[Continuous positive airway pressure (cpap) device, Coretext o...|[0.1952, 0.2380, 0.2519, 0.2630, 0.2775, 0.2791, 0.2832, 0.304...|
|        a breast prosthesis implant|  254|280|C1789|[C1789, L8600, L8010, L8020, L8031, L8039, A4282, A4281, G9829...|[Prosthesis, breast (implantable), Implantable breast prosthes...|[0.0798, 0.1202, 0.1495, 0.1604, 0.1704, 0.1712, 0.1984, 0.226...|
+-----------------------------------+-----+---+-----+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hcpcs_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.2 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
