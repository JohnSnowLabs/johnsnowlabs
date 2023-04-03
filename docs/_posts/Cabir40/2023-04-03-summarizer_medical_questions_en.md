---
layout: model
title: Summarize Clinical Question Notes
author: John Snow Labs
name: summarizer_medical_questions
date: 2023-04-03
tags: [licensed, en, clinical, summarization, tensorflow]
task: Summarization
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalSummarizer
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model can generate questions related to the provided medical information.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/summarizer_medical_questions_en_4.3.2_3.0_1680522989497.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/summarizer_medical_questions_en_4.3.2_3.0_1680522989497.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

summarizer = MedicalSummarizer.pretrained("summarizer_medical_questions", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("summary")\
    .setMaxTextLength(512)\
    .setMaxNewTokens(512)

pipeline = sparknlp.base.Pipeline(stages=[
    document_assembler,
    summarizer  
])

text = """Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val summarizer  = MedicalSummarizer.pretrained("summarizer_medical_questions", "en", "clinical/models")
    .setInputCols("document_prompt")
    .setOutputCol("answer")
    .setMaxTextLength(512)
    .setMaxNewTokens(512)

val pipeline = new Pipeline().setStages(Array(document_assembler, summarizer))

val text = """Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you."""

val data = Seq(Array(text)).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

['What are the treatments for hyperthyroidism?']

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|summarizer_medical_questions|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|920.0 MB|
