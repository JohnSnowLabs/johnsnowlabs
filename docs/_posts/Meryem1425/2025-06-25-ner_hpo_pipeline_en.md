---
layout: model
title: Pipeline for Extracting Clinical Entities Related to HPO Codes
author: John Snow Labs
name: ner_hpo_pipeline
date: 2025-06-25
tags: [licensed, en, clinical, pipeline, ner]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to extract all entities mappable to HPO codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_hpo_pipeline_en_6.0.2_3.4_1750855563916.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_hpo_pipeline_en_6.0.2_3.4_1750855563916.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_hpo_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""She is followed by Dr. X in our office and has a history of severe tricuspid regurgitation. 
On 05/12/08, preserved left and right ventricular systolic function, aortic sclerosis with apparent mild aortic stenosis. 
She has previously had a Persantine Myoview nuclear rest-stress test scan completed at ABCD Medical Center in 07/06 that was negative. 
She has had significant mitral valve regurgitation in the past being moderate, but on the most recent echocardiogram on 05/12/08, that was not felt to be significant. 
She does have a history of significant hypertension in the past. She has had dizzy spells and denies clearly any true syncope. 
She has had bradycardia in the past from beta-blocker therapy.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_hpo_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""She is followed by Dr. X in our office and has a history of severe tricuspid regurgitation. 
On 05/12/08, preserved left and right ventricular systolic function, aortic sclerosis with apparent mild aortic stenosis. 
She has previously had a Persantine Myoview nuclear rest-stress test scan completed at ABCD Medical Center in 07/06 that was negative. 
She has had significant mitral valve regurgitation in the past being moderate, but on the most recent echocardiogram on 05/12/08, that was not felt to be significant. 
She does have a history of significant hypertension in the past. She has had dizzy spells and denies clearly any true syncope. 
She has had bradycardia in the past from beta-blocker therapy.""")

```
</div>

## Results

```bash
|    | chunks                     |   begin |   end | entities   |
|---:|:---------------------------|--------:|------:|:-----------|
|  0 | tricuspid regurgitation    |      68 |    90 | HP         |
|  1 | aortic stenosis            |     199 |   213 | HP         |
|  2 | mitral valve regurgitation |     377 |   402 | HP         |
|  3 | hypertension               |     560 |   571 | HP         |
|  4 | bradycardia                |     661 |   671 | HP         |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_hpo_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
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