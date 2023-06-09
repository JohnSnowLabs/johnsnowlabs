---
layout: model
title: Voice of the Patients (embeddings_clinical_large)
author: John Snow Labs
name: ner_vop_emb_clinical_large_wip
date: 2023-04-12
tags: [licensed, clinical, en, ner, vop, patient]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.0
spark_version: [3.2, 3.0]
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

`Allergen`, `SubstanceQuantity`, `RaceEthnicity`, `Measurements`, `InjuryOrPoisoning`, `Treatment`, `TestResult`, `Modifier`, `Route`, `MedicalDevice`, `Vaccine`, `RelationshipStatus`, `Frequency`, `HealthStatus`, `Procedure`, `Duration`, `DateTime`, `Disease`, `Test`, `Substance`, `Symptom`, `Laterality`, `Dosage`, `ClinicalDept`, `PsychologicalCondition`, `VitalTest`, `Age`, `Drug`, `BodyPart`, `AdmissionDischarge`, `Form`, `Employment`, `Gender`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/VOICE_OF_THE_PATIENTS/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/VOICE_OF_THE_PATIENTS.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_emb_clinical_large_wip_en_4.4.0_3.0_1681315187438.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_emb_clinical_large_wip_en_4.4.0_3.0_1681315187438.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

word_embeddings = WordEmbeddingsModel().pretrained(embeddings_clinical_large, "en", "clinical/models")\
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")                

ner = MedicalNerModel.pretrained("ner_vop_emb_clinical_large_wip", "en", "clinical/models") \
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
    
val word_embeddings = WordEmbeddingsModel().pretrained(embeddings_clinical_large, "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                
    
val ner = MedicalNerModel.pretrained("ner_vop_emb_clinical_large_wip", "en", "clinical/models")
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
| heartrate            | VitalTest              |
| homeopathy           | Treatment              |
| thyroid              | BodyPart               |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_emb_clinical_large_wip|
|Compatibility:|Healthcare NLP 4.4.0+|
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

Hello,I"m 20 year old girl. I"m diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I"m taking weekly supplement of vitamin D and 1000 mcg b12 daily. I"m taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I"m facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you.

## Benchmarking

```bash
                 label    tp   fp   fn  total  precision  recall   f1
              Allergen     0    0    8      8       0.00    0.00 0.00
     SubstanceQuantity     7   10   20     27       0.41    0.26 0.32
         RaceEthnicity     2    0    6      8       1.00    0.25 0.40
          Measurements    36   20   38     74       0.64    0.49 0.55
     InjuryOrPoisoning    65   28   52    117       0.70    0.56 0.62
             Treatment    86   27   56    142       0.76    0.61 0.67
            TestResult   379  150  169    548       0.72    0.69 0.70
              Modifier   644  229  269    913       0.74    0.71 0.72
                 Route    23    5   13     36       0.82    0.64 0.72
         MedicalDevice   171   54   73    244       0.76    0.70 0.73
               Vaccine    21    4   11     32       0.84    0.66 0.74
    RelationshipStatus    18    2   10     28       0.90    0.64 0.75
             Frequency   478  161  165    643       0.75    0.74 0.75
          HealthStatus    75   19   23     98       0.80    0.77 0.78
             Procedure   275   68   91    366       0.80    0.75 0.78
              Duration   884  275  231   1115       0.76    0.79 0.78
              DateTime  1796  397  408   2204       0.82    0.81 0.82
               Disease  1258  323  245   1503       0.80    0.84 0.82
                  Test   752  155  157    909       0.83    0.83 0.83
             Substance   152   37   26    178       0.80    0.85 0.83
               Symptom  3078  547  621   3699       0.85    0.83 0.84
            Laterality   425   62   93    518       0.87    0.82 0.85
                Dosage   266   37   56    322       0.88    0.83 0.85
          ClinicalDept   201   28   35    236       0.88    0.85 0.86
PsychologicalCondition   282   41   32    314       0.87    0.90 0.89
             VitalTest   146   25   11    157       0.85    0.93 0.89
                   Age   295   38   28    323       0.89    0.91 0.90
                  Drug  1040  136   95   1135       0.88    0.92 0.90
              BodyPart  2528  245  217   2745       0.91    0.92 0.92
    AdmissionDischarge    24    1    3     27       0.96    0.89 0.92
                  Form   233   24   18    251       0.91    0.93 0.92
            Employment   988   51   54   1042       0.95    0.95 0.95
                Gender  1173   26   21   1194       0.98    0.98 0.98
             macro_avg 17801 3225 3355  21156       0.80    0.73 0.76
             micro_avg 17801 3225 3355  21156       0.85    0.84 0.84
```
