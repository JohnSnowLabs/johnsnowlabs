---
layout: model
title: Detect Opioid Specific Entities
author: John Snow Labs
name: ner_opioid_small_wip
date: 2024-01-11
tags: [licensed, en, ner, clinical, opioid]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.2.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is designed to detect and label opioid related entities within text data. Opioids are a class of drugs that include the illegal drug heroin, synthetic opioids such as fentanyl, and pain relievers available legally by prescription. The model has been trained using advanced deep learning techniques on a diverse range of text sources and can accurately recognize and classify a wide range of opioid-related entities.
The model’s accuracy and precision have been carefully validated against expert-labeled data to ensure reliable and consistent results. 

Here are the labels of the OPIOID model with their descriptions:

- `communicable_disease`: Communicable disease is a disease that people spread to one another through contact with contaminated surfaces, bodily fluids, blood products, insect bites, or through the air.
- `general_symptoms`: Include all the symptoms,vital findings and signs mentioned in the document, of the patient or someone else.
- `substance_use_disorder` : Mentions of substance use that include unspecific illicit drug abuse.
- `drug_duration`: The duration for which the drug was taken or prescribed.
- `psychiatric_issue`: Psychiatric disorders may also be referred to as mental health conditions is a behavioral or mental pattern that causes significant distress or impairment of personal functioning. A mental disorder is also characterized by a clinically significant disturbance in an individual's cognition, emotional regulation, or behavior. It is usually associated with distress or impairment in important areas of functioning.
- `drug_strength`: The potency of one unit of drug (or a combination of drugs, generally speaking); the measurement units available are described by FDA.
- `drug_quantity`: The quantity associated with drug dosage.
- `other_drug`: Any generic or trade name of the drugs in the text other than the opioids. 
- `drug_form`: The dosage forms available are described by FDA.
- `drug_frequency`: The frequency at which the drug doses are given or being used.
- `opioid_drug`: Any drug mentioned in the text that belongs to the opioid family either legally by prescription as pain relievers like fentanyl, oxycodone, hydrocodone, codeine, morphine, Oxymorphone, Hydromorphone, Methadone, Tramadol, Buprenorphine or illegal street drug like “heroin”.
- `drug_route`: The administration routes available are described by FDA.

## Predicted Entities

`communicable_disease`, `general_symptoms`, `substance_use_disorder`, `drug_duration`, `psychiatric_issue`, `drug_strength`, `drug_quantity`, `other_drug`, `drug_form`, `drug_frequency`, `opioid_drug`, `drug_route`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_opioid_small_wip_en_5.2.0_3.0_1705003638665.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_opioid_small_wip_en_5.2.0_3.0_1705003638665.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_opioid_small_wip", "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    document_assembler, 
    sentenceDetector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
    ])

sample_texts = ["""20 year old male transferred from [**Hospital1 112**] for liver transplant
evaluation after percocet overdose. On Sunday [**3-27**] had a
stressful day and pt took approximately 20 percocet (5/325)
throughout the day after a series of family arguments. Denies
trying to hurt himself. Parents confirm to suicidal attempts in
the past. Pt felt that he had a hangover on Monday secondary to
"percocet withdrawal" and took an additional 5 percocet.  Pt was
admitted to the SICU and followed by Liver, Transplant,
Toxicology, and [**Month/Year (2) **].  He was started on NAC q4hr with gradual
decline in LFT's and INR.  His recovery was c/b hypertension,
for which he was started on clonidine.  Pt was transferred to
the floor on [**4-1**].
 
Past Medical History:
Bipolar D/o (s/p suicide attempts in the past)
ADHD
S/p head injury [**2160**]: s/p MVA with large L3 transverse process
fx, small right frontal epidural hemorrhage-- with
post-traumatic seizures (was previously on dilantin, now dc'd)
 
Social History:
Father is HCP, student in [**Name (NI) 108**], Biology major, parents and
brother live in [**Name (NI) 86**], single without children, lived in a
group home for 3 years as a teenager, drinks alcohol 1 night a
week, denies illict drug use, pt in [**Location (un) 86**] for neuro eval
"""]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_opioid_small_wip", "en", "clinical/models")
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

