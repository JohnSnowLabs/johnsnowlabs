---
layout: model
title: Pipeline to Resolve RxNorm Codes
author: John Snow Labs
name: rxnorm_resolver_pipeline
date: 2024-08-22
tags: [licensed, en, resolver, rxnorm, clinical, pipeline]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline maps entities with their corresponding RxNorm codes. You’ll just feed your text and it will return the corresponding RxNorm codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxnorm_resolver_pipeline_en_5.4.0_3.2_1724335914772.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxnorm_resolver_pipeline_en_5.4.0_3.2_1724335914772.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("rxnorm_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.fullAnnotate("""The patient was prescribed Albuterol inhaler when needed. She was seen by the endocrinology service, prescribed Avandia 4 mg at nights,
Coumadin 5 mg with meals, Metformin 100 mg two times a day, and a daily dose of Lisinopril 10 mg.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("rxnorm_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.fullAnnotate("""The patient was prescribed Albuterol inhaler when needed. She was seen by the endocrinology service, prescribed Avandia 4 mg at nights,
Coumadin 5 mg with meals, Metformin 100 mg two times a day, and a daily dose of Lisinopril 10 mg.""")

```
</div>

## Results

```bash


+-----------------+-----+---+---------+-----------+---------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
|            chunk|begin|end|ner_label|rxnorm_code|                                                        resolved_text|                                                             all_codes|                                                       all_resolutions|                                                      all_k_aux_labels|                                                         all_distances|
+-----------------+-----+---+---------+-----------+---------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
|Albuterol inhaler|   27| 43|     DRUG|     745678|      albuterol metered dose inhaler [albuterol metered dose inhaler]|745678:::2108226:::1154602:::2108233:::2108228:::1649559:::746762::...|albuterol metered dose inhaler [albuterol metered dose inhaler]:::a...|Clinical Drug Form:::Clinical Drug Form:::Clinical Dose Group:::Cli...|4.9847:::5.1028:::5.4746:::5.7809:::6.2859:::6.3948:::6.4499:::6.48...|
|     Avandia 4 mg|  112|123|     DRUG|     261242|                             rosiglitazone 4 MG Oral Tablet [Avandia]|261242:::810073:::153845:::1094008:::2123140:::1369735:::862026:::1...|rosiglitazone 4 MG Oral Tablet [Avandia]:::fesoterodine fumarate 4 ...|Branded Drug:::Branded Drug Comp:::Branded Drug:::Branded Drug Comp...|0.0000:::4.7482:::5.0125:::5.2516:::5.4650:::5.4880:::5.4964:::5.56...|
|    Coumadin 5 mg|  136|148|     DRUG|     855333|                                      warfarin sodium 5 MG [Coumadin]|855333:::438740:::153692:::352120:::1036890:::104363:::201269:::351...|warfarin sodium 5 MG [Coumadin]:::coumarin 5 mg [coumarin 5 mg]:::o...|Branded Drug Comp:::Clinical Drug Comp:::Branded Drug:::Branded Dru...|0.0000:::4.0885:::5.3065:::5.5132:::5.5336:::5.7412:::5.8485:::6.03...|
| Metformin 100 mg|  162|177|     DRUG|     861024|metformin hydrochloride 100 mg/ml [metformin hydrochloride 100 mg/ml]|861024:::334738:::332848:::861026:::333262:::429178:::103910:::4294...|metformin hydrochloride 100 mg/ml [metformin hydrochloride 100 mg/m...|Clinical Drug Comp:::Clinical Drug Comp:::Clinical Drug Comp:::Bran...|6.3835:::6.5293:::6.5728:::6.9061:::6.9297:::6.9512:::6.9935:::7.09...|
| Lisinopril 10 mg|  216|231|     DRUG|     314076|                                         lisinopril 10 MG Oral Tablet|314076:::567576:::565846:::389184:::563611:::328290:::857169:::3127...|lisinopril 10 MG Oral Tablet:::lisinopril 10 mg [prinivil] [lisinop...|Clinical Drug:::Branded Drug Comp:::Branded Drug Comp:::Clinical Dr...|0.0000:::3.6543:::4.2783:::4.2805:::4.6016:::5.1265:::5.5412:::5.72...|
+-----------------+-----+---+---------+-----------+---------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+



```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|rxnorm_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.3 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- TextMatcherInternalModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
