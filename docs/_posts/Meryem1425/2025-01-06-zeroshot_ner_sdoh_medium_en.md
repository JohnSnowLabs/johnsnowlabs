---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_sdoh_medium)
author: John Snow Labs
name: zeroshot_ner_sdoh_medium
date: 2025-01-06
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_sdoh_medium_en_5.5.1_3.0_1736197155160.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_sdoh_medium_en_5.5.1_3.0_1736197155160.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_sdoh_medium", "en", "clinical/models")\
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

data = spark.createDataFrame([["""Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. She has a son, a student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reports having her catholic faith as a means of support as well.  She has a long history of etoh abuse, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day. She had DUI in April and was due to court this week."""]]).toDF("text")

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
pretrained_zero_shot_ner = medical.PretrainedZeroShotNER().pretrained("zeroshot_ner_sdoh_medium", "en", "clinical/models")\
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

data = spark.createDataFrame([["""Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. She has a son, a student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reports having her catholic faith as a means of support as well.  She has a long history of etoh abuse, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day. She had DUI in April and was due to court this week."""]]).toDF("text")

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

val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_sdoh_medium", "en", "clinical/models")
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

val data = Seq([["""Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. She has a son, a student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reports having her catholic faith as a means of support as well.  She has a long history of etoh abuse, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day. She had DUI in April and was due to court this week."""]]).toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+------------------+-----+---+-----------------+----------+
|chunk             |begin|end|ner_label        |confidence|
+------------------+-----+---+-----------------+----------+
|55 years old      |9    |20 |Age              |0.98757917|
|New York          |33   |40 |Geographic_Entity|0.96678746|
|divorced          |45   |52 |Marital_Status   |0.9670806 |
|Mexcian American  |54   |69 |Race_Ethnicity   |0.6176904 |
|woman             |71   |75 |Gender           |0.9907975 |
|financial problems|82   |99 |Financial_Status |0.81308645|
|She               |102  |104|Gender           |0.9993352 |
|apartment         |118  |126|Housing          |0.615918  |
|She               |129  |131|Gender           |0.9991904 |
|diabetes          |158  |165|Other_Disease    |0.8660285 |
|cleaning assistant|307  |324|Employment       |0.5079581 |
|She               |381  |383|Gender           |0.99975115|
|son               |391  |393|Family_Member    |0.99613535|
|student           |398  |404|Education        |0.8893471 |
|college           |409  |415|Education        |0.95348775|
|depression        |447  |456|Mental_Health    |0.9034998 |
|She               |459  |461|Gender           |0.99977094|
|she               |472  |474|Gender           |0.9998542 |
|rehab             |482  |486|Access_To_Care   |0.7825011 |
|her               |507  |509|Gender           |0.99785334|
|catholic faith    |511  |524|Spiritual_Beliefs|0.95611227|
|support           |540  |546|Social_Support   |0.9163973 |
|She               |558  |560|Gender           |0.9997602 |
|her               |609  |611|Gender           |0.9995541 |
|teens             |613  |617|Age              |0.94968903|
|She               |620  |622|Gender           |0.99972373|
|she               |632  |634|Gender           |0.99988306|
|drinker           |653  |659|Alcohol          |0.9500115 |
|beer              |698  |701|Alcohol          |0.7686361 |
|She               |710  |712|Gender           |0.9997906 |
|smokes            |714  |719|Smoking          |0.92108554|
|cigarettes        |731  |740|Smoking          |0.93036956|
|She               |749  |751|Gender           |0.9998215 |
|DUI               |757  |759|Legal_Issues     |0.754453  |
+------------------+-----+---+-----------------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_sdoh_medium|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|711.2 MB|

## Benchmarking

```bash

                  label  precision    recall  f1-score   support
         Access_To_Care     0.6721    0.8094    0.7344      1018
                    Age     0.8487    0.8243    0.8363       905
                Alcohol     0.8774    0.9513    0.9128       677
  Childhood_Development     0.5789    0.8462    0.6875        26
                   Diet     0.4451    0.8021    0.5725        96
             Disability     0.8681    0.9294    0.8977        85
        Eating_Disorder     0.6190    0.7800    0.6903        50
              Education     0.6690    0.7951    0.7266       122
             Employment     0.8914    0.9264    0.9086      4269
Environmental_Condition     0.3739    0.5244    0.5365        82
               Exercise     0.4790    0.7619    0.5882       105
          Family_Member     0.9598    0.9755    0.9676      4042
       Financial_Status     0.4944    0.8224    0.6175       214
                 Gender     0.9920    0.9792    0.9856     10248
      Geographic_Entity     0.6810    0.6930    0.6870       228
 Healthcare_Institution     0.8948    0.3609    0.5143      1391
                Housing     0.7553    0.8753    0.8109       850
           Hypertension     0.5513    0.7049    0.6187        61
                 Income     0.6744    0.6744    0.6744        86
       Insurance_Status     0.6951    0.7170    0.7059       159
               Language     0.4923    0.8421    0.6214        38
           Legal_Issues     0.2261    0.5246    0.5160       122
         Marital_Status     0.9632    0.9458    0.9544       166
          Mental_Health     0.6846    0.8265    0.7489      1003
                      O     0.9840    0.9782    0.9811    169565
                Obesity     0.4667    0.7500    0.5753        28
          Other_Disease     0.7056    0.9214    0.7992      1285
    Other_SDoH_Keywords     0.7738    0.7156    0.7436       545
        Quality_Of_Life     0.4959    0.5021    0.4990       241
         Race_Ethnicity     0.8214    0.8214    0.8214        56
        Sexual_Activity     0.6329    0.9434    0.7576        53
     Sexual_Orientation     0.7778    0.8974    0.8333        39
                Smoking     0.8683    0.9797    0.9206       148
       Social_Exclusion     0.7455    0.8367    0.7885        49
         Social_Support     0.8910    0.8610    0.8757      1367
      Spiritual_Beliefs     0.6149    0.8349    0.7082       109
         Transportation     0.3725    0.8120    0.5108       117
      Violence_Or_Abuse     0.6623    0.6667    0.6645       153
               accuracy        -         -      0.9651    199798
              macro-avg     0.6895    0.8003    0.7288    199798
           weighted-avg     0.9684    0.9651    0.9655    199798


```
