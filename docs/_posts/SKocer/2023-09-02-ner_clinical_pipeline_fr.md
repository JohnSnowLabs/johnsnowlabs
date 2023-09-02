---
layout: model
title: Pipeline to Detect Problem, Test and Treatment (French)
author: John Snow Labs
name: ner_clinical_pipeline
date: 2023-09-02
tags: [licensed, fr, clinical, pipeline, ner]
task: [Named Entity Recognition, Pipeline Healthcare]
language: fr
edition: Healthcare NLP 5.0.2
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_clinical](https://nlp.johnsnowlabs.com/2023/08/29/ner_clinical_tr.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_pipeline_fr_5.0.2_3.2_1693692642148.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_pipeline_fr_5.0.2_3.2_1693692642148.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_clinical_pipeline", "fr", "clinical/models")

result = ner_pipeline.annotate("""Une femme de 50 ans s'est présentée à la clinique orthopédique en se plaignant d'une douleur persistante, d'un gonflement et d'une limitation de l'amplitude de mouvement de son genou droit. La patiente a déclaré avoir des antécédents d'arthrose et s'être déjà blessée au genou. L'examen clinique et les radiographies effectuées ont révélé un rétrécissement de l'espace articulaire, la formation d'ostéophytes et des signes de dégénérescence du cartilage. Pour confirmer le diagnostic et en évaluer la gravité, une IRM a été demandée. L'IRM a montré une perte importante de cartilage et des modifications osseuses correspondant à une arthrose avancée. Après avoir pris en compte l'état de santé et les préférences du patient, un plan de traitement comprenant la prise en charge de la douleur, la kinésithérapie et la possibilité d'une arthroplastie a été discuté.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_clinical_pipeline", "fr", "clinical/models")

val result = ner_pipeline.annotate("""Une femme de 50 ans s'est présentée à la clinique orthopédique en se plaignant d'une douleur persistante, d'un gonflement et d'une limitation de l'amplitude de mouvement de son genou droit. La patiente a déclaré avoir des antécédents d'arthrose et s'être déjà blessée au genou. L'examen clinique et les radiographies effectuées ont révélé un rétrécissement de l'espace articulaire, la formation d'ostéophytes et des signes de dégénérescence du cartilage. Pour confirmer le diagnostic et en évaluer la gravité, une IRM a été demandée. L'IRM a montré une perte importante de cartilage et des modifications osseuses correspondant à une arthrose avancée. Après avoir pris en compte l'état de santé et les préférences du patient, un plan de traitement comprenant la prise en charge de la douleur, la kinésithérapie et la possibilité d'une arthroplastie a été discuté.""")

```
</div>

## Results

```bash
|    | chunks                                 |   begin |   end | entities   |
|---:|:---------------------------------------|--------:|------:|:-----------|
|  0 | douleur persistante                    |      85 |   103 | PROBLEM    |
|  1 | gonflement                             |     111 |   120 | PROBLEM    |
|  2 | mouvement de son genou droit           |     160 |   187 | PROBLEM    |
|  3 | antécédents d'arthrose                 |     222 |   243 | PROBLEM    |
|  4 | blessée au genou                       |     260 |   275 | PROBLEM    |
|  5 | L'examen clinique                      |     278 |   294 | TEST       |
|  6 | les radiographies                      |     299 |   315 | TEST       |
|  7 | rétrécissement de l'espace articulaire |     342 |   379 | PROBLEM    |
|  8 | signes de dégénérescence du cartilage  |     416 |   452 | PROBLEM    |
|  9 | gravité                                |     501 |   507 | PROBLEM    |
| 10 | une IRM                                |     510 |   516 | TEST       |
| 11 | L'IRM                                  |     534 |   538 | TEST       |
| 12 | perte importante de cartilage          |     553 |   581 | PROBLEM    |
| 13 | osseuses correspondant                 |     604 |   625 | PROBLEM    |
| 14 | arthrose avancée                       |     633 |   648 | PROBLEM    |
| 15 | douleur                                |     783 |   789 | PROBLEM    |
| 16 | arthroplastie                          |     834 |   846 | TREATMENT  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|fr|
|Size:|1.3 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel