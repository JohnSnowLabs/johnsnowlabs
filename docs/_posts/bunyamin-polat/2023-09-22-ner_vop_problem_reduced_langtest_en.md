---
layout: model
title: Extract Clinical Problem Entities (low granularity) from Voice of the Patient Documents (LangTest)
author: John Snow Labs
name: ner_vop_problem_reduced_langtest
date: 2023-09-22
tags: [en, licensed, ner, clinical, vop, problem, langtest]
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

This model extracts clinical problems from the documents transferred from the patient’s own sentences. The taxonomy is reduced (one label for all clinical problems). The model is the version of [ner_vop_problem_reduced](https://nlp.johnsnowlabs.com/2023/06/07/ner_vop_problem_reduced_en.html) model augmented with `langtest` library.

| **test_type**             | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|---------------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_abbreviation**      | 855                   | 745                  | 2246                  | 2356                 | 60%                   | 72%                  | 76%                 |
| **add_ocr_typo**          | 1446                  | 900                  | 2023                  | 2569                 | 60%                   | 58%                  | 74%                 |
| **add_punctuation**       | 3                     | 0                    | 44                    | 47                   | 70%                   | 94%                  | 100%                |
| **add_slangs**            | 643                   | 471                  | 1240                  | 1412                 | 70%                   | 66%                  | 75%                 |
| **add_typo**              | 392                   | 353                  | 2964                  | 3016                 | 70%                   | 88%                  | 90%                 |
| **lowercase**             | 139                   | 101                  | 3083                  | 3121                 | 70%                   | 96%                  | 97%                 |
| **number_to_word**        | 42                    | 33                   | 638                   | 647                  | 70%                   | 94%                  | 95%                 |
| **strip_all_punctuation** | 272                   | 242                  | 3228                  | 3258                 | 70%                   | 92%                  | 93%                 |
| **strip_punctuation**     | 79                    | 79                   | 3388                  | 3388                 | 70%                   | 98%                  | 98%                 |
| **swap_entities**         | 692                   | 640                  | 2734                  | 2781                 | 70%                   | 80%                  | 81%                 |
| **titlecase**             | 1257                  | 764                  | 2255                  | 2748                 | 70%                   | 64%                  | 78%                 |
| **uppercase**             | 2510                  | 732                  | 1001                  | 2779                 | 70%                   | 29%                  | 79%                 |
| **weighted average**      | 8330                  | 5060                 | 24844                 | 28122                | 68%                   | 74.89%               | 84.75%              |

## Predicted Entities

`Problem`, `HealthStatus`, `Modifier`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_problem_reduced_langtest_en_5.1.0_3.0_1695367521585.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_problem_reduced_langtest_en_5.1.0_3.0_1695367521585.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_vop_problem_reduced_langtest", "en", "clinical/models") \
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

data = spark.createDataFrame([["I've been experiencing joint pain and fatigue lately, so I went to the rheumatology department. After some tests, they diagnosed me with rheumatoid arthritis and started me on a treatment plan to manage the symptoms."]]).toDF("text")

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
    
val ner = MedicalNerModel.pretrained("ner_vop_problem_reduced_langtest", "en", "clinical/models")
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

val data = Seq("I've been experiencing joint pain and fatigue lately, so I went to the rheumatology department. After some tests, they diagnosed me with rheumatoid arthritis and started me on a treatment plan to manage the symptoms.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------------+---------+
|chunk               |ner_label|
+--------------------+---------+
|pain                |Problem  |
|fatigue             |Problem  |
|rheumatoid arthritis|Problem  |
+--------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_problem_reduced_langtest|
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
HealthStatus  0.80       0.89    0.84      125     
Modifier      0.79       0.78    0.79      1069    
Problem       0.89       0.87    0.88      5762    
micro-avg     0.87       0.86    0.87      6956    
macro-avg     0.83       0.85    0.84      6956    
weighted-avg  0.87       0.86    0.87      6956    
```