---
layout: model
title: Sentence Entity Resolver for UMLS Codes - General Concepts
author: John Snow Labs
name: sbiobertresolve_umls_general_concepts
date: 2025-12-22
tags: [en, entity_resolution, licensed, clinical, umls]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.2.2
spark_version: 3.4
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

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_general_concepts_en_6.2.2_3.4_1766380914938.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_general_concepts_en_6.2.2_3.4_1766380914938.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setWhiteList(["Injury_or_Poisoning","Hyperlipidemia","Kidney_Disease","Oncological","Cerebrovascular_Disease",
                  "Oxygen_Therapy","Heart_Disease","Obesity","Disease_Syndrome_Disorder","Symptom","Treatment",
                  "Diabetes","Injury_or_Poisoning","Procedure","Symptom","Treatment","Drug_Ingredient","VS_Finding",
                  "Communicable_Disease","Drug_BrandName","Hypertension","Imaging_Technique"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings    .pretrained("sbiobert_base_cased_mli","en","clinical/models")\
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

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with an acute hepatitis, and obesity with a BMI of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting."""]]).toDF("text")

result = umls_lp.fit(data).transform(data)


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

ner_model = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner_jsl")

ner_model_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner_jsl"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Injury_or_Poisoning","Hyperlipidemia","Kidney_Disease","Oncological","Cerebrovascular_Disease",
                  "Oxygen_Therapy","Heart_Disease","Obesity","Disease_Syndrome_Disorder","Symptom","Treatment",
                  "Diabetes","Injury_or_Poisoning","Procedure","Symptom","Treatment","Drug_Ingredient","VS_Finding",
                  "Communicable_Disease","Drug_BrandName","Hypertension","Imaging_Technique"])

chunk2doc = medical.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings\
    .pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_general_concepts", "en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")\
    .setCaseSensitive(False)


umls_lp = nlp.Pipeline(stages=[
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

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with an acute hepatitis, and obesity with a BMI of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting."""]]).toDF("text")

result = umls_lp.fit(data).transform(data)

```
```scala


val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel
      .pretrained("sentence_detector_dl_healthcare","en","clinical/models")
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
    
val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, one prior episode of pancreatitis three years prior to presentation, using Sulfonylurea for eight years, and obesity with a BMI of 33.5 kg/m2, presented with a one-week history of frequent urination and polydipsia. Additionally, tube placement on chest was performed following a pneumothorax that occurred 10 years ago.").toDF("text")  

val res = p_model.fit(data).transform(data)


```
</div>

## Results

```bash


