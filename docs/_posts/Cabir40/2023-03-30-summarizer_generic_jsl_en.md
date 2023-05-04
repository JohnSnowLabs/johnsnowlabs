---
layout: model
title: Medical Text Summarization
author: John Snow Labs
name: summarizer_generic_jsl
date: 2023-03-30
tags: [licensed, en, clinical, text_summarization, tensorflow]
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


This model is a modified version of Flan-T5 (LLM) based summarization model that is finetuned with additional data curated by John Snow Labs. This model is further optimized by augmenting the training methodology, and dataset. It can generate summaries from clinical notes up to 512 tokens given the input text (max 1024 tokens)

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/MEDICAL_TEXT_SUMMARIZATION/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/32.Medical_Text_Summarization.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/summarizer_generic_jsl_en_4.3.2_3.0_1680192338463.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/summarizer_generic_jsl_en_4.3.2_3.0_1680192338463.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use


<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("documents")

med_summarizer  = MedicalSummarizer()\
    .pretrained("summarizer_generic_jsl", "en", "clinical/models")\
    .setInputCols("documents")\
    .setOutputCol("summary")\
    .setMaxNewTokens(100)\
    .setMaxTextLength(1024)
    
pipeline = Pipeline(stages=[document_assembler, med_summarizer])

text = """Patient with hypertension, syncope, and spinal stenosis - for recheck.
(Medical Transcription Sample Report)
SUBJECTIVE:
The patient is a 78-year-old female who returns for recheck. She has hypertension. She denies difficulty with chest pain, palpations, orthopnea, nocturnal dyspnea, or edema.
PAST MEDICAL HISTORY / SURGERY / HOSPITALIZATIONS:
Reviewed and unchanged from the dictation on 12/03/2003.
MEDICATIONS:
Atenolol 50 mg daily, Premarin 0.625 mg daily, calcium with vitamin D two to three pills daily, multivitamin daily, aspirin as needed, and TriViFlor 25 mg two pills daily. She also has Elocon cream 0.1% and Synalar cream 0.01% that she uses as needed for rash.
ALLERGIES:..."""

data = spark.createDataFrame([[text]]).toDF("text")

pipeline.fit(data).transform(data)
```

```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("documents")

val med_summarizer  = MedicalSummarizer()
    .pretrained("summarizer_generic_jsl", "en", "clinical/models")
    .setInputCols("documents")
    .setOutputCol("summary")
    .setMaxNewTokens(100)

val pipeline = new Pipeline().setStages(Array(document_assembler, med_summarizer))

val text = """Patient with hypertension, syncope, and spinal stenosis - for recheck.
(Medical Transcription Sample Report)
SUBJECTIVE:
The patient is a 78-year-old female who returns for recheck. She has hypertension. She denies difficulty with chest pain, palpations, orthopnea, nocturnal dyspnea, or edema.
PAST MEDICAL HISTORY / SURGERY / HOSPITALIZATIONS:
Reviewed and unchanged from the dictation on 12/03/2003.
MEDICATIONS:
Atenolol 50 mg daily, Premarin 0.625 mg daily, calcium with vitamin D two to three pills daily, multivitamin daily, aspirin as needed, and TriViFlor 25 mg two pills daily. She also has Elocon cream 0.1% and Synalar cream 0.01% that she uses as needed for rash.
ALLERGIES:..."""

val data = Seq(text).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```

</div>

## Results

```bash
"
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[recheck. A 78-year-old female patient returns for recheck due to hypertension, syncope, and spinal stenosis. She has a history of heart failure, myocardial infarction, lymphoma, and asthma. She has been prescribed Atenolol, Premarin, calcium with vitamin D, multivitamin, aspirin, and TriViFlor. She has also been prescribed El]|
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|summarizer_generic_jsl|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|920.0 MB|

## Benchmarking
### Benchmark on Samsum Dataset

| model_name | model_size | rouge | bleu | bertscore_precision | bertscore_recall: | bertscore_f1 |
|--|--|--|--|--|--|--|
philschmid/flan-t5-base-samsum | 240M | 0.2734 | 0.1813 | 0.8938 | 0.9133 | 0.9034 | 
linydub/bart-large-samsum | 500M | 0.3060 | 0.2168 | 0.8961 | 0.9065 | 0.9013 |
philschmid/bart-large-cnn-samsum | 500M | 0.3794 | 0.1262 | 0.8599 | 0.9153 | 0.8867 | 
transformersbook/pegasus-samsum | 570M | 0.3049 | 0.1543 | 0.8942 | 0.9183 | 0.9061 | 
summarizer_generic_jsl | 240M | 0.2703 | 0.1932 | 0.8944 | 0.9161 | 0.9051 |

