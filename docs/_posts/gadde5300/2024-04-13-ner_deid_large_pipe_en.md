---
layout: model
title: Image De-Identification Pipeline
author: John Snow Labs
name: ner_deid_large_pipe
date: 2024-04-13
tags: [en, licensed, ocr, image, deid, pipeline]
task: Pipeline Healthcare
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Deidentification NER (Large) is a Named Entity Recognition model that annotates text to find protected health information that may need to be deidentified. The entities it annotates are Age, Contact, Date, Id, Location, Name, and Profession. This model is trained with the embeddings_clinical word embeddings model, so be sure to use the same embeddings in the pipeline.

It protects specific health information that could identify living or deceased individuals. The rule preserves patient confidentiality without affecting the values and the information that could be needed for different research purposes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_large_pipe_en_5.3.1_3.0_1713038644675.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_large_pipe_en_5.3.1_3.0_1713038644675.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

nlu_model = PretrainedPipeline("ner_deid_large_pipe", "en", "clinical/models")

image_path = visual.pkg_resources.resource_filename('sparkocr', 'resources/ocr/images/p1.jpg')
image_df = spark.read.format("binaryFile").load(image_path)

result = nlu_model.transform(image_df)
```

</div>

## Results

```bash
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|ner_chunk                                                                                                                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[{chunk, 193, 202, 04/04/2018, {entity -> DATE, sentence -> 1, chunk -> 0, confidence -> 0.9999}, []}, {chunk, 3290, 3290, ., {entity -> NAME, sentence -> 17, chunk -> 1, confidence -> 0.6035}, []}, {chunk, 3388, 3397, 04/12/2018, {entity -> DATE, sentence -> 20, chunk -> 2, confidence -> 1.0}, []}]|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_large_pipe|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- BinaryToImage
- ImageToText
- DocumentAssembler
- SentenceDetector
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter