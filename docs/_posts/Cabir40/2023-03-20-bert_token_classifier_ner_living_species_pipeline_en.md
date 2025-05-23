---
layout: model
title: Pipeline to Detect Living Species
author: John Snow Labs
name: bert_token_classifier_ner_living_species_pipeline
date: 2023-03-20
tags: [en, ner, clinical, licensed, bertfortokenclassification]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.3.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [bert_token_classifier_ner_living_species](https://nlp.johnsnowlabs.com/2022/06/26/bert_token_classifier_ner_living_species_en_3_0.html) model.

## Predicted Entities

`HUMAN`,`SPECIES`




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_living_species_pipeline_en_4.3.0_3.2_1679304760714.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_living_species_pipeline_en_4.3.0_3.2_1679304760714.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("bert_token_classifier_ner_living_species_pipeline", "en", "clinical/models")

text = '''42-year-old woman with end-stage chronic kidney disease, secondary to lupus nephropathy, and on peritoneal dialysis. History of four episodes of bacterial peritonitis and change of Tenckhoff catheter six months prior to admission due to catheter dysfunction. Three peritoneal fluid samples during her hospitalisation tested positive for Fusarium spp. The patient responded favourably and continued outpatient treatment with voriconazole (4mg/kg every 12 hours orally). All three isolates were identified as species of the Fusarium solani complex. In vitro susceptibility to itraconazole, voriconazole and posaconazole, according to Clinical and Laboratory Standards Institute - CLSI (M38-A) methodology, showed a minimum inhibitory concentration (MIC) in all three isolates and for all three antifungals of >16 μg/mL.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("bert_token_classifier_ner_living_species_pipeline", "en", "clinical/models")

val text = "42-year-old woman with end-stage chronic kidney disease, secondary to lupus nephropathy, and on peritoneal dialysis. History of four episodes of bacterial peritonitis and change of Tenckhoff catheter six months prior to admission due to catheter dysfunction. Three peritoneal fluid samples during her hospitalisation tested positive for Fusarium spp. The patient responded favourably and continued outpatient treatment with voriconazole (4mg/kg every 12 hours orally). All three isolates were identified as species of the Fusarium solani complex. In vitro susceptibility to itraconazole, voriconazole and posaconazole, according to Clinical and Laboratory Standards Institute - CLSI (M38-A) methodology, showed a minimum inhibitory concentration (MIC) in all three isolates and for all three antifungals of >16 μg/mL."

val result = pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | ner_chunk               |   begin |   end | ner_label   |   confidence |
|---:|:------------------------|--------:|------:|:------------|-------------:|
|  0 | woman                   |      12 |    16 | HUMAN       |     0.986743 |
|  1 | bacterial               |     145 |   153 | SPECIES     |     0.975256 |
|  2 | Fusarium spp            |     337 |   348 | SPECIES     |     0.998142 |
|  3 | patient                 |     355 |   361 | HUMAN       |     0.994012 |
|  4 | species                 |     507 |   513 | SPECIES     |     0.962562 |
|  5 | Fusarium solani complex |     522 |   544 | SPECIES     |     0.999028 |
|  6 | antifungals             |     792 |   802 | SPECIES     |     0.999852 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_living_species_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|404.8 MB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- MedicalBertForTokenClassifier
- NerConverterInternalModel