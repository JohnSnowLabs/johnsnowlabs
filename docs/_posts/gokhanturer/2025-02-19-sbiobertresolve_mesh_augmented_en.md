---
layout: model
title: Sentence Entity Resolver for MeSH (sbiobert_base_cased_mli embeddings) - Augmented
author: John Snow Labs
name: sbiobertresolve_mesh_augmented
date: 2025-02-19
tags: [en, licensed, clinical, entity_resolution, mesh]
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

This model maps clinical entities to Medical Subject Heading (MeSH) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. In this model, MeSH descriptors, supplementary concepts, and pharmacologic actions datasets were used. 
 
Descriptors: Main subject headings representing biomedical concepts (e.g., "Diabetes Mellitus").
 
Supplementary Concepts: Additional terms, including chemicals and drugs, mapped to existing descriptors.
 
Pharmacologic Actions: Terms describing the biological effects of drugs and chemicals (e.g., "Anti-Inflammatory Agents")

## Predicted Entities

`mesh_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_mesh_augmented_en_5.5.2_3.0_1739977582730.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_mesh_augmented_en_5.5.2_3.0_1739977582730.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
	.setOutputCol("ner_chunk")

chunk2doc = Chunk2Doc()\
	.setInputCols("ner_chunk")\
	.setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli",'en','clinical/models')\
        .setInputCols(["ner_chunk_doc"])\
        .setOutputCol("sbert_embeddings")\
        .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_mesh_augmented","en","clinical/models") \
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

text = """She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. At this time, chest tube placement occurred and thoracoscopy with fluid biopsies, which were performed, revealed malignant mesothelioma."""

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

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_mesh_augmented","en","clinical/models") \
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

text = """She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. At this time, chest tube placement occurred and thoracoscopy with fluid biopsies, which were performed, revealed malignant mesothelioma."""

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

val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_mesh_augmented","en","clinical/models")
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

val data = Seq("""She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. At this time, chest tube placement occurred and thoracoscopy with fluid biopsies, which were performed, revealed malignant mesothelioma.""").toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------------------+-----+---+---------+----------+----------------------+--------------------------------------------------------------------------------+
|                     chunk|begin|end|ner_label|resolution|           description|                                                                       all_codes|
+--------------------------+-----+---+---------+----------+----------------------+--------------------------------------------------------------------------------+
|                chest pain|   38| 47|  PROBLEM|   D002637|            chest pain|D002637:::D005157:::D059350:::D019547:::D015746:::D059226:::D020069:::D010146...|
|bilateral pleural effusion|   67| 92|  PROBLEM|   D010996|      pleural effusion|D010996:::D000069258:::D010490:::D016066:::D010995:::D011654:::D010998:::D016...|
|             the pathology|  140|152|     TEST|   D010336|             pathology|D010336:::D062528:::D037521:::D010335:::D002828:::D014774:::D020763:::C000630...|
|        the pericardectomy|  168|185|TREATMENT|   D010492|        pericardectomy|D010492:::D010491:::D011670:::D061645:::D002387:::D018700:::D064727:::D000069...|
|              mesothelioma|  226|237|  PROBLEM|   D008654|          mesothelioma|                              D008654:::D054363:::D000086002:::D018261:::D018301|
|      chest tube placement|  254|273|TREATMENT|   D015505|            chest tube|D015505:::D000069258:::D019616:::D013907:::D035441:::D013896:::D012121:::D002...|
|     drainage of the fluid|  279|299|  PROBLEM|   C026239|         bouin's fluid|C026239:::D019152:::D005440:::D004322:::D014882:::D013396:::D015916:::D014906...|
|              thoracoscopy|  314|325|TREATMENT|   D013906|          thoracoscopy|D013906:::D020708:::D035423:::D013907:::D000069258:::D013905:::D013897:::D035...|
|            fluid biopsies|  332|345|     TEST|D000073890|       liquid biopsies|D000073890:::D001706:::D005440:::D001707:::D001992:::C026239:::D010533:::D001...|
|    malignant mesothelioma|  385|406|  PROBLEM|D000086002|malignant mesothelioma|                              D000086002:::D008654:::D054363:::D018261:::C535700|
+--------------------------+-----+---+---------+----------+----------------------+--------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_mesh_augmented|
|Compatibility:|Healthcare NLP 5.5.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[mesh_code]|
|Language:|en|
|Size:|2.9 GB|
|Case sensitive:|false|
