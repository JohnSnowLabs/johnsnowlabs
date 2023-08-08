---
layout: model
title: Extract Clinical Entities from Voice of the Patient Documents (embeddings_clinical_large)
author: John Snow Labs
name: ner_vop_emb_clinical_large
date: 2023-06-06
tags: [licensed, clinical, en, ner, vop, patient]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.3
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts healthcare-related terms from the documents transferred from the patient’s own sentences.

## Predicted Entities

`Gender`, `Employment`, `BodyPart`, `Vaccine`, `Age`, `PsychologicalCondition`, `Form`, `Substance`, `ClinicalDept`, `Drug`, `AdmissionDischarge`, `DateTime`, `Test`, `Laterality`, `Route`, `Disease`, `VitalTest`, `Dosage`, `Duration`, `Frequency`, `Allergen`, `Symptom`, `Procedure`, `RelationshipStatus`, `HealthStatus`, `Modifier`, `MedicalDevice`, `SubstanceQuantity`, `InjuryOrPoisoning`, `TestResult`, `Treatment`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/VOP/){:.button.button-orange}
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_emb_clinical_large_en_4.4.3_3.0_1686073213251.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_emb_clinical_large_en_4.4.3_3.0_1686073213251.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical_large", "en", "clinical/models")\
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")                

ner = MedicalNerModel.pretrained("ner_vop_emb_clinical_large", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")
pipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter])

data = spark.createDataFrame([["Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you."]]).toDF("text")

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
    
val word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical_large", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                
    
val ner = MedicalNerModel.pretrained("ner_vop_emb_clinical_large", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")
    
val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

        
val pipeline = new Pipeline().setStages(Array(document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter))    

val data = Seq("Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
| chunk                | ner_label              |
|:---------------------|:-----------------------|
| 20 year old          | Age                    |
| girl                 | Gender                 |
| hyperthyroid         | Disease                |
| 1 month ago          | DateTime               |
| weak                 | Symptom                |
| panic attacks        | PsychologicalCondition |
| depression           | PsychologicalCondition |
| left                 | Laterality             |
| chest                | BodyPart               |
| pain                 | Symptom                |
| increased            | TestResult             |
| heart rate           | VitalTest              |
| rapidly              | Modifier               |
| weight loss          | Symptom                |
| 4 months             | Duration               |
| hospital             | ClinicalDept           |
| discharged           | AdmissionDischarge     |
| hospital             | ClinicalDept           |
| blood tests          | Test                   |
| brain                | BodyPart               |
| mri                  | Test                   |
| ultrasound scan      | Test                   |
| endoscopy            | Procedure              |
| doctors              | Employment             |
| homeopathy doctor    | Employment             |
| he                   | Gender                 |
| hyperthyroid         | Disease                |
| TSH                  | Test                   |
| 0.15                 | TestResult             |
| T3                   | Test                   |
| T4                   | Test                   |
| normal               | TestResult             |
| b12 deficiency       | Disease                |
| vitamin D deficiency | Disease                |
| weekly               | Frequency              |
| supplement           | Drug                   |
| vitamin D            | Drug                   |
| 1000 mcg             | Dosage                 |
| b12                  | Drug                   |
| daily                | Frequency              |
| homeopathy medicine  | Drug                   |
| 40 days              | Duration               |
| 2nd test             | Test                   |
| after 30 days        | DateTime               |
| TSH                  | Test                   |
| 0.5                  | TestResult             |
| now                  | DateTime               |
| weakness             | Symptom                |
| depression           | PsychologicalCondition |
| last week            | DateTime               |
| rapid                | TestResult             |
| heartrate            | VitalTest              |
| homeopathy           | Treatment              |
| thyroid              | BodyPart               |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_emb_clinical_large|
|Compatibility:|Healthcare NLP 4.4.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|3.9 MB|
|Dependencies:|embeddings_clinical_large|

## References

In-house annotated health-related text in colloquial language.

## Sample text from the training dataset

Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you.

## Benchmarking

```bash
                 label    tp   fp   fn  total  precision  recall   f1
                Gender  1293   17   24   1317       0.99    0.98 0.98
            Employment  1184   52   59   1243       0.96    0.95 0.96
              BodyPart  2731  204  169   2900       0.93    0.94 0.94
               Vaccine    40    5    2     42       0.89    0.95 0.92
                   Age   536   42   46    582       0.93    0.92 0.92
PsychologicalCondition   411   38   33    444       0.92    0.93 0.92
                  Form   248   33   18    266       0.88    0.93 0.91
             Substance   394   60   27    421       0.87    0.94 0.90
          ClinicalDept   291   37   35    326       0.89    0.89 0.89
                  Drug  1342  230   98   1440       0.85    0.93 0.89
    AdmissionDischarge    28    1    6     34       0.97    0.82 0.89
              DateTime  3998  579  404   4402       0.87    0.91 0.89
                  Test  1043  116  165   1208       0.90    0.86 0.88
            Laterality   566  101   62    628       0.85    0.90 0.87
                 Route    41    5    7     48       0.89    0.85 0.87
               Disease  1747  269  268   2015       0.87    0.87 0.87
             VitalTest   151   25   21    172       0.86    0.88 0.87
                Dosage   342   51   70    412       0.87    0.83 0.85
              Duration  1943  302  367   2310       0.87    0.84 0.85
             Frequency   910  208  169   1079       0.81    0.84 0.83
              Allergen    33    1   13     46       0.97    0.72 0.83
               Symptom  3557  517 1018   4575       0.87    0.78 0.82
             Procedure   576  132  129    705       0.81    0.82 0.82
    RelationshipStatus    18    2    6     24       0.90    0.75 0.82
          HealthStatus    79   23   28    107       0.77    0.74 0.76
              Modifier   805  213  334   1139       0.79    0.71 0.75
         MedicalDevice   240   70   92    332       0.77    0.72 0.75
     SubstanceQuantity    57   15   28     85       0.79    0.67 0.73
     InjuryOrPoisoning   116   28   60    176       0.81    0.66 0.73
            TestResult   353   95  171    524       0.79    0.67 0.73
             Treatment   134   44   94    228       0.75    0.59 0.66
             macro_avg 25207 3515 4023  29230       0.87    0.83 0.85
             micro_avg 25207 3515 4023  29230       0.88    0.86 0.87
```