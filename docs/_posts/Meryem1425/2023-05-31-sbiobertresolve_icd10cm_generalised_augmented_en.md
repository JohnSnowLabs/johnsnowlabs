---
layout: model
title: Sentence Entity Resolver for ICD-10-CM (general 3 character codes - augmented)
author: John Snow Labs
name: sbiobertresolve_icd10cm_generalised_augmented
date: 2023-05-31
tags: [licensed, en, clinical, entity_resolution, icd10cm]
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

This model maps extracted medical entities to ICD-10-CM codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. It predicts ICD-10-CM codes up to 3 characters (according to ICD-10-CM code structure the first three characters represent general type of the injury or disease).

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_ICD10_CM/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/24.Improved_Entity_Resolvers_in_SparkNLP_with_sBert.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_generalised_augmented_en_4.4.2_3.0_1685508789416.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_generalised_augmented_en_4.4.2_3.0_1685508789416.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")

icd10_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_generalised_augmented","en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

nlpPipeline = Pipeline(stages=[document_assembler, 
                               sentence_detector, 
                               tokenizer, 
                               word_embeddings, 
                               clinical_ner, 
                               ner_converter, 
                               chunk2doc, 
                               sbert_embedder, 
                               icd10_resolver])

data = spark.createDataFrame([["A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."]]).toDF("text")

results = nlpPipeline.fit(data).transform(data)
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

val icd10_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_generalised_augmented","en", "clinical/models")
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
+-------------------------------------+-------+----------+---------------------------------------------------------------------------+-----------------------------------------------------------------+
|                            ner_chunk| entity|icd10_code|                                                                resolutions|                                                        all_codes|
+-------------------------------------+-------+----------+---------------------------------------------------------------------------+-----------------------------------------------------------------+
|        gestational diabetes mellitus|PROBLEM|       O24|[gestational diabetes mellitus [gestational diabetes mellitus], history ...|                                                  [O24, Z86, Z87]|
|subsequent type two diabetes mellitus|PROBLEM|       O24|[pre-existing type 2 diabetes mellitus [pre-existing type 2 diabetes mel...|                                             [O24, E11, E13, Z86]|
|                              obesity|PROBLEM|       E66|[obesity [obesity, unspecified], obese [body mass index [bmi] 40.0-44.9,...|                         [E66, Z68, Q13, Z86, E34, H35, Z83, Q55]|
|                    a body mass index|PROBLEM|       Z68|[finding of body mass index [body mass index [bmi] 40.0-44.9, adult], ob...|                    [Z68, E66, R22, R41, M62, P29, R19, R89, M21]|
|                             polyuria|PROBLEM|       R35|[polyuria [polyuria], polyuric state (disorder) [diabetes insipidus], he...|[R35, E23, R31, R82, N40, E72, O04, R30, R80, E88, N03, P96, N02]|
|                           polydipsia|PROBLEM|       R63|[polydipsia [polydipsia], psychogenic polydipsia [other impulse disorder...|[R63, F63, E23, O40, G47, M79, R06, H53, I44, Q30, I45, R00, M35]|
|                        poor appetite|PROBLEM|       R63|[poor appetite [anorexia], poor feeding [feeding problem of newborn, uns...|[R63, P92, R43, E86, R19, F52, Z72, R06, Z76, R53, R45, F50, R10]|
|                             vomiting|PROBLEM|       R11|[vomiting [vomiting], periodic vomiting [cyclical vomiting, in migraine,...|                                                  [R11, G43, P92]|
|        a respiratory tract infection|PROBLEM|       J98|[respiratory tract infection [other specified respiratory disorders], up...|     [J98, J06, A49, J22, J20, Z59, T17, J04, Z13, J18, P28, J39]|
+-------------------------------------+-------+----------+---------------------------------------------------------------------------+-----------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd10cm_generalised_augmented|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|1.4 GB|
|Case sensitive:|false|
