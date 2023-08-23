---
layout: model
title: Summarize clinical notes (augmented)
author: John Snow Labs
name: summarizer_clinical_jsl_augmented
date: 2023-03-30
tags: [licensed, clinical, en, summarization, tensorflow]
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

This model is a modified version of Flan-T5 (LLM) based summarization model that is at first finetuned with natural instructions and then finetuned with clinical notes, encounters, critical care notes, discharge notes, reports, curated  by John Snow Labs. This model is further optimized by augmenting the training methodology, and dataset. It can generate summaries from clinical notes up to 512 tokens given the input text (max 1024 tokens).

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/MEDICAL_TEXT_SUMMARIZATION/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/32.Medical_Text_Summarization.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/summarizer_clinical_jsl_augmented_en_4.3.2_3.0_1680203312371.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/summarizer_clinical_jsl_augmented_en_4.3.2_3.0_1680203312371.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

summarizer = MedicalSummarizer()\
    .pretrained("summarizer_clinical_jsl_augmented", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("summary")\
    .setMaxTextLength(512)\
    .setMaxNewTokens(512)

pipeline = Pipeline(stages=[document, summarizer])

text = """Patient with hypertension, syncope, and spinal stenosis - for recheck.
(Medical Transcription Sample Report)
SUBJECTIVE:
The patient is a 78-year-old female who returns for recheck. She has hypertension. She denies difficulty with chest pain, palpations, orthopnea, nocturnal dyspnea, or edema.
PAST MEDICAL HISTORY / SURGERY / HOSPITALIZATIONS:
Reviewed and unchanged from the dictation on 12/03/2003.
MEDICATIONS:
Atenolol 50 mg daily, Premarin 0.625 mg daily, calcium with vitamin D two to three pills daily, multivitamin daily, aspirin as needed, and TriViFlor 25 mg two pills daily. She also has Elocon cream 0.1% and Synalar cream 0.01% that she uses as needed for rash."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val summarizer = MedicalSummarizer()
    .pretrained("summarizer_clinical_jsl_augmented", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("summary")
    .setMaxTextLength(512)
    .setMaxNewTokens(512)

val pipeline = new Pipeline().setStages(Array(document, summarizer))
                                        
val text = """Patient with hypertension, syncope, and spinal stenosis - for recheck.
(Medical Transcription Sample Report)
SUBJECTIVE:
The patient is a 78-year-old female who returns for recheck. She has hypertension. She denies difficulty with chest pain, palpations, orthopnea, nocturnal dyspnea, or edema.
PAST MEDICAL HISTORY / SURGERY / HOSPITALIZATIONS:
Reviewed and unchanged from the dictation on 12/03/2003.
MEDICATIONS:
Atenolol 50 mg daily, Premarin 0.625 mg daily, calcium with vitamin D two to three pills daily, multivitamin daily, aspirin as needed, and TriViFlor 25 mg two pills daily. She also has Elocon cream 0.1% and Synalar cream 0.01% that she uses as needed for rash."""

val data = Seq(text).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
A 78-year-old female with hypertension, syncope, and spinal stenosis returns for a recheck. She denies difficulty with chest pain, palpations, orthopnea, nocturnal dyspnea, or edema. Her medications include Atenolol, Premarin, calcium with vitamin D, multivitamin, aspirin, and TriViFlor. She also has Elocon cream and Synalar cream for rash.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|summarizer_clinical_jsl_augmented|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|920.0 MB|

## Benchmarkings

### Benchmark on MtSamples Summarization Dataset : 

| model_name | model_size | rouge | bleu | bertscore_precision | bertscore_recall: | bertscore_f1 |
|--|--|--|--|--|--|--|
philschmid/flan-t5-base-samsum | 250M | 0.1919 | 0.1124 | 0.8409 | 0.8964 | 0.8678 | 
linydub/bart-large-samsum | 500M | 0.1586 | 0.0732 | 0.8747 | 0.8184 | 0.8456 | 
philschmid/bart-large-cnn-samsum |  500M | 0.2170 | 0.1299 | 0.8846 | 0.8436 | 0.8636 |
transformersbook/pegasus-samsum | 500M | 0.1924 | 0.0965 | 0.8920 | 0.8149 | 0.8517 | 
summarizer_clinical_jsl | 250M | 0.4836 | 0.4188 | 0.9041 | 0.9374 | 0.9204 | 
summarizer_clinical_jsl_augmented | 250M | 0.5119 | 0.4545 | 0.9282 | 0.9526 | 0.9402 |

### Benchmark on MIMIC Summarization Dataset :

| model_name | model_size | rouge | bleu | bertscore_precision | bertscore_recall: | bertscore_f1 |
|--|--|--|--|--|--|--|
philschmid/flan-t5-base-samsum | 250M | 0.1910 | 0.1037 | 0.8708 | 0.9056 | 0.8879 | 
linydub/bart-large-samsum | 500M | 0.1252 | 0.0382 | 0.8933 | 0.8440 | 0.8679 |
philschmid/bart-large-cnn-samsum | 500M | 0.1795 | 0.0889 | 0.9172 | 0.8978 | 0.9074 | 
transformersbook/pegasus-samsum | 570M | 0.1425 | 0.0582 | 0.9171 | 0.8682 | 0.8920 |
summarizer_clinical_jsl | 250M | 0.395 | 0.2962 | 0.895 | 0.9316 | 0.913 | 
summarizer_clinical_jsl_augmented | 250M | 0.3964 | 0.307 | 0.9109 | 0.9452 | 0.9227 |


![Benchmark Summary](https://github.com/JohnSnowLabs/jsl-private-projects/blob/llm_benchmarks/internal_projects/LLM_Experiments/jsl-summarization-benchmarks.png?raw=true)

## References

Trained on in-house curated dataset
