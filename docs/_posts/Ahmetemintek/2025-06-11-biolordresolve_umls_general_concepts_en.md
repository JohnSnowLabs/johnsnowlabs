---
layout: model
title: Sentence Entity Resolver for UMLS Codes - General Concepts
author: John Snow Labs
name: biolordresolve_umls_general_concepts
date: 2025-06-11
tags: [licensed, en, biolord, umls, entity_resolution, clinical]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts to the following 4 UMLS CUI code categories using ´[mpnet_embeddings_biolord_2023_c](https://sparknlp.org/2024/04/04/mpnet_embeddings_biolord_2023_c_en.html)´ Sentence Embeddings:

Disease: Unique Identifier: T047 Tree Number: B2.2.1.2.1

Symptom: Unique Identifier: T184 Tree Number: A2.2.2

Medication: Unique Identifier: T074 Tree Number: A1.3.1

Procedure: Unique Identifier: T061 Tree Number: B1.3.1.3

**NOTE**: This model can be used with spark v3.4.0 and above versions.

## Predicted Entities

`UMLS CUI codes for general concepts`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_umls_general_concepts_en_6.0.2_3.4_1749647717107.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_umls_general_concepts_en_6.0.2_3.4_1749647717107.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner_jsl")

ner_model_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner_jsl"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Injury_or_Poisoning","Hyperlipidemia","Kidney_Disease","Oncological","Cerebrovascular_Disease",
                  "Oxygen_Therapy","Heart_Disease","Obesity","Disease_Syndrome_Disorder","Symptom","Treatment","Diabetes",
                  "Injury_or_Poisoning", "Procedure","Symptom","Treatment","Drug_Ingredient","VS_Finding","Communicable_Disease",
                  "Drug_BrandName","Hypertension"
                  ])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embeddings =MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("mpnet_embeddings")\
    .setCaseSensitive(False)

umls_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_umls_general_concepts", "en", "clinical/models") \
    .setInputCols(["mpnet_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")\
    .setCaseSensitive(False)

resolver_pipeline = Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_model_converter,
    chunk2doc,
    embeddings,
    umls_resolver
])

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of pancreatitis three years prior to presentation, associated with an acute hepatitis, and obesity with a BMI of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting."""]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner_jsl")

ner_model_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner_jsl"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Injury_or_Poisoning","Hyperlipidemia","Kidney_Disease","Oncological","Cerebrovascular_Disease",
                  "Oxygen_Therapy","Heart_Disease","Obesity","Disease_Syndrome_Disorder","Symptom","Treatment","Diabetes",
                  "Injury_or_Poisoning", "Procedure","Symptom","Treatment","Drug_Ingredient","VS_Finding","Communicable_Disease",
                  "Drug_BrandName","Hypertension"
                  ])

chunk2doc = medical.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embeddings =nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("mpnet_embeddings")\
    .setCaseSensitive(False)

umls_resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_umls_general_concepts", "en", "clinical/models") \
    .setInputCols(["mpnet_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")\
    .setCaseSensitive(False)

resolver_pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_model_converter,
    chunk2doc,
    embeddings,
    umls_resolver
])

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of pancreatitis three years prior to presentation, associated with an acute hepatitis, and obesity with a BMI of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting."""]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val sentence_detector = new SentenceDetector()
      .setInputCols(Array("document"))
      .setOutputCol("sentence")

val tokenizer = new Tokenizer()
      .setInputCols("sentence")
      .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel
      .pretrained("embeddings_clinical", "en", "clinical/models")
      .setInputCols(Array("sentence", "token"))
      .setOutputCol("embeddings")

val ner_model = MedicalNerModel
      .pretrained("ner_jsl", "en", "clinical/models")
      .setInputCols(Array("sentence", "token", "embeddings"))
      .setOutputCol("ner_jsl")

val ner_model_converter = new NerConverterInternal()
      .setInputCols(Array("sentence", "token", "ner_jsl"))
      .setOutputCol("ner_chunk")
      .setWhiteList(Array("Injury_or_Poisoning","Hyperlipidemia","Kidney_Disease","Oncological","Cerebrovascular_Disease",
                    "Oxygen_Therapy", "Heart_Disease","Obesity","Disease_Syndrome_Disorder","Symptom","Treatment","Diabetes",
                    "Injury_or_Poisoning", "Procedure","Symptom","Treatment","Drug_Ingredient","VS_Finding","Communicable_Disease",
                    "Drug_BrandName","Hypertension","Imaging_Technique"
                  ))

