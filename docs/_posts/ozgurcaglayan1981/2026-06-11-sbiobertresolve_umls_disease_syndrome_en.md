---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes (Disease or Syndrome)
author: John Snow Labs
name: sbiobertresolve_umls_disease_syndrome
date: 2026-06-11
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
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_disease_syndrome_en_6.4.0_3.4_1781214439467.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_disease_syndrome_en_6.4.0_3.4_1781214439467.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setOutputCol("ner_jsl")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner_jsl"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Disease_Syndrome_Disorder","Symptom"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
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

data = spark.createDataFrame([["The patient has a history of systemic lupus erythematosus, multiple sclerosis, and fibromyalgia. She was admitted with sepsis secondary to bacterial pneumonia and developed acute respiratory distress syndrome. Imaging showed findings consistent with pulmonary sarcoidosis and early liver cirrhosis."]]).toDF("text")
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
    .setOutputCol("ner_jsl")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner_jsl"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Disease_Syndrome_Disorder","Symptom"])

chunk2doc = medical.Chunk2Doc()\
    .setInputCols("ner_chunk")\
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

data = spark.createDataFrame([["The patient has a history of systemic lupus erythematosus, multiple sclerosis, and fibromyalgia. She was admitted with sepsis secondary to bacterial pneumonia and developed acute respiratory distress syndrome. Imaging showed findings consistent with pulmonary sarcoidosis and early liver cirrhosis."]]).toDF("text")
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
    .setOutputCol("ner_jsl")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_jsl"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Disease_Syndrome_Disorder", "Symptom"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
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

val data = Seq("The patient has a history of systemic lupus erythematosus, multiple sclerosis, and fibromyalgia. She was admitted with sepsis secondary to bacterial pneumonia and developed acute respiratory distress syndrome. Imaging showed findings consistent with pulmonary sarcoidosis and early liver cirrhosis.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                     | entity                    | umls_code   | resolution                    | all_k_results                                                                       | all_k_distances                                                                     | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:------------------------------|:--------------------------|:------------|:------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| systemic lupus erythematosus  | Disease_Syndrome_Disorder | C0024141    | systemic lupus erythematosus  | C0024141:::C0409974:::C0024137:::C1274838:::C6022675:::C0409977:::C0409976:::C07... | 0.0067:::3.4325:::4.0055:::4.4309:::4.4907:::4.5642:::4.5922:::4.6192:::4.6675::... | 0.0000:::0.0184:::0.0251:::0.0308:::0.0317:::0.0322:::0.0328:::0.0336:::0.0334::... | systemic lupus erythematosus:::lupus erythematosus:::cutaneous lupus erythematos... |
| sclerosis                     | Disease_Syndrome_Disorder | C0036412    | sclera disease                | C0036412:::C0263009:::C0036421:::C0007795:::C0237854:::C0004712:::C0036416:::C00... | 6.4563:::6.5690:::6.7129:::6.8109:::6.8550:::6.9680:::7.2263:::7.5483:::7.5862::... | 0.0689:::0.0695:::0.0752:::0.0738:::0.0762:::0.0792:::0.0860:::0.0915:::0.0957::... | sclera disease:::sclerosis skin:::system; sclerosis:::diffuse sclerosis:::sclero... |
| fibromyalgia                  | Disease_Syndrome_Disorder | C0016053    | fibromyalgia                  | C0016053:::C0751153:::C0751152:::C0015674:::C4703320                                | 0.0070:::3.9297:::4.7923:::6.1085:::7.4228                                          | 0.0000:::0.0242:::0.0364:::0.0572:::0.0843                                          | fibromyalgia:::secondary fibromyalgia:::fibromyalgia primary:::chronic fatigue-f... |
| sepsis                        | Disease_Syndrome_Disorder | C0036690    | sepsis                        | C0036690:::C3164780:::C0242966:::C0152965:::C1141927:::C0684256:::C1141926:::C17... | 0.0084:::4.0589:::4.4404:::4.9625:::5.2109:::5.7252:::5.8590:::5.9812:::5.9983::... | 0.0000:::0.0260:::0.0316:::0.0396:::0.0428:::0.0522:::0.0539:::0.0546:::0.0564::... | sepsis:::clinical sepsis:::syndrome sepsis:::staph sepsis:::wound sepsis:::sepsi... |
| bacterial pneumonia           | Disease_Syndrome_Disorder | C0004626    | bacterial pneumonia           | C0004626:::C0339952:::C0276523:::C0339951:::C1443238:::C0264386:::C0155860:::C05... | 0.0078:::4.8777:::6.3237:::6.3566:::6.6580:::6.8243:::6.8403:::6.8537:::6.8800::... | 0.0000:::0.0377:::0.0640:::0.0656:::0.0706:::0.0734:::0.0762:::0.0770:::0.0777::... | bacterial pneumonia:::bacterial pneumonia secondary:::aids with bacterial pneumo... |
| respiratory distress syndrome | Disease_Syndrome_Disorder | C0035220    | respiratory distress syndrome | C0035220:::C0852283:::C0035222:::C0158940:::C0877339:::C5420230:::C3810183:::C54... | 0.0062:::4.0045:::4.1765:::5.1745:::6.0413:::6.2379:::6.2459:::6.4251:::6.4578::... | 0.0000:::0.0239:::0.0259:::0.0397:::0.0535:::0.0576:::0.0574:::0.0608:::0.0607::... | respiratory distress syndrome:::respiratory distress syndromes:::acquired respir... |
| pulmonary sarcoidosis         | Disease_Syndrome_Disorder | C0036205    | pulmonary sarcoidosis         | C0036205:::C0036202:::C0406396:::C1302844:::C0396073:::C0036206:::C0340201:::C13... | 0.0074:::4.8495:::5.0965:::5.2098:::5.3056:::5.3212:::5.4128:::5.4719:::5.5281::... | 0.0000:::0.0373:::0.0412:::0.0433:::0.0452:::0.0452:::0.0470:::0.0479:::0.0488::... | pulmonary sarcoidosis:::sarcoidosis:::nodular sarcoidosis:::skin sarcoidosis:::l... |
| liver cirrhosis               | Disease_Syndrome_Disorder | C0023890    | hepatic cirrhosis             | C0023890:::C1622502:::C0238065:::C0023892:::C0085699:::C0034069:::C0023891:::C12... | 2.2160:::3.2221:::3.5682:::3.7905:::4.6751:::4.7789:::4.8481:::4.9772:::5.0601::... | 0.0072:::0.0153:::0.0188:::0.0211:::0.0322:::0.0338:::0.0349:::0.0370:::0.0377::... | hepatic cirrhosis:::liver cirrhosis portal:::obstructive liver cirrhosis:::bilia... |
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