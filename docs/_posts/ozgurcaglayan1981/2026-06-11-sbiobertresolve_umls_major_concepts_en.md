---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes (Major Concepts)
author: John Snow Labs
name: sbiobertresolve_umls_major_concepts
date: 2026-06-11
tags: [en, entity_resolution, licensed, clinical, umls, major_concepts]
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

This model maps clinical entities to 4 major categories of UMLS CUI codes. It is trained on the 2026AA release of the Unified Medical Language System (UMLS) dataset. The training data covers "Clinical Finding" (T033), "Medical Device" (T074), "Body Part, Organ, or Organ Component" (T023), and "Injury or Poisoning" (T037) semantic types, comprising approximately 1,270,000 name-CUI pairs. The model uses `sbiobert_base_cased_mli_onnx` embeddings.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_major_concepts_en_6.4.0_3.4_1781216324494.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_major_concepts_en_6.4.0_3.4_1781216324494.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Cerebrovascular_Disease","Communicable_Disease","Diabetes","Disease_Syndrome_Disorder","Heart_Disease","Hyperlipidemia","Hypertension","Injury_or_Poisoning","Kidney_Disease","Medical_Device","Obesity","Oncological","Overweight","Psychological_Condition","Symptom","VS_Finding","ImagingFindings","EKG_Findings","Vaccine_Name","RelativeDate"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_major_concepts","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([["The patient presented with hepatomegaly and peripheral edema. She has a history of tibial fracture and ligament tear in the left knee. She was fitted with a prosthetic knee implant and monitored via an implantable cardiac monitor."]]).toDF("text")
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
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Cerebrovascular_Disease","Communicable_Disease","Diabetes","Disease_Syndrome_Disorder","Heart_Disease","Hyperlipidemia","Hypertension","Injury_or_Poisoning","Kidney_Disease","Medical_Device","Obesity","Oncological","Overweight","Psychological_Condition","Symptom","VS_Finding","ImagingFindings","EKG_Findings","Vaccine_Name","RelativeDate"])

chunk2doc = medical.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_major_concepts","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([["The patient presented with hepatomegaly and peripheral edema. She has a history of tibial fracture and ligament tear in the left knee. She was fitted with a prosthetic knee implant and monitored via an implantable cardiac monitor."]]).toDF("text")
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
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Cerebrovascular_Disease", "Communicable_Disease", "Diabetes", "Disease_Syndrome_Disorder", "Heart_Disease", "Hyperlipidemia", "Hypertension", "Injury_or_Poisoning", "Kidney_Disease", "Medical_Device", "Obesity", "Oncological", "Overweight", "Psychological_Condition", "Symptom", "VS_Finding", "ImagingFindings", "EKG_Findings", "Vaccine_Name", "RelativeDate"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_umls_major_concepts", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
))

val data = Seq("The patient presented with hepatomegaly and peripheral edema. She has a history of tibial fracture and ligament tear in the left knee. She was fitted with a prosthetic knee implant and monitored via an implantable cardiac monitor.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                   | entity                    | umls_code   | resolution                  | all_k_results                                                                       | all_k_distances                                                                     | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:----------------------------|:--------------------------|:------------|:----------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| hepatomegaly                | Symptom                   | C0019209    | hepatomegaly                | C0019209:::C3277279:::C5436272:::C1835881:::C4746801:::C3275672:::C0744871:::C07... | 0.0072:::4.9152:::5.3459:::5.3965:::5.8476:::6.1865:::6.4947:::6.5779:::7.1451::... | 0.0000:::0.0386:::0.0438:::0.0463:::0.0544:::0.0606:::0.0649:::0.0690:::0.0813::... | hepatomegaly:::hepatomegaly (variable):::progressive hepatomegaly:::fluctuating ... |
| peripheral edema            | Symptom                   | C1820687    | distal peripheral edema     | C1820687:::C5970454:::C0521464:::C6053273:::C0544449:::C0577245:::C2825502:::C18... | 4.9970:::7.1707:::7.3667:::7.9493:::7.9676:::8.2377:::8.3377:::8.3708:::8.4964::... | 0.0383:::0.0771:::0.0828:::0.1008:::0.0974:::0.1067:::0.1070:::0.1096:::0.1086::... | distal peripheral edema:::peripheral nerve swelling:::cutaneous edema:::peripher... |
| tibial fracture             | Injury_or_Poisoning       | C0040185    | tibial fracture             | C0040185:::C0262488:::C0272767:::C3687007:::C5691295:::C0749492:::C2862392:::C01... | 0.0072:::4.3259:::4.7913:::4.8150:::5.1589:::5.3061:::5.7201:::5.8100:::5.8214::... | 0.0000:::0.0294:::0.0356:::0.0372:::0.0424:::0.0455:::0.0513:::0.0536:::0.0543::... | tibial fracture:::distal tibia fracture:::fracture of tibial shaft:::tibiotarsal... |
| ligament tear               | Disease_Syndrome_Disorder | C0262538    | ligament tear               | C0262538:::C0435141:::C0435001:::C0435002:::C0850773:::C5700108:::C1443029:::C04... | 0.0069:::4.5686:::4.9397:::5.5044:::6.0969:::6.5182:::6.5712:::6.5793:::6.9161::... | 0.0000:::0.0328:::0.0375:::0.0472:::0.0578:::0.0669:::0.0676:::0.0669:::0.0746::... | ligament tear:::ligament laceration:::ligament injury:::partial ligament tear:::... |
| prosthetic knee implant     | Medical_Device            | C3873943    | implantable knee prosthesis | C3873943:::C4735805:::C0022748:::C0438884:::C4735806:::C3877432:::C3494579:::C19... | 4.6810:::5.2232:::5.6074:::6.2525:::6.5390:::6.6430:::6.6478:::6.6975:::6.9131::... | 0.0347:::0.0451:::0.0516:::0.0649:::0.0711:::0.0735:::0.0700:::0.0734:::0.0797::... | implantable knee prosthesis:::knee prosthetic implant brand:::prosthesis knee:::... |
| implantable cardiac monitor | Medical_Device            | C3879681    | implantable cardiac monitor | C3879681:::C3877203:::C0581396:::C0182148:::C1283808:::C3874706:::C0993755:::C01... | 0.0067:::5.7802:::6.6002:::6.7141:::6.9380:::7.0654:::7.2127:::7.4526:::7.4993::... | 0.0000:::0.0500:::0.0649:::0.0668:::0.0714:::0.0753:::0.0780:::0.0830:::0.0835::... | implantable cardiac monitor:::implantable cardiac monitor patient activator:::ca... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_major_concepts|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|3.7 GB|
|Case sensitive:|false|
