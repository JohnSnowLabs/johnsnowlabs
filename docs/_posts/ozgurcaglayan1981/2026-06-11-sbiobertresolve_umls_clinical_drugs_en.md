---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes (Clinical Drug)
author: John Snow Labs
name: sbiobertresolve_umls_clinical_drugs
date: 2026-06-11
tags: [en, entity_resolution, licensed, clinical, umls, clinical_drug]
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

This model maps clinical drug entities to UMLS CUI codes. It is trained on the 2026AA release of the Unified Medical Language System (UMLS) dataset. The training data covers the "Clinical Drug" (T200) semantic type, comprising approximately 345,000 name-CUI pairs. Unlike the broader drug_substance resolver (T121/T131/T195/T200), this model focuses exclusively on dose-formulation strings such as 'metformin 1000 mg oral tablet'. The model uses `sbiobert_base_cased_mli_onnx` embeddings.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_clinical_drugs_en_6.4.0_3.4_1781207811190.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_clinical_drugs_en_6.4.0_3.4_1781207811190.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained("ner_posology_greedy","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("posology_ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","posology_ner"])\
    .setOutputCol("posology_ner_chunk")\
    .setWhiteList(["DRUG"])

chunk2doc = Chunk2Doc()\
    .setInputCols("posology_ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_clinical_drugs","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([["The patient was prescribed Metformin 500 mg orally twice daily for the management of type 2 diabetes mellitus. Following the diagnosis of hypertension, Lisinopril 10 mg was initiated once daily and the patient's blood pressure improved within two weeks.For postoperative pain control, the physician ordered Ibuprofen 400 mg every 6 hours as needed, not to exceed 1,600 mg per day."]]).toDF("text")
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

ner_model = medical.NerModel.pretrained("ner_posology_greedy","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("posology_ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","posology_ner"])\
    .setOutputCol("posology_ner_chunk")\
    .setWhiteList(["DRUG"])

chunk2doc = medical.Chunk2Doc()\
    .setInputCols("posology_ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_clinical_drugs","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([["The patient was prescribed Metformin 500 mg orally twice daily for the management of type 2 diabetes mellitus. Following the diagnosis of hypertension, Lisinopril 10 mg was initiated once daily and the patient's blood pressure improved within two weeks.For postoperative pain control, the physician ordered Ibuprofen 400 mg every 6 hours as needed, not to exceed 1,600 mg per day."]]).toDF("text")
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
    .pretrained("ner_posology_greedy", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("posology_ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "posology_ner"))
    .setOutputCol("posology_ner_chunk")
    .setWhiteList(Array("DRUG"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("posology_ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_umls_clinical_drugs", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
))

val data = Seq("The patient was prescribed Metformin 500 mg orally twice daily for the management of type 2 diabetes mellitus. Following the diagnosis of hypertension, Lisinopril 10 mg was initiated once daily and the patient's blood pressure improved within two weeks.For postoperative pain control, the physician ordered Ibuprofen 400 mg every 6 hours as needed, not to exceed 1,600 mg per day.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk               | entity   | umls_code   | resolution                   | all_k_results                                                                                                                                                                                                             | all_k_distances                                                                                                                                                                   | all_k_cosine_distances                                                                                                                                                            | all_k_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:------------------------|:---------|:------------|:-----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Metformin 500 mg orally | DRUG     | C0978483    | metformin 500 mg oral tablet | C0978483:::C2719777:::C1329173:::C2719796:::C2719778:::C4281893:::C4282268:::C0937116:::C0694063:::C0978484:::C1319618:::C0701677                                                                                         | 4.5326:::5.6210:::6.0528:::6.2020:::6.4206:::6.5828:::6.6593:::7.3168:::7.3456:::7.4618:::7.5229:::7.5354                                                                         | 0.0331:::0.0512:::0.0590:::0.0625:::0.0672:::0.0703:::0.0718:::0.0867:::0.0873:::0.0909:::0.0916:::0.0932                                                                         | metformin 500 mg oral tablet:::metformin hydrochloride 500 mg:::metformin 500 mg/5 ml oral solution:::metformin hydrochloride 500 mg [glumetza]:::metformin hydrochloride 500 mg [glucophage]:::metformin (eqv-fortamet) 500mg sa tab:::metformin (eqv-glumetza) 500mg sa tab:::glucomannan 500 mg oral capsule:::glucosamine 500 mg oral capsule:::metformin hydrochloride 500 mg oral tablet [metformin]:::glucosamine 500 mg oral tablet:::metformin hydrochloride 500 mg oral tablet [glucophage]                           |
| Lisinopril 10 mg        | DRUG     | C0987217    | lisinopril 10 mg             | C0987217:::C1599995:::C1306426:::C1596055:::C0981555:::C2710728:::C0989578:::C0981441:::C1601040:::C0989604:::C0707937:::C1262965:::C0354403:::C1617547:::C1276892:::C3820195:::C0988891:::C1995640:::C0991735:::C1127563 | 0.0074:::3.6546:::4.2803:::4.6024:::4.8302:::5.5401:::5.7207:::5.8436:::5.9488:::5.9742:::5.9828:::6.1063:::6.4693:::6.4730:::6.4924:::6.5251:::6.5353:::6.5554:::6.6530:::6.7265 | 0.0000:::0.0234:::0.0315:::0.0364:::0.0402:::0.0540:::0.0549:::0.0598:::0.0598:::0.0610:::0.0616:::0.0662:::0.0713:::0.0722:::0.0711:::0.0732:::0.0731:::0.0732:::0.0756:::0.0787 | lisinopril 10 mg:::lisinopril 10 mg [prinivil]:::imidapril 10 mg:::lisinopril 10 mg [zestril]:::lisinopril 10 mg oral tablet:::fosinopril sodium 10 mg:::quinapril 10 mg:::fosinopril 10 mg oral tablet:::quinapril 10 mg [accupril]:::ramipril 10 mg:::lisinopril 10 mg oral tablet [prinivil]:::lercanidipine 10 mg:::lisinopril 10 mg oral tablet [zestril]:::ramipril 10 mg [altace]:::imidapril 10 mg oral tablet:::apremilast 10 mg:::pindolol 10 mg:::nebivolol 10 mg:::propranolol 10 mg oral tablet:::citalopram 10 mg |
| Ibuprofen 400 mg        | DRUG     | C0992428    | ibuprofen 400 mg             | C0992428:::C1600124:::C0689173:::C0786114:::C2718523:::C0590278:::C0708104:::C2718524:::C2718525:::C0987632:::C4282078:::C5188030:::C2718526:::C0688333:::C0350792:::C5188032:::C0987753                                  | 0.0078:::4.0010:::4.1486:::4.2276:::5.7797:::6.3011:::6.4074:::6.4615:::6.5888:::7.0238:::7.0289:::7.0857:::7.2126:::7.2462:::7.2977:::7.3090:::7.3209                            | 0.0000:::0.0258:::0.0278:::0.0293:::0.0553:::0.0652:::0.0664:::0.0693:::0.0717:::0.0816:::0.0816:::0.0821:::0.0859:::0.0876:::0.0882:::0.0877:::0.0898                            | ibuprofen 400 mg:::ibuprofen 400 mg [ibu]:::ibuprofen 400mg tab ud:::ibuprofen 400 mg oral capsule:::fenoprofen 400 mg:::ibuprofen 400 mg oral tablet [relcofen]:::ibuprofen 400 mg oral tablet [ibu]:::fenoprofen 400 mg oral capsule:::fenoprofen 400 mg [nalfon]:::meprobamate 400 mg:::dexibuprofen 400 mg oral tablet:::ibuprofen 4 mg/ml:::fenoprofen 400 mg oral capsule [nalfon]:::cimetidine 400mg tab ud:::mecillinam 400mg injection:::ibuprofen 4 mg/ml [caldolor]:::methocarbamol 400 mg                           |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_clinical_drugs|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|1.0 GB|
|Case sensitive:|false|