---
layout: model
title: Detect Stigmatization Language
author: John Snow Labs
name: ner_stigmatization_wip
date: 2024-08-27
tags: [clinical, en, licensed, ner, stigmatization]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.4.1
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

- `Aggressive`: Hostile, confrontational, or excessively assertive behaviors, including aggression, agitation, belligerence, and combativeness.
- `Argumentative`: Challenging or difficult behaviors, including being uncooperative, argumentative, and defensive.
- `Calm`: Tranquil, composed, and cooperative demeanor, including descriptions such as calm, quiet, and cooperative.
- `Resistant`: Stubborn or oppositional behavior, including descriptions such as obstinate, adamant, refusing, denying, and declining.
- `Credibility_Doubts`: Skepticism or doubt about the accuracy or truthfulness of information given by a patient.
- `Suspected_DSB`: Suspected ulterior motives for obtaining medication, particularly controlled substances.
- `Compliant`: Demonstrates adherence to prescribed medical advice, treatment plans, or medication regimens.
- `Noncompliant`: Does not follow prescribed medical advice, treatment plans, or medication regimens.
- `Collaborative_Decision_Making`: Joint participation of patient and provider in treatment decisions.
- `Neglected_Appearance`: Exhibits signs of inadequate personal care or hygiene.
- `Paternalistic_Tone`: Conveys a sense of authority and control by the healthcare provider over the patient.
- `Poor_Reasoning`: Behaviors or decisions perceived as irrational, illogical, or lacking sound judgment.
- `Poor_Decision_Making`: Careless, irresponsible, or lacking proper attention and management in decision-making.
- `Other_Discriminatory_Language`: Derogatory, outdated, or prejudiced terms related to physical disability, intellectual disability, and age.
- `Positive_Descriptors`: Positive and complimentary terms used to describe a patient's demeanor, behavior, or appearance.
- `Positive_Assessment`: Positive attributes indicating dedication, enthusiasm, or a proactive attitude toward health and treatment.
- `Disoriented`: Confused about time, place, or personal identity.
- `Test`: Mentions of laboratory, pathology, and radiological tests. 
- `Treatment`: Includes therapeutic and minimally invasive treatment and procedures (invasive treatments or procedures are extracted as "Procedure"). 
- `Problem`: Mentions of a medical condition, diagnosis, or symptom impacting the patient.

## Predicted Entities

`Aggressive`, `Argumentative`, `Calm`, `Resistant`, `Credibility_Doubts`, `Suspected_DSB`, `Compliant`, `Noncompliant`, `Collaborative_Decision_Making`, `Neglected_Appearance`, `Paternalistic_Tone`, `Poor_Reasoning`, `Poor_Decision_Making`, `Other_Discriminatory_Language`, `Positive_Descriptors`, `Positive_Assessment`, `Disoriented`, `Test`, `Treatment`, `Problem`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/01.0.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_stigmatization_wip_en_5.4.1_3.0_1724748546038.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_stigmatization_wip_en_5.4.1_3.0_1724748546038.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_stigmatization_wip", "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
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

sample_texts = [
"""The healthcare team observed that Mr. Smith exhibited somewhat aggressive behavior and was highly irritable, especially when discussing his treatment plan. He showed a full range of emotions and fixated on certain incorrect beliefs about his health. Concerns about his poor insight and judgment were frequently discussed in multidisciplinary team meetings. For example, he often insisted that his symptoms were purely due to stress.""",
"""Once stabilized, Mr. Smith was discharged with a comprehensive care plan emphasizing the importance of medication adherence and regular follow-up appointments. Despite extensive counseling on the risks associated with non-compliance, concerns about his judgment persisted. He expressed skepticism about the need for certain medications, particularly those for managing his diabetes and COPD.""",
"""David Brown's hospital stay underscored the significant impact of poor reasoning and judgment on his health outcomes. His initial reluctance to seek care and resistance to necessary treatments highlighted the crucial need for patient education and compliance. Moving forward, strict adherence to his treatment plan and regular follow-up are vital to preventing further complications and ensuring his ongoing well-being.""",
"""Despite his confrontational attitude, efforts were made to educate Mr. Brown on the importance of following his treatment plan and dietary restrictions. Multiple attempts to discuss his condition and the need for continuous care were met with defensiveness. He declined several recommendations, becoming agitated and tearful during discussions about his health.""",
"""Efforts to educate Ms. Martin on the importance of adhering to her asthma management plan were met with resistance. She frequently questioned the necessity of her medications and expressed dissatisfaction with her care. Despite these challenges, the team remained dedicated to providing thorough care, working to address her concerns and educate her on the importance of following her treatment regimen. Ms. Martin became particularly agitated when discussing her anxiety and the impact of her asthma on her quality of life. "No one understands how hard this is for me," she argued during a consultation with the psychiatrist. Despite her defensive attitude, the team continued to offer support and reassurance, acknowledging the complexity of her psychosocial barriers to care.""",
"""History of Present Illness: Ms. ___ is a very pleasant ___ female who underwent a left partial mastectomy and left axillary sentinel node biopsy on ___ for left invasive ductal carcinoma. Her surgical pathology report indicated that all six margins were either involved with or close to atypical or carcinoma cells. We decided to go with a global re-excision lumpectomy, which was then performed on ___."""
]

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

val sample_texts = Seq(
"""The healthcare team observed that Mr. Smith exhibited somewhat aggressive behavior and was highly irritable, especially when discussing his treatment plan. He showed a full range of emotions and fixated on certain incorrect beliefs about his health. Concerns about his poor insight and judgment were frequently discussed in multidisciplinary team meetings. For example, he often insisted that his symptoms were purely due to stress.""",
"""Once stabilized, Mr. Smith was discharged with a comprehensive care plan emphasizing the importance of medication adherence and regular follow-up appointments. Despite extensive counseling on the risks associated with non-compliance, concerns about his judgment persisted. He expressed skepticism about the need for certain medications, particularly those for managing his diabetes and COPD.""",
"""David Brown's hospital stay underscored the significant impact of poor reasoning and judgment on his health outcomes. His initial reluctance to seek care and resistance to necessary treatments highlighted the crucial need for patient education and compliance. Moving forward, strict adherence to his treatment plan and regular follow-up are vital to preventing further complications and ensuring his ongoing well-being.""",
"""Despite his confrontational attitude, efforts were made to educate Mr. Brown on the importance of following his treatment plan and dietary restrictions. Multiple attempts to discuss his condition and the need for continuous care were met with defensiveness. He declined several recommendations, becoming agitated and tearful during discussions about his health.""",
"""Efforts to educate Ms. Martin on the importance of adhering to her asthma management plan were met with resistance. She frequently questioned the necessity of her medications and expressed dissatisfaction with her care. Despite these challenges, the team remained dedicated to providing thorough care, working to address her concerns and educate her on the importance of following her treatment regimen. Ms. Martin became particularly agitated when discussing her anxiety and the impact of her asthma on her quality of life. "No one understands how hard this is for me," she argued during a consultation with the psychiatrist. Despite her defensive attitude, the team continued to offer support and reassurance, acknowledging the complexity of her psychosocial barriers to care.""",
"""History of Present Illness: Ms. ___ is a very pleasant ___ female who underwent a left partial mastectomy and left axillary sentinel node biopsy on ___ for left invasive ductal carcinoma. Her surgical pathology report indicated that all six margins were either involved with or close to atypical or carcinoma cells. We decided to go with a global re-excision lumpectomy, which was then performed on ___."""
).toDF("text")

val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

## Results

