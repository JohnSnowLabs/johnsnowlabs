---
layout: model
title: Extract Mentions of Response to Cancer Treatment (langtest)
author: John Snow Labs
name: ner_oncology_response_to_treatment_langtest
date: 2023-09-04
tags: [en, ner, licensed, clinical, oncology, langtest]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.0.2
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts entities related to the patient's response to the oncology treatment, including clinical response and changes in tumor size. It is the version of [ner_oncology_response_to_treatment](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_response_to_treatment_en.html) model augmented with `langtest` library

Definitions of Predicted Entities:

- `Line_Of_Therapy`: Explicit references to the line of therapy of an oncological therapy (e.g. "first-line treatment").
- `Response_To_Treatment`: Terms related to clinical progress of the patient related to cancer treatment, including "recurrence", "bad response" or "improvement".
- `Size_Trend`: Terms related to the changes in the size of the tumor (such as "growth" or "reduced in size").

## Predicted Entities

`Line_Of_Therapy`, `Response_To_Treatment`, `Size_Trend`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_response_to_treatment_langtest_en_5.0.2_3.0_1693826409453.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_response_to_treatment_langtest_en_5.0.2_3.0_1693826409453.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")\
    .setSplitChars(['-'])

word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")                

ner = MedicalNerModel.pretrained("ner_oncology_response_to_treatment_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter])

data = spark.createDataFrame([["She completed her first-line therapy, but some months later there was recurrence of the breast cancer. "]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
    
val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")
    
val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")
    .setSplitChars(['-'])
    
val word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                
    
val ner = MedicalNerModel.pretrained("ner_oncology_response_to_treatment_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")
    
val ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

        
val pipeline = new Pipeline().setStages(Array(document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter))    

val data = Seq("She completed her first-line therapy, but some months later there was recurrence of the breast cancer. ").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------+---------------------+
|chunk     |ner_label            |
+----------+---------------------+
|first-line|Line_Of_Therapy      |
|recurrence|Response_To_Treatment|
+----------+---------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_response_to_treatment_langtest|
|Compatibility:|Healthcare NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.7 MB|

## References

In-house annotated oncology case reports.

## Benchmarking

```bash
label                    precision  recall  f1-score  support 
B-Response_To_Treatment  0.83       0.83    0.83      289     
I-Response_To_Treatment  0.74       0.77    0.76      209     
B-Size_Trend             0.65       0.69    0.67      101     
I-Size_Trend             0.61       0.69    0.65      49      
B-Line_Of_Therapy        1.00       0.97    0.99      36      
I-Line_Of_Therapy        0.95       0.97    0.96      65      
micro-avg                0.78       0.81    0.79      749     
macro-avg                0.80       0.82    0.81      749     
weighted-avg             0.78       0.81    0.79      749     
```