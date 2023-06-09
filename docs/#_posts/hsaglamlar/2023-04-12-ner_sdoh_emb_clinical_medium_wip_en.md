---
layout: model
title: Social Determinants of Health (clinical_medium)
author: John Snow Labs
name: ner_sdoh_emb_clinical_medium_wip
date: 2023-04-12
tags: [en, clinical_medium, social_determinants, ner, public_health, sdoh, licensed]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.2
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts terminology related to Social Determinants of Health from various kinds of biomedical documents.

## Predicted Entities

`Access_To_Care`, `Age`, `Alcohol`, `Chidhood_Event`, `Communicable_Disease`, `Community_Safety`, `Diet`, `Disability`, `Eating_Disorder`, `Education`, `Employment`, `Environmental_Condition`, `Exercise`, `Family_Member`, `Financial_Status`, `Food_Insecurity`, `Gender`, `Geographic_Entity`, `Healthcare_Institution`, `Housing`, `Hyperlipidemia`, `Hypertension`, `Income`, `Insurance_Status`, `Language`, `Legal_Issues`, `Marital_Status`, `Mental_Health`, `Obesity`, `Other_Disease`, `Other_SDoH_Keywords`, `Population_Group`, `Quality_Of_Life`, `Race_Ethnicity`, `Sexual_Activity`, `Sexual_Orientation`, `Smoking`, `Social_Exclusion`, `Social_Support`, `Spiritual_Beliefs`, `Substance_Duration`, `Substance_Frequency`, `Substance_Quantity`, `Substance_Use`, `Transportation`, `Violence_Or_Abuse`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_NER/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/SOCIAL_DETERMINANT_NER.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_emb_clinical_medium_wip_en_4.3.2_3.2_1681303578006.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_emb_clinical_medium_wip_en_4.3.2_3.2_1681303578006.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_medium", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_sdoh_emb_clinical_medium_wip", "en", "clinical/models")\
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

sample_texts = [["Smith is a 55 years old, divorced Mexcian American woman with financial problems. She speaks spanish. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and does not have access to health insurance or paid sick leave. She has a son student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reprots having her catholic faith as a means of support as well.  She has long history of etoh abuse, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day. She had DUI back in April and was due to be in court this week."]]
             
data = spark.createDataFrame(sample_texts).toDF("text")

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

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_medium", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_sdoh_emb_clinical_medium_wip", "en", "clinical/models")
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

