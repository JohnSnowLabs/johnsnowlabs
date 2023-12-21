---
layout: model
title: Text Classification For Disability (mpnet)
author: John Snow Labs
name: genericclassifier_disability_mpnet
date: 2023-12-21
tags: [disability, classifier, genericclassifier, mpnet, en, licensed]
task: Text Classification
language: en
edition: Healthcare NLP 5.1.4
spark_version: 3.0
supported: true
annotator: GenericClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The PHS-BERT Disability Classifier Model is an advanced text classification tool designed to discern and categorize text based on the context of disability. This model differentiates between mentions of `Disabled` and `Non-Disabled` conditions, aiding in the understanding and analysis of textual data related to disability status. Here's more detailed information about the classes: 

`Disabled`: This classification captures textual references that explicitly or implicitly pertain to a disability. Disability, in this context, refers to a condition (physical, mental, cognitive, or developmental) that substantially limits one or more major life activities. Example: "Since my injury, I've been using a wheelchair, adapting to my new disabled status."

`Non-Disabled`: Texts classified under this category refer to contexts where disability is not a present factor. This includes scenarios where individuals are described as not requiring any special accommodations due to the absence of a disability. Example: "As a non-disabled person, I can easily navigate through the city's streets and public transportation without needing additional assistance."

## Predicted Entities

`Other/Unknown`, `Non-disabled`, `Disabled`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/genericclassifier_disability_mpnet_en_5.1.4_3.0_1703176028787.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/genericclassifier_disability_mpnet_en_5.1.4_3.0_1703176028787.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
        
embeddings = MPNetEmbeddings.pretrained("mpnet_embedding_mpnet_base","en") \
    .setInputCols(["document"]) \
    .setOutputCol("mpnet_embeddings")

features_asm = FeaturesAssembler()\
    .setInputCols(["mpnet_embeddings"])\
    .setOutputCol("features")

generic_classifier = GenericClassifierModel.pretrained("genericclassifier_disability_mpnet", "en", "clinical/models")\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

pipeline = Pipeline(stages=[
    document_assembler,
    embeddings,
    features_asm,
    generic_classifier    
])


