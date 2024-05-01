---
layout: model
title: Sentence Entity Resolver for UMLS Codes - General Concepts
author: John Snow Labs
name: sbiobertresolve_umls_general_concepts
date: 2024-05-01
tags: [en, licensed, umls, resolver]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts to 4 categories (Medication, Symptom, Disease, Procedure) of UMLS CUI codes using ´sbiobert_base_cased_mli´ Sentence Bert Embeddings.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_general_concepts_en_5.3.1_3.4_1714578206593.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_general_concepts_en_5.3.1_3.4_1714578206593.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
                  ])\
    .setReplaceLabels({"Drug_Ingredient" : "DRUG", "Drug_BrandName" : "DRUG"})

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings\
    .pretrained("sbiobert_base_cased_mli",'en','clinical/models')\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_general_concepts, en, clinical/models") \
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
      .setWhiteList(['Injury_or_Poisoning','Hyperlipidemia','Kidney_Disease','Oncological','Cerebrovascular_Disease'
                  ,'Oxygen_Therapy','Heart_Disease','Obesity','Disease_Syndrome_Disorder','Symptom','Treatment','Diabetes','Injury_or_Poisoning'
                  ,'Procedure','Symptom','Treatment','Drug_Ingredient','VS_Finding','Communicable_Disease'
                  ,'Drug_BrandName','Hypertension','Imaging_Technique' 
                  ])\
      .setReplaceLabels({"Drug_Ingredient" : "DRUG", "Drug_BrandName" : "DRUG"})

val chunk2doc = Chunk2Doc()
      .setInputCols("ner_chunk")
      .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
      .pretrained("sbiobert_base_cased_mli", "en","clinical/models")
      .setInputCols(Array("ner_chunk_doc"))
      .setOutputCol("sbert_embeddings")
    
val resolver = SentenceEntityResolverModel
      .pretrained("sbiobertresolve_umls_findings", "en", "clinical/models")
      .setInputCols(Array("ner_chunk_doc", "sbert_embeddings"))
      .setOutputCol("resolution")
      .setDistanceFunction("EUCLIDEAN")

val p_model = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, ner_model, ner_model_converter, chunk2doc, sbert_embedder, resolver))
    
val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of pancreatitis three years prior to presentation, using Sulfonylurea for eight years, and obesity with a BMI of 33.5 kg/m2, presented with a one-week history of frequent urination and polydipsia. Additionally, tube placement on chest was performed following a pneumothorax that occurred 10 years ago.").toDF("text")  

