---
layout: model
title: Medical Text Generation (BioGPT-based)
author: John Snow Labs
name: text_generator_biomedical_biogpt_base
date: 2023-04-03
tags: [licensed, en, clinical, text_generation, biogpt, tensorflow]
task: Text Generation
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalTextGenerator
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

MedicalTextGenerator is a BioGPT-based model for text generation. It can generate texts given a few tokens as an into and can generate up to 512 tokens. This model is directly ported from the official BioGPT checkpoint (base)

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/text_generator_biomedical_biogpt_base_en_4.3.2_3.0_1680514919715.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/text_generator_biomedical_biogpt_base_en_4.3.2_3.0_1680514919715.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("prompt")\
    .setOutputCol("document_prompt")

med_text_generator  = MedicalSummarizer.pretrained("text_generator_biomedical_biogpt_base", "en", "clinical/models")\
    .setInputCols("document_prompt")\
    .setOutputCol("answer")\
    .setMaxNewTokens(256)\
    .setDoSample(True)\
    .setTopK(3)\
    .setRandomSeed(42)

pipeline = Pipeline(stages=[document_assembler, med_text_generator])

data = spark.createDataFrame([["Covid 19 is"], ["The most common cause of stomach pain is"]]).toDF("document_prompt")

pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("prompt")
    .setOutputCol("document_prompt")

val med_text_generator  = MedicalSummarizer.pretrained("text_generator_biomedical_biogpt_base", "en", "clinical/models")
    .setInputCols("document_prompt")
    .setOutputCol("answer")
    .setMaxNewTokens(256)
    .setDoSample(true)
    .setTopK(3)
    .setRandomSeed(42)

val pipeline = new Pipeline().setStages(Array(document_assembler, med_text_generator))

val data = Seq(Array("Covid 19 is", "The most common cause of stomach pain is")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
"
[Covid 19 is a pandemic with high rates in both mortality ( around 5 to 8 percent in the United States ) and economic loss, which are likely related to the disruption of social life. The COVID - 19 crisis has caused a significant reduction in healthcare capacity and has led to an increased risk of infection in healthcare facilities and patients with underlying conditions, which has increased morbidity, increased mortality rates in patients, and increased healthcare costs. The COVID - 19 pandemic has also led to a significant increase in the number of patients with chronic diseases, which has led to an increase in the number of patients with chronic conditions who are at high cardiovascular ( cardiovascular diseases &#91; CDs &#93; ) risk and therefore require intensive care. &quot; This review will discuss the impact of this COVID pandemic in the healthcare system, the potential impact in healthcare providers caring and treating patients with CDs, and the potential impact on the healthcare system. The COVID Pandemias- A Review of the Current Literature. The COVID - 19 pandemic has resulted in a significant increase in the number of patients with cardiovascular disease ( CVD ). The number of patients with CVD is expected to increase by approximately 20 percent by the end of 2020. The number of patients with CVD will also increase by approximately 20 percent by the end of 2020]

[The most common cause of stomach pain is peptic ulcer disease. The diagnosis of gastric ulcer is based on the presence and severity ( as determined by endoscopy ) of the ulcer, as confirmed on the basis ofendoscopic biopsy and gastric mucosal biopsy with urease tests, and by the presence of Helicobacter pylori. The treatment of gastric ulcer is based on the eradication of H. pylori. The aim of this study, conducted on the population aged over 40 in the city of Szczecin, was to determine the prevalence of H. pylori infection in patients with gastric ulcer and to assess the effectiveness of the eradication therapy. MATERIAL AND METHODS: The study involved patients aged over 40 who were admitted to the Gastroenterology Clinic of the Medical University of Szczecin with a diagnosis of gastric ulcer. The study was conducted on the population of patients with gastric ulcer, who were admitted to the Gastroenterology Clinic of the Medical University of Szczecin between January and December 2014. The study included patients with gastric ulcer who were admitted to the Gastroenterology Clinic of the Medical University of Szczecin between January and December 2014. The study was conducted on the population of patients aged over 40 who were admitted to the Gastroenterology Clinic of the] 

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|text_generator_biomedical_biogpt_base|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|917.9 MB|
|Case sensitive:|true|