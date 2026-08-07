---
layout: model
title: Sentence Entity Resolver for HGNC Gene Symbols (BGE (bge_base_en_v1_5_onnx) Embeddings)
author: John Snow Labs
name: bgeresolve_hgnc_2026
date: 2026-08-07
tags: [en, entity_resolution, licensed, clinical, hgnc, gene, bge]
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

This model maps gene symbols and official names to HUGO Gene Nomenclature Committee (HGNC) identifiers using `bge_base_en_v1_5_onnx` embeddings. Trained on the HGNC monthly release dated 2026-08-04.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_hgnc_2026_en_6.4.1_3.4_1786107676486.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_hgnc_2026_en_6.4.1_3.4_1786107676486.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

resolver = SentenceEntityResolverModel.pretrained("bgeresolve_hgnc_2026","en","clinical/models")\
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

resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_hgnc_2026","en","clinical/models")\
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
    .pretrained("bgeresolve_hgnc_2026", "en", "clinical/models")
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
| BRCA1       | GENE     | HGNC:1100   | BRCA1 [BRCA1 DNA repair associated]     | HGNC:1100:::HGNC:28470:::HGNC:58363:::HGNC:950:::HGNC:25008:::HGNC:952:::HGNC:10... | 0.0000:::0.0776:::0.1256:::0.1898:::0.1937:::0.2021:::0.2026:::0.2085:::0.2163::... | BRCA1 [BRCA1 DNA repair associated]:::BRCA1P1 [BRCA1 pseudogene 1]:::BRCA1-OT1 [... | protein-coding gene :: gene with protein product:::pseudogene :: pseudogene:::no... |
| EGFR        | GENE     | HGNC:3236   | EGFR [epidermal growth factor receptor] | HGNC:3236:::HGNC:3229:::HGNC:40207:::HGNC:9600:::HGNC:49511:::HGNC:3420:::HGNC:8... | 0.0000:::0.1528:::0.1778:::0.2075:::0.2304:::0.2435:::0.2572:::0.2609:::0.2622::... | EGFR [epidermal growth factor receptor]:::EGF [epidermal growth factor]:::EGFR-A... | protein-coding gene :: gene with protein product:::protein-coding gene :: gene w... |
| KRAS        | GENE     | HGNC:6407   | KRAS [KRas proto-oncogene, GTPase]      | HGNC:6407:::HGNC:52478:::HGNC:10447:::HGNC:17271:::HGNC:6406:::HGNC:5174:::HGNC:... | 0.0000:::0.2407:::0.2640:::0.2939:::0.2941:::0.3015:::0.3102:::0.3116:::0.3197::... | KRAS [KRas proto-oncogene, GTPase]:::NTRAS [non-coding transcript regulating alt... | protein-coding gene :: gene with protein product:::non-coding RNA :: RNA, long n... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_hgnc_2026|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[resolution]|
|Language:|en|
|Size:|260.7 MB|
|Case sensitive:|false|