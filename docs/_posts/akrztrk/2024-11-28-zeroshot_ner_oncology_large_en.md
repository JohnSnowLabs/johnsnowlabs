---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_oncology_large)
author: John Snow Labs
name: zeroshot_ner_oncology_large
date: 2024-11-28
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_oncology_large_en_5.5.1_3.0_1732825527391.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_oncology_large_en_5.5.1_3.0_1732825527391.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_oncology_large", "en", "clinical/models")\
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

labels = ["Adenopathy", "Age","Biomarker","Biomarker_Result","Body_Part","Cancer_Dx","Cancer_Surgery",
    "Cycle_Count","Cycle_Day","Date","Death_Entit","Directio","Dosage","Duration","Frequency",
    "Gender","Grade","Histological_Type","Imaging_Test","Invasion","Metastasis","Oncogene","Pathology_Test",
    "Race_Ethnicity","Radiation_Dose","Relative_Date","Response_To_Treatment","Route","Smoking_Status",
    "Staging","Therapy","Tumor_Finding","Tumor_Size"]

pretrained_zero_shot_ner = medical.PretrainedZeroShotNER().pretrained("zeroshot_ner_oncology_large", "en", "clinical/models")\
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

labels = Array("Adenopathy", "Age","Biomarker","Biomarker_Result","Body_Part","Cancer_Dx","Cancer_Surgery",
    "Cycle_Count","Cycle_Day","Date","Death_Entit","Directio","Dosage","Duration","Frequency",
    "Gender","Grade","Histological_Type","Imaging_Test","Invasion","Metastasis","Oncogene","Pathology_Test",
    "Race_Ethnicity","Radiation_Dose","Relative_Date","Response_To_Treatment","Route","Smoking_Status",
    "Staging","Therapy","Tumor_Finding","Tumor_Size")

val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_oncology_large", "en", "clinical/models")
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
|Two years ago|1    |13 |Relative_Date    |0.9848315 |
|tumor        |45   |49 |Tumor_Finding    |0.99484324|
|her          |54   |56 |Gender           |0.99652606|
|left         |58   |61 |Direction        |0.99791497|
|breast       |63   |68 |Body_Part        |0.9953009 |
|adenopathies |74   |85 |Adenopathy       |0.9020297 |
|She          |88   |90 |Gender           |0.99673635|
|invasive     |111  |118|Histological_Type|0.90829986|
|ductal       |120  |125|Histological_Type|0.8250756 |
|carcinoma    |127  |135|Cancer_Dx        |0.97008   |
|Last week    |138  |146|Date             |0.9312243 |
|she          |148  |150|Gender           |0.9977864 |
|lung         |177  |180|Body_Part        |0.9972607 |
|metastasis   |182  |191|Metastasis       |0.9868492 |
+-------------+-----+---+-----------------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_oncology_large|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|


```bash
                label  precision    recall  f1-score   support
           Adenopathy     0.6077    0.8587    0.7117        92
                  Age     0.9561    0.9944    0.9749      1074
            Biomarker     0.7034    0.8744    0.7796      1752
     Biomarker_Result     0.5618    0.9026    0.6925      1632
            Body_Part     0.7044    0.9203    0.7980      3540
            Cancer_Dx     0.8526    0.8125    0.8321      1360
       Cancer_Surgery     0.7790    0.7437    0.7609       749
          Cycle_Count     0.7750    0.8857    0.8267       350
            Cycle_Day     0.6928    0.8346    0.7571       254
                 Date     0.9469    0.9881    0.9671       921
         Death_Entity     0.8293    0.9444    0.8831        36
            Direction     0.7025    0.9279    0.7996       957
               Dosage     0.8776    0.8389    0.8578      1111
             Duration     0.6605    0.8855    0.7566       760
            Frequency     0.7386    0.8604    0.7948       394
               Gender     0.9802    0.9984    0.9892      1286
                Grade     0.6317    0.8178    0.7128       258
    Histological_Type     0.5459    0.7878    0.6449       476
         Imaging_Test     0.8467    0.8653    0.8559      2145
             Invasion     0.5461    0.8177    0.6549       181
           Metastasis     0.9530    0.8756    0.9127       394
                    O     0.9709    0.8980    0.9330     66650
             Oncogene     0.6892    0.6996    0.6944       466
       Pathology_Test     0.6896    0.8382    0.7567      1100
       Race_Ethnicity     0.8657    0.9831    0.9206        59
       Radiation_Dose     0.8077    0.8936    0.8485       141
        Relative_Date     0.7965    0.7710    0.7835      1284
Response_To_Treatment     0.5100    0.7988    0.6225       641
                Route     0.6359    0.8493    0.7273       146
       Smoking_Status     0.8983    0.9298    0.9138        57
              Staging     0.5738    0.7848    0.6629       223
              Therapy     0.7295    0.9021    0.8067      2012
        Tumor_Finding     0.8879    0.8474    0.8672      1252
           Tumor_Size     0.8069    0.9803    0.8852      1066
             accuracy          -         -    0.8928     94819
            macro avg     0.7575    0.8709    0.8054     94819
         weighted avg     0.9096    0.8928    0.8975     94819
```
