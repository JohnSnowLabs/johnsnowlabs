---
layout: model
title: Pipeline for SNOMED Drug Sentence Entity Resolver
author: John Snow Labs
name: snomed_drug_resolver_pipeline
date: 2024-03-11
tags: [licensed, en, entity_resolution, clinical, pipeline, snomed, drug]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This advanced pipeline extracts drug entities from clinical texts and utilizes the `sbiobert_base_cased_mli` Sentence Bert Embeddings to map these entities to their corresponding SNOMED codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_drug_resolver_pipeline_en_5.3.0_3.4_1710173654375.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_drug_resolver_pipeline_en_5.3.0_3.4_1710173654375.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("snomed_drug_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""John's doctor prescribed aspirin for his heart condition,
along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and
lansoprazole for his GORD on 2023-12-01.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("snomed_drug_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""John's doctor prescribed aspirin for his heart condition,
along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and
lansoprazole for his GORD on 2023-12-01.""")

```
</div>

## Results

```bash
+------------+-----+---+---------+---------+------------+------------------------------------------------------------+------------------------------------------------------------+
|       chunk|begin|end|ner_label|     code| description|                                                   all_codes|                                                 resolutions|
+------------+-----+---+---------+---------+------------+------------------------------------------------------------+------------------------------------------------------------+
|     aspirin|   25| 31|     DRUG|  7947003|     aspirin|7947003:::358427004:::426365001:::412566001:::25796002:::...|aspirin:::oral aspirin:::aspirin, buffered:::buffered asp...|
| paracetamol|   69| 79|     DRUG|387517004| paracetamol|387517004:::90332006:::437876006:::437818001:::322998004:...|paracetamol:::paracetamol product:::oral form paracetamol...|
| amoxicillin|  109|119|     DRUG| 27658006| amoxicillin|27658006:::350162003:::427483001:::350164002:::117147001:...|amoxicillin:::oral amoxicillin:::amoxicillin sodium:::ora...|
|lansoprazole|  144|155|     DRUG|108666007|lansoprazole|108666007:::437961004:::441863009:::716069007:::108840006...|lansoprazole:::oral form lansoprazole:::dexlansoprazole::...|
+------------+-----+---+---------+---------+------------+------------------------------------------------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_drug_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.4 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- TextMatcherInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
