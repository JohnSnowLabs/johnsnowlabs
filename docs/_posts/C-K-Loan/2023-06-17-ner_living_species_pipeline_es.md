---
layout: model
title: Pipeline to Detect Living Species(w2v_cc_300d)
author: John Snow Labs
name: ner_living_species_pipeline
date: 2023-06-17
tags: [es, ner, clinical, licensed]
task: Named Entity Recognition
language: es
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_living_species](https://nlp.johnsnowlabs.com/2022/06/22/ner_living_species_es_3_0.html) model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_living_species_pipeline_es_4.4.4_3.0_1686996781872.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_living_species_pipeline_es_4.4.4_3.0_1686996781872.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_living_species_pipeline", "es", "clinical/models")

text = '''Lactante varón de dos años. Antecedentes familiares sin interés. Antecedentes personales: Embarazo, parto y periodo neonatal normal. En seguimiento por alergia a legumbres, diagnosticado con diez meses por reacción urticarial generalizada con lentejas y garbanzos, con dieta de exclusión a legumbres desde entonces. En ésta visita la madre describe episodios de eritema en zona maxilar derecha con afectación ocular ipsilateral que se resuelve en horas tras la administración de corticoides. Le ha ocurrido en 5-6 ocasiones, en relación con la ingesta de alimentos previamente tolerados. Exploración complementaria: Cacahuete, ac(ige)19.2 Ku.arb/l. Resultados: Ante la sospecha clínica de Síndrome de Frey, se tranquiliza a los padres, explicándoles la naturaleza del cuadro y se cita para revisión anual.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("ner_living_species_pipeline", "es", "clinical/models")

val text = "Lactante varón de dos años. Antecedentes familiares sin interés. Antecedentes personales: Embarazo, parto y periodo neonatal normal. En seguimiento por alergia a legumbres, diagnosticado con diez meses por reacción urticarial generalizada con lentejas y garbanzos, con dieta de exclusión a legumbres desde entonces. En ésta visita la madre describe episodios de eritema en zona maxilar derecha con afectación ocular ipsilateral que se resuelve en horas tras la administración de corticoides. Le ha ocurrido en 5-6 ocasiones, en relación con la ingesta de alimentos previamente tolerados. Exploración complementaria: Cacahuete, ac(ige)19.2 Ku.arb/l. Resultados: Ante la sospecha clínica de Síndrome de Frey, se tranquiliza a los padres, explicándoles la naturaleza del cuadro y se cita para revisión anual."

val result = pipeline.fullAnnotate(text)
```

{:.nlu-block}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_living_species_pipeline", "es", "clinical/models")

text = '''Lactante varón de dos años. Antecedentes familiares sin interés. Antecedentes personales: Embarazo, parto y periodo neonatal normal. En seguimiento por alergia a legumbres, diagnosticado con diez meses por reacción urticarial generalizada con lentejas y garbanzos, con dieta de exclusión a legumbres desde entonces. En ésta visita la madre describe episodios de eritema en zona maxilar derecha con afectación ocular ipsilateral que se resuelve en horas tras la administración de corticoides. Le ha ocurrido en 5-6 ocasiones, en relación con la ingesta de alimentos previamente tolerados. Exploración complementaria: Cacahuete, ac(ige)19.2 Ku.arb/l. Resultados: Ante la sospecha clínica de Síndrome de Frey, se tranquiliza a los padres, explicándoles la naturaleza del cuadro y se cita para revisión anual.'''

result = pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | ner_chunks     |   begin |   end | ner_label   |   confidence |
|---:|:---------------|--------:|------:|:------------|-------------:|
|  0 | Lactante varón |       0 |    13 | HUMAN       |       0.9926 |
|  1 | familiares     |      41 |    50 | HUMAN       |       0.9994 |
|  2 | personales     |      78 |    87 | HUMAN       |       0.9987 |
|  3 | neonatal       |     116 |   123 | HUMAN       |       0.9731 |
|  4 | legumbres      |     162 |   170 | SPECIES     |       0.9978 |
|  5 | lentejas       |     243 |   250 | SPECIES     |       0.9995 |
|  6 | garbanzos      |     254 |   262 | SPECIES     |       0.9933 |
|  7 | legumbres      |     290 |   298 | SPECIES     |       0.9991 |
|  8 | madre          |     334 |   338 | HUMAN       |       0.9997 |
|  9 | Cacahuete      |     616 |   624 | SPECIES     |       0.9998 |
| 10 | padres         |     728 |   733 | HUMAN       |       0.9992 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_living_species_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
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