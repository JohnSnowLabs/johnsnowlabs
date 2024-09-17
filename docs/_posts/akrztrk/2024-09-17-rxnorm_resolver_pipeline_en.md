---
layout: model
title: Pipeline to Resolve RxNorm Codes
author: John Snow Labs
name: rxnorm_resolver_pipeline
date: 2024-09-17
tags: [licensed, en, resolver, rxnorm, clinical, pipeline]
task: Pipeline Healthcare
language: en
edition: Healthcare NLP 5.4.1
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxnorm_resolver_pipeline_en_5.4.1_3.2_1726601707066.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxnorm_resolver_pipeline_en_5.4.1_3.2_1726601707066.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
+-----------------+-----+---+---------+-----------+--------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
|            chunk|begin|end|ner_label|rxnorm_code|                                                       resolved_text|                                                             all_codes|                                                       all_resolutions|                                                      all_k_aux_labels|                                                         all_distances|
+-----------------+-----+---+---------+-----------+--------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
|Albuterol inhaler|   27| 43|     DRUG|     745678|      albuterol Metered Dose Inhaler[albuterol Metered Dose Inhaler]|745678:::2108226:::1154602:::2108233:::2108228:::435:::746762:::210...|albuterol Metered Dose Inhaler[albuterol Metered Dose Inhaler]:::al...|Clinical Drug Form:::Clinical Drug Form:::Clinical Dose Group:::Cli...|4.9847:::5.1028:::5.4746:::5.7809:::6.2859:::6.3948:::6.4499:::6.48...|
|     Avandia 4 mg|  112|123|     DRUG|     261242|                            rosiglitazone 4 MG Oral Tablet [Avandia]|261242:::810073:::153845:::1094008:::2123140:::1369735:::862026:::1...|rosiglitazone 4 MG Oral Tablet [Avandia]:::fesoterodine fumarate 4 ...|Branded Drug:::Branded Drug Comp:::Branded Drug:::Branded Drug Comp...|0.0000:::4.7482:::5.0125:::5.2516:::5.4650:::5.4880:::5.4964:::5.56...|
|    Coumadin 5 mg|  136|148|     DRUG|     855333|                                     warfarin sodium 5 MG [Coumadin]|855333:::438740:::153692:::352120:::1036890:::104363:::201269:::351...|warfarin sodium 5 MG [Coumadin]:::coumarin 5 MG[coumarin 5 MG]:::ox...|Branded Drug Comp:::Clinical Drug Comp:::Branded Drug:::Branded Dru...|0.0000:::4.0885:::5.3065:::5.5132:::5.5336:::5.7412:::5.8485:::6.03...|
| Metformin 100 mg|  162|177|     DRUG|     861024|metformin hydrochloride 100 MG/ML[metformin hydrochloride 100 MG/ML]|861024:::334738:::332848:::861026:::333262:::439563:::103910:::4505...|metformin hydrochloride 100 MG/ML[metformin hydrochloride 100 MG/ML...|Clinical Drug Comp:::Clinical Drug Comp:::Clinical Drug Comp:::Bran...|6.3835:::6.5293:::6.5728:::6.9061:::6.9297:::6.9512:::6.9935:::7.09...|
| Lisinopril 10 mg|  216|231|     DRUG|     316151|                                  lisinopril 10 MG[lisinopril 10 MG]|316151:::567576:::565846:::393444:::563611:::314076:::328290:::8571...|lisinopril 10 MG[lisinopril 10 MG]:::lisinopril 10 MG [Prinivil][li...|Clinical Drug Comp:::Branded Drug Comp:::Branded Drug Comp:::Clinic...|0.0000:::3.6543:::4.2783:::4.2805:::4.6016:::4.8302:::5.1265:::5.54...|
+-----------------+-----+---+---------+-----------+--------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|rxnorm_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.4.1+|
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