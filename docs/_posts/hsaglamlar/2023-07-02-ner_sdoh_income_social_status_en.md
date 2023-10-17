---
layout: model
title: Extract Income and Social Status Entities from Social Determinants of Health Texts
author: John Snow Labs
name: ner_sdoh_income_social_status
date: 2023-07-02
tags: [education, employment, income, financial_status, maritial_status, sdoh, social_determinants, public_health, en, licensed]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

SDOH NER model is designed to detect and label social determinants of health (SDOH) income and social status-related entities within text data. Social determinants of health are crucial factors that influence individuals' health outcomes, encompassing various social, economic, and environmental elements. The model has been trained using advanced machine-learning techniques on a diverse range of text sources. The model's accuracy and precision have been carefully validated against expert-labeled data to ensure reliable and consistent results. Here are the labels of the SDOH NER model with their description:

- `Education`:Patient’s educational background
- `Employment`: Patient or provider occupational titles.
- `Financial_Status`: Financial status refers to the state and condition of the person’s finances. "financial decline, debt, bankruptcy, etc."
- `Income`: Information regarding the patient’s income
- `Marital_Status`: Terms that indicate the person’s marital status.
- `Population_Group`: The population group that a person belongs to, that does not fall under any other entities. "refugee, prison patient, etc."

## Predicted Entities

`Education`, `Employment`, `Financial_Status`, `Income`, `Marital_Status`, `Population_Group`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/27.0.Social_Determinant_of_Health_Models.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_income_social_status_en_4.4.4_3.0_1688318884654.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_income_social_status_en_4.4.4_3.0_1688318884654.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from pyspark.sql.types import StringType

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_sdoh_income_social_status", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
    ])

sample_texts = ["Pt is described as divorced and pleasant when approached but keeps to himself. Pt is working as a plumber, but he gets financial diffuculties. He has a son student at college. He is an immigrant. He has a low income.", "Smith is a 55 years old, divorced Mexican American woman with financial problems.", "He lives with his family, in his own house in a remote town, with a monthly income of $1200 per month.","She reports feeling unsafe at home but is financially dependent.", "35-year-old, male patient, married, Asian immigrant, morbidly obese with a BMI of 32, and a history of hypertension presents to the clinic with worsening blood pressure readings. He is a high school graduate and is construction worker by profession."]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_sdoh_income_social_status", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
))

val data = Seq(Array("Pt is described as divorced and pleasant when approached but keeps to himself. Pt is working as a plumber, but he gets financial diffuculties. He has a son student at college. He is an immigrant. He has a low income.","Smith is a 55 years old, divorced Mexican American woman with financial problems.", "He lives with his family, in his own house in a remote town, with a monthly income of $1200 per month.","She reports feeling unsafe at home but is financially dependent.", "35-year-old, male patient, married, Asian immigrant, morbidly obese with a BMI of 32, and a history of hypertension presents to the clinic with worsening blood pressure readings. He is a high school graduate and is construction worker by profession.")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---------------------------------+-----+---+----------------+
|chunk                            |begin|end|ner_label       |
+---------------------------------+-----+---+----------------+
|divorced                         |19   |26 |Marital_Status  |
|plumber                          |98   |104|Employment      |
|financial diffuculties           |119  |140|Financial_Status|
|student                          |156  |162|Education       |
|college                          |167  |173|Education       |
|immigrant                        |185  |193|Population_Group|
|low income                       |205  |214|Income          |
|divorced                         |25   |32 |Marital_Status  |
|financial problems               |62   |79 |Financial_Status|
|monthly income of $1200 per month|68   |100|Income          |
|financially dependent            |42   |62 |Financial_Status|
|married                          |27   |33 |Marital_Status  |
|immigrant                        |42   |50 |Population_Group|
|high school graduate             |187  |206|Education       |
|construction worker              |215  |233|Employment      |
+---------------------------------+-----+---+----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_sdoh_income_social_status|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|3.0 MB|
|Dependencies:|embeddings_clinical|

## References

Internal SDOH Project

## Benchmarking

```bash
           label  precision    recall  f1-score   support
       Education       0.85      0.92      0.88        61
      Employment       0.94      0.96      0.95      2142
Financial_Status       0.89      0.76      0.82       128
          Income       0.97      0.80      0.88        41
  Marital_Status       0.97      0.97      0.97        93
Population_Group       0.91      0.87      0.89        23
       micro-avg       0.94      0.95      0.94      2488
       macro-avg       0.92      0.88      0.90      2488
    weighted-avg       0.94      0.95      0.94      2488

```
