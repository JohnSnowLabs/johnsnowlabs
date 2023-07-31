---
layout: model
title: Social Determinants of Health (LangTest)
author: John Snow Labs
name: ner_sdoh_langtest
date: 2023-07-31
tags: [licensed, clinical, en, social_determinants, ner, public_health, sdoh, langtest]
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

SDOH NER model is designed to detect and label social determinants of health (SDOH) entities within text data. Social determinants of health are crucial factors that influence individuals’ health outcomes, encompassing various social, economic, and environmental element. The model has been trained using advanced machine learning techniques on a diverse range of text sources. The model can accurately recognize and classify a wide range of SDOH entities, including but not limited to factors such as socioeconomic status, education level, housing conditions, access to healthcare services, employment status, cultural and ethnic background, neighborhood characteristics, and environmental factors. The model’s accuracy and precision have been carefully validated against expert-labeled data to ensure reliable and consistent results. This model is augmented version of [ner_sdoh](https://nlp.johnsnowlabs.com/2023/06/13/ner_sdoh_en.html)

## Predicted Entities

`Access_To_Care`, `Age`, `Alcohol`, `Childhood_Event`, `Community_Safety`, `Diet`, `Disability`, `Eating_Disorder`, `Education`, `Employment`, `Environmental_Condition`, `Exercise`, `Family_Member`, `Financial_Status`, `Food_Insecurity`, `Gender`, `Geographic_Entity`, `Healthcare_Institution`, `Housing`, `Hyperlipidemia`, `Hypertension`, `Income`, `Insurance_Status`, `Language`, `Legal_Issues`, `Marital_Status`, `Mental_Health`, `Obesity`, `Other_Disease`, `Other_SDoH_Keywords`, `Population_Group`, `Quality_Of_Life`, `Race_Ethnicity`, `Sexual_Activity`, `Sexual_Orientation`, `Smoking`, `Social_Exclusion`, `Social_Support`, `Spiritual_Beliefs`, `Substance_Duration`, `Substance_Frequency`, `Substance_Quantity`, `Substance_Use`, `Transportation`, `Violence_Or_Abuse`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_NER/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/SOCIAL_DETERMINANT_NER.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_langtest_en_5.0.0_3.0_1690799658986.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_langtest_en_5.0.0_3.0_1690799658986.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_sdoh_langtest", "en", "clinical/models")\
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

val sentence_detector = SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_sdoh_langtest", "en", "clinical/models")
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
+--------------------+-----+---+-------------------+
|               chunk|begin|end|          ner_label|
+--------------------+-----+---+-------------------+
|        55 years old|    9| 20|                Age|
|            New York|   33| 40|  Geographic_Entity|
|            divorced|   45| 52|     Marital_Status|
|    Mexcian American|   54| 69|     Race_Ethnicity|
|               woman|   71| 75|             Gender|
|  financial problems|   82| 99|   Financial_Status|
|                 She|  102|104|             Gender|
|             Spanish|  113|119|           Language|
|          Portuguese|  125|134|           Language|
|                 She|  137|139|             Gender|
|           apartment|  153|161|            Housing|
|                 She|  164|166|             Gender|
|            diabetes|  193|200|      Other_Disease|
|    hospitalizations|  268|283|Other_SDoH_Keywords|
|  cleaning assistant|  342|359|         Employment|
|access health ins...|  372|394|   Insurance_Status|
|                 She|  416|418|             Gender|
|                 son|  426|428|      Family_Member|
|             student|  433|439|          Education|
|             college|  444|450|          Education|
|          depression|  482|491|      Mental_Health|
|                 She|  494|496|             Gender|
|                 she|  507|509|             Gender|
|               rehab|  517|521|     Access_To_Care|
|                 her|  542|544|             Gender|
|      catholic faith|  546|559|  Spiritual_Beliefs|
|             support|  575|581|     Social_Support|
|                 She|  593|595|             Gender|
|          etoh abuse|  619|628|            Alcohol|
|                 her|  644|646|             Gender|
|               teens|  648|652|                Age|
|                 She|  655|657|             Gender|
|                 she|  667|669|             Gender|
|               daily|  682|686|Substance_Frequency|
|             drinker|  688|694|            Alcohol|
|            30 years|  700|707| Substance_Duration|
|            drinking|  724|731|            Alcohol|
|                beer|  733|736|            Alcohol|
|               daily|  738|742|Substance_Frequency|
|                 She|  745|747|             Gender|
|              smokes|  749|754|            Smoking|
|              a pack|  756|761| Substance_Quantity|
|          cigarettes|  766|775|            Smoking|
|               a day|  777|781|Substance_Frequency|
|                 She|  784|786|             Gender|
|                 DUI|  792|794|       Legal_Issues|
+--------------------+-----+---+-------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_sdoh_langtest|
|Compatibility:|Healthcare NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|3.0 MB|

## Benchmarking

```bash
                 label       tp     fp     fn    total  precision  recall      f1  
   Other_SDoH_Keywords    359.0  123.0   99.0    458.0     0.7448  0.7838  0.7638  
             Education     96.0   24.0   19.0    115.0        0.8  0.8348   0.817  
      Population_Group     14.0    1.0   14.0     28.0     0.9333     0.5  0.6512  
       Quality_Of_Life     78.0   25.0   20.0     98.0     0.7573  0.7959  0.7761  
       Food_Insecurity     29.0    5.0    3.0     32.0     0.8529  0.9063  0.8788  
               Housing    321.0   57.0   67.0    388.0     0.8492  0.8273  0.8381  
               Smoking    134.0    7.0    5.0    139.0     0.9504   0.964  0.9571  
   Substance_Frequency    104.0   14.0   23.0    127.0     0.8814  0.8189   0.849  
       Eating_Disorder     53.0    2.0    0.0     53.0     0.9636     1.0  0.9815  
  Environmental_Con...     34.0    3.0    5.0     39.0     0.9189  0.8718  0.8947  
               Obesity     13.0    2.0    2.0     15.0     0.8667  0.8667  0.8667  
  Healthcare_Instit...   1350.0   23.0   43.0   1393.0     0.9832  0.9691  0.9761  
      Financial_Status     94.0   26.0   35.0    129.0     0.7833  0.7287   0.755  
                   Age    509.0   65.0   53.0    562.0     0.8868  0.9057  0.8961  
              Exercise     87.0   10.0   27.0    114.0     0.8969  0.7632  0.8246  
  Communicable_Disease     73.0    6.0    9.0     82.0     0.9241  0.8902  0.9068  
          Hypertension     56.0    1.0    5.0     61.0     0.9825   0.918  0.9492  
         Other_Disease    644.0   91.0  103.0    747.0     0.8762  0.8621  0.8691  
     Violence_Or_Abuse     86.0   35.0   40.0    126.0     0.7107  0.6825  0.6964  
     Spiritual_Beliefs     71.0   10.0    7.0     78.0     0.8765  0.9103  0.8931  
            Employment   3424.0  210.0  233.0   3657.0     0.9422  0.9363  0.9392  
      Social_Exclusion     33.0    5.0    3.0     36.0     0.8684  0.9167  0.8919  
        Access_To_Care    464.0  112.0   87.0    551.0     0.8056  0.8421  0.8234  
        Marital_Status    189.0    8.0    2.0    191.0     0.9594  0.9895  0.9742  
                Income     55.0    7.0   10.0     65.0     0.8871  0.8462  0.8661  
                  Diet     52.0   15.0   16.0     68.0     0.7761  0.7647  0.7704  
        Social_Support    866.0  161.0  115.0    981.0     0.8432  0.8828  0.8625  
      Community_Safety     39.0   12.0    5.0     44.0     0.7647  0.8864  0.8211  
            Disability     94.0    2.0    3.0     97.0     0.9792  0.9691  0.9741  
         Mental_Health    740.0  107.0  100.0    840.0     0.8737   0.881  0.8773  
               Alcohol    508.0   39.0   33.0    541.0     0.9287   0.939  0.9338  
      Insurance_Status     99.0   31.0   19.0    118.0     0.7615   0.839  0.7984  
    Substance_Quantity     84.0    9.0   22.0    106.0     0.9032  0.7925  0.8442  
        Hyperlipidemia     11.0    0.0    2.0     13.0        1.0  0.8462  0.9167  
         Family_Member   4118.0  103.0   63.0   4181.0     0.9756  0.9849  0.9802  
          Legal_Issues     58.0   15.0   17.0     75.0     0.7945  0.7733  0.7838  
        Race_Ethnicity     70.0    7.0    3.0     73.0     0.9091  0.9589  0.9333  
                Gender  10175.0  233.0  197.0  10372.0     0.9776   0.981  0.9793  
     Geographic_Entity    170.0   17.0   17.0    187.0     0.9091  0.9091  0.9091  
       Childhood_Event     19.0    0.0    5.0     24.0        1.0  0.7917  0.8837  
    Sexual_Orientation     35.0    9.0   17.0     52.0     0.7955  0.6731  0.7292  
        Transportation     72.0    7.0   14.0     86.0     0.9114  0.8372  0.8727  
    Substance_Duration     34.0   17.0   16.0     50.0     0.6667    0.68  0.6733  
       Sexual_Activity     38.0   29.0    8.0     46.0     0.5672  0.8261  0.6726  
              Language     29.0    3.0    6.0     35.0     0.9063  0.8286  0.8657  
         Substance_Use    312.0   44.0   20.0    332.0     0.8764  0.9398   0.907  
                 macro      -      -      -        -          -       -    0.8592  
                 micro      -      -      -        -          -       -    0.9396   
```
