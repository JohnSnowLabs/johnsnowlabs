---
layout: model
title: Sentence Entity Resolver for LOINC Codes - Augmented (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_loinc_augmented
date: 2024-10-08
tags: [licensed, en, biolord, loinc, entity_resolution, clinical]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.5.0
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps medical entities to Logical Observation Identifiers Names and Codes(LOINC) codes using `mpnet_embeddings_biolord_2023_c` embeddings.
It trained on the augmented version of the dataset which is used in previous LOINC resolver models. It also provides the official resolution of the codes within the brackets.

## Predicted Entities

`loinc_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_loinc_augmented_en_5.5.0_3.0_1728403801539.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_loinc_augmented_en_5.5.0_3.0_1728403801539.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
	
```python
document_assembler = DocumentAssembler()\
	  .setInputCol("text")\
	  .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
	  .setInputCols(["document"])\
	  .setOutputCol("sentence")

tokenizer = Tokenizer()\
	  .setInputCols(["sentence"])\
	  .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
	  .setInputCols(["sentence", "token"])\
	  .setOutputCol("word_embeddings")

ner = MedicalNerModel.pretrained("ner_radiology", "en", "clinical/models") \
	  .setInputCols(["sentence", "token", "word_embeddings"]) \
	  .setOutputCol("ner")

ner_converter = NerConverterInternal()\
	  .setInputCols(["sentence", "token", "ner"])\
	  .setOutputCol("ner_chunk")\
	  .setWhiteList(["Test"])

c2doc = Chunk2Doc()\
	  .setInputCols("ner_chunk")\
	  .setOutputCol("ner_chunk_doc")

biolord_embedding = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
         .setInputCols(["ner_chunk_doc"])\
         .setOutputCol("embeddings")\
         .setCaseSensitive(False)

loinc_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_loinc_augmented","en", "clinical/models")\
	  .setInputCols(["embeddings"]) \
	  .setOutputCol("loinc_code")\
	  .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(
    stages = [
	              document_assembler,
	              sentenceDetectorDL,
	              tokenizer,
	              word_embeddings,
	              ner,
	              ner_converter,
	              c2doc,
	              biolord_embedding,
	              loinc_resolver])

data = spark.createDataFrame([["""The patient is a 22-year-old female with a history of obesity. She has a Body mass index (BMI) of 33.5 kg/m2, aspartate aminotransferase 64, and alanine aminotransferase 126."""]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)
```
```scala
val document_assembler =  new DocumentAssembler()
	  .setInputCol("text")
	  .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
	  .setInputCols(["document"])
	  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
	  .setInputCols(["sentence"])
	  .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
	  .setInputCols(Array("sentence", "token"))
	  .setOutputCol("word_embeddings")

val ner = MedicalNerModel.pretrained("ner_radiology", "en", "clinical/models")
	  .setInputCols(Array("sentence", "token", "word_embeddings"))
	  .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
	  .setInputCols(Array("sentence", "token", "ner"))
	  .setOutputCol("ner_chunk")
	  .setWhiteList(["Test"])

val c2doc = new Chunk2Doc()
	  .setInputCols("ner_chunk")
	  .setOutputCol("ner_chunk_doc")

val biolord_embedding = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")
          .setInputCols(["ner_chunk_doc"])
          .setOutputCol("embeddings")
          .setCaseSensitive(False)

val loinc_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_loinc_augmented","en", "clinical/models")
	  .setInputCols(["embeddings"])
	  .setOutputCol("loinc_code")
	  .setDistanceFunction("EUCLIDEAN")

val resolver_pipeline = new Pipeline(
    stages = [
	              document_assembler,
	              sentenceDetectorDL,
	              tokenizer,
	              word_embeddings,
	              ner,
	              ner_converter,
	              c2doc,
	              biolord_embedding,
	              loinc_resolver])


val data = Seq([["""The patient is a 22-year-old female with a history of obesity. She has a Body mass index (BMI) of 33.5 kg/m2, aspartate aminotransferase 64, and alanine aminotransferase 126."""]]).toDF("text")

val result = resolver_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------------------+-----+---+---------+----------+-------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                     chunk|begin|end|ner_label|loinc_code|                                            description|                                                 resolutions|                                                   all_codes|                                                  aux_labels|
+--------------------------+-----+---+---------+----------+-------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                       BMI|   90| 92|     Test|   39156-5|                    BMI [Body mass index (BMI) [Ratio]]|BMI [Body mass index (BMI) [Ratio]]:::BMI Est [Body mass ...|39156-5:::89270-3:::94138-5:::59574-4:::LP415677-6:::5957...|Observation:::Observation:::Observation:::Observation:::M...|
|aspartate aminotransferase|  110|135|     Test| LP15426-7|Aspartate aminotransferase [Aspartate aminotransferase]|Aspartate aminotransferase [Aspartate aminotransferase]::...|LP15426-7:::100739-2:::LP307348-5:::LP307326-1:::LP307433...|Observation:::Observation:::Observation:::Observation:::O...|
|  alanine aminotransferase|  145|168|     Test| LP15333-5|    Alanine aminotransferase [Alanine aminotransferase]|Alanine aminotransferase [Alanine aminotransferase]:::L-a...|LP15333-5:::59245-1:::100738-4:::LP307326-1:::69383-8:::L...|Observation:::Observation:::Observation:::Observation:::O...|
+--------------------------+-----+---+---------+----------+-------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_loinc_augmented|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[mpnet_embeddings]|
|Output Labels:|[loinc_code]|
|Language:|en|
|Size:|1.1 GB|
|Case sensitive:|false|

## References
This model is trained with augmented version of the LOINC v2.78 dataset released in 2024-08-06.
