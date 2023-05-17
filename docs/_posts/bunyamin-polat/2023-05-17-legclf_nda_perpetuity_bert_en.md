---
layout: model
title: Understanding Perpetuity in "Return of Confidential Information" Clauses (Bert)
author: John Snow Labs
name: legclf_nda_perpetuity_bert
date: 2023-05-17
tags: [en, legal, licensed, bert, nda, classification, perpetuity, tensorflow]
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

Given a clause classified as `RETURN_OF_CONF_INFO` using the `legmulticlf_mnda_sections_paragraph_other` classifier, you can subclassify the sentences as `PERPETUITY` or `OTHER` from it using the `legclf_nda_perpetuity` model. It has been trained with the SOTA approach

## Predicted Entities

`PERPETUITY`, `OTHER`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_nda_perpetuity_bert_en_1.0.0_3.0_1684353033843.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_nda_perpetuity_bert_en_1.0.0_3.0_1684353033843.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequence_classifier = legal.BertForSequenceClassification.pretrained("legclf_nda_perpetuity_bert", "en", "legal/models")\
    .setInputCols(["document", "token"])\
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
"""Notwithstanding the return or destruction of all Evaluation Material, you or your Representatives shall continue to be bound by your obligations of confidentiality and other obligations hereunder.""",
"""There are no intended third party beneficiaries to this Agreement."""
]

df = spark.createDataFrame(pd.DataFrame({"text" : text_list}))

result = model.transform(df)
```

</div>

## Results

```bash
+--------------------------------------------------------------------------------+----------+
|                                                                            text|     class|
+--------------------------------------------------------------------------------+----------+
|Notwithstanding the return or destruction of all Evaluation Material, you or ...|PERPETUITY|
|              There are no intended third-party beneficiaries to this Agreement.|     OTHER|
+--------------------------------------------------------------------------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legclf_nda_perpetuity_bert|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[class]|
|Language:|en|
|Size:|406.4 MB|
|Case sensitive:|true|
|Max sentence length:|512|

## References

In-house annotations on the Non-disclosure Agreements

## Benchmarking

```bash
label         precision  recall  f1-score  support 
OTHER         0.98       1.00    0.99      60      
PERPETUITY    1.00       0.89    0.94      9       
accuracy      -          -       0.99      69      
macro avg     0.99       0.94    0.97      69      
weighted avg  0.99       0.99    0.99      69 
```
