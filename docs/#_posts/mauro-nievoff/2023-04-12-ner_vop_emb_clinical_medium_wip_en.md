---
layout: model
title: Voice of the Patients (embeddings_clinical_medium)
author: John Snow Labs
name: ner_vop_emb_clinical_medium_wip
date: 2023-04-12
tags: [licensed, clinical, en, ner, vop, patient]
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

`Allergen`, `SubstanceQuantity`, `RaceEthnicity`, `Measurements`, `InjuryOrPoisoning`, `Treatment`, `Modifier`, `TestResult`, `MedicalDevice`, `Vaccine`, `Frequency`, `HealthStatus`, `Route`, `RelationshipStatus`, `Procedure`, `Duration`, `DateTime`, `AdmissionDischarge`, `Disease`, `Test`, `Substance`, `Laterality`, `Symptom`, `ClinicalDept`, `Dosage`, `Age`, `Drug`, `VitalTest`, `PsychologicalCondition`, `Form`, `BodyPart`, `Employment`, `Gender`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/VOICE_OF_THE_PATIENTS/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/VOICE_OF_THE_PATIENTS.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_emb_clinical_medium_wip_en_4.4.0_3.0_1681315530573.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_emb_clinical_medium_wip_en_4.4.0_3.0_1681315530573.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

word_embeddings = WordEmbeddingsModel().pretrained(embeddings_clinical_medium, "en", "clinical/models")\
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")                

ner = MedicalNerModel.pretrained("ner_vop_emb_clinical_medium_wip", "en", "clinical/models") \
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
    
val word_embeddings = WordEmbeddingsModel().pretrained(embeddings_clinical_medium, "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                
    
val ner = MedicalNerModel.pretrained("ner_vop_emb_clinical_medium_wip", "en", "clinical/models")
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

val data = Seq("Hello,I"m 20 year old girl. I"m diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I"m taking weekly supplement of vitamin D and 1000 mcg b12 daily. I"m taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I"m facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you.").toDS.toDF("text")

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
| homeopathy medicine  | Treatment              |
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
|Model Name:|ner_vop_emb_clinical_medium_wip|
|Compatibility:|Healthcare NLP 4.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|3.9 MB|
|Dependencies:|embeddings_clinical_medium|

## References

In-house annotated health-related text in colloquial language.

## Sample text from the training dataset

Hello,I"m 20 year old girl. I"m diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I"m taking weekly supplement of vitamin D and 1000 mcg b12 daily. I"m taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I"m facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you.

## Benchmarking

```bash
                 label    tp   fp   fn  total  precision  recall   f1
              Allergen     0    1    8      8       0.00    0.00 0.00
     SubstanceQuantity     9   14   18     27       0.39    0.33 0.36
         RaceEthnicity     2    0    6      8       1.00    0.25 0.40
          Measurements    41   25   33     74       0.62    0.55 0.59
     InjuryOrPoisoning    66   37   51    117       0.64    0.56 0.60
             Treatment    96   39   46    142       0.71    0.68 0.69
              Modifier   642  268  271    913       0.71    0.70 0.70
            TestResult   394  185  154    548       0.68    0.72 0.70
         MedicalDevice   177   76   67    244       0.70    0.73 0.71
               Vaccine    20    4   12     32       0.83    0.63 0.71
             Frequency   456  144  187    643       0.76    0.71 0.73
          HealthStatus    60    4   38     98       0.94    0.61 0.74
                 Route    24    4   12     36       0.86    0.67 0.75
    RelationshipStatus    19    3    9     28       0.86    0.68 0.76
             Procedure   286   91   80    366       0.76    0.78 0.77
              Duration   846  227  269   1115       0.79    0.76 0.77
              DateTime  1813  455  391   2204       0.80    0.82 0.81
    AdmissionDischarge    19    1    8     27       0.95    0.70 0.81
               Disease  1247  318  256   1503       0.80    0.83 0.81
                  Test   734  150  175    909       0.83    0.81 0.82
             Substance   156   48   22    178       0.76    0.88 0.82
            Laterality   440   91   78    518       0.83    0.85 0.84
               Symptom  3069  566  630   3699       0.84    0.83 0.84
          ClinicalDept   205   35   31    236       0.85    0.87 0.86
                Dosage   273   42   49    322       0.87    0.85 0.86
                   Age   294   60   29    323       0.83    0.91 0.87
                  Drug  1035  188  100   1135       0.85    0.91 0.88
             VitalTest   144   23   13    157       0.86    0.92 0.89
PsychologicalCondition   284   32   30    314       0.90    0.90 0.90
                  Form   234   32   17    251       0.88    0.93 0.91
              BodyPart  2532  256  213   2745       0.91    0.92 0.92
            Employment   980   65   62   1042       0.94    0.94 0.94
                Gender  1174   27   20   1194       0.98    0.98 0.98
             macro_avg 17771 3511 3385  21156       0.79    0.73 0.75
             micro_avg 17771 3511 3385  21156       0.84    0.84 0.84
```
