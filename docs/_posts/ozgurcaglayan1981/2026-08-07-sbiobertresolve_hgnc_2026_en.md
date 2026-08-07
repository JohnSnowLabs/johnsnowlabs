---
layout: model
title: Sentence Entity Resolver for HGNC Gene Symbols (sbiobert_base_cased_mli_onnx Embeddings)
author: John Snow Labs
name: sbiobertresolve_hgnc_2026
date: 2026-08-07
tags: [en, entity_resolution, licensed, clinical, hgnc, gene, sbiobert]
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

This model maps gene symbols and official names to HUGO Gene Nomenclature Committee (HGNC) identifiers using `sbiobert_base_cased_mli_onnx` embeddings. Trained on the HGNC monthly release dated 2026-08-04.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_hgnc_2026_en_6.4.1_3.4_1786106342222.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_hgnc_2026_en_6.4.1_3.4_1786106342222.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("word_embeddings")

ner_model = MedicalNerModel.pretrained("ner_human_phenotype_gene_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["GENE"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_hgnc_2026","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[\
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,\
    ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["Genetic testing confirmed a pathogenic BRCA1 variant, and the report also flagged elevated risk associated with the EGFR and KRAS genes."]]).toDF("text")
result = pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("word_embeddings")

ner_model = medical.NerModel.pretrained("ner_human_phenotype_gene_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["GENE"])

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_hgnc_2026","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[\
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,\
    ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["Genetic testing confirmed a pathogenic BRCA1 variant, and the report also flagged elevated risk associated with the EGFR and KRAS genes."]]).toDF("text")
result = pipeline.fit(data).transform(data)
```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
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
    .pretrained("ner_human_phenotype_gene_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("GENE"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_hgnc_2026", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
))

val data = Seq("Genetic testing confirmed a pathogenic BRCA1 variant, and the report also flagged elevated risk associated with the EGFR and KRAS genes.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk   | entity   | HGNC Code   | Resolution                              | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   | all_k_aux_labels                                                                    |
|:------------|:---------|:------------|:----------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| BRCA1       | GENE     | HGNC:1100   | BRCA1 [BRCA1 DNA repair associated]     | HGNC:1100:::HGNC:18994:::HGNC:23057:::HGNC:28153:::HGNC:24170:::HGNC:11551:::HGN... | 0.0000:::0.0269:::0.0295:::0.0320:::0.0324:::0.0329:::0.0327:::0.0339:::0.0366::... | BRCA1 [BRCA1 DNA repair associated]:::BRSK1 [BR serine/threonine kinase 1]:::BRK... | protein-coding gene :: gene with protein product:::protein-coding gene :: gene w... |
| EGFR        | GENE     | HGNC:3236   | EGFR [epidermal growth factor receptor] | HGNC:3236:::HGNC:3229:::HGNC:3697:::HGNC:16898:::HGNC:12691:::HGNC:4194:::HGNC:2... | 0.0000:::0.0178:::0.0428:::0.0500:::0.0497:::0.0533:::0.0555:::0.0581:::0.0600::... | EGFR [epidermal growth factor receptor]:::EGF [epidermal growth factor]:::FGR [F... | protein-coding gene :: gene with protein product:::protein-coding gene :: gene w... |
| KRAS        | GENE     | HGNC:6407   | KRAS [KRas proto-oncogene, GTPase]      | HGNC:6407:::HGNC:58375:::HGNC:6406:::HGNC:56729:::HGNC:15865:::HGNC:6308:::HGNC:... | 0.0000:::0.1054:::0.1097:::0.1096:::0.1083:::0.1161:::0.1178:::0.1234:::0.1186::... | KRAS [KRas proto-oncogene, GTPase]:::KDNBY [KDM5D neighbour, Y-linked]:::KRASP1 ... | protein-coding gene :: gene with protein product:::non-coding RNA :: RNA, long n... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_hgnc_2026|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sbert_embeddings]|
|Output Labels:|[resolution]|
|Language:|en|
|Size:|260.2 MB|
|Case sensitive:|false|