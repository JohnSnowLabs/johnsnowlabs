---
layout: model
title: Social Determinants of Healthcare for Mental Health Classifier ONNX
author: John Snow Labs
name: bert_sequence_classifier_sdoh_mental_health_onnx
date: 2025-09-12
tags: [sdoh, en, clinical, social_determinants_of_heathcare, public_health, mental_health, licensed, onnx]
task: Text Classification
language: en
edition: Healthcare NLP 6.1.1
spark_version: 3.0
supported: true
engine: onnx
annotator: MedicalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The Mental Health classifier employs [MedicalBertForSequenceClassification embeddings](https://sparknlp.org/2022/07/18/biobert_pubmed_base_cased_v1.2_en_3_0.html) within a robust classifier architecture. Trained on a diverse dataset, this model provides accurate label assignments and confidence scores for its predictions. The primary goal of this model is to categorize text into two key labels: `Mental_Disorder` and `No_Or_Not_Mentioned`.

- `Mental_Disorder`: It encompasses a wide range of mental health conditions that affect a person's mood, thinking, behavior, and overall psychological well-being.

- `No_Or_Not_Mentioned`: The patient doesn’t have mental health problems or it is not mentioned in the clinical notes.

## Predicted Entities

`Mental_Disorder`, `No_Or_Not_Mentioned`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_sdoh_mental_health_onnx_en_6.1.1_3.0_1757687035265.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_sdoh_mental_health_onnx_en_6.1.1_3.0_1757687035265.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import DocumentAssembler
from sparknlp_jsl.annotator import SentenceDetectorDLModel, MedicalBertForTokenClassifier
from sparknlp.annotator import Tokenizer, NerConverter
from pyspark.ml import Pipeline

document_assembler = (
    DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

sentenceDetector = (
    SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(["document"])
    .setOutputCol("sentence")
)

tokenizer = (
    Tokenizer()
    .setInputCols(["sentence"])
    .setOutputCol("token")
)

token_classifier = (
    MedicalBertForTokenClassifier.pretrained(
        "bert_sequence_classifier_sdoh_mental_health_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "sentence"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
    NerConverter()
    .setInputCols(["sentence", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = Pipeline(stages=[
    document_assembler,
    sentenceDetector,
    tokenizer,
    token_classifier,
    ner_converter
])

sample_texts= [
  ["John, a 45-year-old man, was diagnosed with bipolar disorder, a mental disorder characterized by alternating periods of elevated mood (mania) and depression. His treatment plan involved a combination of mood stabilizing medication and regular therapy sessions. With proper management and support, John learned to better understand and cope with his condition, leading to improved stability and overall well-being."],
  ["Lisa, a 28-year-old woman, was diagnosed with generalized anxiety disorder (GAD), a mental disorder characterized by excessive worry and persistent anxiety."],
  ["Mark, a 35-year-old man, sought medical help for symptoms of attention-deficit/hyperactivity disorder (ADHD), a neurodevelopmental disorder characterized by inattention, hyperactivity, and impulsivity. After a comprehensive evaluation, Mark was diagnosed with ADHD, and his healthcare provider recommended a multimodal treatment approach. "],
  ["Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy."],
  ["She reported occasional respiratory symptoms, such as wheezing and shortness of breath, but had no signs of a mental disorder. Her healthcare provider assessed her lung function, reviewed her medication regimen, and provided personalized asthma education. "],
  ["During the appointment, her healthcare provider assessed her joint function, reviewed her medication regimen, and discussed the importance of adherence. They also discussed the benefits of regular exercise, maintaining a healthy weight, and using assistive devices when needed to support Anna's joint health. "],       
]

data = spark.createDataFrame(sample_texts).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler = (
    nlp.DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

sentenceDetector = (
    nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(["document"])
    .setOutputCol("sentence")
)

tokenizer = (
    nlp.Tokenizer()
    .setInputCols(["sentence"])
    .setOutputCol("token")
)

token_classifier = (
    medical.MedicalBertForTokenClassifier.pretrained(
        "bert_sequence_classifier_sdoh_mental_health_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "sentence"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
    nlp.NerConverter()
    .setInputCols(["sentence", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    sentenceDetector,
    tokenizer,
    token_classifier,
    ner_converter
])

sample_texts= [
  ["John, a 45-year-old man, was diagnosed with bipolar disorder, a mental disorder characterized by alternating periods of elevated mood (mania) and depression. His treatment plan involved a combination of mood stabilizing medication and regular therapy sessions. With proper management and support, John learned to better understand and cope with his condition, leading to improved stability and overall well-being."],
  ["Lisa, a 28-year-old woman, was diagnosed with generalized anxiety disorder (GAD), a mental disorder characterized by excessive worry and persistent anxiety."],
  ["Mark, a 35-year-old man, sought medical help for symptoms of attention-deficit/hyperactivity disorder (ADHD), a neurodevelopmental disorder characterized by inattention, hyperactivity, and impulsivity. After a comprehensive evaluation, Mark was diagnosed with ADHD, and his healthcare provider recommended a multimodal treatment approach. "],
  ["Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy."],
  ["She reported occasional respiratory symptoms, such as wheezing and shortness of breath, but had no signs of a mental disorder. Her healthcare provider assessed her lung function, reviewed her medication regimen, and provided personalized asthma education. "],
  ["During the appointment, her healthcare provider assessed her joint function, reviewed her medication regimen, and discussed the importance of adherence. They also discussed the benefits of regular exercise, maintaining a healthy weight, and using assistive devices when needed to support Anna's joint health. "],       
]

data = spark.createDataFrame(sample_texts).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotators._
import org.apache.spark.ml.Pipeline
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetectorDLModel()
  .pretrained("sentence_detector_dl","xx")
  .setInputCols(["document"])
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val tokenClassifier = MedicalBertForTokenClassifier
  .pretrained("bert_sequence_classifier_sdoh_mental_health_onnx", "en", "clinical/models")
  .setInputCols("token", "document")
  .setOutputCol("ner")
  .setCaseSensitive(true)

val nerConverter = new NerConverter()
  .setInputCols("document", "token", "ner")
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    tokenClassifier,
    nerConverter
  ))

val data = Seq(Array("John, a 45-year-old man, was diagnosed with bipolar disorder, a mental disorder characterized by alternating periods of elevated mood (mania) and depression. His treatment plan involved a combination of mood stabilizing medication and regular therapy sessions. With proper management and support, John learned to better understand and cope with his condition, leading to improved stability and overall well-being.",
                     "Lisa, a 28-year-old woman, was diagnosed with generalized anxiety disorder (GAD), a mental disorder characterized by excessive worry and persistent anxiety.",
                     "Mark, a 35-year-old man, sought medical help for symptoms of attention-deficit/hyperactivity disorder (ADHD), a neurodevelopmental disorder characterized by inattention, hyperactivity, and impulsivity. After a comprehensive evaluation, Mark was diagnosed with ADHD, and his healthcare provider recommended a multimodal treatment approach. ",
                     "Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy.",
                     "She reported occasional respiratory symptoms, such as wheezing and shortness of breath, but had no signs of a mental disorder. Her healthcare provider assessed her lung function, reviewed her medication regimen, and provided personalized asthma education. ",
                     "During the appointment, her healthcare provider assessed her joint function, reviewed her medication regimen, and discussed the importance of adherence. They also discussed the benefits of regular exercise, maintaining a healthy weight, and using assistive devices when needed to support Anna's joint health. ",
)).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+----------------------------------------------------------------------------------------------------+---------------------+
|                                                                                                text|               result|
+----------------------------------------------------------------------------------------------------+---------------------+
|John, a 45-year-old man, was diagnosed with bipolar disorder, a mental disorder characterized by ...|    [Mental_Disorder]|
|Lisa, a 28-year-old woman, was diagnosed with generalized anxiety disorder (GAD), a mental disord...|    [Mental_Disorder]|
|Mark, a 35-year-old man, sought medical help for symptoms of attention-deficit/hyperactivity diso...|    [Mental_Disorder]|
|Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatm...|[No_Or_Not_Mentioned]|
|She reported occasional respiratory symptoms, such as wheezing and shortness of breath, but had n...|[No_Or_Not_Mentioned]|
|During the appointment, her healthcare provider assessed her joint function, reviewed her medicat...|[No_Or_Not_Mentioned]|
+----------------------------------------------------------------------------------------------------+---------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_sdoh_mental_health_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|