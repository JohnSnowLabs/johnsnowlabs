---
layout: model
title: SDOH Transportation Insecurity For Classification (e5_large)
author: John Snow Labs
name: genericclassifier_sdoh_transportation_insecurity_e5_large
date: 2023-08-13
tags: [transportation, transportation_insecurity, classifier, e5_large, sdoh, en, licensed]
task: Text Classification
language: en
edition: Healthcare NLP 5.0.0
spark_version: 3.0
supported: true
annotator: GenericClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The transportation insecurity classifier employs E5 large embeddings within a generic classifier framework. Trained on a variety of data, the model offers accurate label assignments along with confidence scores for its predictions. The model excels at comprehensively analyzing text, delivering valuable insights into transportation-related insecurity within the provided text. The model's primary task is to categorize text into two key labels: 'No_Transportation_Insecurity_Or_Unknown' and 'Transportation_Insecurity'.

`No_Transportation_Insecurity_Or_Unknown`: This category encompasses statements that indicate the absence of transportation insecurity or situations where the information is unknown or not provided.

`Transportation_Insecurity`: Statements belonging to this category suggest instances of transportation insecurity, where individuals may face challenges in accessing reliable transportation, potentially impacting their overall well-being.

## Predicted Entities

`No_Transportation_Insecurity_Or_Unknown`, `Transportation_Insecurity`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_CLASSIFICATION_GENERIC/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/SOCIAL_DETERMINANT_CLASSIFICATION.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/genericclassifier_sdoh_transportation_insecurity_e5_large_en_5.0.0_3.0_1691945486764.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/genericclassifier_sdoh_transportation_insecurity_e5_large_en_5.0.0_3.0_1691945486764.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
        
e5_emb = E5Embeddings.pretrained("e5_large", 'en')\
    .setInputCols(["document"])\
    .setOutputCol("sentence_embeddings")\
    .setMaxSentenceLength(510)

features_asm = FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

generic_classifier = GenericClassifierModel.pretrained("genericclassifier_sdoh_transportation_insecurity_e5_large", 'en', 'clinical/models')\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

pipeline = Pipeline(stages=[
    document_assembler,
    e5_emb,
    features_asm,
    generic_classifier    
])

text_list = [ """Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy. She is alone and can not drive a car or can not use public bus. """,
                
                "She reported occasional respiratory symptoms, such as wheezing and shortness of breath, but had no signs of a mental disorder. Her healthcare provider assessed her lung function, reviewed her medication regimen, and provided personalized asthma education. She has a transportation problem.", 
                """Patient Information:
Name: Emily Johnson
Age: 68
Gender: Female
Occupation: Retired
Medical Condition: Chronic Obstructive Pulmonary Disease (COPD)
Address: 123 Oak Street, Ruralville, Stateville
Background:
Emily Johnson is a 68-year-old retired teacher residing in the rural town of Ruralville. She was diagnosed with Chronic Obstructive Pulmonary Disease (COPD) five years ago. COPD has led to respiratory symptoms that limit her mobility and energy levels. Despite these challenges, Emily is dedicated to maintaining an active lifestyle and managing her health condition.

Medical History:
Emily's COPD requires regular visits to her pulmonologist, Dr. Robert Davis, who practices in the nearby city of Stateville. She also has occasional appointments with her primary care physician, Dr. Sarah Miller, in Ruralville, for general health check-ups and medication management. Emily uses inhalers and takes oral medications to manage her COPD symptoms.

Emily faces significant transportation challenges due to her remote location and limited mobility. The nearest bus stop is several miles away, and there are no train services available in Ruralville. 

Impact on Healthcare:
Irregular medical visits hinder Dr. Davis and Dr. Miller's ability to monitor her COPD progression, adjust her treatment plan, and provide timely interventions. Additionally, the stress of arranging transportation exacerbates Emily's COPD symptoms and negatively affects her overall well-being.

Proposed Solutions:

Telehealth Consultations: To minimize the need for physical travel, Emily's healthcare providers can offer telehealth consultations for routine check-ups and follow-up appointments. This approach would help her communicate with her doctors without the need to travel long distances.

Conclusion:
Emily Johnson's case highlights the critical role transportation plays in accessing healthcare services, especially for patients in remote areas. Addressing her transportation challenges through innovative solutions can significantly improve her COPD management and overall quality of life. By combining medical expertise with creative transportation options, Emily can receive the care she needs to effectively manage her condition.
""",
"""Patient John is a 60-year-old man who presents to a primary care clinic for a routine check-up. He reports feeling generally healthy, with no significant medical concerns. However, he reveals that he is a smoker and drinks alcohol on a regular basis. The patient also mentions that he has a history of working long hours and has limited time for physical activity and social interactions.

Based on this information, it appears that Patient John's overall health may be affected by several social determinants of health, including tobacco and alcohol use, lack of physical activity, and social isolation. To address these issues, the healthcare provider may recommend a comprehensive physical exam and develop a treatment plan that includes lifestyle modifications, such as smoking cessation and reduction of alcohol intake. Additionally, the patient may benefit from referrals to local organizations that provide resources for physical activity and social engagement. The healthcare provider may also recommend strategies to reduce work-related stress and promote work-life balance. By addressing these social determinants of health, healthcare providers can help promote Patient John's overall health and prevent future health problems. 

Additionally, The distance to the hospital from the John's home is considerable, and there are no available train services.""",

"I can't reach to hospital, because I live far.",

"Based on the presenting symptoms and the information gathered during the assessment, the patient's condition aligns with a diagnosis of paranoid schizophrenia. The severity of his symptoms, including hallucinations, delusions, and impaired social and occupational functioning, necessitates intensive treatment and ongoing support.",

"Lisa, a 28-year-old woman, was diagnosed with generalized anxiety disorder (GAD), a mental disorder characterized by excessive worry and persistent anxiety.",

"Mark, a 35-year-old man, sought medical help for symptoms of attention-deficit/hyperactivity disorder (ADHD), a neurodevelopmental disorder characterized by inattention, hyperactivity, and impulsivity. After a comprehensive evaluation, Mark was diagnosed with ADHD, and his healthcare provider recommended a multimodal treatment approach. "  ]

