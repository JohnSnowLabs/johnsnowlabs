---
layout: model
title: Few-Shot Assertion Model
author: John Snow Labs
name: assertion_fewshotclassifier
date: 2024-04-15
tags: [en, licensed]
task: Assertion Status
language: en
edition: Healthcare NLP 5.3.2
spark_version: 3.0
supported: true
annotator: FewShotAssertionClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Assign assertion status to clinical entities

## Predicted Entities

`absent`, `present`, `conditional`, `associated_with_someone_else`, `hypothetical`, `possible`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_fewshotclassifier_en_5.3.2_3.0_1713190012506.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_fewshotclassifier_en_5.3.2_3.0_1713190012506.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
#define pipeline
ocument_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
   .setInputCols("document")\
   .setOutputCol("sentence")

tokenizer = Tokenizer()\
   .setInputCols(["sentence"])\
   .setOutputCol("token")

embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
   .setInputCols(["sentence", "token"])\
   .setOutputCol("embeddings") \
   .setCaseSensitive(False)

ner = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models") \
   .setInputCols(["sentence", "token", "embeddings"]) \
   .setOutputCol("ner")

ner_converter = NerConverterInternal()\
   .setInputCols(["sentence", "token", "ner"])\
   .setWhiteList(["Disease_Syndrome_Disorder", "Hypertension", "Symptom", "VS_Finding"])\
   .setOutputCol("ner_chunk")

few_shot_assertion_classifier = FewShotAssertionClassifierModel().pretrained("assertion_fewshotclassifier","en", "clinical/models")\
    .setInputCols(["sentence", "ner_chunk"])\
    .setOutputCol("assertion_fewshot")

pipeline = Pipeline()\
    .setStages([
        document_assembler,
        sentence_detector,
        tokenizer,
        embeddings,
        ner,
        ner_converter,
        few_shot_assertion_classifier
])

texts = [
    ["Includes hypertension and chronic obstructive pulmonary disease."],
    ["Her former vascular no arteriovenous malformations are identified; there is no evidence of recurrence of her former vascular malformation."],
    ["He is an elderly gentleman in no acute distress. He is sitting up in bed eating his breakfast."],
    ["Trachea is midline. No jugular venous pressure distention is noted. No adenopathy in the cervical, supraclavicular, or axillary areas."],
    ["Soft and not tender. There may be some fullness in the left upper quadrant, although I do not appreciate a true spleen with inspiration."]
]

spark_df = spark.createDataFrame(texts).toDF("text")

results = pipeline.fit(spark_df).transform(spark_df)

```
```scala
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
   .setInputCols(Array("document"))
   .setOutputCol("sentences")

val tokenizer = Tokenizer()
   .setInputCols(Array("sentence"))
   .setOutputCol("token")

val embeddings = WordEmbeddingsModel
   .pretrained("embeddings_clinical", "en", "clinical/models")
   .setInputCols(Array("sentence", "token"))
   .setOutputCol("embeddings")
   .setCaseSensitive(False)

val ner = MedicalNerModel
   .pretrained("ner_jsl", "en", "clinical/models")
   .setInputCols(["sentence", "token", "embeddings"])
   .setOutputCol("ner")

val nerConverter = NerConverterInternal()
   .setInputCols(Array("sentence", "token", "ner"))
   .setWhiteList("Disease_Syndrome_Disorder", "Hypertension", "Symptom", "VS_Finding")
   .setOutputCol("ner_chunk")

val fewShotAssertionClassifier = LargeFewShotClassifierModel().pretrained("assertion_fewshotclassifier")
  .setInputCols(Array("sentence"))
  .setBatchSize(1)
  .setOutputCol("label")

val pipeline = new Pipeline().setStages(Array(
 documentAssembler, sentenceDetector, tokenizer, embeddings, ner, nerConverter, fewShotAssertionClassifier))

val model = pipeline.fit(Seq().toDS.toDF("text"))
val results = model.transform(
  Seq(Array(
    "Includes hypertension and chronic obstructive pulmonary disease.",
    "Her former vascular no arteriovenous malformations are identified; there is no evidence of recurrence of her former vascular malformation.",
    "He is an elderly gentleman in no acute distress. He is sitting up in bed eating his breakfast."],
    "Trachea is midline. No jugular venous pressure distention is noted. No adenopathy in the cervical, supraclavicular, or axillary areas.",
    "Soft and not tender. There may be some fullness in the left upper quadrant, although I do not appreciate a true spleen with inspiration."
)).toDS.toDF("text"))

results
  .selectExpr("explode(assertion) as assertion")
  .selectExpr("assertion_fewshot.result", "assertion_fewshot.metadata.chunk", "assertion_fewshot.metadata.confidence")
  .show(truncate = false)
```
</div>

## Results

```bash
+-------------------------------------+-----+---+---------+----------+
|chunk                                |begin|end|assertion|confidence|
+-------------------------------------+-----+---+---------+----------+
|hypertension                         |0    |63 |present  |1.0       |
|chronic obstructive pulmonary disease|0    |63 |present  |1.0       |
|arteriovenous malformations          |0    |65 |absent   |1.0       |
|vascular malformation                |67   |137|absent   |0.9999956 |
|distress                             |0    |47 |absent   |1.0       |
|jugular venous pressure distention   |20   |66 |absent   |1.0       |
|adenopathy                           |68   |133|absent   |1.0       |
|tender                               |0    |19 |absent   |0.9999999 |
|fullness                             |21   |135|present  |0.6837093 |
+-------------------------------------+-----+---+---------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_fewshotclassifier|
|Compatibility:|Healthcare NLP 5.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|403.6 MB|
|Case sensitive:|false|

## References

Trained with an augmented version of the i2b2 dataset.
