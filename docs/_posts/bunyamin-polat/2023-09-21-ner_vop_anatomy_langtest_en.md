---
layout: model
title: Extract Anatomical Entities from Voice of the Patient Documents (LangTest)
author: John Snow Labs
name: ner_vop_anatomy_langtest
date: 2023-09-21
tags: [en, clinical, licensed, ner, vop, anatomy, langtest]
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

This model extracts anatomical terms from the documents transferred from the patient’s own sentences. It is the version of [ner_vop_anatomy](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_anatomy_en.html) model augmented with `langtest` library.

| test_type             | before fail_count | after fail_count | before pass_count | after pass_count | minimum pass_rate | before pass_rate | after pass_rate |
|-----------------------|-------------------|------------------|-------------------|------------------|-------------------|------------------|-----------------|
| **add_abbreviation**      | 295               | 288              | 1272              | 1279             | 70%               | 81%              | 82%             |
| **add_ocr_typo**          | 832               | 438              | 937               | 1331             | 70%               | 53%              | 75%             |
| **add_punctuation**       | 0                 | 0                | 22                | 22               | 70%               | 100%             | 100%            |
| **add_typo**              | 134               | 123              | 1559              | 1589             | 70%               | 92%              | 93%             |
| **lowercase**             | 19                | 15               | 1649              | 1653             | 70%               | 99%              | 99%             |
| **strip_all_punctuation** | 64                | 74               | 1717              | 1707             | 70%               | 96%              | 96%             |
| **strip_punctuation**     | 17                | 30               | 1745              | 1732             | 70%               | 99%              | 98%             |
| **swap_entities**         | 183               | 153              | 1542              | 1567             | 70%               | 89%              | 91%             |
| **titlecase**             | 301               | 291              | 1483              | 1493             | 70%               | 83%              | 84%             |
| **uppercase**             | 1286              | 191              | 497               | 1592             | 70%               | 28%              | 89%             |
| **weighted average**      | **3131**              | **1603**             | **12423**             | **13965**            | **70%**               | **79.87%**           | **89.70%**          |

## Predicted Entities

`BodyPart`, `Laterality`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_anatomy_langtest_en_5.1.0_3.0_1695307725354.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_anatomy_langtest_en_5.1.0_3.0_1695307725354.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_vop_anatomy_langtest", "en", "clinical/models") \
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

data = spark.createDataFrame([["Hey everyone, I'm a 30-year-old woman who has been experiencing some lower back pain. My doctor said that I have a herniated disc in my lumbar spine, and recommended physical therapy to strengthen the muscles around the affected area. Any tips for managing back pain?"]]).toDF("text")

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
    
val ner = MedicalNerModel.pretrained("ner_vop_anatomy_langtest", "en", "clinical/models")
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

val data = Seq("Hey everyone, I'm a 30-year-old woman who has been experiencing some lower back pain. My doctor said that I have a herniated disc in my lumbar spine, and recommended physical therapy to strengthen the muscles around the affected area. Any tips for managing back pain?").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------+----------+
|chunk       |ner_label |
+------------+----------+
|lower       |Laterality|
|back        |BodyPart  |
|lumbar spine|BodyPart  |
|muscles     |BodyPart  |
|back        |BodyPart  |
+------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_anatomy_langtest|
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
BodyPart      0.94       0.94    0.94      2676    
Laterality    0.89       0.85    0.87      538     
micro-avg     0.94       0.93    0.93      3214    
macro-avg     0.92       0.90    0.91      3214    
weighted-avg  0.94       0.93    0.93      3214    
```
