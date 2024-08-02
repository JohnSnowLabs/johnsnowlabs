---
layout: model
title: Pipeline to Summarize Radiology Reports
author: John Snow Labs
name: summarizer_radiology_pipeline
date: 2023-06-22
tags: [licensed, en, clinical, summarization, radiology]
task: Summarization
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

This pretrained pipeline is built on the top of [summarizer_radiology](https://nlp.johnsnowlabs.com/2023/04/23/summarizer_jsl_radiology_en.html) model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/summarizer_radiology_pipeline_en_4.4.4_3.4_1687469849024.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/summarizer_radiology_pipeline_en_4.4.4_3.4_1687469849024.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("summarizer_radiology_pipeline", "en", "clinical/models")

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

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("summarizer_radiology_pipeline", "en", "clinical/models")

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

val result = pipeline.fullAnnotate(text)
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
|Model Name:|summarizer_radiology_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|929.2 MB|

## Included Models

- DocumentAssembler
- MedicalSummarizer