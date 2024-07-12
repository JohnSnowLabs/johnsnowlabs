---
layout: model
title: Extract Entities Related to TNM Staging (LangTest)
author: John Snow Labs
name: ner_oncology_tnm_langtest
date: 2023-09-22
tags: [en, ner, clinical, licensed, oncology, tnm, langtest]
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

This model extracts staging information and mentions related to tumors, lymph nodes, and metastases. It is the version of [ner_oncology_tnm](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_tnm_en.html) model augmented with `langtest` library.

Definitions of Predicted Entities:

- `Cancer_Dx`: Mentions of cancer diagnoses (such as "breast cancer") or pathological types that are usually used as synonyms for "cancer" (e.g. "carcinoma"). When anatomical references are present, they are included in the Cancer_Dx extraction.
- `Lymph_Node`: Mentions of lymph nodes and pathological findings of the lymph nodes.
- `Lymph_Node_Modifier`: Words that refer to a lymph node being abnormal (such as "enlargement").
- `Metastasis`: Terms that indicate a metastatic disease. Anatomical references are not included in these extractions.
- `Staging`: Mentions of cancer stage such as "stage 2b" or "T2N1M0". It also includes words such as "in situ", "early-stage" or "advanced".
- `Tumor`: All nonspecific terms that may be related to tumors, either malignant or benign (for example: "mass", "tumor", "lesion", or "neoplasm").
- `Tumor_Description`: Information related to tumor characteristics, such as size, presence of invasion, grade, and hystological type.


| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_typo**         | 249                   | 209                  | 4089                  | 4146                 | 70%                   | 94%                  | 95%                 |
| **lowercase**        | 273                   | 238                  | 4243                  | 4278                 | 70%                   | 94%                  | 95%                 |
| **swap_entities**    | 362                   | 342                  | 1192                  | 1211                 | 70%                   | 77%                  | 78%                 |
| **titlecase**        | 985                   | 712                  | 3517                  | 3790                 | 70%                   | 78%                  | 84%                 |
| **uppercase**        | 1779                  | 378                  | 2736                  | 4137                 | 70%                   | 61%                  | 92%                 |
| **weighted average** | **3648**              | **1879**             | **15777**             | **17562**            | **70%**               | **81.22%**           | **90.33%**          |

## Predicted Entities

`Cancer_Dx`, `Lymph_Node`, `Lymph_Node_Modifier`, `Metastasis`, `Staging`, `Tumor`, `Tumor_Description`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_tnm_langtest_en_5.1.0_3.0_1695387402214.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_tnm_langtest_en_5.1.0_3.0_1695387402214.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_oncology_tnm_langtest", "en", "clinical/models") \
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

data = spark.createDataFrame([["Chest computed tomography (CT) showed pulmonary lesions in the posterior segment of the right upper lobe, and peripheral lung cancer with multiple pulmonary metastases. Multiple metastases of the thoracic vertebrae, sternum, and ribs were considered, which were similar to previous CT images."]]).toDF("text")

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
    
val ner = MedicalNerModel.pretrained("ner_oncology_tnm_langtest", "en", "clinical/models")
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

val data = Seq("Chest computed tomography (CT) showed pulmonary lesions in the posterior segment of the right upper lobe, and peripheral lung cancer with multiple pulmonary metastases. Multiple metastases of the thoracic vertebrae, sternum, and ribs were considered, which were similar to previous CT images.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------+----------+
|chunk                 |ner_label |
+----------------------+----------+
|lesions               |Tumor     |
|peripheral lung cancer|Cancer_Dx |
|metastases            |Metastasis|
|metastases            |Metastasis|
+----------------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_tnm_langtest|
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
label                precision  recall  f1-score  support 
Cancer_Dx            0.88       0.86    0.87      721     
Lymph_Node           0.78       0.77    0.77      271     
Lymph_Node_Modifier  0.79       0.76    0.77      45      
Metastasis           0.92       0.92    0.92      321     
Staging              0.88       0.80    0.84      123     
Tumor                0.90       0.86    0.88      1018    
Tumor_Description    0.70       0.68    0.69      1060    
micro-avg            0.83       0.80    0.81      3559    
macro-avg            0.84       0.81    0.82      3559    
weighted-avg         0.83       0.80    0.81      3559    
```
