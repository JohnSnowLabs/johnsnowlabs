---
layout: model
title: Summarize Radiology Reports
author: John Snow Labs
name: summarizer_radiology
date: 2023-04-23
tags: [clinical, licensed, en, summarization, tensorflow, radiology]
task: Summarization
language: en
edition: Healthcare NLP 4.4.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalSummarizer
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is capable of summarizing radiology reports while preserving the important information such as imaging tests and findings.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/summarizer_radiology_en_4.4.0_3.0_1682218525772.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/summarizer_radiology_en_4.4.0_3.0_1682218525772.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

summarizer = MedicalSummarizer.pretrained("summarizer_radiology", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("summary")\
    .setMaxTextLength(512)\
    .setMaxNewTokens(512)

pipeline = Pipeline(stages=[
    document,
    summarizer  
])

text = """INDICATIONS: Peripheral vascular disease with claudication.

RIGHT:
1. Normal arterial imaging of right lower extremity.
2. Peak systolic velocity is normal.
3. Arterial waveform is triphasic.
4. Ankle brachial index is 0.96.

LEFT:
1. Normal arterial imaging of left lower extremity.
2. Peak systolic velocity is normal.
3. Arterial waveform is triphasic throughout except in posterior tibial artery where it is biphasic.
4. Ankle brachial index is 1.06.

IMPRESSION: 
Normal arterial imaging of both lower lobes.
"""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val summarizer = MedicalSummarizer.pretrained("summarizer_radiology", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("summary")
    .setMaxTextLength(512)
    .setMaxNewTokens(512)

val pipeline = new Pipeline().setStages(Array(document_assembler, summarizer))

val text = """INDICATIONS: Peripheral vascular disease with claudication.

RIGHT:
1. Normal arterial imaging of right lower extremity.
2. Peak systolic velocity is normal.
3. Arterial waveform is triphasic.
4. Ankle brachial index is 0.96.

LEFT:
1. Normal arterial imaging of left lower extremity.
2. Peak systolic velocity is normal.
3. Arterial waveform is triphasic throughout except in posterior tibial artery where it is biphasic.
4. Ankle brachial index is 1.06.

IMPRESSION: 
Normal arterial imaging of both lower lobes.
"""

val data = Seq(text).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
The patient has peripheral vascular disease with claudication. The right lower extremity shows normal arterial imaging, but the peak systolic velocity is normal. The arterial waveform is triphasic throughout, except for the posterior tibial artery, which is biphasic. The ankle brachial index is 0.96. The impression is normal arterial imaging of both lower lobes.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|summarizer_radiology|
|Compatibility:|Healthcare NLP 4.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|920.4 MB|
