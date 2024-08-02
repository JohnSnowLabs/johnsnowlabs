---
layout: model
title: Sentence Entity Resolver for ICD10-CM (Augmented)
author: John Snow Labs
name: sbiobertresolve_icd10cm_augmented
date: 2023-05-20
tags: [icd10cm, entity_resolution, clinical, en, licensed]
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

This model maps extracted medical entities to ICD10-CM codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. Also, it has been augmented with synonyms for making it more accurate and returns the official resolution text within the brackets.

## Predicted Entities

`ICD10CM Codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_augmented_en_4.4.2_3.0_1684591054927.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_augmented_en_4.4.2_3.0_1684591054927.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

chunk2doc = Chunk2Doc().setInputCols("ner_chunk").setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")

icd10_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_augmented","en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

nlpPipeline = Pipeline(stages=[document_assembler, sentence_detector, tokenizer, word_embeddings, clinical_ner, ner_converter, chunk2doc, sbert_embedder, icd10_resolver])

data_ner = spark.createDataFrame([["A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."]]).toDF("text")

results = nlpPipeline.fit(data_ner).transform(data_ner)
```
```scala
val document_assembler = DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")


val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")


val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings")


val clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner")

val ner_converter = NerConverter()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("PROBLEM"))


val chunk2doc = Chunk2Doc().setInputCols("ner_chunk").setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")

val icd10_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_augmented","en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, clinical_ner, ner_converter, chunk2doc, sbert_embedder, icd10_resolver))

val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection.").toDF("text")

val result = pipeline.fit(data).transform(data)
```

{:.nlu-block}
```python
import nlu
nlu.load("en.resolve.icd10cm.augmented").predict("""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection.""")
```
</div>

## Results

```bash
+-------------------------------------+-------+------------+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
|                            ner_chunk| entity|icd10cm_code|                                                           resolutions                                       |                                                             all_codes|
+-------------------------------------+-------+------------+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
|        gestational diabetes mellitus|PROBLEM|       O24.4|gestational diabetes mellitus [gestational diabetes mellitus], gestational diabetes mellitus [gestational... |O24.4, O24.41, O24.43, Z86.32, Z87.5, O24.31, O24.11, O24.1, O24.81...|
|subsequent type two diabetes mellitus|PROBLEM|      O24.11|pre-existing type 2 diabetes mellitus [pre-existing type 2 diabetes mellitus], disorder associated with t... |O24.11, E11.8, E11, E13.9, E11.9, E11.3, E11.44, Z86.3, Z86.39, E11...|
|                              obesity|PROBLEM|       E66.9|obesity [obesity], abdominal obesity [abdominal obesity], obese [obese], central obesity [central obesity... |E66.9, E66.8, Z68.41, Q13.0, E66, E66.01, Z86.39, E34.9, H35.50, Z8...|
|                    a body mass index|PROBLEM|      Z68.41|finding of body mass index [finding of body mass index], observation of body mass index [observation of b... |Z68.41, E66.9, R22.9, Z68.1, R22.3, R22.1, Z68, R22.2, R22.0, R41.8...|
|                             polyuria|PROBLEM|         R35|polyuria [polyuria], nocturnal polyuria [nocturnal polyuria], polyuric state [polyuric state], polyuric ...  |R35, R35.81, R35.8, E23.2, R35.89, R31, R35.0, R82.99, N40.1, E72.3...|
|                           polydipsia|PROBLEM|       R63.1|polydipsia [polydipsia], psychogenic polydipsia [psychogenic polydipsia], primary polydipsia [primary po...  |R63.1, F63.89, E23.2, F63.9, O40, G47.5, M79.89, R63.2, R06.1, H53....|
|                        poor appetite|PROBLEM|       R63.0|poor appetite [poor appetite], poor feeding [poor feeding], bad taste in mouth [bad taste in mouth], unp...  |R63.0, P92.9, R43.8, R43.2, E86, R19.6, F52.0, Z72.4, R06.89, Z76.8...|
|                             vomiting|PROBLEM|       R11.1|vomiting [vomiting], intermittent vomiting [intermittent vomiting], vomiting symptoms [vomiting symptom...   |R11.1, R11, R11.10, G43.A1, P92.1, P92.09, G43.A, R11.13, R11.0       |
|        a respiratory tract infection|PROBLEM|       J98.8|respiratory tract infection [respiratory tract infection], upper respiratory tract infection [upper respi... |J98.8, J06.9, A49.9, J22, J20.9, Z59.3, T17, J04.10, Z13.83, J18.9 ...|
+-------------------------------------+-------+------------+----------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd10cm_augmented|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|1.5 GB|
|Case sensitive:|false|

## References

Trained on ICD10CM 2023 Codes dataset: https://www.cdc.gov/nchs/icd/icd10cm.htm