val chunk2doc = new Chunk2Doc()
      .setInputCols("ner_chunk")
      .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
      .pretrained("sbiobert_base_cased_mli", "en","clinical/models")
      .setInputCols(Array("ner_chunk_doc"))
      .setOutputCol("sbert_embeddings")
      .setCaseSensitive(False)

val resolver = SentenceEntityResolverModel
      .pretrained("sbiobertresolve_umls_findings", "en", "clinical/models")
      .setInputCols(Array("ner_chunk_doc", "sbert_embeddings"))
      .setOutputCol("resolution")
      .setDistanceFunction("EUCLIDEAN")

val embeddings =MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("mpnet_embeddings")
    .setCaseSensitive(False)

val umls_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_umls_general_concepts", "en", "clinical/models")
    .setInputCols(["mpnet_embeddings"])
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")
    .setCaseSensitive(False)

val resolver_pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_model_converter,
    chunk2doc,
    embeddings,
    umls_resolver))

val data = Seq("""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of pancreatitis three years prior to presentation, associated with an acute hepatitis, and obesity with a BMI of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting.""").toDF("text")

val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
+-----------------------------+-----+---+-------------------------+---------+-------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                    ner_chunk|begin|end|                   entity|umls_code|              description|                                               all_k_results|                                           all_k_resolutions|
+-----------------------------+-----+---+-------------------------+---------+-------------------------+------------------------------------------------------------+------------------------------------------------------------+
|gestational diabetes mellitus|   39| 67|                 Diabetes| C0085207|    Diabetes, Gestational|C0085207:::C0032969:::C0342306:::C0743106:::C0341893:::C0...|Diabetes, Gestational:::diabetes mellitus in pregnancy:::...|
|   type two diabetes mellitus|  128|153|                 Diabetes| C0011860|Diabetes Mellitus, Type 2|C0011860:::C1719939:::C1282951:::C1852092:::C2874123:::C0...|Diabetes Mellitus, Type 2:::Disorder due to type II diabe...|
|                         T2DM|  156|159|                 Diabetes| C0011860|                      T2D|C0011860:::C1832387:::C1843807:::C1835887:::C4015183:::C1...|T2D:::T2D2:::THMD2:::TNDM2:::T2D5:::T2D4:::T2D1:::TPMTD::...|
|                 pancreatitis|  184|195|Disease_Syndrome_Disorder| C0030305|             pancreatitis|C0030305:::C0267948:::C0856100:::C0267946:::C0149521:::C0...|pancreatitis:::metabolic pancreatitis:::Pancreatitis aggr...|
|                    hepatitis|  257|265|Disease_Syndrome_Disorder| C0019158|                hepatitis|C0019158:::C0040860:::C0019159:::C0854496:::C0564695:::C0...|hepatitis:::Portal hepatitis:::a hepatitis:::hepatitis h:...|
|                      obesity|  272|278|                  Obesity| C0028754|                  obesity|C0028754:::C1719565:::C0451819:::C1561826:::C0342940:::C2...|obesity:::Obesity-unspecified:::Simple obesity NOS:::Over...|
|                     polyuria|  343|350|                  Symptom| C0032617|             Polyuria NOS|C0032617:::C2830339:::C0016708:::C3888890:::C0848232:::C0...|Polyuria NOS:::Other polyuria:::Micturition frequency and...|
|                   polydipsia|  353|362|                  Symptom| C0085602|           Polydipsia NOS|C0085602:::C0268813:::C3888890:::C0857397:::C1994993:::C5...|Polydipsia NOS:::Primary polydipsia:::Polyuria-polydipsia...|
|                poor appetite|  365|377|                  Symptom| C0232462|     Decrease in appetite|        C0232462:::C0003123:::C0426583:::C0426579:::C1971623|Decrease in appetite:::lack of appetite:::Appetite loss -...|
|                     vomiting|  384|391|                  Symptom| C0042963|        vomiting symptoms|        C0042963:::C0221151:::C0027498:::C0232602:::C0474496|vomiting symptoms:::VOMITING, PROJECTILE:::vomiting and n...|
+-----------------------------+-----+---+-------------------------+---------+-------------------------+------------------------------------------------------------+------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_umls_general_concepts|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[mpnet_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|4.0 GB|
|Case sensitive:|false|

## References

Trained on concepts from clinical general concepts for the 2025AA release of the Unified Medical Language System® (UMLS) Knowledge Sources: https://www.nlm.nih.gov/research/umls/index.html