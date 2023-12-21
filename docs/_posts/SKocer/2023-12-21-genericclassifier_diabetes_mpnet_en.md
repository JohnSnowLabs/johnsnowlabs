---
layout: model
title: Text Classification for Diabetes (mpnet)
author: John Snow Labs
name: genericclassifier_diabetes_mpnet
date: 2023-12-21
tags: [diabetes, classifier, genericclassifier, mpnet, en, licensed]
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

The PHS-BERT Diabetes Classifier Model is an advanced text classification tool designed to accurately identify and categorize textual data based on different types of diabetes. This innovative model is adept at distinguishing between 'Diabetes Type 1', 'Diabetes Type 2', 'Gestational Diabetes', 'Other/Unknown', and 'No Diabetes' contexts, offering critical insights into texts related to diabetes-specific health issues, management strategies, and preventative measures. The detailed descriptions of the classes are as follows:

`Type 1`: This category includes texts specifically related to Diabetes Type 1, often focusing on its autoimmune nature, the necessity of insulin therapy, and daily management challenges. For instance, a text might detail the intricacies of balancing insulin doses with diet and exercise in Type 1 Diabetes. Example: "Individuals with Diabetes Type 1 must diligently monitor their blood glucose levels and adjust insulin doses accordingly."

`Type 2`: Texts under this classification pertain to Diabetes Type 2, typically discussing aspects such as insulin resistance, the impact of lifestyle choices, and management through medication, diet, and physical activity. An example text might explore how dietary changes and regular exercise can significantly improve blood sugar control in Type 2 Diabetes. Example: "Lifestyle modifications play a crucial role in managing Diabetes Type 2, alongside medication."

`Gestational`: This classification covers texts related to Gestational Diabetes, focusing on its management during pregnancy to ensure both maternal and fetal health. These texts might include guidelines for monitoring blood glucose and making dietary adjustments during pregnancy. Example: "Effective management of Gestational Diabetes involves careful monitoring of dietary intake to maintain stable blood sugar levels."

`Other/Unknown`: Texts in this category cover cases where the type of diabetes is not specified or discusses other forms of diabetes. These texts often provide general information on diabetes symptoms, diagnosis, and management strategies suitable for various forms of the condition. Example: "Patients with unspecified types of diabetes should follow general guidelines for blood sugar control, pending a more specific diagnosis."

`No`: This category encompasses texts relating to individuals without diabetes, focusing on preventive strategies, healthy lifestyle choices, and risk reduction for developing diabetes. These texts might discuss the importance of diet and exercise in preventing diabetes, especially in individuals with a family history of the disease. Example: "Adopting a healthy diet and regular exercise routine is key to preventing the development of diabetes, particularly in those with genetic predispositions."

## Predicted Entities

`Other/Unknown`, `No`, `Type 1`, `Type 2`, `Gestational`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/genericclassifier_diabetes_mpnet_en_5.1.4_3.0_1703180465833.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/genericclassifier_diabetes_mpnet_en_5.1.4_3.0_1703180465833.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

generic_classifier = GenericClassifierModel.pretrained("genericclassifier_diabetes_mpnet", "en", "clinical/models")\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

pipeline = Pipeline(stages=[
    document_assembler,
    embeddings,
    features_asm,
    generic_classifier    
])


