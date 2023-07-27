---
layout: model
title: Extract Section Headers and Diagnoses from Clinical Documents
author: John Snow Labs
name: ner_section_header_diagnosis
date: 2023-07-26
tags: [licensed, clinical, en, ner, diagnosis, section_header, common_diagnosis]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.0.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This NER model analyzes clinical documents, focusing on diverse medical conditions and key sections of patient records. Defined labels representing diseases like heart disease, diabetes, and Alzheimer's help provide deeper insights into the diagnosis and treatment patterns

Definitions of Predicted Entities

`Heart disease`: References to any diagnosed cardiovascular pathology that compromises the heart's structure or function.

`Cerebrovascular disease`: References to diagnosed pathologies that affect cerebral circulation or blood vessels within the brain.

`Oncological Disease`: Refers to confirmed diagnoses associated with malignant growths or tumors, which arise from uncontrolled and abnormal cell division.

`Respiratory disease`: References to diagnosed pathologies that compromise the structure or function of the respiratory tract.

`Obesity`: Diagnosis of the condition characterized by excessive body fat that adversely affects a patient's health. (overweight and BMI will not be extracted under this label).

`Diabetes`: Diagnosis of any form of diabetes mellitus, chronic disease that occurs either when the pancreas does not produce enough insulin or when the body cannot effectively use the insulin it produces.

`Infectious disease`: Diagnosed conditions that pertain to diseases caused by infectious pathogens, such as bacteria, viruses, fungi, or parasites.

`Kidney disease`: Diagnoses related to pathologies that compromise the renal function or structure.

`Mental disorder`: Diagnoses encompassing a wide array of psychiatric or psychological disorders that affect cognitive, emotional, or behavioral function.

`Alzheimer Disease`: Specific diagnosis of Alzheimer's disease, a neurodegenerative disorder characterized by progressive cognitive decline.

`Patient info header`: The section of a document that contains essential details about the patient such as the patient's full name, date of birth, gender, contact information, insurance details and any other pertinent demographic data necessary for accurate patient identification.

`Medical History Header`: Identifies the section of a medical document that contains a summary of the patient's medical conditions. It encompasses details about the patient's overall health, including chronic illnesses, past injuries, and significant events related to their health.

`Clinical History Header`: Identifies section headers that refer to the patient's clinical history, including previous and ongoing healthcare encounters and interventions.

`History of Present Illness Header`: Identifies section headers that refer to the narrative description of the development of the patient's present illness from the first sign or symptom until the present.

`Medications Header`: Identifies section headers that pertain to the patient's current and past medications.

`Allergies Header`: Identifies section headers that detail the patient's known allergies, including drug allergies and other types of hypersensitivity reactions.

`Laboratory Results Header`: Identifies section headers that include results of lab tests, such as blood tests, urine tests, or other laboratory examinations.

`Imaging Studies Header`: Identifies section headers that summarize the findings of imaging studies, such as X-rays, CT scans, or MRI scans.

`Diagnosis Header`: Identifies section headers that list the patient's current and past diagnoses.

`Treatment Plan Header`: Identifies section headers that outline the patient's management plan, including medications, therapies, surgeries, or other interventions.

## Predicted Entities

`Heart disease`, `Cerebrovascular disease`, `Respiratory disease`, `Alzheimer Disease`, `Obesity`, `Oncological Disease`, `Diabetes`, `Infectious disease`, `Kidney disease`, `Mental disorder`, `Patient info header`, `Medical History Header`, `Clinical History Header`, `History of Present Illness Header`, `Medications Header`, `Allergies Header`, `Laboratory Results Header`, `Imaging Studies Header`, `Diagnosis Header`, `Treatment Plan Header`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_section_header_diagnosis_en_5.0.0_3.0_1690389774550.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_section_header_diagnosis_en_5.0.0_3.0_1690389774550.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
# Annotator that transforms a text column from dataframe into an Annotation ready for NLP
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
        
sentenceDetector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")
 
# Tokenizer splits words in a relevant format for NLP
tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

# Clinical word embeddings trained on PubMED dataset
word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_section_header_diagnosis", "en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")\
    .setLabelCasing("upper") #decide if we want to return the tags in upper or lower case 

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

nlpPipeline = Pipeline(stages=[
        documentAssembler,
        sentenceDetector,
        tokenizer,
        word_embeddings,
        clinical_ner,
        ner_converter])


