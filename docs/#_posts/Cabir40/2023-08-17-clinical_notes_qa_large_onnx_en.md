---
layout: model
title: Medical Question Answering on Clinical Notes (Large - ONNX)
author: John Snow Labs
name: clinical_notes_qa_large_onnx
date: 2023-08-17
tags: [licensed, clinical, en, question_answering, onnx]
task: Question Answering
language: en
edition: Healthcare NLP 5.0.1
spark_version: 3.0
supported: true
engine: onnx
annotator: MedicalQuestionAnswering
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is capable of open-book question answering on Medical Notes.

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/MEDICAL_QA_CLINICAL_NOTES/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/31.Medical_Question_Answering.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_notes_qa_large_onnx_en_5.0.1_3.0_1692290656229.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_notes_qa_large_onnx_en_5.0.1_3.0_1692290656229.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = MultiDocumentAssembler()\
    .setInputCols("question", "context")\
    .setOutputCols("document_question", "document_context")

med_qa  = MedicalQuestionAnswering().pretrained("clinical_notes_qa_large_onnx", "en", "clinical/models")\
    .setInputCols(["document_question", "document_context"])\
    .setCustomPrompt("Context: {context} \n Question: {question} \n Answer: ")\
    .setOutputCol("answer")\

pipeline = Pipeline(stages=[document_assembler, med_qa])

note_text = "Patient with a past medical history of hypertension for 15 years.\n(Medical Transcription Sample Report)\nHISTORY OF PRESENT ILLNESS:\nThe patient is a 74-year-old white woman who has a past medical history of hypertension for 15 years, history of CVA with no residual hemiparesis and uterine cancer with pulmonary metastases, who presented for evaluation of recent worsening of the hypertension. According to the patient, she had stable blood pressure for the past 12-15 years on 10 mg of lisinopril."

question = "What is the primary issue reported by patient?"

data = spark.createDataFrame([[question, note_text]]).toDF("question", "context")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new MultiDocumentAssembler()
    .setInputCols("question", "context")
    .setOutputCols("document_question", "document_context")

val med_qa = MedicalQuestionAnswering.pretrained("clinical_notes_qa_large_onnx", "en", "clinical/models")
    .setInputCols(Array("document_question", "document_context"))
    .setOutputCol("answer")
    .setCustomPrompt("Context: {context} \n Question: {question} \n Answer: ")

val pipeline = new Pipeline().setStages(Array(document_assembler, med_qa))

note_text = "Patient with a past medical history of hypertension for 15 years.\n(Medical Transcription Sample Report)\nHISTORY OF PRESENT ILLNESS:\nThe patient is a 74-year-old white woman who has a past medical history of hypertension for 15 years, history of CVA with no residual hemiparesis and uterine cancer with pulmonary metastases, who presented for evaluation of recent worsening of the hypertension. According to the patient, she had stable blood pressure for the past 12-15 years on 10 mg of lisinopril."
question = "What is the primary issue reported by patient?"

val data = Seq( 
    (question, note_text))
    .toDS.toDF("question", "context")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------------------------------------------------------+
|result                                                       |
+-------------------------------------------------------------+
|[The primary issue reported by the patient is hypertension.] |
+-------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_notes_qa_large_onnx|
|Compatibility:|Healthcare NLP 5.0.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.0 GB|
|Case sensitive:|true|

## References

Trained on in-house curated dataset on clinical notes.

## Benchmarking

```bash
Rouge Score 61.1
```