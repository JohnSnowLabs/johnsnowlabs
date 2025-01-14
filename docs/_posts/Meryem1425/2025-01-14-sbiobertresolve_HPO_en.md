---
layout: model
title: Entity Resolver for Human Phenotype Ontology
author: John Snow Labs
name: sbiobertresolve_HPO
date: 2025-01-14
tags: [licensed, en, clinical, entity_resolution, hpo]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.5.1
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps phenotypic abnormalities, medical terms associated with hereditary diseases, encountered in human to Human Phenotype Ontology (HPO) codes using sbiobert_base_cased_mli Sentence Bert Embeddings, and has faster load time, with a speedup of about 6X when compared to previous versions. Also the load process now is more memory friendly meaning that the maximum memory required during load time is smaller, reducing the chances of OOM exceptions, and thus relaxing hardware requirements.

## Predicted Entities

`This model returns Human Phenotype Ontology (HPO) codes for phenotypic abnormalities encountered in human diseases. It also returns associated codes from the following vocabularies for each HPO code: - SNOMEDCT_US - UMLS (Unified Medical Language System ) - ORPHA (international reference resource for information on rare diseases and orphan drugs) - EPCC (European Paediatric Cardiac Code - another region-specific or discipline-specific coding system related to healthcare or medical classification) - Fyler (unique identifier used within a specific coding system or database)`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_HPO_en_5.5.1_3.0_1736867087979.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_HPO_en_5.5.1_3.0_1736867087979.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

ner = MedicalNerModel.pretrained("ner_human_phenotype_gene_clinical", "en", "clinical/models") \
	  .setInputCols(["sentence", "token", "word_embeddings"]) \
	  .setOutputCol("ner")\

ner_converter = NerConverterInternal()\
	  .setInputCols(["sentence", "token", "ner"])\
	  .setOutputCol("ner_chunk")\
  	.setWhiteList(["HP"])

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("{name}", "en", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("hpo")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages = [document_assembler,
                                       sentenceDetectorDL,
                                       tokenizer,
                                       word_embeddings,
                                       ner,
                                       ner_converter,
                                       c2doc,
                                       sbert_embedder,
                                       resolver])

data = spark.createDataFrame([["""She is followed by Dr. X in our office and has a history of severe tricuspid regurgitation. On 05/12/08, preserved left and right ventricular systolic function, aortic sclerosis with apparent mild aortic stenosis. She has previously had a Persantine Myoview nuclear rest-stress test scan completed at ABCD Medical Center in 07/06 that was negative. She has had significant mitral valve regurgitation in the past being moderate, but on the most recent echocardiogram on 05/12/08, that was not felt to be significant. She does have a history of significant hypertension in the past. She has had dizzy spells and denies clearly any true syncope. She has had bradycardia in the past from beta-blocker therapy."""]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

ner = medical.NerModel.pretrained("ner_human_phenotype_gene_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "word_embeddings"]) \
    .setOutputCol("ner")\

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["HP"])

c2doc = nlp.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("{name}", "en", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("hpo")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = nlp.Pipeline().setStages([document_assembler,
                                       sentenceDetectorDL,
                                       tokenizer,
                                       word_embeddings,
                                       ner,
                                       ner_converter,
                                       c2doc,
                                       sbert_embedder,
                                       resolver])


data = spark.createDataFrame([["""She is followed by Dr. X in our office and has a history of severe tricuspid regurgitation. On 05/12/08, preserved left and right ventricular systolic function, aortic sclerosis with apparent mild aortic stenosis. She has previously had a Persantine Myoview nuclear rest-stress test scan completed at ABCD Medical Center in 07/06 that was negative. She has had significant mitral valve regurgitation in the past being moderate, but on the most recent echocardiogram on 05/12/08, that was not felt to be significant. She does have a history of significant hypertension in the past. She has had dizzy spells and denies clearly any true syncope. She has had bradycardia in the past from beta-blocker therapy."""]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)

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

val ner = MedicalNerModel.pretrained("ner_human_phenotype_gene_clinical","en","clinical/models")
  .setInputCols(Array("sentence","token","word_embeddings")) 
  .setOutputCol("ner") 

val ner_converter = new NerConverterInternal()
  .setInputCols(Array("sentence","token","ner")) 
  .setOutputCol("ner_chunk") 
  .setWhiteList(Array("HP")) 

val c2doc = new Chunk2Doc()
  .setInputCols("ner_chunk") 
  .setOutputCol("ner_chunk_doc") 

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
  .setInputCols(Array("ner_chunk_doc")) 
  .setOutputCol("sbert_embeddings") 
  .setCaseSensitive(false) 

val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_HPO","en","clinical/models")
  .setInputCols(Array("sbert_embeddings")) 
  .setOutputCol("resolution") 
  .setDistanceFunction("EUCLIDEAN") 

val resolver_pipeline = new Pipeline().setStages(Array(
  document_assembler, 
  sentenceDetectorDL, 
  tokenizer, 
  word_embeddings, 
  ner, 
  ner_converter, 
  c2doc, 
  sbert_embedder, 
  resolver))

val data = Seq([["""She is followed by Dr. X in our office and has a history of severe tricuspid regurgitation. On 05/12/08, preserved left and right ventricular systolic function, aortic sclerosis with apparent mild aortic stenosis. She has previously had a Persantine Myoview nuclear rest-stress test scan completed at ABCD Medical Center in 07/06 that was negative. She has had significant mitral valve regurgitation in the past being moderate, but on the most recent echocardiogram on 05/12/08, that was not felt to be significant. She does have a history of significant hypertension in the past. She has had dizzy spells and denies clearly any true syncope. She has had bradycardia in the past from beta-blocker therapy."""]]).toDF("text")

val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+--------------------------+-----+---+---------+----------+--------------------------+--------------------------------------------------------------------------------+
|                     chunk|begin|end|ner_label|resolution|               description|                                                                       all_codes|
+--------------------------+-----+---+---------+----------+--------------------------+--------------------------------------------------------------------------------+
|   tricuspid regurgitation|   67| 89|       HP|HP:0005180|   tricuspid regurgitation|Fyler:1161||SNOMEDCT_US:111287006||UMLS:C0040961:::EPCC:06.01.92||ICD-10:Q22....|
|           aortic stenosis|  197|211|       HP|HP:0001650|           aortic stenosis|Fyler:1411||SNOMEDCT_US:60573004||UMLS:C0003507:::SNOMEDCT_US:204368006||UMLS...|
|mitral valve regurgitation|  373|398|       HP|HP:0001653|mitral valve regurgitation|Fyler:1151||SNOMEDCT_US:48724000||UMLS:C0026266||UMLS:C3551535:::EPCC:06.02.9...|
|              hypertension|  555|566|       HP|HP:0000822|              hypertension|SNOMEDCT_US:24184005||SNOMEDCT_US:38341003||UMLS:C0020538||UMLS:C0497247:::-:...|
|               bradycardia|  655|665|       HP|HP:0001662|               bradycardia|SNOMEDCT_US:48867003||UMLS:C0428977:::Fyler:7013||SNOMEDCT_US:49710005||UMLS:...|
+--------------------------+-----+---+---------+----------+--------------------------+--------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_HPO|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[hpo_code]|
|Language:|en|
|Size:|120.6 MB|
|Case sensitive:|false|
