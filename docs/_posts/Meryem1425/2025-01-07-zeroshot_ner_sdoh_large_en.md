---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_sdoh_large)
author: John Snow Labs
name: zeroshot_ner_sdoh_large
date: 2025-01-07
tags: [licensed, en, ner, sdoh, zeroshot, clinical]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.5.1
spark_version: 3.0
supported: true
annotator: PretrainedZeroShotNER
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Zero-shot Named Entity Recognition (NER) enables the identification of entities in text with minimal effort. By leveraging pre-trained language models and contextual understanding, zero-shot NER extends entity recognition capabilities to new domains and languages. While the model card includes default labels as examples, it is important to highlight that users are not limited to these labels.

**The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. For best results, it is recommended to use labels that are conceptually similar to the provided defaults.**

## Predicted Entities

`Access_To_Care`, `Age`, `Alcohol`, `Childhood_Development`, `Diet`, `Disability`, `Eating_Disorder`, `Education`, `Employment`, `Environmental_Condition`, `Exercise`, `Family_Member`, `Financial_Status`, `Gender`, `Geographic_Entity`, `Healthcare_Institution`, `Housing`, `Hypertension`, `Income`, `Insurance_Status`, `Language`, `Legal_Issues`, `Marital_Status`, `Mental_Health`, `Obesity`, `Other_Disease`, `Other_SDoH_Keywords`, `Quality_Of_Life`, `Race_Ethnicity`, `Sexual_Activity`, `Sexual_Orientation`, `Smoking`, `Social_Exclusion`, `Social_Support`, `Spiritual_Beliefs`, `Transportation`, `Violence_Or_Abuse`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_sdoh_large_en_5.5.1_3.0_1736274628326.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_sdoh_large_en_5.5.1_3.0_1736274628326.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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


labels = [
'Access_To_Care', 'Age', 'Alcohol', 'Childhood_Development', 'Diet', 'Disability',
'Eating_Disorder', 'Education', 'Employment', 'Environmental_Condition', 'Exercise',
'Family_Member', 'Financial_Status', 'Gender', 'Geographic_Entity', 'Healthcare_Institution',
'Housing', 'Hypertension', 'Income', 'Insurance_Status', 'Language', 'Legal_Issues',
'Marital_Status', 'Mental_Health', 'Obesity', 'Other_Disease', 'Other_SDoH_Keywords',
'Quality_Of_Life', 'Race_Ethnicity', 'Sexual_Activity', 'Sexual_Orientation', 'Smoking',
'Social_Exclusion', 'Social_Support', 'Spiritual_Beliefs', 'Transportation', 'Violence_Or_Abuse'
]
pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_sdoh_large", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("ner")\
    .setPredictionThreshold(0.5)\
    .setLabels(labels)

ner_converter = NerConverterInternal()\
    .setInputCols("sentence", "token", "ner")\
    .setOutputCol("ner_chunk")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
])

data = spark.createDataFrame([["""Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She speaks Spanish and Portuguese. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. She has a son, a student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reports having her catholic faith as a means of support as well.  She has a long history of alcohol, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day."""]]).toDF("text")

result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")


labels = [
'Access_To_Care', 'Age', 'Alcohol', 'Childhood_Development', 'Diet', 'Disability',
'Eating_Disorder', 'Education', 'Employment', 'Environmental_Condition', 'Exercise',
'Family_Member', 'Financial_Status', 'Gender', 'Geographic_Entity', 'Healthcare_Institution',
'Housing', 'Hypertension', 'Income', 'Insurance_Status', 'Language', 'Legal_Issues',
'Marital_Status', 'Mental_Health', 'Obesity', 'Other_Disease', 'Other_SDoH_Keywords',
'Quality_Of_Life', 'Race_Ethnicity', 'Sexual_Activity', 'Sexual_Orientation', 'Smoking',
'Social_Exclusion', 'Social_Support', 'Spiritual_Beliefs', 'Transportation', 'Violence_Or_Abuse'
]
pretrained_zero_shot_ner = medical.PretrainedZeroShotNER().pretrained("zeroshot_ner_sdoh_large", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("ner")\
    .setPredictionThreshold(0.5)\
    .setLabels(labels)

ner_converter = medical.NerConverterInternal()\
    .setInputCols("sentence", "token", "ner")\
    .setOutputCol("ner_chunk")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
])

data = spark.createDataFrame([["""Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She speaks Spanish and Portuguese. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. She has a son, a student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reports having her catholic faith as a means of support as well.  She has a long history of alcohol, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day."""]]).toDF("text")

result = pipeline.fit(data).transform(data)

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

labels = Array("Access_To_Care", "Age", "Alcohol", "Childhood_Development", "Diet", "Disability",
"Eating_Disorder", "Education", "Employment", "Environmental_Condition", "Exercise",
"Family_Member", "Financial_Status", "Gender", "Geographic_Entity", "Healthcare_Institution",
"Housing", "Hypertension", "Income", "Insurance_Status", "Language", "Legal_Issues",
"Marital_Status", "Mental_Health", "Obesity", "Other_Disease", "Other_SDoH_Keywords",
"Quality_Of_Life", "Race_Ethnicity", "Sexual_Activity", "Sexual_Orientation", "Smoking",
"Social_Exclusion", "Social_Support", "Spiritual_Beliefs", "Transportation", "Violence_Or_Abuse")

