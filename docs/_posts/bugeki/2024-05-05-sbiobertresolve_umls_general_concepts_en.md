---
layout: model
title: Sentence Entity Resolver for UMLS Codes - General Concepts
author: John Snow Labs
name: sbiobertresolve_umls_general_concepts
date: 2024-05-05
tags: [en, licensed, entity_resolution, umls]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.2
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts to the following 4 UMLS CUI code categories using ´sbiobert_base_cased_mli´ Sentence Bert Embeddings:

Disease: Unique Identifier: T047 Tree Number: B2.2.1.2.1

Symptom: Unique Identifier: T184 Tree Number: A2.2.2

Medication: Unique Identifier: T074 Tree Number: A1.3.1

Procedure: Unique Identifier: T061 Tree Number: B1.3.1.3

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_general_concepts_en_5.3.2_3.0_1714938183825.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_general_concepts_en_5.3.2_3.0_1714938183825.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setWhiteList(['Injury_or_Poisoning','Hyperlipidemia','Kidney_Disease','Oncological','Cerebrovascular_Disease'
                  ,'Oxygen_Therapy','Heart_Disease','Obesity','Disease_Syndrome_Disorder','Symptom','Treatment','Diabetes','Injury_or_Poisoning'
                  ,'Procedure','Symptom','Treatment','Drug_Ingredient','VS_Finding','Communicable_Disease'
                  ,'Drug_BrandName','Hypertension'
                  ])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings\
    .pretrained("sbiobert_base_cased_mli",'en','clinical/models')\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_general_concepts", "en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

umls_lp = Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_model_converter,
    chunk2doc,
    sbert_embedder,
    resolver
])

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with an acute hepatitis, and obesity with a BMI of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting."""]]).toDF("text")

result = umls_lp.fit(data).transform(data)
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
      .setWhiteList(["Injury_or_Poisoning","Hyperlipidemia","Kidney_Disease","Oncological","Cerebrovascular_Disease",
                    "Oxygen_Therapy", "Heart_Disease","Obesity","Disease_Syndrome_Disorder","Symptom","Treatment","Diabetes","Injury_or_Poisoning",
                    "Procedure","Symptom","Treatment","Drug_Ingredient","VS_Finding","Communicable_Disease",
                    "Drug_BrandName","Hypertension","Imaging_Technique" 
                  ])

val chunk2doc = new Chunk2Doc()
      .setInputCols("ner_chunk")
      .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
      .pretrained("sbiobert_base_cased_mli", "en","clinical/models")
      .setInputCols(Array("ner_chunk_doc"))
      .setOutputCol("sbert_embeddings")
      .setCaseSensitive(False)
    
val resolver = SentenceEntityResolverModel
      .pretrained("sbiobertresolve_umls_general_concepts", "en", "clinical/models")
      .setInputCols(Array("ner_chunk_doc", "sbert_embeddings"))
      .setOutputCol("resolution")
      .setDistanceFunction("EUCLIDEAN")

val p_model = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_model_converter,
    chunk2doc,
    sbert_embedder,
    resolver))
    
val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of pancreatitis three years prior to presentation, using Sulfonylurea for eight years, and obesity with a BMI of 33.5 kg/m2, presented with a one-week history of frequent urination and polydipsia. Additionally, tube placement on chest was performed following a pneumothorax that occurred 10 years ago.").toDF("text")  

val res = p_model.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------------+-----+---+-------------------------+---------+------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                    ner_chunk|begin|end|                   entity|umls_code|                 resolved_text|                                               all_k_results|                                           all_k_resolutions|
+-----------------------------+-----+---+-------------------------+---------+------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|gestational diabetes mellitus|   39| 67|                 Diabetes| C0085207| gestational diabetes mellitus|C0085207:::C0032969:::C2063017:::C1283034:::C0271663:::C3...|gestational diabetes mellitus:::pregnancy diabetes mellit...|
|   type two diabetes mellitus|  128|153|                 Diabetes| C0011860|      type 2 diabetes mellitus|C0011860:::C1719939:::C1832387:::C0348921:::C0271640:::C0...|type 2 diabetes mellitus:::disorder associated with type ...|
|                         T2DM|  156|159|                 Diabetes| C0011860|               type 2 diabetes|C0011860:::C0948893:::C1832387:::C1719939:::C0348921:::C0...|type 2 diabetes:::z type diabetes:::type 2 diabetes melli...|
|                 pancreatitis|  185|196|Disease_Syndrome_Disorder| C0030305|                  pancreatitis|C0030305:::C5208246:::C0747199:::C0267947:::C0747195:::C0...|pancreatitis:::immune-mediated pancreatitis:::pancreatiti...|
|                 Sulfonylurea|  239|250|          Drug_Ingredient| C2316111|administration of sulfonylurea|C2316111:::C4067411:::C5231442:::C0037023:::C1263725:::C0...|administration of sulfonylurea:::inj, isavuconazonium sul...|
|                      obesity|  275|281|                  Obesity| C0028754|                       obesity|C0028754:::C0342940:::C0342942:::C0857116:::C1561826:::C0...|obesity:::abdominal obesity:::generalized obesity:::obesi...|
|           frequent urination|  346|363|                  Symptom| C0085606|     frequent/urgent urination|C0085606:::C0848390:::C0856128:::C0848342:::C5682033:::C0...|frequent/urgent urination:::excessive urination:::urinary...|
|                   polydipsia|  369|378|                  Symptom| C0085602|                    polydipsia|C0085602:::C0857397:::C1994993:::C1540939:::C0030508:::C0...|polydipsia:::polydipsia (nocturnal):::(excessive thirst) ...|
|               tube placement|  396|409|                Procedure| C0883304|                tube placement|C0883304:::C5788004:::C0175730:::C1282807:::C0728466:::C0...|tube placement:::insertion of tube:::tube device:::tube h...|
|                 pneumothorax|  446|457|Disease_Syndrome_Disorder| C0032326|                  pneumothorax|C0032326:::C0264557:::C0019077:::C1405275:::C0264558:::C0...|pneumothorax:::persistent pneumothorax:::hemopneumothorax...|
+-----------------------------+-----+---+-------------------------+---------+------------------------------+------------------------------------------------------------+------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_general_concepts|
|Compatibility:|Healthcare NLP 5.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|3.8 GB|
|Case sensitive:|false|

## References

Trained on disease, symptom, medication and procedure concepts of the ´2023AB´ release of the Unified Medical Language System® (UMLS). Knowledge Sources: https://www.nlm.nih.gov/research/umls/index.html
