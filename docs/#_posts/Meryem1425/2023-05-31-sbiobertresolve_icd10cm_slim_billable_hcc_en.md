---
layout: model
title: Sentence Entity Resolver for Billable ICD10-CM HCC Codes (sbiobertresolve_icd10cm_slim_billable_hcc)
author: John Snow Labs
name: sbiobertresolve_icd10cm_slim_billable_hcc
date: 2023-05-31
tags: [licensed, en, clinical, icd10cm, entity_resolution]
task: Entity Resolution
language: en
edition: Healthcare NLP 4.4.2
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted clinical entities to ICD-10-CM codes using `sbiobert_base_cased_mli` sentence bert embeddings. In this model, synonyms having low cosine similarity to unnormalized terms are dropped. It returns the official resolution text within the brackets and also provides billable and Hierarchical Condition Categories (HCC) information of the codes in `all_k_aux_labels` parameter in the metadata. This column can be divided to get further details: `billable status || hcc status || hcc score`. For example, if `all_k_aux_labels` is like `1||1||19` which means the `billable status` is 1, `hcc status` is 1, and `hcc score` is 19.

## Predicted Entities

`ICD-10-CM Codes`, `billable status`, `hcc status`, `hcc score`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_ICD10_CM/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/ER_ICD10_CM.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_slim_billable_hcc_en_4.4.2_3.0_1685500916240.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_slim_billable_hcc_en_4.4.2_3.0_1685500916240.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")\

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc") 

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

icd_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_slim_billable_hcc", "en", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages = [document_assembler,
                                       sentenceDetectorDL,
                                       tokenizer,
                                       word_embeddings,
                                       ner,
                                       ner_converter,
                                       c2doc,
                                       sbert_embedder,
                                       icd_resolver])

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."""]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)
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
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList("PROBLEM")

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols("ner_chunk_doc")
    .setOutputCol("sbert_embeddings")

val icd10_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_slim_billable_hcc","en", "clinical/models")
    .setInputCols("sbert_embeddings") 
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(document_assembler, 
                               sentence_detector, 
                               tokenizer, 
                               word_embeddings, 
                               clinical_ner, 
                               ner_converter, 
                               chunk2doc, 
                               sbert_embedder, 
                               icd10_resolver))

val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection.").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------------------------------+-------+----------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
|                            ner_chunk| entity|icd10_code|                                                                resolutions|                                                                  all_codes|                                                                   hcc_list|
+-------------------------------------+-------+----------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
|        gestational diabetes mellitus|PROBLEM|     O24.4|[gestational diabetes mellitus [gestational diabetes mellitus], gestatio...|[O24.4, O24.41, Z86.32, O24.11, O24.81, P70.2, O24.01, O24.42, O24.414, ...|[0||0||0, 0||0||0, 1||0||0, 0||0||0, 0||0||0, 1||0||0, 0||0||0, 0||0||0,...|
|subsequent type two diabetes mellitus|PROBLEM|       E11|[type 2 diabetes mellitus [type 2 diabetes mellitus], type 2 diabetes me...|[E11, E11.62, E11.5, E11.69, E11.59, E09, E11.6, E11.8, E11.4, E11.628, ...|[0||0||0, 0||0||0, 0||0||0, 1||1||18, 1||1||18, 0||0||0, 0||0||0, 1||1||...|
|                              obesity|PROBLEM|       E66|[overweight and obesity [overweight and obesity], overweight [overweight...|[E66, E66.3, E66.8, E66.0, E66.1, E88.81, E66.09, E66.01, E34.4, E66.9, ...|[0||0||0, 1||0||0, 1||0||0, 0||0||0, 1||0||0, 1||0||0, 1||0||0, 1||1||22...|
|                    a body mass index|PROBLEM|       Z68|[body mass index [bmi] [body mass index [bmi]], localized adiposity [loc...|[Z68, E65, L02.221, Z96.81, Y92.81, Y93.75, L02.23, L02.22, M67.49, R73,...|[0||0||0, 1||0||0, 1||0||0, 1||0||0, 0||0||0, 1||0||0, 0||0||0, 0||0||0,...|
|                             polyuria|PROBLEM|       R35|[polyuria [polyuria], nocturnal polyuria [nocturnal polyuria], other pol...|[R35, R35.81, R35.89, R35.8, R31, R30.0, E72.01, R80, R34, R82.4, R82.99...|[0||0||0, 1||0||0, 1||0||0, 0||0||0, 0||0||0, 1||0||0, 1||1||23, 0||0||0...|
|                           polydipsia|PROBLEM|     R63.1|[polydipsia [polydipsia], polyhydramnios [polyhydramnios], parasomnia [p...|[R63.1, O40, G47.5, R63.2, R00.2, G47.1, G47.13, F51.11, G47.19, L68.3, ...|[1||0||0, 0||0||0, 0||0||0, 1||0||0, 1||0||0, 0||0||0, 1||0||0, 1||0||0,...|
|                             vomiting|PROBLEM|     R11.1|[vomiting [vomiting], cyclical vomiting [cyclical vomiting], nausea [nau...|[R11.1, G43.A, R11.0, R11, R11.14, R11.12, R23.1, G47.51, R11.10, H57.03...|[0||0||0, 0||0||0, 1||0||0, 0||0||0, 1||0||0, 1||0||0, 1||0||0, 1||0||0,...|
|        a respiratory tract infection|PROBLEM|       T17|[foreign body in respiratory tract [foreign body in respiratory tract], ...|[T17, T81.4, T81.81, J95.851, T17.8, Z87.0, J44.0, J06, T81.44, Z22, T17...|[0||0||0, 0||0||0, 0||0||0, 1||1||114, 0||0||0, 0||0||0, 1||1||111, 0||0...|
+-------------------------------------+-------+----------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd10cm_slim_billable_hcc|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|435.3 MB|
|Case sensitive:|false|
