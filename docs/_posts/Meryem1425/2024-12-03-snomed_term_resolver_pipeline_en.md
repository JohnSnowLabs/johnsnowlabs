---
layout: model
title: Pipeline to Resolve SNOMED Term Codes
author: John Snow Labs
name: snomed_term_resolver_pipeline
date: 2024-12-03
tags: [licensed, en, resolver, snomed, snomed_term]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained resolver pipeline extracts SNOMED terms and map them to their corresponding SNOMED codes using `BertSentenceChunkEmbeddings` which gets the embeddings of the sentence and the chunks then averages them. This helps the pipeline to return more context-aware resolutions. Also you can find the SNOMED code domain classes in the `all_k_aux_labels` column in the metadata.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_term_resolver_pipeline_en_5.3.1_3.4_1733244327645.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_term_resolver_pipeline_en_5.3.1_3.4_1733244327645.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("snomed_term_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""[['The patient was diagnosed with acute appendicitis and scheduled for immediate surgery.'],
                                  ['His hypertension is currently managed with a combination of lifestyle modifications and medication.'],
                                  ['Laboratory tests indicate the individual has hyperthyroidism requiring further endocrinological assessment.'],
                                  ['The patient exhibited recurrent upper respiratory tract infections and presented with symptoms such as nasal congestion which persisted despite previous courses of symptomatic treatment.']]""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("snomed_term_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""(('The patient was diagnosed with acute appendicitis and scheduled for immediate surgery.'),
                                      ('His hypertension is currently managed with a combination of lifestyle modifications and medication.'),
                                      ('Laboratory tests indicate the individual has hyperthyroidism requiring further endocrinological assessment.'),
                                      ('The patient exhibited recurrent upper respiratory tract infections and presented with symptoms such as nasal congestion which persisted despite previous courses of symptomatic treatment.'))""")

```
</div>

## Results

```bash

+-------+----------------------------------+-----------+-----------+-------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|text_id|                         ner_chunk|     entity|snomed_code|                                description|                                                   all_codes|                                                 resolutions|                                            all_k_aux_labels|
+-------+----------------------------------+-----------+-----------+-------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|      0|                acute appendicitis|snomed_term|   85189001|                         acute appendicitis|85189001:::286967008:::4998000:::84534001:::235770006:::2...|acute appendicitis:::acute perforated appendicitis:::acut...|Clinical Finding:::Clinical Finding:::Clinical Finding:::...|
|      1|                      hypertension|snomed_term|  302192008|              on treatment for hypertension|302192008:::38341003:::275944005:::308502002:::270440008:...|on treatment for hypertension:::hypertension:::hypertensi...|Procedure:::Clinical Finding:::Procedure:::Clinical Findi...|
|      2|                   hyperthyroidism|snomed_term|   34486009|                            hyperthyroidism|34486009:::237510004:::4997005:::161442007:::722941003:::...|hyperthyroidism:::iodine-induced hyperthyroidism:::factit...|Clinical Finding:::Clinical Finding:::Clinical Finding:::...|
|      3|upper respiratory tract infections|snomed_term|  195708003|recurrent upper respiratory tract infection|195708003:::54150009:::312118003:::54398005:::195647007::...|recurrent upper respiratory tract infection:::upper respi...|Clinical Finding:::Clinical Finding:::Clinical Finding:::...|
|      3|                  nasal congestion|snomed_term|   68235000|                           nasal congestion|68235000:::267100006:::2571000112102:::19452008:::6461100...|nasal congestion:::nasal obstruction present:::recurrent ...|Clinical Finding:::Context-dependent:::No_Concept_Class::...|
+-------+----------------------------------+-----------+-----------+-------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_term_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.1+|
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
- BertSentenceChunkEmbeddings
- SentenceEntityResolverModel