val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_sdoh_large", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("ner")
    .setPredictionThreshold(0.5)
    .setLabels(labels)

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")


val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
))

val data = Seq([["""Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She speaks Spanish and Portuguese. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. She has a son, a student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reports having her catholic faith as a means of support as well.  She has a long history of alcohol, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day."""]]).toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+------------------+-----+---+-------------------+----------+
|chunk             |begin|end|ner_label          |confidence|
+------------------+-----+---+-------------------+----------+
|55 years old      |9    |20 |Age                |0.985943  |
|New York          |33   |40 |Geographic_Entity  |0.93693453|
|divorced          |45   |52 |Marital_Status     |0.9977914 |
|Mexcian American  |54   |69 |Race_Ethnicity     |0.7580686 |
|woman             |71   |75 |Gender             |0.99670666|
|financial problems|82   |99 |Financial_Status   |0.98300755|
|She               |102  |104|Gender             |0.99510634|
|Spanish           |113  |119|Language           |0.98981714|
|Portuguese        |125  |134|Language           |0.9745797 |
|She               |137  |139|Gender             |0.99644274|
|apartment         |153  |161|Housing            |0.97819704|
|She               |164  |166|Gender             |0.997265  |
|diabetes          |193  |200|Other_Disease      |0.95706624|
|hospitalizations  |268  |283|Other_SDoH_Keywords|0.69986516|
|cleaning assistant|342  |359|Employment         |0.84834933|
|health insurance  |379  |394|Insurance_Status   |0.8337548 |
|She               |416  |418|Gender             |0.99722373|
|son               |426  |428|Family_Member      |0.99653184|
|student           |433  |439|Education          |0.53395987|
|college           |444  |450|Education          |0.6121527 |
|depression        |482  |491|Mental_Health      |0.9893406 |
|She               |494  |496|Gender             |0.99657154|
|she               |507  |509|Gender             |0.99869967|
|rehab             |517  |521|Access_To_Care     |0.9899094 |
|her               |542  |544|Gender             |0.9876253 |
|support           |575  |581|Social_Support     |0.97643244|
|She               |593  |595|Gender             |0.99524057|
|alcohol           |619  |625|Alcohol            |0.96861035|
|her               |641  |643|Gender             |0.9950836 |
|teens             |645  |649|Age                |0.92979825|
|She               |652  |654|Gender             |0.98894835|
|she               |664  |666|Gender             |0.9956169 |
|drinker           |685  |691|Alcohol            |0.8265905 |
|drinking          |721  |728|Alcohol            |0.7135196 |
|She               |742  |744|Gender             |0.99702305|
|smokes            |746  |751|Smoking            |0.7797317 |
|cigarettes        |763  |772|Smoking            |0.7294187 |
+------------------+-----+---+-------------------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_sdoh_large|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|

## Benchmarking

```bash

                  label  precision    recall  f1-score   support
         Access_To_Care     0.6424    0.8929    0.7472      1018
                    Age     0.8843    0.9547    0.9182       905
                Alcohol     0.9254    0.9527    0.9389       677
  Childhood_Development     0.4808    0.9615    0.6410        26
                   Diet     0.3397    0.7396    0.5656        96
             Disability     0.8081    0.9412    0.8696        85
        Eating_Disorder     0.8571    0.9600    0.9057        50
              Education     0.6981    0.9098    0.7900       122
             Employment     0.8755    0.9489    0.9107      4269
Environmental_Condition     0.3977    0.8293    0.5375        82
               Exercise     0.5568    0.9810    0.7103       105
          Family_Member     0.9758    0.9785    0.9771      4042
       Financial_Status     0.5668    0.8131    0.6679       214
                 Gender     0.9931    0.9802    0.9866     10248
      Geographic_Entity     0.7679    0.7544    0.7611       228
 Healthcare_Institution     0.9062    0.3753    0.5308      1391
                Housing     0.7224    0.8847    0.7953       850
           Hypertension     0.4919    1.0000    0.6595        61
                 Income     0.6574    0.8256    0.7320        86
       Insurance_Status     0.7326    0.7925    0.7613       159
               Language     0.5286    0.9737    0.6852        38
           Legal_Issues     0.3495    0.8279    0.4915       122
         Marital_Status     0.9022    1.0000    0.9486       166
          Mental_Health     0.6068    0.8893    0.7214      1003
                      O     0.9884    0.9739    0.9811    169565
                Obesity     0.5641    0.7857    0.6567        28
          Other_Disease     0.7644    0.9214    0.8356      1285
    Other_SDoH_Keywords     0.6272    0.8550    0.7236       545
        Quality_Of_Life     0.3376    0.5519    0.5189       241
         Race_Ethnicity     0.6235    0.9464    0.7518        56
        Sexual_Activity     0.5506    0.9245    0.6901        53
     Sexual_Orientation     0.8636    0.9744    0.9157        39
                Smoking     0.9295    0.9797    0.9539       148
       Social_Exclusion     0.3409    0.9184    0.4972        49
         Social_Support     0.8700    0.8961    0.8829      1367
      Spiritual_Beliefs     0.6850    0.7982    0.7373       109
         Transportation     0.4195    0.8462    0.5609       117
      Violence_Or_Abuse     0.3631    0.7974    0.4990       153
               accuracy       -         -       0.9653    199798
              macro-avg     0.6735    0.8773    0.7436    199798
           weighted-avg     0.9715    0.9653    0.9668    199798


```
