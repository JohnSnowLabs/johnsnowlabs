---
layout: model
title: Extract Clinical Entities from Voice of the Patient Documents (LangTest)
author: John Snow Labs
name: ner_vop_langtest
date: 2023-10-10
tags: [en, clinical, licensed, ner, vop, langtest]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.1.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts healthcare-related terms from the documents transferred from the patient’s own sentences. It is the version of [ner_vop](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_en.html) model augmented with `langtest` library.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**     | 3230                  | 1015                 | 1520                  | 3735                 | 70%                   | 32%                  | 79%                 |
| **add_typo**         | 1088                  | 942                  | 3472                  | 3645                 | 70%                   | 76%                  | 79%                 |
| **lowercase**        | 413                   | 346                  | 4043                  | 4110                 | 70%                   | 91%                  | 92%                 |
| **swap_entities**    | 986                   | 1018                 | 3541                  | 3497                 | 70%                   | 78%                  | 77%                 |
| **titlecase**        | 2424                  | 1364                 | 2382                  | 3442                 | 70%                   | 50%                  | 72%                 |
| **uppercase**        | 4361                  | 1433                 | 445                   | 3373                 | 70%                   | 9%                   | 70%                 |
| **weighted average** | **12502**             | **6118**             | **15403**             | **21802**            | **70%**               | **55.20%**           | **78.09%**          |

## Predicted Entities

`Gender`, `Employment`, `Age`, `BodyPart`, `Substance`, `Form`, `PsychologicalCondition`, `Vaccine`, `Drug`, `DateTime`, `ClinicalDept`, `Laterality`, `Test`, `AdmissionDischarge`, `Disease`, `VitalTest`, `Dosage`, `Duration`, `RelationshipStatus`, `Route`, `Allergen`, `Frequency`, `Symptom`, `Procedure`, `HealthStatus`, `InjuryOrPoisoning`, `Modifier`, `Treatment`, `SubstanceQuantity`, `MedicalDevice`, `TestResult`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_langtest_en_5.1.1_3.0_1696921310149.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_langtest_en_5.1.1_3.0_1696921310149.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")                

ner = MedicalNerModel.pretrained("ner_vop_langtest", "en", "clinical/models") \
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
    
val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")
    
val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")
    
val word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                
    
val ner = MedicalNerModel.pretrained("ner_vop_langtest", "en", "clinical/models")
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
+--------------------+----------------------+
|chunk               |ner_label             |
+--------------------+----------------------+
|20 year old         |Age                   |
|girl                |Gender                |
|hyperthyroid        |Disease               |
|1 month ago         |DateTime              |
|weak                |Symptom               |
|light               |Symptom               |
|digestion           |Symptom               |
|panic attacks       |PsychologicalCondition|
|depression          |PsychologicalCondition|
|left                |Laterality            |
|chest               |BodyPart              |
|pain                |Symptom               |
|increased           |TestResult            |
|heart rate          |VitalTest             |
|rapidly             |Modifier              |
|weight loss         |Symptom               |
|4 months            |Duration              |
|hospital            |ClinicalDept          |
|discharged          |AdmissionDischarge    |
|hospital            |ClinicalDept          |
|blood tests         |Test                  |
|brain               |BodyPart              |
|mri                 |Test                  |
|ultrasound scan     |Test                  |
|endoscopy           |Procedure             |
|doctors             |Employment            |
|homeopathy doctor   |Employment            |
|he                  |Gender                |
|hyperthyroid        |Disease               |
|TSH                 |Test                  |
|0.15                |TestResult            |
|T3                  |Test                  |
|T4                  |Test                  |
|normal              |TestResult            |
|b12 deficiency      |Disease               |
|vitamin D deficiency|Disease               |
|weekly              |Frequency             |
|supplement          |Drug                  |
|vitamin D           |Drug                  |
|1000 mcg            |Dosage                |
|b12                 |Drug                  |
|daily               |Frequency             |
|homeopathy medicine |Drug                  |
|40 days             |Duration              |
|2nd test            |Test                  |
|after 30 days       |DateTime              |
|TSH                 |Test                  |
|0.5                 |TestResult            |
|now                 |DateTime              |
|weakness            |Symptom               |
|depression          |PsychologicalCondition|
|last week           |DateTime              |
|rapid heartrate     |Symptom               |
|allopathy medicine  |Drug                  |
|homeopathy          |Treatment             |
|thyroid             |BodyPart              |
|allopathy           |Treatment             |
+--------------------+----------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_langtest|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.7 MB|

## References

In-house annotated health-related text in colloquial language.

## Sample text from the training dataset

Hello,I’m 20 year old girl. I’m diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss, from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I’m taking weekly supplement of vitamin D and 1000 mcg b12 daily. I’m taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I’m facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you.

## Benchmarking

```bash
label                   precision  recall  f1-score  support 
AdmissionDischarge      0.78       0.78    0.78      32      
Age                     0.83       0.87    0.85      248     
Allergen                0.86       0.41    0.56      29      
BodyPart                0.91       0.92    0.91      2089    
ClinicalDept            0.93       0.83    0.88      184     
DateTime                0.82       0.86    0.84      1599    
Disease                 0.81       0.83    0.82      1140    
Dosage                  0.79       0.80    0.80      238     
Drug                    0.89       0.86    0.87      897     
Duration                0.81       0.75    0.78      802     
Employment              0.96       0.92    0.94      831     
Form                    0.90       0.89    0.90      207     
Frequency               0.80       0.67    0.73      499     
Gender                  0.98       0.98    0.98      1047    
HealthStatus            0.77       0.81    0.79      72      
InjuryOrPoisoning       0.73       0.64    0.68      102     
Laterality              0.79       0.89    0.84      397     
MedicalDevice           0.69       0.72    0.70      190     
Modifier                0.80       0.70    0.75      839     
Procedure               0.85       0.72    0.78      297     
PsychologicalCondition  0.89       0.90    0.90      272     
RelationshipStatus      1.00       0.90    0.95      10      
Route                   0.79       0.67    0.72      33      
Substance               0.88       0.82    0.85      281     
SubstanceQuantity       0.88       0.49    0.63      43      
Symptom                 0.87       0.82    0.84      2690    
Test                    0.83       0.79    0.81      590     
TestResult              0.71       0.72    0.71      367     
Treatment               0.81       0.67    0.74      104     
Vaccine                 0.92       0.86    0.89      14      
VitalTest               0.76       0.74    0.75      74      
micro-avg               0.86       0.83    0.85      16217   
macro-avg               0.84       0.78    0.80      16217   
weighted-avg            0.86       0.83    0.84      16217   
```
