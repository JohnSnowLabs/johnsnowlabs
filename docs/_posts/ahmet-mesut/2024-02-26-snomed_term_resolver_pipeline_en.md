---
layout: model
title: Pipeline to Resolve SNOMED Term Codes
author: John Snow Labs
name: snomed_term_resolver_pipeline
date: 2024-02-26
tags: [licensed, en, resolver, snomed]
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

This pretrained resolver pipeline extracts SNOMED terms and map them to their corresponding SNOMED codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_term_resolver_pipeline_en_5.2.1_3.2_1708965219570.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_term_resolver_pipeline_en_5.2.1_3.2_1708965219570.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

resolver_pipeline = PretrainedPipeline("snomed_term_resolver_pipeline", "en", "clinical/models")

result = resolver_pipeline.annotate("""This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction. He was subsequently transferred to the CCU for close monitoring. He was hemodynamically stable at the time of admission to the CCU.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val resolver_pipeline = PretrainedPipeline("snomed_term_resolver_pipeline", "en", "clinical/models")

val result = resolver_pipeline.annotate("""This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction. He was subsequently transferred to the CCU for close monitoring. He was hemodynamically stable at the time of admission to the CCU.""")

```
</div>

## Results

```bash

+------------------------------------------------+-----+---+-----------+-----------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                                       ner_chunk|begin|end|     entity|snomed_code|                                                  resolution|                                                   all_codes|                                             all_resolutions|                                              all_aux_labels|
+------------------------------------------------+-----+---+-----------+-----------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                                    tobacco use,|   52| 63|snomed_term|  110483000|                                                 tobacco use|110483000:::39953003:::711013002:::57264008:::102407002::...|tobacco use:::tobacco - substance:::assessment of tobacco...|Clinical Finding:::Substance:::Procedure:::Organism:::Sub...|
|                                   hypertension,|   65| 77|snomed_term|   38341003|                                                hypertension|38341003:::270440008:::161501007:::73578008:::59621000:::...|hypertension:::hypertension monitored:::h/o: hypertension...|Clinical Finding:::Clinical Finding:::Context-dependent::...|
|                    chronic renal insufficiency,|   79|106|snomed_term|  723190009|                                 chronic renal insufficiency|723190009:::709044004:::42399005:::425369003:::90688005::...|chronic renal insufficiency:::chronic renal impairment:::...|Clinical Finding:::Clinical Finding:::Clinical Finding:::...|
|                                           COPD,|  108|112|snomed_term|   13645005|                                                        copd|13645005:::414400006:::223792000:::60349006:::223821008::...|copd:::coning:::clare:::ump:::cos:::ling:::cshase:::esp::...|Clinical Finding:::Clinical Finding:::Location:::Substanc...|
|                                      gastritis,|  114|123|snomed_term|    4556007|                                                   gastritis|4556007:::235656001:::42541005:::413241009:::108679100011...|gastritis:::chemical gastritis:::irritant gastritis:::sus...|Clinical Finding:::Clinical Finding:::Clinical Finding:::...|
|                    nonspecific ST-T abnormality|  177|204|snomed_term|  428750005|                                nonspecific st-t abnormality|428750005:::164934002:::2967003:::83456009:::93127002:::3...|nonspecific st-t abnormality:::ecg: t wave abnormal:::non...|Clinical Finding:::Clinical Finding:::Clinical Finding:::...|
|                         cardiac catheterization|  265|287|snomed_term|   41976001|                                     cardiac catheterization|41976001:::705923009:::721968000:::467735004:::129085009:...|cardiac catheterization:::cardiac catheter:::cardiac cath...|Procedure:::Physical Object:::Record Artifact:::Physical ...|
|                                       occlusion|  300|308|snomed_term|   50173008|                                                   occlusion|50173008:::263823007:::278684003:::246407001:::109501002:...|occlusion:::occluded:::functional occlusion:::method of o...|Morph Abnormality:::Qualifier Value:::Clinical Finding:::...|
|left anterior descending coronary artery lesion,|  321|368|snomed_term|  876859003|stenosis of anterior descending branch of left coronary a...|876859003:::371804009:::840608004:::1255623001:::12555690...|stenosis of anterior descending branch of left coronary a...|Clinical Finding:::Clinical Finding:::Clinical Finding:::...|
|                                     hypotension|  395|405|snomed_term|   45007003|                                                 hypotension|45007003:::241727003:::19721008:::28651003:::67763001:::9...|hypotension:::induced hypotension:::globe hypotension:::p...|Clinical Finding:::Procedure:::Clinical Finding:::Clinica...|
|                          hemodynamically stable|  583|604|snomed_term|  301459008|                                      hemodynamically stable|301459008:::301148008:::271651005:::409683007:::359746009...|hemodynamically stable:::pulse rate stable:::stable blood...|Clinical Finding:::Clinical Finding:::Clinical Finding:::...|
+------------------------------------------------+-----+---+-----------+-----------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_term_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|4.3 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
