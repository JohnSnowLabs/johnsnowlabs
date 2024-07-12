---
layout: model
title: Social Determinants of Health (clinical_large)
author: John Snow Labs
name: ner_sdoh_emb_clinical_large_wip
date: 2023-04-17
tags: [en, clinical_large, social_determinants, public_health, ner, sdoh, pyspark_30, licensed]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.0
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
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/27.0.Social_Determinant_of_Health_Models.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_emb_clinical_large_wip_en_4.3.2_3.0_1681756284245.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_emb_clinical_large_wip_en_4.3.2_3.0_1681756284245.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_large", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_sdoh_emb_clinical_large_wip", "en", "clinical/models")\
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

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_large", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("c", "en", "clinical/models")
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
|Mexcian           |34   |40 |Race_Ethnicity     |
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
|daily             |652  |656|Substance_Quantity |
|drinker           |658  |664|Alcohol            |
|30 years          |670  |677|Substance_Duration |
|drinking beer     |694  |706|Alcohol            |
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
|Model Name:|ner_sdoh_emb_clinical_large_wip|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|3.0 MB|
|Dependencies:|embeddings_clinical_large|

## References

Internal SHOP Project

## Benchmarking

```bash
                  label  precision    recall  f1-score   support
             Employment       0.94      0.96      0.95      2075
         Social_Support       0.91      0.90      0.90       658
    Other_SDoH_Keywords       0.82      0.87      0.85       259
 Healthcare_Institution       0.99      0.95      0.97       781
                Alcohol       0.96      0.97      0.96       258
                 Gender       0.99      0.99      0.99      4957
          Other_Disease       0.89      0.94      0.91       583
         Access_To_Care       0.86      0.88      0.87       520
          Mental_Health       0.89      0.81      0.85       494
                    Age       0.92      0.96      0.94       433
         Marital_Status       1.00      1.00      1.00        92
     Substance_Quantity       0.88      0.86      0.87        58
          Substance_Use       0.91      0.97      0.94       192
          Family_Member       0.97      0.99      0.98      2094
       Financial_Status       0.86      0.65      0.74       124
         Race_Ethnicity       0.93      0.93      0.93        27
       Insurance_Status       0.93      0.87      0.90        85
      Spiritual_Beliefs       0.86      0.81      0.83        52
                Housing       0.88      0.85      0.87       400
      Geographic_Entity       0.86      0.88      0.87       113
             Disability       0.93      0.93      0.93        44
        Quality_Of_Life       0.89      0.75      0.81        67
                 Income       0.89      0.77      0.83        31
              Education       0.85      0.88      0.86        58
         Transportation       0.86      0.89      0.88        57
           Legal_Issues       0.72      0.91      0.80        47
                Smoking       0.98      0.97      0.98        66
    Substance_Frequency       0.93      0.75      0.83        57
           Hypertension       1.00      1.00      1.00        21
      Violence_Or_Abuse       0.83      0.62      0.71        63
               Exercise       0.96      0.88      0.92        57
                   Diet       0.95      0.87      0.91        70
     Sexual_Orientation       0.68      1.00      0.81        13
               Language       0.89      0.73      0.80        22
       Social_Exclusion       0.96      0.90      0.93        29
     Substance_Duration       0.75      0.85      0.80        39
   Communicable_Disease       1.00      0.84      0.91        31
         Chidhood_Event       0.88      0.61      0.72        23
       Community_Safety       0.95      0.93      0.94        44
       Population_Group       0.89      0.62      0.73        13
         Hyperlipidemia       0.78      1.00      0.88         7
        Food_Insecurity       1.00      0.93      0.96        29
        Eating_Disorder       0.67      0.92      0.77        13
        Sexual_Activity       0.84      0.90      0.87        29
Environmental_Condition       1.00      1.00      1.00        20
                Obesity       1.00      1.00      1.00        12
              micro-avg       0.95      0.95      0.95     15217
              macro-avg       0.90      0.88      0.88     15217
           weighted-avg       0.95      0.95      0.95     15217

```
