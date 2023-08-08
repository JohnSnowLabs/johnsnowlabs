---
layout: model
title: Extract Substance Usage Entities from Social Determinants of Health Texts
author: John Snow Labs
name: ner_sdoh_substance_usage
date: 2023-07-02
tags: [alcohol, smoke, substance, sdoh, social_detrminants, en, licensed, public_health]
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

SDOH NER model is designed to detect and label social determinants of health (SDOH) substance use related entities within text data. Social determinants of health are crucial factors that influence individuals' health outcomes, encompassing various social, economic, and environmental elements. The model has been trained using advanced machine-learning techniques on a diverse range of text sources. The model's accuracy and precision have been carefully validated against expert-labeled data to ensure reliable and consistent results. Here are the labels of the SDOH NER model with their description:

- `Alcohol`: Mentions of an alcohol drinking habit.
- `Smoking`: mentions of smoking habit. "smoking, cigarette, tobacco, etc."
- `Substance_Duration`: The duration associated with the health behaviors. "for 2 years, 3 months, etc"
- `Substance_Frequency`: The frequency associated with the health behaviors. "five days a week, daily, weekly, monthly, etc"
- `Substance_Quantity`: The quantity associated with the health behaviors. "2 packs, 40 ounces, ten to twelve, moderate, etc"
- `Substance_Use`: Mentions of illegal recreational drugs use. Include also substances that can create dependency including here caffeine and tea.  "overdose, cocaine, illicit substance intoxication, coffee, etc."

## Predicted Entities

`Alcohol`, `Smoking`, `Substance_Duration`, `Substance_Frequency`, `Substance_Quantity`, `Substance_Use`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/SOCIAL_DETERMINANT_NER.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_substance_usage_en_4.4.4_3.0_1688320068416.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_substance_usage_en_4.4.4_3.0_1688320068416.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained("ner_sdoh_substance_usage", "en", "clinical/models")\
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

sample_texts = ["He does drink occasional alcohol approximately 5 to 6 alcoholic drinks per month.", "He continues to smoke one pack of cigarettes daily, as he has for the past 28 years.", "She smokes 1 ppd. Her partner is an alcoholic and a drug abuser for the last 5 years.He was using cocaine."]

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

val ner_model = MedicalNerModel.pretrained("ner_sdoh_substance_usage", "en", "clinical/models")
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

val data = Seq(Array("He does drink occasional alcohol approximately 5 to 6 alcoholic drinks per month.", "He continues to smoke one pack of cigarettes daily, as he has for the past 28 years.", "She smokes 1 ppd. Her partner is an alcoholic and a drug abuser for the last 5 years.He was using cocaine.")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------+-----+---+-------------------+
|chunk           |begin|end|ner_label          |
+----------------+-----+---+-------------------+
|drink           |8    |12 |Alcohol            |
|occasional      |14   |23 |Substance_Frequency|
|alcohol         |25   |31 |Alcohol            |
|5 to 6          |47   |52 |Substance_Quantity |
|alcoholic drinks|54   |69 |Alcohol            |
|per month       |71   |79 |Substance_Frequency|
|smoke           |16   |20 |Smoking            |
|one pack        |22   |29 |Substance_Quantity |
|cigarettes      |34   |43 |Smoking            |
|daily           |45   |49 |Substance_Frequency|
|past 28 years   |70   |82 |Substance_Duration |
|smokes          |4    |9  |Smoking            |
|1 ppd           |11   |15 |Substance_Quantity |
|alcoholic       |36   |44 |Alcohol            |
|drug abuser     |52   |62 |Substance_Use      |
|last 5 years    |72   |83 |Substance_Duration |
|cocaine         |99   |105|Substance_Use      |
+----------------+-----+---+-------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_sdoh_substance_usage|
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
            Alcohol       0.99      0.99      0.99       265
            Smoking       0.97      1.00      0.99        71
 Substance_Duration       0.93      0.81      0.87        48
Substance_Frequency       0.92      0.75      0.83        48
 Substance_Quantity       0.94      0.89      0.92        55
      Substance_Use       0.95      0.93      0.94       192
          micro-avg       0.96      0.94      0.95       679
          macro-avg       0.95      0.90      0.92       679
       weighted-avg       0.96      0.94      0.95       679
```