text_list = ["""Patient Information: 
Patient Name: John Smith 
Age: 45 
Gender: Male 
Date of Birth: January 15, 1976 
Address: 123 Main Street, Anytown, USA 
Phone Number: 555-1234 
Insurance Provider: XYZ Insurance

Final Diagnosis and Treatment Plan: 
1. Diagnosis: COPD exacerbation 
2. Treatment Plan: 
- Increase inhaler usage to every 2-4 hours 
- Continue oral corticosteroids for 5 days 
- Supplemental oxygen therapy to maintain oxygen saturation above 92% 
- Pulmonary rehabilitation program to improve lung function 
- Smoking cessation counseling 
- Regular follow-up appointments to monitor progress

Medical History: 
The patient has a history of respiratory disease, specifically chronic obstructive pulmonary disease (COPD). He was diagnosed with COPD five years ago and has been on regular medication since then. He also has a history of obesity, classified as class 2 obesity. Additionally, the patient has a history of type 1 diabetes, which was diagnosed during childhood. The patient does not have any history of mental disorders or heart disease.

Clinical History: 
The patient presented with complaints of shortness of breath, wheezing, and coughing. He has been experiencing these symptoms for the past week and they have been progressively worsening. The patient also reports fatigue and difficulty performing daily activities due to breathing difficulties. There is no history of fever or chest pain.

Chief Complaint: 
The patient's chief complaint is persistent shortness of breath and wheezing, which is affecting his quality of life and daily activities.

History of Present Illness: 
The patient's symptoms started with a mild cough and gradually progressed to severe shortness of breath. The patient has been using his inhaler more frequently but has not experienced significant relief. He denies any recent exposure to allergens or respiratory infections.

Medications: 
The patient is currently taking the following medications: 
1. Inhaler (Combivent) - 2 puffs every 4-6 hours 
2. Oral corticosteroids (Prednisone) - 10 mg daily 
3. Bronchodilator (Albuterol) - as needed for acute symptoms 
4. Insulin (Lantus) - long-acting insulin for diabetes management

Physical Examination: 
On physical examination, the patient appears to be in moderate distress. He has increased respiratory rate and uses accessory muscles for breathing. Auscultation of the lungs reveals bilateral wheezing and decreased breath sounds. The patient's oxygen saturation is 90% on room air.

Laboratory Results: 
The patient's laboratory results show an elevated white blood cell count, indicating an inflammatory response. Arterial blood gas analysis reveals respiratory acidosis. Pulmonary function tests demonstrate a significant decrease in forced expiratory volume in one second (FEV1) and forced vital capacity (FVC), consistent with obstructive lung disease.

Imaging Studies: 
The patient underwent a chest X-ray, which shows hyperinflation of the lungs and flattened diaphragms, characteristic of COPD. There are no signs of pneumonia or other acute lung abnormalities.""",
             
"""A 52-year-old Caucasian female is here for her six-month evaluation. She has known diagnoses of COPD, Type 1 Diabetes, and Obesity Class 1. She has a 15-year history of smoking but quit five years ago. Family history is significant for COPD and obesity. Her current medications include Combivent for COPD and a mixture of NPH and Regular insulin for diabetes. She has no known drug allergies.

The patient reports frequent coughing with clear to white sputum, dyspnea on exertion, fatigue, and episodes of wheezing. Concurrently, she has noticed increased thirst, polyuria, unexplained weight loss, and tingling in her hands and feet. Additionally, she complains of frequent headaches and difficulty in swallowing solid foods. She remains compliant with her medications.

On physical examination, her BMI is 29.7, and decreased breath sounds and wheezing are noted upon lung auscultation. Laboratory findings show an HbA1c of 8.1% and an FEV1 of 52% of predicted. Barium swallow confirms esophageal dysmotility. MRI of the brain was normal, ruling out significant neurological causes for the headaches.

COPD
Obesity Class 1
Diabetes Type 1
Esophageal Dysmotility
Chronic Headaches
The treatment strategy includes continuing Combivent for COPD management and considering bronchodilator titration based on symptomatology. A gastroenterologist consultation is advised for esophageal dysmotility, and potential pharmacological therapy or surgical intervention may be considered. Frequent blood glucose monitoring and insulin adjustments are recommended. For chronic headaches, a prophylactic medication like Topiramate can be considered after a neurology consult. A low-calorie, high-fiber diet is recommended for obesity.
""",
             
"""The patient, a 55-year-old male who came in reporting persistent fatigue, shortness of breath, and an overall feeling of nausea, has a medical history that is not without complications. Upon examination, it became evident that he carries excess weight, in fact, the patient's body mass index (BMI) characterizes him as having class 2 obesity. It's common knowledge that a BMI of over 35 is categorized as class 2 obesity, this is a condition that heightens the risk of developing other health issues such as diabetes and cardiovascular diseases, hence making weight management a top priority. The patient revealed to us that he has been previously diagnosed with Type 2 diabetes which is often synonymous with increased weight. Type 2 diabetes causes the body to resist insulin or fail to produce enough of it, leading to an elevation in blood sugar levels. An optimal control of his glycemic levels will be paramount in management of the clinical condition.

Moreover, the patient's heart condition was suspected as he presented classic symptoms of heart diseases such as hypertension - a prevalent condition that results in a persistent elevation in the blood pressure that can potentially lead to other serious heart ailments. Further tests were carried out and the patient's worst fear came to light - a diagnosis of myocardial infarction. Better known as a heart attack, a myocardial infarction is a potentially lethal condition that occurs when the blood supply to the heart is blocked, typically due to a blood clot obstructing a coronary artery. This tragic occurrence can fatally damage the heart muscle if not promptly treated.

The patient also complained of recurring bouts of chest tightness and shortness of breath, symptoms that could not simply be dismissed as being associated with his heart diseases. Upon further investigation, it surfaced that the patient was battling chronic bronchitis. Chronic bronchitis is a type of chronic obstructive pulmonary disease (COPD) that causes inflammation and constriction of the bronchial tubes, posing difficulty for the patient to breathe easily. A comprehensive treatment plan was suggested which included inhalers, medication, and possibly pulmonary rehabilitation.

On top of these physical challenges, the patient also revealed that he has been experiencing prolonged periods of sadness, loss of interest, and difficulty sleeping. After being referred to our staff psychiatrist, he was diagnosed with depression. Depression is a serious mental health disorder that can significantly interfere with a person's daily life and can even lead to suicidal thoughts if left untreated. With a comprehensive treatment plan including counseling and medication, he will be able to manage his mental health alongside his physical conditions.

Altogether, the patient's treatment will require meticulous management of his diabetes and obesity through dietary changes and regular exercise. Furthermore, his heart condition and chronic bronchitis will involve a complex treatment plan that includes medication, lifestyle changes, and possibly surgical interventions. His mental health will also need to be carefully monitored with regular psychiatric consultations and prescribed medication. It will not be an easy journey, but with consistent care and support, the patient stands a good chance of managing these conditions and improving his quality of life.""",
             
"""Jane Simmons, a 32-year-old graphic designer from Seattle, has been experiencing episodes of high anxiety, palpitations, and increasing thirst and hunger. She had gestational diabetes during her last pregnancy and has been feeling extremely stressed lately due to work pressure. No known allergies were reported.

Her BMI slotted her in class 1 obesity. An irregular heartbeat was noted on her cardiac auscultation. Blood tests indicated elevated blood sugar levels even post-prandially. A 24-hour Holter monitor showed occasional premature ventricular contractions (PVCs). Based on her symptoms and clinical findings, she underwent a psychological assessment which hinted at a generalized anxiety disorder.

She was prescribed a low dose of a beta-blocker for her cardiac rhythm and an SSRI for her anxiety. Dietary modifications were recommended for her post-gestational diabetes and she was initiated on Metformin. Regular follow-ups were emphasized to monitor her cardiac rhythm and mental health.

Diagnoses:

Post-Gestational Diabetes
Class 1 Obesity
Generalized Anxiety Disorder
Premature Ventricular Contractions"""

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

val generic_classifier = GenericClassifierModel.pretrained("genericclassifier_diabetes_mpnet", "en", "clinical/models")
    .setInputCols("features")
    .setOutputCol("prediction")

val pipeline = new PipelineModel().setStages(Array(
    document_assembler,
    embeddings,
    features_asm,
    generic_classifier    
))


val data = Seq(Array("""Patient Information: 
Patient Name: John Smith 
Age: 45 
Gender: Male 
Date of Birth: January 15, 1976 
Address: 123 Main Street, Anytown, USA 
Phone Number: 555-1234 
Insurance Provider: XYZ Insurance

Final Diagnosis and Treatment Plan: 
1. Diagnosis: COPD exacerbation 
2. Treatment Plan: 
- Increase inhaler usage to every 2-4 hours 
- Continue oral corticosteroids for 5 days 
- Supplemental oxygen therapy to maintain oxygen saturation above 92% 
- Pulmonary rehabilitation program to improve lung function 
- Smoking cessation counseling 
- Regular follow-up appointments to monitor progress

Medical History: 
The patient has a history of respiratory disease, specifically chronic obstructive pulmonary disease (COPD). He was diagnosed with COPD five years ago and has been on regular medication since then. He also has a history of obesity, classified as class 2 obesity. Additionally, the patient has a history of type 1 diabetes, which was diagnosed during childhood. The patient does not have any history of mental disorders or heart disease.

Clinical History: 
The patient presented with complaints of shortness of breath, wheezing, and coughing. He has been experiencing these symptoms for the past week and they have been progressively worsening. The patient also reports fatigue and difficulty performing daily activities due to breathing difficulties. There is no history of fever or chest pain.

Chief Complaint: 
The patient's chief complaint is persistent shortness of breath and wheezing, which is affecting his quality of life and daily activities.

History of Present Illness: 
The patient's symptoms started with a mild cough and gradually progressed to severe shortness of breath. The patient has been using his inhaler more frequently but has not experienced significant relief. He denies any recent exposure to allergens or respiratory infections.

Medications: 
The patient is currently taking the following medications: 
1. Inhaler (Combivent) - 2 puffs every 4-6 hours 
2. Oral corticosteroids (Prednisone) - 10 mg daily 
3. Bronchodilator (Albuterol) - as needed for acute symptoms 
4. Insulin (Lantus) - long-acting insulin for diabetes management

Physical Examination: 
On physical examination, the patient appears to be in moderate distress. He has increased respiratory rate and uses accessory muscles for breathing. Auscultation of the lungs reveals bilateral wheezing and decreased breath sounds. The patient's oxygen saturation is 90% on room air.

Laboratory Results: 
The patient's laboratory results show an elevated white blood cell count, indicating an inflammatory response. Arterial blood gas analysis reveals respiratory acidosis. Pulmonary function tests demonstrate a significant decrease in forced expiratory volume in one second (FEV1) and forced vital capacity (FVC), consistent with obstructive lung disease.

Imaging Studies: 
The patient underwent a chest X-ray, which shows hyperinflation of the lungs and flattened diaphragms, characteristic of COPD. There are no signs of pneumonia or other acute lung abnormalities.""",
             
"""A 52-year-old Caucasian female is here for her six-month evaluation. She has known diagnoses of COPD, Type 1 Diabetes, and Obesity Class 1. She has a 15-year history of smoking but quit five years ago. Family history is significant for COPD and obesity. Her current medications include Combivent for COPD and a mixture of NPH and Regular insulin for diabetes. She has no known drug allergies.

The patient reports frequent coughing with clear to white sputum, dyspnea on exertion, fatigue, and episodes of wheezing. Concurrently, she has noticed increased thirst, polyuria, unexplained weight loss, and tingling in her hands and feet. Additionally, she complains of frequent headaches and difficulty in swallowing solid foods. She remains compliant with her medications.

On physical examination, her BMI is 29.7, and decreased breath sounds and wheezing are noted upon lung auscultation. Laboratory findings show an HbA1c of 8.1% and an FEV1 of 52% of predicted. Barium swallow confirms esophageal dysmotility. MRI of the brain was normal, ruling out significant neurological causes for the headaches.

COPD
Obesity Class 1
Diabetes Type 1
Esophageal Dysmotility
Chronic Headaches
The treatment strategy includes continuing Combivent for COPD management and considering bronchodilator titration based on symptomatology. A gastroenterologist consultation is advised for esophageal dysmotility, and potential pharmacological therapy or surgical intervention may be considered. Frequent blood glucose monitoring and insulin adjustments are recommended. For chronic headaches, a prophylactic medication like Topiramate can be considered after a neurology consult. A low-calorie, high-fiber diet is recommended for obesity.
""",
             
"""The patient, a 55-year-old male who came in reporting persistent fatigue, shortness of breath, and an overall feeling of nausea, has a medical history that is not without complications. Upon examination, it became evident that he carries excess weight, in fact, the patient's body mass index (BMI) characterizes him as having class 2 obesity. It's common knowledge that a BMI of over 35 is categorized as class 2 obesity, this is a condition that heightens the risk of developing other health issues such as diabetes and cardiovascular diseases, hence making weight management a top priority. The patient revealed to us that he has been previously diagnosed with Type 2 diabetes which is often synonymous with increased weight. Type 2 diabetes causes the body to resist insulin or fail to produce enough of it, leading to an elevation in blood sugar levels. An optimal control of his glycemic levels will be paramount in management of the clinical condition.

Moreover, the patient's heart condition was suspected as he presented classic symptoms of heart diseases such as hypertension - a prevalent condition that results in a persistent elevation in the blood pressure that can potentially lead to other serious heart ailments. Further tests were carried out and the patient's worst fear came to light - a diagnosis of myocardial infarction. Better known as a heart attack, a myocardial infarction is a potentially lethal condition that occurs when the blood supply to the heart is blocked, typically due to a blood clot obstructing a coronary artery. This tragic occurrence can fatally damage the heart muscle if not promptly treated.

The patient also complained of recurring bouts of chest tightness and shortness of breath, symptoms that could not simply be dismissed as being associated with his heart diseases. Upon further investigation, it surfaced that the patient was battling chronic bronchitis. Chronic bronchitis is a type of chronic obstructive pulmonary disease (COPD) that causes inflammation and constriction of the bronchial tubes, posing difficulty for the patient to breathe easily. A comprehensive treatment plan was suggested which included inhalers, medication, and possibly pulmonary rehabilitation.

On top of these physical challenges, the patient also revealed that he has been experiencing prolonged periods of sadness, loss of interest, and difficulty sleeping. After being referred to our staff psychiatrist, he was diagnosed with depression. Depression is a serious mental health disorder that can significantly interfere with a person's daily life and can even lead to suicidal thoughts if left untreated. With a comprehensive treatment plan including counseling and medication, he will be able to manage his mental health alongside his physical conditions.

Altogether, the patient's treatment will require meticulous management of his diabetes and obesity through dietary changes and regular exercise. Furthermore, his heart condition and chronic bronchitis will involve a complex treatment plan that includes medication, lifestyle changes, and possibly surgical interventions. His mental health will also need to be carefully monitored with regular psychiatric consultations and prescribed medication. It will not be an easy journey, but with consistent care and support, the patient stands a good chance of managing these conditions and improving his quality of life.""",
             
"""Jane Simmons, a 32-year-old graphic designer from Seattle, has been experiencing episodes of high anxiety, palpitations, and increasing thirst and hunger. She had gestational diabetes during her last pregnancy and has been feeling extremely stressed lately due to work pressure. No known allergies were reported.

Her BMI slotted her in class 1 obesity. An irregular heartbeat was noted on her cardiac auscultation. Blood tests indicated elevated blood sugar levels even post-prandially. A 24-hour Holter monitor showed occasional premature ventricular contractions (PVCs). Based on her symptoms and clinical findings, she underwent a psychological assessment which hinted at a generalized anxiety disorder.

She was prescribed a low dose of a beta-blocker for her cardiac rhythm and an SSRI for her anxiety. Dietary modifications were recommended for her post-gestational diabetes and she was initiated on Metformin. Regular follow-ups were emphasized to monitor her cardiac rhythm and mental health.

Diagnoses:

Post-Gestational Diabetes
Class 1 Obesity
Generalized Anxiety Disorder
Premature Ventricular Contractions""")).toDF("text")


val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+-------------+
|                                                                                                text|       result|
+----------------------------------------------------------------------------------------------------+-------------+
|Patient Information: 
Patient Name: John Smith 
Age: 45 
Gender: Male 
Date of Birth: January 15,...                                                                        |         [No]|
|A 52-year-old Caucasian female is here for her six-month evaluation. She has known diagnoses of C...|     [Type 1]|
|The patient, a 55-year-old male who came in reporting persistent fatigue, shortness of breath, an...|     [Type 2]|
|Jane Simmons, a 32-year-old graphic designer from Seattle, has been experiencing episodes of high...|[Gestational]|
+----------------------------------------------------------------------------------------------------+-------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|genericclassifier_diabetes_mpnet|
|Compatibility:|Healthcare NLP 5.1.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[features]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|3.4 MB|

## References

`Type 1`:
For individuals diagnosed with Diabetes Type 1, managing blood sugar levels through insulin therapy and diet adjustments is crucial, as this condition typically develops in childhood or adolescence.
Case studies focusing on Diabetes Type 1 often highlight the importance of early detection, continuous glucose monitoring, and the impact of autoimmune factors.
Living with Diabetes Type 1 requires constant awareness of carbohydrate intake, physical activity, and insulin management to maintain optimal health.

`Type 2`:
In adults, Diabetes Type 2 is often associated with lifestyle factors and obesity, with texts emphasizing the importance of diet, exercise, and weight management in controlling blood sugar levels.
Case studies related to Diabetes Type 2 frequently discuss the role of insulin resistance, the need for medication management, and potential complications like cardiovascular disease.
Preventative strategies for Diabetes Type 2, including regular screenings and lifestyle modifications, are key topics in health care literature for adults at risk of this condition.

`Gestational`:
Gestational Diabetes, occurring during pregnancy, requires careful monitoring to protect both maternal and fetal health, as highlighted in pregnancy-related medical texts.
The condition of Gestational Diabetes is often managed through dietary adjustments and, in some cases, insulin therapy, to ensure stable blood glucose levels throughout pregnancy.
Texts on Gestational Diabetes typically cover its impact on pregnancy outcomes, risks of developing Type 2 Diabetes postpartum, and guidelines for glucose testing during pregnancy.

`Other/Unknown`:
The patient's neuropathy assessment shows early signs of sensory loss in the feet, warranting close monitoring and preventive care in diabetes management.
Monitoring the efficacy of sulfonylurea treatment in managing the patient's MODY type 7 diabetes.
The patient's neuropathy assessment shows early signs of sensory loss in the feet, warranting close monitoring and preventive care in diabetes management.

`No`:
Patient's normal insulin sensitivity and absence of glucose in urine samples conclusively demonstrate they do not have diabetes.In the context of no diabetes, case studies might explore the impact of lifestyle choices on maintaining normal blood sugar levels and preventing metabolic disorders.
Patient's thorough medical history and current health parameters strongly indicate they do not have diabetes and are at low risk for its onset.

## Benchmarking

```bash
        label  precision    recall  f1-score   support
  Gestational       0.97      0.98      0.97       450
           No       0.61      0.97      0.75       182
Other/Unknown       0.78      0.66      0.72        80
       Type 1       0.97      0.89      0.93       745
       Type 2       0.91      0.87      0.89       931
     accuracy                           0.90      2388
    macro-avg       0.85      0.87      0.85      2388
 weighted-avg       0.91      0.90      0.90      2388
```