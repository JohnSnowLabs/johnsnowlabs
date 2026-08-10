---
layout: model
title: Sentence Entity Resolver for MeSH Codes (sbiobert_base_cased_mli_onnx Embeddings)
author: John Snow Labs
name: sbiobertresolve_mesh_2026
date: 2026-08-10
tags: [en, entity_resolution, licensed, clinical, mesh, sbiobert]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical/veterinary entities to MeSH (Medical Subject Headings) Unique Identifiers (UI) using `sbiobert_base_cased_mli_onnx` Sentence Embeddings.

Trained on the MeSH 2026 dataset (NLM-native descriptors, entry terms, supplemental concept records, and pharmacologic actions only).

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_mesh_2026_en_6.4.1_3.4_1786392589795.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_mesh_2026_en_6.4.1_3.4_1786392589795.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("word_embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

chunk2doc = Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_mesh_2026","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("mesh_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,\
    ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The patient has a long history of diabetes mellitus and hypertension, and presented today with pneumonia and possible myocardial infarction."]]).toDF("text")
result = pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("word_embeddings")

ner_model = medical.NerModel.pretrained("ner_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_mesh_2026","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("mesh_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,\
    ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The patient has a long history of diabetes mellitus and hypertension, and presented today with pneumonia and possible myocardial infarction."]]).toDF("text")
result = pipeline.fit(data).transform(data)
```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("word_embeddings")

val ner_model = MedicalNerModel
    .pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val chunk2doc = new Chunk2Doc()
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("ner_chunk_doc")

val embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_mesh_2026", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("mesh_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
))

val data = Seq("The patient has a long history of diabetes mellitus and hypertension, and presented today with pneumonia and possible myocardial infarction.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk             | entity   | MeSH Code   | Resolution            | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:----------------------|:---------|:------------|:----------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| diabetes mellitus     | PROBLEM  | D003920     | diabetes mellitus     | D003920:::D048909:::D003922:::D003924:::D000099074:::D003923:::D005905:::D003921    | 0.0000:::0.0271:::0.0333:::0.0445:::0.0479:::0.0647:::0.0800:::0.0790               | diabetes mellitus:::complications of diabetes mellitus:::insulin-dependent diabe... |
| hypertension          | PROBLEM  | D006973     | hypertension          | D006973:::D000075222:::D000802:::C072778:::D059468:::D000092244:::D058246:::D009... | 0.0000:::0.0340:::0.0350:::0.0403:::0.0457:::0.0636:::0.0685:::0.0735:::0.0789::... | hypertension:::essential hypertension:::hypertensin:::hypertensive factor:::hype... |
| pneumonia             | PROBLEM  | D011014     | pneumonia             | D011014:::D000092124:::D018410:::D011020:::D000098968:::D011015:::D007711:::D000... | 0.0000:::0.0754:::0.0891:::0.1197:::0.1175:::0.1202:::0.1271:::0.1243:::0.1296::... | pneumonia:::organizing pneumonia:::bacterial pneumonia:::pneumonia, pcp:::commun... |
| myocardial infarction | PROBLEM  | D009203     | myocardial infarction | D009203:::D056989:::D056988:::D000072657:::D002544:::D020243                        | 0.0000:::0.0269:::0.0306:::0.0354:::0.0547:::0.0583                                 | myocardial infarction:::inferior myocardial infarction:::anterior wall myocardia... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_mesh_2026|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sbert_embeddings]|
|Output Labels:|[mesh_code]|
|Language:|en|
|Size:|1.7 GB|
|Case sensitive:|false|