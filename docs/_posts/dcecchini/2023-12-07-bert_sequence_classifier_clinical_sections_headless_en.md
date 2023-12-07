---
layout: model
title: Bert for Sequence Classification (Clinical Documents Sections, Headless)
author: John Snow Labs
name: bert_sequence_classifier_clinical_sections_headless
date: 2023-12-07
tags: [licensed, en, clinical, sections, tensorflow]
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

This is a BERT-based model for classification of clinical documents sections. This model is trained on clinical document sections without the section header in the text, e.g., when splitting the document with `ChunkSentenceSplitter` annotator with parameter `setInsertChunk=False`.

## Predicted Entities

`Complications and Risk Factors`, `Consultation and Referral`, `Diagnostic and Laboratory Data`, `Discharge Information`, `Habits`, `History`, `Patient Information`, `Procedures`, `Other`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_clinical_sections_headless_en_5.1.1_3.0_1701911612184.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_clinical_sections_headless_en_5.1.1_3.0_1701911612184.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequenceClassifier = medical.BertForSequenceClassification.load('bert_sequence_classifier_clinical_sections_headless', 'en', 'clinical/models')\
    .setInputCols(["document", 'token'])\
    .setOutputCol("prediction").setCaseSensitive(False)

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

val seq = BertForSequenceClassification.pretrained("bert_sequence_classifier_clinical_sections_headless", "en", "clinical/models")
.setInputCols(Array("token", "sentence"))
.setOutputCol("label")
.setCaseSensitive(True)

val pipeline = new Pipeline().setStages(Array(
documentAssembler,
sentenceDetector,
tokenizer,
seq))

val test_sentences = """It was a pleasure taking care of you! You came to us with 
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
nlu.load("en.classify.bert_sequence.clinical_sections_headless").predict("""It was a pleasure taking care of you! You came to us with 
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
|Model Name:|bert_sequence_classifier_clinical_sections_headless|
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
Complications and Risk Factors     0.9965    0.9870    0.9917      2000
     Consultation and Referral     0.8546    0.9235    0.8877      1216
Diagnostic and Laboratory Data     0.8587    0.9085    0.8829      2000
         Discharge Information     0.8177    0.6930    0.7502      2000
                        Habits     0.9431    0.9216    0.9322       306
                       History     0.9316    0.9405    0.9361      2000
                         Other     0.5750    0.9471    0.7156       170
           Patient Information     0.7817    0.7735    0.7776      2000
                    Procedures     0.9333    0.9375    0.9354      2000
```