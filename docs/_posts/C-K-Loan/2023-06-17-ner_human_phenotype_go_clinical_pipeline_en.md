---
layout: model
title: Pipeline to Detect Normalized Genes and Human Phenotypes
author: John Snow Labs
name: ner_human_phenotype_go_clinical_pipeline
date: 2023-06-17
tags: [ner, clinical, licensed, en]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_human_phenotype_go_clinical](https://nlp.johnsnowlabs.com/2021/03/31/ner_human_phenotype_go_clinical_en.html) model.

## Predicted Entities

`GO`, `HP`



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_human_phenotype_go_clinical_pipeline_en_4.4.4_3.0_1686985963431.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_human_phenotype_go_clinical_pipeline_en_4.4.4_3.0_1686985963431.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_human_phenotype_go_clinical_pipeline", "en", "clinical/models")

text = '''Another disease that shares two of the tumor components of CT, namely GIST and tricarboxylic acid cycle is the Carney-Stratakis syndrome (CSS) or dyad.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("ner_human_phenotype_go_clinical_pipeline", "en", "clinical/models")

val text = "Another disease that shares two of the tumor components of CT, namely GIST and tricarboxylic acid cycle is the Carney-Stratakis syndrome (CSS) or dyad."

val result = pipeline.fullAnnotate(text)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.med_ner.human_phenotype_clinical.pipeline").predict("""Another disease that shares two of the tumor components of CT, namely GIST and tricarboxylic acid cycle is the Carney-Stratakis syndrome (CSS) or dyad.""")
```

</div>


## Results

```bash
|    | ner_chunk                |   begin |   end | ner_label   |   confidence |
|---:|:-------------------------|--------:|------:|:------------|-------------:|
|  0 | tumor                    |      39 |    43 | HP          |     0.9996   |
|  1 | tricarboxylic acid cycle |      79 |   102 | GO          |     0.994633 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_human_phenotype_go_clinical_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel