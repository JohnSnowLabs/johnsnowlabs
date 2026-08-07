---
layout: model
title: Sentence Entity Resolver for HGNC Gene Symbols (BioLORD (mpnet_embeddings_biolord_2023_c) Embeddings)
author: John Snow Labs
name: biolordresolve_hgnc_2026
date: 2026-08-07
tags: [en, entity_resolution, licensed, clinical, hgnc, gene, biolord]
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

This model maps gene symbols and official names to HUGO Gene Nomenclature Committee (HGNC) identifiers using `mpnet_embeddings_biolord_2023_c` embeddings. Trained on the HGNC monthly release dated 2026-08-04.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_hgnc_2026_en_6.4.1_3.4_1786107013832.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_hgnc_2026_en_6.4.1_3.4_1786107013832.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)\
    .setBatchSize(1)

resolver = SentenceEntityResolverModel.pretrained("biolordresolve_hgnc_2026","en","clinical/models")\
    .setInputCols(["embeddings"])\
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

embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)\
    .setBatchSize(1)

resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_hgnc_2026","en","clinical/models")\
    .setInputCols(["embeddings"])\
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

val embedder = MPNetEmbeddings
    .pretrained("mpnet_embeddings_biolord_2023_c", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("embeddings")
    .setCaseSensitive(false)
    .setBatchSize(1)

val resolver = SentenceEntityResolverModel
    .pretrained("biolordresolve_hgnc_2026", "en", "clinical/models")
    .setInputCols(Array("embeddings"))
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
| BRCA1       | GENE     | HGNC:1100   | BRCA1 [BRCA1 DNA repair associated]     | HGNC:1100:::HGNC:1101:::HGNC:28470:::HGNC:58363:::HGNC:25008:::HGNC:1099:::HGNC:... | 0.0000:::0.0690:::0.0980:::0.1656:::0.1882:::0.1962:::0.2005:::0.2085:::0.2125::... | BRCA1 [BRCA1 DNA repair associated]:::BRCA2 [BRCA2 DNA repair associated]:::BRCA... | protein-coding gene :: gene with protein product:::protein-coding gene :: gene w... |
| EGFR        | GENE     | HGNC:3236   | EGFR [epidermal growth factor receptor] | HGNC:3236:::HGNC:3229:::HGNC:40207:::HGNC:26810:::HGNC:3235:::HGNC:9600:::HGNC:2... | 0.0000:::0.1780:::0.2620:::0.2658:::0.2740:::0.2741:::0.2873:::0.2949:::0.3080::... | EGFR [epidermal growth factor receptor]:::EGF [epidermal growth factor]:::EGFR-A... | protein-coding gene :: gene with protein product:::protein-coding gene :: gene w... |
| KRAS        | GENE     | HGNC:6407   | KRAS [KRas proto-oncogene, GTPase]      | HGNC:6407:::HGNC:6406:::HGNC:7108:::HGNC:4021:::HGNC:6215:::HGNC:5176:::HGNC:303... | 0.0000:::0.2699:::0.3207:::0.3300:::0.3371:::0.3408:::0.3481:::0.3614:::0.3659::... | KRAS [KRas proto-oncogene, GTPase]:::KRASP1 [KRas proto-oncogene, GTPase pseudog... | protein-coding gene :: gene with protein product:::pseudogene :: pseudogene:::pr... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_hgnc_2026|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[resolution]|
|Language:|en|
|Size:|260.8 MB|
|Case sensitive:|false|