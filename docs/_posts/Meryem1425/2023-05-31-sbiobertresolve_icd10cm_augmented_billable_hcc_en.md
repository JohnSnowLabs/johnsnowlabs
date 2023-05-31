---
layout: model
title: Sentence Entity Resolver for Billable ICD10-CM HCC Codes
author: John Snow Labs
name: sbiobertresolve_icd10cm_augmented_billable_hcc
date: 2023-05-31
tags: [licensed, en, clinical, hcc, icd10cm, entity_resolution]
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

This model maps extracted medical entities to ICD-10-CM codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings and it supports 7-digit codes with HCC status. It has been updated by dropping the invalid codes that exist in the previous versions. In the result, look for the `all_k_aux_labels` parameter in the metadata to get HCC status. The HCC status can be divided to get further information: `billable status`, `hcc status`, and `hcc score`. For example if the result is `1||1||8`: `the billable status is 1`, `hcc status is 1`, and `hcc score is 8`.

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_ICD10_CM/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_augmented_billable_hcc_en_4.4.2_3.0_1685507415461.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_augmented_billable_hcc_en_4.4.2_3.0_1685507415461.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

`sbiobertresolve_icd10cm_augmented_billable_hcc` resolver model must be used with `sbiobert_base_cased_mli` as embeddings.

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")\

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc") 

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

