---
layout: model
title: Pipeline for SNOMED Conditions Sentence Entity Resolver
author: John Snow Labs
name: snomed_conditions_resolver_pipeline
date: 2024-03-11
tags: [licensed, en, entity_resolution, clinical, pipeline, snomed, conditions]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This advanced pipeline extracts clinical conditions from clinical texts and utilizes the `sbiobert_base_cased_mli` Sentence Bert Embeddings to map these entities to their corresponding SNOMED codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_conditions_resolver_pipeline_en_5.3.0_3.2_1710173616813.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_conditions_resolver_pipeline_en_5.3.0_3.2_1710173616813.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("snomed_conditions_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""Medical professionals rushed in the bustling emergency room to attend to the patient with distressed breathing.
          The attending physician immediately noted signs of respiratory distress, including stridor, a high-pitched sound indicative of upper respiratory tract obstruction.
          The patient, struggling to breathe, exhibited dyspnea. Concern raised when they began experiencing syncope,
          a sudden loss of consciousness likely stemming from inadequate oxygenation. Further examination revealed a respiratory tract hemorrhage.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("snomed_conditions_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""Medical professionals rushed in the bustling emergency room to attend to the patient with distressed breathing.
          The attending physician immediately noted signs of respiratory distress, including stridor, a high-pitched sound indicative of upper respiratory tract obstruction.
          The patient, struggling to breathe, exhibited dyspnea. Concern raised when they began experiencing syncope,
          a sudden loss of consciousness likely stemming from inadequate oxygenation. Further examination revealed a respiratory tract hemorrhage.""")

```
</div>

## Results

```bash
+-----------------------------------+-----+---+-------------------------+---------+-----------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                              chunk|begin|end|                ner_label|     code|                        description|                                                   all_codes|                                                 resolutions|
+-----------------------------------+-----+---+-------------------------+---------+-----------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|               distressed breathing|   90|109|                  Symptom|271825005|               distressed breathing|271825005:::230145002:::386813002:::248585001:::47653008:...|distressed breathing:::difficulty breathing:::breathing a...|
|               respiratory distress|  173|192|               VS_Finding|271825005|               respiratory distress|271825005:::418092006:::75483001:::373895009:::230145002:...|respiratory distress:::respiratory tract congestion:::pai...|
|                            stridor|  205|211|                  Symptom| 70407001|                            stridor|70407001:::301826004:::58596002:::301287002:::307487006::...|stridor:::intermittent stridor:::inhalatory stridor:::exp...|
|               a high-pitched sound|  214|233|                  PROBLEM| 51406002|                 high pitched voice|51406002:::300211002:::271661003:::405495005:::23292001::...|high pitched voice:::responds to high frequency sounds:::...|
|upper respiratory tract obstruction|  249|283|Disease_Syndrome_Disorder| 68372009|upper respiratory tract obstruction|68372009:::79688008:::73342002:::301252002:::201060008:::...|upper respiratory tract obstruction:::respiratory obstruc...|
|              struggling to breathe|  309|329|                  Symptom|289105003|   difficulty controlling breathing|289105003:::230145002:::289116005:::386813002:::271825005...|difficulty controlling breathing:::difficulty breathing::...|
|                            dyspnea|  342|348|                  Symptom|267036007|                            dyspnea|267036007:::60845006:::25209001:::34560001:::59265000:::8...|dyspnea:::exertional dyspnea:::inspiratory dyspnea:::expi...|
|                            syncope|  395|401|                  Symptom|271594007|                            syncope|271594007:::234167006:::90129003:::445535007:::31457007::...|syncope:::situational syncope:::tussive syncope:::witness...|
|     a sudden loss of consciousness|  414|443|                  PROBLEM| 32834005|        brief loss of consciousness|32834005:::40863000:::7862002:::15203004:::419045004:::27...|brief loss of consciousness:::moderate loss of consciousn...|
|             inadequate oxygenation|  466|487|                  Symptom|238161004|           impaired oxygen delivery|238161004:::70944005:::238162006:::123826004:::238160003:...|impaired oxygen delivery:::impaired gas exchange:::impair...|
|     a respiratory tract hemorrhage|  519|548|                  PROBLEM| 95431003|       respiratory tract hemorrhage|95431003:::233783005:::405541003:::78144005:::276543004::...|respiratory tract hemorrhage:::tracheal hemorrhage:::bron...|
+-----------------------------------+-----+---+-------------------------+---------+-----------------------------------+------------------------------------------------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_conditions_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.7 GB|

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
