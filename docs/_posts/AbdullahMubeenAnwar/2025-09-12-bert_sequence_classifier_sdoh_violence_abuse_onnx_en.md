---
layout: model
title: Social Determinants of Healthcare for Violence and Abuse Classifier ONNX
author: John Snow Labs
name: bert_sequence_classifier_sdoh_violence_abuse_onnx
date: 2025-09-12
tags: [sdoh, en, clinical, social_determinants_of_heathcare, public_health, violence, abuse, licensed, onnx]
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

The Violence and Abuse classifier employs [MedicalBertForSequenceClassification embeddings](https://sparknlp.org/2022/07/18/biobert_pubmed_base_cased_v1.2_en_3_0.html) within a robust classifier architecture. Trained on a diverse dataset, this model provides accurate label assignments and confidence scores for its predictions. The primary goal of this model is to categorize text into four key labels: `Domestic_Violence_Abuse`, `Personal_Violence_Abuse`, `No_Violence_Abuse` and `Unknown`.

- `Domestic_Violence_Abuse`:This category refers to a pattern of behavior in any relationship that is aimed at gaining or maintaining power and control over an intimate partner or family member.

- `Personal_Violence_Abuse`: This category encompasses any form of violence or abuse that is directed towards an individual, whether admitted by the perpetrator or recognized by the victim.

- `No_Violence_Abuse`: This category denotes the complete absence of violence and abuse in any form.

- `Unknown`: This category covers when the nature or type of violence or abuse within a given text cannot be clearly identified or defined.

## Predicted Entities

`Domestic_Violence_Abuse`, `Personal_Violence_Abuse`, `No_Violence_Abuse`, `Unknown`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_sdoh_violence_abuse_onnx_en_6.1.1_3.0_1757687107061.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_sdoh_violence_abuse_onnx_en_6.1.1_3.0_1757687107061.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

sequence_classifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_sdoh_violence_abuse_onnx", "en", "clinical/models")\
  .setInputCols(["document", "token"])\
  .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])

sample_texts = [
                ["Repeated visits for fractures, with vague explanations suggesting potential family-related trauma."],
                ["Patient presents with multiple bruises in various stages of healing, suggestive of repeated physical abuse."],
                ["There are no reported instances or documented episodes indicating the patient poses a risk of violence."] ,
                ["Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy."]
                ]

data = spark.createDataFrame(sample_texts).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```

{:.jsl-block}
```python
document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

sequenceClassifier = medical.BertForSequenceClassification.pretrained("bert_sequence_classifier_sdoh_violence_abuse_onnx", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])

sample_texts = [
                ["Repeated visits for fractures, with vague explanations suggesting potential family-related trauma."],
                ["Patient presents with multiple bruises in various stages of healing, suggestive of repeated physical abuse."],
                ["There are no reported instances or documented episodes indicating the patient poses a risk of violence."] ,
                ["Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy."]
                ]

data = spark.createDataFrame(sample_texts).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

```
```scala
val document_assembler = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")

val tokenizer = new Tokenizer() 
    .setInputCols(Array("document")) 
    .setOutputCol("token")

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_sdoh_violence_abuse_onnx", "en", "clinical/models")
  .setInputCols(Array("document","token"))
  .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))
val data = Seq(Array("Repeated visits for fractures, with vague explanations suggesting potential family-related trauma.",
                     "Patient presents with multiple bruises in various stages of healing, suggestive of repeated physical abuse.",
                     "There are no reported instances or documented episodes indicating the patient poses a risk of violence." ,
                     "Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy.",
                    )).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+----------------------------------------------------------------------------------------------------+-------------------------+
|                                                                                                text|                   result|
+----------------------------------------------------------------------------------------------------+-------------------------+
|  Repeated visits for fractures, with vague explanations suggesting potential family-related trauma.|[Domestic_Violence_Abuse]|
|Patient presents with multiple bruises in various stages of healing, suggestive of repeated physi...|[Personal_Violence_Abuse]|
|There are no reported instances or documented episodes indicating the patient poses a risk of vio...|      [No_Violence_Abuse]|
|Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatm...|                [Unknown]|
+----------------------------------------------------------------------------------------------------+-------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_sdoh_violence_abuse_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|