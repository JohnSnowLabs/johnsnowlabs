---
layout: model
title: Named Entity Recognition Profiling (SDOH)
author: John Snow Labs
name: ner_profiling_sdoh
date: 2023-06-27
tags: [licensed, en, clinical, profiling, ner_profiling, ner, sdoh, social_determinants_of_health]
task: [Named Entity Recognition, Pipeline Healthcare]
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

This pipeline can be used to explore all the available pretrained NER models at once for Social Determinants of Health. When you run this pipeline over your text, you will end up with the predictions coming out of each pretrained clinical NER model trained with `embeddings_clinical`. 

Here are the NER models that this pretrained pipeline includes:

`ner_sdoh`, `ner_sdoh_social_environment_wip`, `ner_sdoh_mentions`, `ner_sdoh_demographics_wip`, `ner_sdoh_community_condition_wip`, `ner_sdoh_substance_usage_wip`, `ner_sdoh_access_to_healthcare_wip`, `ner_sdoh_health_behaviours_problems_wip`, `ner_sdoh_income_social_status_wip`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_profiling_sdoh_en_4.4.4_3.4_1687845759026.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_profiling_sdoh_en_4.4.4_3.4_1687845759026.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_profiling_pipeline = PretrainedPipeline("ner_profiling_sdoh", 'en', 'clinical/models')

