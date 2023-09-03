---
layout: model
title: Pipeline to Detect Problem, Test and Treatment (Italian)
author: John Snow Labs
name: ner_clinical_pipeline
date: 2023-09-02
tags: [licensed, it, clinical, pipeline, ner]
task: [Named Entity Recognition, Pipeline Healthcare]
language: it
edition: Healthcare NLP 5.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_clinical](https://nlp.johnsnowlabs.com/2023/08/29/ner_clinical_tr.html) model.

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CLINICAL_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_pipeline_it_5.0.2_3.4_1693691918355.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_pipeline_it_5.0.2_3.4_1693691918355.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_clinical_pipeline", "it", "clinical/models")

result = ner_pipeline.annotate("""Una donna di 50 anni si è presentata alla clinica ortopedica lamentando dolore persistente, gonfiore e limitata capacità di movimento del ginocchio destro. La paziente ha riferito un'anamnesi di osteoartrite e un precedente infortunio al ginocchio. Sono stati eseguiti un esame clinico e delle radiografie che hanno rivelato un restringimento dello spazio articolare, la formazione di osteofiti e segni di degenerazione della cartilagine. Per confermare la diagnosi e valutarne la gravità, è stata ordinata una risonanza magnetica. La risonanza magnetica ha mostrato un'estesa perdita di cartilagine e alterazioni ossee coerenti con un'osteoartrite avanzata. Dopo aver considerato le condizioni e le preferenze del paziente, è stato discusso un piano di trattamento che prevedeva il controllo del dolore, la fisioterapia e la possibilità di un intervento di sostituzione dell'articolazione.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_clinical_pipeline", "it", "clinical/models")

val result = ner_pipeline.annotate("""Una donna di 50 anni si è presentata alla clinica ortopedica lamentando dolore persistente, gonfiore e limitata capacità di movimento del ginocchio destro. La paziente ha riferito un'anamnesi di osteoartrite e un precedente infortunio al ginocchio. Sono stati eseguiti un esame clinico e delle radiografie che hanno rivelato un restringimento dello spazio articolare, la formazione di osteofiti e segni di degenerazione della cartilagine. Per confermare la diagnosi e valutarne la gravità, è stata ordinata una risonanza magnetica. La risonanza magnetica ha mostrato un'estesa perdita di cartilagine e alterazioni ossee coerenti con un'osteoartrite avanzata. Dopo aver considerato le condizioni e le preferenze del paziente, è stato discusso un piano di trattamento che prevedeva il controllo del dolore, la fisioterapia e la possibilità di un intervento di sostituzione dell'articolazione.""")

```
</div>

## Results

```bash
|    | chunks                                              |   begin |   end | entities   |
|---:|:----------------------------------------------------|--------:|------:|:-----------|
|  0 | dolore persistente                                  |      72 |    89 | PROBLEM    |
|  1 | gonfiore                                            |      92 |    99 | PROBLEM    |
|  2 | limitata capacità di movimento del ginocchio destro |     103 |   153 | PROBLEM    |
|  3 | osteoartrite                                        |     195 |   206 | PROBLEM    |
|  4 | infortunio al ginocchio                             |     224 |   246 | PROBLEM    |
|  5 | un esame clinico                                    |     269 |   284 | TEST       |
|  6 | delle radiografie                                   |     288 |   304 | TEST       |
|  7 | un restringimento dello spazio articolare           |     325 |   365 | PROBLEM    |
|  8 | formazione di osteofiti                             |     371 |   393 | PROBLEM    |
|  9 | segni di degenerazione della cartilagine            |     397 |   436 | PROBLEM    |
| 10 | una risonanza magnetica                             |     507 |   529 | TEST       |
| 11 | La risonanza magnetica                              |     532 |   553 | TEST       |
| 12 | un'estesa perdita di cartilagine                    |     567 |   598 | PROBLEM    |
| 13 | alterazioni ossee coerenti                          |     602 |   627 | PROBLEM    |
| 14 | un'osteoartrite avanzata                            |     633 |   656 | PROBLEM    |
| 15 | dolore                                              |     797 |   802 | PROBLEM    |
| 16 | fisioterapia                                        |     808 |   819 | TREATMENT  |
| 17 | un intervento di sostituzione dell'articolazione    |     841 |   888 | TREATMENT  |
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
|Language:|it|
|Size:|1.2 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