text_list = ["""Name: Fatima Williams
Age: 17 years old
Gender: Female
Race: Black
Employment Status: Unemployed
Relationship Status: Single
Sexual Orientation: Prefers not to disclose the information
Religion: Islam
BMI: Underweight
Unhealthy Habits: Prefers not to disclose the information
Socioeconomic Status: Low class
Area of Residence: Rural
Disability Status: Disabled

Discharge Summary:
Fatima is a 17-year-old Muslim teen who presented to the clinic with recurring headaches and joint pain. Her medical history reveals a persistent struggle with being underweight and a disability that limits her physical activities. Fatima resides in a rural area, where access to consistent medical care and nutritious food is challenging due to her low socioeconomic status.

Upon evaluation, Fatima's physical examination and laboratory tests revealed nutritional deficiencies and signs of chronic pain linked to her underweight status and physical disability. Her living situation as a single, unemployed teen in a rural setting has compounded her health challenges, making it difficult for her to maintain a stable health condition.

During her hospital stay, Fatima received nutritional supplements and was enrolled in a pain management program tailored to her specific needs. Social workers were also involved to provide guidance on accessing community resources and support systems available to individuals in her situation.

At the time of discharge, a comprehensive care plan was established. This included regular outpatient follow-ups, a diet plan enriched with necessary nutrients, and continued engagement with social services to address her socioeconomic challenges. Fatima was also encouraged to participate in community support groups for young individuals with similar backgrounds and challenges.

In summary, Fatima's case highlights the intricate interplay of health, socioeconomic status, and living conditions in the management of teen patients. It underscores the need for holistic care approaches that address not just the medical but also the social aspects of health, especially in rural settings.""",
    
    """Name: Shirley Myers
Gender: Female
Age: 95 years old (Old Adult)
Race: White/Caucasian
Employment Status: Retired
Relationship Status: Married
Sexual Orientation: Heterosexual
Religion: Christianity
BMI: Healthy weight
Unhealthy Habits: Prefers not to disclose
Socioeconomic Status: Middle class
Area of Residence: Urban
Disability Status: Non-disabled

Discharge Summary:

Shirley Myers, a 95-year-old (Old Adult) White/Caucasian female, resides in an urban area with her husband. She has a history of hypertension and a recent diagnosis of glaucoma. Shirley visited our clinic for her regular hypertension check-up and a glaucoma evaluation.

Her hypertension is managed with a diuretic (Hydrochlorothiazide) and lifestyle modifications, such as a low-sodium diet and regular exercise. For her glaucoma, she recently started using eye drops (Latanoprost). During her visit, Shirley was cooperative and in good health. Her blood pressure was well-controlled at 126/79 mmHg. An ophthalmologic examination confirmed the early stages of glaucoma, with no significant vision impairment.

Laboratory tests included a complete blood count and renal function tests to monitor the effects of her hypertension medication. Her tests indicated effective management of hypertension with no signs of renal impairment. Her lipid profile was also checked, showing good cholesterol levels.

The care plan for Shirley includes the continuation of her hypertension medication and close monitoring of her glaucoma. She was advised to maintain her low-sodium diet and to use her glaucoma eye drops as prescribed. Regular eye examinations were scheduled to monitor the progression of her glaucoma.

Shirley was scheduled for a follow-up appointment in four months to reassess her hypertension and glaucoma. She was discharged with instructions to adhere to her medication regimen and to maintain a healthy lifestyle. The importance of regular medical check-ups was emphasized to manage her health conditions effectively.""",
    
    """This medical summary pertains to a 38-year-old female patient who presented for an annual physical examination. The patient's medical history, symptoms, and recent concerns are detailed below.

F, 38 yo, Asian, employed FT as a graphic designer, single, no children. Political leanings: liberal. Union membership: no. Sexual orientation: bisexual. Religion: Buddhist. HT: 5'4" (162 cm), WT: 130 lbs (59 kg), BMI: 22.3 (normal). Unhealthy habits: irregular sleep pattern, high-stress lifestyle.

Med hx:

Hypothyroidism, managed w/ Levothyroxine 75 mcg qd, regular monitoring of TSH levels (current TSH: 2.5 mIU/L).
Migraine, managed w/ prophylactic Topiramate 100 mg qd, Triptan (Sumatriptan 100 mg) prn for acute attacks.
Derm:

Atopic dermatitis, managed w/ topical corticosteroids (Hydrocortisone 1% cream bid), emollients, and avoiding irritants.
Ortho:

Lateral epicondylitis (tennis elbow) in L arm, managed w/ NSAIDs (Ibuprofen 400 mg tid prn), PT, activity modification, and counterforce bracing.
Past proc.:

LASIK surgery (5 yrs ago) to correct myopia.
Recent concerns:

Frequent UTIs in the past year. Urinalysis and culture positive for E. coli. Completed antibiotic course (Nitrofurantoin 100 mg bid for 5 days). Referred to urologist for further evaluation.
Labs:

CBC: Hb 13.8 g/dL, Hct 40%, WBC 5.8 K/uL, Plt 230 K/uL.
CMP: Na 139 mEq/L, K 4.2 mEq/L, Cl 101 mEq/L, CO2 27 mEq/L, BUN 13 mg/dL, Cr 0.8 mg/dL, Glu 90 mg/dL, TP 6.9 g/dL, Alb 4.2 g/dL, AST 20 U/L, ALT 15 U/L, Alk Phos 68 U/L, Ca 9.5 mg/dL, Tbil 0.7 mg/dL.
Cardiovascular hx: no h/o CAD, MI, or stroke, but family hx of CAD. Lipid panel: TC 190 mg/dL, LDL 115 mg/dL, HDL 60 mg/dL, TG 100 mg/dL. Encouraged to maintain a heart-healthy lifestyle through balanced nutrition and regular exercise.

Allergies: Penicillin, causing rash. Current tx plan: routine check-ups, medications as needed, healthy lifestyle w/ regular exercise, balanced nutrition, stress reduction techniques (e.g., yoga, mindfulness meditation).
"""]


df = spark.createDataFrame(text_list, StringType()).toDF("text")
result = pipeline.fit(df).transform(df)

result.select("text", "prediction.result").show(truncate=100)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
        
