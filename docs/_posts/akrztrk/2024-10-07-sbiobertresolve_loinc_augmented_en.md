---
layout: model
title: Sentence Entity Resolver for LOINC (sbiobert_base_cased_mli embeddings)
author: John Snow Labs
name: sbiobertresolve_loinc_augmented
date: 2024-10-07
tags: [licensed, en, entity_resolution, loinc, clinical]
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

This model maps extracted clinical NER entities to Logical Observation Identifiers Names and Codes(LOINC) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. It trained on the augmented version of the dataset which is used in previous LOINC resolver models. It also provides the official resolution of the codes within the brackets.

## Predicted Entities

`loinc_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_loinc_augmented_en_5.5.0_3.0_1728318394102.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_loinc_augmented_en_5.5.0_3.0_1728318394102.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

tokenizer = Tokenizer()\
	.setInputCols(["sentence"])\
	.setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
	.setInputCols(["sentence", "token"])\
	.setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_radiology", "en", "clinical/models") \
	.setInputCols(["sentence", "token", "embeddings"]) \
	.setOutputCol("ner")

ner_converter = NerConverterInternal() \
 	  .setInputCols(["sentence", "token", "ner"]) \
	  .setOutputCol("ner_chunk")\
	  .setWhiteList(["Test"])

chunk2doc = Chunk2Doc()\
  	.setInputCols("ner_chunk")\
  	.setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
	  .setInputCols(["ner_chunk_doc"])\
	  .setOutputCol("sbert_embeddings")\
	  .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc_augmented","en", "clinical/models") \
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

data = spark.createDataFrame([["""The patient is a 22-year-old female with a history of obesity. She has a Body mass index (BMI) of 33.5 kg/m2, aspartate aminotransferase 64, and alanine aminotransferase 126."""]]).toDF("text")

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

val ner_model = MedicalNerModel.pretrained("ner_radiology","en","clinical/models")
  .setInputCols(Array("sentence","token","embeddings"))
  .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
  .setInputCols(Array("sentence","token","ner"))
  .setOutputCol("ner_chunk")
  .setWhiteList(Array("Test"))

val chunk2doc = new Chunk2Doc()
  .setInputCols("ner_chunk")
  .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("sbert_embeddings")
  .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc_augmented","en","clinical/models")
  .setInputCols(Array("sbert_embeddings"))
  .setOutputCol("resolution")
  .setDistanceFunction("EUCLIDEAN")

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

val data = Seq([["""The patient is a 22-year-old female with a history of obesity. She has a Body mass index (BMI) of 33.5 kg/m2, aspartate aminotransferase 64, and alanine aminotransferase 126."""]]).toDF("text")

val result = nlpPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------------------+-----+---+---------+----------+-------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                     chunk|begin|end|ner_label|loinc_code|                                            description|                                                 resolutions|                                                   all_codes|                                                  aux_labels|
+--------------------------+-----+---+---------+----------+-------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                       BMI|   90| 92|     Test|   39156-5|                    BMI [Body mass index (BMI) [Ratio]]|BMI [Body mass index (BMI) [Ratio]]:::BM [IDH1 gene exon ...|39156-5:::100305-2:::LP266933-3:::100225-2:::LP241982-0::...|Observation:::Observation:::Observation:::Observation:::O...|
|aspartate aminotransferase|  110|135|     Test| LP15426-7|Aspartate aminotransferase [Aspartate aminotransferase]|Aspartate aminotransferase [Aspartate aminotransferase]::...|LP15426-7:::100739-2:::LP307348-5:::LP15333-5:::LP307326-...|Observation:::Observation:::Observation:::Observation:::O...|
|  alanine aminotransferase|  145|168|     Test| LP15333-5|    Alanine aminotransferase [Alanine aminotransferase]|Alanine aminotransferase [Alanine aminotransferase]:::Ala...|LP15333-5:::LP307326-1:::100738-4:::LP307348-5:::LP15426-...|Observation:::Observation:::Observation:::Observation:::O...|
+--------------------------+-----+---+---------+----------+-------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_loinc_augmented|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[loinc_code]|
|Language:|en|
|Size:|1.1 GB|
|Case sensitive:|false|

## References
This model is trained with augmented version of the LOINC v2.78 dataset released in 2024-08-06.
