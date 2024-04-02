---
layout: model
title: Social Determinants of Health - Core (MedicalBertForTokenClassifier)
author: John Snow Labs
name: bert_token_classifier_ner_sdoh_core
date: 2024-04-02
tags: [bertfortokenclassification, ner, clinical, en, licensed, sdoh, social_determinants, public_health, tensorflow]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalBertForTokenClassifier
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_sdoh_core_en_5.3.0_3.0_1712032149223.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_sdoh_core_en_5.3.0_3.0_1712032149223.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence = SentenceDetectorDLModel\
    .pretrained("sentence_detector_dl_healthcare","en","clinical/models") \
    .setInputCols(['document'])\
    .setOutputCol('sentence')\

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

tokenClassifier = MedicalBertForTokenClassifier.pretrained("bert_token_classifier_ner_sdoh_core", "en", "clinical/models")\
  .setInputCols("token", "sentence")\
  .setOutputCol("ner")\

ner_model_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

ner_pipeline = Pipeline(
    stages = [
        document,
        sentence,
        tokenizer,
        tokenClassifier,
        ner_model_converter       
    ])

sample_texts = [["""Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She speaks Spanish and Portuguese. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. She has a son, a student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reports having her catholic faith as a means of support as well.  She has a long history of etoh abuse, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day. She had DUI in April and was due to court this week."""]]
             
data = spark.createDataFrame(sample_texts).toDF("text")

result = ner_pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val tokenClassifier = MedicalBertForTokenClassifier.pretrained("bert_token_classifier_ner_sdoh_core", "en", "clinical/models")
  .setInputCols(Array("token", "sentence"))
  .setOutputCol("ner")

val ner_model_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
        document,
        sentence,
        tokenizer,
        tokenClassifier,
        ner_model_converter       
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
+-----------------------+-----+---+-------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_sdoh_core|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|404.6 MB|
|Case sensitive:|false|
|Max sentence length:|512|

## Benchmarking

```bash
                  label  precision    recall  f1-score   support
         Access_To_Care       0.76      0.78      0.77       610
        Childhood_Event       0.86      0.63      0.73        19
       Community_Safety       0.68      0.74      0.71        62
             Disability       0.90      0.93      0.91        96
        Eating_Disorder       0.85      0.89      0.87        37
              Education       0.70      0.72      0.71       159
Environmental_Condition       0.87      0.72      0.79        18
               Exercise       0.90      0.92      0.91       151
          Family_Member       0.95      0.98      0.97      4174
       Financial_Status       0.73      0.72      0.73       116
        Food_Insecurity       0.84      0.89      0.86        36
      Geographic_Entity       0.54      0.05      0.09       301
 Healthcare_Institution       0.97      0.86      0.91      1630
                Housing       0.81      0.76      0.78       392
                 Income       0.83      0.36      0.50        56
       Insurance_Status       0.77      0.63      0.69        98
           Legal_Issues       0.62      0.66      0.64       179
          Mental_Health       0.82      0.80      0.81      1436
    Other_SDoH_Keywords       0.76      0.81      0.79       521
       Population_Group       0.81      0.77      0.79        93
        Quality_Of_Life       0.90      0.47      0.62        55
       Social_Exclusion       0.89      0.84      0.86        49
         Social_Support       0.84      0.88      0.86       953
      Spiritual_Beliefs       0.83      0.80      0.82       107
     Substance_Duration       0.55      0.68      0.60       105
    Substance_Frequency       0.57      0.87      0.68       275
     Substance_Quantity       0.48      0.72      0.58       223
          Substance_Use       0.83      0.85      0.84       655
         Transportation       0.73      0.79      0.76       160
      Violence_Or_Abuse       0.77      0.79      0.78       287
              micro-avg       0.85      0.85      0.85     13053
              macro-avg       0.75      0.72      0.72     13053
           weighted-avg       0.85      0.85      0.84     13053
```