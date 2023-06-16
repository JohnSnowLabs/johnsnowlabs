---
layout: model
title: Three Class Assertion Status (embeddings_clinical_large) - Voice of the Patients
author: John Snow Labs
name: assertion_vop_three_class_emb_clinical_large_wip
date: 2023-06-16
tags: [licensed, vop, en, assertion, clinical]
task: Assertion Status
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: AssertionDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Assertion status model used to predict if an NER chunk refers to a positive finding from the patient (Present_Or_Past), if it refers to a family member or another person (SomeoneElse) or if it is mentioned but not as something present (Hypothetical_Or_Absent).

## Predicted Entities

`Present_Or_Past`, `Hypothetical_Or_Absent`, `SomeoneElse`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_vop_three_class_emb_clinical_large_wip_en_4.4.4_3.0_1686925909999.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_vop_three_class_emb_clinical_large_wip_en_4.4.4_3.0_1686925909999.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\\
    .setInputCol("text")\\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\\
    .setInputCols(["document"])\\
    .setOutputCol("sentence")

tokenizer = Tokenizer() \\
    .setInputCols(["sentence"]) \\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical_large", "en", "clinical/models")\\
    .setInputCols(["sentence", "token"]) \\
    .setOutputCol("embeddings")                

ner = MedicalNerModel.pretrained("ner_vop_emb_clinical_large", "en", "clinical/models") \\
    .setInputCols(["sentence", "token", "embeddings"]) \\
    .setOutputCol("ner")

ner_converter = NerConverterInternal() \\
    .setInputCols(["sentence", "token", "ner"]) \\
    .setOutputCol("ner_chunk")

assertion = AssertionDLModel.pretrained("assertion_vop_three_class_emb_clinical_large_wip", "en", "clinical/models") \\
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \\
    .setOutputCol("assertion")

pipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter,
                            assertion])

data = spark.createDataFrame([["I was feeling a lot of anxiety honestly. It was right after my mother was diagnosed with diabetes."]]).toDF("text")

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
    
val ner = MedicalNerModel.pretrained("ner_vop_emb_clinical_large", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")
    
val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val clinical_assertion = AssertionDLModel.pretrained("assertion_vop_three_class_emb_clinical_large_wip","en","clinical/models")
    .setInputCols("sentence","ner_chunk","embeddings")
    .setOutputCol("assertion")
        
val pipeline = new Pipeline().setStages(Array(document_assembler,
                                              sentence_detector,
                                              tokenizer,
                                              word_embeddings,
                                              ner,
                                              ner_converter,
                                              assertion))

val data = Seq("I was feeling a lot of anxiety honestly. It was right after my mother was diagnosed with diabetes.").toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
| chunk    | ner_label              | assertion       |
|:---------|:-----------------------|:----------------|
| anxiety  | PsychologicalCondition | Present_Or_Past |\n| mother   | Gender                 | SomeoneElse     |
| diabetes | Disease                | SomeoneElse     |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_vop_three_class_emb_clinical_large_wip|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, chunk, embeddings]|
|Output Labels:|[assertion]|
|Language:|en|
|Size:|945.9 KB|
|Dependencies:|embeddings_clinical_large|

## References

In-house annotated health-related text in colloquial language.

## Sample text from the training dataset

Hey there! I'm a 20-year-old girl who recently got diagnosed with hyperthyroidism. I've been dealing with a bunch of crappy symptoms like feeling weak, dizzy, having trouble digesting stuff, panic attacks, feeling down, sharp chest pain, racing heart, and losing weight like crazy for the past four months. Finally, I ended up in the hospital and just got discharged. Man, those doctors couldn't figure out what was wrong with me! I had to go through a bunch of tests like bloodwork, MRI, ultrasound, and even an endoscopy, but they were all clueless. But hey, I finally saw a homeopathy doc who figured out I have hyperthyroidism. My TSH levels were super low at 0.15, but T3 and T4 were fine. Turns out, I also have low B12 and vitamin D, so now I'm taking supplements for that. Been doing the homeopathy thing for 40 days now, and my TSH is up to 0.5, which is a bit of a relief. But now I'm having trouble breathing and my heart is racing like crazy. Should I start regular medicine or stick to homeopathy? Some friends are telling me not to take any chances, but I don't know, man. What do you think? Thanks, and sorry for my bad english 😐

## Benchmarking

```bash
                 label  precision  recall  f1-score  support
Hypothetical_Or_Absent       0.80    0.77      0.78   970
       Present_Or_Past       0.84    0.86      0.85  1457
           SomeoneElse       0.77    0.82      0.80   211
              accuracy       0.82    0.82      0.82     2638
             macro avg       0.81    0.82      0.81  2638
          weighted avg       0.82    0.82      0.82  2638
```