---
layout: model
title: Voice of the Patients (embeddings_clinical_large)
author: John Snow Labs
name: ner_vop_wip_emb_clinical_large
date: 2023-05-19
tags: [licensed, clinical, en, ner, vop, patient]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.2
spark_version: 3.0
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

`Gender`, `Employment`, `BodyPart`, `Age`, `PsychologicalCondition`, `Form`, `Vaccine`, `Drug`, `Substance`, `ClinicalDept`, `Laterality`, `DateTime`, `Test`, `VitalTest`, `Disease`, `Dosage`, `Route`, `Duration`, `Procedure`, `AdmissionDischarge`, `Symptom`, `Frequency`, `RelationshipStatus`, `HealthStatus`, `Allergen`, `Modifier`, `SubstanceQuantity`, `TestResult`, `MedicalDevice`, `Treatment`, `InjuryOrPoisoning`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/VOP/){:.button.button-orange}
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_wip_emb_clinical_large_en_4.4.2_3.0_1684511324500.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_wip_emb_clinical_large_en_4.4.2_3.0_1684511324500.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_vop_wip_emb_clinical_large", "en", "clinical/models") \
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
    
val ner = MedicalNerModel.pretrained("ner_vop_wip_emb_clinical_large", "en", "clinical/models")
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
| light                | Symptom                |
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
| after 30 days        | DateTime               |
| TSH                  | Test                   |
| 0.5                  | TestResult             |
| now                  | DateTime               |
| weakness             | Symptom                |
| depression           | PsychologicalCondition |
| last week            | DateTime               |
| rapid                | TestResult             |
| heartrate            | VitalTest              |
| allopathy medicine   | Treatment              |
| homeopathy           | Treatment              |
| thyroid              | BodyPart               |
| allopathy            | Treatment              |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_wip_emb_clinical_large|
|Compatibility:|Healthcare NLP 4.4.2+|
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
                Gender  1294   25   23   1317       0.98    0.98 0.98
            Employment  1171   47   72   1243       0.96    0.94 0.95
              BodyPart  2710  199  190   2900       0.93    0.93 0.93
                   Age   539   47   43    582       0.92    0.93 0.92
PsychologicalCondition   417   45   27    444       0.90    0.94 0.92
                  Form   250   33   16    266       0.88    0.94 0.91
               Vaccine    37    2    5     42       0.95    0.88 0.91
                  Drug  1311  144  129   1440       0.90    0.91 0.91
             Substance   399   69   22    421       0.85    0.95 0.90
          ClinicalDept   288   25   38    326       0.92    0.88 0.90
            Laterality   538   47   90    628       0.92    0.86 0.89
              DateTime  3992  602  410   4402       0.87    0.91 0.89
                  Test  1064  141  144   1208       0.88    0.88 0.88
             VitalTest   154   32   18    172       0.83    0.90 0.86
               Disease  1755  316  260   2015       0.85    0.87 0.86
                Dosage   347   62   65    412       0.85    0.84 0.85
                 Route    41    7    7     48       0.85    0.85 0.85
              Duration  1845  233  465   2310       0.89    0.80 0.84
             Procedure   555   83  150    705       0.87    0.79 0.83
    AdmissionDischarge    25    1    9     34       0.96    0.74 0.83
               Symptom  3710  727  865   4575       0.84    0.81 0.82
             Frequency   851  159  228   1079       0.84    0.79 0.81
    RelationshipStatus    18    3    6     24       0.86    0.75 0.80
          HealthStatus    83   29   24    107       0.74    0.78 0.76
              Allergen    29    1   17     46       0.97    0.63 0.76
              Modifier   783  189  356   1139       0.81    0.69 0.74
     SubstanceQuantity    60   17   25     85       0.78    0.71 0.74
            TestResult   364  114  160    524       0.76    0.69 0.73
         MedicalDevice   225   56  107    332       0.80    0.68 0.73
             Treatment   142   34   86    228       0.81    0.62 0.70
     InjuryOrPoisoning   104   24   72    176       0.81    0.59 0.68
             macro_avg 25101 3513 4129  29230       0.87    0.82 0.84
             micro_avg 25101 3513 4129  29230       0.88    0.86 0.87
```
