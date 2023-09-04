---
layout: model
title: Sentence Entity Resolver for LOINC (sbiobert_base_cased_mli embeddings)
author: John Snow Labs
name: sbiobertresolve_loinc_augmented
date: 2023-08-01
tags: [loinc, entity_resolution, clinical, en, licensed]
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

This model maps extracted clinical NER entities to Logical Observation Identifiers Names and Codes(LOINC) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. It trained on the augmented version of the dataset which is used in previous LOINC resolver models. It also provides the official resolution of the codes within the brackets.

## Predicted Entities

`loinc_code`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_LOINC/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/24.Improved_Entity_Resolvers_in_SparkNLP_with_sBert.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_loinc_augmented_en_5.0.0_3.0_1690896071392.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_loinc_augmented_en_5.0.0_3.0_1690896071392.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

`sbiobertresolve_loinc_augmented` resolver model must be used with `sbiobert_base_cased_mli` as embeddings.


<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols("document")\
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained('embeddings_clinical','en', 'clinical/models')\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner = MedicalNerModel.pretrained("ner_radiology", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")\
    .setWhiteList(['Test'])

chunk2doc = Chunk2Doc().setInputCols("ner_chunk").setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)


resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc_augmented","en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("loinc_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline_loinc = Pipeline(stages = [documentAssembler, sentenceDetector, tokenizer, word_embeddings, ner, ner_converter, chunk2doc, sbert_embedder, resolver])

data = spark.createDataFrame([["""The patient is a 22-year-old female with a history of obesity. She has a Body mass index (BMI) of 33.5 kg/m2, aspartate aminotransferase 64, and alanine aminotransferase 126."""]]).toDF("text")

results = pipeline_loinc.fit(data).transform(data)
```
```scala
val documentAssembler = DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = Tokenizer() 
    .setInputCols(Array("document"))
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_radiology", "en", "clinical/models") 
    .setInputCols(Array("sentence", "token", "embeddings")) 
    .setOutputCol("ner")

val ner_converter = NerConverter() 
    .setInputCols(Array("sentence", "token", "ner")) 
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Test"))

val chunk2doc = Chunk2Doc() 
    .setInputCols("ner_chunk") 
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en","clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc_augmented", "en", "clinical/models") 
    .setInputCols(Array("ner_chunk", "sbert_embeddings")) 
    .setOutputCol("loinc_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline_loinc = new Pipeline().setStages(Array(documentAssembler, sentenceDetector, tokenizer, word_embeddings, ner, ner_converter, chunk2doc, sbert_embedder, resolver))

val data = Seq("The patient is a 22-year-old female with a history of obesity. She has a Body mass index (BMI) of 33.5 kg/m2, aspartate aminotransferase 64, and alanine aminotransferase 126.").toDF("text")

val result = pipeline_loinc.fit(data).transform(data)
```

{:.nlu-block}
```python
import nlu
nlu.load("en.resolve.loinc.augmented").predict("""The patient is a 22-year-old female with a history of obesity. She has a Body mass index (BMI) of 33.5 kg/m2, aspartate aminotransferase 64, and alanine aminotransferase 126.""")
```
</div>

## Results

```bash
+-------+--------------------------+------+----------+----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
|sent_id|                 ner_chunk|entity|loinc_code|                                                                                           all_codes|                                                                                         resolutions|
+-------+--------------------------+------+----------+----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
|      1|                       BMI|  Test|   39156-5|39156-5:::LP241982-0:::89270-3:::100847-3:::8277-6:::LP65821-8:::LP65822-6:::LP253556-7:::LA21328...|BMI [Body mass index]:::BFI [BFI]:::BMI Est [Body mass index]:::BldA [Gas & ammonia panel]:::BSA ...|
|      1|aspartate aminotransferase|  Test|   14409-7|14409-7:::1916-6:::16324-6:::16325-3:::43822-6:::3082-5:::2325-9:::100739-2:::59245-1:::27344-1::...|Aspartate aminotransferase [Aspartate aminotransferase]:::Aspartate aminotransferase/Alanine amin...|
|      1|  alanine aminotransferase|  Test|   16324-6|16324-6:::16325-3:::1916-6:::14409-7:::59245-1:::100738-4:::25302-1:::1740-0:::43822-6:::76625-3:...|Alanine aminotransferase [Alanine aminotransferase]:::Alanine aminotransferase/Aspartate aminotra...|
+-------+--------------------------+------+----------+----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_loinc_augmented|
|Compatibility:|Healthcare NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[loinc_code]|
|Language:|en|
|Size:|912.5 MB|
|Case sensitive:|false|

## References

Trained on standard LOINC coding system.