text = '''
Patient Name: Samantha Johnson
Age: 52
Gender: Female
Patient Info:
Name: Samantha Johnson
Age: 52
Gender: Female
Medical History:
Patient has a history of Chronic respiratory disease.
Clinical History:
Patient presented with shortness of breath and chest pain.
Chief Complaint:
Patient complained of chest pain and difficulty breathing.
History of Present Illness:
Patient has been experiencing chest pain and shortness of breath for the past week. Symptoms were relieved by medication at first but became worse over time.
Past Medical History:
Patient has a history of Asthma and was previously diagnosed with Bronchitis.
Medications:
Patient is currently taking Albuterol, Singulair, and Advair for respiratory issues.
Allergies:
Patient has a documented allergy to Penicillin.
Physical Examination:
Patient had diffuse wheezing and decreased breath sounds on lung auscultation. Heart rate and rhythm were regular.
Laboratory Results:
Pulmonary function test results showed a decrease in Forced Expiratory Volume in one second (FEV1).
Imaging Studies:
Chest x-ray showed bilateral infiltrates consistent with Chronic obstructive pulmonary disease (COPD).
Diagnosis:
The patient was diagnosed with COPD exacerbation.
Treatment Plan:
The patient was managed with nebulized bronchodilators, steroid therapy, and oxygen as needed. The patient was discharged with instructions to continue bronchodilator and steroid therapy and to follow up with primary care physician in two weeks.
'''


data = spark.createDataFrame([[text]]).toDF("text")

result = nlpPipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

// Tokenizer splits words in a relevant format for NLP
val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

// Clinical word embeddings trained on PubMED dataset
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_section_header_diagnosis", "en", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")
  .setLabelCasing("upper") // decide if we want to return the tags in upper or lower case

val ner_converter = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")

val nlpPipeline = new Pipeline()
  .setStages(Array(documentAssembler, sentenceDetector, tokenizer, word_embeddings, clinical_ner, ner_converter))

val text = '''
Patient Name: Samantha Johnson
Age: 52
Gender: Female
Patient Info:
Name: Samantha Johnson
Age: 52
Gender: Female
Medical History:
Patient has a history of Chronic respiratory disease.
Clinical History:
Patient presented with shortness of breath and chest pain.
Chief Complaint:
Patient complained of chest pain and difficulty breathing.
History of Present Illness:
Patient has been experiencing chest pain and shortness of breath for the past week. Symptoms were relieved by medication at first but became worse over time.
Past Medical History:
Patient has a history of Asthma and was previously diagnosed with Bronchitis.
Medications:
Patient is currently taking Albuterol, Singulair, and Advair for respiratory issues.
Allergies:
Patient has a documented allergy to Penicillin.
Physical Examination:
Patient had diffuse wheezing and decreased breath sounds on lung auscultation. Heart rate and rhythm were regular.
Laboratory Results:
Pulmonary function test results showed a decrease in Forced Expiratory Volume in one second (FEV1).
Imaging Studies:
Chest x-ray showed bilateral infiltrates consistent with Chronic obstructive pulmonary disease (COPD).
Diagnosis:
The patient was diagnosed with COPD exacerbation.
Treatment Plan:
The patient was managed with nebulized bronchodilators, steroid therapy, and oxygen as needed. The patient was discharged with instructions to continue bronchodilator and steroid therapy and to follow up with primary care physician in two weeks.
'''

val data: DataFrame = Seq(text).toDS.toDF("text")

val result = nlpPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
|index|chunks|begin|end|sentence\_id|entities|confidence|
|---|---|---|---|---|---|---|
|0|Patient Info|55|66|0|PATIENT\_INFO\_HEADER|0\.91190004|
|1|Medical History|115|129|0|MEDICAL\_HISTORY\_HEADER|0\.8115|
|2|Chronic respiratory disease|157|183|0|RESPIRATORY\_DISEASE|0\.7356667|
|3|Clinical History|186|201|1|CLINICAL\_HISTORY\_HEADER|0\.76595|
|4|Chief Complaint|263|277|2|CHIEF\_COMPLAINT\_HEADER|0\.8484|
|5|History of Present Illness|339|364|3|HISTORY\_PRES\_ILNESS\_HEADER|0\.9933|
|6|Past Medical History|525|544|5|MEDICAL\_HISTORY\_HEADER|0\.7084667|
|7|Asthma|572|577|5|RESPIRATORY\_DISEASE|0\.9994|
|8|Bronchitis|613|622|5|RESPIRATORY\_DISEASE|0\.8429|
|9|Medications|625|635|6|MEDICATIONS\_HEADER|0\.9991|
|10|Allergies|723|731|7|ALLERGIES\_HEADER|0\.9999|
|11|Laboratory Results|919|936|10|LAB\_RESULTS\_HEADER|0\.95780003|
|12|Imaging Studies|1039|1053|11|IMAGING\_HEADER|0\.93614995|
|13|Chronic obstructive pulmonary disease|1113|1149|11|RESPIRATORY\_DISEASE|0\.816625|
|14|COPD|1152|1155|11|RESPIRATORY\_DISEASE|0\.9985|
|15|Diagnosis|1159|1167|12|DIAGNOSIS\_HEADER|0\.9993|
|16|COPD exacerbation|1201|1217|12|RESPIRATORY\_DISEASE|0\.87365|
|17|Treatment Plan|1220|1233|13|TREATMENT\_PLAN\_HEADER|0\.95054996|
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_section_header_diagnosis|
|Compatibility:|Healthcare NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|3.0 MB|

