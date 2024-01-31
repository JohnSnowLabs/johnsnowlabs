---
layout: model
title: Pipeline for SNOMED Codes - Procedure and Measurement Version
author: John Snow Labs
name: snomed_procedures_measurements_resolver_pipeline
date: 2024-01-31
tags: [licensed, en, snomed, pipeline, resolver, procedure, measurements]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline extracts `Procedure` and measurement (`Test`) entities and maps them to their corresponding SNOMED codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_procedures_measurements_resolver_pipeline_en_5.2.1_3.4_1706726530964.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_procedures_measurements_resolver_pipeline_en_5.2.1_3.4_1706726530964.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("snomed_procedures_measurements_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""Based on the severity of her abdominal examination and the persistence of her symptoms,
            it has been determined that she requires a laparoscopic jejunectomy, possible appendectomy, and
            cholecystectomy. Laboratory values indicate a white blood cell count of 15.3,
            hemoglobin level of 12.8, and normal platelet count. Alkaline phosphatase is elevated at 184,
            while liver function tests are otherwise normal. Electrolyte levels are within the normal range.
            Glucose levels are at 134, and creatinine is 0.7.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("snomed_procedures_measurements_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""Based on the severity of her abdominal examination and the persistence of her symptoms,
            it has been determined that she requires a laparoscopic jejunectomy, possible appendectomy, and
            cholecystectomy. Laboratory values indicate a white blood cell count of 15.3,
            hemoglobin level of 12.8, and normal platelet count. Alkaline phosphatase is elevated at 184,
            while liver function tests are otherwise normal. Electrolyte levels are within the normal range.
            Glucose levels are at 134, and creatinine is 0.7.""")

```
</div>

## Results

```bash

+------------------------+-----+---+---------+-----------+--------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                   chunk|begin|end|ner_label|snomed_code|                      resolution|                                           all_k_resolutions|                                                 all_k_codes|
+------------------------+-----+---+---------+-----------+--------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|laparoscopic jejunectomy|  143|166|Procedure| 1220546008|laparoscopic excision of jejunum|laparoscopic excision of jejunum:::laparoscopic appendice...|1220546008:::6025007:::307195003:::1220549001:::708627007...|
|            appendectomy|  178|189|Procedure|   80146002|                    appendectomy|appendectomy:::appendicotomy:::appendicectomy:::secondary...|80146002:::17041004:::149412002:::82730006:::174045003:::...|
|         cholecystectomy|  208|222|Procedure|   38102005|                 cholecystectomy|cholecystectomy:::choledochectomy:::cholecystotomy:::endo...|38102005:::6402000:::44337006:::45595009:::34130000:::899...|
|  white blood cell count|  253|274|     Test|     767002|          white blood cell count|white blood cell count:::white blood cell test:::differen...|767002:::252305002:::142922003:::44190001:::391558003:::4...|
|        hemoglobin level|  297|312|     Test|  313995005|              hemoglobin a level|hemoglobin a level:::plasma hemoglobin level:::hemoglobin...|313995005:::104142005:::407705000:::143073002:::35170002:...|
|          platelet count|  334|347|     Test|   61928009|                  platelet count|platelet count:::plateletcrit:::platelet estimate:::mean ...|61928009:::250314004:::8574009:::75672003:::80329005:::40...|
|    Alkaline phosphatase|  350|369|     Test|   88810008|alkaline phosphatase measurement|alkaline phosphatase measurement:::alkaline phosphatase s...|88810008:::45745006:::143948004:::166625007:::271234008::...|
|    liver function tests|  409|428|     Test|  143927001|            liver function tests|liver function tests:::liver function test:::liver functi...|143927001:::26958001:::166601004:::269992001:::736164009:...|
|      Electrolyte levels|  452|469|     Test|   79301008|        electrolytes measurement|electrolytes measurement:::electrolyte regulation:::blood...|79301008:::276025008:::144342002:::401142008:::386275008:...|
|          Glucose levels|  512|525|     Test|  144323001|             serum glucose level|serum glucose level:::plasma glucose level:::blood glucos...|144323001:::167094009:::144184004:::36048009:::72191006::...|
|                     BUN|  539|541|     Test|  105011006|                 bun measurement|bun measurement:::cinching:::bost operation:::pexy:::blou...|105011006:::16227009:::85651007:::1431002:::46747009:::45...|
|              creatinine|  553|562|     Test|   70901006|          creatinine measurement|creatinine measurement:::plasma creatinine level:::serum ...|70901006:::166729007:::166713004:::144658009:::313936008:...|
+------------------------+-----+---+---------+-----------+--------------------------------+------------------------------------------------------------+------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_procedures_measurements_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
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
- NerConverterInternalModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
