---
layout: model
title: Detect Adverse Drug Events (langtest)
author: John Snow Labs
name: ner_ade_clinical_langtest
date: 2023-07-31
tags: [ner, clinical, licensed, en, langtest]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.0.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Detect adverse reactions of drugs in reviews, tweets, and medical text using pretrained NER model. This model is augmented version of [ner_ade_clinical](https://nlp.johnsnowlabs.com/2021/04/01/ner_ade_clinical_en.html)

## Predicted Entities

`DRUG`, `ADE`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ADE/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/16.Adverse_Drug_Event_ADE_NER_and_Classifier.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_ade_clinical_langtest_en_5.0.0_3.0_1690825306693.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_ade_clinical_langtest_en_5.0.0_3.0_1690825306693.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
         
sentence_detector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_ade_clinical_langtest", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")
    
nlp_pipeline = Pipeline(
    stages=[
        document_assembler, 
        sentence_detector, 
        tokenizer, 
        word_embeddings, 
        clinical_ner, 
        ner_converter
    ])

text ="""I asked my doctor what could have caused this, and he said it was probably from the Lipitor. Recently I experienced extreme stomach pain that stretched to my side and back. The stomach pain came suddenly and it would come and go for a week before it became so bad I could not sleep. I had just gotten over a urinary tract infection (one of the side-effects) and I thought it had returned, but the symptoms were different. I still had the urge to urinate constantly, but it would come and go, and I would have no symptoms for a day, then it would return again. I remembered reading the pamphlet that comes with the prescription drugs, and it mentioning some of the symptoms that I was experiencing. I stopped taking the Lipitor for a day, and I did not have any more stomach pain or urgency. I also had been experiencing lack of energy for quite some time, and I attributed this to stress, but after reading this website, I feel it was due to the Lipitor also. I don't think I will take this drug anymore, and since I read that taking vitamin C can help you with your cholesterol, I think I will try this method instead. I think there should be a better alternative to lowering cholesterol than such a potent drug that can cause so many side effects. I don't want to be a case-study when they finally take this drug off the market."""

data = spark.createDataFrame([[text]]).toDF("text")

result = nlp_pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
         
val sentence_detector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val embeddings_clinical = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_ade_clinical_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
 	.setInputCols(Array("sentence", "token", "ner"))
 	.setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(document_assembler, 
                                              sentence_detector, 
                                              tokenizer, 
                                              embeddings_clinical, 
                                              ner, 
                                              ner_converter))


text ="""I asked my doctor what could have caused this, and he said it was probably from the Lipitor. Recently I experienced extreme stomach pain that stretched to my side and back. The stomach pain came suddenly and it would come and go for a week before it became so bad I could not sleep. I had just gotten over a urinary tract infection (one of the side-effects) and I thought it had returned, but the symptoms were different. I still had the urge to urinate constantly, but it would come and go, and I would have no symptoms for a day, then it would return again. I remembered reading the pamphlet that comes with the prescription drugs, and it mentioning some of the symptoms that I was experiencing. I stopped taking the Lipitor for a day, and I did not have any more stomach pain or urgency. I also had been experiencing lack of energy for quite some time, and I attributed this to stress, but after reading this website, I feel it was due to the Lipitor also. I don't think I will take this drug anymore, and since I read that taking vitamin C can help you with your cholesterol, I think I will try this method instead. I think there should be a better alternative to lowering cholesterol than such a potent drug that can cause so many side effects. I don't want to be a case-study when they finally take this drug off the market."""

val data = Seq(text).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------------------+-----+----+---------+
|chunk                     |begin|end |ner_label|
+--------------------------+-----+----+---------+
|the Lipitor               |80   |90  |DRUG     |
|stomach pain              |124  |135 |ADE      |
|back                      |167  |170 |ADE      |
|stomach pain              |177  |188 |ADE      |
|urinary tract infection   |308  |330 |ADE      |
|urge to urinate constantly|438  |463 |ADE      |
|the prescription drugs    |610  |631 |DRUG     |
|the Lipitor               |715  |725 |DRUG     |
|lack of energy            |820  |833 |ADE      |
|Lipitor                   |946  |952 |DRUG     |
|vitamin C                 |1034 |1042|DRUG     |
|I don't                   |1250 |1256|DRUG     |
+--------------------------+-----+----+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_ade_clinical_langtest|
|Compatibility:|Healthcare NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|2.8 MB|

## References

Trained by in-house dataset.

## Benchmarking

```bash
 label      tp      fp      fn   total  precision  recall      f1  
    DRUG  8482.0  1068.0  1113.0  9595.0     0.8882   0.884  0.8861  
     ADE  1881.0   769.0   811.0  2692.0     0.7098  0.6987  0.7042  
   macro      -       -       -       -       -       -      0.7951
   micro      -       -       -       -       -       -      0.8462
```