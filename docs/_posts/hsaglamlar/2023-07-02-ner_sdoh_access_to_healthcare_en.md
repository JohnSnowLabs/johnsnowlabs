---
layout: model
title: Extract Access to Healthcare Entities from Social Determinants of Health Texts
author: John Snow Labs
name: ner_sdoh_access_to_healthcare
date: 2023-07-02
tags: [access_to_healthcare, licensed, en, sdoh, public_health, social_determinants, healthcare]
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

SDOH NER model is designed to detect and label social determinants of health (SDOH)  access to healthcare entities within text data. Social determinants of health are crucial factors that influence individuals' health outcomes, encompassing various social, economic, and environmental element. 
The model has been trained using advanced machine learning techniques on a diverse range of text sources. The model's accuracy and precision have been carefully validated against expert-labeled data to ensure reliable and consistent results. Here are the labels of the SDOH NER model with their description:

- `Access_To_Care`: Patient’s ability or barriers to access the care needed. "long distances, access to health care, rehab program, etc."
- `Healthcare_Institution`:  Health care institution means every place, institution, building or agency. "hospital, clinic, trauma centers, etc."
- `Insurance_Status`: Information regarding the patient’s insurance status. "uninsured, insured, Medicare, Medicaid, etc."

## Predicted Entities

`Access_To_Care`, `Healthcare_Institution`, `Insurance_Status`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/27.0.Social_Determinant_of_Health_Models.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_access_to_healthcare_en_4.4.4_3.0_1688317404315.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_access_to_healthcare_en_4.4.4_3.0_1688317404315.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained("ner_sdoh_access_to_healthcare", "en", "clinical/models")\
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

sample_texts = ["She has a pension and private health insurance, she reports feeling lonely and isolated.", "pt has a Medicare insurance and he visited oncology clinic last week.", "He also reported food insecurity during his childhood and lack of access to adequate healthcare. He is uninsured.", "She used to work as a unit clerk at XYZ Medical Center.","Smith works as a cleaning assistant at ABC Clinic and has access to health insurance. She is aware she needs rehab.", "he has a limited insurance."]

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

val ner_model = MedicalNerModel.pretrained("ner_sdoh_access_to_healthcare", "en", "clinical/models")
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

val data = Seq(Array("She has a pension and private health insurance, she reports feeling lonely and isolated.", "pt has a Medicare insurance and he visited oncology clinic last week.", "He also reported food insecurity during his childhood and lack of access to adequate healthcare. He is uninsured.", "She used to work as a unit clerk at XYZ Medical Center.","Smith works as a cleaning assistant at ABC Clinic and has access to health insurance. She is aware she needs rehab.", "he has a limited insurance.")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------------+-----+---+----------------------+
|chunk                        |begin|end|ner_label             |
+-----------------------------+-----+---+----------------------+
|private health insurance     |22   |45 |Insurance_Status      |
|Medicare insurance           |9    |26 |Insurance_Status      |
|oncology clinic              |43   |57 |Healthcare_Institution|
|access to adequate healthcare|66   |94 |Access_To_Care        |
|uninsured                    |103  |111|Insurance_Status      |
|XYZ Medical Center           |36   |53 |Healthcare_Institution|
|ABC Clinic                   |39   |48 |Healthcare_Institution|
|health insurance             |68   |83 |Insurance_Status      |
|rehab                        |109  |113|Access_To_Care        |
|limited insurance            |9    |25 |Insurance_Status      |
+-----------------------------+-----+---+----------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_sdoh_access_to_healthcare|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|850.9 KB|
|Dependencies:|embeddings_clinical|

## References

Internal SDOH Project

## Benchmarking

```bash
                 label  precision    recall  f1-score   support
        Access_To_Care       0.90      0.92      0.91       483
Healthcare_Institution       0.99      0.95      0.97       726
      Insurance_Status       0.93      0.83      0.88        90
             micro-avg       0.95      0.93      0.94      1299
             macro-avg       0.94      0.90      0.92      1299
          weighted-avg       0.95      0.93      0.94      1299
```
