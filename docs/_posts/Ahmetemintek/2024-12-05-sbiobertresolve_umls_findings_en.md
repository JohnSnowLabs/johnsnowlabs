---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes
author: John Snow Labs
name: sbiobertresolve_umls_findings
date: 2024-12-05
tags: [en, entity_resolution, licensed, clinical, umls]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.5.1
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical findings to their corresponding UMLS CUI codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. It is trained on ´2024AB´ release of the Unified Medical Language System (UMLS) dataset.

## Predicted Entities

`umls cui codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_findings_en_5.5.1_3.0_1733410479994.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_findings_en_5.5.1_3.0_1733410479994.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
      .setInputCol('text')\
      .setOutputCol('document')

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", 'clinical/models') \
    .setInputCols("document") \
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
      .setInputCols("sentence")\
      .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
      .setInputCols(["sentence", "token"])\
      .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("clinical_ner")

ner_model_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "clinical_ner"])\
    .setOutputCol("ner_chunk")

chunk2doc = Chunk2Doc().setInputCols("ner_chunk").setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings\
     .pretrained("sbiobert_base_cased_mli",'en','clinical/models')\
     .setInputCols(["ner_chunk_doc"])\
     .setOutputCol("sbert_embeddings")

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_findings","en", "clinical/models") \
     .setInputCols(["sbert_embeddings"]) \
     .setOutputCol("resolution")\
     .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages = [document_assembler, sentence_detector, tokenizer, word_embeddings, ner_model, ner_model_converter, chunk2doc, sbert_embedder, resolver])

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with an acute hepatitis, and obesity with a BMI of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting."""]]).toDF("text")

results = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val sentence_detector = new SentenceDetectorDLModel
      .pretrained("sentence_detector_dl_healthcare", "en", 'clinical/models') \
      .setInputCols("document") \
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

val ner_model_converter = new NerConverterInternal()
      .setInputCols(Array("sentence", "token", "clinical_ner"))
      .setOutputCol("ner_chunk")

val chunk2doc = Chunk2Doc().setInputCols("ner_chunk").setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
      .pretrained("sbiobert_base_cased_mli", "en","clinical/models")
      .setInputCols(Array("ner_chunk_doc"))
      .setOutputCol("sbert_embeddings")
    
val resolver = SentenceEntityResolverModel
      .pretrained("sbiobertresolve_umls_findings", "en", "clinical/models")
      .setInputCols(Array("ner_chunk_doc", "sbert_embeddings"))
      .setOutputCol("resolution")
      .setDistanceFunction("EUCLIDEAN")

val p_model = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, ner_model, ner_model_converter, chunk2doc, sbert_embedder, resolver))
    
val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with an acute hepatitis, and obesity with a BMI of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting.").toDF("text")  

val res = p_model.fit(data).transform(data)
```
</div>

## Results

