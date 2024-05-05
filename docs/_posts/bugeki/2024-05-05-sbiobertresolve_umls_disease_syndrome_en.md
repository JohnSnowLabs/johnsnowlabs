---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes (Disease or Syndrome)
author: John Snow Labs
name: sbiobertresolve_umls_disease_syndrome
date: 2024-05-05
tags: [en, licensed, entity_resolution, umls]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.2
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities to UMLS CUI codes. It is trained on ´2021AB´ UMLS dataset. The complete dataset has 127 different categories, and this model is trained on the ´Disease or Syndrome´ category using ´sbiobert_base_cased_mli´ embeddings.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_disease_syndrome_en_5.3.2_3.0_1714942230477.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_disease_syndrome_en_5.3.2_3.0_1714942230477.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setWhiteList(['Disease_Syndrome_Disorder','Symptom'])\

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli",'en','clinical/models')\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(false)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_disease_syndrome, en, clinical/models") \
    .setInputCols(["ner_chunk","sbert_embeddings"]) \
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

data = spark.createDataFrame([["""A 35-year-old female with a past medical history significant for rheumatoid arthritis diagnosed 10 years ago, currently managed with methotrexate and prednisone, presented with a three-week history of progressively worsening joint pain and swelling, predominantly involving the wrists, knees, and ankles. She reported morning stiffness lasting over an hour. The patient denied any recent infections to the affected joints."""]]).toDF("text")

result = umls_lp.fit(data).transform(data)
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

val ner_model = MedicalNerModel
      .pretrained("ner_jsl", "en", "clinical/models")
      .setInputCols(Array("sentence", "token", "embeddings"))
      .setOutputCol("ner_jsl")

val ner_model_converter = new NerConverterInternal()
      .setInputCols(Array("sentence", "token", "ner_jsl"))
      .setOutputCol("ner_chunk")
      .setWhiteList(["Disease_Syndrome_Disorder","Symptom"])

val chunk2doc = new Chunk2Doc()
      .setInputCols("ner_chunk")
      .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
      .pretrained("sbiobert_base_cased_mli", "en","clinical/models")
      .setInputCols(Array("ner_chunk_doc"))
      .setOutputCol("sbert_embeddings")
      .setCaseSensitive(False)
    
val resolver = SentenceEntityResolverModel
      .pretrained("sbiobertresolve_umls_disease_syndrome", "en", "clinical/models")
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
    
val data = Seq("A 35-year-old female with a past medical history significant for rheumatoid arthritis diagnosed 10 years ago, currently managed with methotrexate and prednisone, presented with a three-week history of progressively worsening joint pain and swelling, predominantly involving the wrists, knees, and ankles. She reported morning stiffness lasting over an hour. The patient denied any recent infections to the affected joints.").toDF("text")  

val res = p_model.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------------+-----+---+-------------------------+---------+--------------------+------------------------------------------------------------+------------------------------------------------------------+
|           ner_chunk|begin|end|                   entity|umls_code|       resolved_text|                                               all_k_results|                                           all_k_resolutions|
+--------------------+-----+---+-------------------------+---------+--------------------+------------------------------------------------------------+------------------------------------------------------------+
|rheumatoid arthritis|   65| 84|Disease_Syndrome_Disorder| C0003873|rheumatoid arthritis|C0003873:::C0857204:::C0035436:::C3842272:::C0241786:::C0...|rheumatoid arthritis:::rheumatoid arthropathy:::rheumatic...|
|          joint pain|  225|234|                  Symptom| C0162296| multiple joint pain|C0162296:::C0748680:::C0423690:::C0553642:::C5700083:::C0...|multiple joint pain:::shoulder pain exertional:::facet jo...|
|            swelling|  240|247|                  Symptom| C1411141|  wandering swelling|C1411141:::C0037580:::C0281913:::C2938877:::C0497156:::C0...|wandering swelling:::soft tissue swelling:::muscles swell...|
|           stiffness|  326|334|                  Symptom| C1410087|    stiffness; spine|C1410087:::C0014481:::C1861404:::C0277460:::C5554232:::C0...|stiffness; spine:::stiff sickness:::thumbs, stiff:::scaly...|
|          infections|  388|397|Disease_Syndrome_Disorder| C0851162|          infections|C0851162:::C0578491:::C0009450:::C0747002:::C0858744:::C0...|infections:::infections site:::infection:::infections op:...|
|     affected joints|  406|420|                  Symptom| C0022408|   joint dysfunction|C0022408:::C0409271:::C5191746:::C0231586:::C4280547:::C0...|joint dysfunction:::derangement of multiple joints:::diso...|
+--------------------+-----+---+-------------------------+---------+--------------------+------------------------------------------------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_disease_syndrome|
|Compatibility:|Healthcare NLP 5.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|1.3 GB|
|Case sensitive:|false|