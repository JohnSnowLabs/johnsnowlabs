---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes (Drug & Substance)
author: John Snow Labs
name: sbiobertresolve_umls_drug_substance
date: 2026-06-11
tags: [en, entity_resolution, licensed, clinical, umls, drug_substance]
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

This model maps drug and substance mentions to UMLS CUI codes. It is trained on the 2026AA release of the Unified Medical Language System (UMLS) dataset. The training data covers the "Pharmacologic Substance" (T121), "Hazardous or Poisonous Substance" (T131), "Antibiotic" (T195), and "Clinical Drug" (T200) semantic types, comprising approximately 736,000 name-CUI pairs. The model uses `sbiobert_base_cased_mli_onnx` embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_drug_substance_en_6.4.0_3.4_1781201167587.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_drug_substance_en_6.4.0_3.4_1781201167587.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_drug_substance","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([["Concurrent exposure to warfarin and aspirin increased the risk of bleeding complications.The patient reported a hypersensitivity reaction to penicillin during childhood. CYP2D6 polymorphisms may affect the metabolism of codeine and influence therapeutic response."]]).toDF("text")
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

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_drug_substance","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([["Concurrent exposure to warfarin and aspirin increased the risk of bleeding complications.The patient reported a hypersensitivity reaction to penicillin during childhood. CYP2D6 polymorphisms may affect the metabolism of codeine and influence therapeutic response."]]).toDF("text")
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
    .pretrained("sbiobertresolve_umls_drug_substance", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
))

val data = Seq("Concurrent exposure to warfarin and aspirin increased the risk of bleeding complications.The patient reported a hypersensitivity reaction to penicillin during childhood. CYP2D6 polymorphisms may affect the metabolism of codeine and influence therapeutic response.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk   | entity   | umls_code   | resolution   | all_k_results                                                                                                                                                                                       | all_k_distances                                                                                                                                                 | all_k_cosine_distances                                                                                                                                          | all_k_resolutions                                                                                                                                                                                                                                                                                         |
|:------------|:---------|:------------|:-------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| warfarin    | DRUG     | C0043031    | warfarin     | C0043031:::C1564392:::C3216124:::C4688338:::C2917452:::C3216123:::C4700122:::C0605881:::C0376218:::C0282378:::C2932026:::C3216122:::C4726812                                                        | 0.0076:::5.5030:::5.8307:::5.9602:::6.0613:::6.1307:::6.8694:::7.1658:::7.3749:::7.5164:::7.8038:::7.8668:::9.2414                                              | 0.0000:::0.0509:::0.0571:::0.0593:::0.0616:::0.0629:::0.0799:::0.0873:::0.0914:::0.0960:::0.1039:::0.1041:::0.1472                                              | warfarin:::gen-warfarin:::warfarin pill:::(s)-warfarin:::warfarin reversal agent:::warfarin oral product:::coumadin (warfarin):::pindone - warfarin:::warfarin sodium:::warfarin potassium:::tecarfarin:::warfarin injectable product:::tecarfarin sodium                                                 |
| aspirin     | DRUG     | C0004057    | aspirin      | C0004057:::C5874014:::C0085847:::C0719394:::C1330609:::C0732305:::C0721617:::C0718687:::C3208543:::C0981808:::C3843719:::C3657044:::C0718828:::C0719069:::C0699267                                  | 0.0065:::4.6537:::4.6710:::5.2103:::5.7011:::5.7392:::6.0872:::6.4565:::6.5413:::6.7318:::6.8337:::6.9156:::7.0098:::7.0618:::7.0645                            | 0.0000:::0.0362:::0.0362:::0.0458:::0.0550:::0.0545:::0.0624:::0.0701:::0.0721:::0.0765:::0.0775:::0.0808:::0.0833:::0.0848:::0.0837                            | aspirin:::aspirin ec:::aspirin-like agent:::aspirin coating:::ysp aspirin:::oral aspirin:::med aspirin:::aspirin buffered:::aspirin pill:::aspirin sodium:::aspirin or aspirin-containing product:::glucose-aspirin:::bayer aspirin:::ctd aspirin:::empirin                                               |
| penicillin  | DRUG     | C0030842    | penicillin   | C0030842:::C0368637:::C0070233:::C0030840:::C0030827:::C0733823:::C0072176:::C1144789:::C0002435:::C5437787:::C0309731:::C0071128:::C0070557:::C2052681:::C0070217:::C0646668:::C0030830            | 0.0068:::3.3155:::3.5097:::3.7410:::4.4491:::4.5848:::4.7200:::5.4107:::5.8299:::5.8894:::6.0979:::6.1210:::6.1842:::6.4158:::6.6279:::6.6613:::6.7066          | 0.0000:::0.0199:::0.0222:::0.0249:::0.0361:::0.0380:::0.0393:::0.0534:::0.0627:::0.0612:::0.0675:::0.0690:::0.0700:::0.0749:::0.0808:::0.0813:::0.0807          | penicillin:::penicillin at:::penicillin n:::penicillin-v:::penicillin g:::penicillin vk:::propicillin:::penicillin drug:::penicillin hx:::penicillin-containing product:::penicillin-strep:::pirbenicillin:::penicillin b:::penicillin combinations:::penamecillin:::cpe-penicillin:::procaine penicillin |
| codeine     | DRUG     | C0009214    | codéine      | C0009214:::C1564489:::C0015109:::C1321982:::C0719406:::C0771376:::C1658635:::C1878775:::C1530537:::C0722815:::C1245651:::C2106312:::C0604312:::C5228588:::C0643805:::C2699334:::C0539178:::C0771490 | 0.0069:::5.7327:::5.9077:::7.0613:::7.3694:::7.8120:::8.2009:::8.4765:::8.5368:::8.6281:::8.7298:::8.7403:::8.7599:::8.7676:::8.7865:::8.8030:::8.8626:::8.9205 | 0.0000:::0.0542:::0.0572:::0.0824:::0.0870:::0.1010:::0.1087:::0.1178:::0.1163:::0.1202:::0.1277:::0.1237:::0.1266:::0.1230:::0.1280:::0.1285:::0.1288:::0.1326 | codéine:::codétricine:::codethyline:::codeine hcl:::codehist dh:::codeine anhyd:::codeprex:::ascomp with codeine:::decoderm:::procort:::codeine elixir:::codeine combinations:::caytine:::padcev:::ceritine:::citatepine:::scriptene:::codeine camsyl                                                     |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_drug_substance|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|2.1 GB|
|Case sensitive:|false|