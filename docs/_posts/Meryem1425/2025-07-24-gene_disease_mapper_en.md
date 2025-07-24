---
layout: model
title: Gene To Disease Mapping
author: John Snow Labs
name: gene_disease_mapper
date: 2025-07-24
tags: [licensed, en, gene, disease, mapping]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.0.4
spark_version: 3.4
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps genes to their related diseases. It also returns all the possible diseases in the `all_k_resolutions` in the metadata.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/gene_disease_mapper_en_6.0.4_3.4_1753329447602.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/gene_disease_mapper_en_6.0.4_3.4_1753329447602.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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


mapperModel = ChunkMapperModel.pretrained("gene_disease_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["disease"])
    
nlp_pipeline = Pipeline(stages=[document_assembler, 
                                sentence_detector, 
                                tokenizer, 
                                word_embeddings, 
                                clinical_ner, 
                                ner_converter, 
                                mapperModel])

model = nlp_pipeline.fit(spark.createDataFrame([['']]).toDF("text"))

result = model.transform(spark.createDataFrame([["We will systematically examine seven genes (CHN1, MDH1, and SNAP25) that are altered in the three neurodegenerative diseases."]]).toDF("text"))

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


mapperModel = medical.ChunkMapperModel.pretrained("gene_disease_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["disease"])
    
nlp_pipeline = nlp.Pipeline(stages=[document_assembler, 
                                    sentence_detector, 
                                    tokenizer, 
                                    word_embeddings, 
                                    clinical_ner, 
                                    ner_converter, 
                                    mapperModel])

model = nlp_pipeline.fit(spark.createDataFrame([['']]).toDF("text"))

result = model.transform(spark.createDataFrame([["We will systematically examine seven genes (CHN1, MDH1, and SNAP25) that are altered in the three neurodegenerative diseases."]]).toDF("text"))

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

val mapperModel = ChunkMapperModel.pretrained("gene_disease_mapper", "en", "clinical/models")
    .setInputCols("ner_chunk")
    .setOutputCol("mappings")
    .setRels(Array("disease"))
    
val nlp_pipeline = new Pipeline().setStages(Array(document_assembler, 
                                                  sentence_detector, 
                                                  tokenizer, 
                                                  word_embeddings, 
                                                  clinical_ner, 
                                                  ner_converter, 
                                                  mapperModel))

val data = Seq("""\We will systematically examine seven genes (CHN1, MDH1, and SNAP25) that are altered in the three neurodegenerative diseases."""\).toDF("text")

val result = nlp_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  gene|                  disease|                                                                                                                                                                                       all_k_resolutions|
+------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  CHN1|preaxial hand polydactyly|preaxial hand polydactyly:::brachydactyly:::marcus gunn jaw winking synkinesis:::triphalangeal thumb:::duane anomaly:::seizure:::global developmental delay:::irregular hyperpigmentation:::ectopic k...|
|  MDH1|        hyperglutamatemia|hyperglutamatemia:::hypertonia:::seizure:::global developmental delay:::infra-orbital crease:::hypsarrhythmia:::partial agenesis of the corpus callosum:::autosomal recessive inheritance:::axial hyp...|
|SNAP25|              poor speech|poor speech:::poor head control:::proximal muscle weakness:::motor delay:::gait disturbance:::bulbar palsy:::areflexia:::seizure:::hypotonia:::ataxia:::intellectual disability:::hyporeflexia:::dysa...|
+------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|gene_disease_mapper|
|Compatibility:|Healthcare NLP 6.0.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|1.6 MB|