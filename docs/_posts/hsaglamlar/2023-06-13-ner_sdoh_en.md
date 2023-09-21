---
layout: model
title: Social Determinants of Health
author: John Snow Labs
name: ner_sdoh
date: 2023-06-13
tags: [clinical, en, social_determinants, ner, public_health, sdoh, licensed]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.3
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

SDOH NER model is designed to detect and label social determinants of health (SDOH) entities within text data. Social determinants of health are crucial factors that influence individuals' health outcomes, encompassing various social, economic, and environmental element. 
The model has been trained using advanced machine learning techniques on a diverse range of text sources. The model can accurately recognize and classify a wide range of SDOH entities, including but not limited to factors such as socioeconomic status, education level, housing conditions, access to healthcare services, employment status, cultural and ethnic background, neighborhood characteristics, and environmental factors. The model's accuracy and precision have been carefully validated against expert-labeled data to ensure reliable and consistent results. Here are the labels of the SDOH NER model with their description:

- `Access_To_Care`: Patient’s ability or barriers to access the care needed. "long distances, access to health care, rehab program, etc."
- `Age`: All mention of ages including "Newborn, Infant, Child, Teenager, Teenage, Adult, etc."
- `Alcohol`: Mentions of alcohol drinking habit.
- `Chidhood_Event`: Childhood events mentioned by the patient. "childhood trauma, childhood abuse, etc."
- `Communicable_Disease`: Include all the communicable diseases. "HIV, hepatitis, tuberculosis, sexually transmitted diseases, etc."
- `Community_Safety`: safety of the neighborhood or places of study or work. "dangerous neighborhood, safe area, etc."
- `Diet`: Information regarding the patient’s dietary habits. "vegetarian, vegan, healthy foods, low-calorie diet, etc."
- `Disability`: Mentions related to disability
- `Eating_Disorder`: This entity is used to extract eating disorders. "anorexia, bulimia, pica, etc."
- `Education`:Patient’s educational background
- `Employment`: Patient or provider occupational titles.
- `Environmental_Condition`: Conditions of the environment where people live. "pollution, air quality, noisy environment, etc."
- `Exercise`: Mentions of the exercise habits of a patient. "exercise, physical activity, play football, go to the gym, etc."
- `Family_Member`: Nouns that refer to a family member. "mother, father, brother, sister, etc."
- `Financial_Status`: Financial status refers to the state and condition of the person’s finances. "financial decline, debt, bankruptcy, etc."
- `Food_Insecurity`: Food insecurity is defined as a lack of consistent access to enough food for every person in a household to live an active, healthy life. "food insecurity, scarcity of protein, lack of food, etc."
- `Gender`: Gender-specific nouns and pronouns
- `Geographic_Entity`: Geographical location refers to a specific physical point on Earth. 
- `Healthcare_Institution`:  Health care institution means every place, institution, building or agency. "hospital, clinic, trauma centers, etc."
- `Housing`: Conditions of the patient’s living spaces. "homeless, housing, small apartment, etc."
- `Hyperlipidemia`: Terms that indicate hyperlipidemia and relevant subtypes. "hyperlipidemia, hypercholesterolemia, elevated cholesterol, etc."
- `Hypertension`: Terms related to hypertension. "hypertension, high blood pressure, etc."
- `Income`: Information regarding the patient’s income
- `Insurance_Status`: Information regarding the patient’s insurance status. "uninsured, insured, Medicare, Medicaid, etc."
- `Language`: A system of conventional spoken, manual (signed) or written symbols by means of which human beings express themselves. "English, Spanish-speaking, bilingual, etc. "
- `Legal_Issues`: Issues that have legal implications. "legal issues, legal problems, detention , in prison, etc."
- `Marital_Status`: Terms that indicate the person’s marital status.
- `Mental_Health`: Include all the mental, neurodegenerative and neurodevelopmental diagnosis, disorders, conditions or syndromes mentioned. "depression, anxiety, bipolar disorder, psychosis, etc."
- `Obesity`: Terms related to the patient being obese. "obesity, overweight, etc."
- `Other_Disease`: Include all the diseases mentioned. "psoriasis, thromboembolism, etc." 
- `Other_SDoH_Keywords`: This label is used to annotated terms or sentences that provide information about social determinants of health that are not already extracted under any other entity label. "minimal activities of daily living, ack of government programs, etc."
- `Population_Group`: The population group that a person belongs to, that does not fall under any other entities. "refugee, prison patient, etc."
- `Quality_Of_Life`: Quality of life refers to how an individual feels about their current station in life. " lower quality of life, profoundly impact his quality of life, etc."
- `Race_Ethnicity`: The race and ethnicity categories include racial, ethnic, and national origins.
- `Sexual_Activity`: Mentions of patient’s sexual behaviors. "monogamous, sexual activity, inconsistent condom use, etc."
- `Sexual_Orientation`:  Terms that are related to sexual orientations. "gay, bisexual, heterosexual, etc."
- `Smoking`: mentions of smoking habit. "smoking, cigarette, tobacco, etc."
- `Social_Exclusion`: Absence or lack of rights or accessibility to services or goods that are expected of the majority of the population. "social exclusion, social isolation, gender discrimination, etc."
- `Social_Support`: he presence of friends, family or other people to turn to for comfort or help.  "social support, live with family, etc."
- `Spiritual_Beliefs`: Spirituality is concerned with beliefs beyond self, usually related to the existence of a superior being. "spiritual beliefs, religious beliefs, strong believer, etc."
- `Substance_Duration`: The duration associated with the health behaviors. "for 2 years, 3 months, etc"
- `Substance_Frequency`: The frequency associated with the health behaviors. "five days a week, daily, weekly, monthly, etc"
- `Substance_Quantity`: The quantity associated with the health behaviors. "2 packs , 40 ounces,ten to twelve, modarate, etc"
- `Substance_Use`: Mentions of illegal recreational drugs use. Include also substances that can create dependency including here caffeine and tea.  "overdose, cocaine, illicit substance intoxication, coffee etc."
- `Transportation`: mentions of accessibility to transportation means. "car, bus, train, etc."
- `Violence_Or_Abuse`: Episodes of abuse or violence experienced and reported by the patient. "domestic violence, sexual abuse, etc."

