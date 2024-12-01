---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_vop_large)
author: John Snow Labs
name: zeroshot_ner_vop_large
date: 2024-11-30
tags: [licensed, en, ner, vop, zeroshot, clinical]
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

`AdmissionDischarge`, `Age`, `Allergen`, `BodyPart`, `ClinicalDept`, `DateTime`, `Disease`,  
`Dosage`, `Drug`, `Duration`, `Employment`, `Form`, `Frequency`, `Gender`, `Laterality`, `MedicalDevice`,  
`Modifier`, `Procedure`, `PsychologicalCondition`, `RaceEthnicity`, `Substance`, `Symptom`, `Test`,  
`Treatment`, `Vaccine`  

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_vop_large_en_5.5.1_3.0_1732980381062.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_vop_large_en_5.5.1_3.0_1732980381062.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

labels = [
    'AdmissionDischarge', 'Age', 'Allergen','BodyPart','ClinicalDept','DateTime','Disease',
    'Dosage','Drug','Duration','Employment','Form','Frequency','Gender','Laterality','MedicalDevice',
    'Modifier','Procedure','PsychologicalCondition','RaceEthnicity','Substance','Symptom','Test',
    'Treatment','Vaccine']

pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_vop_large", "en", "clinical/models")\
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

data = spark.createDataFrame([["""Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you."""]]).toDF("text")

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

labels = [
    'AdmissionDischarge', 'Age', 'Allergen','BodyPart','ClinicalDept','DateTime','Disease',
    'Dosage','Drug','Duration','Employment','Form','Frequency','Gender','Laterality','MedicalDevice',
    'Modifier','Procedure','PsychologicalCondition','RaceEthnicity','Substance','Symptom','Test',
    'Treatment','Vaccine']

pretrained_zero_shot_ner = medical.PretrainedZeroShotNER().pretrained("zeroshot_ner_vop_large", "en", "clinical/models")\
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

data = spark.createDataFrame([["""Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you."""]]).toDF("text")

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

labels = Array(
    "AdmissionDischarge", "Age", "Allergen", "BodyPart", "ClinicalDept", "DateTime", "Disease",
    "Dosage", "Drug", "Duration", "Employment", "Form", "Frequency", "Gender", "Laterality", "MedicalDevice",
    "Modifier", "Procedure", "PsychologicalCondition", "RaceEthnicity", "Substance", "Symptom", "Test",
    "Treatment", "Vaccine")

val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_vop_large", "en", "clinical/models")
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

val data = Seq([["""Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you."""]]).toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+--------------------+-----+----+----------------------+----------+
|chunk               |begin|end |ner_label             |confidence|
+--------------------+-----+----+----------------------+----------+
|20 year old         |11   |21  |Age                   |0.99549705|
|girl                |23   |26  |Gender                |0.99473166|
|hyperthyroid        |48   |59  |Disease               |0.72869056|
|1 month ago         |61   |71  |DateTime              |0.93013126|
|weak                |88   |91  |Symptom               |0.98246646|
|light               |94   |98  |Symptom               |0.914502  |
|digestion           |112  |120 |Symptom               |0.7636672 |
|panic attacks       |123  |135 |PsychologicalCondition|0.7021233 |
|depression          |138  |147 |PsychologicalCondition|0.88090825|
|left                |150  |153 |Laterality            |0.9534648 |
|chest               |155  |159 |BodyPart              |0.90008795|
|pain                |161  |164 |Symptom               |0.96790904|
|heart rate          |177  |186 |Test                  |0.86297375|
|weight loss         |197  |207 |Symptom               |0.96102   |
|4 months            |216  |223 |Duration              |0.9639058 |
|hospital            |259  |266 |ClinicalDept          |0.93731934|
|discharged          |277  |286 |AdmissionDischarge    |0.9054539 |
|hospital            |293  |300 |ClinicalDept          |0.93180996|
|blood tests         |320  |330 |Test                  |0.94237006|
|brain               |333  |337 |BodyPart              |0.7430142 |
|mri                 |339  |341 |Test                  |0.93738127|
|ultrasound scan     |344  |358 |Test                  |0.94679016|
|endoscopy           |361  |369 |Test                  |0.5370005 |
|doctors             |392  |398 |Employment            |0.7688288 |
|homeopathy doctor   |487  |503 |Employment            |0.93872774|
|he                  |513  |514 |Gender                |0.974668  |
|hyperthyroid        |547  |558 |Disease               |0.71458954|
|TSH                 |567  |569 |Test                  |0.9895893 |
|T3                  |580  |581 |Test                  |0.9048731 |
|T4                  |587  |588 |Test                  |0.9588674 |
|b12 deficiency      |614  |627 |Disease               |0.55843806|
|vitamin D deficiency|633  |652 |Disease               |0.5240673 |
|weekly              |668  |673 |Frequency             |0.66599834|
|supplement          |675  |684 |Drug                  |0.5972447 |
|vitamin D           |689  |697 |Drug                  |0.86098486|
|1000 mcg            |703  |710 |Dosage                |0.9711681 |
|b12                 |712  |714 |Drug                  |0.83438593|
|daily               |716  |720 |Frequency             |0.93205667|
|homeopathy medicine |734  |752 |Drug                  |0.5354072 |
|40 days             |758  |764 |Duration              |0.9758632 |
|after 30 days       |784  |796 |DateTime              |0.8755744 |
|TSH                 |802  |804 |Test                  |0.98604935|
|now                 |813  |815 |DateTime              |0.8677737 |
|weakness            |850  |857 |Symptom               |0.9838275 |
|depression          |863  |872 |PsychologicalCondition|0.89689744|
|last week           |913  |921 |DateTime              |0.8067833 |
|thyroid             |1075 |1081|BodyPart              |0.8369291 |
+--------------------+-----+----+----------------------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_vop_large|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|

## Benchmarking

```bash
                 label  precision    recall  f1-score   support
    AdmissionDischarge     0.4507    0.9697    0.6154        33
                   Age     0.8991    0.9635    0.9302       657
              Allergen     0.3717    0.9130    0.5283        46
              BodyPart     0.8916    0.9583    0.9238      2953
          ClinicalDept     0.7534    0.9424    0.8373       295
              DateTime     0.8348    0.8969    0.8648      4395
               Disease     0.8917    0.7993    0.8430      2277
                Dosage     0.6617    0.8898    0.7590       499
                  Drug     0.8271    0.9246    0.8732      1340
              Duration     0.7676    0.8581    0.8103      2255
            Employment     0.9338    0.9522    0.9429      1214
                  Form     0.6627    0.9621    0.7848       290
             Frequency     0.6645    0.9149    0.7698      1093
                Gender     0.9564    0.9675    0.9619      1293
            Laterality     0.6961    0.9548    0.8052       619
         MedicalDevice     0.5978    0.6781    0.6354       320
              Modifier     0.3887    0.9112    0.5449      1092
                     O     0.9849    0.9468    0.9655    114576
             Procedure     0.6593    0.7295    0.6926       573
PsychologicalCondition     0.8029    0.9236    0.8590       419
         RaceEthnicity     0.8810    1.0000    0.9367        37
             Substance     0.8292    0.9618    0.8906       419
               Symptom     0.7636    0.8518    0.8053      4501
                  Test     0.8112    0.8481    0.8292      1560
             Treatment     0.3214    0.6562    0.5315       192
               Vaccine     0.9444    0.7391    0.8293        46
              accuracy          -         -    0.9352    142994
             macro avg     0.7403    0.8890    0.7950    142994
          weighted avg     0.9471    0.9352    0.9393    142994
```
