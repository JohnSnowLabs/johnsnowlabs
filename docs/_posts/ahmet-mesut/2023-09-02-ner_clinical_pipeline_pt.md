---
layout: model
title: Pipeline to Detect Problem, Test and Treatment (Portuguese)
author: John Snow Labs
name: ner_clinical_pipeline
date: 2023-09-02
tags: [licensed, pt, clinical, pipeline, ner]
task: [Named Entity Recognition, Pipeline Healthcare]
language: pt
edition: Healthcare NLP 5.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_clinical](https://nlp.johnsnowlabs.com/2023/08/16/ner_clinical_pt.html) model.

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CLINICAL_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_pipeline_pt_5.0.2_3.4_1693689950298.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_pipeline_pt_5.0.2_3.4_1693689950298.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_clinical_pipeline", "pt", "clinical/models")

result = ner_pipeline.annotate("""Uma mulher de 50 anos veio à clínica ortopédica com queixas de dor persistente, inchaço e limitação da amplitude de movimentos no joelho direito. A doente referia uma história de osteoartrite e uma lesão anterior no joelho. Foi efectuado um exame clínico e radiografias que revelaram um estreitamento do espaço articular, formação de osteófitos e sinais de degeneração da cartilagem. Para confirmar o diagnóstico e avaliar a gravidade, foi pedida uma ressonância magnética. A RM mostrou uma perda extensa de cartilagem e alterações ósseas consistentes com osteoartrite avançada. Depois de considerar a condição e as preferências do doente, foi discutido um plano de tratamento que envolvia o controlo da dor, fisioterapia e a possibilidade de cirurgia de substituição da articulação.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_clinical_pipeline", "pt", "clinical/models")

val result = ner_pipeline.annotate("""Uma mulher de 50 anos veio à clínica ortopédica com queixas de dor persistente, inchaço e limitação da amplitude de movimentos no joelho direito. A doente referia uma história de osteoartrite e uma lesão anterior no joelho. Foi efectuado um exame clínico e radiografias que revelaram um estreitamento do espaço articular, formação de osteófitos e sinais de degeneração da cartilagem. Para confirmar o diagnóstico e avaliar a gravidade, foi pedida uma ressonância magnética. A RM mostrou uma perda extensa de cartilagem e alterações ósseas consistentes com osteoartrite avançada. Depois de considerar a condição e as preferências do doente, foi discutido um plano de tratamento que envolvia o controlo da dor, fisioterapia e a possibilidade de cirurgia de substituição da articulação.""")

```
</div>

## Results

```bash
|    | chunks                                                 |   begin |   end | entities   |
|---:|:-------------------------------------------------------|--------:|------:|:-----------|
|  0 | dor persistente                                        |      63 |    77 | PROBLEM    |
|  1 | inchaço                                                |      80 |    86 | PROBLEM    |
|  2 | limitação da amplitude de movimentos no joelho direito |      90 |   143 | PROBLEM    |
|  3 | osteoartrite                                           |     179 |   190 | PROBLEM    |
|  4 | uma lesão anterior no joelho                           |     194 |   221 | PROBLEM    |
|  5 | exame clínico                                          |     241 |   253 | TEST       |
|  6 | radiografias                                           |     257 |   268 | TEST       |
|  7 | estreitamento do espaço articular                      |     287 |   319 | PROBLEM    |
|  8 | osteófitos                                             |     334 |   343 | PROBLEM    |
|  9 | sinais de degeneração da cartilagem                    |     347 |   381 | PROBLEM    |
| 10 | uma ressonância magnética                              |     447 |   471 | TEST       |
| 11 | A RM                                                   |     474 |   477 | TEST       |
| 12 | perda extensa de cartilagem                            |     491 |   517 | PROBLEM    |
| 13 | alterações ósseas                                      |     521 |   537 | PROBLEM    |
| 14 | osteoartrite avançada                                  |     556 |   576 | PROBLEM    |
| 15 | dor                                                    |     704 |   706 | PROBLEM    |
| 16 | fisioterapia                                           |     709 |   720 | TREATMENT  |
| 17 | cirurgia de substituição da articulação                |     743 |   781 | TREATMENT  |
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
|Language:|pt|
|Size:|1.2 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
