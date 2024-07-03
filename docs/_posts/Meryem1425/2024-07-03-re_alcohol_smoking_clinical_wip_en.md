---
layout: model
title: Relation Extraction between Treatment-Issue Entities and Drinking-Smoking Status
author: John Snow Labs
name: re_alcohol_smoking_clinical_wip
date: 2024-07-03
tags: [licensed, clinical, en, relation_extraction, alcohol, smoking, alcohol_smoking, treatment, issue, drinking_status, smoking_status]
task: Relation Extraction
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.0
supported: true
annotator: RelationExtractionModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This relation extraction model identifies various relations between different clinical entities. It recognizes relations between treatment cessation and withdrawal with drinking and smoking status, as well as relations between various health issues (Neurologic, Psychiatric, Cardiovascular, Respiratory, GUT, and Other Health Issues) and drinking and smoking status. In this model, the relations are labeled as 'is_caused_by' and 'is_used_for'.

## Predicted Entities

`is_caused_by`, `is_used_for`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/re_alcohol_smoking_clinical_wip_en_5.3.3_3.0_1720022272909.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/re_alcohol_smoking_clinical_wip_en_5.3.3_3.0_1720022272909.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
    .setInputCols("document") \
    .setOutputCol("sentence")

tokenizer = RegexTokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token") \
    .setPattern('\\s+|(?=[-.:;*+,\(\)\/$&%\\[\\]])|(?<=[-.:;*+,\(\)\/$&%\\[\\]])')

embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_alcohol_smoking", "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pos_tagger = PerceptronModel()\
    .pretrained("pos_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token"])\
    .setOutputCol("pos_tags")

dependency_parser = DependencyParserModel()\
    .pretrained("dependency_conllu", "en")\
    .setInputCols(["sentence", "pos_tags", "token"])\
    .setOutputCol("dependencies")

clinical_re_Model = RelationExtractionModel()\
    .pretrained("re_alcohol_smoking_clinical_wip", "en", "clinical/models")\
    .setInputCols(["embeddings", "pos_tags", "ner_chunk", "dependencies"])\
    .setOutputCol("relations")\
    .setMaxSyntacticDistance(4)\
    .setRelationPairs(["Cessation_Treatment-Drinking_Status",
    "Withdrawal_Treatment-Drinking_Status",
    "Cessation_Treatment-Smoking_Status",
    "Withdrawal_Treatment-Smoking_Status",
    "Neurologic_Issues-Drinking_Status",
    "Neurologic_Issues-Smoking_Status",
    "Psychiatric_Issues-Drinking_Status",
    "Psychiatric_Issues-Smoking_Status",
    "Cardiovascular_Issues-Drinking_Status",
    "Cardiovascular_Issues-Smoking_Status",
    "Respiratory_Issues-Drinking_Status",
    "Respiratory_Issues-Smoking_Status",
    "GUT_Issues-Drinking_Status",
    "GUT_Issues-Smoking_Status",
    "Other_Health_Issues-Drinking_Status",
    "Other_Health_Issues-Smoking_Status"])

re_pipeline = Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter,
    pos_tagger,
    dependency_parser,
    clinical_re_Model
])

text = ["""Pulmonary Function Tests: Demonstrates airflow limitation consistent with chronic obstructive pulmonary disease
 (COPD). Diagnosis: Acute exacerbation of COPD secondary to smoking.
 Diagnosis: Alcoholic fatty liver disease and smoking-related respiratory symptoms.Management: The patient received alcohol cessation counseling and support services to address her alcohol use disorder. She was also provided with smoking cessation pharmacotherapy and behavioral interventions to help her quit smoking."""]


