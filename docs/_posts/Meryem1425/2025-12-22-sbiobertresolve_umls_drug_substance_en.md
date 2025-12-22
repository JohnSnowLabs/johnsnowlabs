---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes (Drug & Substance)
author: John Snow Labs
name: sbiobertresolve_umls_drug_substance
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

This model maps drug and substances to UMLS CUI codes. It is trained on ´2025AA´ release of the Unified Medical Language System (UMLS) dataset. The complete dataset has 127 different categories, and this model is trained on the “Clinical Drug”, “Pharmacologic Substance”, “Antibiotic”, and “Hazardous or Poisonous Substance” categories using ´sbiobert_base_cased_mli´ embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_drug_substance_en_6.2.2_3.4_1766390538829.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_drug_substance_en_6.2.2_3.4_1766390538829.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","posology_ner"])\
    .setOutputCol("posology_ner_chunk")\
    .setWhiteList(["DRUG"])

chunk2doc = Chunk2Doc()\
    .setInputCols("posology_ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_drug_substance","en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
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


data = spark.createDataFrame([["""She was immediately given hydrogen peroxide 30 mg to treat the infection on her leg, and has been advised Neosporin Cream for 5 days. She has a history of taking magnesium hydroxide 100mg/1ml and metformin 1000 mg."""]]).toDF("text")

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

ner_model_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","posology_ner"])\
    .setOutputCol("posology_ner_chunk")\
    .setWhiteList(["DRUG"])

chunk2doc = medical.Chunk2Doc()\
    .setInputCols("posology_ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_drug_substance","en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[
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


data = spark.createDataFrame([["""She was immediately given hydrogen peroxide 30 mg to treat the infection on her leg, and has been advised Neosporin Cream for 5 days. She has a history of taking magnesium hydroxide 100mg/1ml and metformin 1000 mg."""]]).toDF("text")

result = pipeline.fit(data).transform(data)

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

val ner_model = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")
      .setInputCols(Array("sentence", "token", "embeddings"))
      .setOutputCol("posology_ner")

val ner_model_converter = new NerConverterInternal()
      .setInputCols(Array("sentence", "token", "posology_ner"))
      .setOutputCol("posology_ner_chunk")
      .setWhiteList(Array("DRUG"))

val chunk2doc = new Chunk2Doc()
      .setInputCols("posology_ner_chunk")
      .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en","clinical/models")
      .setInputCols(Array("ner_chunk_doc"))
      .setOutputCol("sbert_embeddings")
      .setCaseSensitive(False)
    
val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_drug_substance", "en", "clinical/models")
      .setInputCols(Array("sbert_embeddings"))
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
    
val data = Seq("She was immediately given hydrogen peroxide 30 mg to treat the infection on her leg, and has been advised Neosporin Cream for 5 days. She has a history of taking magnesium hydroxide 100mg/1ml and metformin 1000 mg.").toDF("text")  

val res = p_model.fit(data).transform(data)


```
</div>

## Results

```bash


+-------------------------------+--------+------------+----------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ner_chunk                     | entity | umls_code  | resolution                 | all_k_resolutions                                                                | all_k_results                                                                    | all_k_distances                                                                  | all_k_cosine_distances                                                           |
+-------------------------------+--------+------------+----------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| hydrogen peroxide 30 mg       | DRUG   | C1126248   | hydrogen peroxide 30 mg/ml | hydrogen peroxide 30 mg/ml:::hydrogen peroxide solution 30%:::hydrogen peroxid...| C1126248:::C0304655:::C1605252:::C0304656:::C1154260:::C2242362:::C1724195:::... | 4.3731:::4.7154:::5.3302:::6.2122:::6.8675:::7.2770:::7.4682:::7.8312:::7.858... | 0.0323:::0.0369:::0.0483:::0.0649:::0.0807:::0.0890:::0.0957:::0.1018:::0.106... |
| Neosporin Cream               | DRUG   | C0132149   | neosporin cream            | neosporin cream:::neosporin ointment:::neomycin sulfate cream:::neosporin topi...| C0132149:::C0306959:::C4722788:::C0704071:::C0698988:::C1252084:::C3833898:::... | 0.0000:::6.5758:::7.0688:::7.3112:::7.3482:::7.3820:::7.4605:::7.7285:::7.891... | 0.0000:::0.0782:::0.0888:::0.0953:::0.0934:::0.0964:::0.0941:::0.1052:::0.111... |
| magnesium hydroxide 100mg/1ml | DRUG   | C1134402   | magnesium hydroxide 100 mg | magnesium hydroxide 100 mg:::magnesium hydroxide 100 mg/ml:::magnesium sulph...  | C1134402:::C1126785:::C4317023:::C4051486:::C4047137:::C1131100:::C1371187:::... | 4.9759:::5.1251:::5.8597:::6.5641:::6.5735:::6.8202:::6.8606:::6.9799:::7.007... | 0.0401:::0.0432:::0.0565:::0.0688:::0.0700:::0.0764:::0.0781:::0.0783:::0.079... |
| metformin 1000 mg             | DRUG   | C0987664   | metformin 1000 mg          | metformin 1000 mg:::metformin hydrochloride 1000 mg:::metformin hcl 1000mg ta... | C0987664:::C2719784:::C0978482:::C2719786:::C4282269:::C2719794:::C4282270:::... | 0.0000:::5.2988:::5.3783:::5.9071:::6.1034:::6.3066:::6.6597:::6.6626:::6.782... | 0.0000:::0.0445:::0.0454:::0.0553:::0.0586:::0.0632:::0.0698:::0.0707:::0.072... |
+-------------------------------+--------+------------+----------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_drug_substance|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|3.0 GB|
|Case sensitive:|false|