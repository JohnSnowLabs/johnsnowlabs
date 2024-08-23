---
layout: model
title: Sentence Entity Resolver for RxNorm (sbiobert_base_cased_mli embeddings)
author: John Snow Labs
name: sbiobertresolve_rxnorm_augmented_v2
date: 2024-08-14
tags: [rxnorm, licensed, en, clinical, entity_resolution]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. Additionally, this model returns concept classes of the drugs in `all_k_aux_labels` column in the metadata.

## Predicted Entities

`RxNorm Codes`, `Concept Classes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_rxnorm_augmented_v2_en_5.4.0_3.0_1723638077203.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_rxnorm_augmented_v2_en_5.4.0_3.0_1723638077203.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

ner = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")\

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

rxnorm_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented_v2", "en", "clinical/models")\
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("rxnorm_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages = [document_assembler,
                                       sentenceDetectorDL,
                                       tokenizer,
                                       word_embeddings,
                                       ner,
                                       ner_converter,
                                       c2doc,
                                       sbert_embedder,
                                       rxnorm_resolver])

text= "The patient was prescribed aspirin and and Albuterol inhaler, two puffs every 4 hours as needed for asthma. He was seen by the endocrinology service and she was discharged on Coumadin 5 mg with meals , and metformin 1000 mg two times a day and Lisinopril 10 mg daily"

data = spark.createDataFrame([[text]]).toDF("text")
result = resolver_pipeline.fit(data).transform(data)

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

val ner = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("DRUG"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols("ner_chunk_doc")
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

val rxnorm_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented_v2", "en", "clinical/models")
    .setInputCols("sbert_embeddings")
    .setOutputCol("rxnorm_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
                               document_assembler,
                               sentence_detector,
                               tokenizer,
                               word_embeddings,
                               ner,
                               ner_converter,
                               chunk2doc,
                               sbert_embedder,
                               rxnorm_resolver))

val data = Seq("The patient was prescribed aspirin and and Albuterol inhaler, two puffs every 4 hours as needed for asthma. He was seen by the endocrinology service and she was discharged on Coumadin 5 mg with meals , and metformin 1000 mg two times a day and Lisinopril 10 mg daily").toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------+------+----------+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|        ner_chunk|entity|RxNormCode|                                                   resolutions|                                                                                                                                     all_k_resolutions|                                                                                                                                         all_k_results|                                                                                                                                       all_k_distances|                                                                                                                                all_k_cosine_distances|                                                                                                                                      all_k_aux_labels|
+-----------------+------+----------+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|          aspirin|  DRUG|      1191|                                              aspirin[aspirin]|aspirin[aspirin]:::aspirin Oral Powder Product:::YSP Aspirin[YSP Aspirin]:::Med Aspirin[Med Aspirin]:::aspirin Pill[aspirin Pill]:::Bayer Aspirin[B...|1191:::1295740:::405403:::218266:::1154070:::215568:::202547:::1154069:::1154068:::2393783:::1008988:::375972:::724441:::392499:::1007240:::1294937...|0.0000:::4.1826:::5.7007:::6.0877:::6.5428:::7.0099:::7.0654:::7.1438:::7.1438:::7.7893:::8.1658:::8.3308:::8.3676:::8.3848:::8.4302:::8.5257:::8.5...|0.0000:::0.0292:::0.0550:::0.0624:::0.0722:::0.0834:::0.0837:::0.0853:::0.0853:::0.1031:::0.1145:::0.1173:::0.1182:::0.1191:::0.1197:::0.1215:::0.1...|Ingredient:::Clinical Dose Group:::Brand Name:::Brand Name:::Clinical Dose Group:::Brand Name:::Brand Name:::Clinical Dose Group:::Clinical Dose Gr...|
|Albuterol inhaler|  DRUG|    745678|albuterol Metered Dose Inhaler[albuterol Metered Dose Inhaler]|albuterol Metered Dose Inhaler[albuterol Metered Dose Inhaler]:::albuterol Inhalation Solution[albuterol Inhalation Solution]:::albuterol Inhalant ...|745678:::2108226:::1154602:::2108233:::2108228:::435:::746762:::2108250:::2108246:::1154603:::745790:::2108248:::370790:::2108257:::801916:::164996...|4.9847:::5.1028:::5.4746:::5.7809:::6.2859:::6.3948:::6.4499:::6.4818:::6.7662:::7.0795:::7.0946:::7.1218:::7.1481:::7.1788:::7.3386:::7.3764:::7.3...|0.0414:::0.0439:::0.0505:::0.0562:::0.0676:::0.0683:::0.0706:::0.0721:::0.0777:::0.0842:::0.0856:::0.0859:::0.0855:::0.0879:::0.0917:::0.0923:::0.0...|Clinical Drug Form:::Clinical Drug Form:::Clinical Dose Group:::Clinical Drug Form:::Branded Drug Form:::Ingredient:::Branded Drug Form:::Branded D...|
|    Coumadin 5 mg|  DRUG|    855333|                               warfarin sodium 5 MG [Coumadin]|warfarin sodium 5 MG [Coumadin]:::coumarin 5 MG[coumarin 5 MG]:::oxybutynin chloride 5 MG Oral Tablet [Urimin]:::nitisinone 5 MG Oral Capsule [Orfa...|855333:::438740:::153692:::352120:::1036890:::104363:::201269:::351399:::668467:::668694:::200795:::153618:::108781:::2475857:::905173:::450946:::1...|0.0000:::4.0885:::5.3065:::5.5132:::5.5336:::5.7412:::5.8485:::6.0303:::6.0509:::6.0850:::6.1168:::6.1305:::6.1361:::6.1406:::6.1748:::6.1943:::6.2...|0.0000:::0.0287:::0.0479:::0.0518:::0.0525:::0.0578:::0.0585:::0.0622:::0.0643:::0.0636:::0.0634:::0.0647:::0.0630:::0.0647:::0.0662:::0.0666:::0.0...|Branded Drug Comp:::Clinical Drug Comp:::Branded Drug:::Branded Drug:::Branded Drug Comp:::Branded Drug:::Branded Drug:::Branded Drug:::Branded Dru...|
|metformin 1000 mg|  DRUG|    316255|                          metformin 1000 MG[metformin 1000 MG]|metformin 1000 MG[metformin 1000 MG]:::metformin hydrochloride 1000 MG[metformin hydrochloride 1000 MG]:::metformin hydrochloride 1000 MG [Fortamet...|316255:::860995:::860997:::861014:::861004:::861005:::1428922:::334887:::331454:::1659290:::336889:::1656316:::316337:::333653:::1538099:::446597::...|0.0000:::5.2988:::5.9071:::6.3066:::6.5777:::6.6626:::6.8523:::6.9814:::7.1142:::7.1192:::7.1218:::7.1317:::7.1372:::7.1397:::7.1481:::7.1978:::7.2...|0.0000:::0.0445:::0.0553:::0.0632:::0.0679:::0.0707:::0.0739:::0.0769:::0.0812:::0.0801:::0.0792:::0.0806:::0.0810:::0.0816:::0.0810:::0.0827:::0.0...|Clinical Drug Comp:::Clinical Drug Comp:::Branded Drug Comp:::Branded Drug Comp:::Clinical Drug:::Branded Drug Comp:::Clinical Drug Comp:::Clinical...|
| Lisinopril 10 mg|  DRUG|    316151|                            lisinopril 10 MG[lisinopril 10 MG]|lisinopril 10 MG[lisinopril 10 MG]:::lisinopril 10 MG [Prinivil][lisinopril 10 MG [Prinivil]]:::lisinopril 10 MG [Carace][lisinopril 10 MG [Carace]...|316151:::567576:::565846:::393444:::563611:::314076:::328290:::857165:::316616:::857170:::207892:::564368:::568625:::316627:::206765:::385588:::201...|0.0000:::3.6543:::4.2783:::4.2805:::4.6016:::4.8302:::5.1265:::5.5412:::5.7201:::5.7306:::5.7759:::5.8688:::5.9488:::5.9750:::5.9838:::6.1065:::6.3...|0.0000:::0.0234:::0.0325:::0.0315:::0.0363:::0.0402:::0.0460:::0.0540:::0.0549:::0.0569:::0.0563:::0.0579:::0.0598:::0.0610:::0.0617:::0.0662:::0.0...|Clinical Drug Comp:::Branded Drug Comp:::Branded Drug Comp:::Clinical Drug Comp:::Branded Drug Comp:::Clinical Drug:::Clinical Drug Comp:::Clinical...|
+-----------------+------+----------+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_rxnorm_augmented_v2|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[rxnorm_code]|
|Language:|en|
|Size:|1.1 GB|
|Case sensitive:|false|
