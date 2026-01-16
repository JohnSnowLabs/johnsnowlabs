---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes (Disease or Syndrome)
author: John Snow Labs
name: sbiobertresolve_umls_disease_syndrome
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

This model maps clinical entities to UMLS CUI codes. The complete dataset has 127 different categories, and this model is trained on the “Disease or Syndrome” category using ´sbiobert_base_cased_mli´ embeddings.

## Predicted Entities

`UMLS CUI codes for Disease or Syndrome`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_disease_syndrome_en_6.2.2_3.4_1766388075704.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_disease_syndrome_en_6.2.2_3.4_1766388075704.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setWhiteList(["Disease_Syndrome_Disorder","Symptom"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_disease_syndrome", "en", "clinical/models") \
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
    .setWhiteList(["Disease_Syndrome_Disorder","Symptom"])

chunk2doc = medical.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_disease_syndrome", "en", "clinical/models") \
    .setInputCols(["ner_chunk","sbert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

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

data = spark.createDataFrame([["""A 35-year-old female with a past medical history significant for rheumatoid arthritis diagnosed 10 years ago, currently managed with methotrexate and prednisone, presented with a three-week history of progressively worsening joint pain and swelling, predominantly involving the wrists, knees, and ankles. She reported morning stiffness lasting over an hour. The patient denied any recent infections to the affected joints."""]]).toDF("text")

result = umls_lp.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val  sentence_detector = SentenceDetectorDLModel
      .pretrained("sentence_detector_dl_healthcare","en","clinical/models")
      .setInputCols(Array("document"))
      .setOutputCol("sentence")

val tokenizer = new Tokenizer()
      .setInputCols(Array("sentence"))
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
      .setWhiteList(Array("Disease_Syndrome_Disorder","Symptom"))

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


+----------------------+---------------------------+------------+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ner_chunk            | entity                    | umls_code  | resolution            | all_k_resolutions                                                                 | all_k_results                                                                    | all_k_distances                                                                  | all_k_cosine_distances                                                           |
+----------------------+---------------------------+------------+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| rheumatoid arthritis | Disease_Syndrome_Disorder | C0003873   | rheumatoid arthritis  | rheumatoid arthritis:::rheumatoid arthropathy:::rheumatic arthritis:::rheumato... | C0003873:::C0857204:::C0035436:::C3842272:::C0241786:::C0409651:::C0852006:::... | 0.0000:::2.6543:::3.0397:::3.7683:::3.8342:::3.9105:::4.1216:::4.1865:::4.211... | 0.0000:::0.0104:::0.0138:::0.0213:::0.0221:::0.0229:::0.0255:::0.0261:::0.026... |
| joint pain           | Symptom                   | C0162296   | multiple joint pain   | multiple joint pain:::shoulder pain exertional:::facet joint pain:::myofascial... | C0162296:::C0748680:::C0423690:::C0553642:::C5700083:::C0013390:::C0745574:::... | 3.4499:::5.1713:::5.2817:::5.5698:::5.7625:::5.9209:::5.9710:::5.9961:::6.079... | 0.0172:::0.0387:::0.0406:::0.0448:::0.0481:::0.0509:::0.0518:::0.0519:::0.053... |
| swelling             | Symptom                   | C1411141   | wandering swelling    | wandering swelling:::soft tissue swelling:::muscles swelling:::limbal swelling... | C1411141:::C0037580:::C0281913:::C2938877:::C0497156:::C0859055:::C0241822:::... | 6.0648:::6.7036:::7.2996:::7.7305:::8.1316:::8.1945:::8.4125:::8.4801:::8.640... | 0.0556:::0.0665:::0.0784:::0.0893:::0.0991:::0.1015:::0.1080:::0.1076:::0.110... |
| stiffness            | Symptom                   | C1410087   | stiffness; spine      | stiffness; spine:::stiff sickness:::thumbs, stiff:::scaly leg:::stiff lung:::s... | C1410087:::C0014481:::C1861404:::C0277460:::C5554232:::C0085292:::C0158199:::... | 7.7399:::8.8853:::8.9370:::9.0310:::9.0316:::9.1911:::9.3530:::9.3598:::9.635... | 0.0937:::0.1219:::0.1217:::0.1238:::0.1256:::0.1304:::0.1394:::0.1350:::0.139... |
| infections           | Disease_Syndrome_Disorder | C0851162   | infections            | infections:::infections site:::infection:::infections op:::induced infections:... | C0851162:::C0578491:::C0009450:::C0747002:::C0858744:::C0749769:::C0442886:::... | 0.0000:::5.3371:::5.3800:::5.3940:::5.7704:::6.1681:::7.1752:::7.4329:::7.471... | 0.0000:::0.0453:::0.0461:::0.0463:::0.0522:::0.0591:::0.0804:::0.0888:::0.087... |
| affected joints      | Symptom                   | C0022408   | joint dysfunction     | joint dysfunction:::derangement of multiple joints:::disorder of joint region:... | C0022408:::C0409271:::C5191746:::C0231586:::C4280547:::C0702154:::C0003864:::... | 6.8566:::7.4435:::7.5452:::7.6765:::7.9062:::8.1095:::8.2893:::8.4961:::8.519... | 0.0689:::0.0824:::0.0844:::0.0851:::0.0937:::0.0972:::0.1032:::0.1051:::0.107... |
+----------------------+---------------------------+------------+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_disease_syndrome|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|1.3 GB|
|Case sensitive:|false|

## References

Trained on ´2025AB´ UMLS dataset’s ´Disease or Syndrome´ category. https://www.nlm.nih.gov/research/umls/index.html
