---
layout: model
title: Sentence Entity Resolver for ICD-9-CM
author: John Snow Labs
name: sbiobertresolve_icd9
date: 2024-04-12
tags: [entity_resolution, licensed, en, icd9, clinical]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted medical entities to ICD-9-CM codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

## Predicted Entities

`ICD-9-CM Codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd9_en_5.3.1_3.0_1712955352372.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd9_en_5.3.1_3.0_1712955352372.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = Tokenizer()\
  .setInputCols(["sentence"])\
  .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
  .setInputCols(["sentence","token"])\
  .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
  .setInputCols(["sentence","token","embeddings"])\
  .setOutputCol("ner")

ner_converter = NerConverter()\
  .setInputCols(["sentence","token","ner"])\
  .setOutputCol("ner_chunk")\
  .setWhiteList(['PROBLEM'])

chunk2doc = Chunk2Doc()\
  .setInputCols("ner_chunk")\
  .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
  .setInputCols(["ner_chunk_doc"])\
  .setOutputCol("sbert_embeddings")\
  .setCaseSensitive(False)

icd9_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd9","en", "clinical/models") \
  .setInputCols(["sbert_embeddings"]) \
  .setOutputCol("resolution")\
  .setDistanceFunction("EUCLIDEAN")

nlpPipeline = Pipeline(
    stages=[
      document_assembler,
      sentence_detector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      chunk2doc,
      sbert_embedder,
      icd9_resolver])


clinical_note = ["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and type two diabetes mellitus, associated with an acute alcoholic hepatitis and obesity."""]


data= spark.createDataFrame([clinical_note]).toDF('text')
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

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence","token"))
  .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence","token","embeddings"))
  .setOutputCol("ner")

val ner_converter = new NerConverter()
  .setInputCols(Array("sentence","token","ner"))
  .setOutputCol("ner_chunk")
  .setWhiteList(Array("PROBLEM"))

val chunk2doc = new Chunk2Doc()
  .setInputCols("ner_chunk")
  .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("sbert_embeddings")
  .setCaseSensitive(False)

val icd9_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd9","en", "clinical/models") 
  .setInputCols(Array("sbert_embeddings")) 
  .setOutputCol("resolution")
  .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(
    Array(
        document_assembler, 
        sentence_detector, 
        tokenizer, 
        word_embeddings, 
        clinical_ner, 
        ner_converter, 
        chunk2doc, 
        sbert_embedder, 
        icd9_resolver))

val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and type two diabetes mellitus, associated with an acute alcoholic hepatitis and obesity.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------------+-------+---------+------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|                        chunk| entity|ıcd9_code|                                                        resolution|                                                                   all_k_results|                                                               all_k_resolutions|
+-----------------------------+-------+---------+------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|gestational diabetes mellitus|PROBLEM|   V12.21|hx gestational diabetes [Personal history of gestational diabetes]|V12.21:::775.1:::V18.0:::249:::250:::249.7:::249.71:::249.9:::249.61:::648.0:...|hx gestational diabetes [Personal history of gestational diabetes]:::neonat d...|
|   type two diabetes mellitus|PROBLEM|      249|         secondary diabetes mellitus [Secondary diabetes mellitus]|249:::250:::V18.0:::775.1:::249.7:::249.71:::249.9:::249.6:::V77.1:::249.5:::...|secondary diabetes mellitus [Secondary diabetes mellitus]:::diabetes mellitus...|
| an acute alcoholic hepatitis|PROBLEM|    571.1|             acute alcoholic hepatitis [Acute alcoholic hepatitis]|571.1:::303.0:::571.2:::303.01:::303.02:::571.0:::902.22:::070.0:::864.19:::0...|acute alcoholic hepatitis [Acute alcoholic hepatitis]:::acute alcoholic intox...|
|                      obesity|PROBLEM|    278.0|                   overweight and obesity [Overweight and obesity]|278.0:::278.01:::278.02:::649.11:::V77.8:::278.00:::278:::649.12:::729.31:::2...|overweight and obesity [Overweight and obesity]:::morbid obesity [Morbid obes...|
+-----------------------------+-------+---------+------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd9|
|Compatibility:|Healthcare NLP 5.3.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[icd9cm_code]|
|Language:|en|
|Size:|86.7 MB|
|Case sensitive:|false|