## Predicted Entities

`Access_To_Care`, `Age`, `Alcohol`, `Chidhood_Event`, `Communicable_Disease`, `Community_Safety`, `Diet`, `Disability`, `Eating_Disorder`, `Education`, `Employment`, `Environmental_Condition`, `Exercise`, `Family_Member`, `Financial_Status`, `Food_Insecurity`, `Gender`, `Geographic_Entity`, `Healthcare_Institution`, `Housing`, `Hyperlipidemia`, `Hypertension`, `Income`, `Insurance_Status`, `Language`, `Legal_Issues`, `Marital_Status`, `Mental_Health`, `Obesity`, `Other_Disease`, `Other_SDoH_Keywords`, `Population_Group`, `Quality_Of_Life`, `Race_Ethnicity`, `Sexual_Activity`, `Sexual_Orientation`, `Smoking`, `Social_Exclusion`, `Social_Support`, `Spiritual_Beliefs`, `Substance_Duration`, `Substance_Frequency`, `Substance_Quantity`, `Substance_Use`, `Transportation`, `Violence_Or_Abuse`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/27.0.Social_Determinant_of_Health_Models.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_en_4.4.3_3.0_1686654976160.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_en_4.4.3_3.0_1686654976160.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained("ner_sdoh", "en", "clinical/models")\
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

val ner_model = MedicalNerModel.pretrained("ner_sdoh", "en", "clinical/models")
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

