---
layout: model
title: Bert for Sequence Classification (Clinical Documents Sections, Headless) ONNX
author: John Snow Labs
name: bert_sequence_classifier_clinical_sections_headless_onnx
date: 2025-09-12
tags: [clinical, sections, en, licensed, onnx]
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

This is a BERT-based model for classification of clinical documents sections. This model is trained on clinical document sections without the section header in the text, e.g., when splitting the document with `ChunkSentenceSplitter` annotator with parameter `setInsertChunk=False`.

## Predicted Entities

`Consultation and Referral`, `Habits`, `Complications and Risk Factors`, `Diagnostic and Laboratory Data`, `Discharge Information`, `History`, `Impression`, `Patient Information`, `Procedures`, `Other`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_clinical_sections_headless_onnx_en_6.1.1_3.0_1757683263339.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_clinical_sections_headless_onnx_en_6.1.1_3.0_1757683263339.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequence_classifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_clinical_sections_headless_onnx", "en", "clinical/models")\
  .setInputCols(["document", "token"])\
  .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])
example_df = spark.createDataFrame(
        [["""It was a pleasure taking care of you! You came to us with 
stomach pain and worsening distension. While you were here we 
did a paracentesis to remove 1.5L of fluid from your belly. We 
also placed you on you 40 mg of Lasix and 50 mg of Aldactone to 
help you urinate the excess fluid still in your belly. As we 
discussed, everyone has a different dose of lasix required to 
make them urinate and it's likely that you weren't taking a high 
enough dose. Please take these medications daily to keep excess 
fluid off and eat a low salt diet. You will follow up with Dr. 
___ in liver clinic and from there have your colonoscopy 
and EGD scheduled. """]]).toDF("text")

model = pipeline.fit(example_df)
result = model.transform(example_df)
```

{:.jsl-block}
```python
document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

sequenceClassifier = medical.BertForSequenceClassification.pretrained("bert_sequence_classifier_clinical_sections_headless_onnx", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])

example_df = spark.createDataFrame(
        [["""It was a pleasure taking care of you! You came to us with 
stomach pain and worsening distension. While you were here we 
did a paracentesis to remove 1.5L of fluid from your belly. We 
also placed you on you 40 mg of Lasix and 50 mg of Aldactone to 
help you urinate the excess fluid still in your belly. As we 
discussed, everyone has a different dose of lasix required to 
make them urinate and it's likely that you weren't taking a high 
enough dose. Please take these medications daily to keep excess 
fluid off and eat a low salt diet. You will follow up with Dr. 
___ in liver clinic and from there have your colonoscopy 
and EGD scheduled. """]]).toDF("text")

model = pipeline.fit(example_df)
result = model.transform(example_df)

```
```scala
val document_assembler = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")

val tokenizer = new Tokenizer() 
    .setInputCols(Array("document")) 
    .setOutputCol("token")

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_clinical_sections_headless_onnx", "en", "clinical/models")
  .setInputCols(Array("document","token"))
  .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))
val data = Seq("""It was a pleasure taking care of you! You came to us with 
stomach pain and worsening distension. While you were here we 
did a paracentesis to remove 1.5L of fluid from your belly. We 
also placed you on you 40 mg of Lasix and 50 mg of Aldactone to 
help you urinate the excess fluid still in your belly. As we 
discussed, everyone has a different dose of lasix required to 
make them urinate and it's likely that you weren't taking a high 
enough dose. Please take these medications daily to keep excess 
fluid off and eat a low salt diet. You will follow up with Dr. 
___ in liver clinic and from there have your colonoscopy 
and EGD scheduled. """).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+-----------------------+
|result                 |
+-----------------------+
|[Discharge Information]|
+-----------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_clinical_sections_headless_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|