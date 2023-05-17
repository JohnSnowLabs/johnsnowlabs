---
layout: model
title: Understanding Restriction Level of Assignment Clauses(Bert)
author: John Snow Labs
name: legclf_nda_assigments_bert
date: 2023-05-17
tags: [en, legal, licensed, bert, nda, classification, assigments, tensorflow]
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

Given a clause classified as `ASSIGNMENT ` using the `legmulticlf_mnda_sections_paragraph_other` classifier, you can subclassify the sentences as `PERMISSIVE_ASSIGNMENT`, `RESTRICTIVE_ASSIGNMENT` or `OTHER` from it using the `legclf_nda_assigments_bert` model. It has been trained with the SOTA approach.

## Predicted Entities

`PERMISSIVE_ASSIGNMENT`, `RESTRICTIVE_ASSIGNMENT`, `OTHER`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_nda_assigments_bert_en_1.0.0_3.0_1684350248553.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_nda_assigments_bert_en_1.0.0_3.0_1684350248553.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

sequence_classifier = legal.BertForSequenceClassification.pretrained("legclf_nda_assigments_bert", "en", "legal/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("class")\
    .setCaseSensitive(True)\
    .setMaxSentenceLength(512)

clf_pipeline = nlp.Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])

empty_df = spark.createDataFrame([['']]).toDF("text")

model = clf_pipeline.fit(empty_df)

text_list = [
"""This Agreement will be binding upon and inure to the benefit of each Party and its respective heirs, successors and assigns""",
"""All notices and other communications provided for in this Agreement and the other Loan Documents shall be in writing and may (subject to paragraph (b) below) be telecopied (faxed), mailed by certified mail return receipt requested, or delivered by hand or overnight courier service to the intended recipient at the addresses specified below or at such other address as shall be designated by any party listed below in a notice to the other parties listed below given in accordance with this Section.""",
"""This Agreement is a personal contract for XCorp, and the rights and interests of XCorp hereunder may not be sold, transferred, assigned, pledged or hypothecated except as otherwise expressly permitted by the Company"""
]

df = spark.createDataFrame(pd.DataFrame({"text" : text_list}))

result = model.transform(df)
```

</div>

## Results

```bash
+--------------------------------------------------------------------------------+----------------------+
|                                                                            text|                 class|
+--------------------------------------------------------------------------------+----------------------+
|This Agreement will be binding upon and inure to the benefit of each Party an...| PERMISSIVE_ASSIGNMENT|
|All notices and other communications provided for in this Agreement and the o...|                 OTHER|
|This Agreement is a personal contract for XCorp, and the rights and interests...|RESTRICTIVE_ASSIGNMENT|
+--------------------------------------------------------------------------------+----------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legclf_nda_assigments_bert|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[class]|
|Language:|en|
|Size:|406.4 MB|
|Case sensitive:|true|
|Max sentence length:|512|

## Sample text from the training dataset

In-house annotations on the Non-disclosure Agreements

## Benchmarking

```bash
label                   precision  recall  f1-score  support 
OTHER                   0.98       1.00    0.99      124     
PERMISSIVE_ASSIGNMENT   1.00       0.93    0.97      15      
RESTRICTIVE_ASSIGNMENT  1.00       0.96    0.98      25      
accuracy                -          -       0.99      164     
macro avg               0.99       0.96    0.98      164     
weighted avg            0.99       0.99    0.99      164     
```