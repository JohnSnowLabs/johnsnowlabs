---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_deid_subentity_nonMedical_large)
author: John Snow Labs
name: zeroshot_ner_deid_subentity_nonMedical_large
date: 2025-12-28
tags: [licensed, en, ner, deid, zeroshot, clinical, generic, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.2.2
spark_version: 3.4
supported: true
engine: onnx
annotator: PretrainedZeroShotNER
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Zero-shot Named Entity Recognition (NER) enables the identification of entities in text with minimal effort. By leveraging pre-trained language models and contextual understanding, zero-shot NER extends entity recognition capabilities to new domains and languages. While the model card includes default labels as examples, it is important to highlight that users are not limited to these labels.

The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. For best results, it is recommended to use labels that are conceptually similar to the provided defaults.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_subentity_nonMedical_large_en_6.2.2_3.4_1766883678589.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_subentity_nonMedical_large_en_6.2.2_3.4_1766883678589.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

labels = ["ACCOUNTNUM", "AGE", "CITY", "COUNTRY", "DATE", "DEVICE", "DLN", "DOCTOR", "EMAIL", "GENDER", "HOSPITAL", "IDNUM", "IP", "LOCATION_OTHER", "MEDICALRECORD", "NAME", "ORGANIZATION", "PATIENT", "PHONE", "PLATE", "PROFESSION", "SSN", "STATE", "STREET", "TIME", "URL", "USERNAME", "VIN", "ZIP"]

pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_subentity_nonMedical_large", "en", "clinical/models")\
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

data = spark.createDataFrame([["""On February 14, 2024, patient Sarah Mitchell, a 42-year-old female (SSN: 456-78-9012, MRN: MRN-2024-78945), was admitted to St.Mary's Regional Hospital at 1500 Healthcare Boulevard, Boston, MA 02108.

Dr. Robert Chen, MD (License: DL-12345678), examined the patient in the Cardiology Department. Contact: phone +1-617-555-2468, E-mail: sarah.mitchell@techmail.com. She resides at 789 Maple Avenue, Apt 3C, Cambridge, MA 02139.

Emergency contact: James Mitchell (+1-617-555-2469). Insurance: Policy HLTH-987654321, BlueCross BlueShield. Discharged February 15, 2024. Follow-up: March 1, 2024, at 11:00 AM."""]]).toDF("text")

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

labels = ["ACCOUNTNUM", "AGE", "CITY", "COUNTRY", "DATE", "DEVICE", "DLN", "DOCTOR", "EMAIL", "GENDER", "HOSPITAL", "IDNUM", "IP", "LOCATION_OTHER", "MEDICALRECORD", "NAME", "ORGANIZATION", "PATIENT", "PHONE", "PLATE", "PROFESSION", "SSN", "STATE", "STREET", "TIME", "URL", "USERNAME", "VIN", "ZIP"]

pretrained_zero_shot_ner = medical.PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_subentity_nonMedical_large", "en", "clinical/models")\
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

data = spark.createDataFrame([["""On February 14, 2024, patient Sarah Mitchell, a 42-year-old female (SSN: 456-78-9012, MRN: MRN-2024-78945), was admitted to St.Mary's Regional Hospital at 1500 Healthcare Boulevard, Boston, MA 02108.

Dr. Robert Chen, MD (License: DL-12345678), examined the patient in the Cardiology Department. Contact: phone +1-617-555-2468, E-mail: sarah.mitchell@techmail.com. She resides at 789 Maple Avenue, Apt 3C, Cambridge, MA 02139.

Emergency contact: James Mitchell (+1-617-555-2469). Insurance: Policy HLTH-987654321, BlueCross BlueShield. Discharged February 15, 2024. Follow-up: March 1, 2024, at 11:00 AM."""]]).toDF("text")

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

val labels = Array("ACCOUNTNUM", "AGE", "CITY", "COUNTRY", "DATE", "DEVICE", "DLN", "DOCTOR", "EMAIL", "GENDER", "HOSPITAL", "IDNUM", "IP", "LOCATION_OTHER", "MEDICALRECORD", "NAME", "ORGANIZATION", "PATIENT", "PHONE", "PLATE", "PROFESSION", "SSN", "STATE", "STREET", "TIME", "URL", "USERNAME", "VIN", "ZIP")

val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_subentity_nonMedical_large", "en", "clinical/models")
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

val data = Seq("""On February 14, 2024, patient Sarah Mitchell, a 42-year-old female (SSN: 456-78-9012, MRN: MRN-2024-78945), was admitted to St.Mary's Regional Hospital at 1500 Healthcare Boulevard, Boston, MA 02108.

Dr. Robert Chen, MD (License: DL-12345678), examined the patient in the Cardiology Department. Contact: phone +1-617-555-2468, E-mail: sarah.mitchell@techmail.com. She resides at 789 Maple Avenue, Apt 3C, Cambridge, MA 02139.

Emergency contact: James Mitchell (+1-617-555-2469). Insurance: Policy HLTH-987654321, BlueCross BlueShield. Discharged February 15, 2024. Follow-up: March 1, 2024, at 11:00 AM.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+---------------------------+-----+---+--------------+----------+
|chunk                      |begin|end|ner_label     |confidence|
+---------------------------+-----+---+--------------+----------+
|February 14, 2024          |3    |19 |DATE          |0.9978829 |
|Sarah Mitchell             |30   |43 |PATIENT       |0.9996172 |
|42-year-old                |48   |58 |AGE           |0.9977164 |
|female                     |60   |65 |GENDER        |0.94535685|
|456-78-9012                |73   |83 |SSN           |0.9957628 |
|MRN-2024-78945             |91   |104|MEDICALRECORD |0.9977089 |
|1500 Healthcare Boulevard  |155  |179|STREET        |0.99362284|
|Boston                     |182  |187|CITY          |0.9986701 |
|MA                         |190  |191|STATE         |0.999084  |
|02108                      |193  |197|ZIP           |0.9933094 |
|Robert Chen                |205  |215|DOCTOR        |0.9995503 |
|DL-12345678                |231  |241|DLN           |0.9995552 |
|Cardiology                 |273  |282|HOSPITAL      |0.7655589 |
|+1-617-555-2468            |311  |325|PHONE         |0.99838436|
|sarah.mitchell@techmail.com|336  |362|EMAIL         |0.5817256 |
|She                        |365  |367|NAME          |0.706219  |
|789 Maple Avenue           |380  |395|STREET        |0.99547416|
|Apt 3C                     |398  |403|LOCATION_OTHER|0.9998995 |
|Cambridge                  |406  |414|CITY          |0.9983443 |
|MA                         |417  |418|STATE         |0.999726  |
|02139                      |420  |424|ZIP           |0.9982576 |
|James Mitchell             |447  |460|NAME          |0.89618254|
|+1-617-555-2469            |463  |477|PHONE         |0.9961054 |
|HLTH-987654321             |499  |512|IDNUM         |0.9831487 |
|BlueCross BlueShield       |515  |534|ORGANIZATION  |0.9567745 |
|February 15, 2024          |548  |564|DATE          |0.992326  |
|March 1, 2024              |578  |590|DATE          |0.94422466|
|11:00 AM                   |596  |603|TIME          |0.9995034 |
+---------------------------+-----+---+--------------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_deid_subentity_nonMedical_large|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|