val data = Seq("""Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She speaks Spanish and Portuguese. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. She has a son, a student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reports having her catholic faith as a means of support as well.  She has a long history of etoh abuse, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day. She had DUI in April and was due to court this week.""").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------+-----+---+-------------------+
|chunk             |begin|end|ner_label          |
+------------------+-----+---+-------------------+
|55 years old      |9    |20 |Age                |
|New York          |33   |40 |Geographic_Entity  |
|divorced          |45   |52 |Marital_Status     |
|Mexcian American  |54   |69 |Race_Ethnicity     |
|woman             |71   |75 |Gender             |
|financial problems|82   |99 |Financial_Status   |
|She               |102  |104|Gender             |
|Spanish           |113  |119|Language           |
|Portuguese        |125  |134|Language           |
|She               |137  |139|Gender             |
|apartment         |153  |161|Housing            |
|She               |164  |166|Gender             |
|diabetes          |193  |200|Other_Disease      |
|hospitalizations  |268  |283|Other_SDoH_Keywords|
|cleaning assistant|342  |359|Employment         |
|health insurance  |379  |394|Insurance_Status   |
|She               |416  |418|Gender             |
|son               |426  |428|Family_Member      |
|student           |433  |439|Education          |
|college           |444  |450|Education          |
|depression        |482  |491|Mental_Health      |
|She               |494  |496|Gender             |
|she               |507  |509|Gender             |
|rehab             |517  |521|Access_To_Care     |
|her               |542  |544|Gender             |
|catholic faith    |546  |559|Spiritual_Beliefs  |
|support           |575  |581|Social_Support     |
|She               |593  |595|Gender             |
|etoh abuse        |619  |628|Alcohol            |
|her               |644  |646|Gender             |
|teens             |648  |652|Age                |
|She               |655  |657|Gender             |
|she               |667  |669|Gender             |
|daily             |682  |686|Substance_Frequency|
|drinker           |688  |694|Alcohol            |
|30 years          |700  |707|Substance_Duration |
|drinking          |724  |731|Alcohol            |
|beer              |733  |736|Alcohol            |
|daily             |738  |742|Substance_Frequency|
|She               |745  |747|Gender             |
|smokes            |749  |754|Smoking            |
|a pack            |756  |761|Substance_Quantity |
|cigarettes        |766  |775|Smoking            |
|a day             |777  |781|Substance_Frequency|
|She               |784  |786|Gender             |
|DUI               |792  |794|Legal_Issues       |
+------------------+-----+---+-------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_sdoh|
|Compatibility:|Healthcare NLP 4.4.3+|
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
                  label   precision    recall  f1-score   support
         Access_To_Care       0.88      0.88      0.88       544
                    Age       0.93      0.95      0.94       466
                Alcohol       0.96      0.98      0.97       263
         Chidhood_Event       1.00      0.53      0.69        19
   Communicable_Disease       0.96      1.00      0.98        51
       Community_Safety       0.95      0.85      0.89        65
                   Diet       0.89      0.75      0.82        89
             Disability       0.93      0.97      0.95        38
        Eating_Disorder       0.95      0.91      0.93        44
              Education       0.89      0.94      0.91        67
             Employment       0.94      0.95      0.95      2087
Environmental_Condition       0.95      1.00      0.97        18
               Exercise       0.90      0.86      0.88        65
          Family_Member       0.98      0.98      0.98      2061
       Financial_Status       0.73      0.77      0.75       116
        Food_Insecurity       0.81      0.88      0.84        43
                 Gender       0.99      0.98      0.98      4858
      Geographic_Entity       0.95      0.84      0.89       106
 Healthcare_Institution       0.94      0.98      0.96       721
                Housing       0.93      0.88      0.90       369
         Hyperlipidemia       0.86      0.60      0.71        10
           Hypertension       0.88      0.77      0.82        30
                 Income       0.82      0.75      0.79        61
       Insurance_Status       0.89      0.82      0.85        66
               Language       0.96      0.92      0.94        26
           Legal_Issues       0.89      0.79      0.84        63
         Marital_Status       0.96      1.00      0.98        90
          Mental_Health       0.87      0.85      0.86       491
                Obesity       0.85      1.00      0.92        11
          Other_Disease       0.90      0.89      0.90       609
    Other_SDoH_Keywords       0.81      0.85      0.83       258
       Population_Group       1.00      0.86      0.92        14
        Quality_Of_Life       0.61      0.86      0.72        44
         Race_Ethnicity       0.97      0.90      0.94        41
        Sexual_Activity       0.78      0.84      0.81        45
     Sexual_Orientation       0.80      1.00      0.89        12
                Smoking       0.99      0.97      0.98        76
       Social_Exclusion       0.88      0.88      0.88        25
         Social_Support       0.87      0.95      0.91       676
      Spiritual_Beliefs       0.83      0.83      0.83        53
     Substance_Duration       0.78      0.69      0.73        52
    Substance_Frequency       0.52      0.83      0.64        46
     Substance_Quantity       0.82      0.88      0.85        51
          Substance_Use       0.91      0.97      0.94       207
         Transportation       0.85      0.83      0.84        42
      Violence_Or_Abuse       0.87      0.70      0.77       112
              micro-avg       0.94      0.94      0.94     15301
              macro-avg       0.88      0.87      0.87     15301
           weighted-avg       0.94      0.94      0.94     15301
```
