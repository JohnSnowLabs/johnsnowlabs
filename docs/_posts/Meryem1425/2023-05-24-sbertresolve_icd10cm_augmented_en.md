---
layout: model
title: Sentence Entity Resolver for ICD10-CM (Augmented)
author: John Snow Labs
name: sbertresolve_icd10cm_augmented
date: 2023-05-24
tags: [en, clinical, licensed, icd10cm, entity_resolution]
task: Entity Resolution
language: en
edition: Healthcare NLP 4.4.2
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted medical entities to ICD10-CM codes using `sbert_jsl_medium_uncased`. Also, it has been augmented with synonyms for making it more accurate.

## Predicted Entities

`ICD10CM Codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbertresolve_icd10cm_augmented_en_4.4.2_3.0_1684961214137.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbertresolve_icd10cm_augmented_en_4.4.2_3.0_1684961214137.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverter()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(['PROBLEM'])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

bert_embeddings = BertSentenceEmbeddings.pretrained("sbert_jsl_medium_uncased", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bert_embeddings")\
    .setCaseSensitive(False)

icd10_resolver = SentenceEntityResolverModel.pretrained("sbertresolve_icd10cm_augmented", "en", "clinical/models") \
    .setInputCols(["bert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

nlpPipeline = Pipeline(stages=[document_assembler, 
                               sentence_detector, 
                               tokenizer, 
                               word_embeddings, 
                               clinical_ner, 
                               ner_converter, 
                               chunk2doc, 
                               bert_embeddings, 
                               icd10_resolver])

data_ner = spark.createDataFrame([["A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis, and obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."]]).toDF("text")

results = nlpPipeline.fit(data_ner).transform(data_ner)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList("PROBLEM")

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val bert_embeddings = BertSentenceEmbeddings.pretrained("sbert_jsl_medium_uncased", "en", "clinical/models")
    .setInputCols("ner_chunk_doc")
    .setOutputCol("bert_embeddings")
    .setCaseSensitive(False)

val icd10_resolver = SentenceEntityResolverModel.pretrained("sbertresolve_icd10cm_augmented", "en", "clinical/models")
    .setInputCols("bert_embeddings")
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, clinical_ner, ner_converter, chunk2doc, sbert_embedder, icd10_resolver))

val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis, and obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection.").toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
| ner_chunk                             | entity   | icd10_code   | all_codes                                                                           | resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:--------------------------------------|:---------|:-------------|:------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| gestational diabetes mellitus         | PROBLEM  | O24.4        | O24.4:::O24.41:::O24.43:::Z86.32:::K86.8:::P70.2:::O24.434:::E10.9                  | gestational diabetes mellitus:::gestational diabetes mellitus:::gestational diabetes mellitus in the puerperium:::history of gestational diabetes mellitus:::secondary pancreatic diabetes mellitus:::neonatal diabetes mellitus:::gestational diabetes mellitus in the puerperium, insulin controlled:::juvenile onset diabetes mellitus                                                                                                                            |
| subsequent type two diabetes mellitus | PROBLEM  | E11          | E11:::E11.9:::E10.9:::E10:::E13.9:::Z83.3:::L83:::E11.8:::E11.32:::E10.8:::Z86.39   | type 2 diabetes mellitus:::type ii diabetes mellitus:::type i diabetes mellitus:::type 1 diabetes mellitus:::secondary diabetes mellitus:::fh: diabetes mellitus:::type 2 diabetes mellitus with acanthosis nigricans:::complication of type ii diabetes mellitus:::secondary endocrine diabetes mellitus:::complication of type i diabetes mellitus:::history of diabetes mellitus type ii:::pregnancy and type 2 diabetes mellitus                                 |
| HTG-induced pancreatitis              | PROBLEM  | M79.3        | M79.3:::F10.2:::K85.3:::T46.5X:::K85.20:::K85.32:::T50.90:::A39.8:::J98.5           | drug-induced panniculitis:::drug-induced chronic pancreatitis:::drug-induced acute pancreatitis:::drug-induced pericarditis:::alcohol-induced pancreatitis:::drug induced acute pancreatitis with infected necrosis:::drug-induced dermatomyositis:::rbn - retrobulbar neuritis:::drug-induced granulomatous mediastinitis                                                                                                                                           |
| acute hepatitis                       | PROBLEM  | K72.0        | K72.0:::B15:::B17.2:::B17.10:::B17.1:::B16:::B17.9:::B18.8                          | acute hepatitis:::acute hepatitis a:::acute hepatitis e:::acute hepatitis c:::acute hepatitis c:::acute hepatitis b:::acute viral hepatitis:::chronic hepatitis e                                                                                                                                                                                                                                                                                                    |
| obesity                               | PROBLEM  | E66.9        | E66.9:::E66.8:::P90:::Q13.0:::M79.4:::Z86.39                                        | obesity:::upper body obesity:::childhood obesity:::central obesity:::localised obesity:::history of obesity                                                                                                                                                                                                                                                                                                                                                          |
| a body mass index                     | PROBLEM  | E66.9        | E66.9:::Z68.41:::Z68:::E66.8:::Z68.45:::Z68.4:::Z68.1:::Z68.2                       | observation of body mass index:::finding of body mass index:::body mass index [bmi]:::body mass index equal to or greater than 40:::body mass index [bmi] 70 or greater, adult:::body mass index [bmi] 40 or greater, adult:::body mass index [bmi] 19.9 or less, adult:::body mass index [bmi] 20-29, adult                                                                                                                                                         |
| polyuria                              | PROBLEM  | R35          | R35:::E88.8:::R30.0:::N28.89:::O04.8:::R82.4:::E74.8:::R82.2                        | polyuria:::sialuria:::stranguria:::isosthenuria:::oliguria:::ketonuria:::xylosuria:::biliuria                                                                                                                                                                                                                                                                                                                                                                        |
| polydipsia                            | PROBLEM  | R63.1        | R63.1:::Q17.0:::Q89.4:::Q89.09:::Q74.8:::H53.8:::H53.2:::Q13.2                      | polydipsia:::polyotia:::polysomia:::polysplenia:::polymelia:::palinopsia:::polyopia:::polycoria                                                                                                                                                                                                                                                                                                                                                                      |
| poor appetite                         | PROBLEM  | R63.0        | R63.0:::R63.2:::P92.9:::R45.81:::Z55.8:::R41.84:::R41.3:::Z74.8                     | poor appetite:::excessive appetite:::poor feeding:::poor self-esteem:::poor education:::poor concentration:::poor memory:::poor informal care arrangements (finding)                                                                                                                                                                                                                                                                                                 |
| vomiting                              | PROBLEM  | R11.1        | R11.1:::K91.0:::K92.0:::A08.39:::R11:::P92.0:::P92.09:::R11.12                      | vomiting:::vomiting bile:::vomiting blood:::viral vomiting:::vomiting (disorder):::vomiting of newborn:::vomiting in newborn (disorder):::projectile vomiting                                                                                                                                                                                                                                                                                                        |
| a respiratory tract infection         | PROBLEM  | J98.8        | J98.8:::J06.9:::P39.3:::J22:::N39.0:::A49.9:::Z59.3:::T83.51                        | respiratory tract infection:::upper respiratory tract infection:::urinary tract infection:::lrti - lower respiratory tract infection:::uti - urinary tract infection:::bacterial respiratory infection:::institution-acquired respiratory infection:::catheter-associated urinary tract infection                                                                                                                                                                    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbertresolve_icd10cm_augmented|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|1.0 GB|
|Case sensitive:|false|