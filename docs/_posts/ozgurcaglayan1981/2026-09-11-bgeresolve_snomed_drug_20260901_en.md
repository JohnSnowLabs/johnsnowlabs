---
layout: model
title: Sentence Entity Resolver for SNOMED CT (Drugs) (bge_base_en_v1_5_onnx embeddings)
author: John Snow Labs
name: bgeresolve_snomed_drug_20260901
date: 2026-09-11
tags: [en, snomed, resolver, licensed, clinical, drug, bge]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted clinical NER entities to SNOMED CT concepts using `bge_base_en_v1_5_onnx` embeddings.

It is trained on SNOMED CT US Edition 20260901 release.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_snomed_drug_20260901_en_6.4.1_3.4_1789150659590.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_snomed_drug_20260901_en_6.4.1_3.4_1789150659590.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_posology","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_tags")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner_tags"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

chunk2doc = Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("bgeresolve_snomed_drug_20260901","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")\
    .setThreshold(1000)

pipeline = Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and lansoprazole for his GORD."]]).toDF("text")
result = pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained("ner_posology","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_tags")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner_tags"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_snomed_drug_20260901","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")\
    .setThreshold(1000)

pipeline = nlp.Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and lansoprazole for his GORD."]]).toDF("text")
result = pipeline.fit(data).transform(data)
```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel
    .pretrained("ner_posology", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner_tags")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_tags"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("DRUG"))

val chunk2doc = new Chunk2Doc()
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("ner_chunk_doc")

val embedder = BGEEmbeddings
    .pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("bgeresolve_snomed_drug_20260901", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
    .setOutputCol("snomed_code")
    .setDistanceFunction("EUCLIDEAN")
    .setThreshold(1000)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_model, ner_converter, chunk2doc, embedder, resolver
))

val data = Seq("John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and lansoprazole for his GORD.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| chunk        | label   |   snomed_code | resolution   | all_codes                                                                           | all_resolutions                                                                     |
|:-------------|:--------|--------------:|:-------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| aspirin      | DRUG    |     387458008 | aspirin      | 387458008:::25796002:::7947003:::774656009:::426365001:::412569008:::319796006::... | aspirin:::aluminium aspirin:::aspirin-containing product:::aspirin only product:... |
| paracetamol  | DRUG    |     387517004 | paracetamol  | 387517004:::90332006:::437876006:::1285524005:::412499001:::437818001:::77706700... | paracetamol:::paracetamol-containing product:::paracetamol-containing product in... |
| amoxicillin  | DRUG    |     372687004 | amoxicillin  | 372687004:::427483001:::27658006:::96068000:::785686003:::1197004003:::114848000... | amoxicillin:::amoxicillin sodium:::amoxicillin-containing product:::amoxicillin ... |
| lansoprazole | DRUG    |     386888004 | lansoprazole | 386888004:::108666007:::437961004:::409145007:::776475007:::437976007:::78553300... | lansoprazole:::lansoprazole-containing product:::lansoprazole-containing product... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_snomed_drug_20260901|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|238.5 MB|
|Case sensitive:|false|