val res = p_model.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------------+-----+---+-------------------------+---------+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|ner_chunk                    |begin|end|entity                   |umls_code|resolved_text                |all_k_results                                                                                                                                                                           |all_k_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+-----------------------------+-----+---+-------------------------+---------+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|gestational diabetes mellitus|39   |67 |Diabetes                 |C0085207 |gestational diabetes mellitus|C0085207:::C0032969:::C2063017:::C1283034:::C0271663:::C3646651:::C0271662:::C3839604:::C3649763:::C3662020:::C3828492:::C0341893:::C2011197                                            |gestational diabetes mellitus:::pregnancy diabetes mellitus:::pregnancy complicated by diabetes mellitus:::maternal diabetes mellitus:::gestational diabetes mellitus, a2:::pregnancy complicated by chronic diabetes mellitus:::gestational diabetes mellitus, a1:::postpartum gestational diabetes mellitus:::chronic diabetes mellitus in pregnancy:::pre-existing diabetes mellitus in pregnancy:::pregestational diabetes:::pregnancy + diabetes mellitus:::gestational diabetes mellitus with baby delivered|
|type two diabetes mellitus   |128  |153|Diabetes                 |C0011860 |type 2 diabetes mellitus     |C0011860:::C1719939:::C1832387:::C0348921:::C0271640:::C0348919:::C0877302:::C0011849:::C1852092:::C1719988:::C0349363:::C0837056                                                       |type 2 diabetes mellitus:::disorder associated with type 2 diabetes mellitus:::type 2 diabetes mellitus 2:::pre-existing type 2 diabetes mellitus:::secondary diabetes mellitus:::disorder of eye with type 2 diabetes mellitus:::insulin-requiring type 2 diabetes mellitus:::diabetes mellitus:::insulin-dependent diabetes mellitus 2:::neurological disorder with type 2 diabetes mellitus:::multiple complications of type 2 diabetes mellitus:::type 2 diabetes mellitus with features of insulin resistance|
|T2DM                         |156  |159|Diabetes                 |C0011860 |type 2 diabetes              |C0011860:::C0948893:::C1832387:::C1719939:::C0348921:::C0011849:::C0837056:::C0854110:::C0342257:::C0271640:::C4290092                                                                  |type 2 diabetes:::z type diabetes:::type 2 diabetes mellitus 2:::disorder associated with type 2 diabetes mellitus:::pre-existing type 2 diabetes mellitus:::diabetes mellitus:::type 2 diabetes mellitus with features of insulin resistance:::insulin resistant diabetes (mellitus):::compl diabetes mellitus:::secondary diabetes mellitus:::idiopathic diabetes (mellitus)                                                                                                                                    |
|HTG-induced pancreatitis     |184  |207|Disease_Syndrome_Disorder|C0376670 |alcohol-induced pancreatitis |C0376670:::C1868971:::C0267940:::C2350449:::C0341460:::C5208246:::C0001339:::C0341470:::C4302243:::C0030305:::C0341468:::C0341473:::C0948393:::C0267941:::C2215076:::C0349628:::C0341464|alcohol-induced pancreatitis:::toxic pancreatitis:::hemorrhage pancreatitis:::graft pancreatitis:::alcohol-induced acute pancreatitis:::immune-mediated pancreatitis:::pancreatitis acute:::alcohol-induced chronic pancreatitis:::igg4 related pancreatitis:::pancreatitis:::traumatic acute pancreatitis (disorder):::drug-induced chronic pancreatitis:::edematous pancreatitis:::necrotizing pancreatitis:::acute apoplectic pancreatitis:::post-ercp acute pancreatitis:::viral acute pancreatitis (disorder)|
|hepatitis                    |269  |277|Disease_Syndrome_Disorder|C0019158 |hepatitis                    |C0019158:::C0019159:::C0814152:::C0042721:::C0011226:::C0854495:::C0854496:::C0019163:::C0744855:::C0400906:::C0085293:::C0276434:::C0858814:::C0040860                                 |hepatitis:::hepatitis a:::hepatitis g:::viral hepatitis:::hepatitis d:::hepatitis f:::hepatitis h:::serum hepatitis:::immune hepatitis:::hepatitis - viral:::viral hepatitis e:::viral (infectious) hepatitis a:::hepatitis symptoms:::portal hepatitis                                                                                                                                                                                                                                                           |
|obesity                      |284  |290|Obesity                  |C0028754 |obesity                      |C0028754:::C0342940:::C0342942:::C0857116:::C1561826:::C0694533:::C4237343:::C0028756:::C2936179:::C1398735:::C2062945:::C0267992:::C4759305:::C5681294:::C2937224:::C1408387           |obesity:::abdominal obesity:::generalized obesity:::obesity gross:::overweight and obesity:::moderate obesity:::overweight or obesity:::morbid obesity:::visceral obesity:::glandular; obesity:::secondary obesity:::endogenous; obesity:::gynoid obesity:::genetic obesity:::constitutional obesity:::excess; calories with obesity                                                                                                                                                                              |
|polyuria                     |355  |362|Symptom                  |C0032617 |polyuria                     |C0032617:::C0848232:::C0016708:::C2830339:::C0018965:::C0151582:::C3888890:::C2936921                                                                                                   |polyuria:::nocturnal polyuria:::frequency of urination and polyuria:::other polyuria:::hematuria:::uricosuria:::polyuria-polydipsia syndrome:::saccharopinuria                                                                                                                                                                                                                                                                                                                                                    |
|polydipsia                   |365  |374|Symptom                  |C0085602 |polydipsia                   |C0085602:::C0857397:::C1994993:::C1540939:::C0030508:::C0343211:::C3888890:::C0393777:::C0206085:::C0917799:::C0751757                                                                  |polydipsia:::polydipsia (nocturnal):::(excessive thirst) or (polydipsia):::(excessive fluid intake) or (polydipsia):::parasomnia:::polyalgia:::polyuria-polydipsia syndrome:::hypnogenic paroxysmal dystonias:::periodic hypersomnias:::hypersomnias:::idiopathic hypersomnias                                                                                                                                                                                                                                    |
|poor appetite                |377  |389|Symptom                  |C0232462 |poor appetite                |C0232462:::C0003123:::C0011168:::C0162429:::C0426579:::C0578994:::C0241333:::C2364111:::C0231218:::C0018520:::C2198804:::C3714552:::C0235309                                            |poor appetite:::lack of appetite:::poor swallowing:::poor nutrition:::loss of appetite:::bad mouth taste:::taste unpleasantness:::loss of sense taste:::feeling poorly (malaise):::bad breath:::dissatisfied with body weight:::general weakness:::stomach discomfort                                                                                                                                                                                                                                             |
|vomiting                     |396  |403|Symptom                  |C0042963 |vomiting                     |C0042963:::C0401157:::C0152165:::C0152164:::C0859028:::C0374544:::C0750325:::C0850437:::C0520905:::C0027498                                                                             |vomiting:::intermittent vomiting:::persistent vomiting:::periodic vomiting:::vomiting reflex:::induction of vomiting:::vomit recurrent:::feel like vomiting:::postop vomiting:::nausea vomiting                                                                                                                                                                                                                                                                                                                   |
+-----------------------------+-----+---+-------------------------+---------+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_general_concepts|
|Compatibility:|Healthcare NLP 5.3.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|3.8 GB|
|Case sensitive:|false|