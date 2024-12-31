---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_clinical_large)
author: John Snow Labs
name: zeroshot_ner_clinical_large
date: 2024-11-27
tags: [licensed, en, ner, zeroshot, clinical]
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

`PROBLEM`, `TREATMENT`, `TEST`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_clinical_large_en_5.5.1_3.0_1732713397823.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_clinical_large_en_5.5.1_3.0_1732713397823.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

labels = ['PROBLEM', 'TREATMENT','TEST'] # You can change the entities
pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_clinical_large", "en", "clinical/models")\
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

data = spark.createDataFrame([["""Mr. ABC is a 60-year-old gentleman who had stress test earlier today in my office with severe chest pain after 5 minutes of exercise on the standard Bruce with horizontal ST depressions and moderate apical ischemia on stress imaging only. He required 3 sublingual nitroglycerin in total. The patient underwent cardiac catheterization with myself today which showed mild-to-moderate left main distal disease of 30%, a severe mid-LAD lesion of 99%, and a mid-left circumflex lesion of 80% with normal LV function and some mild luminal irregularities in the right coronary artery with some moderate stenosis seen in the mid to distal right PDA."""]]).toDF("text")

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

labels = Array("PROBLEM", "TREATMENT","TEST") # You can change the entities
val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_clinical_large", "en", "clinical/models")
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

val data = Seq([["""Mr. ABC is a 60-year-old gentleman who had stress test earlier today in my office with severe chest pain after 5 minutes of exercise on the standard Bruce with horizontal ST depressions and moderate apical ischemia on stress imaging only. He required 3 sublingual nitroglycerin in total. The patient underwent cardiac catheterization with myself today which showed mild-to-moderate left main distal disease of 30%, a severe mid-LAD lesion of 99%, and a mid-left circumflex lesion of 80% with normal LV function and some mild luminal irregularities in the right coronary artery with some moderate stenosis seen in the mid to distal right PDA."""]]).toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-------------------------------------------------------------+-----+---+---------+----------+
|chunk                                                        |begin|end|ner_label|confidence|
+-------------------------------------------------------------+-----+---+---------+----------+
|stress test                                                  |44   |54 |TEST     |0.98778325|
|severe chest pain                                            |88   |104|PROBLEM  |0.99439317|
|the standard Bruce                                           |137  |154|TREATMENT|0.8145296 |
|horizontal ST depressions                                    |161  |185|PROBLEM  |0.9864226 |
|moderate apical ischemia                                     |191  |214|PROBLEM  |0.9951188 |
|stress imaging                                               |219  |232|TEST     |0.7248742 |
|3 sublingual nitroglycerin                                   |252  |277|TREATMENT|0.7286957 |
|cardiac catheterization                                      |311  |333|TEST     |0.98853767|
|mild-to-moderate left main distal disease                    |366  |406|PROBLEM  |0.995087  |
|a severe mid-LAD lesion                                      |416  |438|PROBLEM  |0.991574  |
|a mid-left circumflex lesion                                 |452  |479|PROBLEM  |0.99646026|
|some mild luminal irregularities in the right coronary artery|516  |576|PROBLEM  |0.96139634|
|some moderate stenosis                                       |583  |604|PROBLEM  |0.86587936|
+-------------------------------------------------------------+-----+---+---------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_clinical_large|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|


## Benchmarking

```bash
       label  precision    recall  f1-score   support
   B-PROBLEM      0.870     0.916     0.892      4460
      B-TEST      0.851     0.920     0.884      2946
 B-TREATMENT      0.886     0.905     0.895      3447
   I-PROBLEM      0.873     0.899     0.886      6312
      I-TEST      0.855     0.877     0.866      2610
 I-TREATMENT      0.905     0.847     0.875      2941
    accuracy           -        -     0.947     86628
   macro-avg      0.888     0.904     0.895     86628
weighted-avg      0.948     0.947     0.947     86628
```
