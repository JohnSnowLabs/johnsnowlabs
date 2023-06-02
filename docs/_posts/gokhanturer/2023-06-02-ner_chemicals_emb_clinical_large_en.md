---
layout: model
title: Detect Chemicals in Text (embeddings_clinical_large)
author: John Snow Labs
name: ner_chemicals_emb_clinical_large
date: 2023-06-02
tags: [ner, clinical, licensed, en, chemicals]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.3
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Extract different types of chemical compounds mentioned in text using pretrained NER model. ( Trained with embeddings_clinical_large )

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CHEMICALS/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_chemicals_emb_clinical_large_en_4.4.3_3.0_1685713522857.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_chemicals_emb_clinical_large_en_4.4.3_3.0_1685713522857.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence") 

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_large", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

species_ner = MedicalNerModel.pretrained("ner_chemicals_emb_clinical_large", "en", "clinical/models" ) \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("species_ner")
    
species_ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "species_ner"]) \
    .setOutputCol("species_ner_chunk")

species_ner_pipeline = Pipeline(stages=[
    documentAssembler, 
    sentenceDetector,
    tokenizer,
    word_embeddings,
    species_ner,
    species_ner_converter])

empty_data = spark.createDataFrame([[""]]).toDF("text")

species_ner_model = species_ner_pipeline.fit(empty_data)

results = species_ner_model.transform(spark.createDataFrame([['''Differential cell - protective function of two resveratrol (trans - 3, 5, 4 - trihydroxystilbene) glucosides against oxidative stress. Resveratrol (trans - 3, 5, 4  - trihydroxystilbene ; RSV) , a natural polyphenol, exerts a beneficial effect on health and diseases. 
RSV targets and activates the NAD(+) - dependent protein deacetylase SIRT1; in turn, SIRT1 induces an intracellular antioxidative mechanism by inducing mitochondrial superoxide dismutase (SOD2). Most RSV found in plants is glycosylated, and the effect of these glycosylated forms on SIRT1 has not been studied. ''']]).toDF("text"))
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")
    
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_large", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val anatomy_ner_model = MedicalNerModel.pretrained("ner_chemicals_emb_clinical_large", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("anatomy_ner")

val anatomy_ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("anatomy_ner_chunk")

val posology_pipeline = new PipelineModel().setStages(Array(document_assembler, 
                                                   sentence_detector,
                                                   tokenizer,
                                                   word_embeddings,
                                                   anatomy_ner_model,
                                                   anatomy_ner_converter))

val data = Seq(""" Differential cell - protective function of two resveratrol (trans - 3, 5, 4 - trihydroxystilbene) glucosides against oxidative stress. Resveratrol (trans - 3, 5, 4  - trihydroxystilbene ; RSV) , a natural polyphenol, exerts a beneficial effect on health and diseases. 
RSV targets and activates the NAD(+) - dependent protein deacetylase SIRT1; in turn, SIRT1 induces an intracellular antioxidative mechanism by inducing mitochondrial superoxide dismutase (SOD2). Most RSV found in plants is glycosylated, and the effect of these glycosylated forms on SIRT1 has not been studied.""").toDS.toDF("text")

val result = model.fit(data).transform(data)
```
</div>

## Results

```bash
|    | chunks                                           |   begin |   end | entities   |
|---:|:-------------------------------------------------|--------:|------:|:-----------|
|  0 | resveratrol                                      |      48 |    58 | CHEM       |
|  1 | trans - 3, 5, 4 - trihydroxystilbene) glucosides |      61 |   108 | CHEM       |
|  2 | Resveratrol                                      |     136 |   146 | CHEM       |
|  3 | trans - 3, 5, 4  - trihydroxystilbene            |     149 |   185 | CHEM       |
|  4 | RSV                                              |     189 |   191 | CHEM       |
|  5 | polyphenol                                       |     206 |   215 | CHEM       |
|  6 | NAD(+)                                           |     300 |   305 | CHEM       |
|  7 | superoxide                                       |     436 |   445 | CHEM       |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_chemicals_emb_clinical_large|
|Compatibility:|Healthcare NLP 4.4.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|2.8 MB|

## Benchmarking

```bash
       label     precision  recall   f1-score  support
        CHEM       0.94      0.93      0.94     62001
   micro-avg       0.94      0.93      0.94     62001
   macro-avg       0.94      0.93      0.94     62001
weighted-avg       0.94      0.93      0.94     62001
```
