---
layout: model
title: Relation Extraction between Test and Results (ReDL)
author: John Snow Labs
name: redl_oncology_test_result_biobert
date: 2024-07-03
tags: [licensed, en, clinical, oncology, relation_extraction, tensorflow, test]
task: Relation Extraction
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.0
supported: true
engine: tensorflow
annotator: RelationExtractionDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This relation extraction model links test extractions to their corresponding results.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/redl_oncology_test_result_biobert_en_5.3.3_3.0_1720047204001.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/redl_oncology_test_result_biobert_en_5.3.3_3.0_1720047204001.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\ .setInputCol("text")\ .setOutputCol("document")
sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
.setInputCols(["document"])
.setOutputCol("sentence")

tokenizer = Tokenizer()
.setInputCols(["sentence"])
.setOutputCol("token")

word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")
.setInputCols(["sentence", "token"])
.setOutputCol("embeddings")

ner = MedicalNerModel.pretrained("ner_oncology_wip", "en", "clinical/models")
.setInputCols(["sentence", "token", "embeddings"])
.setOutputCol("ner")

ner_converter = NerConverterInternal()
.setInputCols(["sentence", "token", "ner"])
.setOutputCol("ner_chunk")

pos_tagger = PerceptronModel.pretrained("pos_clinical", "en", "clinical/models")
.setInputCols(["sentence", "token"])
.setOutputCol("pos_tags")

dependency_parser = DependencyParserModel.pretrained("dependency_conllu", "en")
.setInputCols(["sentence", "pos_tags", "token"])
.setOutputCol("dependencies")

re_ner_chunk_filter = RENerChunksFilter()
.setInputCols(["ner_chunk", "dependencies"])
.setOutputCol("re_ner_chunk")
.setMaxSyntacticDistance(10)
.setRelationPairs(["Biomarker-Biomarker_Result", "Biomarker_Result-Biomarker", "Oncogene-Biomarker_Result", "Biomarker_Result-Oncogene", "Pathology_Test-Pathology_Result", "Pathology_Result-Pathology_Test"])

re_model = RelationExtractionDLModel.pretrained("redl_oncology_test_result_biobert_wip", "en", "clinical/models")
.setInputCols(["re_ner_chunk", "sentence"])
.setOutputCol("relation_extraction")

pipeline = Pipeline(stages=[document_assembler, sentence_detector, tokenizer, word_embeddings, ner, ner_converter, pos_tagger, dependency_parser, re_ner_chunk_filter, re_model])

data = spark.createDataFrame([["Pathology showed tumor cells, which were positive for estrogen and progesterone receptors."]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

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
    
val word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                
    
val ner = MedicalNerModel.pretrained("ner_oncology_wip", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")
    
val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pos_tagger = PerceptronModel.pretrained("pos_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("pos_tags")
    
val dependency_parser = DependencyParserModel.pretrained("dependency_conllu", "en")
    .setInputCols(Array("sentence", "pos_tags", "token"))
    .setOutputCol("dependencies")

val re_ner_chunk_filter = new RENerChunksFilter()
     .setInputCols(Array("ner_chunk", "dependencies"))
     .setOutputCol("re_ner_chunk")
     .setMaxSyntacticDistance(10)
     .setRelationPairs(Array("Biomarker-Biomarker_Result", "Biomarker_Result-Biomarker", "Oncogene-Biomarker_Result", "Biomarker_Result-Oncogene", "Pathology_Test-Pathology_Result", "Pathology_Result-Pathology_Test"))

val re_model = RelationExtractionDLModel.pretrained("redl_oncology_test_result_biobert_wip", "en", "clinical/models")
      .setPredictionThreshold(0.5f)
      .setInputCols(Array("re_ner_chunk", "sentence"))
      .setOutputCol("relation_extraction")

val pipeline = new Pipeline().setStages(Array(document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter,
                            pos_tagger,
                            dependency_parser,
                            re_ner_chunk_filter,
                            re_model))

val data = Seq("Pathology showed tumor cells, which were positive for estrogen and progesterone receptors.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-------------+----------------+-------------+-----------+---------+----------------+-------------+-----------+--------------------+----------+
|     relation|         entity1|entity1_begin|entity1_end|   chunk1|         entity2|entity2_begin|entity2_end|              chunk2|confidence|
+-------------+----------------+-------------+-----------+---------+----------------+-------------+-----------+--------------------+----------+
|is_finding_of|  Pathology_Test|            0|          8|Pathology|Pathology_Result|           17|         27|         tumor cells| 0.8494344|
|is_finding_of|Biomarker_Result|           41|         48| positive|       Biomarker|           54|         61|            estrogen|0.99451536|
|is_finding_of|Biomarker_Result|           41|         48| positive|       Biomarker|           67|         88|progesterone rece...|0.99218905|
+-------------+----------------+-------------+-----------+---------+----------------+-------------+-----------+--------------------+----------+
 
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|redl_oncology_test_result_biobert|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[re_ner_chunk, sentence]|
|Output Labels:|[relation_extraction]|
|Language:|en|
|Size:|405.4 MB|