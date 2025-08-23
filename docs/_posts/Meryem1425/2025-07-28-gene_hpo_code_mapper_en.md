---
layout: model
title: Gene To HPO Code Mapping
author: John Snow Labs
name: gene_hpo_code_mapper
date: 2025-07-28
tags: [licensed, en, gene, hpo, mapping]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.0.4
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps genes to their corresponding HPO codes. It also returns all the possible HPO codes in the `all_k_resolutions` in the metadata.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/gene_hpo_code_mapper_en_6.0.4_3.0_1753715435916.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/gene_hpo_code_mapper_en_6.0.4_3.0_1753715435916.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_human_phenotype_gene_clinical_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["GENE"])


mapperModel = ChunkMapperModel.pretrained("gene_hpo_code_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["hpo_code"])
    
nlp_pipeline = Pipeline(stages=[document_assembler, 
                                sentence_detector, 
                                tokenizer, 
                                word_embeddings, 
                                clinical_ner, 
                                ner_converter, 
                                mapperModel])

model = nlp_pipeline.fit(spark.createDataFrame([['']]).toDF("text"))

result = model.transform(spark.createDataFrame([["""We will systematically examine seven genes (CHN1, MDH1, and SNAP25) that are altered in the three neurodegenerative diseases."""]]).toDF("text"))


```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
     
sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = medical.NerModel.pretrained("ner_human_phenotype_gene_clinical_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["GENE"])

mapperModel = medical.ChunkMapperModel.pretrained("gene_hpo_code_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["hpo_code"])
    
nlp_pipeline = nlp.Pipeline(stages=[document_assembler, 
                                    sentence_detector, 
                                    tokenizer, 
                                    word_embeddings, 
                                    clinical_ner, 
                                    ner_converter, 
                                    mapperModel])

model = nlp_pipeline.fit(spark.createDataFrame([['']]).toDF("text"))

result = model.transform(spark.createDataFrame([["""We will systematically examine seven genes (CHN1, MDH1, and SNAP25) that are altered in the three neurodegenerative diseases."""]]).toDF("text"))


```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
     
val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_human_phenotype_gene_clinical_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("GENE"))

val mapperModel = ChunkMapperModel.pretrained("gene_hpo_code_mapper", "en", "clinical/models")
    .setInputCols("ner_chunk")
    .setOutputCol("mappings")
    .setRels(Array("hpo_code"))
    
val nlp_pipeline = new Pipeline().setStages(Array(document_assembler, 
                                sentence_detector, 
                                tokenizer, 
                                word_embeddings, 
                                clinical_ner, ner_converter, 
                                mapperModel))

val sample_texts = Seq("""We will systematically examine seven genes (CHN1, MDH1, and SNAP25) that are altered in the three neurodegenerative diseases.""").toDF("text")

val result = nlp_pipeline.fit(sample_texts).transform(sample_texts)

```
</div>

## Results

```bash

+------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  gene|  hpo_code|                                                                                                                                                                                       all_k_resolutions|
+------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  CHN1|HP:0001177|HP:0001177:::HP:0001156:::HP:0025186:::HP:0001199:::HP:0009921:::HP:0001250:::HP:0001263:::HP:0007400:::HP:0000086:::HP:0001357:::HP:0000006:::HP:0003974:::HP:0000175:::HP:0003312:::HP:0009601:::HP...|
|  MDH1|HP:0500149|HP:0500149:::HP:0001276:::HP:0001250:::HP:0001263:::HP:0100876:::HP:0002521:::HP:0001338:::HP:0000007:::HP:0008936:::HP:0012110:::HP:0200134:::HP:0007068:::HP:0000253:::HP:0000232:::HP:0001510:::HP...|
|SNAP25|HP:0002465|HP:0002465:::HP:0002421:::HP:0003701:::HP:0001270:::HP:0001288:::HP:0001283:::HP:0001284:::HP:0001250:::HP:0001252:::HP:0001251:::HP:0001249:::HP:0001265:::HP:0001260:::HP:0001263:::HP:0002515:::HP...|
+------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|gene_hpo_code_mapper|
|Compatibility:|Healthcare NLP 6.0.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|733.1 KB|
