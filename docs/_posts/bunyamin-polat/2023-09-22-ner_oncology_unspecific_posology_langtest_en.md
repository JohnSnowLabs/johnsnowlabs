---
layout: model
title: Extract Cancer Therapies and Posology Information (LangTest)
author: John Snow Labs
name: ner_oncology_unspecific_posology_langtest
date: 2023-09-22
tags: [en, ner, licensed, clinical, oncology, posology, langtest]
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

This model extracts mentions of treatments and posology information using unspecific labels (low granularity). It is the version of [ner_oncology_unspecific_posology](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_unspecific_posology_en.html) model augmented with `langtest` library.

Definitions of Predicted Entities:

- `Cancer_Therapy`: Mentions of cancer treatments, including chemotherapy, radiotherapy, surgery, and others.
- `Posology_Information`: Terms related to the posology of the treatment, including duration, frequencies, and dosage.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**     | 658                   | 228                  | 630                   | 1060                 | 70%                   | 49%                  | 82%                 |
| **add_slangs**       | 20                    | 14                   | 1268                  | 1274                 | 60%                   | 98%                  | 99%                 |
| **add_typo**         | 167                   | 142                  | 1121                  | 1146                 | 60%                   | 87%                  | 89%                 |
| **lowercase**        | 166                   | 116                  | 1122                  | 1172                 | 70%                   | 87%                  | 91%                 |
| **titlecase**        | 600                   | 200                  | 688                   | 1088                 | 70%                   | 53%                  | 84%                 |
| **uppercase**        | 1195                  | 268                  | 93                    | 1020                 | 60%                   | 7%                   | 79%                 |
| **weighted average** | **2806**              | **968**              | **4922**              | **6760**             | **65%**               | **63.69%**           | **87.47%**          |

## Predicted Entities

`Cancer_Therapy`, `Posology_Information`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_unspecific_posology_langtest_en_5.1.0_3.0_1695384084019.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_unspecific_posology_langtest_en_5.1.0_3.0_1695384084019.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_oncology_unspecific_posology_langtest", "en", "clinical/models") \
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

data = spark.createDataFrame([["The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses. She is currently receiving his second cycle of chemotherapy and is in good overall condition."]]).toDF("text")

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
    
val ner = MedicalNerModel.pretrained("ner_oncology_unspecific_posology_langtest", "en", "clinical/models")
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

val data = Seq("The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses. She is currently receiving his second cycle of chemotherapy and is in good overall condition.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------+--------------------+
|chunk           |ner_label           |
+----------------+--------------------+
|adriamycin      |Cancer_Therapy      |
|60 mg/m2        |Posology_Information|
|cyclophosphamide|Cancer_Therapy      |
|600 mg/m2       |Posology_Information|
|six courses     |Posology_Information|
|second cycle    |Posology_Information|
|chemotherapy    |Cancer_Therapy      |
+----------------+--------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_unspecific_posology_langtest|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.6 MB|

## References

In-house annotated oncology case reports.

## Benchmarking

```bash
label                 precision  recall  f1-score  support 
Cancer_Therapy        0.90       0.90    0.90      1845    
Posology_Information  0.87       0.86    0.87      1199    
micro-avg             0.89       0.89    0.89      3044    
macro-avg             0.89       0.88    0.88      3044    
weighted-avg          0.89       0.89    0.89      3044 
```