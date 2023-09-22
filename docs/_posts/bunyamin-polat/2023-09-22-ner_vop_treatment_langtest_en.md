---
layout: model
title: Extract Treatment Entities from Voice of the Patient Documents (LangTest)
author: John Snow Labs
name: ner_vop_treatment_langtest
date: 2023-09-22
tags: [en, ner, clinical, licensed, vop, treatment, langtest]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.1.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts treatments mentioned in documents transferred from the patient’s own sentences. It is the version of [ner_vop_treatment](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_treatment_en.html) model augmented with `langtest` library.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**     | 773                   | 514                  | 1009                  | 1268                 | 60%                   | 57%                  | 71%                 |
| **add_typo**         | 173                   | 131                  | 1541                  | 1577                 | 70%                   | 90%                  | 92%                 |
| **lowercase**        | 73                    | 74                   | 1603                  | 1602                 | 70%                   | 96%                  | 96%                 |
| **number_to_word**   | 101                   | 103                  | 524                   | 522                  | 70%                   | 84%                  | 84%                 |
| **swap_entities**    | 328                   | 331                  | 1380                  | 1394                 | 70%                   | 81%                  | 81%                 |
| **titlecase**        | 648                   | 285                  | 1152                  | 1515                 | 70%                   | 64%                  | 84%                 |
| **uppercase**        | 1282                  | 304                  | 518                   | 1496                 | 70%                   | 29%                  | 83%                 |
| **weighted average** | **3378**              | **1742**             | **7727**              | **9374**             | **69%**               | **69.58%**           | **84.33%**          |

## Predicted Entities

`Drug`, `Form`, `Dosage`, `Frequency`, `Route`, `Duration`, `Procedure`, `Treatment`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_treatment_langtest_en_5.1.0_3.0_1695373543924.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_treatment_langtest_en_5.1.0_3.0_1695373543924.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_vop_treatment_langtest", "en", "clinical/models") \
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

data = spark.createDataFrame([["Greetings, I'm a 51-year-old woman who has been struggling with depression. I was prescribed 20mg of Prozac daily by my doctor. My mood has improved, but I've been experiencing a bit of nausea and dry mouth. Has anyone else taken Prozac for depression? How long until you saw a significant improvement? Any tips for managing the side effects?"]]).toDF("text")

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
    
val ner = MedicalNerModel.pretrained("ner_vop_treatment_langtest", "en", "clinical/models")
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

val data = Seq("Greetings, I'm a 51-year-old woman who has been struggling with depression. I was prescribed 20mg of Prozac daily by my doctor. My mood has improved, but I've been experiencing a bit of nausea and dry mouth. Has anyone else taken Prozac for depression? How long until you saw a significant improvement? Any tips for managing the side effects?").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------+---------+
|chunk |ner_label|
+------+---------+
|20mg  |Dosage   |
|Prozac|Drug     |
|daily |Frequency|
|Prozac|Drug     |
+------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_treatment_langtest|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.6 MB|

## References

In-house annotated health-related text in colloquial language.

## Sample text from the training dataset

Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you.

## Benchmarking

```bash
label         precision  recall  f1-score  support 
Dosage        0.85       0.84    0.84      221     
Drug          0.91       0.93    0.92      820     
Duration      0.85       0.82    0.83      812     
Form          0.88       0.99    0.93      196     
Frequency     0.87       0.83    0.85      459     
Procedure     0.76       0.76    0.76      280     
Route         0.82       0.85    0.84      33      
Treatment     0.87       0.82    0.84      116     
micro-avg     0.87       0.86    0.86      2937    
macro-avg     0.85       0.85    0.85      2937    
weighted-avg  0.87       0.86    0.86      2937    
```