```bash
+----------------------------------+-----+---+-----------------------------+
|chunk                             |begin|end|ner_label                    |
+----------------------------------+-----+---+-----------------------------+
|aggressive                        |63   |72 |Aggressive                   |
|irritable                         |98   |106|Aggressive                   |
|poor insight and judgment         |269  |293|Poor_Reasoning               |
|discussed                         |311  |319|Collaborative_Decision_Making|
|insisted                          |379  |386|Credibility_Doubts           |
|his symptoms                      |393  |404|PROBLEM                      |
|stress                            |425  |430|PROBLEM                      |
|adherence                         |114  |122|Compliant                    |
|non-compliance                    |218  |231|Noncompliant                 |
|judgment                          |253  |260|Poor_Reasoning               |
|certain medications               |316  |334|TREATMENT                    |
|his diabetes                      |369  |380|PROBLEM                      |
|COPD                              |386  |389|PROBLEM                      |
|poor reasoning and judgment       |66   |92 |Poor_Reasoning               |
|reluctance                        |130  |139|Resistant                    |
|resistance                        |158  |167|Resistant                    |
|treatments                        |182  |191|TREATMENT                    |
|compliance                        |248  |257|Compliant                    |
|adherence                         |283  |291|Compliant                    |
|further complications             |361  |381|PROBLEM                      |
|confrontational                   |12   |26 |Argumentative                |
|his treatment plan                |108  |125|TREATMENT                    |
|dietary restrictions              |131  |150|TREATMENT                    |
|defensiveness                     |243  |255|Argumentative                |
|declined                          |261  |268|Resistant                    |
|agitated                          |304  |311|Aggressive                   |
|tearful                           |317  |323|PROBLEM                      |
|adhering                          |51   |58 |Compliant                    |
|her asthma management plan        |63   |88 |TREATMENT                    |
|resistance                        |104  |113|Resistant                    |
|questioned                        |131  |140|Resistant                    |
|her medications                   |159  |173|TREATMENT                    |
|her care                          |210  |217|TREATMENT                    |
|thorough care                     |287  |299|TREATMENT                    |
|her treatment regimen             |381  |401|TREATMENT                    |
|agitated                          |435  |442|Aggressive                   |
|her anxiety                       |460  |470|PROBLEM                      |
|her asthma                        |490  |499|PROBLEM                      |
|argued                            |575  |580|Argumentative                |
|defensive                         |639  |647|Argumentative                |
|support                           |687  |693|TREATMENT                    |
|her psychosocial barriers         |744  |768|PROBLEM                      |
|pleasant                          |46   |53 |Positive_Descriptors         |
|a left partial mastectomy         |80   |104|TREATMENT                    |
|left axillary sentinel node biopsy|110  |143|TEST                         |
|left invasive ductal carcinoma    |156  |185|PROBLEM                      |
|atypical or carcinoma cells       |287  |313|PROBLEM                      |
|decided                           |319  |325|Collaborative_Decision_Making|
|a global re-excision lumpectomy   |338  |368|TREATMENT                    |
+----------------------------------+-----+---+-----------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_stigmatization_wip|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|4.9 MB|

## Benchmarking

```bash
                        label  precision    recall  f1-score   support
                   Aggressive       0.98      0.75      0.85        57
                Argumentative       0.94      0.98      0.96        46
                         Calm       0.86      1.00      0.92        24
Collaborative_Decision_Making       0.96      0.95      0.95        55
                    Compliant       0.98      1.00      0.99        59
           Credibility_Doubts       0.98      0.98      0.98        55
                  Disoriented       1.00      0.73      0.84        11
         Neglected_Appearance       0.75      1.00      0.86         6
                 Noncompliant       1.00      0.92      0.96        38
Other_Discriminatory_Language       1.00      1.00      1.00         2
                      PROBLEM       0.91      0.90      0.91       580
           Paternalistic_Tone       0.84      0.97      0.90        32
         Poor_Decision_Making       0.81      0.85      0.83        34
               Poor_Reasoning       0.89      0.99      0.94        74
          Positive_Assessment       1.00      0.86      0.92        35
         Positive_Descriptors       1.00      1.00      1.00         4
                    Resistant       1.00      1.00      1.00        40
                Suspected_DSB       1.00      1.00      1.00         6
                         TEST       0.96      0.85      0.90        87
                    TREATMENT       0.92      0.91      0.92       480
                    micro-avg       0.93      0.91      0.92      1725
                    macro-avg       0.94      0.93      0.93      1725
                 weighted-avg       0.93      0.91      0.92      1725
```
