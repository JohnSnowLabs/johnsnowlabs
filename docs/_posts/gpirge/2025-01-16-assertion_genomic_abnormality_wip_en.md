---
layout: model
title: "Genomic Assertion Status Model: Classifying Normal, Affected, and Variant Entities"
author: John Snow Labs
name: assertion_genomic_abnormality_wip
date: 2025-01-16
tags: [en, clinical, licensed, assertion, gene, normal, variant, affected]
task: Assertion Status
language: en
edition: Healthcare NLP 5.5.1
spark_version: 3.0
supported: true
annotator: AssertionDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This assertion status detection model is trained to classify entities (Gene and MPG) extracted by the NER model `ner_genes_phenotypes` into three categories: 

`Normal`, for genes and molecules part of normal physiology; 

`Affected`, for molecules or proteins impacted by genetic mutations; 

`Variant`, for genes that are abnormal or of a variant type, enabling precise characterization of genomic and molecular states.

## Predicted Entities

`Normal`, `Affected`, `Variant`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_genomic_abnormality_wip_en_5.5.1_3.0_1737034731887.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_genomic_abnormality_wip_en_5.5.1_3.0_1737034731887.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = WordEmbeddingsModel.pretrained('embeddings_clinical', "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained('ner_genes_phenotypes', "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(['sentence', 'token', 'ner'])\
    .setOutputCol('ner_chunk')\
    .setWhiteList(['Gene', 'MPG'])

assertion = AssertionDLModel.pretrained("assertion_genomic_abnormality_wip", "en", "clinical/models")\
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter,
    assertion
    ])

sample_texts = ["""
The ATP7B gene provides instructions for a copper-transporting ATPase essential for copper homeostasis. Mutations in the ATP7B gene cause Wilson disease, an autosomal recessive disorder of copper metabolism. 
Over 500 mutations have been identified, including missense, nonsense, and splice site mutations. The variant ATP7B protein leads to impaired copper excretion and accumulation in various organs, particularly the liver and brain. 
Clinical presentations of Wilson disease include hepatic dysfunction, neurological symptoms (e.g., tremors, dystonia), and psychiatric disturbances. 
Kayser-Fleischer rings, copper deposits in the cornea, are a characteristic sign. Gene-environment interactions are significant, with dietary copper intake and other environmental factors influencing disease progression. 
Diagnosis involves a combination of clinical symptoms, low serum ceruloplasmin, high urinary copper, and genetic testing. 
Treatment focuses on reducing copper accumulation through chelation therapy with drugs like penicillamine or trientine, and zinc supplementation to block copper absorption. 
Liver transplantation may be necessary in severe cases. The worldwide prevalence of Wilson disease is estimated at 1 in 30,000, with higher rates in certain isolated populations.
"""]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = nlp.WordEmbeddingsModel.pretrained('embeddings_clinical', "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained('ner_genes_phenotypes', "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(['sentence', 'token', 'ner'])\
    .setOutputCol('ner_chunk')\
    .setWhiteList(['Gene', 'MPG'])

assertion = medical.AssertionDLModel.pretrained("assertion_genomic_abnormality_wip", "en", "clinical/models")\
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")

pipeline = nlp.Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter,
    assertion
    ])

sample_texts = ["""
The ATP7B gene provides instructions for a copper-transporting ATPase essential for copper homeostasis. Mutations in the ATP7B gene cause Wilson disease, an autosomal recessive disorder of copper metabolism. 
Over 500 mutations have been identified, including missense, nonsense, and splice site mutations. The variant ATP7B protein leads to impaired copper excretion and accumulation in various organs, particularly the liver and brain. 
Clinical presentations of Wilson disease include hepatic dysfunction, neurological symptoms (e.g., tremors, dystonia), and psychiatric disturbances. 
Kayser-Fleischer rings, copper deposits in the cornea, are a characteristic sign. Gene-environment interactions are significant, with dietary copper intake and other environmental factors influencing disease progression. 
Diagnosis involves a combination of clinical symptoms, low serum ceruloplasmin, high urinary copper, and genetic testing. 
Treatment focuses on reducing copper accumulation through chelation therapy with drugs like penicillamine or trientine, and zinc supplementation to block copper absorption. 
Liver transplantation may be necessary in severe cases. The worldwide prevalence of Wilson disease is estimated at 1 in 30,000, with higher rates in certain isolated populations.
"""]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_genes_phenotypes", "en", "clinical/models")
    .setInputCols(Array("sentence", "token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(['Gene', 'MPG'])
    
val assertion = AssertionDLModel.pretrained("assertion_genomic_abnormality_wip", "en", "clinical/models")
    .setInputCols(Array("sentence", "ner_chunk", "embeddings"))
    .setOutputCol("assertion")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentenceDetector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter,
    assertion
))

val sample_texts = Seq("""The ATP7B gene provides instructions for a copper-transporting ATPase essential for copper homeostasis. Mutations in the ATP7B gene cause Wilson disease, an autosomal recessive disorder of copper metabolism. 
Over 500 mutations have been identified, including missense, nonsense, and splice site mutations. The variant ATP7B protein leads to impaired copper excretion and accumulation in various organs, particularly the liver and brain. 
Clinical presentations of Wilson disease include hepatic dysfunction, neurological symptoms (e.g., tremors, dystonia), and psychiatric disturbances. 
Kayser-Fleischer rings, copper deposits in the cornea, are a characteristic sign. Gene-environment interactions are significant, with dietary copper intake and other environmental factors influencing disease progression. 
Diagnosis involves a combination of clinical symptoms, low serum ceruloplasmin, high urinary copper, and genetic testing. 
Treatment focuses on reducing copper accumulation through chelation therapy with drugs like penicillamine or trientine, and zinc supplementation to block copper absorption. 
Liver transplantation may be necessary in severe cases. The worldwide prevalence of Wilson disease is estimated at 1 in 30,000, with higher rates in certain isolated populations.
""").toDF("text")

val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

## Results

```bash
+-------------+-----+---+---------+---------+----------+
|chunk        |begin|end|ner_label|assertion|confidence|
+-------------+-----+---+---------+---------+----------+
|ATP7B gene   |5    |14 |MPG      |Normal   |0.9835    |
|ATPase       |64   |69 |MPG      |Normal   |0.9979    |
|ATP7B gene   |122  |131|MPG      |Affected |0.9974    |
|ATP7B protein|319  |331|MPG      |Affected |0.9713    |
|ceruloplasmin|873  |885|MPG      |Affected |0.9707    |
+-------------+-----+---+---------+---------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_genomic_abnormality_wip|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, ner_chunk, embeddings]|
|Output Labels:|[assertion_pred]|
|Language:|en|
|Size:|944.2 KB|

## References

In-house annotated case reports.

## Benchmarking

```bash
       label  precision    recall  f1-score   support
    Affected       0.84      0.82      0.83       342
      Normal       0.82      0.86      0.84       315
     Variant       0.88      0.84      0.86        94
    accuracy                           0.84       751
   macro-avg       0.85      0.84      0.84       751
weighted-avg       0.84      0.84      0.84       751
```