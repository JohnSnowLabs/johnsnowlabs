---
layout: model
title: Sentence Entity Resolver for HGNC Gene Symbols - Augmented (BGE (bge_base_en_v1_5_onnx) Embeddings)
author: John Snow Labs
name: bgeresolve_hgnc_augmented_2026
date: 2026-08-07
tags: [en, entity_resolution, licensed, clinical, hgnc, gene, bge, augmented]
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

This model maps gene symbols, official names, and their known alias/previous symbols and names to HUGO Gene Nomenclature Committee (HGNC) identifiers using `bge_base_en_v1_5_onnx` embeddings. Trained on the HGNC monthly release dated 2026-08-04.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_hgnc_augmented_2026_en_6.4.1_3.4_1786109830398.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_hgnc_augmented_2026_en_6.4.1_3.4_1786109830398.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("bgeresolve_hgnc_augmented_2026","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

embedder = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_hgnc_augmented_2026","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

val embedder = BGEEmbeddings
    .pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("bgeresolve_hgnc_augmented_2026", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
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
| BRCA1       | GENE     | HGNC:1100   | BRCA1 [BRCA1 DNA repair associated]     | HGNC:1100:::HGNC:28470:::HGNC:950:::HGNC:58363:::HGNC:20473:::HGNC:25008:::HGNC:... | 0.0000:::0.0776:::0.1254:::0.1256:::0.1322:::0.1937:::0.1971:::0.1986:::0.2021::... | BRCA1 [BRCA1 DNA repair associated]:::BRCA1P1 [BRCA1 pseudogene 1]:::BRCA1 assoc... | protein-coding gene :: gene with protein product:::pseudogene :: pseudogene:::pr... |
| EGFR        | GENE     | HGNC:3236   | EGFR [epidermal growth factor receptor] | HGNC:3236:::HGNC:20561:::HGNC:54482:::HGNC:7029:::HGNC:3229:::HGNC:5465:::HGNC:4... | 0.0000:::0.0938:::0.1377:::0.1402:::0.1528:::0.1632:::0.1778:::0.1923:::0.2075::... | EGFR [epidermal growth factor receptor]:::EGFR-RS [rhomboid 5 homolog 1]:::Lnc-E... | protein-coding gene :: gene with protein product:::protein-coding gene :: gene w... |
| KRAS        | GENE     | HGNC:6407   | KRAS [KRas proto-oncogene, GTPase]      | HGNC:6407:::HGNC:6406:::HGNC:17898:::HGNC:10447:::HGNC:7989:::HGNC:25121:::HGNC:... | 0.0000:::0.2075:::0.2275:::0.2300:::0.2397:::0.2404:::0.2407:::0.2457:::0.2547::... | KRAS [KRas proto-oncogene, GTPase]:::KRAS1P [KRas proto-oncogene, GTPase pseudog... | protein-coding gene :: gene with protein product:::pseudogene :: pseudogene:::pr... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_hgnc_augmented_2026|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[resolution]|
|Language:|en|
|Size:|566.3 MB|
|Case sensitive:|false|