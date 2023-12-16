---
layout: model
title: Extract Demographic Entities from Oncology Texts (langtest)
author: John Snow Labs
name: ner_oncology_demographics_langtest
date: 2023-09-03
tags: [en, ner, licensed, clinical, oncology, demographics, langtest]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.0.2
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts demographic information from oncology texts, including age, gender, and smoking status. It is the version of [ner_oncology_demographics](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_demographics_en.html) model augmented with `langtest` library

Definitions of Predicted Entities:

- `Age`: All mention of ages, past or present, related to the patient or with anybody else.
- `Gender`: Gender-specific nouns and pronouns (including words such as "him" or "she", and family members such as "father").
- `Race_Ethnicity`: The race and ethnicity categories include racial and national origin or sociocultural groups.
- `Smoking_Status`: All mentions of smoking related to the patient or to someone else.

## Predicted Entities

`Age`, `Gender`, `Race_Ethnicity`, `Smoking_Status`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_demographics_langtest_en_5.0.2_3.0_1693752265725.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_demographics_langtest_en_5.0.2_3.0_1693752265725.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_oncology_demographics_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter])

data = spark.createDataFrame([["The patient is a 40 year old man with history of heavy smoking."]]).toDF("text")

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
    
val ner = MedicalNerModel.pretrained("ner_oncology_demographics_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")
    
val ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

        
val pipeline = new Pipeline().setStages(Array(document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter))    

val data = Seq("The patient is a 40 year old man with history of heavy smoking.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------+--------------+
|chunk      |ner_label     |
+-----------+--------------+
|40 year old|Age           |
|man        |Gender        |
|smoking    |Smoking_Status|
+-----------+--------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_demographics_langtest|
|Compatibility:|Healthcare NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.8 MB|

## References

In-house annotated oncology case reports.

## Benchmarking

```bash
label             precision  recall  f1-score  support 
B-Gender          0.99       1.00    0.99      1235    
B-Age             0.97       0.96    0.97      224     
I-Age             0.98       0.99    0.99      799     
B-Smoking_Status  0.93       0.89    0.91      57      
I-Gender          0.00       0.00    0.00      1       
B-Race_Ethnicity  0.87       1.00    0.93      45      
I-Race_Ethnicity  0.71       0.83    0.77      6       
I-Smoking_Status  0.67       0.91    0.77      11      
micro-avg         0.98       0.99    0.98      2378    
macro-avg         0.76       0.82    0.79      2378    
weighted-avg      0.98       0.99    0.98      2378   
```
