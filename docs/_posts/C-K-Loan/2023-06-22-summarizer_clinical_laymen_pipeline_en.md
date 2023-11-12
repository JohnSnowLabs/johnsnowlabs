---
layout: model
title: Pipeline to Summarize Clinical Notes in Laymen Terms
author: John Snow Labs
name: summarizer_clinical_laymen_pipeline
date: 2023-06-22
tags: [licensed, en, clinical, summarization, laymen_terms]
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

This pretrained pipeline is built on the top of [summarizer_clinical_laymen](https://nlp.johnsnowlabs.com/2023/05/31/summarizer_clinical_laymen_en.html) model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/summarizer_clinical_laymen_pipeline_en_4.4.4_3.4_1687461901192.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/summarizer_clinical_laymen_pipeline_en_4.4.4_3.4_1687461901192.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("summarizer_clinical_laymen_pipeline", "en", "clinical/models")

text = """
Olivia Smith was seen in my office for evaluation for elective surgical weight loss on October 6, 2008. Olivia Smith is a 34-year-old female with a BMI of 43. She is 5'6" tall and weighs 267 pounds. She is motivated to attempt surgical weight loss because she has been overweight for over 20 years and wants to have more energy and improve her self-image. She is not only affected physically, but also socially by her weight. When she loses weight she always regains it and she always gains back more weight than she has lost. At one time, she lost 100 pounds and gained the weight back within a year. She has tried numerous commercial weight loss programs including Weight Watcher's for four months in 1992 with 15-pound weight loss, RS for two months in 1990 with six-pound weight loss, Slim Fast for six weeks in 2004 with eight-pound weight loss, an exercise program for two months in 2007 with a five-pound weight loss, Atkin's Diet for three months in 2008 with a ten-pound weight loss, and Dexatrim for one month in 2005 with a five-pound weight loss. She has also tried numerous fat reduction or fad diets. She was on Redux for nine months with a 100-pound weight loss.

PAST MEDICAL HISTORY: She has a history of hypertension and shortness of breath.

PAST SURGICAL HISTORY: Pertinent for cholecystectomy.

PSYCHOLOGICAL HISTORY: Negative.

SOCIAL HISTORY: She is single. She drinks alcohol once a week. She does not smoke.

FAMILY HISTORY: Pertinent for obesity and hypertension.

MEDICATIONS: Include Topamax 100 mg twice daily, Zoloft 100 mg twice daily, Abilify 5 mg daily, Motrin 800 mg daily, and a multivitamin.

ALLERGIES: She has no known drug allergies.

REVIEW OF SYSTEMS: Negative.

PHYSICAL EXAM: This is a pleasant female in no acute distress. Alert and oriented x 3. HEENT: Normocephalic, atraumatic. Extraocular muscles intact, nonicteric sclerae. Chest is clear to auscultation bilaterally. Cardiovascular is normal sinus rhythm. Abdomen is obese, soft, nontender and nondistended. Extremities show no edema, clubbing or cyanosis.

ASSESSMENT/PLAN: This is a 34-year-old female with a BMI of 43 who is interested in surgical weight via the gastric bypass as opposed to Lap-Band. Olivia Smith will be asking for a letter of medical necessity from Dr. Andrew Johnson. She will also see my nutritionist and social worker and have an upper endoscopy. Once this is completed, we will submit her to her insurance company for approval.
"""

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("summarizer_clinical_laymen_pipeline", "en", "clinical/models")

val text = """
Olivia Smith was seen in my office for evaluation for elective surgical weight loss on October 6, 2008. Olivia Smith is a 34-year-old female with a BMI of 43. She is 5'6" tall and weighs 267 pounds. She is motivated to attempt surgical weight loss because she has been overweight for over 20 years and wants to have more energy and improve her self-image. She is not only affected physically, but also socially by her weight. When she loses weight she always regains it and she always gains back more weight than she has lost. At one time, she lost 100 pounds and gained the weight back within a year. She has tried numerous commercial weight loss programs including Weight Watcher's for four months in 1992 with 15-pound weight loss, RS for two months in 1990 with six-pound weight loss, Slim Fast for six weeks in 2004 with eight-pound weight loss, an exercise program for two months in 2007 with a five-pound weight loss, Atkin's Diet for three months in 2008 with a ten-pound weight loss, and Dexatrim for one month in 2005 with a five-pound weight loss. She has also tried numerous fat reduction or fad diets. She was on Redux for nine months with a 100-pound weight loss.

PAST MEDICAL HISTORY: She has a history of hypertension and shortness of breath.

PAST SURGICAL HISTORY: Pertinent for cholecystectomy.

PSYCHOLOGICAL HISTORY: Negative.

SOCIAL HISTORY: She is single. She drinks alcohol once a week. She does not smoke.

FAMILY HISTORY: Pertinent for obesity and hypertension.

MEDICATIONS: Include Topamax 100 mg twice daily, Zoloft 100 mg twice daily, Abilify 5 mg daily, Motrin 800 mg daily, and a multivitamin.

ALLERGIES: She has no known drug allergies.

REVIEW OF SYSTEMS: Negative.

PHYSICAL EXAM: This is a pleasant female in no acute distress. Alert and oriented x 3. HEENT: Normocephalic, atraumatic. Extraocular muscles intact, nonicteric sclerae. Chest is clear to auscultation bilaterally. Cardiovascular is normal sinus rhythm. Abdomen is obese, soft, nontender and nondistended. Extremities show no edema, clubbing or cyanosis.

ASSESSMENT/PLAN: This is a 34-year-old female with a BMI of 43 who is interested in surgical weight via the gastric bypass as opposed to Lap-Band. Olivia Smith will be asking for a letter of medical necessity from Dr. Andrew Johnson. She will also see my nutritionist and social worker and have an upper endoscopy. Once this is completed, we will submit her to her insurance company for approval.
"""

val result = pipeline.fullAnnotate(text)
```
</div>


## Results

```bash
This is a clinical note about a 34-year-old woman who is interested in having weight loss surgery. She has been overweight for over 20 years and wants to have more energy and improve her self-image. She has tried many diets and weight loss programs, but has not been successful in keeping the weight off. She has a history of hypertension and shortness of breath, but is not allergic to any medications. She will have an upper endoscopy and will be contacted by a nutritionist and social worker. The plan is to have her weight loss surgery through the gastric bypass, rather than Lap-Band.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|summarizer_clinical_laymen_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|929.3 MB|

## Included Models

- DocumentAssembler
- MedicalSummarizer