val data = Seq("Smith is a 55 years old, divorced Mexcian American woman with financial problems. She speaks spanish. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and does not have access to health insurance or paid sick leave. She has a son student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reprots having her catholic faith as a means of support as well.  She has long history of etoh abuse, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day. She had DUI back in April and was due to be in court this week.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------+-----+---+-------------------+
|chunk             |begin|end|ner_label          |
+------------------+-----+---+-------------------+
|55 years old      |11   |22 |Age                |
|divorced          |25   |32 |Marital_Status     |
|Mexcian           |34   |40 |Gender             |
|American          |42   |49 |Race_Ethnicity     |
|woman             |51   |55 |Gender             |
|financial problems|62   |79 |Financial_Status   |
|She               |82   |84 |Gender             |
|spanish           |93   |99 |Language           |
|She               |102  |104|Gender             |
|apartment         |118  |126|Housing            |
|She               |129  |131|Gender             |
|diabetes          |158  |165|Other_Disease      |
|hospitalizations  |233  |248|Other_SDoH_Keywords|
|cleaning assistant|307  |324|Employment         |
|health insurance  |354  |369|Insurance_Status   |
|She               |391  |393|Gender             |
|son               |401  |403|Family_Member      |
|student           |405  |411|Education          |
|college           |416  |422|Education          |
|depression        |454  |463|Mental_Health      |
|She               |466  |468|Gender             |
|she               |479  |481|Gender             |
|rehab             |489  |493|Access_To_Care     |
|her               |514  |516|Gender             |
|catholic faith    |518  |531|Spiritual_Beliefs  |
|support           |547  |553|Social_Support     |
|She               |565  |567|Gender             |
|etoh abuse        |589  |598|Alcohol            |
|her               |614  |616|Gender             |
|teens             |618  |622|Age                |
|She               |625  |627|Gender             |
|she               |637  |639|Gender             |
|daily             |652  |656|Substance_Frequency|
|drinker           |658  |664|Alcohol            |
|30 years          |670  |677|Substance_Duration |
|drinking          |694  |701|Alcohol            |
|beer              |703  |706|Alcohol            |
|daily             |708  |712|Substance_Frequency|
|She               |715  |717|Gender             |
|smokes            |719  |724|Smoking            |
|a pack            |726  |731|Substance_Quantity |
|cigarettes        |736  |745|Smoking            |
|a day             |747  |751|Substance_Frequency|
|She               |754  |756|Gender             |
|DUI               |762  |764|Legal_Issues       |
+------------------+-----+---+-------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_sdoh_emb_clinical_medium_wip|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|3.0 MB|
|Dependencies:|embeddings_clinical_medium|

## References

Internal SHOP Project

## Benchmarking

```bash
                  label  precision    recall  f1-score   support
      Geographic_Entity       0.89      0.88      0.88       106
                 Gender       0.99      0.99      0.99      4957
 Healthcare_Institution       0.98      0.96      0.97       776
             Employment       0.95      0.95      0.95      2120
         Access_To_Care       0.90      0.81      0.85       459
                 Income       0.79      0.79      0.79        29
         Social_Support       0.90      0.92      0.91       629
          Family_Member       0.97      0.99      0.98      2101
                    Age       0.94      0.93      0.94       436
          Mental_Health       0.89      0.86      0.87       479
                Alcohol       0.96      0.96      0.96       254
          Substance_Use       0.88      0.95      0.91       208
           Hypertension       0.96      1.00      0.98        24
          Other_Disease       0.90      0.94      0.92       583
             Disability       0.93      0.97      0.95        40
       Insurance_Status       0.87      0.85      0.86        85
         Transportation       0.82      0.96      0.89        53
     Sexual_Orientation       0.78      0.95      0.86        19
         Marital_Status       0.98      0.96      0.97        90
         Race_Ethnicity       0.92      0.96      0.94        25
      Spiritual_Beliefs       0.80      0.80      0.80        51
                Housing       0.89      0.85      0.87       366
              Education       0.87      0.86      0.86        70
    Other_SDoH_Keywords       0.78      0.88      0.83       237
               Language       0.87      0.77      0.82        26
    Substance_Frequency       0.92      0.83      0.87        65
           Legal_Issues       0.77      0.85      0.81        55
       Social_Exclusion       0.97      0.97      0.97        30
       Financial_Status       0.88      0.66      0.75       123
      Violence_Or_Abuse       0.82      0.65      0.73        57
     Substance_Quantity       0.88      0.93      0.90        56
                Smoking       0.99      0.99      0.99        71
       Population_Group       0.91      0.71      0.80        14
         Hyperlipidemia       0.78      1.00      0.88         7
       Community_Safety       0.98      1.00      0.99        47
               Exercise       0.91      0.88      0.90        60
        Food_Insecurity       1.00      1.00      1.00        29
        Eating_Disorder       0.67      0.92      0.77        13
        Quality_Of_Life       0.79      0.82      0.81        61
        Sexual_Activity       0.89      0.83      0.86        29
         Chidhood_Event       0.90      0.72      0.80        25
                   Diet       0.97      0.92      0.94        62
     Substance_Duration       0.66      0.95      0.78        39
Environmental_Condition       1.00      1.00      1.00        20
                Obesity       1.00      1.00      1.00        14
   Communicable_Disease       1.00      0.94      0.97        32
              micro-avg       0.95      0.95      0.95     15132
              macro-avg       0.89      0.90      0.89     15132
           weighted-avg       0.95      0.95      0.95     15132
```