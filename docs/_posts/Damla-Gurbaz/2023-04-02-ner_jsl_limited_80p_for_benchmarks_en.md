---
layout: model
title: Detect Clinical Entities
author: John Snow Labs
name: ner_jsl_limited_80p_for_benchmarks
date: 2023-04-02
tags: [ner, licensed, en, clinical, benchmark]
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

`Important Note:` This model is trained with a partial dataset that is used to train [ner_jsl](https://nlp.johnsnowlabs.com/2022/10/19/ner_jsl_en.html); and meant to be used for benchmarking run at [LLMs Healthcare Benchmarks](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/tutorials/academic/LLMs_in_Healthcare).

Pretrained named entity recognition deep learning model for clinical terminology. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state-of-the-art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN. This model is the official version of jsl_ner_wip_clinical model.

Definitions of Predicted Entities:

- `Injury_or_Poisoning`: Physical harm or injury caused to the body, including those caused by accidents, falls, or poisoning of a patient or someone else. 
- `Direction`: All the information relating to the laterality of the internal and external organs. 
- `Test`: Mentions of laboratory, pathology, and radiological tests. 
- `Admission_Discharge`: Terms that indicate the admission and/or the discharge of a patient. 
- `Death_Entity`: Mentions that indicate the death of a patient. 
- `Relationship_Status`: State of patients romantic or social relationships (e.g. single, married, divorced). 
- `Duration`: The duration of a medical treatment or medication use. 
- `Respiration`: Number of breaths per minute. 
- `Hyperlipidemia`: Terms that indicate hyperlipidemia with relevant subtypes and synonims.  
- `Birth_Entity`: Mentions that indicate giving birth. 
- `Age`: All mention of ages, past or present, related to the patient or with anybody else. 
- `Labour_Delivery`: Extractions include stages of labor and delivery. 
- `Family_History_Header`: identifies section headers that correspond to Family History of the patient. 
- `BMI`: Numeric values and other text information related to Body Mass Index. 
- `Temperature`: All mentions that refer to body temperature. 
- `Alcohol`: Terms that indicate alcohol use, abuse or drinking issues of a patient or someone else. 
- `Kidney_Disease`: Terms that refer to any kidney diseases (includes mentions of modifiers such as "Acute" or "Chronic"). 
- `Oncological`: All the cancer, tumor or metastasis related extractions mentioned in the document, of the patient or someone else. 
- `Medical_History_Header`: Identifies section headers that correspond to Past Medical History of a patient. 
- `Cerebrovascular_Disease`: All terms that refer to cerebrovascular diseases and events.  
- `Oxygen_Therapy`: Breathing support triggered by patient or entirely or partially by machine (e.g. ventilator, BPAP, CPAP). 
- `O2_Saturation`: Systemic arterial, venous or peripheral oxygen saturation measurements. 
- `Psychological_Condition`: All the Mental health diagnosis, disorders, conditions or syndromes of a patient or someone else. 
- `Heart_Disease`: All mentions of acquired, congenital or degenerative heart diseases. 
- `Employment`: All mentions of patient or provider occupational titles and employment status . 
- `Obesity`: Terms related to a patient being obese (overweight and BMI are extracted as different labels). 
- `Disease_Syndrome_Disorder`: All the diseases mentioned in the document, of the patient or someone else (excluding diseases that are extracted with their specific labels, such as "Heart_Disease" etc.). 
- `Pregnancy`: All terms related to Pregnancy (excluding terms that are extracted with their specific labels, such as "Labour_Delivery" etc.). 
- `ImagingFindings`: All mentions of radiographic and imagistic findings. 
- `Procedure`: All mentions of invasive medical or surgical procedures or treatments. 
- `Medical_Device`: All mentions related to medical devices and supplies. 
- `Race_Ethnicity`: All terms that refer to racial and national origin of sociocultural groups. 
- `Section_Header`: All the section headers present in the text  (Medical History, Family History, Social History, Physical Examination and Vital signs Headers are extracted separately with their specific labels). 
- `Symptom`: All the symptoms mentioned in the document, of a patient or someone else. 
- `Treatment`: Includes therapeutic and minimally invasive treatment and procedures (invasive treatments or procedures are extracted as "Procedure"). 
- `Substance`: All mentions of substance use related to the patient or someone else (recreational drugs, illicit drugs). 
- `Route`: Drug and medication administration routes available described by [FDA](https://wayback.archive-it.org/7993/20171115111313/https:/www.fda.gov/Drugs/DevelopmentApprovalProcess/FormsSubmissionRequirements/ElectronicSubmissions/DataStandardsManualmonographs/ucm071667.htm). 
- `Drug_Ingredient`: Active ingredient/s found in drug products. 
- `Blood_Pressure`: Systemic blood pressure, mean arterial pressure, systolic and/or diastolic are extracted. 
- `Diet`: All mentions and information regarding patients dietary habits. 
- `External_body_part_or_region`: All mentions related to external body parts or organs that can be examined by naked eye. 
- `LDL`: All mentions related to the lab test and results for LDL (Low Density Lipoprotein). 
- `VS_Finding`: Qualitative data (e.g. Fever, Cyanosis, Tachycardia) and any other symptoms that refers to vital signs. 
- `Allergen`: Allergen related extractions mentioned in the document. 
- `EKG_Findings`: All mentions of EKG readings. 
- `Imaging_Technique`: All mentions of special radiographic views or special imaging techniques used in radiology. 
- `Triglycerides`: All mentions terms related to specific lab test for Triglycerides. 
- `RelativeTime`: Time references that are relative to different times or events (e.g. words such as "approximately", "in the morning"). 
- `Gender`: Gender-specific nouns and pronouns. 
- `Pulse`: Peripheral heart rate, without advanced information like measurement location. 
- `Social_History_Header`: Identifies section headers that correspond to Social History of a patient. 
- `Substance_Quantity`: All mentions of substance quantity (quantitative information related to illicit/recreational drugs). 
- `Diabetes`: All terms related to diabetes mellitus. 
- `Modifier`: Terms that modify the symptoms, diseases or risk factors. If a modifier is included in ICD-10 name of a specific disease, the respective modifier is not extracted separately. 
- `Internal_organ_or_component`: All mentions related to internal body parts or organs that can not be examined by naked eye. 
- `Clinical_Dept`: Terms that indicate the medical and/or surgical departments. 
- `Form`: Drug and medication forms available described by [FDA](https://wayback.archive-it.org/7993/20171115111313/https:/www.fda.gov/Drugs/DevelopmentApprovalProcess/FormsSubmissionRequirements/ElectronicSubmissions/DataStandardsManualmonographs/ucm071667.htm). 
- `Drug_BrandName`: Commercial labeling name chosen by the labeler or the drug manufacturer for a drug containing a single or multiple drug active ingredients. 
- `Strength`: Potency of one unit of drug (or a combination of drugs) the measurement units available are described by [FDA](https://wayback.archive-it.org/7993/20171115111313/https:/www.fda.gov/Drugs/DevelopmentApprovalProcess/FormsSubmissionRequirements/ElectronicSubmissions/DataStandardsManualmonographs/ucm071667.htm). 
- `Fetus_NewBorn`: All terms related to fetus, infant, new born (excluding terms that are extracted with their specific labels, such as "Labour_Delivery", "Pregnancy" etc.). 
- `RelativeDate`: Temporal references that are relative to the date of the text or to any other specific date (e.g. "approximately two years ago", "about two days ago"). 
- `Height`: All mentions related to a patients height. 
- `Test_Result`: Terms related to all the test results present in the document (clinical tests results are included). 
- `Sexually_Active_or_Sexual_Orientation`: All terms that are related to sexuality, sexual orientations and sexual activity. 
- `Frequency`: Frequency of administration for a dose prescribed. 
- `Time`: Specific time references (hour and/or minutes). 
- `Weight`: All mentions related to a patients weight. 
- `Vaccine`: Generic and brand name of vaccines or vaccination procedure. 
- `Vital_Signs_Header`: Identifies section headers that correspond to Vital Signs of a patient. 
- `Communicable_Disease`: Includes all mentions of communicable diseases. 
- `Dosage`: Quantity prescribed by the physician for an active ingredient; measurement units are available described by [FDA](https://wayback.archive-it.org/7993/20171115111313/https:/www.fda.gov/Drugs/DevelopmentApprovalProcess/FormsSubmissionRequirements/ElectronicSubmissions/DataStandardsManualmonographs/ucm071667.htm). 
- `Overweight`: Terms related to the patient being overweight (BMI and Obesity is extracted separately). 
- `Hypertension`: All terms related to Hypertension (quantitative data such as 150/100 is extracted as Blood_Pressure). 
- `HDL`: Terms related to the lab test for HDL (High Density Lipoprotein). 
- `Total_Cholesterol`: Terms related to the lab test and results for cholesterol. 
- `Smoking`: All mentions of smoking status of a patient. 
- `Date`: Mentions of an exact date, in any format, including day number, month and/or year.

## Predicted Entities

`Injury_or_Poisoning`, `Direction`, `Test`, `Admission_Discharge`, `Death_Entity`, `Relationship_Status`, `Duration`, `Respiration`, `Hyperlipidemia`, `Birth_Entity`, `Age`, `Labour_Delivery`, `Family_History_Header`, `BMI`, `Temperature`, `Alcohol`, `Kidney_Disease`, `Oncological`, `Medical_History_Header`, `Cerebrovascular_Disease`, `Oxygen_Therapy`, `O2_Saturation`, `Psychological_Condition`, `Heart_Disease`, `Employment`, `Obesity`, `Disease_Syndrome_Disorder`, `Pregnancy`, `ImagingFindings`, `Procedure`, `Medical_Device`, `Race_Ethnicity`, `Section_Header`, `Symptom`, `Treatment`, `Substance`, `Route`, `Drug_Ingredient`, `Blood_Pressure`, `Diet`, `External_body_part_or_region`, `LDL`, `VS_Finding`, `Allergen`, `EKG_Findings`, `Imaging_Technique`, `Triglycerides`, `RelativeTime`, `Gender`, `Pulse`, `Social_History_Header`, `Substance_Quantity`, `Diabetes`, `Modifier`, `Internal_organ_or_component`, `Clinical_Dept`, `Form`, `Drug_BrandName`, `Strength`, `Fetus_NewBorn`, `RelativeDate`, `Height`, `Test_Result`, `Sexually_Active_or_Sexual_Orientation`, `Frequency`, `Time`, `Weight`, `Vaccine`, `Vaccine_Name`, `Vital_Signs_Header`, `Communicable_Disease`, `Dosage`, `Overweight`, `Hypertension`, `HDL`, `Total_Cholesterol`, `Smoking`, `Date`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_JSL/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_jsl_limited_80p_for_benchmarks_en_4.3.2_3.0_1680468591578.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_jsl_limited_80p_for_benchmarks_en_4.3.2_3.0_1680468591578.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence") 

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner = MedicalNerModel.pretrained("ner_jsl_limited_80p_for_benchmarks", "en", "clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")
    
ner_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

ner_pipeline = Pipeline(stages=[
    documentAssembler, 
    sentenceDetector,
    tokenizer,
    word_embeddings,
    ner,
    ner_converter])


data = spark.createDataFrame([["""The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea.
"""]]).toDF("text")

result = ner_pipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
        .setInputCol("text")
        .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
        .setInputCols("document") 
        .setOutputCol("sentence")

val tokenizer = new Tokenizer()
        .setInputCols("sentence")
        .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
        .setInputCols(Array("sentence", "token"))
        .setOutputCol("embeddings")

val jsl_ner = MedicalNerModel.pretrained("ner_jsl_limited_80p_for_benchmarks",  "en",  "clinical/models")
        .setInputCols(Array("sentence", "token", "embeddings"))
        .setOutputCol("jsl_ner")

val jsl_ner_converter = new NerConverterInternal()
        .setInputCols(Array("sentence", "token", "jsl_ner"))
        .setOutputCol("ner_chunk")

val jsl_ner_pipeline = new Pipeline().setStages(Array(
            documentAssembler, 
            sentenceDetector, 
            tokenizer, 
            embeddings, 
            jsl_ner, 
            jsl_ner_converter))


val data = Seq("""The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea.""").toDS.toDF("text")

val result = jsl_ner_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
|    | chunks                                    |   begin |   end |   sentence_id | entities                     |
|---:|:------------------------------------------|--------:|------:|--------------:|:-----------------------------|
|  0 | 21-day-old                                |      18 |    27 |             0 | Age                          |
|  1 | Caucasian                                 |      29 |    37 |             0 | Race_Ethnicity               |
|  2 | male                                      |      39 |    42 |             0 | Gender                       |
|  3 | 2 days                                    |      53 |    58 |             0 | Duration                     |
|  4 | congestion                                |      63 |    72 |             0 | Symptom                      |
|  5 | mom                                       |      76 |    78 |             0 | Gender                       |
|  6 | suctioning yellow discharge               |      89 |   115 |             0 | Symptom                      |
|  7 | nares                                     |     136 |   140 |             0 | External_body_part_or_region |
|  8 | she                                       |     148 |   150 |             0 | Gender                       |
|  9 | mild                                      |     169 |   172 |             0 | Modifier                     |
| 10 | problems with his breathing while feeding |     174 |   214 |             0 | Symptom                      |
| 11 | perioral cyanosis                         |     238 |   254 |             0 | Symptom                      |
| 12 | retractions                               |     259 |   269 |             0 | Symptom                      |
| 13 | Influenza vaccine                         |     326 |   342 |             1 | Vaccine_Name                 |
| 14 | One day ago                               |     345 |   355 |             2 | RelativeDate                 |
| 15 | mom                                       |     358 |   360 |             2 | Gender                       |
| 16 | tactile temperature                       |     377 |   395 |             2 | Symptom                      |
| 17 | Tylenol                                   |     418 |   424 |             2 | Drug_BrandName               |
| 18 | Baby                                      |     427 |   430 |             3 | Age                          |
| 19 | decreased p.o                             |     450 |   462 |             3 | Symptom                      |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_jsl_limited_80p_for_benchmarks|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|15.3 MB|

## References

Trained on data gathered and manually annotated by John Snow Labs. https://www.johnsnowlabs.com/data/

## Benchmarking

```bash
                 label      tp      fp      fn   total  precision  recall      f1  
            VS_Finding   164.0    69.0    40.0   204.0     0.7039  0.8039  0.7506  
             Direction  3394.0   452.0   367.0  3761.0     0.8825  0.9024  0.8923  
           Respiration    74.0     3.0     5.0    79.0      0.961  0.9367  0.9487  
  Cerebrovascular_D...   103.0    27.0    14.0   117.0     0.7923  0.8803   0.834  
  Family_History_He...    80.0     1.0     1.0    81.0     0.9877  0.9877  0.9877  
         Heart_Disease   432.0    74.0    64.0   496.0     0.8538   0.871  0.8623  
       ImagingFindings    66.0    32.0   102.0   168.0     0.6735  0.3929  0.4962  
          RelativeTime   103.0    55.0    82.0   185.0     0.6519  0.5568  0.6006  
              Strength   552.0    56.0    37.0   589.0     0.9079  0.9372  0.9223  
               Smoking   105.0     3.0     9.0   114.0     0.9722  0.9211  0.9459  
        Medical_Device  3043.0   530.0   364.0  3407.0     0.8517  0.8932  0.8719  
              Allergen     1.0     1.0    17.0    18.0        0.5  0.0556     0.1  
          EKG_Findings    42.0    36.0    53.0    95.0     0.5385  0.4421  0.4855  
                 Pulse   106.0    23.0    17.0   123.0     0.8217  0.8618  0.8413  
  Psychological_Con...   103.0    35.0    20.0   123.0     0.7464  0.8374  0.7893  
            Overweight     5.0     3.0     0.0     5.0      0.625     1.0  0.7692  
         Triglycerides     3.0     0.0     2.0     5.0        1.0     0.6    0.75  
               Obesity    34.0     4.0     7.0    41.0     0.8947  0.8293  0.8608  
   Admission_Discharge   283.0    30.0     7.0   290.0     0.9042  0.9759  0.9386  
                   HDL     2.0     1.0     0.0     2.0     0.6667     1.0     0.8  
              Diabetes   107.0     8.0     3.0   110.0     0.9304  0.9727  0.9511  
        Section_Header  3184.0   185.0   118.0  3302.0     0.9451  0.9643  0.9546  
                   Age   524.0    49.0    61.0   585.0     0.9145  0.8957   0.905  
         O2_Saturation    29.0    10.0    13.0    42.0     0.7436  0.6905   0.716  
        Kidney_Disease    82.0     8.0    17.0    99.0     0.9111  0.8283  0.8677  
                  Test  2063.0   451.0   414.0  2477.0     0.8206  0.8329  0.8267  
  Communicable_Disease    22.0     9.0     9.0    31.0     0.7097  0.7097  0.7097  
          Hypertension   124.0     4.0     7.0   131.0     0.9688  0.9466  0.9575  
  External_body_par...  2277.0   405.0   353.0  2630.0      0.849  0.8658  0.8573  
        Oxygen_Therapy    70.0    17.0    10.0    80.0     0.8046   0.875  0.8383  
              Modifier  1960.0   357.0   549.0  2509.0     0.8459  0.7812  0.8123  
           Test_Result   796.0   178.0   210.0  1006.0     0.8172  0.7913   0.804  
                   BMI     4.0     0.0     1.0     5.0        1.0     0.8  0.8889  
       Labour_Delivery    55.0    31.0    26.0    81.0     0.6395   0.679  0.6587  
            Employment   192.0    24.0    48.0   240.0     0.8889     0.8  0.8421  
         Fetus_NewBorn    24.0    19.0    43.0    67.0     0.5581  0.3582  0.4364  
         Clinical_Dept   795.0    57.0    85.0   880.0     0.9331  0.9034   0.918  
                  Time    22.0    11.0     9.0    31.0     0.6667  0.7097  0.6875  
             Procedure  2458.0   413.0   503.0  2961.0     0.8561  0.8301  0.8429  
                  Diet    21.0     6.0    30.0    51.0     0.7778  0.4118  0.5385  
           Oncological   342.0    62.0    77.0   419.0     0.8465  0.8162  0.8311  
                   LDL     4.0     0.0     0.0     4.0        1.0     1.0     1.0  
               Symptom  5777.0  1069.0  1277.0  7054.0     0.8439   0.819  0.8312  
           Temperature    86.0     5.0    12.0    98.0     0.9451  0.8776  0.9101  
    Vital_Signs_Header   201.0    23.0    14.0   215.0     0.8973  0.9349  0.9157  
   Relationship_Status    44.0     1.0     3.0    47.0     0.9778  0.9362  0.9565  
     Total_Cholesterol    10.0     5.0     7.0    17.0     0.6667  0.5882   0.625  
        Blood_Pressure   131.0    35.0    23.0   154.0     0.7892  0.8506  0.8188  
   Injury_or_Poisoning   431.0    71.0   140.0   571.0     0.8586  0.7548  0.8034  
       Drug_Ingredient  1508.0   106.0   158.0  1666.0     0.9343  0.9052  0.9195  
             Treatment   124.0    36.0    68.0   192.0      0.775  0.6458  0.7045  
             Pregnancy    89.0    40.0    38.0   127.0     0.6899  0.7008  0.6953  
               Vaccine     1.0     0.0     4.0     5.0        1.0     0.2  0.3333  
  Disease_Syndrome_...  2471.0   551.0   432.0  2903.0     0.8177  0.8512  0.8341  
                Height    12.0     3.0     9.0    21.0        0.8  0.5714  0.6667  
             Frequency   500.0   103.0   110.0   610.0     0.8292  0.8197  0.8244  
                 Route   797.0    77.0    70.0   867.0     0.9119  0.9193  0.9156  
              Duration   258.0    52.0   106.0   364.0     0.8323  0.7088  0.7656  
          Death_Entity    38.0     7.0     3.0    41.0     0.8444  0.9268  0.8837  
  Internal_organ_or...  5434.0   839.0   984.0  6418.0     0.8663  0.8467  0.8564  
          Vaccine_Name     5.0     1.0     3.0     8.0     0.8333   0.625  0.7143  
               Alcohol    78.0    13.0     6.0    84.0     0.8571  0.9286  0.8914  
    Substance_Quantity     0.0     9.0     1.0     1.0        0.0     0.0     0.0  
                  Date   455.0    25.0    12.0   467.0     0.9479  0.9743  0.9609  
        Hyperlipidemia    34.0     0.0     2.0    36.0        1.0  0.9444  0.9714  
  Social_History_He...    75.0     3.0     3.0    78.0     0.9615  0.9615  0.9615  
     Imaging_Technique    25.0    16.0    23.0    48.0     0.6098  0.5208  0.5618  
        Race_Ethnicity   110.0     0.0     2.0   112.0        1.0  0.9821   0.991  
        Drug_BrandName   788.0    65.0    53.0   841.0     0.9238   0.937  0.9303  
          RelativeDate   488.0   150.0    98.0   586.0     0.7649  0.8328  0.7974  
                Gender  5189.0    66.0    55.0  5244.0     0.9874  0.9895  0.9885  
                Dosage   229.0    32.0    69.0   298.0     0.8774  0.7685  0.8193  
                  Form   179.0    22.0    37.0   216.0     0.8905  0.8287  0.8585  
  Medical_History_H...   112.0     7.0     6.0   118.0     0.9412  0.9492  0.9451  
          Birth_Entity     2.0     2.0     5.0     7.0        0.5  0.2857  0.3636  
             Substance    60.0     6.0    11.0    71.0     0.9091  0.8451  0.8759  
  Sexually_Active_o...     2.0     1.0     1.0     3.0     0.6667  0.6667  0.6667  
                Weight    77.0     8.0    12.0    89.0     0.9059  0.8652  0.8851
                 macro     -        -       -      -          -      -     0.7914
                 micro     -        -       -      -          -      -     0.8691
  

```
