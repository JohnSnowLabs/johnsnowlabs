---
layout: model
title: Pipeline to Detect Adverse Drug Events (BertForTokenClassification)
author: John Snow Labs
name: bert_token_classifier_ner_ade_pipeline
date: 2023-06-16
tags: [ner, bertfortokenclassification, adverse, ade, licensed, en]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [bert_token_classifier_ner_ade](https://nlp.johnsnowlabs.com/2022/01/04/bert_token_classifier_ner_ade_en.html) model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_ade_pipeline_en_4.4.4_3.4_1686922272139.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_ade_pipeline_en_4.4.4_3.4_1686922272139.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("bert_token_classifier_ner_ade_pipeline", "en", "clinical/models")

text = '''I have an allergic reaction to vancomycin so I have itchy skin, sore throat/burning/itching, numbness of tongue and gums. I would not recommend this drug to anyone, especially since I have never had such an adverse reaction to any other medication.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("bert_token_classifier_ner_ade_pipeline", "en", "clinical/models")

val text = "I have an allergic reaction to vancomycin so I have itchy skin, sore throat/burning/itching, numbness of tongue and gums. I would not recommend this drug to anyone, especially since I have never had such an adverse reaction to any other medication."

val result = pipeline.fullAnnotate(text)
```

{:.nlu-block}
```python
import nlu
nlu.load("en.classify.token_bert.ade_pipeline").predict("""I have an allergic reaction to vancomycin so I have itchy skin, sore throat/burning/itching, numbness of tongue and gums. I would not recommend this drug to anyone, especially since I have never had such an adverse reaction to any other medication.""")
```
</div>

## Results

```bash
|sentence_id|chunk                      |begin|end|ner_label|
+-----------+---------------------------+-----+---+---------+
|0          |allergic reaction          |10   |26 |ADE      |
|0          |vancomycin                 |31   |40 |DRUG     |
|0          |itchy skin                 |52   |61 |ADE      |
|0          |sore throat/burning/itching|64   |90 |ADE      |
|0          |numbness of tongue and gums|93   |119|ADE      |
|1          |other                      |231  |235|DRUG     |
|1          |medication                 |237  |246|DRUG     |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_ade_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|404.9 MB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- MedicalBertForTokenClassifier
- NerConverterInternalModel