+-------------------------------+---------------------------+-----------+-------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ner_chunk                     | entity                    | umls_code | resolution                    | all_k_resolutions                                                                | all_k_results                                                                    | all_k_distances                                                                  | all_k_cosine_distances                                                           |
+-------------------------------+---------------------------+-----------+-------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| gestational diabetes mellitus | Diabetes                  | C0085207  | gestational diabetes mellitus | gestational diabetes mellitus:::pregnancy diabetes mellitus:::pregnancy compl... | C0085207:::C0032969:::C2063017:::C1283034:::C0271663:::C3646651:::C0271662:::... | 0.0000:::4.1541:::4.7731:::4.8692:::4.8845:::5.1056:::5.1560:::5.3717:::5.422... | 0.0000:::0.0253:::0.0332:::0.0347:::0.0354:::0.0381:::0.0394:::0.0423:::0.043... |
| type two diabetes mellitus    | Diabetes                  | C0011860  | type 2 diabetes mellitus      | type 2 diabetes mellitus:::disorder associated with type 2 diabetes mellitus:... | C0011860:::C1719939:::C1832387:::C0348921:::C0271640:::C0348919:::C0877302:::... | 2.0974:::4.0218:::4.3644:::5.0391:::5.1188:::5.1474:::5.1523:::5.1755:::5.186... | 0.0065:::0.0241:::0.0284:::0.0374:::0.0388:::0.0397:::0.0394:::0.0394:::0.039... |
| HTG-induced pancreatitis      | Disease_Syndrome_Disorder | C0376670  | alcohol-induced pancreatitis  | alcohol-induced pancreatitis:::immune-mediated pancreatitis:::graft pancreati... | C0376670:::C5208246:::C2350449:::C0030305:::C4302243:::C0267940:::C5197785:::... | 5.0379:::5.1012:::5.2246:::5.4594:::5.4631:::5.7266:::5.7850:::5.8433:::5.867... | 0.0406:::0.0413:::0.0442:::0.0478:::0.0480:::0.0522:::0.0537:::0.0543:::0.055... |
| hepatitis                     | Disease_Syndrome_Disorder | C0019158  | hepatitis                     | hepatitis:::hepatitis a:::hepatitis g:::viral hepatitis:::hepatitis d:::hepat... | C0019158:::C0019159:::C0814152:::C0042721:::C0011226:::C0854495:::C0854496:::... | 0.0000:::3.2380:::3.3070:::3.8885:::3.9127:::4.0509:::4.4446:::4.7614:::5.182... | 0.0000:::0.0168:::0.0176:::0.0242:::0.0246:::0.0263:::0.0318:::0.0367:::0.043... |
| obesity                       | Obesity                   | C0028754  | obesity                       | obesity:::abdominal obesity:::generalized obesity:::obesity gross:::overweigh... | C0028754:::C0342940:::C0342942:::C0857116:::C1561826:::C0694533:::C0028756:::... | 0.0000:::3.8693:::4.2493:::4.3092:::4.4595:::4.6116:::4.7044:::4.8433:::5.078... | 0.0000:::0.0218:::0.0268:::0.0272:::0.0290:::0.0316:::0.0327:::0.0343:::0.037... |
| polyuria                      | Symptom                   | C0032617  | polyuria                      | polyuria:::nocturnal polyuria:::vasopressin-related polyuria:::frequency of u... | C0032617:::C0848232:::C0011848:::C0016708:::C2830339:::C0018965:::C0271593:::... | 0.0000:::6.9423:::7.4279:::7.8679:::8.1204:::8.4072:::8.4671:::8.5297:::8.6544   | 0.0000:::0.0751:::0.0870:::0.0970:::0.1063:::0.1103:::0.1138:::0.1126:::0.1175   |
| polydipsia                    | Symptom                   | C0085602  | polydipsia                    | polydipsia:::polydipsia (nocturnal):::primary polydipsia:::organic primary po... | C0085602:::C0857397:::C0268813:::C5921912:::C1994993:::C1540939:::C0030508:::... | 0.0000:::6.0919:::6.3915:::8.3840:::8.4267:::8.7742:::9.9300:::9.9648:::9.9985   | 0.0000:::0.0572:::0.0635:::0.1105:::0.1111:::0.1217:::0.1520:::0.1553:::0.1552   |
| poor appetite                 | Symptom                   | C0232462  | poor appetite                 | poor appetite:::lack of appetite:::poor swallowing:::poor nutrition:::loss of... | C0232462:::C0003123:::C0011168:::C0162429:::C0426579:::C0578994:::C0241333:::... | 0.0000:::5.7668:::6.4633:::6.6977:::6.8478:::6.8481:::7.0058:::7.4409:::7.514... | 0.0000:::0.0482:::0.0611:::0.0652:::0.0685:::0.0681:::0.0712:::0.0809:::0.082... |
| vomiting                      | Symptom                   | C0042963  | vomiting                      | vomiting:::intermittent vomiting:::persistent vomiting:::periodic vomiting:::... | C0042963:::C0401157:::C0152165:::C0152164:::C0859028:::C0374544:::C4324485:::... | 0.0000:::3.6352:::5.4750:::5.7050:::5.8952:::6.1391:::6.1762:::6.2872:::6.297... | 0.0000:::0.0196:::0.0446:::0.0484:::0.0527:::0.0568:::0.0579:::0.0585:::0.059... |
+-------------------------------+---------------------------+-----------+-------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_general_concepts|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|4.0 GB|
|Case sensitive:|false|