---
layout: model
title: Pipeline to Detect Living Species (bert_embeddings_bert_base_fr_cased)
author: John Snow Labs
name: ner_living_species_bert_pipeline
date: 2023-06-16
tags: [fr, ner, clinical, licensed, bert]
task: Named Entity Recognition
language: fr
edition: Healthcare NLP 4.4.4
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_living_species_bert](https://nlp.johnsnowlabs.com/2022/06/23/ner_living_species_bert_fr_3_0.html) model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_living_species_bert_pipeline_fr_4.4.4_3.4_1686938944752.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_living_species_bert_pipeline_fr_4.4.4_3.4_1686938944752.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_living_species_bert_pipeline", "fr", "clinical/models")

text = '''Femme de 47 ans allergique à l'iode, fumeuse sociale, opérée pour des varices, deux césariennes et un abcès fessier. Vit avec son mari et ses trois enfants, travaille comme enseignante. Initialement, le patient a eu une bonne évolution, mais au 2ème jour postopératoire, il a commencé à montrer une instabilité hémodynamique. Les sérologies pour Coxiella burnetii, Bartonella henselae, Borrelia burgdorferi, Entamoeba histolytica, Toxoplasma gondii, herpès simplex virus 1 et 2, cytomégalovirus, virus d'Epstein Barr, virus de la varicelle et du zona et parvovirus B19 étaient négatives. Cependant, un test au rose Bengale positif pour Brucella, le test de Coombs et les agglutinations étaient également positifs avec un titre de 1/40.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("ner_living_species_bert_pipeline", "fr", "clinical/models")

val text = "Femme de 47 ans allergique à l'iode, fumeuse sociale, opérée pour des varices, deux césariennes et un abcès fessier. Vit avec son mari et ses trois enfants, travaille comme enseignante. Initialement, le patient a eu une bonne évolution, mais au 2ème jour postopératoire, il a commencé à montrer une instabilité hémodynamique. Les sérologies pour Coxiella burnetii, Bartonella henselae, Borrelia burgdorferi, Entamoeba histolytica, Toxoplasma gondii, herpès simplex virus 1 et 2, cytomégalovirus, virus d'Epstein Barr, virus de la varicelle et du zona et parvovirus B19 étaient négatives. Cependant, un test au rose Bengale positif pour Brucella, le test de Coombs et les agglutinations étaient également positifs avec un titre de 1/40."

val result = pipeline.fullAnnotate(text)
```

{:.nlu-block}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_living_species_bert_pipeline", "fr", "clinical/models")

text = '''Femme de 47 ans allergique à l'iode, fumeuse sociale, opérée pour des varices, deux césariennes et un abcès fessier. Vit avec son mari et ses trois enfants, travaille comme enseignante. Initialement, le patient a eu une bonne évolution, mais au 2ème jour postopératoire, il a commencé à montrer une instabilité hémodynamique. Les sérologies pour Coxiella burnetii, Bartonella henselae, Borrelia burgdorferi, Entamoeba histolytica, Toxoplasma gondii, herpès simplex virus 1 et 2, cytomégalovirus, virus d'Epstein Barr, virus de la varicelle et du zona et parvovirus B19 étaient négatives. Cependant, un test au rose Bengale positif pour Brucella, le test de Coombs et les agglutinations étaient également positifs avec un titre de 1/40.'''

result = pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | ner_chunks                       |   begin |   end | ner_label   |   confidence |
|---:|:---------------------------------|--------:|------:|:------------|-------------:|
|  0 | Femme                            |       0 |     4 | HUMAN       |     1        |
|  1 | mari                             |     130 |   133 | HUMAN       |     1        |
|  2 | enfants                          |     148 |   154 | HUMAN       |     0.9999   |
|  3 | patient                          |     203 |   209 | HUMAN       |     0.9993   |
|  4 | Coxiella burnetii                |     346 |   362 | SPECIES     |     0.9879   |
|  5 | Bartonella henselae              |     365 |   383 | SPECIES     |     0.9926   |
|  6 | Borrelia burgdorferi             |     386 |   405 | SPECIES     |     0.9959   |
|  7 | Entamoeba histolytica            |     408 |   428 | SPECIES     |     0.9913   |
|  8 | Toxoplasma gondii                |     431 |   447 | SPECIES     |     0.97845  |
|  9 | cytomégalovirus                  |     479 |   493 | SPECIES     |     0.9976   |
| 10 | virus d'Epstein Barr             |     496 |   515 | SPECIES     |     0.967967 |
| 11 | virus de la varicelle et du zona |     518 |   549 | SPECIES     |     0.985429 |
| 12 | parvovirus B19                   |     554 |   567 | SPECIES     |     0.98595  |
| 13 | Brucella                         |     636 |   643 | SPECIES     |     0.9995   |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_living_species_bert_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|fr|
|Size:|410.6 MB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- BertEmbeddings
- MedicalNerModel
- NerConverterInternalModel