---
layout: model
title: Voice of the Patients
author: John Snow Labs
name: ner_vop_wip
date: 2023-03-30
tags: [en, licensed]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.0
spark_version: [3.0, 3.2]
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts healthcare-related terms from the documents transferred from the patient’s own sentences.

Note: ‘wip’ suffix indicates that the model development is work-in-progress and will be finalised and the model performance will improved in the upcoming releases.

## Predicted Entities

`SubstanceQuantity`, `Measurements`, `Treatment`, `Modifier`, `RaceEthnicity`, `Allergen`, `TestResult`, `InjuryOrPoisoning`, `Frequency`, `MedicalDevice`, `Procedure`, `Duration`, `DateTime`, `HealthStatus`, `Route`, `Vaccine`, `Disease`, `Symptom`, `RelationshipStatus`, `Dosage`, `Substance`, `VitalTest`, `AdmissionDischarge`, `Test`, `Laterality`, `ClinicalDept`, `PsychologicalCondition`, `Age`, `BodyPart`, `Drug`, `Employment`, `Form`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_wip_en_4.4.0_3.2_1680207981665.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_wip_en_4.4.0_3.2_1680207981665.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")                

ner = MedicalNerModel.pretrained("ner_vop_wip", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")
pipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter])

data = spark.createDataFrame([["Hello,I"m 20 year old girl. I"m diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I"m taking weekly supplement of vitamin D and 1000 mcg b12 daily. I"m taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I"m facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you."]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
    
val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")
    
val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")
    
val word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                
    
val ner = MedicalNerModel.pretrained("ner_vop_wip", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")
    
val ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

        
val pipeline = new Pipeline().setStages(Array(document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter))    

val data = Seq("Hello,I"m 20 year old girl. I"m diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I"m taking weekly supplement of vitamin D and 1000 mcg b12 daily. I"m taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I"m facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| chunk                       | ner_label              |
|:----------------------------|:-----------------------|
| 20 year old                 | Age                    |
| girl                        | Gender                 |
| hyperthyroid                | Disease                |
| 1 month ago                 | DateTime               |
| weak                        | Symptom                |
| light headed,poor digestion | Symptom                |
| panic attacks               | PsychologicalCondition |
| depression                  | PsychologicalCondition |
| left                        | Laterality             |
| chest                       | BodyPart               |
| pain                        | Symptom                |
| increased                   | TestResult             |
| heart rate                  | VitalTest              |
| rapidly                     | Modifier               |
| weight loss                 | Symptom                |
| 4 months                    | Duration               |
| hospital                    | ClinicalDept           |
| discharged                  | AdmissionDischarge     |
| hospital                    | ClinicalDept           |
| blood tests                 | Test                   |
| brain                       | BodyPart               |
| mri                         | Test                   |
| ultrasound scan             | Test                   |
| endoscopy                   | Procedure              |
| doctors                     | Employment             |
| homeopathy doctor           | Employment             |
| he                          | Gender                 |
| hyperthyroid                | Disease                |
| TSH                         | Test                   |
| 0.15                        | TestResult             |
| T3                          | Test                   |
| T4                          | Test                   |
| normal                      | TestResult             |
| b12 deficiency              | Disease                |
| vitamin D deficiency        | Disease                |
| weekly                      | Frequency              |
| supplement                  | Drug                   |
| vitamin D                   | Drug                   |
| 1000 mcg                    | Dosage                 |
| b12                         | Drug                   |
| daily                       | Frequency              |
| homeopathy medicine         | Drug                   |
| 40 days                     | Duration               |
| 2nd test                    | Test                   |
| after 30 days               | DateTime               |
| TSH                         | Test                   |
| 0.5                         | TestResult             |
| now                         | DateTime               |
| weakness                    | Symptom                |
| depression                  | PsychologicalCondition |
| last week                   | DateTime               |
| rapid                       | TestResult             |
| heartrate                   | VitalTest              |
| allopathy medicine          | Treatment              |
| homeopathy                  | Treatment              |
| thyroid                     | BodyPart               |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_wip|
|Compatibility:|Healthcare NLP 4.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|3.9 MB|
|Dependencies:|embeddings_clinical|

## References

In-house annotated health-related text in colloquial language.

## Benchmarking

```bash
                 label    tp   fp   fn  total  precision  recall   f1
     SubstanceQuantity     9    6    8     17       0.60    0.53 0.56
          Measurements    30   15   31     61       0.67    0.49 0.57
             Treatment    67   32   26     93       0.68    0.72 0.70
              Modifier   638  253  184    822       0.72    0.78 0.74
         RaceEthnicity     5    0    3      8       1.00    0.63 0.77
              Allergen     7    0    4     11       1.00    0.64 0.78
            TestResult   371  110   95    466       0.77    0.80 0.78
     InjuryOrPoisoning   113   27   30    143       0.81    0.79 0.80
             Frequency   424   81  112    536       0.84    0.79 0.81
         MedicalDevice   186   42   39    225       0.82    0.83 0.82
             Procedure   288   67   63    351       0.81    0.82 0.82
              Duration   786  165  181    967       0.83    0.81 0.82
              DateTime  1738  409  288   2026       0.81    0.86 0.83
          HealthStatus    76   24    5     81       0.76    0.94 0.84
                 Route    38    2   13     51       0.95    0.75 0.84
               Vaccine    22    3    5     27       0.88    0.81 0.85
               Disease  1168  228  149   1317       0.84    0.89 0.86
               Symptom  2877  646  318   3195       0.82    0.90 0.86
    RelationshipStatus    18    0    5     23       1.00    0.78 0.88
                Dosage   268   36   39    307       0.88    0.87 0.88
             Substance   167   28   19    186       0.86    0.90 0.88
             VitalTest   122   13   16    138       0.90    0.88 0.89
    AdmissionDischarge    25    2    4     29       0.93    0.86 0.89
                  Test   699   84   93    792       0.89    0.88 0.89
            Laterality   456   41   59    515       0.92    0.89 0.90
          ClinicalDept   169   14   24    193       0.92    0.88 0.90
PsychologicalCondition   264   30   14    278       0.90    0.95 0.92
                   Age   250   24   17    267       0.91    0.94 0.92
              BodyPart  2344  189  135   2479       0.93    0.95 0.94
                  Drug   962   53   46   1008       0.95    0.95 0.95
            Employment   863   50   47    910       0.95    0.95 0.95
                  Form   201   15    7    208       0.93    0.97 0.95
                Gender  1196   28   12   1208       0.98    0.99 0.98
             macro_avg 16847 2717 2091  18938       0.86    0.83 0.84
             micro_avg 16847 2717 2091  18938       0.86    0.89 0.88
```