---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_oncology_medium)
author: John Snow Labs
name: zeroshot_ner_oncology_medium
date: 2024-11-27
tags: [licensed, en, ner, oncology, zeroshot, clinical]
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

Zero-shot Named Entity Recognition (NER) enables the identification of entities in text with minimal effort. By leveraging pre-trained language models and contextual understanding, zero-shot NER extends entity recognition capabilities to new domains and languages.
While the model card includes default labels as examples, it is important to highlight that users are not limited to these labels. The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. For best results, it is recommended to use labels that are conceptually similar to the provided defaults.


## Predicted Entities
`Adenopathy`, `Age`, `Biomarker`, `Biomarker_Result`, `Body_Part`, `Cancer_Dx`, `Cancer_Surgery`,  
`Cycle_Count`, `Cycle_Day`, `Date`, `Death_Entit`, `Directio`, `Dosage`, `Duration`, `Frequency`,  
`Gender`, `Grade`, `Histological_Type`, `Imaging_Test`, `Invasion`, `Metastasis`, `Oncogene`, `Pathology_Test`,  
`Race_Ethnicity`, `Radiation_Dose`, `Relative_Date`, `Response_To_Treatment`, `Route`, `Smoking_Status`,  
`Staging`, `Therapy`, `Tumor_Finding`, `Tumor_Size`  


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_oncology_medium_en_5.5.1_3.0_1732750114892.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_oncology_medium_en_5.5.1_3.0_1732750114892.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

labels = ["Adenopathy", "Age","Biomarker","Biomarker_Result","Body_Part","Cancer_Dx","Cancer_Surgery",
    "Cycle_Count","Cycle_Day","Date","Death_Entit","Directio","Dosage","Duration","Frequency",
    "Gender","Grade","Histological_Type","Imaging_Test","Invasion","Metastasis","Oncogene","Pathology_Test",
    "Race_Ethnicity","Radiation_Dose","Relative_Date","Response_To_Treatment","Route","Smoking_Status",
    "Staging","Therapy","Tumor_Finding","Tumor_Size"]

pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_oncology_medium", "en", "clinical/models")\
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

data = spark.createDataFrame([["""Two years ago, the patient presented with a tumor in her left breast and adenopathies. She was diagnosed with invasive ductal carcinoma. Last week she was also found to have a lung metastasis."""]]).toDF("text")

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

labels = ["Adenopathy", "Age","Biomarker","Biomarker_Result","Body_Part","Cancer_Dx","Cancer_Surgery",
    "Cycle_Count","Cycle_Day","Date","Death_Entit","Directio","Dosage","Duration","Frequency",
    "Gender","Grade","Histological_Type","Imaging_Test","Invasion","Metastasis","Oncogene","Pathology_Test",
    "Race_Ethnicity","Radiation_Dose","Relative_Date","Response_To_Treatment","Route","Smoking_Status",
    "Staging","Therapy","Tumor_Finding","Tumor_Size"]

val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_oncology_medium", "en", "clinical/models")
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

val data = Seq([["""Two years ago, the patient presented with a tumor in her left breast and adenopathies. She was diagnosed with invasive ductal carcinoma. Last week she was also found to have a lung metastasis."""]]).toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-------------+-----+---+-----------------+----------+
|chunk        |begin|end|ner_label        |confidence|
+-------------+-----+---+-----------------+----------+
|Two years ago|1    |13 |Relative_Date    |0.9153258 |
|tumor        |45   |49 |Tumor_Finding    |0.98980695|
|her          |54   |56 |Gender           |0.99849236|
|left         |58   |61 |Direction        |0.99010885|
|breast       |63   |68 |Body_Part        |0.97540295|
|adenopathies |74   |85 |Adenopathy       |0.83176845|
|She          |88   |90 |Gender           |0.9997961 |
|invasive     |111  |118|Invasion         |0.93775606|
|ductal       |120  |125|Histological_Type|0.90716   |
|carcinoma    |127  |135|Cancer_Dx        |0.946235  |
|Last week    |138  |146|Relative_Date    |0.8142577 |
|she          |148  |150|Gender           |0.99979   |
|lung         |177  |180|Body_Part        |0.98785883|
|metastasis   |182  |191|Metastasis       |0.99683565|
+-------------+-----+---+-----------------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_oncology_medium|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|711.2 MB|
