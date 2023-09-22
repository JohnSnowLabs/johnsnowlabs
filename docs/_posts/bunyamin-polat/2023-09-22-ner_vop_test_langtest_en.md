---
layout: model
title: Extract Test Entities from Voice of the Patient Documents (LangTest
author: John Snow Labs
name: ner_vop_test_langtest
date: 2023-09-22
tags: [en, clinical, ner, licensed, vop, test, langtest]
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

This model extracts test mentions from the documents transferred from the patient’s own sentences. It is the version of [ner_vop_test](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_test_en.html) model augmented with `langtest` library.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_abbreviation** | 149                   | 124                  | 305                   | 330                  | 70%                   | 67%                  | 73%                 |
| **add_ocr_typo**     | 280                   | 117                  | 217                   | 380                  | 70%                   | 44%                  | 76%                 |
| **add_punctuation**  | 0                     | 0                    | 4                     | 4                    | 70%                   | 100%                 | 100%                |
| **add_typo**         | 61                    | 51                   | 426                   | 430                  | 70%                   | 87%                  | 89%                 |
| **lowercase**        | 53                    | 50                   | 427                   | 430                  | 70%                   | 89%                  | 90%                 |
| **titlecase**        | 169                   | 83                   | 337                   | 423                  | 70%                   | 67%                  | 84%                 |
| **uppercase**        | 417                   | 106                  | 89                    | 400                  | 70%                   | 18%                  | 79%                 |
| **weighted average** | **1129**              | **531**              | **1805**              | **2397**             | **70%**               | **61.52%**           | **81.86%**          |

## Predicted Entities

`VitalTest`, `Test`, `Measurements`, `TestResult`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_test_langtest_en_5.1.0_3.0_1695371748577.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_test_langtest_en_5.1.0_3.0_1695371748577.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_vop_test_langtest", "en", "clinical/models") \
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

data = spark.createDataFrame([["I went to the endocrinology department to get my thyroid levels checked. They ordered a blood test and found out that I have hypothyroidism, so now I'm on medication to manage it."]]).toDF("text")

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
    
val ner = MedicalNerModel.pretrained("ner_vop_test_langtest", "en", "clinical/models")
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

val data = Seq("I went to the endocrinology department to get my thyroid levels checked. They ordered a blood test and found out that I have hypothyroidism, so now I'm on medication to manage it.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------+---------+
|chunk         |ner_label|
+--------------+---------+
|thyroid levels|Test     |
|blood test    |Test     |
+--------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_test_langtest|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.5 MB|

## References

In-house annotated health-related text in colloquial language.

## Sample text from the training dataset

Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you.

## Benchmarking

```bash
label         precision  recall  f1-score  support 
Measurements  0.74       0.74    0.74      81      
Test          0.86       0.85    0.85      607     
TestResult    0.76       0.81    0.78      343     
VitalTest     0.92       0.97    0.95      89      
micro-avg     0.82       0.84    0.83      1120    
macro-avg     0.82       0.84    0.83      1120    
weighted-avg  0.82       0.84    0.83      1120    
```
