---
layout: model
title: Detect Social Determinants of Health Mentions
author: John Snow Labs
name: ner_sdoh_mentions
date: 2022-12-18
tags: [en, licensed, ner, sdoh, mentions, clinical]
task: Named Entity Recognition
language: en
nav_key: models
edition: Healthcare NLP 4.2.2
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Named Entity Recognition model is intended for detecting Social Determinants of Health mentions in clinical notes and trained by using MedicalNerApproach annotator that allows to train generic NER models based on Neural Networks.

| Entitiy Name     | Descriptions                                                                                                                                        | Sample Texts                                                                                                                                                    | chunks+labels                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| sdoh_community   | The patient's social<br/> and community networks, including family members,<br/> friends, and other social connections.     | - He has a 27 yo son.<br/> - The patient lives with mother.<br/> - She is a widow.<br/> - Married and has two children.<br/>                                    | - (son),(sdoh_community)<br/> - (mother),(sdoh_community)<br/> - (widow),(sdoh_community)<br/> - (Married, children),(sdoh_community,sdoh_community)<br/>   |
| sdoh_economics   | The patient's economic<br/> status and financial resources, including their<br/> occupation, income, and employment status. | - The patient worked as an accountant.<br/> - He is a retired history professor.<br/> - She is a lawyer.<br/> - Worked in insurance, currently unemployed.<br/> | - (worked),(sdoh_economics)<br/> - (retired),(sdoh_economics)<br/> - (lawyer),(sdoh_economics)<br/> - (worked, unemployed),(sdoh_economics, sdoh_economics) |
| sdoh_education   | The patient's education-related<br/> passages such as schooling, college, or degrees attained.                              | - She graduated from high school.<br/> - He is a fourth grade teacher in inner city.<br/> - He completed some college.<br/>                                     | - (graduated from high school),(sdoh_education)<br/> - (teacher),(sdoh_education)<br/> - (college),(sdoh_education)<br/>                                    |
| sdoh_environment | The patient's living<br/> environment and access to housing.                                                                | - He lives at home.<br/> - Her other daughter lives in the apartment below.<br/> - The patient lives with her husband in a retirement community.<br/>           | - (home),(sdoh_environment)<br/> - (apartment),(sdoh_environment)<br/> - (retirement community),(sdoh_environment)<br/>                                     |
| behavior_tobacco | This entity is labeled based on any indication of<br/> the patient's current or past tobacco<br/> use and smoking history                           | - She smoked one pack a day for forty years.<br/> - The patient denies tobacco use.<br/> - The patient smokes an occasional cigar.<br/>                         | - (smoked one pack),(behavior_tobacco)<br/> - (tobacco),(behavior_tobacco)<br/> - (smokes an occasional cigar),(behavior_tobacco)<br/>                      |
| behavior_alcohol | This entity is used to label indications of<br/> the patient's alcohol consumption.                                                                 | - She drinks alcohol.<br/> - The patient denies ethanol.<br/> - He denies ETOH.<br/>                                                                            | - (alcohol),(behavior_alcohol)<br/> - (ethanol),(behavior_alcohol)<br/> - (ETOH),(behavior_alcohol)<br/>                                                    |
| behavior_drug    | This entity is used to label any indications of<br/> the patient's current or past drug use.                                                        | - She denies any intravenous drug abuse.<br/> - No illicit drug use including IV per family.<br/> - The patient any using recreational drugs.<br/>              | - (intravenous drug),(behavior_drug)<br/> - (illicit drug, IV),(behavior_drug, behavior_drug)<br/> - (recreational drugs),(behavior_drug)<br/>              |


## Predicted Entities

`sdoh_community`, `sdoh_economics`, `sdoh_education`, `sdoh_environment`, `behavior_tobacco`, `behavior_alcohol`, `behavior_drug`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/27.0.Social_Determinant_of_Health_Models.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_mentions_en_4.2.2_3.0_1671369830893.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_mentions_en_4.2.2_3.0_1671369830893.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")\
      
sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
    .setInputCols("document")\
    .setOutputCol("sentence")
    
tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")
    
embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("embeddings")
    
ner_model = MedicalNerModel.pretrained("ner_sdoh_mentions", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")
    
ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")
    
nlpPipeline = Pipeline(stages=[
    document_assembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter])

data = spark.createDataFrame([["Mr. Known lastname 9880 is a pleasant, cooperative gentleman with a long standing history (20 years) diverticulitis. He is married and has 3 children. He works in a bank. He denies any alcohol or intravenous drug use. He has been smoking for many years."]]).toDF("text")

result = nlpPipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
    
val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")
    .setInputCols("document")
    .setOutputCol("sentence")
    
val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")
    
val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")
    
val ner_model = MedicalNerModel.pretrained("ner_sdoh_mentions", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")
    
val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    
val nlpPipeline = new PipelineModel().setStages(Array(
    document_assembler, 
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter))

val data = Seq("Mr. Known lastname 9880 is a pleasant, cooperative gentleman with a long standing history (20 years) diverticulitis. He is married and has 3 children. He works in a bank. He denies any alcohol or intravenous drug use. He has been smoking for many years.").toDS.toDF("text")

val result = nlpPipeline.fit(data).transform(data)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.med_ner.sdoh_mentions").predict("""Mr. Known lastname 9880 is a pleasant, cooperative gentleman with a long standing history (20 years) diverticulitis. He is married and has 3 children. He works in a bank. He denies any alcohol or intravenous drug use. He has been smoking for many years.""")
```

</div>

## Results

```bash
+----------------+----------------+
|chunk           |ner_label       |
+----------------+----------------+
|married         |sdoh_community  |
|children        |sdoh_community  |
|works           |sdoh_economics  |
|alcohol         |behavior_alcohol|
|intravenous drug|behavior_drug   |
|smoking         |behavior_tobacco|
+----------------+----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_sdoh_mentions|
|Compatibility:|Healthcare NLP 4.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|15.1 MB|

## Benchmarking

```bash
           label  precision    recall  f1-score   support
behavior_alcohol       0.95      0.94      0.94       798
   behavior_drug       0.93      0.92      0.92       366
behavior_tobacco       0.95      0.95      0.95       936
  sdoh_community       0.97      0.97      0.97       969
  sdoh_economics       0.95      0.91      0.93       363
  sdoh_education       0.69      0.65      0.67        34
sdoh_environment       0.93      0.90      0.92       651
       micro-avg       0.95      0.94      0.94      4117
       macro-avg       0.91      0.89      0.90      4117
    weighted-avg       0.95      0.94      0.94      4117
```
