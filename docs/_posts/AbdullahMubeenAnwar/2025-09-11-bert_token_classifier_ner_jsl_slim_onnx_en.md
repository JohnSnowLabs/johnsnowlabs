---
layout: model
title: Detect Clinical Entities (Slim version, BertForTokenClassifier, ONNX)
author: John Snow Labs
name: bert_token_classifier_ner_jsl_slim_onnx
date: 2025-09-11
tags: [medical, clinical, ner, en, licensed, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.1.1
spark_version: 3.0
supported: true
engine: onnx
annotator: MedicalBertForTokenClassifier
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a pretrained **Named Entity Recognition (NER)** deep learning model for clinical terminology.  
It is based on the **`bert_token_classifier_ner_jsl`** model, but with more **generalized entities**.  

Predicted Entities and Definitions:

- **Death_Entity** — Mentions that indicate the death of a patient.  
- **Medical_Device** — Mentions related to medical devices and supplies.  
- **Vital_Signs_Header** — Section headers corresponding to vital signs of a patient.  
- **Allergen** — Allergen-related mentions.  
- **Drug_BrandName** — Commercial name chosen by the labeler or manufacturer for a drug containing one or more active ingredients.  
- **Clinical_Dept** — Mentions of medical and/or surgical departments.  
- **Symptom** — Mentions of symptoms, either of the patient or someone else.  
- **External_body_part_or_region** — Mentions of external body parts or organs visible to the naked eye.  
- **Admission_Discharge** — Mentions indicating patient admission and/or discharge.  
- **Age** — Mentions of age (past or present, patient or others).  
- **Birth_Entity** — Mentions of childbirth.  
- **Oncological** — Mentions of cancer, tumors, or metastasis (patient or others).  
- **Substance_Quantity** — Quantitative mentions of illicit or recreational drug use.  
- **Test_Result** — Mentions of clinical test results.  
- **Test** — Mentions of laboratory, pathology, and radiological tests.  
- **Procedure** — Mentions of invasive medical or surgical procedures/treatments.  
- **Treatment** — Mentions of therapeutic or minimally invasive treatments (excluding invasive “Procedure”).  
- **Disease_Syndrome_Disorder** — Mentions of diseases, syndromes, or disorders (excluding those with specific labels such as *Heart_Disease*).

## Predicted Entities

`B-Birth_Entity`, `I-Vital_Sign`, `I-Test_Result`, `B-Death_Entity`, `I-Header`, `B-Vital_Sign`, `B-Disease_Syndrome_Disorder`, `B-Substance_Quantity`, `I-Pregnancy_Newborn`, `I-Clinical_Dept`, `I-Body_Part`, `B-Demographics`, `I-Admission_Discharge`, `I-Oncological`, `B-Test`, `I-Death_Entity`, `I-Date_Time`, `B-Oncological`, `I-Lifestyle`, `B-Drug`, `O`, `I-Demographics`, `I-Disease_Syndrome_Disorder`, `B-Medical_Device`, `B-Symptom`, `B-Clinical_Dept`, `B-Body_Part`, `B-Header`, `I-Medical_Device`, `I-Symptom`, `B-Lifestyle`, `B-Physical_Measurement`, `B-Procedure`, `B-Treatment`, `B-Age`, `I-Drug`, `I-Substance_Quantity`, `I-Treatment`, `B-Admission_Discharge`, `I-Physical_Measurement`, `B-Alergen`, `B-Date_Time`, `B-Test_Result`, `I-Age`, `I-Test`, `I-Procedure`, `B-Pregnancy_Newborn`, `I-Alergen`, `PAD`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_jsl_slim_onnx_en_6.1.1_3.0_1757558295426.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_jsl_slim_onnx_en_6.1.1_3.0_1757558295426.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.base import DocumentAssembler
from sparknlp_jsl.annotator import SentenceDetectorDLModel, MedicalBertForTokenClassifier
from sparknlp.annotator import Tokenizer, NerConverter
from pyspark.ml import Pipeline

document_assembler = (
    DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

sentenceDetector = (
    SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(["document"])
    .setOutputCol("sentence")
)

tokenizer = (
    Tokenizer()
    .setInputCols(["sentence"])
    .setOutputCol("token")
)

token_classifier = (
    MedicalBertForTokenClassifier.pretrained(
        "bert_token_classifier_ner_jsl_slim_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "sentence"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
     NerConverterInternal()
    .setInputCols(["sentence", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = Pipeline(stages=[
    document_assembler,
    sentenceDetector,
    tokenizer,
    token_classifier,
    ner_converter
])

test_sentence = "HISTORY: 30-year-old female presents for digital bilateral mammography secondary to a soft tissue lump palpated by the patient in the upper right shoulder. The patient has a family history of breast cancer within her mother at age 58. Patient denies personal history of breast cancer."
data = spark.createDataFrame([[test_sentence]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```
{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")


sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")


tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")


token_classifier = medical.BertForTokenClassifier.pretrained(
        "bert_token_classifier_ner_jsl_slim_onnx",
        "en",
        "clinical/models"
    )\
    .setInputCols(["token", "sentence"])\
    .setOutputCol("ner")\
    .setCaseSensitive(True)


ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")


pipeline = nlp.Pipeline(stages=[
    document_assembler,
    sentenceDetector,
    tokenizer,
    token_classifier,
    ner_converter
])

test_sentence = "HISTORY: 30-year-old female presents for digital bilateral mammography secondary to a soft tissue lump palpated by the patient in the upper right shoulder. The patient has a family history of breast cancer within her mother at age 58. Patient denies personal history of breast cancer."
data = spark.createDataFrame([[test_sentence]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```

```scala
import com.johnsnowlabs.nlp.base.DocumentAssembler
import com.johnsnowlabs.nlp.annotators.Tokenizer
import com.johnsnowlabs.nlp.annotators.ner.NerConverter
import com.johnsnowlabs.nlp.annotators.classifier.dl.MedicalBertForTokenClassifier
import com.johnsnowlabs.nlp.annotators.sentence_detector_dl.SentenceDetectorDLApproach
import org.apache.spark.ml.Pipeline

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetectorDLModel()
  .pretrained("sentence_detector_dl","xx")
  .setInputCols("document")
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val tokenClassifier = MedicalBertForTokenClassifier
  .pretrained("bert_token_classifier_ner_jsl_slim_onnx", "en", "clinical/models")
  .setInputCols(Array("token", "document"))
  .setOutputCol("ner")
  .setCaseSensitive(true)

val nerConverter = new  NerConverterInternal()
  .setInputCols(Array("document", "token", "ner"))
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    tokenClassifier,
    nerConverter
  ))

val testSentence = "HISTORY: 30-year-old female presents for digital bilateral mammography secondary to a soft tissue lump palpated by the patient in the upper right shoulder. The patient has a family history of breast cancer within her mother at age 58. Patient denies personal history of breast cancer."
val data = Seq(testSentence).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+----------------+------------+
|text            |entity      |
+----------------+------------+
|HISTORY:        |Header      |
|30-year-old     |Age         |
|female          |Demographics|
|mammography     |Test        |
|soft tissue lump|Symptom     |
|shoulder        |Body_Part   |
|breast cancer   |Oncological |
|her mother      |Demographics|
|age 58          |Age         |
|breast cancer   |Oncological |
+----------------+------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_jsl_slim_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|403.8 MB|
|Case sensitive:|true|
|Max sentence length:|128|