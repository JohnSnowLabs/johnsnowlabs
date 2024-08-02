---
layout: model
title: Legal Subpoena Classification
author: John Snow Labs
name: legclf_subpoena
date: 2023-06-05
tags: [en, legal, subpoena, licensed, tensorflow]
task: Text Classification
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: LegalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a multiclass classification model designed to determine the category of a section within a subpoena. The model can identify various classes, including `ATTACHMENT`,  `INSTRUCTION`,  `ARGUMENT`,  `DEFINITION`,  `REQUEST_FOR_ISSUANCE_OF_SUBPOENA`,  `NOTIFICATION`,  `DOCUMENT_REQUEST`,  `PRELIMINARY_STATEMENT`,  `CERTIFICATE_OF_SERVICE`,  `STATEMENT_OF_FACTS`,  `CONCLUSION`,  `BACKGROUND`,  `CERTIFICATE_OF_FILING`,  `INTRODUCTION`,  `DECLARATION` . A subpoena is a formal document issued by a court, grand jury, legislative body or committee, or authorized administrative agency. It commands an individual to appear at a specific time and provide testimony, either orally or in writing, regarding the matter specified in the document.

## Predicted Entities

`ATTACHMENT`, `INSTRUCTION`, `ARGUMENT`, `DEFINITION`, `REQUEST_FOR_ISSUANCE_OF_SUBPOENA`, `NOTIFICATION`, `DOCUMENT_REQUEST`, `PRELIMINARY_STATEMENT`, `CERTIFICATE_OF_SERVICE`, `STATEMENT_OF_FACTS`, `CONCLUSION`, `BACKGROUND`, `CERTIFICATE_OF_FILING`, `INTRODUCTION`, `DECLARATION`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_subpoena_en_1.0.0_3.0_1685989784048.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_subpoena_en_1.0.0_3.0_1685989784048.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

seq_classifier = legal.BertForSequenceClassification.pretrained("legclf_subpoena", "en", "legal/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("class")

pipeline = nlp.Pipeline(stages=[documentAssembler, tokenizer, seq_classifier])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = pipeline.fit(empty_data)

result = model.transform(spark.createDataFrame(data).toDF("text"))

result.select("text", "class.result").show(truncate=False)
```

</div>

## Results

```bash
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+
|text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |result      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+
|The Defendant filed a response opposing the Plaintiff's motion for summary judgment on November 15, 2023. The Defendant argues that there are genuine issues of material fact that should be decided by a jury, including disputes regarding the condition of the premises and the Plaintiff's alleged contributory negligence.The Court has reviewed the motions, responses, supporting evidence, and legal arguments presented by both parties. The Court held a hearing on December 5, 2023, to consider the Plaintiff's motion for summary judgment and to address any outstanding procedural matters.                                           |[BACKGROUND]|
|As the evidence in question was obtained through an unlawful search and seizure, it is tainted and should be suppressed under the fruit of the poisonous tree doctrine.D. Exclusionary RuleThe exclusionary rule is a vital tool for safeguarding individuals' Fourth Amendment rights and deterring law enforcement misconduct.Suppressing the unlawfully obtained evidence in this case would serve the purpose of the exclusionary rule by deterring future unlawful searches and seizures.Allowing the introduction of unlawfully obtained evidence would undermine the Fourth Amendment's protections and erode public trust in law enforcement.|[ARGUMENT]  |
|Sample Case: The Plaintiff claims strict liability against the Defendant, who owns a wild animal sanctuary. The Plaintiff argues that they were attacked and injured by one of the animals under the Defendant's care. Strict liability imposes liability on the Defendant without the need to prove negligence, as the ownership and management of wild animals are recognized as inherently dangerous activities."Intentional Tort" shall encompass a deliberate or intentional act by one party that causes harm or injury to another, resulting in legal liability and potential claims for damages.                                             |[DEFINITION]|
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legclf_subpoena|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[class]|
|Language:|en|
|Size:|403.0 MB|
|Case sensitive:|true|
|Max sentence length:|512|

## References

In house annotated data

## Benchmarking

```bash
label                                  precision    recall  f1-score   support
                        ARGUMENT       0.96      0.78      0.86        32
                      ATTACHMENT       0.90      0.93      0.92        41
                      BACKGROUND       0.87      0.92      0.89        37
           CERTIFICATE_OF_FILING       1.00      0.90      0.95        29
          CERTIFICATE_OF_SERVICE       0.84      0.90      0.87        29
                      CONCLUSION       1.00      1.00      1.00        36
                     DECLARATION       0.86      1.00      0.93        25
                      DEFINITION       0.97      1.00      0.99        35
                DOCUMENT_REQUEST       0.96      0.93      0.95        75
                     INSTRUCTION       0.99      0.97      0.98        73
                    INTRODUCTION       0.94      1.00      0.97        48
                    NOTIFICATION       1.00      0.97      0.99        34
           PRELIMINARY_STATEMENT       0.96      1.00      0.98        45
REQUEST_FOR_ISSUANCE_OF_SUBPOENA       1.00      0.98      0.99        42
              STATEMENT_OF_FACTS       1.00      0.98      0.99        49
                        accuracy       -         -         0.95       630
                       macro-avg       0.95      0.95      0.95       630
                    weighted-avg       0.96      0.95      0.95       630
```