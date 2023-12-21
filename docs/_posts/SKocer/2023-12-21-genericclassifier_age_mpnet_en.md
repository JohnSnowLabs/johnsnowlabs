---
layout: model
title: Text Classification for Age (mpnet)
author: John Snow Labs
name: genericclassifier_age_mpnet
date: 2023-12-21
tags: [age, classifier, genericclassifier, mpnet, en, licensed]
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

The PHS-BERT Age Classifier Model is a sophisticated text classification tool tailored to identify and categorize text according to different age groups. This model distinguishes among 'Old Adult', 'Adult', and 'Child and Teen' contexts, providing valuable insights into textual data that references age-specific scenarios or concerns. Detailed information about the classes is as follows:

`Old Adult`: This category includes texts that pertain to older adults, often addressing age-specific health issues, lifestyle considerations, or geriatric care. For instance, a text might discuss mobility challenges or medical conditions more prevalent in elderly populations. Example: "The geriatric clinic specializes in treating common old adult ailments like arthritis and osteoporosis."

`Adult`: Texts under this classification refer to the adult age group, encompassing a wide range of topics from general health care to workplace issues. These texts often deal with health, social, and economic aspects relevant to the adult population. Example: "Adult health screenings are vital for early detection of conditions like hypertension and diabetes."

`Child and Teen`: This classification captures texts related to children and teenagers, focusing on pediatric health, developmental stages, educational concerns, and youth-related social issues. Example: "Pediatricians recommend regular check-ups to monitor child and teen growth and development stages."

`Other/Unknown`: This category includes texts where the patient's age is not specified or is irrelevant to the content. These texts may cover a wide range of topics applicable to all age groups or focus on general health and wellness issues that are not age-specific. For example, a text might discuss the importance of maintaining a balanced diet and regular exercise routine for overall health, without targeting a specific age group. Example: "Regular exercise and a balanced diet are essential for maintaining good health, regardless of age."

## Predicted Entities

`Other/Unknown`, `Old Adult`, `Adult`, `Child and Teen`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/genericclassifier_age_mpnet_en_5.1.4_3.0_1703181685794.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/genericclassifier_age_mpnet_en_5.1.4_3.0_1703181685794.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

generic_classifier = GenericClassifierModel.pretrained("genericclassifier_age_mpnet", "en", "clinical/models")\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

pipeline = Pipeline(stages=[
    document_assembler,
    embeddings,
    features_asm,
    generic_classifier    
])



