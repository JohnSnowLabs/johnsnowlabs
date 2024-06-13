---
layout: model
title: Sentence Entity Resolver for UMLS Codes - General Concepts
author: John Snow Labs
name: sbiobertresolve_umls_general_concepts
date: 2024-06-12
tags: [en, licensed, entity_resolution, umls]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts to the following 4 UMLS CUI code categories using `sbiobert_base_cased_mli` Sentence Bert Embeddings:

Disease: Unique Identifier: T047 Tree Number: B2.2.1.2.1

Symptom: Unique Identifier: T184 Tree Number: A2.2.2

Medication: Unique Identifier: T074 Tree Number: A1.3.1

Procedure: Unique Identifier: T061 Tree Number: B1.3.1.3

## Predicted Entities

`UMLS CUI codes for general concepts`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_general_concepts_en_5.3.3_3.0_1718235332729.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_general_concepts_en_5.3.3_3.0_1718235332729.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
                  ,'Drug_BrandName','Hypertension','Imaging_Technique'
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

val sentence_detector = SentenceDetectorDLModel
      .pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
      .setInputCols(Array("document"))\
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
                    "Oxygen_Therapy", "Heart_Disease","Obesity","Disease_Syndrome_Disorder","Symptom","Treatment","Diabetes","Injury_or_Poisoning",
                    "Procedure","Symptom","Treatment","Drug_Ingredient","VS_Finding","Communicable_Disease",
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
|    | ner_chunk                     | entity                    | umls_code   | resolution                    | all_k_results                                          | all_k_distances                              | all_k_cosine_distances                       | all_k_resolutions                                                                            |
|---:|:------------------------------|:--------------------------|:------------|:------------------------------|:-------------------------------------------------------|:---------------------------------------------|:---------------------------------------------|:---------------------------------------------------------------------------------------------|
|  0 | gestational diabetes mellitus | Diabetes                  | C0085207    | gestational diabetes mellitus | C0085207:::C0032969:::C2063017:::C1283034:::C0271663...| 0.0000:::4.1541:::4.7731:::4.8692:::4.8845...| 0.0000:::0.0253:::0.0332:::0.0347:::0.0354...| gestational diabetes mellitus:::pregnancy diabetes mellitus:::pregnancy complicated by dia...|
|  1 | type two diabetes mellitus    | Diabetes                  | C0011860    | type 2 diabetes mellitus      | C0011860:::C1719939:::C1832387:::C0348921:::C0271640...| 2.0974:::4.0218:::4.3644:::5.0391:::5.1188...| 0.0065:::0.0241:::0.0284:::0.0374:::0.0388...| type 2 diabetes mellitus:::disorder associated with type 2 diabetes mellitus:::type 2 diab...|
|  2 | T2DM                          | Diabetes                  | C0011860    | type 2 diabetes               | C0011860:::C0948893:::C1832387:::C1719939:::C0348921...| 6.5569:::7.8811:::8.0288:::8.1008:::8.3863...| 0.0666:::0.0973:::0.0988:::0.1004:::0.1061...| type 2 diabetes:::z type diabetes:::type 2 diabetes mellitus 2:::disorder associated with ...|
|  3 | HTG-induced pancreatitis      | Disease_Syndrome_Disorder | C0376670    | alcohol-induced pancreatitis  | C0376670:::C1868971:::C0267940:::C2350449:::C5208246...| 5.6616:::6.1229:::6.1748:::6.1966:::6.5241...| 0.0515:::0.0606:::0.0610:::0.0625:::0.0681...| alcohol-induced pancreatitis:::toxic pancreatitis:::hemorrhage pancreatitis:::graft pancre...|
|  4 | hepatitis                     | Disease_Syndrome_Disorder | C0019158    | hepatitis                     | C0019158:::C0019159:::C0814152:::C0042721:::C0011226...| 0.0000:::3.2380:::3.3070:::3.8885:::3.9127...| 0.0000:::0.0168:::0.0176:::0.0242:::0.0246...| hepatitis:::hepatitis a:::hepatitis g:::viral hepatitis:::hepatitis d:::hepatitis f:::hepa...|
|  5 | obesity                       | Obesity                   | C0028754    | obesity                       | C0028754:::C0342940:::C0342942:::C0857116:::C1561826...| 0.0000:::3.8693:::4.2493:::4.3092:::4.4595...| 0.0000:::0.0218:::0.0268:::0.0272:::0.0290...| obesity:::abdominal obesity:::generalized obesity:::obesity gross:::overweight and obesity...|
|  6 | polyuria                      | Symptom                   | C0032617    | polyuria                      | C0032617:::C0848232:::C0016708:::C2830339:::C0018965...| 0.0000:::6.9423:::7.8679:::8.1204:::8.4072...| 0.0000:::0.0751:::0.0970:::0.1063:::0.1103...| polyuria:::nocturnal polyuria:::frequency of urination and polyuria:::other polyuria:::hem...|
|  7 | polydipsia                    | Symptom                   | C0085602    | polydipsia                    | C0085602:::C0857397:::C1994993:::C1540939:::C0030508...| 0.0000:::6.0919:::8.4267:::8.7742:::9.9300...| 0.0000:::0.0572:::0.1111:::0.1217:::0.1520...| polydipsia:::polydipsia (nocturnal):::(excessive thirst) or (polydipsia):::(excessive flui...|
|  8 | poor appetite                 | Symptom                   | C0232462    | appetite poor                 | C0232462:::C0003123:::C0011168:::C0162429:::C0426579...| 3.3118:::5.7668:::6.4633:::6.6977:::6.8478...| 0.0159:::0.0482:::0.0611:::0.0652:::0.0685...| appetite poor:::lack of appetite:::poor swallowing:::poor nutrition:::loss of appetite:::b...|
|  9 | vomiting                      | Symptom                   | C0042963    | vomiting                      | C0042963:::C0401157:::C0152165:::C0152164:::C0859028...| 0.0000:::3.6352:::5.4750:::5.7050:::5.8952...| 0.0000:::0.0196:::0.0446:::0.0484:::0.0527...| vomiting:::intermittent vomiting:::persistent vomiting:::periodic vomiting:::vomiting refl...|
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_general_concepts|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|3.9 GB|
|Case sensitive:|false|

## References

Trained on disease, symptom, medication and procedure concepts of the ´2024AA´ release of the Unified Medical Language System® (UMLS). Knowledge Sources: https://www.nlm.nih.gov/research/umls/index.html
