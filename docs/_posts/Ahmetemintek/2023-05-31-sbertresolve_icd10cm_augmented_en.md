---
layout: model
title: Sentence Entity Resolver for ICD-10-CM Codes (sbertresolve_icd10cm_augmented)
author: John Snow Labs
name: sbertresolve_icd10cm_augmented
date: 2023-05-31
tags: [en, clinical, licensed, icd10cm, entity_resolution]
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

This model maps clinical entities and concepts to ICD-10-CM codes using `sbert_jsl_medium_uncased` sentence bert embeddings. It also returns the official resolution text within the brackets inside the metadata. The model is augmented with synonyms, and previous augmentations are flexed according to cosine distances to unnormalized terms (ground truths).

## Predicted Entities

`ICD-10-CM Codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbertresolve_icd10cm_augmented_en_4.4.2_3.0_1685531969657.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbertresolve_icd10cm_augmented_en_4.4.2_3.0_1685531969657.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

bert_embeddings = BertSentenceEmbeddings.pretrained("sbert_jsl_medium_uncased", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bert_embeddings")\
    .setCaseSensitive(False)

icd10_resolver = SentenceEntityResolverModel.pretrained("sbertresolve_icd10cm_augmented", "en", "clinical/models")\
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

data_ner = spark.createDataFrame([["A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, three years prior to presentation, associated with acute hepatitis, and obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting."]]).toDF("text")

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

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("PROBLEM"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val bert_embeddings = BertSentenceEmbeddings.pretrained("sbert_jsl_medium_uncased", "en", "clinical/models")
    .setInputCols("ner_chunk_doc")
    .setOutputCol("bert_embeddings")
    .setCaseSensitive(False)

val icd10_resolver = SentenceEntityResolverModel.pretrained("sbertresolve_icd10cm_augmented", "en", "clinical/models")
    .setInputCols("bert_embeddings")
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")
    
val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, clinical_ner, ner_converter, chunk2doc, sbert_embedder, icd10_resolver))

val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, three years prior to presentation, associated with acute hepatitis, and obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting.").toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------------------------------+-------+----------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
|                            ner_chunk| entity|icd10_code|                                                                resolutions|                                                                  all_codes|
+-------------------------------------+-------+----------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
|        gestational diabetes mellitus|PROBLEM|     O24.4|[gestational diabetes mellitus [gestational diabetes mellitus], maternal...|     [O24.4, O24.41, O24.43, Z86.32, K86.8, P70.2, O24.434, E10.9, O24.430]|
|subsequent type two diabetes mellitus|PROBLEM|       E11|[type 2 diabetes mellitus [type 2 diabetes mellitus], type ii diabetes m...|[E11, E11.9, E10.9, E10, E13.9, Z83.3, L83, E11.8, E11.32, E10.8, Z86.39...|
|                      acute hepatitis|PROBLEM|     K72.0|[acute hepatitis [acute and subacute hepatic failure], acute hepatitis a...|[K72.0, B15, B17.2, B17.1, B16, B17.9, B18.8, B15.9, K75.2, K73.9, B17.1...|
|                              obesity|PROBLEM|     E66.9|[obesity [obesity, unspecified], upper body obesity [other obesity], chi...|                                  [E66.9, E66.8, P90, Q13.0, M79.4, Z86.39]|
|                    a body mass index|PROBLEM|     E66.9|[observation of body mass index [obesity, unspecified], finding of body ...|[E66.9, Z68.41, Z68, E66.8, Z68.45, Z68.4, Z68.1, Z68.2, R22.9, Z68.22, ...|
|                             polyuria|PROBLEM|       R35|[polyuria [polyuria], sialuria [other specified metabolic disorders], st...|[R35, E88.8, R30.0, N28.89, O04.8, R82.4, E74.8, R82.2, E73.9, R82.0, R3...|
|                           polydipsia|PROBLEM|     R63.1|[polydipsia [polydipsia], polyotia [accessory auricle], polysomia [conjo...|[R63.1, Q17.0, Q89.4, Q89.09, Q74.8, H53.8, H53.2, Q13.2, R63.8, E23.2, ...|
|                        poor appetite|PROBLEM|     R63.0|[poor appetite [anorexia], excessive appetite [polyphagia], poor feeding...|[R63.0, R63.2, P92.9, R45.81, Z55.8, R41.84, R41.3, Z74.8, R46.89, R45.8...|
|                             vomiting|PROBLEM|     R11.1|[vomiting [vomiting], vomiting bile [vomiting following gastrointestinal...|[R11.1, K91.0, K92.0, A08.39, R11, P92.0, P92.09, R11.12, R11.10, O21.9,...|
+-------------------------------------+-------+----------+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbertresolve_icd10cm_augmented|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|938.1 MB|
|Case sensitive:|false|