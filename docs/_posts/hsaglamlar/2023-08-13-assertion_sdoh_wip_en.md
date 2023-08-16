---
layout: model
title: Detect Assertion Status from Social Determinants of Health (SDOH) Entities
author: John Snow Labs
name: assertion_sdoh_wip
date: 2023-08-13
tags: [sdoh, assertion, clinical, social_determinants, en, licensed]
task: Assertion Status
language: en
edition: Healthcare NLP 5.0.0
spark_version: 3.0
supported: true
annotator: AssertionDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The Spark NLP assertion model utilizes a sophisticated neural network, powered by a Bidirectional Long Short-Term Memory (BiLSTM) framework. This model specializes in classifying assertions in text into six distinct entities: 'Absent', 'Present', 'Someone_Else', 'Past', 'Hypothetical', and 'Possible'.

Each entity represents a unique type of assertion, such as denoting absence, indicating presence, referring to someone else, discussing past events, speculating hypothetically, or suggesting potential conditions.

Trained on diverse data with annotated examples, the model has learned to accurately identify these assertion types within text. It not only categorizes but also provides confidence scores for predictions, offering insights into the certainty of each entity assignment.

`Present`: Indicates the presence of a specific condition, attribute, or factor.
`Absent`: Denotes the absence of a particular condition, attribute, or factor.
`Someone_Else`: Highlights instances where the statement pertains to someone other than the patient.
`Past`: Refers to assertions related to events or conditions that occurred in the past.
`Hypothetical`: Relates to hypothetical or speculative assertions about potential conditions or situations.
`Possible`: Signifies assertions that suggest a potential but uncertain condition.

## Predicted Entities

`Present`, `Absent`, `Someone_Else`, `Past`, `Hypothetical`, `Possible`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_sdoh_wip_en_5.0.0_3.0_1691921639033.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_sdoh_wip_en_5.0.0_3.0_1691921639033.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = WordEmbeddingsModel.pretrained('embeddings_clinical', "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_sdoh", "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(['sentence', 'token', 'ner'])\
    .setOutputCol('ner_chunk')

assertion = AssertionDLModel.pretrained("assertion_sdoh_wip", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")



pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter,
    assertion
    ])


empty_data = spark.createDataFrame([[""]]).toDF("text")
model = pipeline.fit(empty_data)

sample_texts= ["""Smith works as a cleaning assistant and does not have access to health insurance or paid sick leave. But she has generally housing problems. She lives in a apartment now.  She has long history of EtOH abuse, beginning in her teens. She is aware she needs to attend Rehab Programs. She had DUI back in April and was due to be in court this week. Her partner is an alcoholic and a drug abuser for the last 5 years. She also mentioned feeling socially isolated and lack of a strong support system. """]
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_sdoh", "en", "clinical/models") 
    .setInputCols(Array("sentence", "token", "embeddings")) 
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal() 
    .setInputCols(Array("sentence", "token", "ner")) 
    .setOutputCol("ner_chunk") 
    .setBlackList(Array("RelativeDate", "Gender"))
    
val clinical_assertion = AssertionDLModel.pretrained("assertion_sdoh_wip", "en", "clinical/models") 
    .setInputCols(Array("sentence", "ner_chunk", "embeddings")) 
    .setOutputCol("assertion")
    
val nlpPipeline = Pipeline().setStages(Array(documentAssembler, 
    sentenceDetector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    clinical_assertion))

val data= Seq("""Smith works as a cleaning assistant and does not have access to health insurance or paid sick leave. But she has generally housing problems. She lives in a apartment now.  She has long history of EtOH abuse, beginning in her teens. She is aware she needs to attend Rehab Programs. She had DUI back in April and was due to be in court this week. Her partner is an alcoholic and a drug abuser for the last 5 years. She also mentioned feeling socially isolated and lack of a strong support system. """).toDS.toDF("text")

val result = nlpPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------+-----+---+------------------+------------+--------------------+
|chunk             |begin|end|ner_label         |assertion   |assertion_confidence|
+------------------+-----+---+------------------+------------+--------------------+
|cleaning assistant|17   |34 |Employment        |Present     |0.7926              |
|health insurance  |64   |79 |Insurance_Status  |Absent      |0.5072              |
|apartment         |156  |164|Housing           |Present     |0.9956              |
|EtOH abuse        |196  |205|Alcohol           |Past        |0.6054              |
|Rehab Programs    |265  |278|Access_To_Care    |Hypothetical|0.5861              |
|DUI               |289  |291|Legal_Issues      |Past        |0.5037              |
|alcoholic         |363  |371|Alcohol           |Someone_Else|0.9868              |
|drug abuser       |379  |389|Substance_Use     |Someone_Else|0.9996              |
|last 5 years      |399  |410|Substance_Duration|Someone_Else|0.9951              |
|socially isolated |440  |456|Social_Exclusion  |Present     |0.9673              |
|strong support    |472  |485|Social_Support    |Absent      |0.9597              |
+------------------+-----+---+------------------+------------+--------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_sdoh_wip|
|Compatibility:|Healthcare NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, chunk, embeddings]|
|Output Labels:|[assertion]|
|Language:|en|
|Size:|10.8 MB|
|Dependencies:|embeddings_clinical|

## References

Internal SDOH project

## Benchmarking

```bash
       label  precision    recall  f1-score   support
      Absent       0.86      0.74      0.80       259
Hypothetical       0.74      0.57      0.65       340
        Past       0.64      0.57      0.60       258
    Possible       0.55      0.48      0.51        69
     Present       0.79      0.86      0.82      1696
Someone_Else       0.69      0.68      0.69       309
    accuracy        -         -        0.76      2931
   macro-avg       0.71      0.65      0.68      2931
weighted-avg       0.76      0.76      0.76      2931
```