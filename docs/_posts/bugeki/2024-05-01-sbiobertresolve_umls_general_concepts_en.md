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
|gestational diabetes mellitus|39   |67 |Diabetes                 |C0085207 |gestational diabetes mellitus|C0085207:::C0032969:::C2063017:::C1283034                                           |gestational diabetes mellitus:::pregnancy diabetes mellitus:::pregnancy complicated by diabetes mellitus|
|type two diabetes mellitus   |128  |153|Diabetes                 |C0011860 |type 2 diabetes mellitus     |C0011860:::C1719939:::C1832387:::C0348921                                                       |type 2 diabetes mellitus:::disorder associated with type 2 diabetes mellitus:::type 2 diabetes mellitus 2|
|T2DM                         |156  |159|Diabetes                 |C0011860 |type 2 diabetes              |C0011860:::C0948893:::C1832387:::C1719939                                                                  |type 2 diabetes:::z type diabetes:::type 2 diabetes mellitus 2                                                                                                                                    |
|HTG-induced pancreatitis     |184  |207|Disease_Syndrome_Disorder|C0376670 |alcohol-induced pancreatitis |C0376670:::C1868971:::C0267940:::C2350449|alcohol-induced pancreatitis:::toxic pancreatitis:::hemorrhage pancreatitis|
|hepatitis                    |269  |277|Disease_Syndrome_Disorder|C0019158 |hepatitis                    |C0019158:::C0019159:::C0814152:::C0042721                                 |hepatitis:::hepatitis a:::hepatitis g                                                                                                                                                                                                                                                           |
|obesity                      |284  |290|Obesity                  |C0028754 |obesity                      |C0028754:::C0342940:::C0342942:::C0857116           |obesity:::abdominal obesity:::generalized obesity                                                                                                                                                                              |
|polyuria                     |355  |362|Symptom                  |C0032617 |polyuria                     |C0032617:::C0848232:::C0016708:::C28303391                                                                                                   |polyuria:::nocturnal polyuria:::frequency of urination and polyuria                                                                                                                                                                                                                                                                                                                                                    |
|polydipsia                   |365  |374|Symptom                  |C0085602 |polydipsia                   |C0085602:::C0857397:::C1994993:::C1540939                                                                  |polydipsia:::polydipsia (nocturnal):::(excessive thirst) or (polydipsia)                                                                                                                                                                                                                                    |
|poor appetite                |377  |389|Symptom                  |C0232462 |poor appetite                |C0232462:::C0003123:::C0011168:::C0162429                                            |poor appetite:::lack of appetite:::poor swallowing                                                                                                                                                                                                                                             |
|vomiting                     |396  |403|Symptom                  |C0042963 |vomiting                     |C0042963:::C0401157:::C0152165:::C0152164                                                                             |vomiting:::intermittent vomiting:::persistent vomiting                                                                                                                                                                                                                                                                                                                   |
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
