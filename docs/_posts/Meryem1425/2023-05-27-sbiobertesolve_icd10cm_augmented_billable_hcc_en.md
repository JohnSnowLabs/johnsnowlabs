---
layout: model
title: Sentence Entity Resolver for Billable ICD10-CM HCC Codes
author: John Snow Labs
name: sbiobertesolve_icd10cm_augmented_billable_hcc
date: 2023-05-27
tags: [licensed, en, hcc, icd10cm, entity_resolution]
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

This model maps extracted medical entities to ICD-10-CM codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings and it supports with HCC status. It has been updated by dropping the invalid codes that exist in the previous versions. In the result, look for the `all_k_aux_labels` parameter in the metadata to get HCC status. The HCC status can be divided to get further information: `billable status`, `hcc status`, and `hcc score`.

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_ICD10_CM/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertesolve_icd10cm_augmented_billable_hcc_en_4.4.2_3.0_1685174316346.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertesolve_icd10cm_augmented_billable_hcc_en_4.4.2_3.0_1685174316346.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")

icd10_resolver = SentenceEntityResolverModel.pretrained("sbiobertesolve_icd10cm_augmented_billable_hcc","en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

nlpPipeline = Pipeline(stages=[document_assembler, 
                               sentence_detector, 
                               tokenizer, 
                               word_embeddings, 
                               clinical_ner, 
                               ner_converter, 
                               chunk2doc, 
                               sbert_embedder, 
                               icd10_resolver])

data = spark.createDataFrame([["A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis, and obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."]]).toDF("text")

results = nlpPipeline.fit(data).transform(data)
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

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols("ner_chunk_doc")
    .setOutputCol("sbert_embeddings")

val icd10_resolver = SentenceEntityResolverModel.pretrained("sbiobertesolve_icd10cm_augmented_billable_hcc","en", "clinical/models")
    .setInputCols("sbert_embeddings") 
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(document_assembler, 
                               sentence_detector, 
                               tokenizer, 
                               word_embeddings, 
                               clinical_ner, 
                               ner_converter, 
                               chunk2doc, 
                               sbert_embedder, 
                               icd10_resolver))

