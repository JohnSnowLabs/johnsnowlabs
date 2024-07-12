---
layout: model
title: Detect SNOMED Terms
author: John Snow Labs
name: ner_snomed_term
date: 2024-02-13
tags: [ner, en, clinical, licensed, snomed]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Name Entity Recognition(NER) model extracts SNOMED terms from clinical text. It has been trained using the `embeddings_clinical` embeddings model.

## Predicted Entities

`snomed_term`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_snomed_term_en_5.2.1_3.0_1707823546698.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_snomed_term_en_5.2.1_3.0_1707823546698.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence") 

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("embeddings")

ner = MedicalNerModel.pretrained("ner_snomed_term", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

nlpPipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            embeddings,
                            ner,
                            ner_converter])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

text_list = ["The patient was diagnosed with acute appendicitis and scheduled for immediate surgery.",
"Due to experiencing chronic pain the patient was referred to a fibromyalgia specialist for further evaluation.",
"His hypertension is currently managed with a combination of lifestyle modifications and medication.",
"The child was brought in with symptoms of acute otitis including ear pain and fever.",
"Laboratory tests indicate the individual has hyperthyroidism requiring further endocrinological assessment.",
"The radiograph showed evidence of a distal radius fracture from a recent fall."]

data = spark.createDataFrame(text_list, StringType()).toDF("text")

result = model.transform(data)
```
```scala
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_snomed_term", "en", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")

val nerConverter = new NerConverter()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline()
  .setStages(Array(documentAssembler, sentenceDetector, tokenizer, embeddings, ner, nerConverter))

val textList = Seq(
  "The patient was diagnosed with acute appendicitis and scheduled for immediate surgery.",
  "Due to experiencing chronic pain the patient was referred to a fibromyalgia specialist for further evaluation.",
  "His hypertension is currently managed with a combination of lifestyle modifications and medication.",
  "The child was brought in with symptoms of acute otitis including ear pain and fever.",
  "Laboratory tests indicate the individual has hyperthyroidism requiring further endocrinological assessment.",
  "The radiograph showed evidence of a distal radius fracture from a recent fall."
)

val data = Seq(textList).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------+-----------+
|chunk             |ner_label  |
+------------------+-----------+
|acute appendicitis|snomed_term|
|chronic pain      |snomed_term|
|fibromyalgia      |snomed_term|
|hypertension      |snomed_term|
|otitis            |snomed_term|
|ear pain          |snomed_term|
|hyperthyroidism   |snomed_term|
|radiograph        |snomed_term|
|radius fracture   |snomed_term|
+------------------+-----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_snomed_term|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.6 MB|

## References

In-house annotated dataset

## Benchmarking

```bash
label          precision  recall  f1-score  support 
B-snomed_term  0.87       0.88    0.87      5210    
I-snomed_term  0.85       0.91    0.88      4922    
micro-avg      0.86       0.89    0.88      10132   
macro-avg      0.86       0.89    0.88      10132   
weighted-avg   0.86       0.89    0.88      10132   
```
