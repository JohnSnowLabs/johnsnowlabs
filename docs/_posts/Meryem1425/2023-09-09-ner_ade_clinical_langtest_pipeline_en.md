---
layout: model
title: Pipeline to Detect Adverse Drug Events (langtest)
author: John Snow Labs
name: ner_ade_clinical_langtest_pipeline
date: 2023-09-09
tags: [licensed, en, ade, clinical, pipeline, ner]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.1.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_ade_clinical_langtest](https://nlp.johnsnowlabs.com/2023/07/31/ner_ade_clinical_langtest_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_ade_clinical_langtest_pipeline_en_5.1.0_3.0_1694280973257.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_ade_clinical_langtest_pipeline_en_5.1.0_3.0_1694280973257.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_ade_clinical_langtest_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""I asked my doctor what could have caused this, and he said it was probably from the Lipitor. Recently I experienced extreme stomach pain that stretched to my side and back. The stomach pain came suddenly and it would come and go for a week before it became so bad I could not sleep. I had just gotten over a urinary tract infection (one of the side-effects) and I thought it had returned, but the symptoms were different. I still had the urge to urinate constantly, but it would come and go, and I would have no symptoms for a day, then it would return again. I remembered reading the pamphlet that comes with the prescription drugs, and it mentioning some of the symptoms that I was experiencing. I stopped taking the Lipitor for a day, and I did not have any more stomach pain or urgency. I also had been experiencing lack of energy for quite some time, and I attributed this to stress, but after reading this website, I feel it was due to the Lipitor also. I don't think I will take this drug anymore, and since I read that taking vitamin C can help you with your cholesterol, I think I will try this method instead. I think there should be a better alternative to lowering cholesterol than such a potent drug that can cause so many side effects. I don't want to be a case-study when they finally take this drug off the market.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_ade_clinical_langtest_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""I asked my doctor what could have caused this, and he said it was probably from the Lipitor. Recently I experienced extreme stomach pain that stretched to my side and back. The stomach pain came suddenly and it would come and go for a week before it became so bad I could not sleep. I had just gotten over a urinary tract infection (one of the side-effects) and I thought it had returned, but the symptoms were different. I still had the urge to urinate constantly, but it would come and go, and I would have no symptoms for a day, then it would return again. I remembered reading the pamphlet that comes with the prescription drugs, and it mentioning some of the symptoms that I was experiencing. I stopped taking the Lipitor for a day, and I did not have any more stomach pain or urgency. I also had been experiencing lack of energy for quite some time, and I attributed this to stress, but after reading this website, I feel it was due to the Lipitor also. I don't think I will take this drug anymore, and since I read that taking vitamin C can help you with your cholesterol, I think I will try this method instead. I think there should be a better alternative to lowering cholesterol than such a potent drug that can cause so many side effects. I don't want to be a case-study when they finally take this drug off the market.""")

```
</div>

## Results

```bash
|    | chunks                     |   begin |   end | entities   |
|---:|:---------------------------|--------:|------:|:-----------|
|  0 | the Lipitor                |      80 |    90 | DRUG       |
|  1 | stomach pain               |     124 |   135 | ADE        |
|  2 | back                       |     167 |   170 | ADE        |
|  3 | stomach pain               |     177 |   188 | ADE        |
|  4 | urinary tract infection    |     308 |   330 | ADE        |
|  5 | urge to urinate constantly |     438 |   463 | ADE        |
|  6 | the prescription drugs     |     610 |   631 | DRUG       |
|  7 | the Lipitor                |     715 |   725 | DRUG       |
|  8 | lack of energy             |     820 |   833 | ADE        |
|  9 | Lipitor                    |     946 |   952 | DRUG       |
| 10 | vitamin C                  |    1034 |  1042 | DRUG       |
| 11 | I don't                    |    1250 |  1256 | DRUG       |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_ade_clinical_langtest_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.1.0+|
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