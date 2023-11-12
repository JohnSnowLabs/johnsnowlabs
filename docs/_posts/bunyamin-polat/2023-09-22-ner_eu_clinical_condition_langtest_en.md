---
layout: model
title: Detect Clinical Conditions (LangTest - ner_eu_clinical_condition)
author: John Snow Labs
name: ner_eu_clinical_condition_langtest
date: 2023-09-22
tags: [en, ner, licensed, clinical, condition, langtest]
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

Pretrained named entity recognition (NER) deep learning model for clinical conditions. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state-of-the-art model for NER: Chiu & Nichols, Named Entity Recognition with Bidirectional LSTM-CNN. The model is the version of [ner_eu_clinical_condition](https://nlp.johnsnowlabs.com/2023/02/06/ner_eu_clinical_condition_en.html) model augmented with `langtest` library.

| **test_type**             | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|---------------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_abbreviation**      | 25                    | 31                   | 348                   | 486                  | 80%                   | 93%                  | 94%                 |
| **add_ocr_typo**          | 61                    | 66                   | 360                   | 501                  | 80%                   | 86%                  | 88%                 |
| **add_typo**              | 41                    | 41                   | 383                   | 528                  | 80%                   | 90%                  | 93%                 |
| **lowercase**             | 6                     | 5                    | 435                   | 583                  | 80%                   | 99%                  | 99%                 |
| **number_to_word**        | 4                     | 7                    | 131                   | 161                  | 80%                   | 97%                  | 96%                 |
| **strip_all_punctuation** | 22                    | 23                   | 421                   | 565                  | 80%                   | 95%                  | 96%                 |
| **strip_punctuation**     | 6                     | 5                    | 437                   | 582                  | 80%                   | 99%                  | 99%                 |
| **swap_entities**         | 60                    | 43                   | 138                   | 225                  | 80%                   | 70%                  | 84%                 |
| **titlecase**             | 106                   | 93                   | 337                   | 493                  | 80%                   | 76%                  | 84%                 |
| **uppercase**             | 193                   | 104                  | 250                   | 484                  | 80%                   | 56%                  | 82%                 |
| **weighted average**      | **524**               | **418**              | **3240**              | **4608**             | **80%**               | **86.08%**           | **91.68%**          |

## Predicted Entities

`clinical_condition`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_eu_clinical_condition_langtest_en_5.1.0_3.0_1695396170806.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_eu_clinical_condition_langtest_en_5.1.0_3.0_1695396170806.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

tokenizer = Tokenizer()\
	.setInputCols(["sentence"])\
	.setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
	.setInputCols(["sentence", "token"])\
	.setOutputCol("embeddings")

ner = MedicalNerModel.pretrained('ner_eu_clinical_condition_langtest', "en", "clinical/models") \
	.setInputCols(["sentence", "token", "embeddings"]) \
	.setOutputCol("ner")
 
ner_converter = NerConverterInternal()\
	.setInputCols(["sentence", "token", "ner"])\
	.setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
	document_assembler,
	sentence_detector,
	tokenizer,
	word_embeddings,
	ner,
	ner_converter])

data = spark.createDataFrame([["""Hyperparathyroidism was considered upon the fourth occasion. The history of weakness and generalized joint pains were present. He also had history of epigastric pain diagnosed informally as gastritis. He had previously had open reduction and internal fixation for the initial two fractures under general anesthesia. He sustained mandibular fracture."""]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val documenter = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols("sentence")
  .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
	.setInputCols(Array("sentence", "token"))
	.setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_eu_clinical_condition_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(documenter, sentence_detector, tokenizer, word_embeddings, ner_model, ner_converter))

val data = Seq(Array("""Hyperparathyroidism was considered upon the fourth occasion. The history of weakness and generalized joint pains were present. He also had history of epigastric pain diagnosed informally as gastritis. He had previously had open reduction and internal fixation for the initial two fractures under general anesthesia. He sustained mandibular fracture.""")).toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------------+------------------+
|chunk              |ner_label         |
+-------------------+------------------+
|Hyperparathyroidism|clinical_condition|
|weakness           |clinical_condition|
|joint pains        |clinical_condition|
|epigastric pain    |clinical_condition|
|gastritis          |clinical_condition|
|fractures          |clinical_condition|
|anesthesia         |clinical_condition|
|mandibular fracture|clinical_condition|
+-------------------+------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_eu_clinical_condition_langtest|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.6 MB|

## References

The corpus used for model training is provided by European Clinical Case Corpus (E3C), a project aimed at offering a freely available multilingual corpus of semantically annotated clinical narratives.

## Benchmarking

```bash
label               precision  recall  f1-score  support 
clinical_condition  0.95       0.95    0.95      432     
micro-avg           0.95       0.95    0.95      432     
macro-avg           0.95       0.95    0.95      432     
weighted-avg        0.95       0.95    0.95      432      
```
