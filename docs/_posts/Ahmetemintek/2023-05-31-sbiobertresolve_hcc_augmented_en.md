---
layout: model
title: Sentence Entity Resolver for Hierarchical Condition Categories (HCC) codes (Augmented)
author: John Snow Labs
name: sbiobertresolve_hcc_augmented
date: 2023-05-31
tags: [en, entity_resolution, clinical, hcc, licensed]
task: Entity Resolution
language: en
edition: Healthcare NLP 4.4.2
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted medical entities to Hierarchical Condition Categories (HCC) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

## Predicted Entities

`HCC Codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_hcc_augmented_en_4.4.2_3.0_1685528056939.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_hcc_augmented_en_4.4.2_3.0_1685528056939.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
	.setInputCol("text")\
	.setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
	.setInputCols(["document"]) \
	.setOutputCol("sentence")\

tokenizer = Tokenizer()\
	.setInputCols(["sentence"])\
	.setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
	.setInputCols(["sentence", "token"])\
	.setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models") \
	.setInputCols(["sentence", "token", "embeddings"]) \
	.setOutputCol("ner")

ner_converter = NerConverterInternal() \
 	  .setInputCols(["sentence", "token", "ner"]) \
	  .setOutputCol("ner_chunk")\
	  .setWhiteList(["PROBLEM"])

chunk2doc = Chunk2Doc()\
  	.setInputCols("ner_chunk")\
  	.setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
	  .setInputCols(["ner_chunk_doc"])\
	  .setOutputCol("sbert_embeddings")\
	  .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_hcc_augmented","en", "clinical/models") \
	  .setInputCols(["sbert_embeddings"]) \
	  .setOutputCol("resolution")\
	  .setDistanceFunction("EUCLIDEAN")


nlpPipeline = Pipeline(stages=[document_assembler,
                               sentence_detector,
                               tokenizer,
                               word_embeddings,
                               ner_model,
                               ner_converter,
                               chunk2doc,
                               sbert_embedder,
                               resolver])

data = spark.createDataFrame([["""The patient's medical record indicates a diagnosis of Diabetes and Chronic Obstructive Pulmonary Disease, requiring comprehensive care and management."""]]).toDF("text")

result = nlpPipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document") 

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
 .setInputCols(Array("document")) 
 .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
 .setInputCols(Array("sentence")) 
 .setOutputCol("token") 

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
 .setInputCols(Array("sentence","token")) 
 .setOutputCol("embeddings") 

val ner_model = MedicalNerModel.pretrained("ner_clinical","en","clinical/models")
 .setInputCols(Array("sentence","token","embeddings")) 
 .setOutputCol("ner") 

val ner_converter = new NerConverterInternal()
 .setInputCols(Array("sentence","token","ner")) 
 .setOutputCol("ner_chunk") 
 .setWhiteList(Array("PROBLEM")) 

val chunk2doc = new Chunk2Doc()
 .setInputCols("ner_chunk") 
 .setOutputCol("ner_chunk_doc") 

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
 .setInputCols(Array("ner_chunk_doc")) 
 .setOutputCol("sbert_embeddings") 
 .setCaseSensitive(false) 

val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_hcc_augmented","en","clinical/models")
 .setInputCols(Array("sbert_embeddings")) 
 .setOutputCol("resolution") 
 setDistanceFunction("EUCLIDEAN") 

val nlpPipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector, 
    tokenizer, 
    word_embeddings, 
    ner_model, 
    ner_converter, 
    chunk2doc, 
    sbert_embedder, 
    resolver)) 

val data = Seq("""The patient"s medical record indicates a diagnosis of Diabetes and Chronic Obstructive Pulmonary Disease,requiring comprehensive care and management.""").toDF("text")

val result = nlpPipeline.fit(data).transform(data) 
```
</div>

## Results

```bash
+-------------------------------------+-----+---+---------+--------+------------------+------------------------------------------------------------+
|                                chunk|begin|end|ner_label|hcc_code|         all_codes|                                                 resolutions|
+-------------------------------------+-----+---+---------+--------+------------------+------------------------------------------------------------+
|                             Diabetes|   54| 61|  PROBLEM|      19|       19:::0:::18|diabetes monitored [type 2 diabetes mellitus without comp...|
|Chronic Obstructive Pulmonary Disease|   67|103|  PROBLEM|     111|111:::112:::85:::0|chronic obstructive pulmonary disease [chronic obstructiv...|
+-------------------------------------+-----+---+---------+--------+------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_hcc_augmented|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[hcc]|
|Language:|en|
|Size:|1.4 GB|
|Case sensitive:|false|