text_list = ["""Patient Information:
Gender: Non-binary
Age: 27 years old
Race: Native American
Ethnicity: Navajo
Employment Status: Part-time
Job Title: Barista
Marital Status: Single
Political Affiliation: Independent
Union Membership: Not applicable
Sexual Orientation: Demisexual
Religion: None
Height: 5 feet 6 inches
Weight: 180 pounds
Obesity: Class 2 Obesity
Unhealthy Habits: Smokes Cigarettes
Socioeconomic Status: Low income
Area of Residence: Rural
Disability Status: None

Discharge Summary:

The patient presented with a fever, cough, and shortness of breath. The patient reported experiencing symptoms for the past week and sought medical care due to worsening symptoms. Upon examination, the patient was diagnosed with pneumonia.

The patient's medical history revealed no significant health issues. However, the patient exhibited several risk factors for pneumonia, including being a smoker and having class 2 obesity.

During the hospital stay, the patient received antibiotics and breathing treatments. The patient responded well to the treatments, and their symptoms significantly improved. Consequently, the patient was discharged and advised to follow up with their primary care physician.

Additionally, the patient was advised to quit smoking due to the increased risk for developing respiratory infections such as pneumonia. The patient was provided with resources to assist in their smoking cessation efforts.

Overall, the patient's prognosis is good. However, the patient is advised to maintain good respiratory health practices to reduce the risk of future respiratory infections. The patient was educated regarding the importance of maintaining a healthy lifestyle, good nutrition, and regular exercise to improve their overall health, mitigate the risk of future health problems, and manage their class 2 obesity.""",
             
"""Name: Anne Harris
Gender: Female
Age: 87 years old (Old Adult)
Race: White/Caucasian
Employment Status: Retired
Relationship Status: Married
Sexual Orientation: Heterosexual
Religion: Christianity
BMI: Healthy weight
Unhealthy Habits: Prefers not to disclose the information
Socioeconomic Status: Middle class
Area of Residence: Urban
Disability Status: Non-disabled

Discharge Summary:
Anne Harris, an 87-year-old (Old Adult) female, attended our clinic for her semi-annual health check-up. Living in an urban area with her husband, Anne enjoys a retired life with hobbies that include gentle yoga, painting, and social gatherings with friends. She has a history of well-controlled type 2 diabetes and stable ischemic heart disease.

During her visit, Anne reported that her diabetes is managed with oral medication, specifically metformin, and dietary control. Her recent HbA1c levels have been within the target range. For her heart condition, she takes a daily low-dose aspirin and a statin.

The physical examination showed an elderly woman in stable condition. Her cardiovascular examination was normal, with a regular heart rhythm and controlled blood pressure. Her diabetic foot examination revealed no signs of ulcers or neuropathy.

Laboratory tests included a complete blood count, which was normal, and a comprehensive metabolic panel. Her renal function tests were within normal limits, important for her diabetes management.

Anne was advised to continue her medication regimen for diabetes and ischemic heart disease. She was encouraged to maintain her active lifestyle and dietary habits. Regular follow-up visits were recommended to monitor her diabetes, heart health, and overall well-being.""",
             
"""Name: Aaliyah Harris
Gender: Female
Age: 17 years old (Teen)
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
Aaliyah Harris, a 17-year-old (Teen) Muslim female, presented with recurrent severe headaches and visual disturbances, raising concerns for possible intracranial hypertension. Her condition was further complicated by her underweight status and disability, and she faced challenges accessing specialized care due to her rural location.

Upon examination, Aaliyah exhibited papilledema and visual field deficits. MRI of the brain and lumbar puncture were performed, which indicated raised intracranial pressure without any structural abnormalities.

Her management included the initiation of acetazolamide to reduce cerebrospinal fluid production and alleviate intracranial pressure. Nutritional counseling was provided to improve her overall health status, focusing on a diet that accommodates her Islamic dietary practices.

Physical therapy sessions, tailored to her disability, focused on low-impact exercises to minimize the risk of exacerbating her condition.

Upon discharge, Aaliyah's headache frequency had reduced, and her visual symptoms showed improvement. She was scheduled for regular follow-up appointments with a neurologist to closely monitor her condition. Efforts were made to coordinate continued care and support within her rural community.

Aaliyah Harris's case highlights the importance of addressing potential neurological conditions in teens and managing them effectively in the context of additional challenges such as undernutrition, disability, and limited healthcare access.""",

"""Name: Daniel Martinez
Gender: Male
Age: Not specified
Race: White/Caucasian
Employment Status: Employed
Relationship Status: Single
Sexual Orientation: Heterosexual
Religion: Christianity
BMI: Underweight
Unhealthy Habits: Substance use
Socioeconomic Status: High
Area of Residence: Urban
Disability Status: Non-disabled
Discharge Summary:
Daniel Martinez, an employed male from an urban background, was admitted due to complications arising from substance use and an underweight condition. His hospital stay involved a comprehensive treatment plan encompassing medical detoxification, intensive psychological therapy, and nutritional support. The therapy sessions focused on exploring the root causes of his substance use, developing effective coping mechanisms, and fostering resilience for sustained recovery. Concurrently, nutritional counseling aimed to improve his dietary habits and ensure a gradual increase to a healthy body weight. Danielâ€™s engagement in the treatment process was proactive, and he demonstrated significant improvement in his health. At discharge, he was provided with a detailed aftercare plan, including ongoing therapy, dietitian consultations, and participation in support groups, to support his continued recovery and health improvement."""
    
]


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

val generic_classifier = GenericClassifierModel.pretrained("genericclassifier_age_mpnet", "en", "clinical/models")
    .setInputCols("features")
    .setOutputCol("prediction")

val pipeline = new PipelineModel().setStages(Array(
    document_assembler,
    embeddings,
    features_asm,
    generic_classifier    
))