icd_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_augmented_billable_hcc", "en", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages = [document_assembler,
                                       sentenceDetectorDL,
                                       tokenizer,
                                       word_embeddings,
                                       ner,
                                       ner_converter,
                                       c2doc,
                                       sbert_embedder,
                                       icd_resolver])

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis and obesity , presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."""]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)
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

val icd10_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_augmented_billable_hcc", "en", "clinical/models")
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

val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis and obesity , presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection.").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
| ner_chunk                             | entity   | icd10_code   | all_codes                                                                              | resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | hcc_list                                                                                                                                                                                                                                                                                   |
|:--------------------------------------|:---------|:-------------|:---------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| gestational diabetes mellitus         | PROBLEM  | O24.4        | O24.4:::O24.41:::Z86.32:::O24.11:::O24.81:::P70.2:::O24.01:::O24.42...                 | gestational diabetes mellitus [gestational diabetes mellitus]:::gestational diabetes mellitus in pregnancy [gestational diabetes mellitus in pregnancy]:::personal history of gestational diabetes [personal history of gestational diabetes]:::pre-existing type 2 diabetes mellitus, in pregnancy [pre-existing type 2 diabetes mellitus, in pregnancy]...                                                                                                                                                     | '0||0||0', '0||0||0', '1||0||0', '0||0||0', '0||0||0', '1||0||0', '0||0||0', '0||0||0', '1||0||0', '0||0||0', '1||0||0', '1||0||0', '1||0||0', '0||0||0', '1||0||0', '1||0||0', '1||0||0', '0||0||0', '1||0||0', '1||1||18', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||1||18'        |
| subsequent type two diabetes mellitus | PROBLEM  | E11          | E11:::E11.62:::E11.5:::E11.69:::E11.59:::E09:::E11.6:::E11.8...                        | type 2 diabetes mellitus [type 2 diabetes mellitus]:::type 2 diabetes mellitus with skin complications [type 2 diabetes mellitus with skin complications]:::type 2 diabetes mellitus with circulatory complications [type 2 diabetes mellitus with circulatory complications]:::type 2 diabetes mellitus with other specified complication [type 2 diabetes mellitus with other specified complication]...                                                                                                       | '0||0||0', '0||0||0', '0||0||0', '1||1||18', '1||1||18', '0||0||0', '0||0||0', '1||1||18', '0||0||0', '1||1||18', '0||0||0', '1||1||18', '1||1||18', '0||0||0', '0||0||0', '1||1||18', '0||0||0', '0||0||0', '1||1||18', '0||0||0', '1||0||0', '0||0||0', '1||1||18'                       |
| T2DM                                  | PROBLEM  | Q06.0        | Q06.0:::N94.0:::B48.3:::L02.42:::R14.2:::L02.43:::R29.702:::H53.55...                  | amyelia [amyelia]:::mittelschmerz [mittelschmerz]:::geotrichosis [geotrichosis]:::furuncle of limb [furuncle of limb]:::eructation [eructation]:::carbuncle of limb [carbuncle of limb]:::nihss score 2 [nihss score 2]:::tritanomaly [tritanomaly]:::beriberi [beriberi]:::megaloureter [megaloureter]...                                                                                                                                                                                                       | '1||1||72', '1||0||0', '1||0||0', '0||0||0', '1||0||0', '0||0||0', '1||0||0', '1||0||0', '0||0||0', '1||0||0', '1||0||0', '1||0||0', '0||0||0', '1||0||0', '1||0||0', '1||0||0', '0||0||0', '0||0||0', '0||0||0', '0||0||0', '1||1||86', '1||0||0', '1||0||0', '1||0||0', '1||0||0'        |
| HTG-induced pancreatitis              | PROBLEM  | K85.3        | K85.3:::K85:::K86.0:::K85.2:::K85.1:::K85.0:::K85.32:::K85.8:::B25.2...                | drug induced acute pancreatitis [drug induced acute pancreatitis]:::acute pancreatitis [acute pancreatitis]:::alcohol-induced chronic pancreatitis [alcohol-induced chronic pancreatitis]:::alcohol induced acute pancreatitis [alcohol induced acute pancreatitis]:::biliary acute pancreatitis [biliary acute pancreatitis]:::idiopathic acute pancreatitis [idiopathic acute pancreatitis]...                                                                                                                 | '0||0||0', '0||0||0', '1||1||34', '0||0||0', '0||0||0', '0||0||0', '1||0||0', '0||0||0', '1||1||6', '0||0||0', '1||0||0', '1||0||0', '0||0||0', '1||0||0', '1||0||0', '1||0||0', '0||0||0', '0||0||0', '1||0||0', '1||1||34', '0||0||0', '1||0||0', '1||0||0', '0||0||0', '0||0||0'        |
| acute hepatitis                       | PROBLEM  | B15          | B15:::B17.2:::B16:::K71.2:::B17.1:::B00.81:::K75.4:::K70.1:::B17.8:::B17...            | acute hepatitis a [acute hepatitis a]:::acute hepatitis e [acute hepatitis e]:::acute hepatitis b [acute hepatitis b]:::toxic liver disease with acute hepatitis [toxic liver disease with acute hepatitis]:::acute hepatitis c [acute hepatitis c]:::herpesviral hepatitis [herpesviral hepatitis]:::autoimmune hepatitis [autoimmune hepatitis]:::alcoholic hepatitis [alcoholic hepatitis]...                                                                                                                 | '0||0||0', '1||0||0', '0||0||0', '1||0||0', '0||0||0', '1||0||0', '1||1||29', '0||0||0', '1||0||0', '0||0||0', '1||0||0', '0||0||0', '1||1||23', '0||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '0||0||0', '1||1||6', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0'        |
| obesity                               | PROBLEM  | E66          | E66:::E66.3:::E66.8:::E66.0:::E66.1:::E88.81:::E66.09:::E66.01:::E34.4...              | overweight and obesity [overweight and obesity]:::overweight [overweight]:::other obesity [other obesity]:::obesity due to excess calories [obesity due to excess calories]:::drug-induced obesity [drug-induced obesity]:::metabolic syndrome [metabolic syndrome]:::other obesity due to excess calories [other obesity due to excess calories]:::morbid (severe) obesity due to excess calories [morbid (severe) obesity due to excess calories]...                                                           | '0||0||0', '1||0||0', '1||0||0', '0||0||0', '1||0||0', '1||0||0', '1||0||0', '1||1||22', '1||1||23', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '0||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '0||0||0', '1||0||0', '1||0||0', '1||0||0', '1||1||18', '0||0||0', '1||0||0'       |
| polyuria                              | PROBLEM  | R35          | R35:::R35.81:::R35.89:::R35.8:::R31:::R30.0:::E72.01:::R80:::R34:::R82.4...            | polyuria [polyuria]:::nocturnal polyuria [nocturnal polyuria]:::other polyuria [other polyuria]:::other polyuria [other polyuria]:::hematuria [hematuria]:::dysuria [dysuria]:::cystinuria [cystinuria]:::proteinuria [proteinuria]:::anuria and oliguria [anuria and oliguria]:::acetonuria [acetonuria]:::hyperuricosuria [hyperuricosuria]:::bacteriuria [bacteriuria]:::chyluria [chyluria]...                                                                                                               | '0||0||0', '1||0||0', '1||0||0', '0||0||0', '0||0||0', '1||0||0', '1||1||23', '0||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '0||0||0', '0||0||0', '1||0||0', '0||0||0', '1||0||0', '1||0||0', '1||0||0', '0||0||0', '0||0||0'         |
| polydipsia                            | PROBLEM  | R63.1        | R63.1:::O40:::G47.5:::R63.2:::R00.2:::G47.1:::G47.13:::F51.11:::G47.19...              | polydipsia [polydipsia]:::polyhydramnios [polyhydramnios]:::parasomnia [parasomnia]:::polyphagia [polyphagia]:::palpitations [palpitations]:::hypersomnia [hypersomnia]:::recurrent hypersomnia [recurrent hypersomnia]:::primary hypersomnia [primary hypersomnia]:::other hypersomnia [other hypersomnia]:::polytrichia [polytrichia]:::orthopnea [orthopnea]:::epigastric abdominal rigidity [epigastric abdominal rigidity]...                                                                               | '0||0||0', '1||0||0', '1||0||0', '0||0||0', '0||0||0', '1||0||0', '1||1||23', '0||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '0||0||0', '0||0||0', '1||0||0', '0||0||0', '1||0||0', '1||0||0', '1||0||0', '0||0||0', '0||0||0'         |
| poor appetite                         | PROBLEM  | R45.81       | R45.81:::R68.82:::Z59.4:::R29.810:::R46.4:::R53.1:::R06.02:::R45.0:::E63.9...          | low self-esteem [low self-esteem]:::decreased libido [decreased libido]:::lack of adequate food [lack of adequate food]:::facial weakness [facial weakness]:::slowness and poor responsiveness [slowness and poor responsiveness]:::weakness [weakness]:::shortness of breath [shortness of breath]:::nervousness [nervousness]:::nutritional deficiency, unspecified [nutritional deficiency, unspecified]...                                                                                                   | '1||0||0', '1||0||0', '0||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '0||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '0||0||0', '0||0||0', '1||0||0', '1||0||0', '0||0||0', '1||0||0', '1||0||0', '1||0||0'          |
| vomiting                              | PROBLEM  | R11.1        | R11.1:::G43.A:::R11.0:::R11:::R11.14:::R11.12:::R23.1:::G47.51:::R11.10...             | vomiting [vomiting]:::cyclical vomiting [cyclical vomiting]:::nausea [nausea]:::nausea and vomiting [nausea and vomiting]:::bilious vomiting [bilious vomiting]:::projectile vomiting [projectile vomiting]:::pallor [pallor]:::confusional arousals [confusional arousals]:::vomiting, unspecified [vomiting, unspecified]:::miosis [miosis]:::facial weakness [facial weakness]:::nasal congestion [nasal congestion]...                                                                                       | '0||0||0', '0||0||0', '1||0||0', '0||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '1||0||0', '0||0||0', '0||0||0', '1||0||0', '0||0||0', '1||1||83', '1||0||0', '1||0||0', '1||0||0'         |
| a respiratory tract infection         | PROBLEM  | T17          | T17:::T81.4:::T81.81:::J95.851:::T17.8:::Z87.0:::J44.0:::J06:::T81.44:::Z22...         | foreign body in respiratory tract [foreign body in respiratory tract]:::infection following a procedure [infection following a procedure]:::complication of inhalation therapy [complication of inhalation therapy]:::ventilator associated pneumonia [ventilator associated pneumonia]:::foreign body in other parts of respiratory tract [foreign body in other parts of respiratory tract]:::personal history of diseases of the respiratory system [personal history of diseases of the respiratory system]  | '0||0||0', '0||0||0', '0||0||0', '1||1||114', '0||0||0', '0||0||0', '1||1||111', '0||0||0', '0||0||0', '0||0||0', '0||0||0', '0||0||0', '1||0||0', '0||0||0', '0||0||0', '0||0||0', '1||1||112', '0||0||0', '1||1||82', '0||0||0', '0||0||0', '0||0||0', '0||0||0', '0||0||0', '0||0||0'   |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd10cm_augmented_billable_hcc|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|1.4 GB|
|Case sensitive:|false|
