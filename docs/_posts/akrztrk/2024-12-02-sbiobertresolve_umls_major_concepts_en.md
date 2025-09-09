---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes
author: John Snow Labs
name: sbiobertresolve_umls_major_concepts
date: 2024-12-02
tags: [entity_resolution, umls, clinical, en, licensed]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.5.1
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
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/05.0.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_major_concepts_en_5.5.1_3.0_1733163024044.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_major_concepts_en_5.5.1_3.0_1733163024044.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
                   "Vaccine_Name", "RelativeDate"])

chunk2doc = Chunk2Doc()\
      .setInputCols("ner_chunk")\
      .setOutputCol("ner_chunk_doc")

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

{:.jsl-block}
```python
document_assembler = nlp.DocumentAssembler()\
      .setInputCol('text')\
      .setOutputCol('document')

sentence_detector =nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", 'clinical/models')\
      .setInputCols(["document"])\
      .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
      .setInputCols("sentence")\
      .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
      .setInputCols(["sentence", "token"])\
      .setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_model_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Cerebrovascular_Disease", "Communicable_Disease", "Diabetes", "Disease_Syndrome_Disorder",
                   "Heart_Disease", "Hyperlipidemia", "Hypertension", "Injury_or_Poisoning", "Kidney_Disease", "Medical-Device", "Obesity",
                   "Oncological", "Overweight", "Psychological_Condition",
                   "Symptom", "VS_Finding", "ImagingFindings", "EKG_Findings",
                   "Vaccine_Name", "RelativeDate"])

chunk2doc = medical.Chunk2Doc()\
      .setInputCols("ner_chunk")\
      .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings\
     .pretrained("sbiobert_base_cased_mli",'en','clinical/models')\
     .setInputCols(["ner_chunk_doc"])\
     .setOutputCol("sbert_embeddings")

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_major_concepts","en", "clinical/models") \
     .setInputCols(["sbert_embeddings"]) \
     .setOutputCol("resolution")\
     .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages = [document_assembler, sentence_detector, tokenizer, word_embeddings, ner_model, ner_model_converter, chunk2doc, sbert_embedder, resolver])

data = spark.createDataFrame([["""A female patient got influenza vaccine and one day after she has complains of ankle pain. She has only history of gestational diabetes mellitus diagnosed prior to presentation and subsequent type two diabetes mellitus (T2DM)"""]]).toDF("text")

results = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val sentence_detector = new SentenceDetectorDLModel
      .pretrained("sentence_detector_dl_healthcare", "en", 'clinical/models')
      .setInputCols(["document"])\
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
                   "Vaccine_Name", "RelativeDate"))

val chunk2doc = Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

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
+-----------------------------+------------+---------+------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|                    ner_chunk|      entity|umls_code|                                resolution|                                                               all_k_resolutions|                                                                   all_k_results|                                                                 all_k_distances|                                                          all_k_cosine_distances|
+-----------------------------+------------+---------+------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|            influenza vaccine|Vaccine_Name| C1260452|                      vaccin for influenza|vaccin for influenza:::influenza vaccinations:::influenza vaccination given::...|C1260452:::C0260381:::C4302763:::C4473357:::C3476067:::C0586139:::C1719141:::...|6.8250:::6.8309:::7.2029:::7.5281:::7.7098:::7.7339:::7.9169:::7.9927:::8.236...|0.0776:::0.0777:::0.0854:::0.0947:::0.0969:::0.0987:::0.1033:::0.1047:::0.112...|
|                one day after|RelativeDate| C0420328|                 follow-up 1 day (finding)|follow-up 1 day (finding):::initial day:::1/day:::1 = 1 day:::within 1 day or...|C0420328:::C4534547:::C5441960:::C5939023:::C3843067:::C3842292:::C3843680:::...|7.2691:::8.1345:::8.6351:::8.6644:::9.3661:::9.6892:::9.9726:::10.0212:::10.2...|0.0814:::0.1016:::0.1151:::0.1151:::0.1348:::0.1451:::0.1521:::0.1574:::0.157...|
|                   ankle pain|     Symptom| C4047548|                bilateral ankle joint pain|bilateral ankle joint pain:::joint and leg pain:::bilateral calf pain:::ankle...|C4047548:::C4315239:::C2032293:::C2089776:::C0576209:::C0587992:::C0311395:::...|4.8134:::6.7158:::6.9567:::7.1444:::7.1515:::7.1661:::7.2401:::7.2610:::7.368...|0.0337:::0.0665:::0.0703:::0.0751:::0.0741:::0.0755:::0.0766:::0.0764:::0.078...|
|gestational diabetes mellitus|    Diabetes| C3532257|uncontrolled gestational diabetes mellitus|uncontrolled gestational diabetes mellitus:::diabetes mellitus during pregnan...|C3532257:::C2183115:::C3161145:::C4303558:::C3840222:::C2114054:::C3874269:::...|4.9175:::5.2200:::6.3563:::7.1692:::7.2144:::7.2542:::7.2949:::7.4942:::7.620...|0.0358:::0.0401:::0.0596:::0.0750:::0.0773:::0.0778:::0.0776:::0.0820:::0.085...|
|   type two diabetes mellitus|    Diabetes| C4016960|type 2 diabetes mellitus, association with|type 2 diabetes mellitus, association with:::type 2 diabetes mellitus (t2d)::...|C4016960:::C4014362:::C4016735:::C3532488:::C0260526:::C2733146:::C1320657:::...|4.3761:::5.4035:::5.5192:::6.1712:::6.2650:::6.3819:::6.4434:::6.4926:::6.857...|0.0285:::0.0438:::0.0460:::0.0568:::0.0583:::0.0616:::0.0618:::0.0638:::0.069...|
|                         T2DM|    Diabetes| C3854130|                                       t2d|t2d:::t2:::t2b:::t2a:::ttpp2:::t2a2:::te2:::t2 segment:::v2d:::timi 2:::adhd2...|C3854130:::C0475373:::C0475388:::C0475387:::C2750473:::C3869849:::C3496459:::...|3.1500:::4.5297:::5.1459:::5.3037:::5.3750:::5.7386:::5.7419:::5.8413:::6.150...|0.0160:::0.0335:::0.0440:::0.0466:::0.0488:::0.0550:::0.0538:::0.0571:::0.061...|
+-----------------------------+------------+---------+------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_major_concepts|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|4.2 GB|
|Case sensitive:|false|

## References

Trained on concepts from clinical major concepts for the 2024AB release of the Unified Medical Language System® (UMLS) Knowledge Sources: https://www.nlm.nih.gov/research/umls/index.html