val data = Seq(Array("""Patient Information:
Gender: Non-binary
Age: 27 years old
Race: Native American
Ethnicity: Navajo
Employment Status: Part-time
Job Title: Barista
Marital Status: Single
Political Affiliation: Independent
Union Membership: Not applicable
Sexual Orientation: Demisexual
Religion: None
Height: 5 feet 6 inches
Weight: 180 pounds
Obesity: Class 2 Obesity
Unhealthy Habits: Smokes Cigarettes
Socioeconomic Status: Low income
Area of Residence: Rural
Disability Status: None

Discharge Summary:

The patient presented with a fever, cough, and shortness of breath. The patient reported experiencing symptoms for the past week and sought medical care due to worsening symptoms. Upon examination, the patient was diagnosed with pneumonia.

The patient's medical history revealed no significant health issues. However, the patient exhibited several risk factors for pneumonia, including being a smoker and having class 2 obesity.

During the hospital stay, the patient received antibiotics and breathing treatments. The patient responded well to the treatments, and their symptoms significantly improved. Consequently, the patient was discharged and advised to follow up with their primary care physician.

Additionally, the patient was advised to quit smoking due to the increased risk for developing respiratory infections such as pneumonia. The patient was provided with resources to assist in their smoking cessation efforts.

Overall, the patient's prognosis is good. However, the patient is advised to maintain good respiratory health practices to reduce the risk of future respiratory infections. The patient was educated regarding the importance of maintaining a healthy lifestyle, good nutrition, and regular exercise to improve their overall health, mitigate the risk of future health problems, and manage their class 2 obesity.""",
             
"""Name: Anne Harris
Gender: Female
Age: 87 years old (Old Adult)
Race: White/Caucasian
Employment Status: Retired
Relationship Status: Married
Sexual Orientation: Heterosexual
Religion: Christianity
BMI: Healthy weight
Unhealthy Habits: Prefers not to disclose the information
Socioeconomic Status: Middle class
Area of Residence: Urban
Disability Status: Non-disabled

Discharge Summary:
Anne Harris, an 87-year-old (Old Adult) female, attended our clinic for her semi-annual health check-up. Living in an urban area with her husband, Anne enjoys a retired life with hobbies that include gentle yoga, painting, and social gatherings with friends. She has a history of well-controlled type 2 diabetes and stable ischemic heart disease.

During her visit, Anne reported that her diabetes is managed with oral medication, specifically metformin, and dietary control. Her recent HbA1c levels have been within the target range. For her heart condition, she takes a daily low-dose aspirin and a statin.

The physical examination showed an elderly woman in stable condition. Her cardiovascular examination was normal, with a regular heart rhythm and controlled blood pressure. Her diabetic foot examination revealed no signs of ulcers or neuropathy.

Laboratory tests included a complete blood count, which was normal, and a comprehensive metabolic panel. Her renal function tests were within normal limits, important for her diabetes management.

Anne was advised to continue her medication regimen for diabetes and ischemic heart disease. She was encouraged to maintain her active lifestyle and dietary habits. Regular follow-up visits were recommended to monitor her diabetes, heart health, and overall well-being.""",
             
"""Name: Aaliyah Harris
Gender: Female
Age: 17 years old (Teen)
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
Aaliyah Harris, a 17-year-old (Teen) Muslim female, presented with recurrent severe headaches and visual disturbances, raising concerns for possible intracranial hypertension. Her condition was further complicated by her underweight status and disability, and she faced challenges accessing specialized care due to her rural location.

Upon examination, Aaliyah exhibited papilledema and visual field deficits. MRI of the brain and lumbar puncture were performed, which indicated raised intracranial pressure without any structural abnormalities.

Her management included the initiation of acetazolamide to reduce cerebrospinal fluid production and alleviate intracranial pressure. Nutritional counseling was provided to improve her overall health status, focusing on a diet that accommodates her Islamic dietary practices.

Physical therapy sessions, tailored to her disability, focused on low-impact exercises to minimize the risk of exacerbating her condition.

Upon discharge, Aaliyah's headache frequency had reduced, and her visual symptoms showed improvement. She was scheduled for regular follow-up appointments with a neurologist to closely monitor her condition. Efforts were made to coordinate continued care and support within her rural community.

Aaliyah Harris's case highlights the importance of addressing potential neurological conditions in teens and managing them effectively in the context of additional challenges such as undernutrition, disability, and limited healthcare access.""",

"""Name: Daniel Martinez
Gender: Male
Age: Not specified
Race: White/Caucasian
Employment Status: Employed
Relationship Status: Single
Sexual Orientation: Heterosexual
Religion: Christianity
BMI: Underweight
Unhealthy Habits: Substance use
Socioeconomic Status: High
Area of Residence: Urban
Disability Status: Non-disabled
Discharge Summary:
Daniel Martinez, an employed male from an urban background, was admitted due to complications arising from substance use and an underweight condition. His hospital stay involved a comprehensive treatment plan encompassing medical detoxification, intensive psychological therapy, and nutritional support. The therapy sessions focused on exploring the root causes of his substance use, developing effective coping mechanisms, and fostering resilience for sustained recovery. Concurrently, nutritional counseling aimed to improve his dietary habits and ensure a gradual increase to a healthy body weight. Danielâ€™s engagement in the treatment process was proactive, and he demonstrated significant improvement in his health. At discharge, he was provided with a detailed aftercare plan, including ongoing therapy, dietitian consultations, and participation in support groups, to support his continued recovery and health improvement."""
)).toDF("text")


