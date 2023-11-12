---
layout: model
title: RE Pipeline between Body Parts and Procedures
author: John Snow Labs
name: re_bodypart_proceduretest_pipeline
date: 2023-06-13
tags: [licensed, clinical, relation_extraction, body_part, procedures, en]
task: Relation Extraction
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [re_bodypart_proceduretest](https://nlp.johnsnowlabs.com/2021/01/18/re_bodypart_proceduretest_en.html) model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/re_bodypart_proceduretest_pipeline_en_4.4.4_3.2_1686664541054.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/re_bodypart_proceduretest_pipeline_en_4.4.4_3.2_1686664541054.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("re_bodypart_proceduretest_pipeline", "en", "clinical/models")

pipeline.fullAnnotate("TECHNIQUE IN DETAIL: After informed consent was obtained from the patient and his mother, the chest was scanned with portable ultrasound.")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("re_bodypart_proceduretest_pipeline", "en", "clinical/models")

pipeline.fullAnnotate("TECHNIQUE IN DETAIL: After informed consent was obtained from the patient and his mother, the chest was scanned with portable ultrasound.")
```


{:.nlu-block}
```python
import nlu
nlu.load("en.relation.bodypart_proceduretest.pipeline").predict("""TECHNIQUE IN DETAIL: After informed consent was obtained from the patient and his mother, the chest was scanned with portable ultrasound.""")
```

</div>



## Results

```bash
| index | relations | entity1                      | entity1_begin | entity1_end | chunk1 | entity2 | entity2_end | entity2_end | chunk2              | confidence |
|-------|-----------|------------------------------|---------------|-------------|--------|---------|-------------|-------------|---------------------|------------|
| 0     | 1         | External_body_part_or_region | 94            | 98          | chest  | Test    | 117         | 135         | portable ultrasound | 1.0        |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|re_bodypart_proceduretest_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- PerceptronModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- DependencyParserModel
- RelationExtractionModel