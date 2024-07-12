---
layout: model
title: Sentence Entity Resolver for Billable ICD10-CM HCC Codes (sbertresolve_icd10cm_slim_billable_hcc)
author: John Snow Labs
name: sbertresolve_icd10cm_slim_billable_hcc
date: 2023-05-31
tags: [icd10cm, licensed, slim, en, clinical]
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

This model maps clinical entities and concepts to ICD-10-CM codes using sentence bert embeddings. In this model, synonyms having low cosine similarity to unnormalized terms are dropped. It also returns the official resolution text within the brackets inside the metadata. The model is augmented with synonyms, and previous augmentations are flexed according to cosine distances to unnormalized terms (ground truths).

Outputs 7-digit billable ICD codes. In the result, look for aux_label parameter in the metadata to get Hierarchical Condition Categories (HCC) status. This column can be divided to get further details: `billable status || hcc status || hcc score`. For example, if `all_k_aux_labels` is like `1||1||19` which means the `billable status` is 1, `hcc status` is 1, and `hcc score` is 19.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/24.Improved_Entity_Resolvers_in_SparkNLP_with_sBert.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbertresolve_icd10cm_slim_billable_hcc_en_4.4.2_3.0_1685498851777.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbertresolve_icd10cm_slim_billable_hcc_en_4.4.2_3.0_1685498851777.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverter()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(['PROBLEM'])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

bert_embeddings = BertSentenceEmbeddings.pretrained("sbert_jsl_medium_uncased", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bert_embeddings")\
    .setCaseSensitive(False)

icd10_resolver = SentenceEntityResolverModel.SentenceEntityResolverModel.pretrained("sbertresolve_icd10cm_slim_billable_hcc", "en", "clinical/models")\
    .setInputCols(["bert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

nlpPipeline = Pipeline(stages=[document_assembler, 
                               sentence_detector, 
                               tokenizer, 
                               word_embeddings, 
                               clinical_ner, 
                               ner_converter, 
                               chunk2doc, 
                               bert_embeddings, 
                               icd10_resolver])

data_ner = spark.createDataFrame([["A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin."]]).toDF("text")


results = nlpPipeline.fit(data_ner).transform(data_ner)
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

val bert_embeddings = BertSentenceEmbeddings.pretrained("sbert_jsl_medium_uncased", "en", "clinical/models")
    .setInputCols("ner_chunk_doc")
    .setOutputCol("bert_embeddings")
    .setCaseSensitive(False)

val icd10_resolver = SentenceEntityResolverModel.pretrained("sbertresolve_icd10cm_slim_billable_hcc", "en", "clinical/models")
    .setInputCols("bert_embeddings")
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")
    
val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, clinical_ner, ner_converter, chunk2doc, sbert_embedder, icd10_resolver))

val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin.").toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------------------------------+-------+----------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
|                            ner_chunk| entity|icd10_code|                                                                resolutions|                                                                  all_codes|
+-------------------------------------+-------+----------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
|        gestational diabetes mellitus|PROBLEM|     O24.4|[gestational diabetes mellitus [gestational diabetes mellitus], gestatio...|[O24.4, O24.43, P70.2, O24.434, O24.430, O24.435, O24.41, E13, O24.13, O...|
|subsequent type two diabetes mellitus|PROBLEM|       E11|[type 2 diabetes mellitus [type 2 diabetes mellitus], type 1 diabetes me...|[E11, E10, E11.3, E11.65, E11.1, E10.3, E11.64, E11.0, E11.5, E10.59, E1...|
|                              obesity|PROBLEM|     E66.1|[drug-induced obesity [drug-induced obesity], obesity due to excess calo...|[E66.1, E66.0, E66.9, O99.210, O99.213, O99.212, E66, O99.211, E66.8, E6...|
|                    a body mass index|PROBLEM|       Z68|[body mass index [bmi] [body mass index [bmi]], body mass index [bmi] 70...|[Z68, Z68.45, Z68.4, Z68.1, Z68.2, Z68.22, Z68.21, Z68.25, Z68.43, Z68.2...|
|                             polyuria|PROBLEM|       R35|[polyuria [polyuria], biliuria [biliuria], chyluria [chyluria], anuria a...|[R35, R82.2, R82.0, R34, R80, R35.89, R35.8, R82.991, R82.4, D75.1, L68....|
|                           polydipsia|PROBLEM|     R63.1|[polydipsia [polydipsia], polymyositis [polymyositis], polyhydramnios [p...|[R63.1, M33.2, O40, F63.3, Q69, O15, K22.81, N89.7, M30.0, N47.1, D72.82...|
|                             vomiting|PROBLEM|     R11.1|[vomiting [vomiting], vomiting of newborn [vomiting of newborn], nausea ...|[R11.1, P92.0, R11, R11.12, G43.A, R11.0, R11.13, R11.14, P92.01, O21, O...|
+-------------------------------------+-------+----------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbertresolve_icd10cm_slim_billable_hcc|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|297.8 MB|
|Case sensitive:|false|
