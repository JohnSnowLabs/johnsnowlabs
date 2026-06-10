---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes (Findings)
author: John Snow Labs
name: sbiobertresolve_umls_findings
date: 2026-06-10
tags: [en, entity_resolution, licensed, clinical, umls, findings]
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

This model maps clinical findings to UMLS CUI codes. It is trained on the 2026AA release of the Unified Medical Language System (UMLS) dataset. The training data covers the "Finding" (T033) semantic type, comprising approximately 736,000 name-CUI pairs. The model uses `sbiobert_base_cased_mli_onnx` embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_findings_en_6.4.0_3.4_1781088479110.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_findings_en_6.4.0_3.4_1781088479110.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_findings","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([["A 28-year-old female with a history of gestational diabetes mellitus diagnosed with a HTG-induced pancreatitis associated with acute hepatitis and obesity."]]).toDF("text")
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

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_findings","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([["A 28-year-old female with a history of gestational diabetes mellitus diagnosed with a HTG-induced pancreatitis associated with acute hepatitis and obesity."]]).toDF("text")
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
    .pretrained("sbiobertresolve_umls_findings", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
))

val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed with a HTG-induced pancreatitis associated with acute hepatitis and obesity.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                     | entity   | umls_code   | resolution                                 | all_k_results                                                                                                                                                                                                                                   | all_k_distances                                                                                                                                                                                     | all_k_cosine_distances                                                                                                                                                                              | all_k_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:------------------------------|:---------|:------------|:-------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| gestational diabetes mellitus | PROBLEM  | C3532257    | uncontrolled gestational diabetes mellitus | C3532257:::C2183115:::C3161145:::C4303558:::C3840222:::C2114054:::C3874269:::C0455488:::C1313937:::C5769536:::C4511231:::C3648970:::C4304438                                                                                                    | 4.9165:::5.2208:::6.7677:::7.1690:::7.2145:::7.2549:::7.2947:::7.6204:::8.0204:::8.0207:::8.2793:::8.3303:::8.3387                                                                                  | 0.0357:::0.0401:::0.0666:::0.0750:::0.0773:::0.0778:::0.0776:::0.0852:::0.0947:::0.0953:::0.0999:::0.1037:::0.1033                                                                                  | uncontrolled gestational diabetes mellitus:::diabetes mellitus during pregnancy:::personal history of gestational diabetes:::maternal history of gestational diabetes:::supervision of high risk pregnancy with history of gestational diabetes mellitus done:::pre-existing maternal diabetes:::maternal history of diabetes mellitus:::h/o: diabetes mellitus:::fh: diabetes mellitus:::brachial plexus lesion due to diabetes mellitus:::lesion of skin due to diabetes mellitus:::gestational diabetes mellitus in pregnancy, controlled:::maternal history of diabetes mellitus type 2 (situation)                                                                                                                                                                       |
| a HTG-induced pancreatitis    | PROBLEM  | C3808945    | secondary pancreatitis                     | C3808945:::C1835382:::C3887021:::C5678547:::C0311178:::C4554179:::C1556678:::C1963198:::C1556677:::C1556680:::C0747197:::C0940751:::C6053254:::C1142315:::C1969419:::C0813176:::C1963128:::C2198728:::C0940754:::C0941207:::C2021748:::C4480022 | 6.5311:::7.0593:::7.8104:::8.1008:::8.2069:::8.2771:::8.4365:::8.4504:::8.5014:::8.8644:::9.0496:::9.0603:::9.0724:::9.0947:::9.1106:::9.3806:::9.5456:::9.5847:::9.6197:::9.6421:::9.6656:::9.6687 | 0.0693:::0.0806:::0.0971:::0.1090:::0.1119:::0.1151:::0.1193:::0.1189:::0.1197:::0.1301:::0.1318:::0.1358:::0.1408:::0.1303:::0.1404:::0.1411:::0.1528:::0.1505:::0.1480:::0.1521:::0.1521:::0.1566 | secondary pancreatitis:::pancreatitis, acute in some:::history of pancreatitis (situation):::pancreatitis, acute or chronic:::hyperalimentation formula for pancreatitis:::pancreatitis, ctcae_5:::grade 2 pancreatitis, ctcae:::pancreatitis, ctcae_3:::grade 1 pancreatitis, ctcae:::grade 4 pancreatitis, ctcae:::pancreatitis chronic with acute exacerbation:::stone appearance of pancreatic obstruction:::pancreatitis, ctcae 6.0:::biopsy pancreas abnormal:::pancreatitis, chronic, susceptibility to:::pancreas problem:::pancreatic hemorrhage, ctcae:::abdominal ct atrophic pancreatic:::partial pancreatic obstruction:::appearance of pancreatic obstruction:::abdominal mri dilated pancreatic duct:::bedside index of severity in acute pancreatitis (bisap) |
| acute hepatitis               | PROBLEM  | C4750596    | acute infectious hepatitis suspected       | C4750596:::C0151325:::C0744827:::C5233349:::C0559141:::C1262283:::C1861901:::C2362615:::C0458068:::C1287410:::C0744864:::C0744835:::C3551918:::C5232888:::C0239571:::C3160950:::C0744834:::C0744863                                             | 5.1797:::6.7695:::7.8964:::8.1287:::8.1904:::8.4223:::8.4769:::8.5234:::8.5465:::8.7510:::8.8541:::9.2669:::9.2799:::9.3626:::9.4410:::9.4805:::9.7114:::9.7988                                     | 0.0412:::0.0710:::0.0962:::0.1028:::0.1039:::0.1094:::0.1111:::0.1118:::0.1139:::0.1196:::0.1217:::0.1353:::0.1325:::0.1363:::0.1421:::0.1440:::0.1489:::0.1480                                     | acute infectious hepatitis suspected:::infectious hepatitis present:::active hepatitis:::abnormal liver enzymes during acute episode:::fh: hepatitis:::exposure to hepatitis a:::subacute progressive viral hepatitis:::exposure to hepatitis:::immune status hepatitis a:::finding of hepatitis a status:::hepatitis status:::b exposure hepatitis:::hepatomegaly associated with infection:::elevated liver enzymes during acute episodes:::fetor hepaticus:::withdrawal hepatitis:::b core hepatitis:::hepatitis serology abnormal                                                                                                                                                                                                                                         |
| obesity                       | PROBLEM  | C4759928    | obesity                                    | C4759928:::C0311277:::C4016383:::C0426650:::C0455493:::C4551560:::C2945676:::C0455373:::C4479421:::C3549879:::C0497406:::C0240674:::C2026325:::C0154270:::C1281429:::C0240597:::C0424629                                                        | 0.0060:::3.8687:::5.1252:::5.1358:::5.2384:::5.4275:::5.4309:::5.6515:::5.7546:::5.8175:::5.9281:::6.0570:::6.3784:::6.4720:::6.5115:::6.6109:::6.6449                                              | 0.0000:::0.0218:::0.0393:::0.0383:::0.0403:::0.0431:::0.0435:::0.0473:::0.0485:::0.0506:::0.0513:::0.0547:::0.0609:::0.0619:::0.0634:::0.0652:::0.0657                                              | obesity:::abdominal obesity:::obesity, association with:::obese abdomen:::h/o: obesity:::trunk obesity:::diabetes obesity:::fh: obesity:::overweight or obese:::obesity, increased risk of:::overweight:::pectoral obesity:::centrifugal obesity:::localised obesity:::exogenous obesity:::obesity sensation:::peripheral obesity                                                                                                                                                                                                                                                                                                                                                                                                                                             |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_findings|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|2.1 GB|
|Case sensitive:|false|