## References

trained by  in-house datasets

## Benchmarking

```bash
                       label   tp  fp  fn  total  precision   recall       f1
          B-Allergies_header  165   2   3    168   0.988024 0.982143 0.985075
          I-Allergies_header   72   4   2     74   0.947368 0.972973 0.960000
                 B-Alzheimer  372   5   2    374   0.986737 0.994652 0.990679
                 I-Alzheimer  253   3   2    255   0.988281 0.992157 0.990215
   B-Cerebrovascular_disease  298  23  23    321   0.928349 0.928349 0.928349
   I-Cerebrovascular_disease  304  15  11    315   0.952978 0.965079 0.958991
    B-Chief_complaint_header  216   5  22    238   0.977376 0.907563 0.941176
    I-Chief_complaint_header  204   5  27    231   0.976077 0.883117 0.927273
   B-Clinical_history_header  165  40   4    169   0.804878 0.976331 0.882353
   I-Clinical_history_header  165  40   5    170   0.804878 0.970588 0.880000
                  B-Diabetes  806  19  14    820   0.976970 0.982927 0.979939
                  I-Diabetes  742  16   5    747   0.978892 0.993307 0.986047
          B-Diagnosis_header  251   8  12    263   0.969112 0.954373 0.961686
          I-Diagnosis_header   13   5   6     19   0.722222 0.684211 0.702703
             B-Heart_disease  846  24  31    877   0.972414 0.964652 0.968517
             I-Heart_disease  666  25  25    691   0.963821 0.963821 0.963821
B-History_pres_ilness_header  217   2   1    218   0.990868 0.995413 0.993135
I-History_pres_ilness_header  729  12   5    734   0.983806 0.993188 0.988475
            B-Imaging_header  181   6   5    186   0.967914 0.973118 0.970509
            I-Imaging_header  203   6   3    206   0.971292 0.985437 0.978313
        B-Infectious_disease  279  41  19    298   0.871875 0.936242 0.902913
        I-Infectious_disease  278  22  14    292   0.926667 0.952055 0.939189
            B-Kidney_disease  520   1   5    525   0.998081 0.990476 0.994264
            I-Kidney_disease  915   0   6    921   1.000000 0.993485 0.996732
        B-Lab_results_header  213   0  12    225   1.000000 0.946667 0.972603
        I-Lab_results_header  259   1  18    277   0.996154 0.935018 0.964618
    B-Medical_history_header  443  23  21    464   0.950644 0.954741 0.952688
    I-Medical_history_header  751  40  28    779   0.949431 0.964056 0.956688
        B-Medications_header  226   7   9    235   0.969957 0.961702 0.965812
        I-Medications_header   70   8   8     78   0.897436 0.897436 0.897436
           B-Mental_disorder  467  26  28    495   0.947262 0.943434 0.945344
           I-Mental_disorder  320  18  19    339   0.946746 0.943953 0.945347
                   B-Obesity  605   0   8    613   1.000000 0.986949 0.993432
       B-Oncological_disease  398  23   8    406   0.945368 0.980296 0.962515
       I-Oncological_disease  411  12   5    416   0.971631 0.987981 0.979738
       B-Patient_info_header  285   8   5    290   0.972696 0.982759 0.977702
       I-Patient_info_header  291   8   4    295   0.973244 0.986441 0.979798
       B-Respiratory_disease 1077  18  14   1091   0.983562 0.987168 0.985361
       I-Respiratory_disease  585  11  14    599   0.981544 0.976628 0.979079
     B-Treatment_plan_header  263  15   9    272   0.946043 0.966912 0.956364
     I-Treatment_plan_header  263  15   1    264   0.946043 0.996212 0.970480
               Macro-average  15787 562 463  -     0.951869  0.95936  0.95560
               Micro-average  15787 562 463  -     0.965624  0.97150  0.96855
```
