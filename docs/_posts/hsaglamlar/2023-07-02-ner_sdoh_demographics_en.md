---
layout: model
title: Extract Demographic Entities from Social Determinants of Health Texts
author: John Snow Labs
name: ner_sdoh_demographics
date: 2023-07-02
tags: [family_member, age, gender, geographic_entity, language, race_ethnicity, spiritual_beliefs, sdoh, social_determinants, public_health, en, licensed]
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

This SDOH NER model is designed to detect and label social determinants of health (SDOH) demographic entities within text data. Social determinants of health are crucial factors that influence individuals' health outcomes, encompassing various social, economic, and environmental elements. The model has been trained using advanced machine-learning techniques on a diverse range of text sources. The model's accuracy and precision have been carefully validated against expert-labeled data to ensure reliable and consistent results. Here are the labels of the SDOH NER model with their description:

- `Age`: All mention of ages including "Newborn, Infant, Child, Teenager, Teenage, Adult, etc."
- `Family_Member`: Nouns that refer to a family member. "mother, father, brother, sister, etc."
- `Gender`: Gender-specific nouns and pronouns
- `Geographic_Entity`: Geographical location refers to a specific physical point on Earth. 
- `Language`: A system of conventional spoken, manual (signed), or written symbols by means of which human beings express themselves. "English, Spanish-speaking, etc. "
- `Race_Ethnicity`: The race and ethnicity categories include racial, ethnic, and national origins.
- `Spiritual_Beliefs`: Spirituality is concerned with beliefs beyond self, usually related to the existence of a superior being. "spiritual beliefs, religious beliefs, etc."

## Predicted Entities

`Age`, `Family_Member`, `Gender`, `Geographic_Entity`, `Language`, `Race_Ethnicity`, `Spiritual_Beliefs`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/27.0.Social_Determinant_of_Health_Models.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_demographics_en_4.4.4_3.0_1688323815011.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_demographics_en_4.4.4_3.0_1688323815011.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained("ner_sdoh_demographics", "en", "clinical/models")\
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

sample_texts = ["Maria, a 35-year-old Hispanic woman, visited her healthcare provider for a routine check-up. As a bilingual individual, she was able to communicate comfortably in both English and Spanish. Maria shared that she practices Catholicism and finds strength and comfort in her faith. She has religious beliefs.",
"Ali, a 20 years old African American man, lives in New York. He is Muslim. He lives with his parents.",
"SOCIAL HISTORY: He is a former tailor from Korea. He has a Buddhist faith. He is an older adult.",
"He lives alone in France, single and no children. He speaks French and Portuguese. He is a member of Protestant Church",
"Pt is at her 60s married, Caucasian, Orthodox woman. Pt speaks English reasonably well. She lives with her son and husband."]


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

val ner_model = MedicalNerModel.pretrained("ner_sdoh_demographics", "en", "clinical/models")
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

val data = Seq(Array("Maria, a 35-year-old Hispanic woman, visited her healthcare provider for a routine check-up. As a bilingual individual, she was able to communicate comfortably in both English and Spanish. Maria shared that she practices Catholicism and finds strength and comfort in her faith. She has religious beliefs.",
"Ali, a 20 years old African American man, lives in New York. He is Muslim. He lives with his parents.",
"SOCIAL HISTORY: He is a former tailor from Korea. He has a Buddhist faith. He is an older adult.",
"He lives alone in France, single and no children. He speaks French and Portuguese. He is a member of Protestant Church",
"Pt is at her 60s married, Caucasian, Orthodox woman. Pt speaks English reasonably well. She lives with her son and husband.")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------+-----+---+-----------------+
|chunk            |begin|end|ner_label        |
+-----------------+-----+---+-----------------+
|35-year-old      |9    |19 |Age              |
|Hispanic         |21   |28 |Race_Ethnicity   |
|woman            |30   |34 |Gender           |
|her              |45   |47 |Gender           |
|bilingual        |98   |106|Language         |
|she              |120  |122|Gender           |
|English          |168  |174|Language         |
|Spanish          |180  |186|Language         |
|she              |207  |209|Gender           |
|Catholicism      |221  |231|Spiritual_Beliefs|
|her              |267  |269|Gender           |
|faith            |271  |275|Spiritual_Beliefs|
|She              |278  |280|Gender           |
|religious beliefs|286  |302|Spiritual_Beliefs|
|20 years old     |7    |18 |Age              |
|African American |20   |35 |Race_Ethnicity   |
|man              |37   |39 |Gender           |
|New York         |51   |58 |Geographic_Entity|
|He               |61   |62 |Gender           |
|Muslim           |67   |72 |Spiritual_Beliefs|
|He               |75   |76 |Gender           |
|his              |89   |91 |Gender           |
|parents          |93   |99 |Family_Member    |
|He               |16   |17 |Gender           |
|Korea            |43   |47 |Geographic_Entity|
|He               |50   |51 |Gender           |
|Buddhist faith   |59   |72 |Spiritual_Beliefs|
|He               |75   |76 |Gender           |
|older adult      |84   |94 |Age              |
|He               |0    |1  |Gender           |
|France           |18   |23 |Geographic_Entity|
|children         |40   |47 |Family_Member    |
|He               |50   |51 |Gender           |
|French           |60   |65 |Language         |
|Portuguese       |71   |80 |Language         |
|He               |83   |84 |Gender           |
|Protestant       |101  |110|Spiritual_Beliefs|
|her              |9    |11 |Gender           |
|60s              |13   |15 |Age              |
|Caucasian        |26   |34 |Race_Ethnicity   |
|Orthodox         |37   |44 |Spiritual_Beliefs|
|woman            |46   |50 |Gender           |
|English          |63   |69 |Language         |
|She              |88   |90 |Gender           |
|her              |103  |105|Gender           |
|son              |107  |109|Family_Member    |
|husband          |115  |121|Family_Member    |
+-----------------+-----+---+-----------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_sdoh_demographics|
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
              Age       0.93      0.94      0.93       470
    Family_Member       0.98      0.99      0.99      1958
           Gender       0.99      0.98      0.99      5021
Geographic_Entity       0.92      0.93      0.92       104
         Language       1.00      0.91      0.95        22
   Race_Ethnicity       1.00      0.96      0.98        28
Spiritual_Beliefs       0.96      0.91      0.94        57
        micro-avg       0.98      0.98      0.98      7660
        macro-avg       0.97      0.95      0.96      7660
     weighted-avg       0.98      0.98      0.98      7660

```