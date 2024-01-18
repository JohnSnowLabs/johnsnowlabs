---
layout: model
title: Pipeline for Human Phenotype Ontology (HPO) Sentence Entity Resolver
author: John Snow Labs
name: hpo_resolver_pipeline
date: 2024-01-18
tags: [licensed, en, entity_resolution, clinical, pipeline, hpo]
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

This advanced pipeline extracts human phenotype entities from clinical texts and utilizes the `sbiobert_base_cased_mli` Sentence Bert Embeddings to map these entities to their corresponding Human Phenotype Ontology (HPO) codes. It also returns associated codes from the following vocabularies for each HPO code: - MeSH (Medical Subject Headings)- SNOMED- UMLS (Unified Medical Language System ) - ORPHA (international reference resource for information on rare diseases and orphan drugs) - OMIM (Online Mendelian Inheritance in Man).

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_resolver_pipeline_en_5.2.1_3.4_1705567225042.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_resolver_pipeline_en_5.2.1_3.4_1705567225042.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("hpo_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""She is followed by Dr. X in our office and has a history of severe tricuspid regurgitation. On 05/12/08, preserved left and right ventricular systolic function, aortic sclerosis with apparent mild aortic stenosis. She has previously had a Persantine Myoview nuclear rest-stress test scan completed at ABCD Medical Center in 07/06 that was negative. She has had significant mitral valve regurgitation in the past being moderate, but on the most recent echocardiogram on 05/12/08, that was not felt to be significant. She does have a history of significant hypertension in the past. She has had dizzy spells and denies clearly any true syncope. She has had bradycardia in the past from beta-blocker therapy.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("hpo_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""She is followed by Dr. X in our office and has a history of severe tricuspid regurgitation. On 05/12/08, preserved left and right ventricular systolic function, aortic sclerosis with apparent mild aortic stenosis. She has previously had a Persantine Myoview nuclear rest-stress test scan completed at ABCD Medical Center in 07/06 that was negative. She has had significant mitral valve regurgitation in the past being moderate, but on the most recent echocardiogram on 05/12/08, that was not felt to be significant. She does have a history of significant hypertension in the past. She has had dizzy spells and denies clearly any true syncope. She has had bradycardia in the past from beta-blocker therapy.""")

```
</div>

## Results

```bash
+--------------------------+-----+---+---------+----------+--------------------------+--------------------------------------------------+
|                     chunk|begin|end|ner_label|resolution|               description|                                         all_codes|
+--------------------------+-----+---+---------+----------+--------------------------+--------------------------------------------------+
|   tricuspid regurgitation|   67| 89|       HP|HP:0005180|   tricuspid regurgitation|MSH:D014262||SNOMED:111287006||UMLS:C0040961||O...|
|           aortic stenosis|  197|211|       HP|HP:0001650|           aortic stenosis|MSH:D001024||SNOMED:60573004||UMLS:C0003507||OR...|
|mitral valve regurgitation|  373|398|       HP|HP:0001653|mitral valve regurgitation|MSH:D008944||SNOMED:48724000||UMLS:C0026266,C35...|
|              hypertension|  555|566|       HP|HP:0000822|              hypertension|MSH:D006973||SNOMED:24184005,38341003||UMLS:C00...|
|               bradycardia|  655|665|       HP|HP:0001662|               bradycardia|MSH:D001919||SNOMED:48867003||UMLS:C0428977||OR...|
+--------------------------+-----+---+---------+----------+--------------------------+--------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_resolver_pipeline|
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
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
