---
layout: model
title: Mapping ICD10CM Codes To Chronic Indicators
author: John Snow Labs
name: icd10cm_chronic_indicator_mapper
date: 2024-10-02
tags: [licensed, en, clinical, mapping, icd10cm, chronic, chronic_indicator]
task: Chunk Mapping
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This mapper model links ICD-10-CM codes to their corresponding chronicity indicators.
The `chronic indicator` can have three different values;
 
- `0`: "not chronic"
- `1`: "chronic"
- `9`: "no determination"

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_chronic_indicator_mapper_en_5.4.1_3.0_1727865931204.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_chronic_indicator_mapper_en_5.4.1_3.0_1727865931204.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("clinical_ner")

clinical_ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","clinical_ner"])\
    .setOutputCol("clinical_ner_chunk")\
    .setWhiteList(['PROBLEM'])

chunk2doc = Chunk2Doc() \
    .setInputCols("clinical_ner_chunk") \
    .setOutputCol("doc_chunk")

sbiobert_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["doc_chunk"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

icd_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_augmented_billable_hcc","en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("icd10cm")\
    .setDistanceFunction("EUCLIDEAN")

doc2chunk = Doc2Chunk()\
    .setInputCols(['icd10cm'])\
    .setOutputCol('chunk')

mapperModel = ChunkMapperModel.pretrained("icd10cm_chronic_indicator_mapper","en", "clinical/models")\
    .setInputCols(["chunk"])\
    .setOutputCol("chronic_indicator_mapping")\
    .setRels(["chronic_indicator"])

pipeline = Pipeline(
    stages=[
      document_assembler,
      sentence_detector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      clinical_ner_converter,
      chunk2doc,
      sbiobert_embeddings,
      icd_resolver,
      doc2chunk,
      mapperModel
      ])

data = spark.createDataFrame([["""A 42-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with besity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."""]]).toDF("text")

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

val clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("clinical_ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "clinical_ner"))
    .setOutputCol("clinical_ner_chunk")
    .setWhiteList((Array("PROBLEM"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("clinical_ner_chunk")
    .setOutputCol("doc_chunk")

val sbiobert_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["doc_chunk"])
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(False)

val icd_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_augmented_billable_hcc","en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) 
    .setOutputCol("icd10cm")
    .setDistanceFunction("EUCLIDEAN")

val doc2chunk = new Doc2Chunk()
      .setInputCols(["icd10cm"])
      .setOutputCol("chunk")

val mapperModel = ChunkMapperModel.pretrained("icd10cm_chronic_indicator_mapper","en", "clinical/models")\
    .setInputCols(["chunk"])
    .setOutputCol("chronic_indicator_mapping")
    .setRels(["chronic_indicator"])

val pipeline = new Pipeline().setStages(Array(
      document_assembler,
      sentence_detector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      clinical_ner_converter,
      chunk2doc,
      sbiobert_embeddings,
      icd_resolver,
      doc2chunk,
      mapperModel))

val data = Seq("""A 42-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with besity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection.""").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-----------+-----+---+-------------------------------------+-------+-------+------------------------------------------------------------------------------------------+-----------------+
|sentence_id|begin|end|                               entity|  label|icd10cm|                                                                                resolution|chronic_indicator|
+-----------+-----+---+-------------------------------------+-------+-------+------------------------------------------------------------------------------------------+-----------------+
|          0|   39| 67|        gestational diabetes mellitus|PROBLEM|  O24.4|                             gestational diabetes mellitus [gestational diabetes mellitus]|                0|
|          0|  117|153|subsequent type two diabetes mellitus|PROBLEM| O24.11|pre-existing type 2 diabetes mellitus [pre-existing type 2 diabetes mellitus, in pregna...|                1|
|          0|  172|178|                              obesity|PROBLEM|  E66.9|                                                            obesity [obesity, unspecified]|                1|
|          0|  185|201|                    a body mass index|PROBLEM| Z68.41|                       finding of body mass index [body mass index [bmi] 40.0-44.9, adult]|                9|
|          0|  261|268|                             polyuria|PROBLEM|    R35|                                                                       polyuria [polyuria]|                0|
|          0|  271|280|                           polydipsia|PROBLEM|  R63.1|                                                                   polydipsia [polydipsia]|                0|
|          0|  283|295|                        poor appetite|PROBLEM|  R63.0|                                                                  poor appetite [anorexia]|                0|
|          0|  302|309|                             vomiting|PROBLEM|  R11.1|                                                                       vomiting [vomiting]|                0|
|          1|  403|431|        a respiratory tract infection|PROBLEM|  J98.8|                       respiratory tract infection [other specified respiratory disorders]|                0|
+-----------+-----+---+-------------------------------------+-------+-------+------------------------------------------------------------------------------------------+-----------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_chronic_indicator_mapper|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|1.0 MB|
