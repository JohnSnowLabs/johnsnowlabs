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


Zero-shot Named Entity Recognition (NER) enables the identification of entities in text with minimal effort. By leveraging pre-trained language models and contextual understanding, zero-shot NER extends entity recognition capabilities to new domains and languages. While the model card includes default labels as examples, it is important to highlight that users are not limited to these labels. 

**The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. For best results, it is recommended to use labels that are conceptually similar to the provided defaults.**



## Predicted Entities
`Adenopathy`, `Age`, `Biomarker`, `Biomarker_Result`, `Body_Part`, `Cancer_Dx`, `Cancer_Surgery`,  
`Cycle_Count`, `Cycle_Day`, `Date`, `Death_Entit`, `Directio`, `Dosage`, `Duration`, `Frequency`,  
`Gender`, `Grade`, `Histological_Type`, `Imaging_Test`, `Invasion`, `Metastasis`, `Oncogene`, `Pathology_Test`,  
`Race_Ethnicity`, `Radiation_Dose`, `Relative_Date`, `Response_To_Treatment`, `Route`, `Smoking_Status`,  
`Staging`, `Therapy`, `Tumor_Finding`, `Tumor_Size`  


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/01.4.ZeroShot_Clinical_NER.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
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

labels = Array("Adenopathy", "Age","Biomarker","Biomarker_Result","Body_Part","Cancer_Dx","Cancer_Surgery",
    "Cycle_Count","Cycle_Day","Date","Death_Entit","Directio","Dosage","Duration","Frequency",
    "Gender","Grade","Histological_Type","Imaging_Test","Invasion","Metastasis","Oncogene","Pathology_Test",
    "Race_Ethnicity","Radiation_Dose","Relative_Date","Response_To_Treatment","Route","Smoking_Status",
    "Staging","Therapy","Tumor_Finding","Tumor_Size")

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


## Benchmarking

```bash
                label  precision    recall  f1-score   support
           Adenopathy     0.4527    0.7283    0.5583        92
                  Age     0.9583    0.9851    0.9715      1074
            Biomarker     0.6589    0.8191    0.7303      1752
     Biomarker_Result     0.4782    0.8450    0.6107      1632
            Body_Part     0.6761    0.8969    0.7710      3540
            Cancer_Dx     0.8778    0.7397    0.8029      1360
       Cancer_Surgery     0.6859    0.7143    0.6998       749
          Cycle_Count     0.8182    0.8229    0.8205       350
            Cycle_Day     0.6464    0.7126    0.6779       254
                 Date     0.9743    0.9870    0.9806       921
         Death_Entity     0.9189    0.9444    0.9315        36
            Direction     0.7552    0.8412    0.7958       957
               Dosage     0.7772    0.8164    0.7963      1111
             Duration     0.6831    0.8566    0.7601       760
            Frequency     0.7599    0.7310    0.7451       394
               Gender     0.9807    0.9876    0.9841      1286
                Grade     0.5390    0.6434    0.5866       258
    Histological_Type     0.5192    0.6239    0.5668       476
         Imaging_Test     0.8460    0.8503    0.8482      2145
             Invasion     0.4538    0.8674    0.5958       181
           Metastasis     0.9441    0.8579    0.8989       394
             Oncogene     0.6986    0.5322    0.6041       466
       Pathology_Test     0.7308    0.7082    0.7193      1100
       Race_Ethnicity     0.8889    0.9492    0.9180        59
       Radiation_Dose     0.5897    0.8156    0.6845       141
        Relative_Date     0.8698    0.6558    0.7478      1284
Response_To_Treatment     0.4634    0.6412    0.5380       641
                Route     0.5722    0.7055    0.6319       146
       Smoking_Status     0.9200    0.8070    0.8598        57
              Staging     0.5579    0.7130    0.6260       223
              Therapy     0.7379    0.8733    0.7999      2012
        Tumor_Finding     0.8662    0.8634    0.8648      1252
           Tumor_Size     0.7529    0.9859    0.8538      1066
             accuracy          -         -    0.8744     94819
            macro avg     0.7354    0.8063    0.7618     94819
         weighted avg     0.8907    0.8744    0.8792     94819
```