val embeddings = MPNetEmbeddings.pretrained("mpnet_embedding_mpnet_base","en")
    .setInputCols("document")
    .setOutputCol("mpnet_embeddings")

val features_asm = new FeaturesAssembler()
    .setInputCols("mpnet_embeddings")
    .setOutputCol("features")

val generic_classifier = GenericClassifierModel.pretrained("genericclassifier_disability_mpnet", "en", "clinical/models")
    .setInputCols("features")
    .setOutputCol("prediction")

val pipeline = new PipelineModel().setStages(Array(
    document_assembler,
    embeddings,
    features_asm,
    generic_classifier    
))


val data = Seq(Array("""Name: Fatima Williams
Age: 17 years old
Gender: Female
Race: Black
Employment Status: Unemployed
Relationship Status: Single
Sexual Orientation: Prefers not to disclose the information
Religion: Islam
BMI: Underweight
Unhealthy Habits: Prefers not to disclose the information
Socioeconomic Status: Low class
Area of Residence: Rural
Disability Status: Disabled

Discharge Summary:
Fatima is a 17-year-old Muslim teen who presented to the clinic with recurring headaches and joint pain. Her medical history reveals a persistent struggle with being underweight and a disability that limits her physical activities. Fatima resides in a rural area, where access to consistent medical care and nutritious food is challenging due to her low socioeconomic status.

Upon evaluation, Fatima's physical examination and laboratory tests revealed nutritional deficiencies and signs of chronic pain linked to her underweight status and physical disability. Her living situation as a single, unemployed teen in a rural setting has compounded her health challenges, making it difficult for her to maintain a stable health condition.

During her hospital stay, Fatima received nutritional supplements and was enrolled in a pain management program tailored to her specific needs. Social workers were also involved to provide guidance on accessing community resources and support systems available to individuals in her situation.

At the time of discharge, a comprehensive care plan was established. This included regular outpatient follow-ups, a diet plan enriched with necessary nutrients, and continued engagement with social services to address her socioeconomic challenges. Fatima was also encouraged to participate in community support groups for young individuals with similar backgrounds and challenges.

In summary, Fatima's case highlights the intricate interplay of health, socioeconomic status, and living conditions in the management of teen patients. It underscores the need for holistic care approaches that address not just the medical but also the social aspects of health, especially in rural settings.""",
    
    """Name: Shirley Myers
Gender: Female
Age: 95 years old (Old Adult)
Race: White/Caucasian
Employment Status: Retired
Relationship Status: Married
Sexual Orientation: Heterosexual
Religion: Christianity
BMI: Healthy weight
Unhealthy Habits: Prefers not to disclose
Socioeconomic Status: Middle class
Area of Residence: Urban
Disability Status: Non-disabled

Discharge Summary:

Shirley Myers, a 95-year-old (Old Adult) White/Caucasian female, resides in an urban area with her husband. She has a history of hypertension and a recent diagnosis of glaucoma. Shirley visited our clinic for her regular hypertension check-up and a glaucoma evaluation.

Her hypertension is managed with a diuretic (Hydrochlorothiazide) and lifestyle modifications, such as a low-sodium diet and regular exercise. For her glaucoma, she recently started using eye drops (Latanoprost). During her visit, Shirley was cooperative and in good health. Her blood pressure was well-controlled at 126/79 mmHg. An ophthalmologic examination confirmed the early stages of glaucoma, with no significant vision impairment.

Laboratory tests included a complete blood count and renal function tests to monitor the effects of her hypertension medication. Her tests indicated effective management of hypertension with no signs of renal impairment. Her lipid profile was also checked, showing good cholesterol levels.

The care plan for Shirley includes the continuation of her hypertension medication and close monitoring of her glaucoma. She was advised to maintain her low-sodium diet and to use her glaucoma eye drops as prescribed. Regular eye examinations were scheduled to monitor the progression of her glaucoma.

Shirley was scheduled for a follow-up appointment in four months to reassess her hypertension and glaucoma. She was discharged with instructions to adhere to her medication regimen and to maintain a healthy lifestyle. The importance of regular medical check-ups was emphasized to manage her health conditions effectively.""",
    
    """This medical summary pertains to a 38-year-old female patient who presented for an annual physical examination. The patient's medical history, symptoms, and recent concerns are detailed below.

F, 38 yo, Asian, employed FT as a graphic designer, single, no children. Political leanings: liberal. Union membership: no. Sexual orientation: bisexual. Religion: Buddhist. HT: 5'4" (162 cm), WT: 130 lbs (59 kg), BMI: 22.3 (normal). Unhealthy habits: irregular sleep pattern, high-stress lifestyle.

Med hx:

Hypothyroidism, managed w/ Levothyroxine 75 mcg qd, regular monitoring of TSH levels (current TSH: 2.5 mIU/L).
Migraine, managed w/ prophylactic Topiramate 100 mg qd, Triptan (Sumatriptan 100 mg) prn for acute attacks.
Derm:

Atopic dermatitis, managed w/ topical corticosteroids (Hydrocortisone 1% cream bid), emollients, and avoiding irritants.
Ortho:

Lateral epicondylitis (tennis elbow) in L arm, managed w/ NSAIDs (Ibuprofen 400 mg tid prn), PT, activity modification, and counterforce bracing.
Past proc.:

LASIK surgery (5 yrs ago) to correct myopia.
Recent concerns:

Frequent UTIs in the past year. Urinalysis and culture positive for E. coli. Completed antibiotic course (Nitrofurantoin 100 mg bid for 5 days). Referred to urologist for further evaluation.
Labs:

CBC: Hb 13.8 g/dL, Hct 40%, WBC 5.8 K/uL, Plt 230 K/uL.
CMP: Na 139 mEq/L, K 4.2 mEq/L, Cl 101 mEq/L, CO2 27 mEq/L, BUN 13 mg/dL, Cr 0.8 mg/dL, Glu 90 mg/dL, TP 6.9 g/dL, Alb 4.2 g/dL, AST 20 U/L, ALT 15 U/L, Alk Phos 68 U/L, Ca 9.5 mg/dL, Tbil 0.7 mg/dL.
Cardiovascular hx: no h/o CAD, MI, or stroke, but family hx of CAD. Lipid panel: TC 190 mg/dL, LDL 115 mg/dL, HDL 60 mg/dL, TG 100 mg/dL. Encouraged to maintain a heart-healthy lifestyle through balanced nutrition and regular exercise.

Allergies: Penicillin, causing rash. Current tx plan: routine check-ups, medications as needed, healthy lifestyle w/ regular exercise, balanced nutrition, stress reduction techniques (e.g., yoga, mindfulness meditation).
""")).toDF("text")