result = ner_profiling_pipeline.annotate("""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis three years prior to presentation , associated with an acute hepatitis , and obesity with a body mass index ( BMI ) of 33.5 kg/m2 , presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_profiling_pipeline = PretrainedPipeline("ner_profiling_sdoh", "en", "clinical/models")

val result = ner_profiling_pipeline.annotate("""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis three years prior to presentation , associated with an acute hepatitis , and obesity with a body mass index ( BMI ) of 33.5 kg/m2 , presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .""")

```
</div>

## Results

```bash
 
 ******************** ner_sdoh_access_to_healthcare_wip Model Results ******************** 

[('A', 'O'), ('28-year-old', 'O'), ('female', 'O'), ('with', 'O'), ('a', 'O'), ('history', 'O'), ('of', 'O'), ('gestational', 'O'), ('diabetes', 'O'), ('mellitus', 'O'), ('diagnosed', 'O'), ('eight', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), ('and', 'O'), ('subsequent', 'O'), ('type', 'O'), ('two', 'O'), ('diabetes', 'O'), ('mellitus', 'O'), ('(', 'O'), ('T2DM', 'O'), ('),', 'O'), ('one', 'O'), ('prior', 'O'), ('episode', 'O'), ('of', 'O'), ('HTG-induced', 'O'), ('pancreatitis', 'O'), ('three', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), (',', 'O'), ('associated', 'O'), ('with', 'O'), ('an', 'O'), ('acute', 'O'), ('hepatitis', 'O'), (',', 'O'), ('and', 'O'), ('obesity', 'O'), ('with', 'O'), ('a', 'O'), ('body', 'O'), ('mass', 'B-Insurance_Status'), ('index', 'I-Insurance_Status'), ('(', 'O'), ('BMI', 'O'), (')', 'O'), ('of', 'O'), ('33.5', 'O'), ('kg/m2', 'O'), (',', 'O'), ('presented', 'O'), ('with', 'O'), ('a', 'O'), ('one-week', 'O'), ('history', 'O'), ('of', 'O'), ('polyuria', 'O'), (',', 'O'), ('polydipsia', 'O'), (',', 'O'), ('poor', 'O'), ('appetite', 'O'), (',', 'O'), ('and', 'O'), ('vomiting', 'O'), ('.', 'O')]


 ******************** ner_sdoh_mentions Model Results ******************** 

[('A', 'O'), ('28-year-old', 'O'), ('female', 'O'), ('with', 'O'), ('a', 'O'), ('history', 'O'), ('of', 'O'), ('gestational', 'O'), ('diabetes', 'O'), ('mellitus', 'O'), ('diagnosed', 'O'), ('eight', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), ('and', 'O'), ('subsequent', 'O'), ('type', 'O'), ('two', 'O'), ('diabetes', 'O'), ('mellitus', 'O'), ('(', 'O'), ('T2DM', 'O'), ('),', 'O'), ('one', 'O'), ('prior', 'O'), ('episode', 'O'), ('of', 'O'), ('HTG-induced', 'O'), ('pancreatitis', 'O'), ('three', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), (',', 'O'), ('associated', 'O'), ('with', 'O'), ('an', 'O'), ('acute', 'O'), ('hepatitis', 'O'), (',', 'O'), ('and', 'O'), ('obesity', 'O'), ('with', 'O'), ('a', 'O'), ('body', 'O'), ('mass', 'O'), ('index', 'O'), ('(', 'O'), ('BMI', 'O'), (')', 'O'), ('of', 'O'), ('33.5', 'O'), ('kg/m2', 'O'), (',', 'O'), ('presented', 'O'), ('with', 'O'), ('a', 'O'), ('one-week', 'O'), ('history', 'O'), ('of', 'O'), ('polyuria', 'O'), (',', 'O'), ('polydipsia', 'O'), (',', 'O'), ('poor', 'O'), ('appetite', 'O'), (',', 'O'), ('and', 'O'), ('vomiting', 'O'), ('.', 'O')]

 
 ******************** ner_sdoh Model Results ******************** 

[('A', 'O'), ('28-year-old', 'B-Age'), ('female', 'B-Gender'), ('with', 'O'), ('a', 'O'), ('history', 'O'), ('of', 'O'), ('gestational', 'B-Other_Disease'), ('diabetes', 'I-Other_Disease'), ('mellitus', 'I-Other_Disease'), ('diagnosed', 'O'), ('eight', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), ('and', 'O'), ('subsequent', 'O'), ('type', 'O'), ('two', 'O'), ('diabetes', 'B-Other_Disease'), ('mellitus', 'I-Other_Disease'), ('(', 'O'), ('T2DM', 'B-Other_Disease'), ('),', 'O'), ('one', 'O'), ('prior', 'O'), ('episode', 'O'), ('of', 'O'), ('HTG-induced', 'O'), ('pancreatitis', 'B-Other_Disease'), ('three', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), (',', 'O'), ('associated', 'O'), ('with', 'O'), ('an', 'O'), ('acute', 'B-Other_Disease'), ('hepatitis', 'I-Other_Disease'), (',', 'O'), ('and', 'O'), ('obesity', 'B-Obesity'), ('with', 'O'), ('a', 'O'), ('body', 'O'), ('mass', 'O'), ('index', 'O'), ('(', 'O'), ('BMI', 'O'), (')', 'O'), ('of', 'O'), ('33.5', 'O'), ('kg/m2', 'O'), (',', 'O'), ('presented', 'O'), ('with', 'O'), ('a', 'O'), ('one-week', 'O'), ('history', 'O'), ('of', 'O'), ('polyuria', 'B-Other_Disease'), (',', 'O'), ('polydipsia', 'B-Other_Disease'), (',', 'O'), ('poor', 'O'), ('appetite', 'O'), (',', 'O'), ('and', 'O'), ('vomiting', 'O'), ('.', 'O')]

 
 ******************** ner_social_environment Model Results ******************** 

[('A', 'O'), ('28-year-old', 'O'), ('female', 'O'), ('with', 'O'), ('a', 'O'), ('history', 'O'), ('of', 'O'), ('gestational', 'O'), ('diabetes', 'O'), ('mellitus', 'O'), ('diagnosed', 'O'), ('eight', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), ('and', 'O'), ('subsequent', 'O'), ('type', 'O'), ('two', 'O'), ('diabetes', 'O'), ('mellitus', 'O'), ('(', 'O'), ('T2DM', 'O'), ('),', 'O'), ('one', 'O'), ('prior', 'O'), ('episode', 'O'), ('of', 'O'), ('HTG-induced', 'O'), ('pancreatitis', 'O'), ('three', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), (',', 'O'), ('associated', 'O'), ('with', 'O'), ('an', 'O'), ('acute', 'O'), ('hepatitis', 'O'), (',', 'O'), ('and', 'O'), ('obesity', 'O'), ('with', 'O'), ('a', 'O'), ('body', 'O'), ('mass', 'O'), ('index', 'O'), ('(', 'O'), ('BMI', 'O'), (')', 'O'), ('of', 'O'), ('33.5', 'O'), ('kg/m2', 'O'), (',', 'O'), ('presented', 'O'), ('with', 'O'), ('a', 'O'), ('one-week', 'O'), ('history', 'O'), ('of', 'O'), ('polyuria', 'O'), (',', 'O'), ('polydipsia', 'O'), (',', 'O'), ('poor', 'O'), ('appetite', 'O'), (',', 'O'), ('and', 'O'), ('vomiting', 'O'), ('.', 'O')]


 ******************** ner_sdoh_demographics_wip Model Results ******************** 

[('A', 'O'), ('28-year-old', 'B-Gender'), ('female', 'B-Gender'), ('with', 'O'), ('a', 'O'), ('history', 'O'), ('of', 'O'), ('gestational', 'O'), ('diabetes', 'O'), ('mellitus', 'O'), ('diagnosed', 'O'), ('eight', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), ('and', 'O'), ('subsequent', 'O'), ('type', 'O'), ('two', 'O'), ('diabetes', 'O'), ('mellitus', 'O'), ('(', 'O'), ('T2DM', 'O'), ('),', 'O'), ('one', 'O'), ('prior', 'O'), ('episode', 'O'), ('of', 'O'), ('HTG-induced', 'O'), ('pancreatitis', 'O'), ('three', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), (',', 'O'), ('associated', 'O'), ('with', 'O'), ('an', 'O'), ('acute', 'O'), ('hepatitis', 'O'), (',', 'O'), ('and', 'O'), ('obesity', 'O'), ('with', 'O'), ('a', 'O'), ('body', 'O'), ('mass', 'O'), ('index', 'O'), ('(', 'O'), ('BMI', 'O'), (')', 'O'), ('of', 'O'), ('33.5', 'O'), ('kg/m2', 'O'), (',', 'O'), ('presented', 'O'), ('with', 'O'), ('a', 'O'), ('one-week', 'O'), ('history', 'O'), ('of', 'O'), ('polyuria', 'O'), (',', 'O'), ('polydipsia', 'O'), (',', 'O'), ('poor', 'O'), ('appetite', 'O'), (',', 'O'), ('and', 'O'), ('vomiting', 'O'), ('.', 'O')]

 
 ******************** ner_sdoh_community_condition_wip Model Results ******************** 

[('A', 'O'), ('28-year-old', 'O'), ('female', 'O'), ('with', 'O'), ('a', 'O'), ('history', 'O'), ('of', 'O'), ('gestational', 'O'), ('diabetes', 'O'), ('mellitus', 'O'), ('diagnosed', 'O'), ('eight', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), ('and', 'O'), ('subsequent', 'O'), ('type', 'O'), ('two', 'O'), ('diabetes', 'O'), ('mellitus', 'O'), ('(', 'O'), ('T2DM', 'O'), ('),', 'O'), ('one', 'O'), ('prior', 'O'), ('episode', 'O'), ('of', 'O'), ('HTG-induced', 'O'), ('pancreatitis', 'O'), ('three', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), (',', 'O'), ('associated', 'O'), ('with', 'O'), ('an', 'O'), ('acute', 'O'), ('hepatitis', 'O'), (',', 'O'), ('and', 'O'), ('obesity', 'O'), ('with', 'O'), ('a', 'O'), ('body', 'O'), ('mass', 'O'), ('index', 'O'), ('(', 'O'), ('BMI', 'O'), (')', 'O'), ('of', 'O'), ('33.5', 'O'), ('kg/m2', 'O'), (',', 'O'), ('presented', 'O'), ('with', 'O'), ('a', 'O'), ('one-week', 'O'), ('history', 'O'), ('of', 'O'), ('polyuria', 'O'), (',', 'O'), ('polydipsia', 'O'), (',', 'O'), ('poor', 'B-Community_Living_Conditions'), ('appetite', 'I-Community_Living_Conditions'), (',', 'O'), ('and', 'O'), ('vomiting', 'O'), ('.', 'O')]


 ******************** ner_sdoh_health_behaviours_problems_wip Model Results ******************** 

[('A', 'O'), ('28-year-old', 'O'), ('female', 'O'), ('with', 'O'), ('a', 'O'), ('history', 'O'), ('of', 'O'), ('gestational', 'B-Other_Disease'), ('diabetes', 'I-Other_Disease'), ('mellitus', 'I-Other_Disease'), ('diagnosed', 'O'), ('eight', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), ('and', 'O'), ('subsequent', 'O'), ('type', 'O'), ('two', 'O'), ('diabetes', 'B-Other_Disease'), ('mellitus', 'I-Other_Disease'), ('(', 'O'), ('T2DM', 'B-Other_Disease'), ('),', 'O'), ('one', 'O'), ('prior', 'O'), ('episode', 'O'), ('of', 'O'), ('HTG-induced', 'O'), ('pancreatitis', 'B-Other_Disease'), ('three', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), (',', 'O'), ('associated', 'O'), ('with', 'O'), ('an', 'O'), ('acute', 'B-Other_Disease'), ('hepatitis', 'I-Other_Disease'), (',', 'O'), ('and', 'O'), ('obesity', 'B-Obesity'), ('with', 'O'), ('a', 'O'), ('body', 'O'), ('mass', 'O'), ('index', 'O'), ('(', 'O'), ('BMI', 'B-Obesity'), (')', 'O'), ('of', 'O'), ('33.5', 'O'), ('kg/m2', 'B-Obesity'), (',', 'O'), ('presented', 'O'), ('with', 'O'), ('a', 'O'), ('one-week', 'O'), ('history', 'O'), ('of', 'O'), ('polyuria', 'B-Other_Disease'), (',', 'O'), ('polydipsia', 'B-Eating_Disorder'), (',', 'O'), ('poor', 'O'), ('appetite', 'O'), (',', 'O'), ('and', 'O'), ('vomiting', 'O'), ('.', 'O')]

 
 ******************** ner_sdoh_income_social_status_wip Model Results ******************** 

[('A', 'O'), ('28-year-old', 'O'), ('female', 'O'), ('with', 'O'), ('a', 'O'), ('history', 'O'), ('of', 'O'), ('gestational', 'O'), ('diabetes', 'O'), ('mellitus', 'O'), ('diagnosed', 'O'), ('eight', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), ('and', 'O'), ('subsequent', 'O'), ('type', 'O'), ('two', 'O'), ('diabetes', 'O'), ('mellitus', 'O'), ('(', 'O'), ('T2DM', 'O'), ('),', 'O'), ('one', 'O'), ('prior', 'O'), ('episode', 'O'), ('of', 'O'), ('HTG-induced', 'O'), ('pancreatitis', 'O'), ('three', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), (',', 'O'), ('associated', 'O'), ('with', 'O'), ('an', 'O'), ('acute', 'O'), ('hepatitis', 'O'), (',', 'O'), ('and', 'O'), ('obesity', 'O'), ('with', 'O'), ('a', 'O'), ('body', 'O'), ('mass', 'O'), ('index', 'O'), ('(', 'O'), ('BMI', 'O'), (')', 'O'), ('of', 'O'), ('33.5', 'O'), ('kg/m2', 'O'), (',', 'O'), ('presented', 'O'), ('with', 'O'), ('a', 'O'), ('one-week', 'O'), ('history', 'O'), ('of', 'O'), ('polyuria', 'O'), (',', 'O'), ('polydipsia', 'O'), (',', 'O'), ('poor', 'O'), ('appetite', 'O'), (',', 'O'), ('and', 'O'), ('vomiting', 'O'), ('.', 'O')]

 
 ******************** ner_sdoh_substance_usage_wip Model Results ******************** 

[('A', 'O'), ('28-year-old', 'O'), ('female', 'O'), ('with', 'O'), ('a', 'O'), ('history', 'O'), ('of', 'O'), ('gestational', 'O'), ('diabetes', 'O'), ('mellitus', 'O'), ('diagnosed', 'O'), ('eight', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), ('and', 'O'), ('subsequent', 'O'), ('type', 'O'), ('two', 'O'), ('diabetes', 'O'), ('mellitus', 'O'), ('(', 'O'), ('T2DM', 'O'), ('),', 'O'), ('one', 'O'), ('prior', 'O'), ('episode', 'O'), ('of', 'O'), ('HTG-induced', 'O'), ('pancreatitis', 'O'), ('three', 'O'), ('years', 'O'), ('prior', 'O'), ('to', 'O'), ('presentation', 'O'), (',', 'O'), ('associated', 'O'), ('with', 'O'), ('an', 'O'), ('acute', 'O'), ('hepatitis', 'O'), (',', 'O'), ('and', 'O'), ('obesity', 'O'), ('with', 'O'), ('a', 'O'), ('body', 'O'), ('mass', 'O'), ('index', 'O'), ('(', 'O'), ('BMI', 'O'), (')', 'O'), ('of', 'O'), ('33.5', 'O'), ('kg/m2', 'O'), (',', 'O'), ('presented', 'O'), ('with', 'O'), ('a', 'O'), ('one-week', 'O'), ('history', 'O'), ('of', 'O'), ('polyuria', 'O'), (',', 'O'), ('polydipsia', 'B-Alcohol'), (',', 'O'), ('poor', 'O'), ('appetite', 'O'), (',', 'O'), ('and', 'O'), ('vomiting', 'O'), ('.', 'O')]

 
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_profiling_sdoh|
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
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel