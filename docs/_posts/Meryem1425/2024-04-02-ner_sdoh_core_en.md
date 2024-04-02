---
layout: model
title: Social Determinants of Health - Core
author: John Snow Labs
name: ner_sdoh_core
date: 2024-04-02
tags: [licensed, en, clinical, ner, social_determinants, public_health, sdoh, core]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

SDOH NER model is designed to detect and label social determinants of health (SDOH) entities within text data. Social determinants of health are crucial factors that influence individuals’ health outcomes, encompassing various social, economic, and environmental element. The model has been trained using advanced machine learning techniques on a diverse range of text sources. The model can accurately recognize and classify a wide range of SDOH entities, including but not limited to factors such as socioeconomic status, education level, housing conditions, access to healthcare services, employment status, cultural and ethnic background, neighborhood characteristics, and environmental factors. The model’s accuracy and precision have been carefully validated against expert-labeled data to ensure reliable and consistent results. Here are the labels of the SDOH NER model with their description:

- `Access_To_Care` : Patient’s ability or barriers to access the care needed. "long distances, access to health care, rehab program, etc."
- `Chidhood_Event` : Childhood events mentioned by the patient. “childhood trauma, childhood abuse, etc.”
- `Community_Safety` : safety of the neighborhood or places of study or work. “dangerous neighborhood, safe area, etc.”
- `Disability` : Mentions related to disability
- `Eating_Disorder` : This entity is used to extract eating disorders. “anorexia, bulimia, pica, etc.”
- `Education` : Patient’s educational background
- `Environmental_Condition` : Conditions of the environment where people live. “pollution, air quality, noisy environment, etc.”
- `Exercise` : Mentions of the exercise habits of a patient. “exercise, physical activity, play football, go to the gym, etc.”
- `Family_Member` : Nouns that refer to a family member. “mother, father, brother, sister, etc.”
- `Financial_Status` : Financial status refers to the state and condition of the person’s finances. “financial decline, debt, bankruptcy, etc.”
- `Food_Insecurity` : Food insecurity is defined as a lack of consistent access to enough food for every person in a household to live an active, healthy life. “food insecurity, scarcity of protein, lack of food, etc.”
- `Geographic_Entity` : Geographical location refers to a specific physical point on Earth.
- `Healthcare_Institution` : Health care institution means every place, institution, building or agency. “hospital, clinic, trauma centers, etc.”
- `Housing` : Conditions of the patient’s living spaces. “homeless, housing, small apartment, etc.”
- `Income` : Information regarding the patient’s income
- `Insurance_Status` : Information regarding the patient’s insurance status. “uninsured, insured, Medicare, Medicaid, etc.”
- `Legal_Issues` : Issues that have legal implications. “legal issues, legal problems, detention , in prison, etc.”
- `Mental_Health` : Include all the mental, neurodegenerative and neurodevelopmental diagnosis, disorders, conditions or syndromes mentioned. “depression, anxiety, bipolar disorder, psychosis, etc.”
- `Other_SDoH_Keywords` : This label is used to annotated terms or sentences that provide information about social determinants of health that are not already extracted under any other entity label. “minimal activities of daily living, ack of government programs, etc.”
- `Population_Group` : The population group that a person belongs to, that does not fall under any other entities. “refugee, prison patient, etc.”
- `Quality_Of_Life` : Quality of life refers to how an individual feels about their current station in life. “ lower quality of life, profoundly impact his quality of life, etc.”
- `Social_Exclusion` : Absence or lack of rights or accessibility to services or goods that are expected of the majority of the population. “social exclusion, social isolation, gender discrimination, etc.”
- `Social_Support` : he presence of friends, family or other people to turn to for comfort or help. “social support, live with family, etc.”
- `Spiritual_Beliefs`: Spirituality is concerned with beliefs beyond self, usually related to the existence of a superior being. “spiritual beliefs, religious beliefs, strong believer, etc.”
- `Substance_Duration` : The duration associated with the health behaviors. “for 2 years, 3 months, etc”
- `Substance_Frequency` : The frequency associated with the health behaviors. “five days a week, daily, weekly, monthly, etc”
- `Substance_Quantity` : The quantity associated with the health behaviors. “2 packs , 40 ounces,ten to twelve, modarate, etc”
- `Substance_Use` : Mentions of illegal recreational drugs use. Include also substances that can create dependency including here caffeine and tea. “overdose, cocaine, illicit substance intoxication, coffee etc.”
- `Transportation` : mentions of accessibility to transportation means. “car, bus, train, etc.”
- `Violence_Or_Abuse` : Episodes of abuse or violence experienced and reported by the patient. “domestic violence, sexual abuse, etc.”