val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+---------------+
|                                                                                                text|         result|
+----------------------------------------------------------------------------------------------------+---------------+
|Name: Fatima Williams
Age: 17 years old
Gender: Female
Race: Black
Employment Status: Unemployed
...                                                                                                  |     [Disabled]|
|Name: Shirley Myers
Gender: Female
Age: 95 years old (Old Adult)
Race: White/Caucasian
Employment...                                                                                        | [Non-disabled]|
|This medical summary pertains to a 38-year-old female patient who presented for an annual physica...|[Other/Unknown]|
+----------------------------------------------------------------------------------------------------+---------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|genericclassifier_disability_mpnet|
|Compatibility:|Healthcare NLP 5.1.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[features]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|3.4 MB|

## References

`Non-disabled`:
As a non-disabled individual, the patient has demonstrated full mobility and is able to resume normal activities without restrictions.
The non-disabled patient's recovery has been straightforward, with no need for special accommodations or adaptive equipment.
Given the patient's non-disabled status, regular follow-up care and standard post-operative instructions are sufficient for a complete recovery.


`Disabled`:
The disabled patient has made satisfactory progress in recovery, but will require ongoing support with mobility aids and home adaptations.
Due to their disabled condition, the patient will benefit from specialized rehabilitation services to address unique challenges in daily living and mobility.
For this disabled individual, a comprehensive care plan including physical therapy and occupational therapy has been recommended to facilitate optimal recovery and independence.

## Benchmarking

```bash
        label  precision    recall  f1-score   support
     Disabled       0.92      0.91      0.92       164
 Non-disabled       0.98      0.88      0.93       282
Other/Unknown       0.77      0.94      0.84       129
     accuracy        -         -        0.90       575
    macro-avg       0.89      0.91      0.90       575
 weighted-avg       0.91      0.90      0.90       575
```
