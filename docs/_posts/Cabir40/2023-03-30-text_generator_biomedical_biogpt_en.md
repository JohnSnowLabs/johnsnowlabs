---
layout: model
title: Medical Text Generator
author: John Snow Labs
name: text_generator_biomedical_biogpt
date: 2023-03-30
tags: [licensed, en, clinical, text_generation, tensorflow]
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

MedicalTextGenerator is a BioGPT-based model for text generation. It can generate texts given a few tokens as an into and can generate up to 512 tokens. This model is directly ported from the official [BioGPT checkpoint (base)](https://github.com/microsoft/BioGPT)

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/text_generator_biomedical_biogpt_en_4.3.2_3.0_1680174668185.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/text_generator_biomedical_biogpt_en_4.3.2_3.0_1680174668185.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()    .setInputCol("prompt")    .setOutputCol("document_prompt")

med_text_generator = MedicalTextGenerator.pretrained("text_generator_biomedical_biogpt", "en", "clinical/models")    .setInputCols(["document_prompt"])    .setMaxNewTokens(128)    .setDoSample(True)    .setTopK(3)    .setOutputCol("answer")    .setRandomSeed(42)

pipeline = Pipeline(stages=[document_assembler, med_text_generator])

data = spark.createDataFrame([["Covid 19 is"], 
                              ["The most common cause of stomach pain is"], 
                              ['the patient is admitted to the clinic with a severe back pain and we']]).toDF("prompt")

pipeline.fit(data).transform(data).select("answer.result").show(truncate=False)
```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("prompt")
    .setOutputCol("document_prompt")

val med_text_generator = MedicalTextGenerator.pretrained("text_generator_biomedical_biogpt", "en", "clinical/models")
    .setInputCols("document_prompt")
    .setMaxNewTokens(128)
    .setDoSample(true)
    .setTopK(3)
    .setOutputCol("answer")
    .setRandomSeed(42)

val pipeline = new Pipeline(stages=[document_assembler, med_text_generator])

val data = Seq(Array("Covid 19 is","The most common cause of stomach pain is", 
                    "the patient is admitted to the clinic with a severe back pain and we")).toDS.toDF("prompt")

pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
"
# med_text_generator.setStopAtEos(False)
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[Covid 19 is a new coronavirus that causes a severe respiratory disease. In December 2019 the virus was discovered, but its origin is not yet fully understood and no effective treatment is available. &quot; COVID - A New Coronavirus Disease. The COVID - 19 pandemic has caused a global health emergency. The virus is a novel coronavirus that has spread rapidly and caused severe respiratory tract disease and has resulted in more than 250,000 deaths worldwide. The virus is a member of the Coronaviridae family and is transmitted by the respiratory droplet. The main symptoms of COVID - 19 are respiratory and digestive tract symptoms. The virus is a member of]                                                                                                                                                                                               |
|[The most common cause of stomach pain is peptic ulcer, but the diagnosis is often difficult. In patients without a history or signs suggesting a bleeding ulcer or a peptic ulcer, the diagnosis is usually a malignancy. The diagnosis of gastric cancer is often difficult and often delayed. The diagnosis is usually made at endoscopy. The treatment of gastric cancer is surgical, and the 5 years survival rate ranges from 20 % to 30 percent, depending mainly of tumor type and stage. In the case of early gastric cancer, the prognosis depends on the stage of the tumor. The role of the family physician in the management of patients with diabetes mellitus. Diabetes mellitus is]                                                                                                                                                                                |
|[the patient is admitted to the clinic with a severe back pain and we have diagnosed a spinal epidural haematoma with CT and magnetic Resonance. The patient was treated conservatively and the symptoms disappeared. We present the case to show how the spinal cord compression can be treated conservatively. An uncommon complication following percutaneous endoscopic discectomy We describe an extremely rare complication following percutaneous endoscopic discectomy. A patient with a herniated lumbar disc was treated with percutaneous endoscopic discectomy and developed severe back pains after the surgery and was diagnosed with a postoperative epidural hematoma. The patient was treated conservatively and the symptoms disappeared. The role for surgery in the treatment of spinal metastasis: the experience from an Australian tertiary referral centre.]|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


# med_text_generator.setStopAtEos(True)
+------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------+
|[Covid 19 is a pandemic with a high mortality rate.]                                                                          |
|[The most common cause of stomach pain is gastroesophageal ( GE - type, gastroesophageal regurgitation and epigastric pain ).]|
|[the patient is admitted to the clinic with a severe back pain and we performed the CT scan of the spine.]                    |
+------------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|text_generator_biomedical_biogpt|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|917.9 MB|
|Case sensitive:|true|