lmodel = LightPipeline(model)
annotations = lmodel.fullAnnotate(text)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") 
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new RegexTokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")
    .setPattern("\\s+|(?=[-.:;*+,\(\)\/$&%\\[\\]])|(?<=[-.:;*+,\(\)\/$&%\\[\\]])")

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_alcohol_smoking", "en", "clinical/models")
    .setInputCols(Array("sentence", "token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pos_tagger = PerceptronModel()
    .pretrained("pos_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("pos_tags")

val dependency_parser = DependencyParserModel()
    .pretrained("dependency_conllu", "en")
    .setInputCols(Array("sentence", "pos_tags", "token"))
    .setOutputCol("dependencies")

val clinical_re_Model = RelationExtractionModel()
    .pretrained("re_alcohol_smoking_clinical_wip", "en", "clinical/models")
    .setInputCols(Array("embeddings", "pos_tags", "ner_chunk", "dependencies"))
    .setOutputCol("relations")\
    .setMaxSyntacticDistance(4)\
    .setRelationPairs(Array("Cessation_Treatment-Drinking_Status",
    "Withdrawal_Treatment-Drinking_Status",
    "Cessation_Treatment-Smoking_Status",
    "Withdrawal_Treatment-Smoking_Status",
    "Neurologic_Issues-Drinking_Status",
    "Neurologic_Issues-Smoking_Status",
    "Psychiatric_Issues-Drinking_Status",
    "Psychiatric_Issues-Smoking_Status",
    "Cardiovascular_Issues-Drinking_Status",
    "Cardiovascular_Issues-Smoking_Status",
    "Respiratory_Issues-Drinking_Status",
    "Respiratory_Issues-Smoking_Status",
    "GUT_Issues-Drinking_Status",
    "GUT_Issues-Smoking_Status",
    "Other_Health_Issues-Drinking_Status",
    "Other_Health_Issues-Smoking_Status"))

val re_pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter,
    pos_tagger,
    dependency_parser,
    clinical_re_Model
))

val text = Seq("""Pulmonary Function Tests: Demonstrates airflow limitation consistent with chronic obstructive pulmonary disease
 (COPD). Diagnosis: Acute exacerbation of COPD secondary to smoking.
 Diagnosis: Alcoholic fatty liver disease and smoking-related respiratory symptoms.Management: The patient received alcohol cessation counseling and support services to address her alcohol use disorder. She was also provided with smoking cessation pharmacotherapy and behavioral interventions to help her quit smoking.""").toDF("text")


val lmodel = LightPipeline(model)
val annotations = lmodel.fullAnnotate(text)
```
</div>

## Results

```bash
|    |   sentence |   entity1_begin |   entity1_end | chunk1   | entity1            |   entity2_begin |   entity2_end | chunk2                    | entity2             | relation     |   confidence |
|---:|-----------:|----------------:|--------------:|:---------|:-------------------|----------------:|--------------:|:--------------------------|:--------------------|:-------------|-------------:|
|  0 |          2 |             154 |           157 | COPD     | Respiratory_Issues |             172 |           178 | smoking                   | Smoking_Status      | is_caused_by |     0.999902 |
|  2 |          4 |             297 |           303 | alcohol  | Drinking_Status    |             305 |           324 | cessation counseling      | Cessation_Treatment | is_used_for  |     0.999512 |
|  3 |          4 |             297 |           303 | alcohol  | Drinking_Status    |             330 |           345 | support services          | Cessation_Treatment | is_used_for  |     0.933377 |
|  4 |          5 |             411 |           417 | smoking  | Smoking_Status     |             419 |           443 | cessation pharmacotherapy | Cessation_Treatment | is_used_for  |     0.996433 |
|  5 |          5 |             411 |           417 | smoking  | Smoking_Status     |             449 |           472 | behavioral interventions  | Cessation_Treatment | is_used_for  |     0.9565   |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|re_alcohol_smoking_clinical_wip|
|Type:|re|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings, pos_tags, train_ner_chunks, dependencies]|
|Output Labels:|[relations]|
|Language:|en|
|Size:|4.3 MB|
|Max Syntactic Distance:|0|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
           O       0.95      0.96      0.96       309
is_caused_by       0.81      0.67      0.73        33
 is_used_for       0.82      0.87      0.85        47
    accuracy         -         -       0.93       389
   macro-avg       0.86      0.83      0.85       389
weighted-avg       0.92      0.93      0.92       389
```
