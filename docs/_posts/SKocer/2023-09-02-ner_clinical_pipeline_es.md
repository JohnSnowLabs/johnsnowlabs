---
layout: model
title: Pipeline to Detect Problem, Test and Treatment (Turkish)
author: John Snow Labs
name: ner_clinical_pipeline
date: 2023-09-02
tags: [licensed, es, clinical, pipeline, ner]
task: [Named Entity Recognition, Pipeline Healthcare]
language: es
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
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CLINICAL_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_pipeline_es_5.0.2_3.2_1693691191029.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_pipeline_es_5.0.2_3.2_1693691191029.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_clinical_pipeline", "es", "clinical/models")

result = ner_pipeline.annotate("""Una mujer de 50 años acudió a la clínica ortopédica quejándose de dolor persistente, inflamación y limitación de la amplitud de movimiento en la rodilla derecha. La paciente refería antecedentes de artrosis y una lesión previa de rodilla. Se realizó un examen clínico y radiografías que revelaron un estrechamiento del espacio articular, formación de osteofitos y signos de degeneración del cartílago. Para confirmar el diagnóstico y evaluar la gravedad, se solicitó una resonancia magnética. La resonancia mostró una gran pérdida de cartílago y cambios óseos compatibles con una artrosis avanzada. Tras considerar el estado y las preferencias del paciente, se discutió un plan de tratamiento que incluía control del dolor, fisioterapia y la posibilidad de una cirugía de sustitución articular.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_clinical_pipeline", "es", "clinical/models")

val result = ner_pipeline.annotate("""Una mujer de 50 años acudió a la clínica ortopédica quejándose de dolor persistente, inflamación y limitación de la amplitud de movimiento en la rodilla derecha. La paciente refería antecedentes de artrosis y una lesión previa de rodilla. Se realizó un examen clínico y radiografías que revelaron un estrechamiento del espacio articular, formación de osteofitos y signos de degeneración del cartílago. Para confirmar el diagnóstico y evaluar la gravedad, se solicitó una resonancia magnética. La resonancia mostró una gran pérdida de cartílago y cambios óseos compatibles con una artrosis avanzada. Tras considerar el estado y las preferencias del paciente, se discutió un plan de tratamiento que incluía control del dolor, fisioterapia y la posibilidad de una cirugía de sustitución articular.""")

```
</div>

## Results

```bash
|    | chunks                                                        |   begin |   end | entities   |
|---:|:--------------------------------------------------------------|--------:|------:|:-----------|
|  0 | clínica ortopédica                                            |      33 |    50 | TREATMENT  |
|  1 | dolor persistente                                             |      66 |    82 | PROBLEM    |
|  2 | inflamación                                                   |      85 |    95 | PROBLEM    |
|  3 | limitación de la amplitud de movimiento en la rodilla derecha |      99 |   159 | PROBLEM    |
|  4 | artrosis                                                      |     198 |   205 | PROBLEM    |
|  5 | una lesión previa de rodilla                                  |     209 |   236 | PROBLEM    |
|  6 | examen clínico y radiografías                                 |     253 |   281 | TEST       |
|  7 | estrechamiento del espacio articular                          |     300 |   335 | PROBLEM    |
|  8 | formación de osteofitos                                       |     338 |   360 | PROBLEM    |
|  9 | signos de degeneración del cartílago                          |     364 |   399 | PROBLEM    |
| 10 | una resonancia magnética                                      |     467 |   490 | TEST       |
| 11 | resonancia                                                    |     496 |   505 | TEST       |
| 12 | pérdida de cartílago                                          |     523 |   542 | PROBLEM    |
| 13 | cambios óseos compatibles                                     |     546 |   570 | PROBLEM    |
| 14 | una artrosis avanzada                                         |     576 |   596 | PROBLEM    |
| 15 | tratamiento                                                   |     681 |   691 | TREATMENT  |
| 16 | control                                                       |     705 |   711 | TREATMENT  |
| 17 | dolor                                                         |     717 |   721 | PROBLEM    |
| 18 | fisioterapia                                                  |     724 |   735 | TREATMENT  |
| 19 | cirugía de sustitución articular                              |     761 |   792 | TREATMENT  |
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
|Language:|es|
|Size:|1.3 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
