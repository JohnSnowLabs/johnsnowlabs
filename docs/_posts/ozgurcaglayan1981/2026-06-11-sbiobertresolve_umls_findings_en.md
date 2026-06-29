---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes (Findings)
author: John Snow Labs
name: sbiobertresolve_umls_findings
date: 2026-06-11
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
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_findings_en_6.4.0_3.4_1781212530610.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_findings_en_6.4.0_3.4_1781212530610.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

data = spark.createDataFrame([["The patient presented with bilateral pitting edema, marked pallor, and mild jaundice. She reported persistent fatigue, shortness of breath on exertion, and palpitations over the past two weeks. Neurological signs included resting tremor, decreased grip strength, and hyperreflexia in the lower extremities."]]).toDF("text")
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

data = spark.createDataFrame([["The patient presented with bilateral pitting edema, marked pallor, and mild jaundice. She reported persistent fatigue, shortness of breath on exertion, and palpitations over the past two weeks. Neurological signs included resting tremor, decreased grip strength, and hyperreflexia in the lower extremities."]]).toDF("text")
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

val data = Seq("The patient presented with bilateral pitting edema, marked pallor, and mild jaundice. She reported persistent fatigue, shortness of breath on exertion, and palpitations over the past two weeks. Neurological signs included resting tremor, decreased grip strength, and hyperreflexia in the lower extremities.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                              | entity   | umls_code   | resolution                             | all_k_results                                                                       | all_k_distances                                                                     | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:---------------------------------------|:---------|:------------|:---------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| bilateral pitting edema                | PROBLEM  | C2237594    | bilateral pitting edema                | C2237594:::C0333243:::C0474434:::C2237429:::C1720371:::C0239872:::C1720667:::C20... | 0.0053:::5.8159:::5.9590:::5.9763:::6.2356:::6.8254:::6.9342:::6.9694:::7.0641::... | 0.0000:::0.0525:::0.0548:::0.0573:::0.0620:::0.0716:::0.0769:::0.0777:::0.0776::... | bilateral pitting edema:::edema pitted:::edema swelling:::pretibial pitting edem... |
| marked pallor                          | PROBLEM  | C0241137    | pallor                                 | C0241137:::C3808930:::C0858769:::C2216288:::C2032871:::C4060731:::C0239513:::C02... | 4.8115:::4.9060:::4.9650:::6.0754:::6.1752:::6.2752:::6.3400:::6.9676:::7.0999::... | 0.0370:::0.0375:::0.0390:::0.0593:::0.0615:::0.0626:::0.0626:::0.0788:::0.0801::... | pallor:::marked skin pallor:::generalized pallor:::elevation pallor:::localized ... |
| mild jaundice                          | PROBLEM  | C4746972    | jaundice, mild                         | C4746972:::C5543248:::C5543245:::C4748411:::C0022346:::C1865189:::C4016834:::C12... | 4.3314:::6.9510:::8.0172:::8.7211:::8.7350:::8.7897:::9.1888:::9.3150:::9.4603::... | 0.0297:::0.0754:::0.1046:::0.1196:::0.1210:::0.1236:::0.1386:::0.1359:::0.1411::... | jaundice, mild:::jaundice, transient:::jaundice sclerae, transient:::facial edem... |
| persistent fatigue                     | PROBLEM  | C0518656    | chronic fatigue                        | C0518656:::C5933598:::C5776953:::C2673338:::C4229032:::C4062597:::C2586108:::C14... | 4.8824:::5.0607:::5.2009:::5.6237:::5.8474:::5.8864:::5.9858:::6.1056:::6.7468::... | 0.0349:::0.0374:::0.0391:::0.0464:::0.0504:::0.0503:::0.0529:::0.0550:::0.0664::... | chronic fatigue:::physical fatigue:::feeling fatigued:::increased fatigue:::abno... |
| shortness of breath                    | PROBLEM  | C0748646    | intermittent shortness of breath       | C0748646:::C4718286:::C0748648:::C4287837:::C4054481:::C4054523:::C4290027:::C18... | 3.3515:::3.6904:::3.7597:::3.9274:::4.1537:::4.9471:::5.1391:::5.8453:::5.8964::... | 0.0163:::0.0198:::0.0206:::0.0223:::0.0250:::0.0357:::0.0384:::0.0505:::0.0508::... | intermittent shortness of breath:::reports shortness of breath:::shortness of br... |
| palpitations                           | PROBLEM  | C0030252    | palpitations                           | C0030252:::C0849793:::C0425598:::C6013375:::C0237314:::C2032982:::C4727920:::C35... | 0.0074:::4.6483:::5.3840:::5.8426:::5.8661:::6.0391:::6.9111:::7.4610:::7.4664::... | 0.0000:::0.0332:::0.0446:::0.0525:::0.0527:::0.0572:::0.0732:::0.0858:::0.0875::... | palpitations:::abnormal palpitations:::palpitations - bumping:::cardiac palpitat... |
| Neurological signs                     | TEST     | C0422837    | neurological signs symptoms            | C0422837:::C0027854:::C0542115:::C0235027:::C0521654:::C3275580:::C0751377:::C07... | 4.0568:::4.3126:::5.2931:::5.6331:::5.8569:::6.1490:::6.2597:::6.3473:::6.3724::... | 0.0249:::0.0278:::0.0416:::0.0463:::0.0516:::0.0559:::0.0574:::0.0598:::0.0603::... | neurological signs symptoms:::neurological manifestations:::neurologic changes::... |
| resting tremor                         | PROBLEM  | C2186983    | resting tremor in rle                  | C2186983:::C2186987:::C2186988:::C0240492:::C0241510:::C5543596:::C3553930:::C40... | 5.3757:::5.4097:::6.8559:::7.5726:::7.9555:::8.1654:::8.3099:::8.4734:::8.6042::... | 0.0461:::0.0456:::0.0750:::0.0895:::0.0986:::0.1065:::0.1083:::0.1157:::0.1165::... | resting tremor in rle:::resting tremor of head:::frequency of resting tremor of ... |
| decreased grip strength                | PROBLEM  | C3279724    | decreased hand grip strength           | C3279724:::C1698196:::C5436786:::C4479389:::C5933894:::C0231488:::C3550786:::C42... | 3.9862:::5.1893:::6.1292:::6.1866:::6.6705:::6.7477:::6.7826:::7.0021:::7.0128::... | 0.0237:::0.0407:::0.0572:::0.0574:::0.0668:::0.0689:::0.0688:::0.0743:::0.0743::... | decreased hand grip strength:::decreased arm strength:::decreased muscle power::... |
| hyperreflexia in the lower extremities | PROBLEM  | C4015304    | hyperreflexia in the lower extremities | C4015304:::C1836696:::C2674176:::C3670456:::C3549476:::C0240243:::C2047585:::C45... | 0.0066:::2.5880:::4.5667:::6.1905:::6.8618:::7.2944:::7.6982:::7.8805:::7.8848::... | 0.0000:::0.0104:::0.0327:::0.0599:::0.0758:::0.0807:::0.0925:::0.0955:::0.0977::... | hyperreflexia in the lower extremities:::hyperreflexia of the lower limbs:::hype... |
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
