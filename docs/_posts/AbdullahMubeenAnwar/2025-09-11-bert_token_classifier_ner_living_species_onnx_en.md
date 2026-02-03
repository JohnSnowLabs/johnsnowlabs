---
layout: model
title: Detect Living Species - ONNX
author: John Snow Labs
name: bert_token_classifier_ner_living_species_onnx
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

Extract living species from clinical texts which is critical to scientific disciplines like medicine, biology, ecology/biodiversity, nutrition and agriculture. This model is trained with the `BertForTokenClassification` method from the `transformers` library and imported into Spark NLP.

It is trained on the [LivingNER](https://temu.bsc.es/livingner/2022/05/03/multilingual-corpus/) corpus that is composed of clinical case reports extracted from miscellaneous medical specialties including COVID, oncology, infectious diseases, tropical medicine, urology, pediatrics, and others.

**NOTE :**
- The text files were translated from Spanish with a neural machine translation system.
- The annotations were translated with the same neural machine translation system.
- The translated annotations were transferred to the translated text files using an annotation transfer technology.

## Predicted Entities

`B-HUMAN`, `I-HUMAN`, `I-SPECIES`, `O`, `B-SPECIES`, `PAD`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_living_species_onnx_en_6.1.1_3.0_1757560365184.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_living_species_onnx_en_6.1.1_3.0_1757560365184.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
        "bert_token_classifier_ner_living_species_onnx",
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

test_sentence = "42-year-old woman with end-stage chronic kidney disease, secondary to lupus nephropathy, and on peritoneal dialysis. History of four episodes of bacterial peritonitis and change of Tenckhoff catheter six months prior to admission due to catheter dysfunction. Three peritoneal fluid samples during her hospitalisation tested positive for Fusarium spp. The patient responded favourably and continued outpatient treatment with voriconazole (4mg/kg every 12 hours orally). All three isolates were identified as species of the Fusarium solani complex. In vitro susceptibility to itraconazole, voriconazole and posaconazole, according to Clinical and Laboratory Standards Institute - CLSI (M38-A) methodology, showed a minimum inhibitory concentration (MIC) in all three isolates and for all three antifungals of >16 μg/mL."
data = spark.createDataFrame([[test_sentence]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```
{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")


sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(["document"])
    .setOutputCol("sentence")


tokenizer = nlp.Tokenizer()
    .setInputCols(["sentence"])
    .setOutputCol("token")


token_classifier = medical.BertForTokenClassifier.pretrained(
        "bert_token_classifier_ner_living_species_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "sentence"])
    .setOutputCol("ner")
    .setCaseSensitive(True)


ner_converter = medical.NerConverterInternal()
    .setInputCols(["sentence", "token", "ner"])
    .setOutputCol("ner_chunk")


pipeline = nlp.Pipeline(stages=[
    document_assembler,
    sentenceDetector,
    tokenizer,
    token_classifier,
    ner_converter
])

test_sentence = "42-year-old woman with end-stage chronic kidney disease, secondary to lupus nephropathy, and on peritoneal dialysis. History of four episodes of bacterial peritonitis and change of Tenckhoff catheter six months prior to admission due to catheter dysfunction. Three peritoneal fluid samples during her hospitalisation tested positive for Fusarium spp. The patient responded favourably and continued outpatient treatment with voriconazole (4mg/kg every 12 hours orally). All three isolates were identified as species of the Fusarium solani complex. In vitro susceptibility to itraconazole, voriconazole and posaconazole, according to Clinical and Laboratory Standards Institute - CLSI (M38-A) methodology, showed a minimum inhibitory concentration (MIC) in all three isolates and for all three antifungals of >16 μg/mL."
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
  .pretrained("bert_token_classifier_ner_living_species_onnx", "en", "clinical/models")
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

val testSentence = "42-year-old woman with end-stage chronic kidney disease, secondary to lupus nephropathy, and on peritoneal dialysis. History of four episodes of bacterial peritonitis and change of Tenckhoff catheter six months prior to admission due to catheter dysfunction. Three peritoneal fluid samples during her hospitalisation tested positive for Fusarium spp. The patient responded favourably and continued outpatient treatment with voriconazole (4mg/kg every 12 hours orally). All three isolates were identified as species of the Fusarium solani complex. In vitro susceptibility to itraconazole, voriconazole and posaconazole, according to Clinical and Laboratory Standards Institute - CLSI (M38-A) methodology, showed a minimum inhibitory concentration (MIC) in all three isolates and for all three antifungals of >16 μg/mL."
val data = Seq(testSentence).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+-----------------------+-------+
|text                   |entity |
+-----------------------+-------+
|woman                  |HUMAN  |
|bacterial              |SPECIES|
|Fusarium spp           |SPECIES|
|patient                |HUMAN  |
|species                |SPECIES|
|Fusarium solani complex|SPECIES|
|antifungals            |SPECIES|
+-----------------------+-------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_living_species_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|403.7 MB|
|Case sensitive:|true|
|Max sentence length:|128|