---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes
author: John Snow Labs
name: sbiobertresolve_umls_major_concepts
date: 2024-06-12
tags: [entity_resolution, umls, licensed, clinical, en]
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

This model maps clinical entities and concepts to 4 major categories of UMLS CUI codes: `Clinical Findings`, `Medical Devices`, `Anatomical Structures`, `Injuries & Poisoning terms`, using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

## Predicted Entities

`UMLS CUI major concepts`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_major_concepts_en_5.3.3_3.0_1718199675652.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_major_concepts_en_5.3.3_3.0_1718199675652.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
      .setInputCol('text')\
      .setOutputCol('document')

sentence_detector =SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", 'clinical/models')\
      .setInputCols(["document"])\
      .setOutputCol("sentence")

tokenizer = Tokenizer()\
      .setInputCols("sentence")\
      .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
      .setInputCols(["sentence", "token"])\
      .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_model_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Cerebrovascular_Disease", "Communicable_Disease", "Diabetes", "Disease_Syndrome_Disorder", 
                   "Heart_Disease", "Hyperlipidemia", "Hypertension", "Injury_or_Poisoning", "Kidney_Disease", "Medical-Device", "Obesity", 
                   "Oncological", "Overweight", "Psychological_Condition", 
                   "Symptom", "VS_Finding", "ImagingFindings", "EKG_Findings", 
                   "Vaccine_Name"])

chunk2doc = Chunk2Doc().setInputCols("ner_chunk").setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings\
     .pretrained("sbiobert_base_cased_mli",'en','clinical/models')\
     .setInputCols(["ner_chunk_doc"])\
     .setOutputCol("sbert_embeddings")

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_major_concepts","en", "clinical/models") \
     .setInputCols(["sbert_embeddings"]) \
     .setOutputCol("resolution")\
     .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages = [document_assembler, sentence_detector, tokenizer, word_embeddings, ner_model, ner_model_converter, chunk2doc, sbert_embedder, resolver])

data = spark.createDataFrame([["""A female patient got influenza vaccine and one day after she has complains of ankle pain. She has only history of gestational diabetes mellitus diagnosed prior to presentation and subsequent type two diabetes mellitus (T2DM)"""]]).toDF("text")

results = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val sentence_detector = new SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", 'clinical/models')
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
      .setOutputCol("ner")

val ner_model_converter = new NerConverterInternal()
      .setInputCols(Array("sentence", "token", "ner"))
      .setOutputCol("ner_chunk")
      .setWhiteList(Array("Cerebrovascular_Disease", 
                   "Communicable_Disease", "Diabetes", "Disease_Syndrome_Disorder", 
                   "Heart_Disease", "Hyperlipidemia", "Hypertension", "Injury_or_Poisoning", "Kidney_Disease", "Medical-Device", "Obesity", 
                   "Oncological", "Overweight", "Psychological_Condition", 
                   "Symptom", "VS_Finding", "ImagingFindings", "EKG_Findings", 
                   "Vaccine_Name"))

val chunk2doc = Chunk2Doc().setInputCols("ner_chunk").setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
      .pretrained("sbiobert_base_cased_mli", "en","clinical/models")
      .setInputCols(Array("ner_chunk_doc"))
      .setOutputCol("sbert_embeddings")
    
val resolver = SentenceEntityResolverModel
      .pretrained("sbiobertresolve_umls_major_concepts", "en", "clinical/models")
      .setInputCols(Array("ner_chunk_doc", "sbert_embeddings"))
      .setOutputCol("resolution")
      .setDistanceFunction("EUCLIDEAN")

val p_model = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, ner_model, ner_model_converter, chunk2doc, sbert_embedder, resolver))
    
val data = Seq("A female patient got influenza vaccine and one day after she has complains of ankle pain. She has only history of gestational diabetes mellitus diagnosed prior to presentation and subsequent type two diabetes mellitus (T2DM).").toDF("text")  

val res = p_model.fit(data).transform(data)
```
</div>

## Results

```bash
|    | ner_chunk                     | entity       | umls_code   | resolution                                 | all_k_results                                       | all_k_distances                              | all_k_cosine_distances                       | all_k_resolutions                                                                |
|---:|:------------------------------|:-------------|:------------|:-------------------------------------------|:----------------------------------------------------|:---------------------------------------------|:---------------------------------------------|:---------------------------------------------------------------------------------|
|  0 | influenza vaccine             | Vaccine_Name | C0260381    | influenza vaccination                      | C0260381:::C1260452:::C4302763:::C4473357:::C3476...| 6.5367:::6.8250:::7.2029:::7.5281:::7.7098...| 0.0708:::0.0776:::0.0854:::0.0947:::0.0969...| influenza vaccination:::vaccin for influenza:::influenza vaccination given:::d...|
|  1 | ankle pain                    | Symptom      | C4047548    | bilateral ankle joint pain                 | C4047548:::C4315239:::C2032293:::C2089776:::C0576...| 4.8134:::6.7158:::6.9567:::7.1444:::7.1515...| 0.0337:::0.0665:::0.0703:::0.0751:::0.0741...| bilateral ankle joint pain:::joint and leg pain:::bilateral calf pain:::ankle ...|
|  2 | gestational diabetes mellitus | Diabetes     | C2183115    | diabetes mellitus during pregnancy         | C2183115:::C3161145:::C3532257:::C4303558:::C3840...| 5.2200:::6.3563:::6.9305:::7.1692:::7.2144...| 0.0401:::0.0596:::0.0717:::0.0750:::0.0773...| diabetes mellitus during pregnancy:::hx gestational diabetes:::gestational dia...|
|  3 | type two diabetes mellitus    | Diabetes     | C4016960    | type 2 diabetes mellitus, association with | C4016960:::C4014362:::C4016735:::C3532488:::C0260...| 4.3761:::5.4035:::5.5192:::6.1712:::6.2650...| 0.0285:::0.0438:::0.0460:::0.0568:::0.0583...| type 2 diabetes mellitus, association with:::type 2 diabetes mellitus (t2d):::...|
|  4 | T2DM                          | Diabetes     | C4014362    | type 2 diabetes mellitus (t2d)             | C4014362:::C1320657:::C4016960:::C4016735:::C0260...| 7.2798:::7.7099:::8.2517:::8.6288:::8.7378...| 0.0821:::0.0929:::0.1043:::0.1171:::0.1163...| type 2 diabetes mellitus (t2d):::type diabetes:::type 2 diabetes mellitus, ass...|
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_major_concepts|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|4.2 GB|
|Case sensitive:|false|

## References

Trained on concepts from clinical major concepts for the 2024AA release of the Unified Medical Language System® (UMLS) Knowledge Sources: https://www.nlm.nih.gov/research/umls/index.html
