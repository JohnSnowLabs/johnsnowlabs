---
layout: model
title: Sentence Entity Resolver for Billable ICD10-CM HCC Codes
author: John Snow Labs
name: sbiobertresolve_icd10cm_augmented_billable_hcc
date: 2023-05-31
tags: [licensed, en, clinical, hcc, icd10cm, entity_resolution]
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

This model maps extracted medical entities to ICD-10-CM codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings and it supports 7-digit codes with Hierarchical Condition Categories (HCC) status. It has been updated by dropping the invalid codes that exist in the previous versions. In the result, look for the `all_k_aux_labels` parameter in the metadata to get HCC status. The HCC status can be divided to get further information: `billable status`, `hcc status`, and `hcc score`. For example if the result is `1||1||8`: `the billable status is 1`, `hcc status is 1`, and `hcc score is 8`.

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_ICD10_CM/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_augmented_billable_hcc_en_4.4.2_3.0_1685507415461.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_augmented_billable_hcc_en_4.4.2_3.0_1685507415461.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

`sbiobertresolve_icd10cm_augmented_billable_hcc` resolver model must be used with `sbiobert_base_cased_mli` as embeddings.

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

icd_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_augmented_billable_hcc", "en", "clinical/models") \
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

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."""]]).toDF("text")

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

val icd10_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_augmented_billable_hcc", "en", "clinical/models")
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

val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection.").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------------------------------+-------+----------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
|                            ner_chunk| entity|icd10_code|                                                                resolutions|                                                                  all_codes|                                                                   hcc_list|
+-------------------------------------+-------+----------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
|        gestational diabetes mellitus|PROBLEM|     O24.4|[gestational diabetes mellitus [gestational diabetes mellitus], gestatio...|      [O24.4, O24.41, O24.43, Z86.32, Z87.5, O24.31, O24.11, O24.1, O24.81]|[0||0||0, 0||0||0, 0||0||0, 1||0||0, 0||0||0, 0||0||0, 0||0||0, 0||0||0,...|
|subsequent type two diabetes mellitus|PROBLEM|    O24.11|[pre-existing type 2 diabetes mellitus [pre-existing type 2 diabetes mel...|[O24.11, E11.8, E11, E13.9, E11.9, E11.3, E11.44, Z86.3, Z86.39, E11.32,...|[0||0||0, 1||1||18, 0||0||0, 1||1||19, 1||1||19, 0||0||0, 1||1||18, 0||0...|
|                              obesity|PROBLEM|     E66.9|[obesity [obesity, unspecified], abdominal obesity [other obesity], obes...|[E66.9, E66.8, Z68.41, Q13.0, E66, E66.01, Z86.39, E34.9, H35.50, Z83.49...|[1||0||0, 1||0||0, 1||1||22, 1||0||0, 0||0||0, 1||1||22, 1||0||0, 1||0||...|
|                    a body mass index|PROBLEM|    Z68.41|[finding of body mass index [body mass index [bmi] 40.0-44.9, adult], ob...|[Z68.41, E66.9, R22.9, Z68.1, R22.3, R22.1, Z68, R22.2, R22.0, R41.89, M...|[1||1||22, 1||0||0, 1||0||0, 1||0||0, 0||0||0, 1||0||0, 0||0||0, 1||0||0...|
|                             polyuria|PROBLEM|       R35|[polyuria [polyuria], nocturnal polyuria [nocturnal polyuria], polyuric ...|[R35, R35.81, R35.8, E23.2, R31, R35.0, R82.99, N40.1, E72.3, O04.8, R30...|[0||0||0, 1||0||0, 0||0||0, 1||1||23, 0||0||0, 1||0||0, 0||0||0, 1||0||0...|
|                           polydipsia|PROBLEM|     R63.1|[polydipsia [polydipsia], psychogenic polydipsia [other impulse disorder...|[R63.1, F63.89, E23.2, F63.9, O40, G47.5, M79.89, R63.2, R06.1, H53.8, I...|[1||0||0, 1||0||0, 1||1||23, 1||0||0, 0||0||0, 0||0||0, 1||0||0, 1||0||0...|
|                        poor appetite|PROBLEM|     R63.0|[poor appetite [anorexia], poor feeding [feeding problem of newborn, uns...|[R63.0, P92.9, R43.8, R43.2, E86, R19.6, F52.0, Z72.4, R06.89, Z76.89, R...|[1||0||0, 1||0||0, 1||0||0, 1||0||0, 0||0||0, 1||0||0, 1||0||0, 1||0||0,...|
|                             vomiting|PROBLEM|     R11.1|[vomiting [vomiting], intermittent vomiting [nausea and vomiting], vomit...|          [R11.1, R11, R11.10, G43.A1, P92.1, P92.09, G43.A, R11.13, R11.0]|[0||0||0, 0||0||0, 1||0||0, 1||0||0, 1||0||0, 1||0||0, 0||0||0, 1||0||0,...|
|        a respiratory tract infection|PROBLEM|     J98.8|[respiratory tract infection [other specified respiratory disorders], up...|[J98.8, J06.9, A49.9, J22, J20.9, Z59.3, T17, J04.10, Z13.83, J18.9, P28...|[1||0||0, 1||0||0, 1||0||0, 1||0||0, 1||0||0, 1||0||0, 0||0||0, 1||0||0,...|
+-------------------------------------+-------+----------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd10cm_augmented_billable_hcc|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|1.4 GB|
|Case sensitive:|false|
