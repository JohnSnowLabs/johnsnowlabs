---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_vop_medium)
author: John Snow Labs
name: zeroshot_ner_vop_medium
date: 2024-11-29
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

Zero-shot Named Entity Recognition (NER) enables the identification of entities in text with minimal effort. By leveraging pre-trained language models and contextual understanding, zero-shot NER extends entity recognition capabilities to new domains and languages.While the model card includes default labels as examples, it is important to highlight that users are not limited to these labels. 

**The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. For best results, it is recommended to use labels that are conceptually similar to the provided defaults.**

## Predicted Entities

`AdmissionDischarge`, `Age`, `Allergen`, `BodyPart`, `ClinicalDept`, `DateTime`, `Disease`,  
`Dosage`, `Drug`, `Duration`, `Employment`, `Form`, `Frequency`, `Gender`, `Laterality`, `MedicalDevice`,  
`Modifier`, `Procedure`, `PsychologicalCondition`, `RaceEthnicity`, `Substance`, `Symptom`, `Test`,  
`Treatment`, `Vaccine`  


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_vop_medium_en_5.5.1_3.0_1732909881083.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_vop_medium_en_5.5.1_3.0_1732909881083.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_vop_medium", "en", "clinical/models")\
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

pretrained_zero_shot_ner = medical.PretrainedZeroShotNER().pretrained("zeroshot_ner_vop_medium", "en", "clinical/models")\
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

val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_vop_medium", "en", "clinical/models")
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
|20 year old         |11   |21  |Age                   |0.90626055|
|girl                |23   |26  |Gender                |0.9872349 |
|hyperthyroid        |48   |59  |Disease               |0.5882809 |
|1 month ago         |61   |71  |DateTime              |0.89972264|
|weak                |88   |91  |Symptom               |0.94134945|
|light               |94   |98  |Symptom               |0.8042566 |
|digestion           |112  |120 |Symptom               |0.80794823|
|panic attacks       |123  |135 |PsychologicalCondition|0.6966042 |
|depression          |138  |147 |PsychologicalCondition|0.8788635 |
|left                |150  |153 |Laterality            |0.9769653 |
|chest               |155  |159 |BodyPart              |0.9179944 |
|pain                |161  |164 |Symptom               |0.9488603 |
|heart rate          |177  |186 |Test                  |0.852903  |
|weight loss         |197  |207 |Symptom               |0.8533222 |
|4 months            |216  |223 |Duration              |0.91566205|
|hospital            |259  |266 |ClinicalDept          |0.9460183 |
|discharged          |277  |286 |AdmissionDischarge    |0.9330801 |
|hospital            |293  |300 |ClinicalDept          |0.9106594 |
|blood tests         |320  |330 |Test                  |0.9211605 |
|brain               |333  |337 |BodyPart              |0.56395924|
|mri                 |339  |341 |Test                  |0.5211516 |
|ultrasound scan     |344  |358 |Test                  |0.9587256 |
|endoscopy           |361  |369 |Test                  |0.56992483|
|doctors             |392  |398 |Employment            |0.70382017|
|homeopathy doctor   |487  |503 |Employment            |0.8384213 |
|he                  |513  |514 |Gender                |0.9115307 |
|hyperthyroid        |547  |558 |Disease               |0.7546066 |
|TSH                 |567  |569 |Test                  |0.9506327 |
|T4                  |587  |588 |Test                  |0.5156918 |
|b12 deficiency      |614  |627 |Disease               |0.74625975|
|vitamin D deficiency|633  |652 |Disease               |0.6932099 |
|weekly              |668  |673 |Frequency             |0.9117316 |
|vitamin D           |689  |697 |Drug                  |0.9248756 |
|1000 mcg            |703  |710 |Dosage                |0.955836  |
|b12                 |712  |714 |Drug                  |0.74509525|
|daily               |716  |720 |Frequency             |0.87319267|
|40 days             |758  |764 |Duration              |0.90739   |
|after 30 days       |784  |796 |DateTime              |0.5512618 |
|TSH                 |802  |804 |Test                  |0.9578176 |
|now                 |813  |815 |DateTime              |0.8912383 |
|weakness            |850  |857 |Symptom               |0.9487599 |
|depression          |863  |872 |PsychologicalCondition|0.92137915|
|last week           |913  |921 |DateTime              |0.889882  |
|heartrate           |967  |975 |Test                  |0.59811634|
|thyroid             |1075 |1081|BodyPart              |0.87814385|
+--------------------+-----+----+----------------------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_vop_medium|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|711.8 MB|

## Benchmarking

```bash
                 label  precision    recall  f1-score   support
    AdmissionDischarge     0.6562    0.8400    0.7368        25
                   Age     0.9151    0.9513    0.9328       657
              Allergen     0.4500    0.8000    0.5760        45
              BodyPart     0.8746    0.9429    0.9074      2870
          ClinicalDept     0.7930    0.8831    0.8356       308
              DateTime     0.8785    0.8118    0.8438      4489
               Disease     0.7933    0.7746    0.7839      2081
                Dosage     0.5358    0.8423    0.6550       444
                  Drug     0.7968    0.8836    0.8379      1340
              Duration     0.7361    0.8400    0.7846      2225
            Employment     0.9137    0.9268    0.9202      1257
                  Form     0.6570    0.9150    0.7648       247
             Frequency     0.7031    0.8986    0.7889      1144
                Gender     0.9445    0.9670    0.9556      1303
            Laterality     0.7016    0.9009    0.7889       535
         MedicalDevice     0.6979    0.6381    0.6667       315
              Modifier     0.4495    0.8186    0.5803      1141
                     O     0.9747    0.9576    0.9661    113762
             Procedure     0.6328    0.6022    0.6171       641
PsychologicalCondition     0.8365    0.8124    0.8243       485
         RaceEthnicity     0.8182    0.9310    0.8710        29
             Substance     0.7509    0.8833    0.8117       454
               Symptom     0.8088    0.7952    0.8020      4629
                  Test     0.8572    0.7759    0.8146      1486
             Treatment     0.5600    0.5957    0.5773       188
               Vaccine     0.9000    0.5000    0.6429        36
              accuracy          -         -    0.9340    142136
             macro avg     0.7552    0.8265    0.7802    142136
          weighted avg     0.9399    0.9340    0.9359    142136
```
