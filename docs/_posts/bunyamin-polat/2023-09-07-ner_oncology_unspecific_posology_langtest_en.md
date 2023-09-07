---
layout: model
title: Extract Cancer Therapies and Posology Information (LangTest)
author: John Snow Labs
name: ner_oncology_unspecific_posology_langtest
date: 2023-09-07
tags: [en, licensed, ner, clinical, oncology, posology, langtest]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.1.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts mentions of treatments and posology information using unspecific labels (low granularity). It is the version of [ner_oncology_unspecific_posology](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_unspecific_posology_en.html) model augmented with `langtest` library.

Definitions of Predicted Entities:

- `Cancer_Therapy`: Mentions of cancer treatments, including chemotherapy, radiotherapy, surgery, and others.
- `Posology_Information`: Terms related to the posology of the treatment, including duration, frequencies, and dosage.

## Predicted Entities

`Cancer_Therapy`, `Posology_Information`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_unspecific_posology_langtest_en_5.1.0_3.0_1694072793093.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_unspecific_posology_langtest_en_5.1.0_3.0_1694072793093.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")                

ner = MedicalNerModel.pretrained("ner_oncology_unspecific_posology_langtest", "en", "clinical/models") \
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

data = spark.createDataFrame([["The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses. She is currently receiving his second cycle of chemotherapy and is in good overall condition."]]).toDF("text")

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
    
val word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                
    
val ner = MedicalNerModel.pretrained("ner_oncology_unspecific_posology_langtest", "en", "clinical/models")
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

val data = Seq("The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses. She is currently receiving his second cycle of chemotherapy and is in good overall condition.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------+--------------------+
|chunk           |ner_label           |
+----------------+--------------------+
|adriamycin      |Cancer_Therapy      |
|60 mg/m2        |Posology_Information|
|cyclophosphamide|Cancer_Therapy      |
|600 mg/m2       |Posology_Information|
|six courses     |Posology_Information|
|second cycle    |Posology_Information|
|chemotherapy    |Cancer_Therapy      |
+----------------+--------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_unspecific_posology_langtest|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.6 MB|

## References

In-house annotated oncology case reports.

## Benchmarking

```bash
label                   precision  recall  f1-score  support 
B-Posology_Information  0.90       0.88    0.89      1086    
B-Cancer_Therapy        0.93       0.93    0.93      1830    
I-Cancer_Therapy        0.86       0.82    0.84      930     
I-Posology_Information  0.91       0.92    0.91      1817    
micro-avg               0.91       0.90    0.90      5663    
macro-avg               0.90       0.89    0.89      5663    
weighted-avg            0.91       0.90    0.90      5663   
```