val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis, and obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection.").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
| ner_chunk                             | entity   | icd10_code   | all_codes                                                                                   | resolutions                                                                                                                                                                                                                                                                                                                                                     | hcc_list                                                                                                                                                                                                                                   |
|:--------------------------------------|:---------|:-------------|:--------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| gestational diabetes mellitus         | PROBLEM  | O24.41       | O24.41:::O24.4:::O24.43:::Z86.32:::Z87.5:::O24.31:::O24.11:::O24.1:::O24.81                 | gestational diabetes mellitus [gestational diabetes mellitus]:::gestational diabetes mellitus [gestational diabetes mellitus]:::postpartum gestational diabetes mellitus [postpartum gestational diabetes mellitus]:::history of gestational diabetes mellitus [history of gestational diabetes mellitus]...                                                    | 0||0||0:::0||0||0:::0||0||0:::1||0||0:::0||0||0:::0||0||0:::0||0||0:::0||0||0:::0||0||0                                                                                                                                                    |
| subsequent type two diabetes mellitus | PROBLEM  | O24.11       | O24.11:::E11.8:::E11:::E13.9:::E11.9:::E11.3:::E11.44:::Z86.3:::Z86.39:::E11.32...          | pre-existing type 2 diabetes mellitus [pre-existing type 2 diabetes mellitus]:::disorder associated with type 2 diabetes mellitus [disorder associated with type 2 diabetes mellitus]:::type 2 diabetes mellitus [type 2 diabetes mellitus]:::secondary diabetes mellitus [secondary diabetes mellitus]...                                                      | 0||0||0:::1||1||18:::0||0||0:::1||1||19:::1||1||19:::0||0||0:::1||1||18:::0||0||0:::1||0||0:::0||0||0:::1||1||18:::0||0||0                                                                                                                 |
| T2DM                                  | PROBLEM  | E11          | E11:::E11.8:::E11.9:::O24.11:::E10.9:::E13.9:::E11.3:::E88.81:::Z83.3:::D64.9...            | type 2 diabetes mellitus [type 2 diabetes mellitus]:::disorder associated with type 2 diabetes mellitus [disorder associated with type 2 diabetes mellitus]:::diabetes mellitus type 2 [diabetes mellitus type 2]:::pre-existing type 2 diabetes mellitus [pre-existing type 2 diabetes mellitus]...                                                            | 0||0||0:::1||1||18:::1||1||19:::0||0||0:::1||1||19:::1||1||19:::0||0||0:::1||0||0:::1||0||:::1||0||0:::0||0||0:::0||0||0:::1||1||19                                                                                                        |
| HTG-induced pancreatitis              | PROBLEM  | K85.20       | K85.20:::K85.3:::K85.90:::F10.2:::K86.0:::K85.2:::K85.9:::K85.80:::K85.91...                | alcohol-induced pancreatitis [alcohol-induced pancreatitis]:::drug-induced acute pancreatitis [drug-induced acute pancreatitis]:::hemorrhagic pancreatitis [hemorrhagic pancreatitis]:::alcohol-induced chronic pancreatitis [alcohol-induced chronic pancreatitis]:::alcohol-induced chronic pancreatitis [alcohol-induced chronic pancreatitis]...            | 1||0||0:::0||0||0:::1||0||0:::0||0||0:::1||1||34:::0||0||0:::0||0||0:::1||0||0:::1||0||0:::0||0||0:::0||0||0:::0||0||0:::1||0||0                                                                                                           |
| acute hepatitis                       | PROBLEM  | K72.0        | K72.0:::B15:::B17.9:::B17.2:::Z03.89:::B15.9:::B15.0:::B16:::K75.2:::K71.2:::B19.9          | acute hepatitis [acute hepatitis]:::acute hepatitis a [acute hepatitis a]:::acute infectious hepatitis [acute infectious hepatitis]:::acute hepatitis e [acute hepatitis e]:::acute infectious hepatitis suspected [acute infectious hepatitis suspected]:::acute type a viral hepatitis [acute type a viral hepatitis]...                                      | 0||0||0:::0||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::0||0||0:::1||0||0:::1||0||0:::1||0||0                                                                                                                                |
| obesity                               | PROBLEM  | E66.9        | E66.9:::E66.8:::Z68.41:::Q13.0:::E66:::E66.01:::Z86.39:::E34.9:::H35.50...                  | obesity [obesity]:::abdominal obesity [abdominal obesity]:::obese [obese]:::central obesity [central obesity]:::overweight and obesity [overweight and obesity]:::morbid obesity [morbid obesity]:::h/o: obesity [h/o: obesity]:::severe obesity [severe obesity]:::centripetal obesity [centripetal obesity]...                                                | 1||0||0:::1||0||0:::1||1||22:::1||0||0:::0||0||0:::1||1||22:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0                                                                                                                    |
| a body mass index                     | PROBLEM  | Z68.41       | Z68.41:::E66.9:::R22.9:::Z68.1:::R22.3:::R22.1:::Z68:::R22.2:::R22.0...                     | finding of body mass index [finding of body mass index]:::observation of body mass index [observation of body mass index]:::mass of body region [mass of body region]:::finding of body mass index (finding) [finding of body mass index (finding)]:::mass of upper limb [mass of upper limb]...                                                                | 1||1||22:::1||0||0:::1||0||0:::1||0||0:::0||0||0:::1||0||0:::0||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::0||0||0:::1||0||0                                                                   |
| polyuria                              | PROBLEM  | R35          | R35:::R35.81:::R35.8:::E23.2:::R35.89:::R31:::R35.0:::R82.99:::N40.1:::E72.3:::O04.8...     | polyuria [polyuria]:::nocturnal polyuria [nocturnal polyuria]:::polyuric state [polyuric state]:::polyuric state (disorder) [polyuric state (disorder)]:::other polyuria [other polyuria]:::hematuria [hematuria]:::micturition frequency and polyuria [micturition frequency and polyuria]...                                                                  | 0||0||0:::1||0||0:::0||0||0:::1||1||23:::1||0||0:::0||0||0:::1||0||0:::0||0||0:::1||0||0:::1||1||23:::0||0||0:::1||0||0:::1||0||0:::1||1||23:::1||0||0:::0||0||0:::1||0||0:::1||0||0:::1||0||0:::0||0||0:::1||0||0                         |
| polydipsia                            | PROBLEM  | R63.1        | R63.1:::F63.89:::E23.2:::F63.9:::O40:::G47.5:::M79.89:::R63.2:::R06.1:::H53.8...            | polydipsia [polydipsia]:::psychogenic polydipsia [psychogenic polydipsia]:::primary polydipsia [primary polydipsia]:::psychogenic polydipsia (disorder) [psychogenic polydipsia (disorder)]:::polyhydramnios [polyhydramnios]:::parasomnia [parasomnia]:::polyalgia [polyalgia]:::polyphagia [polyphagia]...                                                    | 1||0||0:::1||0||0:::1||1||23:::1||0||0:::0||0||0:::0||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||1||96:::1||0||0:::1||0||0:::0||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::0||0||0:::1||1||40                         |
| poor appetite                         | PROBLEM  | R63.0        | R63.0:::P92.9:::R43.8:::R43.2:::E86:::R19.6:::F52.0:::Z72.4:::R06.89:::Z76.89:::R53.1...    | poor appetite [poor appetite]:::poor feeding [poor feeding]:::bad taste in mouth [bad taste in mouth]:::unpleasant taste in mouth [unpleasant taste in mouth]:::poor fluid intake [poor fluid intake]:::bad breath [bad breath]:::low libido [low libido]:::diet poor (finding) [diet poor (finding)]...                                                        | 1||0||0:::1||0||0:::1||0||0:::1||0||0:::0||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::0||0||0:::0||0||0:::1||0||0:::1||0||0                                                                                        |
| vomiting                              | PROBLEM  | R11.1        | R11.1:::R11:::R11.10:::G43.A1:::P92.1:::P92.09:::G43.A:::R11.13:::R11.0                     | vomiting [vomiting]:::intermittent vomiting [intermittent vomiting]:::vomiting symptoms [vomiting symptoms]:::periodic vomiting [periodic vomiting]:::finding of vomiting [finding of vomiting]:::c/o - vomiting [c/o - vomiting]:::cyclical vomiting [cyclical vomiting]:::faeculent vomit o/e [faeculent vomit o/e]...                                        | 0||0||0:::0||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::0||0||0:::1||0||0:::1||0||0                                                                                                                                                    | 
| a respiratory tract infection         | PROBLEM  | J98.8        | J98.8:::J06.9:::A49.9:::J22:::J20.9:::Z59.3:::T17:::J04.10:::Z13.83:::J18.9:::P28.9...      | respiratory tract infection [respiratory tract infection]:::upper respiratory tract infection [upper respiratory tract infection]:::bacterial respiratory infection [bacterial respiratory infection]:::acute respiratory infection [acute respiratory infection]:::bronchial infection [bronchial infection]...                                                | 1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::0||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0                                                                                                            |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertesolve_icd10cm_augmented_billable_hcc|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|1.5 GB|
|Case sensitive:|false|