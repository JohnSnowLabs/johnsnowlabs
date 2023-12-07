---
layout: model
title: Bert for Sequence Classification (Clinical Documents Sections)
author: John Snow Labs
name: bert_sequence_classifier_clinical_sections
date: 2023-12-07
tags: [clinical, en, licensed, section, tensorflow]
task: Text Classification
language: en
edition: Healthcare NLP 5.1.1
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a BERT-based model for classification of clinical documents sections. This model performs better when the section header is present in the text, e.g., when splitting the document with `ChunkSentenceSplitter` annotator with parameter `setInsertChunk=True`.

## Predicted Entities

`Complications and Risk Factors`, `Consultation and Referral`, `Diagnostic and Laboratory Data`, `Discharge Information`, `Habits`, `History`, `Patient Information`, `Procedures`, `Other`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_clinical_sections_en_5.1.1_3.0_1701907733014.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_clinical_sections_en_5.1.1_3.0_1701907733014.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler() \
    .setInputCol('text') \
    .setOutputCol('document')

tokenizer = nlp.Tokenizer() \
    .setInputCols(['document']) \
    .setOutputCol('token')

sequenceClassifier = medical.BertForSequenceClassification.load('bert_sequence_classifier_clinical_sections', 'en', 'clinical/models')\
    .setInputCols(["document", 'token'])\
    .setOutputCol("prediction").setCaseSensitive(False)

pipeline = nlp.Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequenceClassifier  
])

example_df = spark.createDataFrame(
        [["""Discharge Instructions:
It was a pleasure taking care of you! You came to us with 
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


result = spark_model.transform(example_df)
result.select("prediction.result").show(truncate=False)


```
```scala
val documentAssembler = new DocumentAssembler()
.setInputCol("text")
.setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained()
.setInputCols(Array("document"))
.setOutputCol("sentence")

val tokenizer = new Tokenizer()
.setInputCols("sentence")
.setOutputCol("token")

val seq = BertForSequenceClassification.pretrained("bert_sequence_classifier_clinical_sections", "en", "clinical/models")
.setInputCols(Array("token", "sentence"))
.setOutputCol("label")
.setCaseSensitive(True)

val pipeline = new Pipeline().setStages(Array(
documentAssembler,
sentenceDetector,
tokenizer,
seq))

val test_sentences = """Discharge Instructions:
It was a pleasure taking care of you! You came to us with 
stomach pain and worsening distension. While you were here we 
did a paracentesis to remove 1.5L of fluid from your belly. We 
also placed you on you 40 mg of Lasix and 50 mg of Aldactone to 
help you urinate the excess fluid still in your belly. As we 
discussed, everyone has a different dose of lasix required to 
make them urinate and it's likely that you weren't taking a high 
enough dose. Please take these medications daily to keep excess 
fluid off and eat a low salt diet. You will follow up with Dr. 
___ in liver clinic and from there have your colonoscopy 
and EGD scheduled. """"

val example = Seq(test_sentences).toDS.toDF("text")

val result = pipeline.fit(example).transform(example)

```

{:.nlu-block}
```python
import nlu
nlu.load("en.classify.bert_sequence.clinical_sections").predict("""Discharge Instructions:
It was a pleasure taking care of you! You came to us with 
stomach pain and worsening distension. While you were here we 
did a paracentesis to remove 1.5L of fluid from your belly. We 
also placed you on you 40 mg of Lasix and 50 mg of Aldactone to 
help you urinate the excess fluid still in your belly. As we 
discussed, everyone has a different dose of lasix required to 
make them urinate and it's likely that you weren't taking a high 
enough dose. Please take these medications daily to keep excess 
fluid off and eat a low salt diet. You will follow up with Dr. 
___ in liver clinic and from there have your colonoscopy 
and EGD scheduled. """)

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
|Model Name:|bert_sequence_classifier_clinical_sections|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[class]|
|Language:|en|
|Size:|406.6 MB|
|Case sensitive:|false|
|Max sentence length:|512|

## References

In-house annotation of clinical documents.

## Sample text from the training dataset

Discharge Instructions:
It was a pleasure taking care of you! You came to us with 
stomach pain and worsening distension. While you were here we 
did a paracentesis to remove 1.5L of fluid from your belly. We 
also placed you on you 40 mg of Lasix and 50 mg of Aldactone to 
help you urinate the excess fluid still in your belly. As we 
discussed, everyone has a different dose of lasix required to 
make them urinate and it's likely that you weren't taking a high 
enough dose. Please take these medications daily to keep excess 
fluid off and eat a low salt diet. You will follow up with Dr. 
___ in liver clinic and from there have your colonoscopy 
and EGD scheduled.

## Benchmarking

```bash
                                precision    recall  f1-score   support

Complications and Risk Factors     0.9965    0.9845    0.9904      2000
     Consultation and Referral     0.5187    0.9342    0.6671      1216
Diagnostic and Laboratory Data     0.4736    0.8420    0.6062      2000
         Discharge Information     0.7500    0.5355    0.6249      2000
                        Habits     0.9701    0.8497    0.9059       306
                       History     0.7528    0.9730    0.8489      2000
                         Other     0.9314    0.9588    0.9449       170
           Patient Information     0.2921    0.0390    0.0688      2000
                    Procedures     0.9230    0.5755    0.7090      2000
```