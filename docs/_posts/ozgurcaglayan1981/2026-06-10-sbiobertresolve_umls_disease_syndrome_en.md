---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes (Disease or Syndrome)
author: John Snow Labs
name: sbiobertresolve_umls_disease_syndrome
date: 2026-06-10
tags: [en, entity_resolution, licensed, clinical, umls, disease_syndrome]
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

This model maps disease and syndrome entities to UMLS CUI codes. It is trained on the 2026AA release of the Unified Medical Language System (UMLS) dataset. The training data covers the "Disease or Syndrome" (T047) semantic type, comprising approximately 399,000 name-CUI pairs. The model uses `sbiobert_base_cased_mli_onnx` embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_disease_syndrome_en_6.4.0_3.4_1781089851673.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_disease_syndrome_en_6.4.0_3.4_1781089851673.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained("ner_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("clinical_ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","clinical_ner"])\
    .setOutputCol("clinical_ner_chunk")\
    .setWhiteList(["PROBLEM"])

chunk2doc = Chunk2Doc()\
    .setInputCols("clinical_ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_disease_syndrome","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([["A 28-year-old female with a history of gestational diabetes mellitus and type 2 diabetes mellitus. She presents with joint pain, swelling, and stiffness diagnosed with rheumatoid arthritis."]]).toDF("text")
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

ner_model = medical.NerModel.pretrained("ner_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("clinical_ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","clinical_ner"])\
    .setOutputCol("clinical_ner_chunk")\
    .setWhiteList(["PROBLEM"])

chunk2doc = medical.Chunk2Doc()\
    .setInputCols("clinical_ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_disease_syndrome","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([["A 28-year-old female with a history of gestational diabetes mellitus and type 2 diabetes mellitus. She presents with joint pain, swelling, and stiffness diagnosed with rheumatoid arthritis."]]).toDF("text")
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
    .pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("clinical_ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "clinical_ner"))
    .setOutputCol("clinical_ner_chunk")
    .setWhiteList(Array("PROBLEM"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("clinical_ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_umls_disease_syndrome", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
))

val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus and type 2 diabetes mellitus. She presents with joint pain, swelling, and stiffness diagnosed with rheumatoid arthritis.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                     | entity   | umls_code   | resolution                    | all_k_results                                                                                                                                                                                                  | all_k_distances                                                                                                                                                              | all_k_cosine_distances                                                                                                                                                   | all_k_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:------------------------------|:---------|:------------|:------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| gestational diabetes mellitus | PROBLEM  | C0085207    | gestational diabetes mellitus | C0085207:::C0032969:::C2063017:::C1283034:::C0271663:::C3646651:::C0271662:::C3839604:::C3649763:::C3662020:::C3828492:::C5942818:::C5942820:::C2011197                                                        | 0.0067:::4.1539:::4.7727:::4.8705:::4.8875:::5.1051:::5.1555:::5.3716:::5.4234:::5.6776:::5.8169:::5.8801:::6.0537:::6.1888                                                  | 0.0000:::0.0253:::0.0332:::0.0347:::0.0354:::0.0381:::0.0394:::0.0423:::0.0435:::0.0474:::0.0503:::0.0512:::0.0541:::0.0562                                              | gestational diabetes mellitus:::pregnancy diabetes mellitus:::pregnancy complicated by diabetes mellitus:::maternal diabetes mellitus:::gestational diabetes mellitus, a2:::pregnancy complicated by chronic diabetes mellitus:::gestational diabetes mellitus, a1:::postpartum gestational diabetes mellitus:::chronic diabetes mellitus in pregnancy:::pre-existing diabetes mellitus in pregnancy:::pregestational diabetes:::gestational diabetes type a2:::gestational diabetes type a1:::gestational diabetes mellitus with baby delivered          |
| type 2 diabetes mellitus      | PROBLEM  | C0011860    | type 2 diabetes mellitus      | C0011860:::C1832387:::C0348921:::C1719939:::C0271640:::C0877302:::C1832544:::C1842642:::C1852092:::C0011849:::C0349363:::C0837056:::C0348919:::C5436966                                                        | 0.0070:::3.6034:::4.9385:::5.0371:::5.1726:::5.3524:::5.4309:::5.5112:::5.5551:::5.5987:::5.8758:::5.8890:::5.9425:::6.0150                                                  | 0.0000:::0.0194:::0.0359:::0.0381:::0.0397:::0.0425:::0.0443:::0.0456:::0.0458:::0.0462:::0.0515:::0.0517:::0.0526:::0.0551                                              | type 2 diabetes mellitus:::type 2 diabetes mellitus 2:::pre-existing type 2 diabetes mellitus:::type 2 diabetes mellitus with manifestations:::secondary diabetes mellitus:::insulin-requiring type 2 diabetes mellitus:::type 2 diabetes mellitus 1:::type 2 diabetes mellitus 4:::insulin-dependent diabetes mellitus 2:::diabetes mellitus:::type 2 diabetes mellitus with multiple complications:::type 2 diabetes mellitus with features of insulin resistance:::disorder of eye due to type 2 diabetes mellitus:::type 2 diabetes mellitus, digenic |
| joint pain                    | PROBLEM  | C0162296    | multiple joint pain           | C0162296:::C0748680:::C0423690:::C0553642:::C5700083:::C0013390:::C0745574:::C1142264:::C3662528:::C0745572:::C4545042:::C0031315:::C5828595:::C1262161:::C4048296                                             | 3.4504:::5.1713:::5.2815:::5.5688:::5.7619:::5.9212:::5.9733:::6.0781:::6.2333:::6.2363:::6.2373:::6.3354:::6.4641:::6.5134:::6.6049                                         | 0.0172:::0.0387:::0.0406:::0.0448:::0.0481:::0.0509:::0.0519:::0.0538:::0.0565:::0.0567:::0.0562:::0.0583:::0.0610:::0.0615:::0.0634                                     | multiple joint pain:::shoulder pain exertional:::facet joint pain:::myofascial pain:::chronic pain:::period pain:::knee pain swelling:::rest limb pain:::discogenic pain:::knee pain intermittent:::chronic visceral pain:::phantom limb pain:::chronic secondary pain:::ischaemic limb pain:::phantom limb pains                                                                                                                                                                                                                                         |
| swelling                      | PROBLEM  | C1411141    | wandering swelling            | C1411141:::C0037580:::C0281913:::C2938877:::C0497156:::C0859055:::C0241822:::C3160813:::C4049258:::C0221233:::C1407778:::C0948349:::C0030554                                                                   | 6.0652:::6.7033:::7.2990:::7.7316:::8.1316:::8.1947:::8.4103:::8.4798:::8.6388:::8.6840:::8.7349:::9.0167:::9.0294                                                           | 0.0556:::0.0665:::0.0783:::0.0893:::0.0991:::0.1015:::0.1079:::0.1076:::0.1105:::0.1153:::0.1144:::0.1200:::0.1198                                                       | wandering swelling:::soft tissue swelling:::muscles swelling:::limbal swelling:::swollen glands:::vascular edema:::calabar swelling:::vascular compression:::cerebral congestion:::cyclic edema:::tubular; swelling:::respiratory tract congestion:::tingling                                                                                                                                                                                                                                                                                             |
| stiffness                     | PROBLEM  | C1410087    | stiffness; spine              | C1410087:::C0014481:::C1861404:::C5554232:::C0277460:::C0085292:::C0854443:::C0243025:::C0086541:::C0006905:::C0263955:::C0263909:::C0851796:::C0265221:::C0019572:::C0863100:::C0151514:::C0947912:::C2678098 | 7.7413:::8.8846:::8.9371:::9.0314:::9.0319:::9.1908:::9.3593:::9.6352:::9.7710:::9.7882:::9.8258:::9.8368:::9.8779:::9.9123:::9.9924:::10.1205:::10.1773:::10.2047:::10.2054 | 0.0937:::0.1219:::0.1217:::0.1256:::0.1239:::0.1304:::0.1350:::0.1396:::0.1426:::0.1500:::0.1478:::0.1474:::0.1476:::0.1514:::0.1588:::0.1561:::0.1611:::0.1582:::0.1649 | stiffness; spine:::stiff sickness:::thumbs, stiff:::stiff lung:::scaly leg:::syndrome, stiff-person:::vascular fragility:::hards:::sore, oriental:::capillary fragility:::thoroughpin (disorder):::bowed tendon:::scaly conditions:::syndrome, hard:::hirsute:::tightness jaw:::atrophic:::fatigable weakness:::hysp1                                                                                                                                                                                                                                     |
| rheumatoid arthritis          | PROBLEM  | C0003873    | rheumatoid arthritis          | C0003873:::C0857204:::C0035436:::C3842272:::C0241786:::C0409651:::C0852006:::C0564784:::C0810054:::C0409653:::C0597908                                                                                         | 0.0065:::2.6535:::3.0396:::3.7696:::3.8339:::3.9094:::4.1216:::4.1870:::4.2107:::4.4322:::4.7068                                                                             | 0.0000:::0.0104:::0.0138:::0.0213:::0.0221:::0.0229:::0.0255:::0.0261:::0.0265:::0.0292:::0.0332                                                                         | rheumatoid arthritis:::rheumatoid arthropathy:::rheumatic arthritis:::rheumatoid arthritis - rheumatism:::anarthritic rheumatoid disease:::rheumatoid arthritis/allied condition:::rheumatoid arthritis and associated conditions:::rheumatoid arthritis of multiple joints:::rheumatoid arthritis and related disease:::rheumatoid arthritis with organ / system involvement:::rheumatoidlike arthritis                                                                                                                                                  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_disease_syndrome|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|1.2 GB|
|Case sensitive:|false|