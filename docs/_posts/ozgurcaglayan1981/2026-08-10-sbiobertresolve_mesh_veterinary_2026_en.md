---
layout: model
title: Sentence Entity Resolver for MeSH Codes - Veterinary (sbiobert_base_cased_mli_onnx Embeddings)
author: John Snow Labs
name: sbiobertresolve_mesh_veterinary_2026
date: 2026-08-10
tags: [en, entity_resolution, licensed, clinical, mesh, sbiobert, veterinary]
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

Trained on the MeSH 2026 dataset, augmented by JSL with a veterinary-focused scope.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_mesh_veterinary_2026_en_6.4.1_3.4_1786395752523.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_mesh_veterinary_2026_en_6.4.1_3.4_1786395752523.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_mesh_veterinary_2026","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("mesh_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,\
    ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The dog was diagnosed with rabies and treated with vaccination; tick infestations were also noted, along with coccidiosis."]]).toDF("text")
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

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_mesh_veterinary_2026","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("mesh_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,\
    ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The dog was diagnosed with rabies and treated with vaccination; tick infestations were also noted, along with coccidiosis."]]).toDF("text")
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
    .pretrained("sbiobertresolve_mesh_veterinary_2026", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("mesh_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
))

val data = Seq("The dog was diagnosed with rabies and treated with vaccination; tick infestations were also noted, along with coccidiosis.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk         | entity    | MeSH Code   | Resolution        | all_k_results                                   | all_k_cosine_distances                     | all_k_resolutions                                                                   |
|:------------------|:----------|:------------|:------------------|:------------------------------------------------|:-------------------------------------------|:------------------------------------------------------------------------------------|
| rabies            | PROBLEM   | D011818     | rabies            | D011818:::D011820:::D018114:::C000639155        | 0.0000:::0.0501:::0.1049:::0.2105          | rabies:::rabies virus:::rabies virus group:::rickettsia gravesii                    |
| vaccination       | TREATMENT | D014611     | vaccination       | D014611:::D007114:::D032541:::D007117:::D007115 | 0.0000:::0.0467:::0.0803:::0.0802:::0.0872 | vaccination:::immunization:::mass vaccination:::booster vaccination:::immunizati... |
| tick infestations | PROBLEM   | D013984     | tick infestations | D013984:::D064927:::D017282:::D013987           | 0.0000:::0.0601:::0.0700:::0.0736          | tick infestations:::tick bites:::tick-borne infections:::tick parasite              |
| coccidiosis       | PROBLEM   | D003048     | coccidiosis       | D003048:::D003047:::D010229                     | 0.0000:::0.0423:::0.0941                   | coccidiosis:::coccidioides infection:::paracoccidioides infections                  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_mesh_veterinary_2026|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sbert_embeddings]|
|Output Labels:|[mesh_code]|
|Language:|en|
|Size:|538.8 MB|
|Case sensitive:|false|