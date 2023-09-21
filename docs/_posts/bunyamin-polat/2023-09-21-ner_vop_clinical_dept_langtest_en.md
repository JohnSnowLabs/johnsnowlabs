---
layout: model
title: Extract Clinical Department Entities from Voice of the Patient Documents (LangTest)
author: John Snow Labs
name: ner_vop_clinical_dept_langtest
date: 2023-09-21
tags: [en, clinical, licensed, ner, vop, langtest]
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

This model extracts medical devices and clinical department mentions terms from the documents transferred from the patient’s own sentences. It is the version of [ner_vop_clinical_dept](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_clinical_dept_en.html) model augmented with `langtest` library.

| test_type             | before fail_count | after fail_count | before pass_count | after pass_count | minimum pass_rate | before pass_rate | after pass_rate |
|-----------------------|-------------------|------------------|-------------------|------------------|-------------------|------------------|-----------------|
| add_abbreviation      | 143               | 121              | 258               | 280              | 60%               | 64%              | 70%             |
| add_ocr_typo          | 198               | 98               | 217               | 317              | 60%               | 52%              | 76%             |
| add_typo              | 24                | 29               | 376               | 369              | 70%               | 94%              | 93%             |
| lowercase             | 24                | 18               | 368               | 374              | 70%               | 94%              | 95%             |
| number_to_word        | 2                 | 2                | 83                | 83               | 70%               | 98%              | 98%             |
| strip_all_punctuation | 3                 | 11               | 414               | 406              | 70%               | 99%              | 97%             |
| strip_punctuation     | 3                 | 4                | 413               | 412              | 70%               | 99%              | 99%             |
| swap_entities         | 60                | 69               | 310               | 285              | 70%               | 84%              | 81%             |
| titlecase             | 104               | 83               | 313               | 334              | 70%               | 75%              | 80%             |
| uppercase             | 340               | 70               | 77                | 347              | 70%               | 18%              | 83%             |
| weighted average      | 901               | 505              | 2829              | 3207             | 68%               | 75.84%           | 86.40%          |

## Predicted Entities

`AdmissionDischarge`, `ClinicalDept`, `MedicalDevice`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_clinical_dept_langtest_en_5.1.0_3.0_1695327130583.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_clinical_dept_langtest_en_5.1.0_3.0_1695327130583.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_vop_clinical_dept_langtest", "en", "clinical/models") \
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

data = spark.createDataFrame([["My little brother is having surgery tomorrow in the orthopedic department. He is getting a titanium plate put in his leg to help it heal faster. Wishing him a speedy recovery!"]]).toDF("text")

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
    
val ner = MedicalNerModel.pretrained("ner_vop_clinical_dept_langtest", "en", "clinical/models")
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

val data = Seq("My little brother is having surgery tomorrow in the orthopedic department. He is getting a titanium plate put in his leg to help it heal faster. Wishing him a speedy recovery!").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---------------------+-------------+
|chunk                |ner_label    |
+---------------------+-------------+
|orthopedic department|ClinicalDept |
|titanium plate       |MedicalDevice|
+---------------------+-------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_clinical_dept_langtest|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.7 MB|

## References

In-house annotated health-related text in colloquial language

## Sample text from the training dataset

Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you.

## Benchmarking

```bash
label               precision  recall  f1-score  support 
AdmissionDischarge  0.92       0.96    0.94      23      
ClinicalDept        0.93       0.92    0.93      233     
MedicalDevice       0.82       0.82    0.82      227     
micro-avg           0.88       0.88    0.88      483     
macro-avg           0.89       0.90    0.89      483     
weighted-avg        0.88       0.88    0.88      483     
```