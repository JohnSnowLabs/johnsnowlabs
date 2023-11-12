---
layout: model
title: Pipeline to Detect Social Determinants of Health Mentions
author: John Snow Labs
name: ner_sdoh_mentions_pipeline
date: 2023-06-17
tags: [en, licensed, ner, sdoh, mentions, clinical]
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

This pretrained pipeline is built on the top of [ner_sdoh_mentions](https://nlp.johnsnowlabs.com/2022/12/18/ner_sdoh_mentions_en.html) model.

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/27.0.Social_Determinant_of_Health_Models.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_mentions_pipeline_en_4.4.4_3.0_1686993363957.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_mentions_pipeline_en_4.4.4_3.0_1686993363957.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_sdoh_mentions_pipeline", "en", "clinical/models")

text = '''Mr. Known lastname 9880 is a pleasant, cooperative gentleman with a long standing history (20 years) diverticulitis. He is married and has 3 children. He works in a bank. He denies any alcohol or intravenous drug use. He has been smoking for many years.'''

result = pipeline.fullAnnotate(text)
```

```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("ner_sdoh_mentions_pipeline", "en", "clinical/models")

val text = "Mr. Known lastname 9880 is a pleasant, cooperative gentleman with a long standing history (20 years) diverticulitis. He is married and has 3 children. He works in a bank. He denies any alcohol or intravenous drug use. He has been smoking for many years."

val result = pipeline.fullAnnotate(text)
```

</div>

## Results

```bash
|    | chunks           |   begin |   end | entities         |   confidence |
|---:|:-----------------|--------:|------:|:-----------------|-------------:|
|  0 | married          |     123 |   129 | sdoh_community   |       0.9972 |
|  1 | children         |     141 |   148 | sdoh_community   |       0.9999 |
|  2 | works            |     154 |   158 | sdoh_economics   |       0.9995 |
|  3 | alcohol          |     185 |   191 | behavior_alcohol |       0.9925 |
|  4 | intravenous drug |     196 |   211 | behavior_drug    |       0.9803 |
|  5 | smoking          |     230 |   236 | behavior_tobacco |       0.9997 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_sdoh_mentions_pipeline|
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
