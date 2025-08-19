---
layout: model
title: Sentence Entity Resolver for MeSH Veterinary (sbiobert_base_cased_mli embeddings)
author: John Snow Labs
name: sbiobertresolve_mesh_veterinary
date: 2025-02-19
tags: [en, licensed, clinical, entity_resolution, mesh, veterinary]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.5.2
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities in the veterinary notes to Medical Subject Heading (MeSH) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. In this model, MeSH veterinary-related descriptors, and supplementary concept datasets were used.

## Predicted Entities

`mesh_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_mesh_veterinary_en_5.5.2_3.0_1739988813875.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_mesh_veterinary_en_5.5.2_3.0_1739988813875.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
	
```python
document_assembler = DocumentAssembler()\
	.setInputCol("text")\
	.setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
	.setInputCols(["document"])\
	.setOutputCol("sentence")

tokenizer = Tokenizer()\
	.setInputCols(["sentence"])\
	.setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
	.setInputCols(["sentence", "token"])\
	.setOutputCol("word_embeddings")

ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models") \
	.setInputCols(["sentence", "token", "word_embeddings"]) \
	.setOutputCol("ner")\

ner_converter = NerConverterInternal()\
	.setInputCols(["sentence", "token", "ner"])\
	.setOutputCol("ner_chunk")\
	.setBlackList(["TREATMENT", "TEST"])

chunk2doc = Chunk2Doc()\
	.setInputCols("ner_chunk")\
	.setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli",'en','clinical/models')\
  	.setInputCols(["ner_chunk_doc"])\
  	.setOutputCol("sbert_embeddings")\
  	.setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_mesh_veterinary","en","clinical/models") \
	.setInputCols(["sbert_embeddings"]) \
	.setOutputCol("mesh_code")\
	.setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages = [
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner,
    ner_converter,
    chunk2doc,
    sbert_embedder,
    resolver])

text = "The dog is a labrador retriever, 4-year-old, it was brought in with vomiting and diarrhea for the past 2 days. A preliminary diagnosis of canine parvovirus infection was made, and supportive care was recommended. The owner was advised on isolation precautions to prevent the spread of the virus."

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
document_assembler =nlp.DocumentAssembler()\
	.setInputCol("text")\
	.setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
	.setInputCols(["document"])\
	.setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
	.setInputCols(["sentence"])\
	.setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
	.setInputCols(["sentence", "token"])\
	.setOutputCol("word_embeddings")

ner = medical.NerModel.pretrained("ner_clinical", "en", "clinical/models") \
	.setInputCols(["sentence", "token", "word_embeddings"]) \
	.setOutputCol("ner")\

ner_converter = medical.NerConverterInternal()\
	.setInputCols(["sentence", "token", "ner"])\
	.setOutputCol("ner_chunk")

chunk2doc = nlp.Chunk2Doc()\
	.setInputCols("ner_chunk")\
	.setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli",'en','clinical/models')\
	.setInputCols(["ner_chunk_doc"])\
  	.setOutputCol("sbert_embeddings")\
  	.setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_mesh_veterinary","en","clinical/models") \
	.setInputCols(["sbert_embeddings"]) \
	.setOutputCol("mesh_code")\
	.setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages = [
	document_assembler,
	sentence_detector,
	tokenizer,
	word_embeddings,
	ner,
	ner_converter,
	chunk2doc,
	sbert_embedder,
	resolver])

text = """The dog is a labrador retriever, 4-year-old, it was brought in with vomiting and diarrhea for the past 2 days. A preliminary diagnosis of canine parvovirus infection was made, and supportive care was recommended. The owner was advised on isolation precautions to prevent the spread of the virus."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
  .setInputCols(Array("sentence","token"))
  .setOutputCol("word_embeddings")

val ner = MedicalNerModel.pretrained("ner_clinical","en","clinical/models")
  .setInputCols(Array("sentence","token","word_embeddings"))
  .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
  .setInputCols(Array("sentence","token","ner"))
  .setOutputCol("ner_chunk")

val c2doc = new Chunk2Doc()
  .setInputCols("ner_chunk")
  .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("sbert_embeddings")
  .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_mesh_veterinary","en","clinical/models")
  .setInputCols(Array("sbert_embeddings"))
  .setOutputCol("mesh_code")
  .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
  document_assembler,
  sentenceDetectorDL,
  tokenizer,
  word_embeddings,
  ner,
  ner_converter,
  c2doc,
  sbert_embedder,
  resolver))

val data = Seq("The dog is a labrador retriever, 4-year-old, it was brought in with vomiting and diarrhea for the past 2 days. A preliminary diagnosis of canine parvovirus infection was made, and supportive care was recommended. The owner was advised on isolation precautions to prevent the spread of the virus.").toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---------------------------+-----+---+---------+----------+-------------------+------------------------------------------------------------+------------------------------------------------------------+
|                      chunk|begin|end|ner_label|resolution|        description|                                               all_k_results|                                           all_k_resolutions|
+---------------------------+-----+---+---------+----------+-------------------+------------------------------------------------------------+------------------------------------------------------------+
|                   vomiting|   68| 75|  PROBLEM|   C536228|  periodic vomiting|C536228:::C007262:::C080875:::C002771:::C000626292:::C076...|periodic vomiting:::vomitoxin:::mirage:::propargite:::ena...|
|                   diarrhea|   81| 88|  PROBLEM|   C565627|diarrhea, syndromic|C565627:::C564019:::C531700:::C580192:::C537470:::C000702...|diarrhea, syndromic:::diarrhea, chronic, with villous atr...|
|canine parvovirus infection|  138|164|  PROBLEM|   D017993|  canine parvovirus|D017993:::D052660:::D028323:::D017939:::D017992:::C528774...|canine parvovirus:::bovine parvovirus:::porcine parvoviru...|
|                  the virus|  285|293|  PROBLEM|   D014780|              virus|D014780:::D006678:::D006476:::D012526:::C000623864:::D014...|virus:::aids virus:::andes virus:::virus, associated:::pr...|
+---------------------------+-----+---+---------+----------+-------------------+------------------------------------------------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_mesh_veterinary|
|Compatibility:|Healthcare NLP 5.5.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[mesh_code]|
|Language:|en|
|Size:|2.2 GB|
|Case sensitive:|false|