df = spark.createDataFrame(text_list, StringType()).toDF("text")

result = pipeline.fit(df).transform(df)

result.select("text", "prediction.result").show(truncate=100)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
        
val sentence_embeddings = E5Embeddings.pretrained("e5_large", 'en')
    .setInputCols(["document"])
    .setOutputCol("sentence_embeddings")
    .setMaxSentenceLength(510)

val features_asm = new FeaturesAssembler()
    .setInputCols("sentence_embeddings")
    .setOutputCol("features")

val generic_classifier = GenericClassifierModel.pretrained("genericclassifier_sdoh_transportation_insecurity_e5_large", "en", "clinical/models")
    .setInputCols("features")
    .setOutputCol("prediction")

val pipeline = new PipelineModel().setStages(Array(
    document_assembler,
    sentence_embeddings,
    features_asm,
    generic_classifier))

val data = Seq(Array( """Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy. She is alone and can not drive a car or can not use public bus. """,
                
                "She reported occasional respiratory symptoms, such as wheezing and shortness of breath, but had no signs of a mental disorder. Her healthcare provider assessed her lung function, reviewed her medication regimen, and provided personalized asthma education. She has a transportation problem.", 
                """Patient Information:
Name: Emily Johnson
Age: 68
Gender: Female
Occupation: Retired
Medical Condition: Chronic Obstructive Pulmonary Disease (COPD)
Address: 123 Oak Street, Ruralville, Stateville
Background:
Emily Johnson is a 68-year-old retired teacher residing in the rural town of Ruralville. She was diagnosed with Chronic Obstructive Pulmonary Disease (COPD) five years ago. COPD has led to respiratory symptoms that limit her mobility and energy levels. Despite these challenges, Emily is dedicated to maintaining an active lifestyle and managing her health condition.

Medical History:
Emily's COPD requires regular visits to her pulmonologist, Dr. Robert Davis, who practices in the nearby city of Stateville. She also has occasional appointments with her primary care physician, Dr. Sarah Miller, in Ruralville, for general health check-ups and medication management. Emily uses inhalers and takes oral medications to manage her COPD symptoms.

Emily faces significant transportation challenges due to her remote location and limited mobility. The nearest bus stop is several miles away, and there are no train services available in Ruralville. 

Impact on Healthcare:
Irregular medical visits hinder Dr. Davis and Dr. Miller's ability to monitor her COPD progression, adjust her treatment plan, and provide timely interventions. Additionally, the stress of arranging transportation exacerbates Emily's COPD symptoms and negatively affects her overall well-being.

Proposed Solutions:

Telehealth Consultations: To minimize the need for physical travel, Emily's healthcare providers can offer telehealth consultations for routine check-ups and follow-up appointments. This approach would help her communicate with her doctors without the need to travel long distances.

Conclusion:
Emily Johnson's case highlights the critical role transportation plays in accessing healthcare services, especially for patients in remote areas. Addressing her transportation challenges through innovative solutions can significantly improve her COPD management and overall quality of life. By combining medical expertise with creative transportation options, Emily can receive the care she needs to effectively manage her condition.
""",
"""Patient John is a 60-year-old man who presents to a primary care clinic for a routine check-up. He reports feeling generally healthy, with no significant medical concerns. However, he reveals that he is a smoker and drinks alcohol on a regular basis. The patient also mentions that he has a history of working long hours and has limited time for physical activity and social interactions.

Based on this information, it appears that Patient John's overall health may be affected by several social determinants of health, including tobacco and alcohol use, lack of physical activity, and social isolation. To address these issues, the healthcare provider may recommend a comprehensive physical exam and develop a treatment plan that includes lifestyle modifications, such as smoking cessation and reduction of alcohol intake. Additionally, the patient may benefit from referrals to local organizations that provide resources for physical activity and social engagement. The healthcare provider may also recommend strategies to reduce work-related stress and promote work-life balance. By addressing these social determinants of health, healthcare providers can help promote Patient John's overall health and prevent future health problems. 

Additionally, The distance to the hospital from the John's home is considerable, and there are no available train services.""",

"I can't reach to hospital, because I live far.",

"Based on the presenting symptoms and the information gathered during the assessment, the patient's condition aligns with a diagnosis of paranoid schizophrenia. The severity of his symptoms, including hallucinations, delusions, and impaired social and occupational functioning, necessitates intensive treatment and ongoing support.",

"Lisa, a 28-year-old woman, was diagnosed with generalized anxiety disorder (GAD), a mental disorder characterized by excessive worry and persistent anxiety.",

"Mark, a 35-year-old man, sought medical help for symptoms of attention-deficit/hyperactivity disorder (ADHD), a neurodevelopmental disorder characterized by inattention, hyperactivity, and impulsivity. After a comprehensive evaluation, Mark was diagnosed with ADHD, and his healthcare provider recommended a multimodal treatment approach. "  )).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+-----------------------------------------+
|                                                                                                text|                                   result|
+----------------------------------------------------------------------------------------------------+-----------------------------------------+
|Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatm...|              [Transportation_Insecurity]|
|She reported occasional respiratory symptoms, such as wheezing and shortness of breath, but had n...|              [Transportation_Insecurity]|
|Patient Information:\nName: Emily Johnson\nAge: 68\nGender: Female\nOccupation: Retired\nMedical ...|              [Transportation_Insecurity]|
|Patient John is a 60-year-old man who presents to a primary care clinic for a routine check-up. H...|              [Transportation_Insecurity]|
|                                                      I can't reach to hospital, because I live far.|              [Transportation_Insecurity]|
|Based on the presenting symptoms and the information gathered during the assessment, the patient'...|[No_Transportation_Insecurity_Or_Unknown]|
|Lisa, a 28-year-old woman, was diagnosed with generalized anxiety disorder (GAD), a mental disord...|[No_Transportation_Insecurity_Or_Unknown]|
|Mark, a 35-year-old man, sought medical help for symptoms of attention-deficit/hyperactivity diso...|[No_Transportation_Insecurity_Or_Unknown]|
+----------------------------------------------------------------------------------------------------+-----------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|genericclassifier_sdoh_transportation_insecurity_e5_large|
|Compatibility:|Healthcare NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[features]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|4.3 MB|
|Dependencies:|e5_large|

## References

SDOH internal project

## Benchmarking

```bash
                                 label   precision    recall  f1-score   support
No_Transportation_Insecurity_Or_Unknown       0.96      0.94      0.95       730
              Transportation_Insecurity       0.86      0.89      0.88       302
                               accuracy         -         -       0.93      1032
                              macro-avg       0.91      0.92      0.91      1032
                           weighted-avg       0.93      0.93      0.93      1032
```