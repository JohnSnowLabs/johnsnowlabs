---
layout: model
title: Generic Classifier for Measurement - Pipeline
author: John Snow Labs
name: generic_classifier_measurement_pipeline
date: 2026-03-01
tags: [en, clinical, licensed, classification, pipeline]
task: [Text Classification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.3.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline uses a binary classification model and determines whether clinical sentences include quantitative measurement terms and values.

Classes:

 - MEASUREMENT: Contains numerical health measurements, vital signs, lab results, or test values.
 - OTHER: Doesn’t contain quantitative measurement information.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/generic_classifier_measurement_pipeline_en_6.3.0_3.4_1772404770864.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/generic_classifier_measurement_pipeline_en_6.3.0_3.4_1772404770864.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("generic_classifier_measurement_pipeline", "en", "clinical/models")

sample_text = """ [['This is a 58-year-old male who started out having a toothache in the left lower side of the mouth that is now radiating into his jaw and towards his left ear. Triage nurse reported that he does not believe it is his tooth because he has regular dental appointments, but has not seen a dentist since this new toothache began. The patient denies any facial swelling.'], ['The database was available at this point of time. WBC count is elevated at 19,000 with the left shift, hemoglobin of 17.7, and hematocrit of 55.8 consistent with severe dehydration.'], ['Temperature max is 99, heart rate was 133 to 177, blood pressure is 114/43 (while moving), respiratory rate was 28 to 56 with O2 saturations 97 to 100% on room air. Weight was 4.1 kg.'], ['I will see her back in followup in 3 months, at which time she will be recovering from a shoulder surgery and we will see if she needs any further intervention with regard to the cervical spine.I will also be in touch with Dr. Y to let him know this information prior to the surgery in several weeks.']]"""

result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("generic_classifier_measurement_pipeline", "en", "clinical/models")

sample_text = """ [['This is a 58-year-old male who started out having a toothache in the left lower side of the mouth that is now radiating into his jaw and towards his left ear. Triage nurse reported that he does not believe it is his tooth because he has regular dental appointments, but has not seen a dentist since this new toothache began. The patient denies any facial swelling.'], ['The database was available at this point of time. WBC count is elevated at 19,000 with the left shift, hemoglobin of 17.7, and hematocrit of 55.8 consistent with severe dehydration.'], ['Temperature max is 99, heart rate was 133 to 177, blood pressure is 114/43 (while moving), respiratory rate was 28 to 56 with O2 saturations 97 to 100% on room air. Weight was 4.1 kg.'], ['I will see her back in followup in 3 months, at which time she will be recovering from a shoulder surgery and we will see if she needs any further intervention with regard to the cervical spine.I will also be in touch with Dr. Y to let him know this information prior to the surgery in several weeks.']]"""

result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("generic_classifier_measurement_pipeline", "en", "clinical/models")

val sample_text = """ [['This is a 58-year-old male who started out having a toothache in the left lower side of the mouth that is now radiating into his jaw and towards his left ear. Triage nurse reported that he does not believe it is his tooth because he has regular dental appointments, but has not seen a dentist since this new toothache began. The patient denies any facial swelling.'], ['The database was available at this point of time. WBC count is elevated at 19,000 with the left shift, hemoglobin of 17.7, and hematocrit of 55.8 consistent with severe dehydration.'], ['Temperature max is 99, heart rate was 133 to 177, blood pressure is 114/43 (while moving), respiratory rate was 28 to 56 with O2 saturations 97 to 100% on room air. Weight was 4.1 kg.'], ['I will see her back in followup in 3 months, at which time she will be recovering from a shoulder surgery and we will see if she needs any further intervention with regard to the cervical spine.I will also be in touch with Dr. Y to let him know this information prior to the surgery in several weeks.']]"""

val result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```
</div>

## Results

```bash

| text                                                                                                 | result      |
| :--------------------------------------------------------------------------------------------------- | :---------- |
| This is a 58-year-old male who started out having a toothache in the left lower side of the mouth... | OTHER       |
| The database was available at this point of time. WBC count is elevated at 19,000 with the left s... | MEASUREMENT |
| Temperature max is 99, heart rate was 133 to 177, blood pressure is 114/43 (while moving), respir... | MEASUREMENT |
| I will see her back in followup in 3 months, at which time she will be recovering from a shoulder... | OTHER       |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|generic_classifier_measurement_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- TokenizerModel
- WordEmbeddingsModel
- SentenceEmbeddings
- FeaturesAssembler
- GenericClassifierModel