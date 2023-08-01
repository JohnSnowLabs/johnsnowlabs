---
layout: model
title: Sentence Entity Resolver for LOINC
author: John Snow Labs
name: sbiobertresolve_loinc_numeric
date: 2023-08-01
tags: [licensed, en, clinical, loinc, entity_resolution]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.0.0
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted clinical NER entities to Logical Observation Identifiers Names and Codes(LOINC) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. It is trained with the numeric LOINC codes, without the inclusion of LOINC "Document Ontology" codes starting with the letter "L". It also provides the official resolution of the codes within the brackets.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_loinc_numeric_en_5.0.0_3.0_1690914815831.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_loinc_numeric_en_5.0.0_3.0_1690914815831.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

documentAssembler = DocumentAssembler()    .setInputCol("text")    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")    .setInputCols("document")    .setOutputCol("sentence")

tokenizer = Tokenizer()     .setInputCols(["document"])     .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained('embeddings_clinical','en', 'clinical/models')    .setInputCols(["sentence", "token"])    .setOutputCol("embeddings")

ner = MedicalNerModel.pretrained("ner_radiology", "en", "clinical/models")     .setInputCols(["sentence", "token", "embeddings"])     .setOutputCol("ner")

ner_converter = NerConverter()     .setInputCols(["sentence", "token", "ner"])     .setOutputCol("ner_chunk")    .setWhiteList(['Test'])

chunk2doc = Chunk2Doc().setInputCols("ner_chunk").setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")    .setInputCols(["ner_chunk_doc"])    .setOutputCol("sbert_embeddings")    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc_numeric","en", "clinical/models")     .setInputCols(["sbert_embeddings"])     .setOutputCol("loinc_code")    .setDistanceFunction("EUCLIDEAN")

pipeline_loinc = Pipeline(stages = [documentAssembler, sentenceDetector, tokenizer, word_embeddings, ner, ner_converter, chunk2doc, sbert_embedder, resolver])

data = spark.createDataFrame([["""The patient is a 22-year-old female with a history of obesity. She has a Body mass index (BMI) of 33.5 kg/m2, aspartate aminotransferase 64, and alanine aminotransferase 126."""]]).toDF("text")

results = pipeline_loinc.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
    
val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")
    
val tokenizer = new Tokenizer() 
    .setInputCols(Array("document"))
    .setOutputCol("token")
    
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")
    
val ner = MedicalNerModel.pretrained("ner_radiology", "en", "clinical/models") 
    .setInputCols(Array("sentence", "token", "embeddings")) 
    .setOutputCol("ner")
    
val ner_converter = new NerConverterInternal() 
    .setInputCols(Array("sentence", "token", "ner")) 
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Test"))
    
val chunk2doc = new Chunk2Doc() 
    .setInputCols("ner_chunk") 
    .setOutputCol("ner_chunk_doc")
    
val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en","clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(False)
    
val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc_numeric", "en", "clinical/models") 
    .setInputCols(Array("ner_chunk", "sbert_embeddings")) 
    .setOutputCol("loinc_code")
    .setDistanceFunction("EUCLIDEAN")
    
val pipeline_loinc = new Pipeline().setStages(Array(documentAssembler, 
                                                    sentenceDetector,
                                                    tokenizer,
                                                    word_embeddings,
                                                    ner,
                                                    ner_converter,
                                                    chunk2doc,
                                                    sbert_embedder,
                                                    resolver))
                                                    
val data = Seq("""The patient is a 22-year-old female with a history of obesity. She has a Body mass index (BMI) of 33.5 kg/m2, aspartate aminotransferase 64, and alanine aminotransferase 126."""").toDF("text")

val result = pipeline_loinc.fit(data).transform(data)

```
</div>

## Results

```bash

+-------+--------------------------+------+----------+----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
|sent_id|                 ner_chunk|entity|loinc_code|                                                                                           all_codes|                                                                                         resolutions|
+-------+--------------------------+------+----------+----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
|      1|                       BMI|  Test|   39156-5|39156-5:::89270-3:::100847-3:::8277-6:::3140-1:::914-2:::37219-3:::11895-0:::30201-8:::3139-3:::2...|BMI [Body mass index]:::BMI Est [Body mass index]:::BldA [Gas & ammonia panel]:::BSA [Body surfac...|
|      1|aspartate aminotransferase|  Test|   14409-7|14409-7:::1916-6:::16324-6:::16325-3:::43822-6:::1919-0:::3082-5:::2325-9:::100739-2:::1918-2:::5...|Aspartate aminotransferase [Aspartate aminotransferase]:::Aspartate aminotransferase/Alanine amin...|
|      1|  alanine aminotransferase|  Test|   16324-6|16324-6:::16325-3:::1916-6:::14409-7:::59245-1:::25302-1:::100738-4:::1740-0:::1742-6:::43822-6::...|Alanine aminotransferase [Alanine aminotransferase]:::Alanine aminotransferase/Aspartate aminotra...|
+-------+--------------------------+------+----------+----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_loinc_numeric|
|Compatibility:|Healthcare NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[loinc_code]|
|Language:|en|
|Size:|748.0 MB|
|Case sensitive:|false|