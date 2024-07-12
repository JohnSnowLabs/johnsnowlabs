---
layout: model
title: Extract treatment entities (Voice of the Patients)
author: John Snow Labs
name: ner_vop_treatment_wip
date: 2023-04-20
tags: [licensed, clinical, en, ner, vop, patient, treatment]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts treatments mentioned in documents transferred from the patient’s own sentences.

Note: ‘wip’ suffix indicates that the model development is work-in-progress and will be finalised and the model performance will improved in the upcoming releases.

## Predicted Entities

`Treatment`, `Frequency`, `Procedure`, `Route`, `Duration`, `Dosage`, `Drug`, `Form`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/VOP/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/VOICE_OF_PATIENT.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_treatment_wip_en_4.4.0_3.0_1682013186202.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_treatment_wip_en_4.4.0_3.0_1682013186202.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

word_embeddings = WordEmbeddingsModel().pretrained(embeddings_clinical, "en", "clinical/models")\
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")                

ner = MedicalNerModel.pretrained("ner_vop_treatment_wip", "en", "clinical/models") \
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

data = spark.createDataFrame([["My grandpa was diagnosed with type 2 diabetes and had to make some changes to his lifestyle. He also takes metformin and glipizide to help regulate his blood sugar levels. It"s been a bit of an adjustment, but he"s doing well."]]).toDF("text")

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
    
val word_embeddings = WordEmbeddingsModel().pretrained(embeddings_clinical, "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                
    
val ner = MedicalNerModel.pretrained("ner_vop_treatment_wip", "en", "clinical/models")
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

val data = Seq("My grandpa was diagnosed with type 2 diabetes and had to make some changes to his lifestyle. He also takes metformin and glipizide to help regulate his blood sugar levels. It"s been a bit of an adjustment, but he"s doing well.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
| chunk     | ner_label   |
|:----------|:------------|
| metformin | Drug        |
| glipizide | Drug        |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_treatment_wip|
|Compatibility:|Healthcare NLP 4.4.0+|
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

Hello,I”m 20 year old girl. I”m diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss, from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I”m taking weekly supplement of vitamin D and 1000 mcg b12 daily. I”m taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I”m facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you.

## Benchmarking

```bash
    label   tp  fp  fn  total  precision  recall   f1
Treatment  144  44  67    211       0.77    0.68 0.72
Frequency  801 111 271   1072       0.88    0.75 0.81
Procedure  505 104 112    617       0.83    0.82 0.82
    Route   29   3   8     37       0.91    0.78 0.84
 Duration 1926 382 345   2271       0.83    0.85 0.84
   Dosage  350  56  49    399       0.86    0.88 0.87
     Drug 1210 125 108   1318       0.91    0.92 0.91
     Form  235  23  18    253       0.91    0.93 0.92
macro_avg 5200 848 978   6178       0.86    0.83 0.84
micro_avg 5200 848 978   6178       0.86    0.84 0.85
```
