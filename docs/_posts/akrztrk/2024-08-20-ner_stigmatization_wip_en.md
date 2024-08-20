---
layout: model
title: Detect Stigmatization Language
author: John Snow Labs
name: ner_stigmatization_wip
date: 2024-08-20
tags: [stigmatization, clinical, en, licensed, ner]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Named Entity Recognition (NER) model is specifically trained to extract critical information from clinical text related to stigmatization. This model aims to systematically collect and analyze data on stigmatizing language found in patients' medical records.

It includes entities based on the behavior exhibited by patients as reported in clinical texts:

`Aggressive`: Hostile, confrontational, or excessively assertive behaviors, including aggression, agitation, belligerence, and combativeness.
`Argumentative`: Challenging or difficult behaviors, including being uncooperative, argumentative, and defensive.
`Calm`: Tranquil, composed, and cooperative demeanor, including descriptions such as calm, quiet, and cooperative.
`Resistant`: Stubborn or oppositional behavior, including descriptions such as obstinate, adamant, refusing, denying, and declining.
`Credibility_Doubts`: Skepticism or doubt about the accuracy or truthfulness of information given by a patient.
`Suspected_DSB`: Suspected ulterior motives for obtaining medication, particularly controlled substances.
`Compliant`: Demonstrates adherence to prescribed medical advice, treatment plans, or medication regimens.
`Noncompliant`: Does not follow prescribed medical advice, treatment plans, or medication regimens.
`Well_Kept_Appearance`: Demonstrates good personal care, hygiene, and an orderly appearance.
`Neglected_Appearance`: Exhibits signs of inadequate personal care or hygiene.
`Paternalistic_Tone`: Conveys a sense of authority and control by the healthcare provider over the patient.
`Poor_Reasoning`: Behaviors or decisions perceived as irrational, illogical, or lacking sound judgment.
`Poor_Decision-Making`: Careless, irresponsible, or lacking proper attention and management in decision-making.
`Other_Discriminatory_Language`: Derogatory, outdated, or prejudiced terms related to physical disability, intellectual disability, and age.
`Positive_Descriptors`: Positive and complimentary terms used to describe a patient's demeanor, behavior, or appearance.
`Positive_Assessment`: Positive attributes indicating dedication, enthusiasm, or a proactive attitude toward health and treatment.
`Shared_Decision`: Patients are collaboratively involved in the decision-making process regarding their treatment or care.
`Patient_Autonomy`: Acknowledgement and respect of the patient's right to make their own decisions regarding their healthcare.

## Predicted Entities

`Aggressive`, `Argumentative`, `Calm`, `Resistant`, `Credibility_Doubts`, `Suspected_DSB`, `Compliant`, `Noncompliant`, `Well_Kept_Appearance`, `Neglected_Appearance`, `Paternalistic_Tone`, `Poor_Reasoning`, `Poor_Decision-Making`, `Other_Discriminatory_Language`, `Positive_Descriptors`, `Positive_Assessment`, `Shared_Decision`, `Patient_Autonomy`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_stigmatization_wip_en_5.4.0_3.0_1724152681455.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_stigmatization_wip_en_5.4.0_3.0_1724152681455.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained('ner_stigmatization_wip', "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(['sentence', 'token', 'ner'])\
    .setOutputCol('ner_chunk')

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
    ])

sample_texts = ["""
Despite his confrontational attitude, efforts were made to educate Mr. Brown on the importance of following his treatment plan and dietary restrictions. Multiple attempts to discuss his condition and the need for continuous care were met with defensiveness. He declined several recommendations, becoming agitated and tearful during discussions about his health.
"""]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_stigmatization_wip", "en", "clinical/models")
    .setInputCols(Array("sentence", "token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentenceDetector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
))

val sample_texts = Seq("""Despite his confrontational attitude, efforts were made to educate Mr. Brown on the importance of following his treatment plan and dietary restrictions. Multiple attempts to discuss his condition and the need for continuous care were met with defensiveness. He declined several recommendations, becoming agitated and tearful during discussions about his health.""").toDF("text")

val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_stigmatization_wip|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|5.0 MB|

## Benchmarking

```bash
                        label  precision    recall  f1-score   support
                   Aggressive       0.97      0.51      0.67        72
                Argumentative       0.93      0.96      0.95        57
                         Calm       1.00      0.93      0.96        27
                    Compliant       1.00      0.98      0.99        51
           Credibility_Doubts       0.99      0.87      0.92        77
              Kept_Appearance       1.00      1.00      1.00        20
         Poor_Decision-Making       1.00      0.76      0.86        21
         Neglected_Appearance       0.90      0.78      0.84        23
                 Noncompliant       1.00      0.91      0.96        35
Other_Discriminatory_Language       1.00      0.88      0.94        17
           Paternalistic_Tone       1.00      1.00      1.00        76
             Patient_Autonomy       1.00      0.40      0.57        10
               Poor_Reasoning       1.00      0.85      0.92        41
          Positive_Assessment       0.82      0.98      0.90        48
         Positive_Descriptors       0.86      1.00      0.92         6
                    Resistant       0.88      0.79      0.83        28
              Shared_Decision       1.00      1.00      1.00        18
                Suspected_DSB       0.80      0.67      0.73        12
                    micro-avg       0.96      0.86      0.91       639
                    macro-avg       0.95      0.85      0.89       639
                 weighted-avg       0.96      0.86      0.90       639
```