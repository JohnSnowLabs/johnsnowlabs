---
layout: model
title: Detect Clinical Entities (langtest)
author: John Snow Labs
name: ner_jsl_langtest
date: 2023-07-31
tags: [licensed, clinical, ner, en, langtest]
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

Pretrained named entity recognition deep learning model for clinical terminology. This NER model is trained with the embeddings_clinical word embeddings model, so be sure to use the same embeddings in the pipeline.. This model is augmented of [`ner_jsl`](https://nlp.johnsnowlabs.com/2022/10/19/ner_jsl_en.html).

## Predicted Entities

`Injury_or_Poisoning`, `Direction`, `Test`, `Admission_Discharge`, `Death_Entity`, `Relationship_Status`, `Duration`, `Respiration`, `Hyperlipidemia`, `Birth_Entity`, `Age`, `Labour_Delivery`, `Family_History_Header`, `BMI`, `Temperature`, `Alcohol`, `Kidney_Disease`, `Oncological`, `Medical_History_Header`, `Cerebrovascular_Disease`, `Oxygen_Therapy`, `O2_Saturation`, `Psychological_Condition`, `Heart_Disease`, `Employment`, `Obesity`, `Disease_Syndrome_Disorder`, `Pregnancy`, `ImagingFindings`, `Procedure`, `Medical_Device`, `Race_Ethnicity`, `Section_Header`, `Symptom`, `Treatment`, `Substance`, `Route`, `Drug_Ingredient`, `Blood_Pressure`, `Diet`, `External_body_part_or_region`, `LDL`, `VS_Finding`, `Allergen`, `EKG_Findings`, `Imaging_Technique`, `Triglycerides`, `RelativeTime`, `Gender`, `Pulse`, `Social_History_Header`, `Substance_Quantity`, `Diabetes`, `Modifier`, `Internal_organ_or_component`, `Clinical_Dept`, `Form`, `Drug_BrandName`, `Strength`, `Fetus_NewBorn`, `RelativeDate`, `Height`, `Test_Result`, `Sexually_Active_or_Sexual_Orientation`, `Frequency`, `Time`, `Weight`, `Vaccine`, `Vaccine_Name`, `Vital_Signs_Header`, `Communicable_Disease`, `Dosage`, `Overweight`, `Hypertension`, `HDL`, `Total_Cholesterol`, `Smoking`, `Date`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_JSL/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_jsl_langtest_en_5.0.0_3.0_1690799624953.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_jsl_langtest_en_5.0.0_3.0_1690799624953.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_jsl_langtest", "en", "clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

nlp_pipeline = Pipeline(
    stages=[
        document_assembler, 
        sentence_detector, 
        tokenizer, 
        word_embeddings, 
        clinical_ner, 
        ner_converter
    ])

text ="""The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."""

data = spark.createDataFrame([[text]]).toDF("text")

result = nlp_pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")
    
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_large", "en", "clinical/models")\
    .setInputCols(Array("sentence", "token"))\
    .setOutputCol("embeddings")

val posology_ner_model = MedicalNerModel.pretrained("ner_jsl_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("posology_ner")

val posology_ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("posology_ner_chunk")

val posology_pipeline = new PipelineModel().setStages(Array(document_assembler, 
                                                   sentence_detector,
                                                   tokenizer,
                                                   word_embeddings,
                                                   posology_ner_model,
                                                   posology_ner_converter))

text = """The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."""

val data = Seq(text).toDS.toDF("text")

val result = model.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------------+-----+---+--------------------+
|               chunk|begin|end|           ner_label|
+--------------------+-----+---+--------------------+
|          21-day-old|   17| 26|                 Age|
|           Caucasian|   28| 36|      Race_Ethnicity|
|                male|   38| 41|              Gender|
|          for 2 days|   48| 57|            Duration|
|          congestion|   62| 71|             Symptom|
|                 mom|   75| 77|              Gender|
|           discharge|  106|114| Admission_Discharge|
|               nares|  135|139|External_body_par...|
|                 she|  147|149|              Gender|
|                mild|  168|171|            Modifier|
|problems with his...|  173|213|             Symptom|
|   perioral cyanosis|  237|253|             Symptom|
|         retractions|  258|268|             Symptom|
|   Influenza vaccine|  325|341|        Vaccine_Name|
|         One day ago|  344|354|        RelativeDate|
|                 mom|  357|359|              Gender|
|             Tylenol|  417|423|      Drug_BrandName|
|                Baby|  426|429|                 Age|
|       decreased p.o|  449|461|             Symptom|
|                 His|  472|474|              Gender|
+--------------------+-----+---+--------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_jsl_langtest|
|Compatibility:|Healthcare NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|3.2 MB|

## References

trained by in-house dataset

## Benchmarking

```bash
                 label      tp      fp      fn   total  precision  recall      f1   
            VS_Finding   181.0    48.0    84.0   265.0     0.7904   0.683  0.7328  
             Direction  3422.0   522.0   560.0  3982.0     0.8676  0.8594  0.8635  
           Respiration    57.0     2.0    16.0    73.0     0.9661  0.7808  0.8636  
  Cerebrovascular_D...    74.0    36.0    29.0   103.0     0.6727  0.7184  0.6948  
  Family_History_He...    79.0     6.0     2.0    81.0     0.9294  0.9753  0.9518  
         Heart_Disease   395.0    87.0   133.0   528.0     0.8195  0.7481  0.7822  
       ImagingFindings    38.0    55.0   137.0   175.0     0.4086  0.2171  0.2836  
          RelativeTime   102.0    70.0    90.0   192.0      0.593  0.5313  0.5604  
              Strength   598.0    48.0    58.0   656.0     0.9257  0.9116  0.9186  
               Smoking   124.0     2.0     5.0   129.0     0.9841  0.9612  0.9725  
        Medical_Device  2714.0   482.0   471.0  3185.0     0.8492  0.8521  0.8507  
              Allergen     1.0     4.0    13.0    14.0        0.2  0.0714  0.1053  
          EKG_Findings    28.0    19.0    37.0    65.0     0.5957  0.4308     0.5  
                 Pulse   102.0    29.0    15.0   117.0     0.7786  0.8718  0.8226  
  Psychological_Con...    88.0    12.0    20.0   108.0       0.88  0.8148  0.8462  
            Overweight     2.0     2.0     4.0     6.0        0.5  0.3333     0.4  
         Triglycerides     2.0     0.0     1.0     3.0        1.0  0.6667     0.8  
               Obesity    41.0     7.0     6.0    47.0     0.8542  0.8723  0.8632  
   Admission_Discharge   309.0    28.0     9.0   318.0     0.9169  0.9717  0.9435  
                   HDL     2.0     2.0     1.0     3.0        0.5  0.6667  0.5714  
              Diabetes    91.0    17.0    12.0   103.0     0.8426  0.8835  0.8626  
        Section_Header  3272.0   167.0   167.0  3439.0     0.9514  0.9514  0.9514  
                   Age   558.0    83.0    95.0   653.0     0.8705  0.8545  0.8624  
         O2_Saturation    30.0     8.0    12.0    42.0     0.7895  0.7143    0.75  
        Kidney_Disease    94.0    12.0    24.0   118.0     0.8868  0.7966  0.8393  
                  Test  2145.0   623.0   497.0  2642.0     0.7749  0.8119   0.793  
  Communicable_Disease    16.0    15.0    32.0    48.0     0.5161  0.3333  0.4051  
          Hypertension   139.0     8.0     9.0   148.0     0.9456  0.9392  0.9424  
  External_body_par...  2008.0   455.0   528.0  2536.0     0.8153  0.7918  0.8034  
        Oxygen_Therapy    54.0    15.0    27.0    81.0     0.7826  0.6667    0.72  
              Modifier  2045.0   480.0   677.0  2722.0     0.8099  0.7513  0.7795  
           Test_Result   753.0   203.0   272.0  1025.0     0.7877  0.7346  0.7602  
                   BMI     3.0     0.0     3.0     6.0        1.0     0.5  0.6667  
       Labour_Delivery    49.0    24.0    41.0    90.0     0.6712  0.5444  0.6012  
            Employment   207.0    31.0    64.0   271.0     0.8697  0.7638  0.8134  
         Fetus_NewBorn    40.0    25.0    64.0   104.0     0.6154  0.3846  0.4734  
         Clinical_Dept   806.0   136.0    95.0   901.0     0.8556  0.8946  0.8747  
                  Time    20.0    12.0    21.0    41.0      0.625  0.4878  0.5479  
             Procedure  2455.0   575.0   663.0  3118.0     0.8102  0.7874  0.7986  
                  Diet    29.0     6.0    50.0    79.0     0.8286  0.3671  0.5088  
           Oncological   344.0    82.0    95.0   439.0     0.8075  0.7836  0.7954  
                   LDL     0.0     0.0     3.0     3.0        0.0     0.0     0.0  
               Symptom  6190.0  1617.0  1426.0  7616.0     0.7929  0.8128  0.8027  
           Temperature    70.0    11.0    16.0    86.0     0.8642   0.814  0.8383  
    Vital_Signs_Header   183.0    26.0    22.0   205.0     0.8756  0.8927  0.8841  
     Total_Cholesterol     8.0     1.0     1.0     9.0     0.8889  0.8889  0.8889  
   Relationship_Status    40.0     4.0     5.0    45.0     0.9091  0.8889  0.8989  
        Blood_Pressure   126.0    36.0    24.0   150.0     0.7778    0.84  0.8077  
   Injury_or_Poisoning   380.0   112.0   151.0   531.0     0.7724  0.7156  0.7429  
       Drug_Ingredient  1439.0   177.0   167.0  1606.0     0.8905   0.896  0.8932  
             Treatment   109.0    28.0    82.0   191.0     0.7956  0.5707  0.6646  
             Pregnancy   101.0    20.0    75.0   176.0     0.8347  0.5739  0.6801  
               Vaccine     0.0     0.0     9.0     9.0        0.0     0.0     0.0  
  Disease_Syndrome_...  2543.0   688.0   643.0  3186.0     0.7871  0.7982  0.7926  
                Height    18.0     3.0     9.0    27.0     0.8571  0.6667    0.75  
             Frequency   504.0   108.0   155.0   659.0     0.8235  0.7648  0.7931  
                 Route   737.0   114.0    79.0   816.0      0.866  0.9032  0.8842  
              Duration   277.0   100.0   121.0   398.0     0.7347   0.696  0.7148  
          Death_Entity    37.0    17.0     3.0    40.0     0.6852   0.925  0.7872  
  Internal_organ_or...  5461.0  1326.0  1107.0  6568.0     0.8046  0.8315  0.8178  
          Vaccine_Name     0.0     0.0    12.0    12.0        0.0     0.0     0.0  
               Alcohol    76.0    12.0     9.0    85.0     0.8636  0.8941  0.8786  
    Substance_Quantity     0.0     0.0     6.0     6.0        0.0     0.0     0.0  
                  Date   440.0    16.0    13.0   453.0     0.9649  0.9713  0.9681  
        Hyperlipidemia    30.0     0.0     4.0    34.0        1.0  0.8824  0.9375  
  Social_History_He...    78.0     9.0     8.0    86.0     0.8966   0.907  0.9017  
     Imaging_Technique    26.0    12.0    37.0    63.0     0.6842  0.4127  0.5149  
        Race_Ethnicity   102.0     2.0     5.0   107.0     0.9808  0.9533  0.9668  
        Drug_BrandName   886.0    81.0    86.0   972.0     0.9162  0.9115  0.9139  
          RelativeDate   502.0   153.0   137.0   639.0     0.7664  0.7856  0.7759  
                Gender  5536.0    88.0    66.0  5602.0     0.9844  0.9882  0.9863  
                  Form   183.0    49.0    66.0   249.0     0.7888  0.7349  0.7609  
                Dosage   235.0    44.0    82.0   317.0     0.8423  0.7413  0.7886  
  Medical_History_H...   100.0     7.0    10.0   110.0     0.9346  0.9091  0.9217  
          Birth_Entity     0.0     0.0     6.0     6.0        0.0     0.0     0.0  
             Substance    64.0    13.0    23.0    87.0     0.8312  0.7356  0.7805  
  Sexually_Active_o...     4.0     0.0     0.0     4.0        1.0     1.0     1.0  
                Weight    64.0    18.0    29.0    93.0     0.7805  0.6882  0.7314   
                 macro      -       -       -       -       -       -      0.7224
                 micro      -       -       -       -       -       -      0.8377
```
