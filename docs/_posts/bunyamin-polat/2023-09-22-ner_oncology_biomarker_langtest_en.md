---
layout: model
title: Extract Biomarkers and their Results (LangTest)
author: John Snow Labs
name: ner_oncology_biomarker_langtest
date: 2023-09-22
tags: [en, ner, clinical, licensed, oncology, biomarker, langtest]
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

This model extracts mentions of biomarkers and biomarker results from oncology texts. It is the version of [ner_oncology_biomarker](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_biomarker_en.html) model augmented with `langtest` library.

Definitions of Predicted Entities:

- `Biomarker`: Biological molecules that indicate the presence or absence of cancer, or the type of cancer (including oncogenes).
- `Biomarker_Result`: Terms or values that are identified as the result of biomarkers.

| **test_type**             | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|---------------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_abbreviation**      | 87                    | 75                   | 1879                  | 1891                 | 92%                   | 96%                  | 96%                 |
| **add_ocr_typo**          | 144                   | 125                  | 2037                  | 2056                 | 92%                   | 93%                  | 94%                 |
| **add_punctuation**       | 1                     | 0                    | 97                    | 98                   | 92%                   | 99%                  | 100%                |
| **add_typo**              | 52                    | 40                   | 2128                  | 2149                 | 92%                   | 98%                  | 98%                 |
| **number_to_word**        | 114                   | 82                   | 867                   | 899                  | 92%                   | 88%                  | 92%                 |
| **strip_all_punctuation** | 97                    | 86                   | 2149                  | 2160                 | 92%                   | 96%                  | 96%                 |
| **titlecase**             | 168                   | 164                  | 2092                  | 2096                 | 92%                   | 93%                  | 93%                 |
| **uppercase**             | 217                   | 97                   | 2049                  | 2169                 | 92%                   | 90%                  | 96%                 |
| **weighted average**      | **880**               | **669**              | **13298**             | **13518**            | **92%**               | **93.79%**           | **95.28%**          |

## Predicted Entities

`Biomarker`, `Biomarker_Result`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_biomarker_langtest_en_5.1.0_3.0_1695395379174.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_biomarker_langtest_en_5.1.0_3.0_1695395379174.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_oncology_biomarker_langtest", "en", "clinical/models") \
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

data = spark.createDataFrame([["The results of immunohistochemical examination showed that she tested negative for CK7, synaptophysin (Syn), chromogranin A (CgA), Muc5AC, human epidermal growth factor receptor-2 (HER2), and Muc6; positive for CK20, Muc1, Muc2, E-cadherin, and p53; the Ki-67 index was about 87% ."]]).toDF("text")

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
    
val ner = MedicalNerModel.pretrained("ner_oncology_biomarker_langtest", "en", "clinical/models")
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

val data = Seq("The results of immunohistochemical examination showed that she tested negative for CK7, synaptophysin (Syn), chromogranin A (CgA), Muc5AC, human epidermal growth factor receptor-2 (HER2), and Muc6; positive for CK20, Muc1, Muc2, E-cadherin, and p53; the Ki-67 index was about 87% .").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------+----------------+
|chunk                                   |ner_label       |
+----------------------------------------+----------------+
|negative                                |Biomarker_Result|
|CK7                                     |Biomarker       |
|synaptophysin                           |Biomarker       |
|Syn                                     |Biomarker       |
|chromogranin A                          |Biomarker       |
|CgA                                     |Biomarker       |
|Muc5AC                                  |Biomarker_Result|
|human epidermal growth factor receptor-2|Biomarker       |
|HER2                                    |Biomarker       |
|Muc6                                    |Biomarker       |
|positive                                |Biomarker_Result|
|CK20                                    |Biomarker       |
|Muc1                                    |Biomarker       |
|Muc2                                    |Biomarker       |
|E-cadherin                              |Biomarker       |
|p53                                     |Biomarker       |
|Ki-67 index                             |Biomarker       |
+----------------------------------------+----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_biomarker_langtest|
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
label             precision  recall  f1-score  support 
Biomarker         0.86       0.85    0.85      615     
Biomarker_Result  0.79       0.72    0.75      346     
micro-avg         0.84       0.80    0.82      961     
macro-avg         0.82       0.78    0.80      961     
weighted-avg      0.83       0.80    0.82      961   
```