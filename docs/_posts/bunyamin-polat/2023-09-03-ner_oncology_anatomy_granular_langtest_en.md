---
layout: model
title: Extract Granular Anatomical Entities from Oncology Texts (langtest)
author: John Snow Labs
name: ner_oncology_anatomy_granular_langtest
date: 2023-09-03
tags: [en, licensed, ner, clinical, oncology, granular, langtest]
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

This model extracts mentions of anatomical entities using granular labels. It is the version of [ner_oncology_anatomy_granular](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_anatomy_granular_en.html) model augmented with `langtest` library.

Definitions of Predicted Entities:

- `Direction`: Directional and laterality terms, such as "left", "right", "bilateral", "upper" and "lower".
- `Site_Bone`: Anatomical terms that refer to the human skeleton.
- `Site_Brain`: Anatomical terms that refer to the central nervous system (including the brain stem and the cerebellum).
- `Site_Breast`: Anatomical terms that refer to the breasts.
- `Site_Liver`: Anatomical terms that refer to the liver.
- `Site_Lung`: Anatomical terms that refer to the lungs.
- `Site_Lymph_Node`: Anatomical terms that refer to lymph nodes, excluding adenopathies.
- `Site_Other_Body_Part`: Relevant anatomical terms that are not included in the rest of the anatomical entities.

## Predicted Entities

`Direction`, `Site_Bone`, `Site_Brain`, `Site_Breast`, `Site_Liver`, `Site_Lung`, `Site_Lymph_Node`, `Site_Other_Body_Part`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_anatomy_granular_langtest_en_5.0.2_3.0_1693756631307.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_anatomy_granular_langtest_en_5.0.2_3.0_1693756631307.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_oncology_anatomy_granular_langtest", "en", "clinical/models") \
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

data = spark.createDataFrame([["The patient presented a mass in her left breast, and a possible metastasis in her lungs and in her liver."]]).toDF("text")

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
    
val ner = MedicalNerModel.pretrained("ner_oncology_anatomy_granular_langtest", "en", "clinical/models")
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

val data = Seq("The patient presented a mass in her left breast, and a possible metastasis in her lungs and in her liver.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------+-----------+
|chunk |ner_label  |
+------+-----------+
|left  |Direction  |
|breast|Site_Breast|
|lungs |Site_Lung  |
|liver |Site_Liver |
+------+-----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_anatomy_granular_langtest|
|Compatibility:|Healthcare NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.7 MB|

## References

In-house annotated oncology case reports.

## Benchmarking

```bash
label                   precision  recall  f1-score  support 
B-Direction             0.86       0.94    0.90      870     
B-Site_Bone             0.85       0.82    0.83      247     
B-Site_Lymph_Node       0.86       0.86    0.86      239     
I-Site_Lymph_Node       0.89       0.88    0.88      331     
B-Site_Other_Body_Part  0.78       0.76    0.77      1045    
I-Site_Other_Body_Part  0.66       0.72    0.69      529     
B-Site_Brain            0.86       0.85    0.86      184     
I-Site_Brain            0.80       0.74    0.77      70      
B-Site_Lung             0.82       0.89    0.85      361     
I-Site_Lung             0.76       0.75    0.76      167     
I-Site_Bone             0.80       0.71    0.75      106     
I-Direction             0.74       0.85    0.79      84      
B-Site_Breast           0.90       0.96    0.93      117     
B-Site_Liver            0.81       0.89    0.85      168     
I-Site_Liver            0.50       0.62    0.55      52      
I-Site_Breast           0.93       0.76    0.84      17      
micro-avg               0.80       0.83    0.81      4587    
macro-avg               0.80       0.81    0.80      4587    
weighted-avg            0.80       0.83    0.81      4587    
```
