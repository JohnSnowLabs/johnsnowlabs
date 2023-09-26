---
layout: model
title: Extract Temporal Entities from Voice of the Patient Documents (LangTest)
author: John Snow Labs
name: ner_vop_temporal_langtest
date: 2023-09-22
tags: [en, ner, clinical, licensed, vop, temporal, langtest]
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

This model extracts temporal references from the documents transferred from the patient’s own sentences. It is the version of [ner_vop_temporal](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_temporal_en.html) model augmented with `langtest` library.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**     | 1623                  | 928                  | 1065                  | 1760                 | 60%                   | 40%                  | 65%                 |
| **add_typo**         | 202                   | 161                  | 2401                  | 2432                 | 70%                   | 92%                  | 94%                 |
| **lowercase**        | 55                    | 59                   | 2466                  | 2462                 | 70%                   | 98%                  | 98%                 |
| **swap_entities**    | 609                   | 597                  | 1905                  | 1911                 | 70%                   | 76%                  | 76%                 |
| **titlecase**        | 680                   | 480                  | 2037                  | 2237                 | 70%                   | 75%                  | 82%                 |
| **uppercase**        | 1911                  | 337                  | 805                   | 2379                 | 70%                   | 30%                  | 88%                 |
| **weighted average** | **5080**              | **2562**             | **10679**             | **13181**            | **68%**               | **67.76%**           | **83.73%**          |

## Predicted Entities

`DateTime`, `Duration`, `Frequency`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_temporal_langtest_en_5.1.0_3.0_1695369554858.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_temporal_langtest_en_5.1.0_3.0_1695369554858.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_vop_temporal_langtest", "en", "clinical/models") \
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

data = spark.createDataFrame([["Hi everyone, I'm a 35-year-old woman who was diagnosed with depression last year. I've been taking medication and seeing a therapist for about six months now, and I'm starting to feel a lot better. I have therapy sessions once a week, and I take my medication every day at the same time. I've noticed that my mood tends to be better in the mornings than in the evenings. Has anyone else had a similar experience? Any tips for managing depression long-term?"]]).toDF("text")

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
    
val ner = MedicalNerModel.pretrained("ner_vop_temporal_langtest", "en", "clinical/models")
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

val data = Seq("Hi everyone, I'm a 35-year-old woman who was diagnosed with depression last year. I've been taking medication and seeing a therapist for about six months now, and I'm starting to feel a lot better. I have therapy sessions once a week, and I take my medication every day at the same time. I've noticed that my mood tends to be better in the mornings than in the evenings. Has anyone else had a similar experience? Any tips for managing depression long-term?").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---------------+---------+
|chunk          |ner_label|
+---------------+---------+
|last year      |DateTime |
|six months     |Duration |
|now            |DateTime |
|once a week    |Frequency|
|every day      |Frequency|
|in the mornings|DateTime |
|in the evenings|DateTime |
+---------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_temporal_langtest|
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
DateTime      0.84       0.85    0.84      2131    
Duration      0.80       0.81    0.81      1058    
Frequency     0.84       0.86    0.85      672     
micro-avg     0.83       0.84    0.83      3861    
macro-avg     0.83       0.84    0.83      3861    
weighted-avg  0.83       0.84    0.83      3861
```