val sample_texts = Seq("""20 year old male transferred from [**Hospital1 112**] for liver transplant
evaluation after percocet overdose. On Sunday [**3-27**] had a
stressful day and pt took approximately 20 percocet (5/325)
throughout the day after a series of family arguments. Denies
trying to hurt himself. Parents confirm to suicidal attempts in
the past. Pt felt that he had a hangover on Monday secondary to
"percocet withdrawal" and took an additional 5 percocet.  Pt was
admitted to the SICU and followed by Liver, Transplant,
Toxicology, and [**Month/Year (2) **].  He was started on NAC q4hr with gradual
decline in LFT's and INR.  His recovery was c/b hypertension,
for which he was started on clonidine.  Pt was transferred to
the floor on [**4-1**].
 
Past Medical History:
Bipolar D/o (s/p suicide attempts in the past)
ADHD
S/p head injury [**2160**]: s/p MVA with large L3 transverse process
fx, small right frontal epidural hemorrhage-- with
post-traumatic seizures (was previously on dilantin, now dc'd)
 
Social History:
Father is HCP, student in [**Name (NI) 108**], Biology major, parents and
brother live in [**Name (NI) 86**], single without children, lived in a
group home for 3 years as a teenager, drinks alcohol 1 night a
week, denies illict drug use, pt in [**Location (un) 86**] for neuro eval
""").toDF("text")

val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

## Results

```bash
+-----------------+-----+----+----------------------+
|chunk            |begin|end |ner_label             |
+-----------------+-----+----+----------------------+
|percocet         |92   |99  |opioid_drug           |
|20               |178  |179 |drug_quantity         |
|percocet         |181  |188 |opioid_drug           |
|5/325            |191  |195 |drug_strength         |
|suicidal attempts|303  |319 |psychiatric_issue     |
|hangover         |356  |363 |general_symptoms      |
|percocet         |389  |396 |opioid_drug           |
|withdrawal       |398  |407 |general_symptoms      |
|5                |433  |433 |drug_quantity         |
|percocet         |435  |442 |opioid_drug           |
|NAC              |567  |569 |other_drug            |
|q4hr             |571  |574 |drug_frequency        |
|decline in LFT's |589  |604 |general_symptoms      |
|clonidine        |679  |687 |other_drug            |
|Bipolar          |761  |767 |psychiatric_issue     |
|suicide attempts |778  |793 |psychiatric_issue     |
|ADHD             |808  |811 |psychiatric_issue     |
|dilantin         |976  |983 |other_drug            |
|illict drug use  |1236 |1250|substance_use_disorder|
+-----------------+-----+----+----------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_opioid_small_wip|
|Compatibility:|Healthcare NLP 5.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|4.9 MB|

## Benchmarking

```bash
                 label  precision    recall  f1-score   support
  communicable_disease       0.97      0.70      0.81        47
         drug_duration       0.96      0.90      0.93        84
             drug_form       0.96      0.96      0.96       461
        drug_frequency       0.98      0.98      0.98      1171
         drug_quantity       0.96      0.97      0.97      1058
            drug_route       0.99      0.97      0.98       499
         drug_strength       0.97      0.93      0.95       414
      general_symptoms       0.89      0.78      0.83       425
           opioid_drug       0.99      0.97      0.98       229
            other_drug       0.99      0.94      0.96       804
     psychiatric_issue       0.97      0.94      0.96        34
substance_use_disorder       0.96      0.86      0.91        29
             micro-avg       0.97      0.94      0.96      5255
             macro-avg       0.97      0.91      0.93      5255
          weighted-avg       0.97      0.94      0.95      5255
```