---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes - General Concepts (BioLORD)
author: John Snow Labs
name: biolordresolve_umls_general_concepts
date: 2026-06-11
tags: [en, entity_resolution, licensed, clinical, umls, general_concepts, biolord]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities to 4 general categories of UMLS CUI codes using `mpnet_embeddings_biolord_2023_c` (BioLORD) MPNet Embeddings. It is trained on the 2026AA release of the Unified Medical Language System (UMLS) dataset. The training data covers "Disease or Syndrome" (T047), "Sign or Symptom" (T184), "Medical Device" (T074), and "Therapeutic or Preventive Procedure" (T061) semantic types, comprising approximately 1,170,000 name-CUI pairs. The BioLORD embedding model is Open Source and does not require the `clinical/models` namespace.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_umls_general_concepts_en_6.4.0_3.4_1781219007697.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_umls_general_concepts_en_6.4.0_3.4_1781219007697.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_jsl")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner_jsl"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Injury_or_Poisoning","Hyperlipidemia","Kidney_Disease","Oncological","Cerebrovascular_Disease","Oxygen_Therapy","Heart_Disease","Obesity","Disease_Syndrome_Disorder","Symptom","Treatment","Diabetes","Procedure","Drug_Ingredient","VS_Finding","Communicable_Disease","Drug_BrandName","Hypertension","Imaging_Technique"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

mpnet_embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("mpnet_embeddings")

resolver = SentenceEntityResolverModel.pretrained("biolordresolve_umls_general_concepts","en","clinical/models")\
    .setInputCols(["mpnet_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, mpnet_embedder, resolver
])

data = spark.createDataFrame([["A 28-year-old female with a history of gestational diabetes mellitus diagnosed with a HTG-induced pancreatitis associated with acute hepatitis and obesity. She complains of a 2-week history of polyuria and vomiting."]]).toDF("text")
result = pipeline.fit(data).transform(data)

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

ner_model = medical.NerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_jsl")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner_jsl"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Injury_or_Poisoning","Hyperlipidemia","Kidney_Disease","Oncological","Cerebrovascular_Disease","Oxygen_Therapy","Heart_Disease","Obesity","Disease_Syndrome_Disorder","Symptom","Treatment","Diabetes","Procedure","Drug_Ingredient","VS_Finding","Communicable_Disease","Drug_BrandName","Hypertension","Imaging_Technique"])

chunk2doc = medical.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

mpnet_embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("mpnet_embeddings")

resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_umls_general_concepts","en","clinical/models")\
    .setInputCols(["mpnet_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, mpnet_embedder, resolver
])

data = spark.createDataFrame([["A 28-year-old female with a history of gestational diabetes mellitus diagnosed with a HTG-induced pancreatitis associated with acute hepatitis and obesity. She complains of a 2-week history of polyuria and vomiting."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
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

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_jsl"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Injury_or_Poisoning", "Hyperlipidemia", "Kidney_Disease", "Oncological", "Cerebrovascular_Disease", "Oxygen_Therapy", "Heart_Disease", "Obesity", "Disease_Syndrome_Disorder", "Symptom", "Treatment", "Diabetes", "Procedure", "Drug_Ingredient", "VS_Finding", "Communicable_Disease", "Drug_BrandName", "Hypertension", "Imaging_Technique"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val mpnet_embedder = MPNetEmbeddings
    .pretrained("mpnet_embeddings_biolord_2023_c", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("mpnet_embeddings")

val resolver = SentenceEntityResolverModel
    .pretrained("biolordresolve_umls_general_concepts", "en", "clinical/models")
    .setInputCols(Array("mpnet_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, mpnet_embedder, resolver
))

val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed with a HTG-induced pancreatitis associated with acute hepatitis and obesity. She complains of a 2-week history of polyuria and vomiting.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                     | entity                    | umls_code   | resolution                        | all_k_results                                                                       | all_k_distances                                                                     | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:------------------------------|:--------------------------|:------------|:----------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| gestational diabetes mellitus | Diabetes                  | C0085207    | gestational diabetes mellitus nos | C0085207:::C0032969:::C0743106:::C0342306:::C3839604:::C1391475                     | 0.1877:::0.3434:::0.3639:::0.4381:::0.4432:::0.4457                                 | 0.0176:::0.0590:::0.0662:::0.0960:::0.0982:::0.0993                                 | gestational diabetes mellitus nos:::diabetes mellitus pregnancy:::diabetes melli... |
| HTG-induced pancreatitis      | Disease_Syndrome_Disorder | C4302243    | igg4-related pancreatitis         | C4302243:::C5208246:::C5686570:::C0940932:::C2609129:::C0341473:::C0342270:::C60... | 0.7032:::0.7369:::0.7521:::0.7746:::0.7893:::0.7937:::0.7954:::0.7955:::0.7955::... | 0.2472:::0.2715:::0.2829:::0.3000:::0.3115:::0.3150:::0.3163:::0.3164:::0.3164::... | igg4-related pancreatitis:::immune-mediated pancreatitis:::type 1 autoimmune pan... |
| hepatitis                     | Disease_Syndrome_Disorder | C0019158    | hepatitis                         | C0019158:::C0019159:::C0040860:::C0854496:::C0744855:::C0814152:::C0042721:::C00... | 0.0005:::0.3890:::0.4038:::0.4044:::0.4408:::0.4963:::0.5119:::0.5345:::0.5395::... | 0.0000:::0.0757:::0.0815:::0.0818:::0.0972:::0.1232:::0.1310:::0.1428:::0.1456::... | hepatitis:::a hepatitis:::portal hepatitis:::hepatitis h:::hepatitis immune:::he... |
| obesity                       | Obesity                   | C0028754    | obesity                           | C0028754:::C0348480:::C1561826:::C2937224:::C0342940:::C0149974:::C0451819:::C00... | 0.1020:::0.3973:::0.4182:::0.4429:::0.4480:::0.4532:::0.4596:::0.4617:::0.4727::... | 0.0052:::0.0789:::0.0875:::0.0981:::0.1004:::0.1027:::0.1056:::0.1066:::0.1117::... | obesity:::other obesity:::overweight and obesity:::obesity; constitutional:::upp... |
| polyuria                      | Symptom                   | C0032617    | polyuria                          | C0032617:::C2830339:::C0016708:::C0017980:::C0848232:::C0268189:::C0232881:::C07... | 0.1124:::0.4495:::0.7102:::0.7548:::0.7877:::0.8094:::0.8123:::0.8203:::0.8228::... | 0.0063:::0.1010:::0.2522:::0.2849:::0.3102:::0.3276:::0.3299:::0.3364:::0.3385::... | polyuria:::other polyuria:::micturition frequency and polyuria:::glycosuria rena... |
| vomiting                      | Symptom                   | C0042963    | vomiting                          | C0042963:::C0027498:::C0948239:::C2202714:::C0474496:::C0221151:::C0027497:::C08... | 0.0942:::0.3803:::0.5440:::0.5493:::0.5545:::0.5608:::0.5631:::0.5656:::0.5888::... | 0.0044:::0.0723:::0.1479:::0.1508:::0.1537:::0.1573:::0.1585:::0.1600:::0.1733::... | vomiting:::nausea vomiting:::vomiting medication:::vomiting stool:::vomit diarrh... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_umls_general_concepts|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[mpnet_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|3.4 GB|
|Case sensitive:|false|
