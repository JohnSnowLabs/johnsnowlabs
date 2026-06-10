---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes (Clinical Drug)
author: John Snow Labs
name: sbiobertresolve_umls_clinical_drugs
date: 2026-06-10
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
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_clinical_drugs_en_6.4.0_3.4_1781087540521.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_clinical_drugs_en_6.4.0_3.4_1781087540521.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

data = spark.createDataFrame([["She was immediately given hydrogen peroxide 30 mg to treat the infection on her leg, and has been advised Neosporin Cream for 5 days. She has a history of taking magnesium hydroxide 100mg/1ml and metformin 1000 mg."]]).toDF("text")
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

data = spark.createDataFrame([["She was immediately given hydrogen peroxide 30 mg to treat the infection on her leg, and has been advised Neosporin Cream for 5 days. She has a history of taking magnesium hydroxide 100mg/1ml and metformin 1000 mg."]]).toDF("text")
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

val data = Seq("She was immediately given hydrogen peroxide 30 mg to treat the infection on her leg, and has been advised Neosporin Cream for 5 days. She has a history of taking magnesium hydroxide 100mg/1ml and metformin 1000 mg.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                     | entity   | umls_code   | resolution                      | all_k_results                                                                                                                                                                                                                                                         | all_k_distances                                                                                                                                                                                                       | all_k_cosine_distances                                                                                                                                                                                                | all_k_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:------------------------------|:---------|:------------|:--------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| hydrogen peroxide 30 mg       | DRUG     | C1126248    | hydrogen peroxide 30 mg/ml      | C1126248:::C0304655:::C0304656:::C1154260:::C2242362:::C1724195:::C1131243:::C2344184:::C3163030:::C1128256:::C5210274:::C1124028:::C0988280:::C5964160:::C1146355:::C1146033:::C1124248:::C1140382                                                                   | 4.3736:::4.7154:::6.2109:::6.8676:::7.2759:::7.4670:::7.8317:::7.8579:::7.9625:::8.1030:::8.2337:::8.2724:::8.2933:::8.3435:::8.4092:::8.4143:::8.5022:::8.5770                                                       | 0.0323:::0.0369:::0.0649:::0.0807:::0.0890:::0.0957:::0.1018:::0.1060:::0.1079:::0.1103:::0.1137:::0.1175:::0.1145:::0.1201:::0.1231:::0.1210:::0.1251:::0.1254                                                       | hydrogen peroxide 30 mg/ml:::hydrogen peroxide solution 30%:::hydrogen peroxide 30 mg/ml cutaneous solution:::benzoyl peroxide 30 mg/ml:::hydrogen peroxide 30 mg/ml medicated pad:::benzoyl peroxide 30 mg/ml [oscion]:::hydrogen peroxide 300 mg/ml:::benzoyl peroxide 30 mg/ml [triaz]:::thioctic acid 30 mg:::hydroquinone 30 mg/ml:::acetic acid 30 mg/ml:::piperonyl butoxide 30 mg/ml:::opium 30 mg:::trospium chloride 30 mg:::undecylenic acid 30 mg/ml:::dimethicone 30 mg/ml:::chloroxylenol 30 mg/ml:::menthol 30 mg/ml                                                                                                                                                                                                                                        |
| Neosporin Cream               | DRUG     | C0132149    | neosporin cream                 | C0132149:::C4722788:::C0704071:::C0698988:::C1252084:::C0306945:::C0698810:::C0360316:::C0358174:::C0307085:::C0357999:::C1251940:::C0974727:::C0360244:::C1247195:::C0359716:::C1509926:::C0358020:::C1252116:::C0310288:::C0356678:::C0357619:::C0307668:::C0360245 | 0.0074:::7.0683:::7.3108:::7.3480:::7.3824:::7.4606:::7.7291:::7.8924:::8.0538:::8.1300:::8.2388:::8.2785:::8.5644:::8.6321:::8.6408:::8.6784:::8.6974:::8.7143:::8.7459:::8.7932:::8.7962:::8.8492:::8.8592:::8.8663 | 0.0000:::0.0888:::0.0953:::0.0934:::0.0964:::0.0941:::0.1053:::0.1114:::0.1145:::0.1128:::0.1218:::0.1238:::0.1298:::0.1265:::0.1320:::0.1307:::0.1323:::0.1342:::0.1395:::0.1318:::0.1337:::0.1387:::0.1415:::0.1374 | neosporin cream:::neomycin sulfate cream:::neosporin topical ointment:::naseptin cream:::amcinonide cream:::neo-synalar cream:::nystaform cream:::soframycin cream:::nystan cream:::nupercainal cream:::nystadermal cream:::halcinonide cream:::simply neosporin antibiotic topical ointment:::natuderm cream:::nystatin cream:::sudocrem cream:::niacinamide topical cream:::psoriderm cream:::crotamiton cream:::synalar cream:::sultrin cream:::neosporin eye drops:::spectazole cream:::noratex cream                                                                                                                                                                                                                                                                  |
| magnesium hydroxide 100mg/1ml | DRUG     | C1126785    | magnesium hydroxide 100 mg/ml   | C1126785:::C4051486:::C1131100:::C1134063:::C0778281:::C0980636:::C0356443:::C1131133:::C4048223:::C0359525:::C3500192:::C3265123:::C1133511:::C4051488:::C0793218:::C0356115:::C0691587:::C0776402:::C0697637:::C2684525:::C0979098:::C0715899:::C0698208            | 5.1252:::6.5641:::6.8205:::7.0081:::7.0173:::7.0506:::7.0547:::7.0767:::7.1689:::7.2416:::7.2417:::7.2721:::7.2836:::7.3015:::7.3448:::7.3736:::7.3960:::7.5039:::7.5564:::7.5581:::7.6073:::7.6521:::7.6525          | 0.0432:::0.0688:::0.0764:::0.0791:::0.0805:::0.0840:::0.0830:::0.0811:::0.0856:::0.0878:::0.0853:::0.0871:::0.0882:::0.0866:::0.0903:::0.0912:::0.0878:::0.0949:::0.0962:::0.0933:::0.0977:::0.0963:::0.0949          | magnesium hydroxide 100 mg/ml:::magnesium sulfate 100 mg:::sodium hydroxide 100 mg/ml:::magnesium carbonate 100 mg:::magnesium sulfate 1 gm in 100 ml injection:::thiamine hydrochloride 100mg/1ml injection:::efcortesol 100mg/1ml injection:::magnesium oxide 100 mg:::calcium gluconate 100mg/ml inj_#1:::calcium chloride 100mg/ml inj_#1:::magnesium citrate 100 mg:::thiamine hydrochloride 100 mg:::potassium hydroxide 100 mg/ml:::magnesium sulfate 100mg oral cap:::meptazinol 100mg/1ml injection:::netillin 100mg/1ml injection:::magnesium 100mg oral capsule:::netilmicin 100mg/1ml injection:::masteril 100mg/1ml injection:::magnesium glycinate 100 mg:::octreotide 100micrograms/1ml injection:::neoral 100mg/ml solution:::seconal sodium 100mg capsule |
| metformin 1000 mg             | DRUG     | C2719784    | metformin hydrochloride 1000 mg | C2719784:::C0978482:::C2719794:::C4282269:::C4282270:::C2719791:::C1131727:::C1127374:::C1134233:::C0988066:::C3831896:::C1378048:::C1130654:::C2709682:::C2918085:::C4239013:::C1178493:::C3153230:::C4034050:::C0698428                                             | 5.2990:::5.3787:::6.3065:::6.4404:::6.6587:::6.6636:::6.9815:::7.1144:::7.1224:::7.1367:::7.1479:::7.1979:::7.2507:::7.4017:::7.4986:::7.5102:::7.5206:::7.5244:::7.5976:::7.6009                                     | 0.0445:::0.0454:::0.0632:::0.0654:::0.0698:::0.0707:::0.0769:::0.0812:::0.0792:::0.0810:::0.0810:::0.0827:::0.0833:::0.0874:::0.0900:::0.0899:::0.0886:::0.0904:::0.0935:::0.0911                                     | metformin hydrochloride 1000 mg:::metformin hcl 1000mg tab:::metformin hydrochloride 1000 mg [glumetza]:::metformin (eqv-fortamet) 1000mg sa tab:::metformin (eqv-glumetza) 1000mg sa tab:::metformin hydrochloride 1000 mg [glucophage]:::glycerin 1000 mg:::guaifenesin 1000 mg:::glucosamine 1000 mg:::niacin 1000 mg:::fluralaner 1000 mg:::nabumetone 1000 mg:::mesalamine 1000 mg:::nalidixic acid 1000 mg:::aspirin 1000 mg:::ifosfamide 1000 mg:::glucosamine sulfate 1000 mg:::citicoline 1000 mg:::methotrexate 1000 mg:::azactam 1000 mg injection                                                                                                                                                                                                              |
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