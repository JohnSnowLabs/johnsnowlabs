---
layout: model
title: Extract Treatment Entities from Voice of the Patient Documents (embeddings_clinical_large)
author: John Snow Labs
name: ner_vop_treatment_emb_clinical_large
date: 2023-06-06
tags: [license, clinical, ner, en, vop, treatment, drug, licensed]
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

This model extracts treatments mentioned in documents transferred from the patient’s own sentences.

## Predicted Entities

`Drug`, `Form`, `Route`, `Dosage`, `Duration`, `Procedure`, `Frequency`, `Treatment`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/VOP/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/VOICE_OF_PATIENT.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_treatment_emb_clinical_large_en_4.4.3_3.0_1686077860546.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_treatment_emb_clinical_large_en_4.4.3_3.0_1686077860546.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical_large", "en", "clinical/models")\
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")                

ner = MedicalNerModel.pretrained("ner_vop_treatment_emb_clinical_large", "en", "clinical/models") \
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

data = spark.createDataFrame([["My grandpa was diagnosed with type 2 diabetes and had to make some changes to his lifestyle. He also takes metformin and glipizide to help regulate his blood sugar levels. It's been a bit of an adjustment, but he's doing well."]]).toDF("text")

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
    
val word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical_large", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                
    
val ner = MedicalNerModel.pretrained("ner_vop_treatment_emb_clinical_large", "en", "clinical/models")
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

val data = Seq("My grandpa was diagnosed with type 2 diabetes and had to make some changes to his lifestyle. He also takes metformin and glipizide to help regulate his blood sugar levels. It's been a bit of an adjustment, but he's doing well.").toDS.toDF("text")

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
|Model Name:|ner_vop_treatment_emb_clinical_large|
|Compatibility:|Healthcare NLP 4.4.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|3.8 MB|
|Dependencies:|embeddings_clinical_large|

## References

In-house annotated health-related text in colloquial language.

## Sample text from the training dataset

Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you.

## Benchmarking

```bash
    label   tp  fp  fn  total  precision  recall   f1
     Drug 1265  67 175   1440       0.95    0.88 0.91
     Form  252  35  14    266       0.88    0.95 0.91
    Route   42   5   6     48       0.89    0.88 0.88
   Dosage  331  28  81    412       0.92    0.80 0.86
 Duration 2005 405 305   2310       0.83    0.87 0.85
Procedure  559 104 146    705       0.84    0.79 0.82
Frequency  895 197 184   1079       0.82    0.83 0.82
Treatment  167  55  61    228       0.75    0.73 0.74
macro_avg 5516 896 972   6488       0.86    0.84 0.85
micro_avg 5516 896 972   6488       0.86    0.85 0.85
```
