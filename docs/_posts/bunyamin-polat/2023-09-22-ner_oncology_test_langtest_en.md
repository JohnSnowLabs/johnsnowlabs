---
layout: model
title: Extract Oncology Tests (LangTest)
author: John Snow Labs
name: ner_oncology_test_langtest
date: 2023-09-22
tags: [en, ner, clinical, licensed, oncology, test, langtest]
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

This model extracts mentions of tests from oncology texts, including pathology tests and imaging tests. It is the version of [ner_oncology_test](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_test_en.html) model augmented with `langtest` library.

Definitions of Predicted Entities:

- `Biomarker`: Biological molecules that indicate the presence or absence of cancer, or the type of cancer. Oncogenes are excluded from this category.
- `Biomarker_Result`: Terms or values that are identified as the result of biomarkers.
- `Imaging_Test`: Imaging tests mentioned in texts, such as "chest CT scan".
- `Oncogene`: Mentions of genes that are implicated in the etiology of cancer.
- `Pathology_Test`: Mentions of biopsies or tests that use tissue samples.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**     | 235                   | 213                  | 1937                  | 1959                 | 80%                   | 89%                  | 90%                 |
| **add_typo**         | 101                   | 103                  | 2058                  | 2057                 | 80%                   | 95%                  | 95%                 |
| **number_to_word**   | 87                    | 82                   | 832                   | 837                  | 80%                   | 91%                  | 91%                 |
| **swap_entities**    | 149                   | 126                  | 492                   | 505                  | 80%                   | 77%                  | 80%                 |
| **titlecase**        | 488                   | 184                  | 1761                  | 2065                 | 80%                   | 78%                  | 92%                 |
| **uppercase**        | 645                   | 185                  | 1612                  | 2072                 | 80%                   | 71%                  | 92%                 |
| **weighted average** | **1470**              | **680**              | **6755**              | **7536**             | **80%**               | **82.13%**           | **91.72%**          |

## Predicted Entities

`Biomarker`, `Biomarker_Result`, `Imaging_Test`, `Oncogene`, `Pathology_Test`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_test_langtest_en_5.1.0_3.0_1695391226396.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_test_langtest_en_5.1.0_3.0_1695391226396.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_oncology_test_langtest", "en", "clinical/models") \
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

data = spark.createDataFrame([["A biopsy was conducted using an ultrasound guided thick needle. His chest computed tomography (CT scan) was negative."]]).toDF("text")

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
    
val ner = MedicalNerModel.pretrained("ner_oncology_test_langtest", "en", "clinical/models")
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

val data = Seq("A biopsy was conducted using an ultrasound guided thick needle. His chest computed tomography (CT scan) was negative.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------------------+--------------+
|chunk                    |ner_label     |
+-------------------------+--------------+
|biopsy                   |Pathology_Test|
|ultrasound               |Imaging_Test  |
|chest computed tomography|Imaging_Test  |
|CT scan                  |Imaging_Test  |
+-------------------------+--------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_test_langtest|
|Compatibility:|Healthcare NLP 5.1.0+|
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
label               precision  recall  f1-score  support 
B-Pathology_Test    0.78       0.80    0.79      254     
I-Pathology_Test    0.83       0.75    0.79      263     
B-Imaging_Test      0.85       0.89    0.87      414     
I-Imaging_Test      0.78       0.91    0.84      633     
B-Biomarker_Result  0.82       0.80    0.81      289     
I-Biomarker_Result  0.83       0.82    0.83      374     
B-Biomarker         0.83       0.81    0.82      374     
I-Biomarker         0.85       0.70    0.77      375     
B-Oncogene          0.79       0.86    0.82      100     
I-Oncogene          0.81       0.82    0.81      184     
micro-avg           0.82       0.82    0.82      3260    
macro-avg           0.82       0.81    0.81      3260    
weighted-avg        0.82       0.82    0.82      3260    
```
