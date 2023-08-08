---
layout: model
title: Voice of the Patients
author: John Snow Labs
name: ner_vop_wip
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

`TestResult`, `SubstanceQuantity`, `InjuryOrPoisoning`, `Treatment`, `Modifier`, `HealthStatus`, `MedicalDevice`, `Procedure`, `Symptom`, `Frequency`, `RelationshipStatus`, `Duration`, `Allergen`, `VitalTest`, `Disease`, `Dosage`, `AdmissionDischarge`, `Test`, `Laterality`, `Route`, `DateTime`, `Drug`, `ClinicalDept`, `Vaccine`, `Form`, `Substance`, `PsychologicalCondition`, `Age`, `BodyPart`, `Employment`, `Gender`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/VOP/){:.button.button-orange}
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_wip_en_4.4.2_3.0_1684508941946.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_wip_en_4.4.2_3.0_1684508941946.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    
val word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                
    
val ner = MedicalNerModel.pretrained("ner_vop_wip", "en", "clinical/models")
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
| rapid heartrate      | Symptom                |
| allopathy medicine   | Drug                   |
| homeopathy           | Treatment              |
| thyroid              | BodyPart               |
| allopathy            | Treatment              |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_wip|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|3.9 MB|
|Dependencies:|embeddings_clinical|

## References

In-house annotated health-related text in colloquial language.

## Sample text from the training dataset

"Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you."

## Benchmarking

```bash
                 label    tp   fp   fn  total  precision  recall   f1
            TestResult   353   98  171    524       0.78    0.67 0.72
     SubstanceQuantity    60   20   25     85       0.75    0.71 0.73
     InjuryOrPoisoning   122   37   54    176       0.77    0.69 0.73
             Treatment   150   30   78    228       0.83    0.66 0.74
              Modifier   817  214  322   1139       0.79    0.72 0.75
          HealthStatus    80   24   27    107       0.77    0.75 0.76
         MedicalDevice   250   71   82    332       0.78    0.75 0.77
             Procedure   576  156  129    705       0.79    0.82 0.80
               Symptom  3831  858  744   4575       0.82    0.84 0.83
             Frequency   865  147  214   1079       0.85    0.80 0.83
    RelationshipStatus    19    2    5     24       0.90    0.79 0.84
              Duration  1845  244  465   2310       0.88    0.80 0.84
              Allergen    38    4    8     46       0.90    0.83 0.86
             VitalTest   143   16   29    172       0.90    0.83 0.86
               Disease  1745  296  270   2015       0.85    0.87 0.86
                Dosage   348   48   64    412       0.88    0.84 0.86
    AdmissionDischarge    29    4    5     34       0.88    0.85 0.87
                  Test  1064  136  144   1208       0.89    0.88 0.88
            Laterality   542   68   86    628       0.89    0.86 0.88
                 Route    42    5    6     48       0.89    0.88 0.88
              DateTime  4075  706  327   4402       0.85    0.93 0.89
                  Drug  1323  196  117   1440       0.87    0.92 0.89
          ClinicalDept   280   25   46    326       0.92    0.86 0.89
               Vaccine    37    4    5     42       0.90    0.88 0.89
                  Form   252   34   14    266       0.88    0.95 0.91
             Substance   398   58   23    421       0.87    0.95 0.91
PsychologicalCondition   411   42   33    444       0.91    0.93 0.92
                   Age   529   44   53    582       0.92    0.91 0.92
              BodyPart  2730  224  170   2900       0.92    0.94 0.93
            Employment  1168   37   75   1243       0.97    0.94 0.95
                Gender  1292   21   25   1317       0.98    0.98 0.98
             macro_avg 25414 3869 3816  29230       0.86    0.84 0.85
             micro_avg 25414 3869 3816  29230       0.87    0.87 0.87
```