## Predicted Entities

`Access_To_Care`, `Chidhood_Event`, `Community_Safety`, `Disability`, `Eating_Disorder`, `Education`, `Environmental_Condition`, `Exercise`, `Family_Member`, `Financial_Status`, `Food_Insecurity`, `Geographic_Entity`, `Healthcare_Institution`, `Housing`, `Income`, `Insurance_Status`, `Legal_Issues`, `Mental_Health`, `Other_SDoH_Keywords`, `Population_Group`, `Quality_Of_Life`, `Social_Exclusion`, `Social_Support`, `Spiritual_Beliefs`, `Substance_Duration`, `Substance_Frequency`, `Substance_Quantity`, `Substance_Use`, `Transportation`, `Violence_Or_Abuse`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/27.0.Social_Determinant_of_Health_Models.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_core_en_5.3.0_3.0_1712027554627.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_core_en_5.3.0_3.0_1712027554627.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_sdoh_core", "en", "clinical/models")\
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


sample_texts = [["""Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She speaks Spanish and Portuguese. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. She has a son, a student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reports having her catholic faith as a means of support as well.  She has a long history of etoh abuse, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day. She had DUI in April and was due to court this week."""]]
             
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

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_sdoh_core", "en", "clinical/models")
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


val data = Seq("""Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She speaks Spanish and Portuguese. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. She has a son, a student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reports having her catholic faith as a means of support as well.  She has a long history of etoh abuse, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day. She had DUI in April and was due to court this week.""").toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------+-----+---+-------------------+
|chunk                  |begin|end|label              |
+-----------------------+-----+---+-------------------+
|New York               |33   |40 |Geographic_Entity  |
|financial problems     |82   |99 |Financial_Status   |
|apartment              |153  |161|Housing            |
|hospitalizations       |268  |283|Other_SDoH_Keywords|
|access health insurance|372  |394|Insurance_Status   |
|son                    |426  |428|Family_Member      |
|student                |433  |439|Education          |
|college                |444  |450|Education          |
|depression             |482  |491|Mental_Health      |
|rehab                  |517  |521|Access_To_Care     |
|catholic faith         |546  |559|Spiritual_Beliefs  |
|support                |575  |581|Social_Support     |
|daily                  |682  |686|Substance_Frequency|
|30 years               |700  |707|Substance_Duration |
|daily                  |738  |742|Substance_Frequency|
|a pack                 |756  |761|Substance_Quantity |
|a day                  |777  |781|Substance_Frequency|
|DUI                    |792  |794|Legal_Issues       |
+-----------------------+-----+---+-------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_sdoh_core|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|5.0 MB|

## Benchmarking

```bash
                  label  precision    recall  f1-score   support
         Access_To_Care       0.90      0.84      0.87      1293
        Childhood_Event       0.89      0.74      0.81        34
       Community_Safety       0.85      0.85      0.85       143
             Disability       0.89      0.94      0.91       100
        Eating_Disorder       0.89      1.00      0.94        62
              Education       0.84      0.81      0.82       224
Environmental_Condition       0.85      0.82      0.84        40
               Exercise       0.91      0.90      0.91       195
          Family_Member       0.98      0.98      0.98      4244
       Financial_Status       0.87      0.69      0.77       232
        Food_Insecurity       0.98      0.91      0.95        67
      Geographic_Entity       0.79      0.89      0.84       370
 Healthcare_Institution       0.96      0.95      0.96      1865
                Housing       0.92      0.84      0.88       820
                 Income       0.94      0.85      0.89        79
       Insurance_Status       0.90      0.76      0.83       148
           Legal_Issues       0.80      0.80      0.80       287
          Mental_Health       0.91      0.90      0.91      2023
    Other_SDoH_Keywords       0.83      0.88      0.85       609
       Population_Group       0.95      0.84      0.89       120
        Quality_Of_Life       0.92      0.96      0.94       114
       Social_Exclusion       0.97      0.89      0.93        63
         Social_Support       0.91      0.95      0.93      1298
      Spiritual_Beliefs       0.93      0.91      0.92       151
     Substance_Duration       0.79      0.83      0.81       279
    Substance_Frequency       0.75      0.72      0.73       480
     Substance_Quantity       0.65      0.69      0.67       372
          Substance_Use       0.92      0.96      0.94      1007
         Transportation       0.96      0.87      0.91       239
      Violence_Or_Abuse       0.92      0.79      0.85       466
              micro-avg       0.91      0.90      0.91     17424
              macro-avg       0.89      0.86      0.87     17424
           weighted-avg       0.91      0.90      0.91     17424
```