```bash
|    | ner_chunk                             | entity   | umls_code   | resolution                                 | all_k_results                                          | all_k_distances                              | all_k_cosine_distances                       | all_k_resolutions                                                                                                       |
|---:|:--------------------------------------|:---------|:------------|:-------------------------------------------|:-------------------------------------------------------|:---------------------------------------------|:---------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
|  0 | gestational diabetes mellitus         | PROBLEM  | C3532257    | uncontrolled gestational diabetes mellitus | C3532257:::C2183115:::C3161145:::C4303558:::C3840222:::| 4.9175:::5.2200:::6.3563:::7.1692:::7.214... | 0.0358:::0.0401:::0.0596:::0.0750:::0.0773...| uncontrolled gestational diabetes mellitus:::diabetes mellitus during pregnancy:::hx gestational diabetes:::maternal ...|
|  1 | subsequent type two diabetes mellitus | PROBLEM  | C4016960    | type 2 diabetes mellitus, association with | C4016960:::C3532488:::C4016735:::C4014362:::C5195213...| 5.5572:::6.4306:::6.9971:::7.0924:::7.3414...| 0.0464:::0.0622:::0.0751:::0.0763:::0.0828...| type 2 diabetes mellitus, association with:::history of diabetes mellitus type 2 (situation):::type 2 diabetes melli... |
|  2 | HTG-induced pancreatitis              | PROBLEM  | C3808945    | secondary pancreatitis                     | C3808945:::C1835382:::C1556678:::C1556677:::C1963198...| 7.5300:::7.6941:::8.3460:::8.5169:::8.5591...| 0.0925:::0.0962:::0.1175:::0.1208:::0.1227...| secondary pancreatitis:::pancreatitis, acute in some:::grade 2 pancreatitis, ctcae:::grade 1 pancreatitis, ctcae:::p... |
|  3 | an acute hepatitis                    | PROBLEM  | C4750596    | acute infectious hepatitis suspected       | C4750596:::C5233349:::C0151325:::C1861901:::C5232888...| 5.2956:::7.9441:::8.4300:::8.5172:::9.1431...| 0.0426:::0.0970:::0.1089:::0.1110:::0.1285...| acute infectious hepatitis suspected:::abnormal liver enzymes during acute episode:::infectious hepatitis present:::... |
|  4 | obesity                               | PROBLEM  | C4759928    | obesity                                    | C4759928:::C0311277:::C1556381:::C4016383:::C0426650...| 0.0000:::3.8693:::4.8495:::5.1270:::5.1356...| 0.0000:::0.0218:::0.0345:::0.0394:::0.0383...| obesity:::abdominal obesity:::extreme obesity:::obesity, association with:::obese abdomen:::h/o: obesity:::trunk obe... |
|  5 | a body mass index                     | PROBLEM  | C2240399    | body mass index                            | C2240399:::C0578022:::C4718566:::C2724372:::C0518010...| 5.2691:::5.2779:::6.6425:::6.6482:::7.1232...| 0.0407:::0.0409:::0.0654:::0.0647:::0.0746...| body mass index:::finding of body mass index:::monitors body mass index:::body mass index documented:::body mass:::m... |
|  5 | a BMI                                 | TEST     | C0578022    | bmi                                        | C0578022:::C1862288:::C0684262:::C3888192:::C1833829...| 4.2306:::5.8985:::5.9223:::5.9630:::6.3525...| 0.0278:::0.0534:::0.0545:::0.0558:::0.0638...| bmi:::bas:::bac:::bmnd:::bmyc:::b neg:::bmiq2:::bcll:::buln:::bl:::b/b:::bo:::bao:::bls-aemt:::a & b:::b pos:::be/b0:::b|
|  7 | polyuria                              | PROBLEM  | C5855036    | urinary frequency / polyuria               | C5855036:::C1865279:::C3670443:::C0042023:::C1735369...| 7.5569:::8.1070:::8.4710:::8.8332:::9.1023...| 0.0880:::0.1030:::0.1110:::0.1237:::0.1292...| urinary frequency / polyuria:::foetal polyuria:::polyuria and polydipsia:::pollakiuria:::chronic hematuria:::protein... |
|  8 | polydipsia                            | PROBLEM  | C3670443    | polyuria and polydipsia                    | C3670443:::C0220854:::C0020505:::C0585348:::C0422980...| 8.3037:::9.5939:::10.0704:::10.1917:::10.2...| 0.1057:::0.1381:::0.1573:::0.1641:::0.1675...| polyuria and polydipsia:::polypnea:::polyphagia:::biphasic stridor:::oscillopsia:::polyhydramnios was observed:::mar... |
|  9 | poor appetite                         | PROBLEM  | C5543391    | low appetite                               | C5543391:::C1971624:::C0541799:::C0576456:::C2077391...| 5.4947:::5.7668:::6.1978:::6.4132:::6.6587...| 0.0442:::0.0482:::0.0559:::0.0603:::0.0644...| low appetite:::lack of appetite:::bad taste:::poor feeding:::insufficient nutrition:::poor eater:::inadequate nutrit... |
| 10 | vomiting                              | PROBLEM  | C1287105    | vomit ph                                   | C1287105:::C4015188:::C4324485:::C0439039:::C0577080...| 5.1470:::5.8703:::6.1762:::6.1814:::6.2403...| 0.0398:::0.0514:::0.0579:::0.0571:::0.0589...| vomit ph:::cyclic vomiting:::discolored vomit:::c/o - vomiting:::finding of vomit:::vomit volume:::vomiting crises::... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_findings|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|2.3 GB|
|Case sensitive:|false|

## References

Trained on concepts from clinical findings for the 2024AB release of the Unified Medical Language System® (UMLS) Knowledge Sources: https://www.nlm.nih.gov/research/umls/index.html