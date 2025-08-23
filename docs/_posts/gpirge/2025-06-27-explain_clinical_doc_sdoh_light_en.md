---
layout: model
title: Explain Clinical Document Social Determinants of Health - Light
author: John Snow Labs
name: explain_clinical_doc_sdoh_light
date: 2025-06-27
tags: [licensed, en, clinical, pipeline, ner, social_determinants, sdoh]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to extract social determinants of health related clinical/medical entities from text. 

In this pipeline, 3 NER models and 2 text matchers are used to extract the related entities from text.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_sdoh_light_en_6.0.2_3.4_1751054059446.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_sdoh_light_en_6.0.2_3.4_1751054059446.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_sdoh_light", "en", "clinical/models")

result = ner_pipeline.annotate("""
Alex, 29 YO, completed high school but did not pursue any further education. He resides in a rented studio apartment in an urban area characterized by low-income housing. A.C. is currently unemployed and relies on government assistance for his income, primarily through welfare benefits and supplemental nutrition assistance. His financial situation makes it challenging for him to afford stable housing and other basic needs. Despite efforts to secure employment, A.C. faces barriers such as lack of transportation and limited job opportunities in his area.
Antony does not have health insurance coverage, which has resulted in delayed medical care and limited access to specialized treatments. He relies on community health clinics and free medical services for healthcare needs. Socially, A.C. experiences exclusion due to his economic status and substance use disorder. He struggles to maintain relationships with family and friends, often feeling isolated and marginalized.
Opioids are a class of drugs that include both prescription pain medications and illicit substances. Some common generic opioid names are morphine, codeine, oxycodone, hydrocodone, fentanyl, and heroin. Brand names for prescription opioid medications include OxyContin, Percocet, Vicodin, Opana, and Suboxone.
However, they also produce euphoria, relaxation and drowsiness. With repeated use, tolerance builds requiring higher doses to achieve the same effect.
In addition to addiction and overdose, chronic opioid use can lead to other serious health complications. 
Depression is common among those who use opioids long-term. 
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_sdoh_light", "en", "clinical/models")

val result = ner_pipeline.annotate("""
Alex, 29 YO, completed high school but did not pursue any further education. He resides in a rented studio apartment in an urban area characterized by low-income housing. A.C. is currently unemployed and relies on government assistance for his income, primarily through welfare benefits and supplemental nutrition assistance. His financial situation makes it challenging for him to afford stable housing and other basic needs. Despite efforts to secure employment, A.C. faces barriers such as lack of transportation and limited job opportunities in his area.
Antony does not have health insurance coverage, which has resulted in delayed medical care and limited access to specialized treatments. He relies on community health clinics and free medical services for healthcare needs. Socially, A.C. experiences exclusion due to his economic status and substance use disorder. He struggles to maintain relationships with family and friends, often feeling isolated and marginalized.
Opioids are a class of drugs that include both prescription pain medications and illicit substances. Some common generic opioid names are morphine, codeine, oxycodone, hydrocodone, fentanyl, and heroin. Brand names for prescription opioid medications include OxyContin, Percocet, Vicodin, Opana, and Suboxone.
However, they also produce euphoria, relaxation and drowsiness. With repeated use, tolerance builds requiring higher doses to achieve the same effect.
In addition to addiction and overdose, chronic opioid use can lead to other serious health complications. 
Depression is common among those who use opioids long-term. 
""")

```
</div>

## Results

```bash
|    | chunks                               |   begin |   end | entities         |
|---:|:-------------------------------------|--------:|------:|:-----------------|
|  0 | high school                          |      24 |    34 | Education        |
|  1 | education                            |      67 |    75 | Education        |
|  2 | rented studio apartment              |      94 |   116 | Housing          |
|  3 | low-income housing                   |     152 |   169 | Community_Safety |
|  4 | unemployed                           |     190 |   199 | Employment       |
|  5 | income                               |     245 |   250 | Income           |
|  6 | financial situation                  |     331 |   349 | Financial_Status |
|  7 | afford stable housing                |     383 |   403 | Housing          |
|  8 | lack of transportation               |     494 |   515 | Symptom          |
|  9 | health insurance coverage            |     581 |   605 | Insurance_Status |
| 10 | delayed medical care                 |     630 |   649 | Access_To_Care   |
| 11 | community health clinics             |     710 |   733 | Access_To_Care   |
| 12 | free medical services for healthcare |     739 |   774 | Access_To_Care   |
| 13 | exclusion                            |     810 |   818 | Social_Exclusion |
| 14 | substance use disorder               |     851 |   872 | Mental_Health    |
| 15 | often feeling isolated               |     939 |   960 | Symptom          |
| 16 | marginalized                         |     966 |   977 | Social_Exclusion |
| 17 | Opioids                              |     980 |   986 | DRUG             |
| 18 | drugs                                |    1003 |  1007 | Substance_Use    |
| 19 | pain medications                     |    1040 |  1055 | DRUG             |
| 20 | illicit substances                   |    1061 |  1078 | Substance_Use    |
| 21 | opioid                               |    1101 |  1106 | Substance_Use    |
| 22 | morphine                             |    1118 |  1125 | Substance_Use    |
| 23 | codeine                              |    1128 |  1134 | Substance_Use    |
| 24 | oxycodone                            |    1137 |  1145 | Substance_Use    |
| 25 | hydrocodone                          |    1148 |  1158 | Substance_Use    |
| 26 | fentanyl                             |    1161 |  1168 | DRUG             |
| 27 | heroin                               |    1175 |  1180 | Substance_Use    |
| 28 | prescription opioid                  |    1199 |  1217 | Substance_Use    |
| 29 | OxyContin                            |    1239 |  1247 | Substance_Use    |
| 30 | Percocet                             |    1250 |  1257 | Substance_Use    |
| 31 | Vicodin                              |    1260 |  1266 | Substance_Use    |
| 32 | Opana                                |    1269 |  1273 | DRUG             |
| 33 | Suboxone                             |    1280 |  1287 | Substance_Use    |
| 34 | euphoria                             |    1317 |  1324 | Symptom          |
| 35 | relaxation                           |    1327 |  1336 | Symptom          |
| 36 | drowsiness                           |    1342 |  1351 | Symptom          |
| 37 | addiction                            |    1456 |  1464 | Mental_Health    |
| 38 | overdose                             |    1470 |  1477 | Substance_Use    |
| 39 | chronic opioid use                   |    1480 |  1497 | Substance_Use    |
| 40 | Depression                           |    1548 |  1557 | Mental_Health    |
| 41 | use opioids                          |    1585 |  1595 | Substance_Use    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_sdoh_light|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

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
- TextMatcherInternalModel
- TextMatcherInternalModel
- ChunkMergeModel