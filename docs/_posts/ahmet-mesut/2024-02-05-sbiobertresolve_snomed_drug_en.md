---
layout: model
title: Sentence Entity Resolver for SNOMED Concepts, Drug version (sbiobert_base_cased_mli embeddings)
author: John Snow Labs
name: sbiobertresolve_snomed_drug
date: 2024-02-05
tags: [licensed, en, snomed, drug, resolver]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps detected drug entities to SNOMED codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_drug_en_5.2.1_3.0_1707136788526.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_drug_en_5.2.1_3.0_1707136788526.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = Tokenizer()\
  .setInputCols(["sentence"])\
  .setOutputCol("token")\

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
  .setInputCols(["sentence", "token"])\
  .setOutputCol("embeddings")

ner_posology = MedicalNerModel.pretrained("ner_posology", "en", "clinical/models") \
  .setInputCols(["sentence", "token", "embeddings"]) \
  .setOutputCol("ner_posology")

ner_posology_converter = NerConverterInternal() \
  .setInputCols(["sentence", "token", "ner_posology"]) \
  .setOutputCol("ner_posology_chunk")\
  .setWhiteList(['DRUG'])

chunk2doc = Chunk2Doc()\
  .setInputCols("ner_chunk")\
  .setOutputCol("ner_chunk_doc")

sbert_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
  .setInputCols(["ner_chunk_doc"])\
  .setOutputCol("sbert_embeddings")\
  .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_drug", "en", "clinical/models") \
  .setInputCols(["sbert_embeddings"]) \
  .setOutputCol("snomed_code")\

snomed_pipeline = Pipeline(stages = [
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_posology,
    ner_posology_converter,
    chunk2doc,
    sbert_embeddings,
    snomed_resolver
])


data = spark.createDataFrame([["""The patient is a 30-year-old female with a long history of insulin-dependent diabetes, type 2; coronary artery disease; chronic renal insufficiency; peripheral vascular disease, also secondary to diabetes; who was originally admitted to an outside hospital for what appeared to be acute paraplegia, lower extremities. She did receive a course of Bactrim for 14 days for UTI."""]]).toDF("text")

model = snomed_pipeline.fit(data)
result = model.transform(data)
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
    
val ner_posology = MedicalNerModel.pretrained("ner_posology","en","clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner_posology")
    
val ner_posology_converter = new NerConverterInternal()
    .setInputCols(Array("sentence","token","ner_posology"))
    .setOutputCol("ner_posology_chunk")
    .setWhiteList(Array("DRUG"))
    
val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_posology_chunk")
    .setOutputCol("ner_chunk_doc")
    
val sbert_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)
    
val snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_drug","en","clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("snomed_code")
    
val snomed_pipeline = new Pipeline().setStages(Array( 
         document_assembler, 
         sentence_detector, 
         tokenizer, 
         word_embeddings, 
         ner_posology, 
         ner_posology_converter, 
         chunk2doc, 
         sbert_embeddings, 
         snomed_resolver ))
    
val data = Seq("""She is given Enoxaparin 4000 units subcutaneously daily, folic acid 1 mg daily,levothyroxine 0.1 mg p.o. daily,aspirin 81 mg daily, Haloperidol 150 mg p.o. t.i.d.,magnesium citrate 1 bottle p.o. p.r.n.,sliding scale coverage insulin.""").toDF("text")
    
val model = snomed_pipeline.fit(data)
    
val result = model.transform(data)
```
</div>

## Results

```bash
+-----------------+-----+-----------+------------------------------------+--------------------------------------------------+--------------------------------------------------+
|            chunk|label|snomed_code|                          resolution|                                         all_codes|                                   all_resolutions|
+-----------------+-----+-----------+------------------------------------+--------------------------------------------------+--------------------------------------------------+
|       Enoxaparin| DRUG|  372562003|                          enoxaparin|372562003:::108983001:::108984007:::421012002::...|enoxaparin:::enoxaparin sodium:::enoxaparin-con...|
|       folic acid| DRUG|   63718003|                          folic acid|63718003:::6247001:::226316008:::432165000:::43...|folic acid:::folic acid-containing product:::fo...|
|    levothyroxine| DRUG|  768532006|    levothyroxine-containing product|768532006:::126202002:::768531004:::101938009::...|levothyroxine-containing product:::levothyroxin...|
|          aspirin| DRUG|  387458008|                             aspirin|387458008:::7947003:::411561009:::426365001:::9...|aspirin:::aspirin-containing product:::aspirin ...|
|      Haloperidol| DRUG|  386837002|                         haloperidol|386837002:::10756001:::386531008:::412197008:::...|haloperidol:::haloperidol-containing product:::...|
|magnesium citrate| DRUG|   12495006|magnesium citrate-containing product|12495006:::387401007:::387117008:::387202002:::...|magnesium citrate-containing product:::magnesiu...|
|          insulin| DRUG|   67866001|                             insulin|67866001:::325072002:::414515005:::39487003:::4...|insulin:::insulin aspart:::insulin detemir:::in...|
+-----------------+-----+-----------+------------------------------------+--------------------------------------------------+--------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_drug|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|228.7 MB|
|Case sensitive:|false|