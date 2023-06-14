---
layout: model
title: Extract Clinical Problem Entities from Voice of the Patient Documents (embeddings_clinical)
author: John Snow Labs
name: ner_vop_problem
date: 2023-06-06
tags: [licensed, clinical, ner, en, problem, vop]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.3
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts clinical problems from the documents transferred from the patient’s own sentences using a granular taxonomy.

## Predicted Entities

`PsychologicalCondition`, `Disease`, `Symptom`, `HealthStatus`, `Modifier`, `InjuryOrPoisoning`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/VOICE_OF_THE_PATIENTS/){:.button.button-orange}
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_problem_en_4.4.3_3.0_1686075641877.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_problem_en_4.4.3_3.0_1686075641877.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_vop_problem", "en", "clinical/models") \
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
    
val ner = MedicalNerModel.pretrained("ner_vop_problem", "en", "clinical/models")
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
| chunk                | ner_label   |
|:---------------------|:------------|
| pain                 | Symptom     |
| fatigue              | Symptom     |
| rheumatoid arthritis | Disease     |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_problem|
|Compatibility:|Healthcare NLP 4.4.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|3.8 MB|
|Dependencies:|embeddings_clinical|

## References

In-house annotated health-related text in colloquial language.

## Sample text from the training dataset

Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you.

## Benchmarking

```bash
                 label   tp   fp   fn  total  precision  recall   f1
PsychologicalCondition  413   40   31    444       0.91    0.93 0.92
               Disease 1748  288  267   2015       0.86    0.87 0.86
               Symptom 3726  668  849   4575       0.85    0.81 0.83
          HealthStatus   81   23   26    107       0.78    0.76 0.77
              Modifier  845  259  294   1139       0.77    0.74 0.75
     InjuryOrPoisoning  117   25   59    176       0.82    0.66 0.74
             macro_avg 6930 1303 1526   8456       0.83    0.80 0.81
             micro_avg 6930 1303 1526   8456       0.84    0.82 0.83
```