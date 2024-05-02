---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes (Drug & Substance)
author: John Snow Labs
name: sbiobertresolve_umls_drug_substance
date: 2024-05-02
tags: [en, licensed, entity_resolution, umls]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps drug and substances to UMLS CUI codes. It is trained on 2023AB release of the Unified Medical Language System (UMLS) dataset. The complete dataset has 127 different categories, and this model is trained on the ´Clinical Drug´, ´Pharmacologic Substance´, ´Antibiotic´, and ´Hazardous or Poisonous Substance´ categories using ´sbiobert_base_cased_mli´ embeddings.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_drug_substance_en_5.3.1_3.4_1714651767841.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_drug_substance_en_5.3.1_3.4_1714651767841.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli",'en','clinical/models')\
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


data = spark.createDataFrame([["""A 35-year-old female with a past medical history significant for rheumatoid arthritis diagnosed 10 years ago, currently managed with methotrexate and prednisone, presented with a three-week history of progressively worsening joint pain and swelling, predominantly involving the wrists, knees, and ankles. She reported morning stiffness lasting over an hour. The patient denied any recent infections to the affected joints."""]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val sentence_detector = new SentenceDetector()
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
      .setWhiteList(["DRUG"])

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
    
val data = Seq("A 35-year-old female with a past medical history significant for rheumatoid arthritis diagnosed 10 years ago, currently managed with methotrexate and prednisone, presented with a three-week history of progressively worsening joint pain and swelling, predominantly involving the wrists, knees, and ankles. She reported morning stiffness lasting over an hour. The patient denied any recent infections to the affected joints.").toDF("text")  

val res = p_model.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------------+-----+---+------+---------+--------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                    ner_chunk|begin|end|entity|umls_code|             resolved_text|                                               all_k_results|                                           all_k_resolutions|
+-----------------------------+-----+---+------+---------+--------------------------+------------------------------------------------------------+------------------------------------------------------------+
|      hydrogen peroxide 30 mg|   26| 48|  DRUG| C1126248|hydrogen peroxide 30 mg/ml|C1126248:::C0304655:::C1605252:::C0304656:::C1154260:::C2...|hydrogen peroxide 30 mg/ml:::hydrogen peroxide solution 3...|
|              Neosporin Cream|  107|121|  DRUG| C0132149|           neosporin cream|C0132149:::C0358174:::C0357999:::C0307085:::C0698810:::C0...|neosporin cream:::nystan cream:::nystadermal cream:::nupe...|
|magnesium hydroxide 100mg/1ml|  163|191|  DRUG| C1134402|magnesium hydroxide 100 mg|C1134402:::C1126785:::C4317023:::C4051486:::C4047137:::C1...|magnesium hydroxide 100 mg:::magnesium hydroxide 100 mg/m...|
|            metformin 1000 mg|  197|213|  DRUG| C0987664|         metformin 1000 mg|C0987664:::C2719784:::C0978482:::C2719786:::C4282269:::C2...|metformin 1000 mg:::metformin hydrochloride 1000 mg:::met...|
+-----------------------------+-----+---+------+---------+--------------------------+------------------------------------------------------------+------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_drug_substance|
|Compatibility:|Healthcare NLP 5.3.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|2.9 GB|
|Case sensitive:|false|

## References

Trained on ´2021AB´ UMLS dataset’s ´Clinical Drug´, ´Pharmacologic Substance´, ´Antibiotic´, ´Hazardous or Poisonous Substance´ categories. Knowledge Sources: https://www.nlm.nih.gov/research/umls/index.html
