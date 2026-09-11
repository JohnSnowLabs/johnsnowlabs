---
layout: model
title: Sentence Entity Resolver for SNOMED CT (Body Structures) (sbiobert_base_cased_mli_onnx embeddings)
author: John Snow Labs
name: sbiobertresolve_snomed_bodyStructure_20260901
date: 2026-09-11
tags: [en, snomed, resolver, licensed, clinical, bodystructure, sbiobert]
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

This model maps extracted clinical NER entities to SNOMED CT concepts using `sbiobert_base_cased_mli_onnx` embeddings.

It is trained on SNOMED CT US Edition 20260901 release.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_bodyStructure_20260901_en_6.4.1_3.4_1789151595576.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_bodyStructure_20260901_en_6.4.1_3.4_1789151595576.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_jsl = MedicalNerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_jsl_tags")

ner_jsl_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner_jsl_tags"])\
    .setOutputCol("ner_chunk_jsl")\
    .setWhiteList(["Disease_Syndrome_Disorder", "External_body_part_or_region"])

ner_anatomy = MedicalNerModel.pretrained("ner_anatomy_coarse","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_anatomy_tags")

ner_anatomy_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner_anatomy_tags"])\
    .setOutputCol("ner_chunk_anatomy")

chunk_merger = ChunkMergeApproach()\
    .setInputCols(["ner_chunk_jsl", "ner_chunk_anatomy"])\
    .setOutputCol("ner_chunk")

chunk2doc = Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_bodyStructure_20260901","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")\
    .setThreshold(1000)

pipeline = Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_jsl, ner_jsl_converter, ner_anatomy, ner_anatomy_converter, chunk_merger, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The patient is a 30-year-old female with coronary artery disease, chronic renal insufficiency affecting the kidney, and swelling in the lower limb."]]).toDF("text")
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

ner_jsl = medical.NerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_jsl_tags")

ner_jsl_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner_jsl_tags"])\
    .setOutputCol("ner_chunk_jsl")\
    .setWhiteList(["Disease_Syndrome_Disorder", "External_body_part_or_region"])

ner_anatomy = medical.NerModel.pretrained("ner_anatomy_coarse","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_anatomy_tags")

ner_anatomy_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner_anatomy_tags"])\
    .setOutputCol("ner_chunk_anatomy")

chunk_merger = medical.ChunkMergeApproach()\
    .setInputCols(["ner_chunk_jsl", "ner_chunk_anatomy"])\
    .setOutputCol("ner_chunk")

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_bodyStructure_20260901","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")\
    .setThreshold(1000)

pipeline = nlp.Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_jsl, ner_jsl_converter, ner_anatomy, ner_anatomy_converter, chunk_merger, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The patient is a 30-year-old female with coronary artery disease, chronic renal insufficiency affecting the kidney, and swelling in the lower limb."]]).toDF("text")
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

val ner_jsl = MedicalNerModel
    .pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner_jsl_tags")

val ner_jsl_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_jsl_tags"))
    .setOutputCol("ner_chunk_jsl")
    .setWhiteList(Array("Disease_Syndrome_Disorder", "External_body_part_or_region"))

val ner_anatomy = MedicalNerModel
    .pretrained("ner_anatomy_coarse", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner_anatomy_tags")

val ner_anatomy_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_anatomy_tags"))
    .setOutputCol("ner_chunk_anatomy")

val chunk_merger = new ChunkMergeApproach()
    .setInputCols(Array("ner_chunk_jsl", "ner_chunk_anatomy"))
    .setOutputCol("ner_chunk")

val chunk2doc = new Chunk2Doc()
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("ner_chunk_doc")

val embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_snomed_bodyStructure_20260901", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("snomed_code")
    .setDistanceFunction("EUCLIDEAN")
    .setThreshold(1000)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_jsl, ner_jsl_converter, ner_anatomy, ner_anatomy_converter, chunk_merger, chunk2doc, embedder, resolver
))

val data = Seq("The patient is a 30-year-old female with coronary artery disease, chronic renal insufficiency affecting the kidney, and swelling in the lower limb.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| chunk           | label   |   snomed_code | resolution      | all_codes                                                                           | all_resolutions                                                                     |
|:----------------|:--------|--------------:|:----------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| coronary artery | Anatomy |      41801008 | coronary artery | 41801008:::119204004:::360487004:::55537005:::110554000:::48955001:::1343313006:... | coronary artery:::coronary artery part:::segment of coronary artery:::ostium of ... |
| renal           | Anatomy |      64033007 | renal structure | 64033007:::84924000:::303402001:::58471003:::2841007:::50403003:::91773002:::279... | renal structure:::renal segment:::renal vessels:::renal tubule:::renal artery:::... |
| kidney          | Anatomy |      64033007 | kidney          | 64033007:::119219003:::84924000:::50403003:::72333003:::30737000:::74033008:::58... | kidney:::kidney part:::renal segment:::renal cortex:::capillary of kidney:::medu... |
| lower limb      | Anatomy |      61685007 | lower limb      | 61685007:::30021000:::63337009:::128263001:::120575009:::69548008:::48077000:::3... | lower limb:::lower leg:::lower trunk:::lower body:::lower limb part:::lower body... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_bodyStructure_20260901|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sbert_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|199.6 MB|
|Case sensitive:|false|