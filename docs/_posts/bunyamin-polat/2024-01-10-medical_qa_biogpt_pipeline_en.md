---
layout: model
title: Medical Question Answering Pipeline(biogpt)
author: John Snow Labs
name: medical_qa_biogpt_pipeline
date: 2024-01-10
tags: [licensed, en, biogpt, pipeline, qa]
task: [Question Answering, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [medical_qa_biogpt](https://nlp.johnsnowlabs.com/2023/03/09/medical_qa_biogpt_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/medical_qa_biogpt_pipeline_en_5.2.0_3.0_1704847061964.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/medical_qa_biogpt_pipeline_en_5.2.0_3.0_1704847061964.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

qa_pipeline = PretrainedPipeline("medical_qa_biogpt_pipeline", "en", "clinical/models")

context = """We have previously reported the feasibility of diagnostic and therapeutic peritoneoscopy including liver biopsy, gastrojejunostomy, and tubal ligation by an oral transgastric approach. We present results of per-oral transgastric splenectomy in a porcine model. The goal of this study was to determine the technical feasibility of per-oral transgastric splenectomy using a flexible endoscope. We performed acute experiments on 50-kg pigs. All animals were fed liquids for 3 days prior to procedure. The procedures were performed under general anesthesia with endotracheal intubation. The flexible endoscope was passed per orally into the stomach and puncture of the gastric wall was performed with a needle knife. The puncture was extended to create a 1.5-cm incision using a pull-type sphincterotome, and a double-channel endoscope was advanced into the peritoneal cavity. The peritoneal cavity was insufflated with air through the endoscope. The spleen was visualized. The splenic vessels were ligated with endoscopic loops and clips, and then mesentery was dissected using electrocautery. Endoscopic splenectomy was performed on six pigs. There were no complications during gastric incision and entrance into the peritoneal cavity. Visualization of the spleen and other intraperitoneal organs was very good. Ligation of the splenic vessels and mobilization of the spleen were achieved using commercially available devices and endoscopic accessories."""

question = """Transgastric endoscopic splenectomy: is it possible?"""

result = qa_pipeline.annotate([question], [context])

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val qa_pipeline = PretrainedPipeline("medical_qa_biogpt_pipeline", "en", "clinical/models")

val context = """We have previously reported the feasibility of diagnostic and therapeutic peritoneoscopy including liver biopsy, gastrojejunostomy, and tubal ligation by an oral transgastric approach. We present results of per-oral transgastric splenectomy in a porcine model. The goal of this study was to determine the technical feasibility of per-oral transgastric splenectomy using a flexible endoscope. We performed acute experiments on 50-kg pigs. All animals were fed liquids for 3 days prior to procedure. The procedures were performed under general anesthesia with endotracheal intubation. The flexible endoscope was passed per orally into the stomach and puncture of the gastric wall was performed with a needle knife. The puncture was extended to create a 1.5-cm incision using a pull-type sphincterotome, and a double-channel endoscope was advanced into the peritoneal cavity. The peritoneal cavity was insufflated with air through the endoscope. The spleen was visualized. The splenic vessels were ligated with endoscopic loops and clips, and then mesentery was dissected using electrocautery. Endoscopic splenectomy was performed on six pigs. There were no complications during gastric incision and entrance into the peritoneal cavity. Visualization of the spleen and other intraperitoneal organs was very good. Ligation of the splenic vessels and mobilization of the spleen were achieved using commercially available devices and endoscopic accessories."""

val question = """Transgastric endoscopic splenectomy: is it possible?"""

val result = qa_pipeline.annotate([question], [context])

```
</div>

## Results

```bash
we have developed a new technique of gastric endoscopic splenectomy ( gasps ) using a flexible endoscope. the aim of this study was to evaluate the feasibility
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|medical_qa_biogpt_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.1 GB|

## Included Models

- MultiDocumentAssembler
- MedicalQuestionAnswering