val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+----------------+
|                                                                                                text|          result|
+----------------------------------------------------------------------------------------------------+----------------+
|Patient Information:
Gender: Non-binary
Age: 27 years old
Race: Native American
Ethnicity: Navajo...                                                                                 |         [Adult]|
|Name: Anne Harris
Gender: Female
Age: 87 years old (Old Adult)
Race: White/Caucasian
Employment S...                                                                                      |     [Old Adult]|
|Name: Aaliyah Harris
Gender: Female
Age: 17 years old (Teen)
Race: Black
Employment Status: Unemp...                                                                          |[Child and Teen]|
|Name: Daniel Martinez
Gender: Male
Age: Not specified
Race: White/Caucasian
Employment Status: Em...                                                                             | [Other/Unknown]|
+----------------------------------------------------------------------------------------------------+----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|genericclassifier_age_mpnet|
|Compatibility:|Healthcare NLP 5.1.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[features]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|3.4 MB|

## References

`Other/Unknown`:
For individuals where age remains undetermined, adopting healthy lifestyle habits such as balanced nutrition and moderate physical activity is universally beneficial, regardless of the specific age group.
Mental health care, including effective stress management and nurturing emotional well-being, plays a vital role in the wellness of individuals whose age is not specified, transcending specific age-related health concerns.
In cases where a patient's age is ambiguous, prioritizing general wellness practices, like stress reduction and adequate rest, is key to promoting overall health and well-being.

`Old Adult`:
Improvement in the patient's condition has been noted, but as an old adult, considerations for slower healing processes and age-related complications are integral to their care plan.
Case studies detailing healthcare scenarios specific to older adults, such as managing chronic illnesses or adapting to age-related physical changes.
Particular attention for this old adult should be on managing multiple medications effectively to avoid the common risks of drug interactions in the elderly.

`Adult`:
The patient, identified as an adult, has been advised on balancing work and personal life to mitigate stress-related health issues common in this age group.
Regular health screenings, such as checking blood pressure and cholesterol levels, are particularly important for this adult patient to prevent common health issues.
Adopting a healthy lifestyle, including a balanced diet and regular exercise, is encouraged for this adult to maintain good health and prevent age-related conditions.

`Child and Teen`:
A nutrient-rich diet is recommended for the patient in the child and teen category to support their critical growth and development stages.
Monitoring both social and emotional health is crucial for this patient who falls under the child and teen group, alongside their physical well-being.
Pediatric case files emphasizing health issues, developmental milestones, and educational challenges relevant to children and teenagers.

## Benchmarking

```bash
         label  precision    recall  f1-score   support
         Adult       0.90      0.90      0.90       222
Child and Teen       1.00      0.98      0.99       111
     Old Adult       0.93      0.86      0.89       176
 Other/Unknown       0.74      0.96      0.84        53
      accuracy                           0.91       562
     macro-avg       0.89      0.93      0.91       562
  weighted-avg       0.91      0.91      0.91       562
```
