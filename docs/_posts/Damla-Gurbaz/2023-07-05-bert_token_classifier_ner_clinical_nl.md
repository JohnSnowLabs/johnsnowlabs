---
layout: model
title: Detect Problems, Tests and Treatments (BertForTokenClassifier - Dutch)
author: John Snow Labs
name: bert_token_classifier_ner_clinical
date: 2023-07-05
tags: [licensed, nl, clinical, ner, berfortokenclassification, tensorflow]
task: Named Entity Recognition
language: nl
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalBertForTokenClassifier
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terminology. This model is trained with BertForTokenClassification method from transformers library and imported into Spark NLP.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_clinical_nl_4.4.4_3.0_1688590388744.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_clinical_nl_4.4.4_3.0_1688590388744.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()	.setInputCol("text")	.setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")   .setInputCols(["document"])  .setOutputCol("sentence")

tokenizer = Tokenizer()  .setInputCols("sentence")  .setOutputCol("token")

tokenClassifier = MedicalBertForTokenClassifier.pretrained("bert_token_classifier_ner_clinical", "nl", "clinical/models")  .setInputCols(["token", "sentence"])  .setOutputCol("ner")  .setCaseSensitive(True)

ner_converter = NerConverterInternal()  .setInputCols(["sentence","token","ner"])  .setOutputCol("ner_chunk")

pipeline =  Pipeline(stages=[
		documentAssembler,
		sentenceDetector,
		tokenizer,
		tokenClassifier,
		ner_converter])


sample_text = "Dhr. Van Dijk, 58 jaar oud, kwam naar de kliniek met klachten van aanhoudende hoest, koorts en kortademigheid. We hebben besloten om een röntgenfoto van de borst, bloedonderzoek en een CT-scan te laten uitvoeren. De resultaten wezen op een ernstige longontsteking, een verhoogd aantal witte bloedcellen en mogelijk COPD. Hem is een antibiotica-kuur en een hoestsiroop voorgeschreven. Daarnaast adviseren we hem een voedzaam dieet te volgen."

df = spark.createDataFrame([[sample_text]]).toDF("text")

result = pipeline.fit(df).transform(df)
```
```scala
val documentAssembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx") 	.setInputCols(Array("document"))
	.setOutputCol("sentence")

val tokenizer = new Tokenizer()
	.setInputCols("sentence")
	.setOutputCol("token")

val tokenClassifier = MedicalBertForTokenClassifier.pretrained("bert_token_classifier_ner_clinical", "nl", "clinical/models")
  .setInputCols(Array("token", "sentence"))
  .setOutputCol("ner")
  .setCaseSensitive(True)

val ner_converter = new NerConverterInternal()
	.setInputCols(Array("sentence","token","ner"))
	.setOutputCol("ner_chunk")

val pipeline =  new Pipeline().setStages(Array(
		documentAssembler,
		sentenceDetector,
		tokenizer,
		tokenClassifier,
		ner_converter))

val sample_text = Seq("Dhr. Van Dijk, 58 jaar oud, kwam naar de kliniek met klachten van aanhoudende hoest, koorts en kortademigheid. We hebben besloten om een röntgenfoto van de borst, bloedonderzoek en een CT-scan te laten uitvoeren. De resultaten wezen op een ernstige longontsteking, een verhoogd aantal witte bloedcellen en mogelijk COPD. Hem is een antibiotica-kuur en een hoestsiroop voorgeschreven. Daarnaast adviseren we hem een voedzaam dieet te volgen.").toDS.toDF("text")

val result = pipeline.fit(sample_text).transform(sample_text)
```
</div>

## Results

```bash
+-------------------------------------+---------+
|chunk                                |ner_label|
+-------------------------------------+---------+
|aanhoudende hoest                    |PROBLEM  |
|koorts                               |PROBLEM  |
|kortademigheid                       |PROBLEM  |
|een röntgenfoto van de borst         |TEST     |
|bloedonderzoek                       |TEST     |
|een CT-scan                          |TEST     |
|ernstige longontsteking              |PROBLEM  |
|een verhoogd aantal witte bloedcellen|PROBLEM  |
|COPD                                 |PROBLEM  |
|een antibiotica-kuur                 |TREATMENT|
|hoestsiroop                          |TREATMENT|
|een voedzaam dieet                   |TREATMENT|
+-------------------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_clinical|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|nl|
|Size:|626.3 MB|
|Case sensitive:|true|
|Max sentence length:|128|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
   B-PROBLEM       0.82      0.84      0.83      1346
      B-TEST       0.81      0.77      0.79       635
 B-TREATMENT       0.74      0.82      0.78       631
   I-PROBLEM       0.82      0.84      0.83      1349
      I-TEST       0.64      0.68      0.66       224
 I-TREATMENT       0.67      0.60      0.63       485
           O       0.94      0.92      0.93      6127
    accuracy        -         -        0.87     10797
   macro-avg       0.78      0.78      0.78     10797
weighted-avg       0.87      0.87      0.87     10797
```