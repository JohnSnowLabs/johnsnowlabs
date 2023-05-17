---
layout: model
title: Understanding Non-compete Items in Non-Compete Clauses (Bert)
author: John Snow Labs
name: legclf_nda_non_compete_items_bert
date: 2023-05-17
tags: [en, legal, licensed, bert, classification, nda, non_compete, tensorflow]
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

Given a clause classified as `NON_COMP` using the `legmulticlf_mnda_sections_paragraph_other` classifier, you can subclassify the sentences as `NON_COMPETE_ITEMS`, or `OTHER` from it using the `legclf_nda_non_compete_items_bert` model. It has been trained with the SOTA approach.

## Predicted Entities

`NON_COMPETE_ITEMS`, `OTHER`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_nda_non_compete_items_bert_en_1.0.0_3.0_1684358961459.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_nda_non_compete_items_bert_en_1.0.0_3.0_1684358961459.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequence_classifier = legal.BertForSequenceClassification.pretrained("legclf_nda_non_compete_items_bert", "en", "legal/models")\
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
"""This Agreement will be binding upon and inure to the benefit of each Party and its respective heirs, successors and assigns""",
"""Activity that is in direct competition with the Company's business, including but not limited to developing, marketing, or selling products or services that are similar to those of the Company."""
]

df = spark.createDataFrame(pd.DataFrame({"text" : text_list}))

result = model.transform(df)
```

</div>

## Results

```bash
+--------------------------------------------------------------------------------+-----------------+
|                                                                            text|            class|
+--------------------------------------------------------------------------------+-----------------+
|This Agreement will be binding upon and inure to the benefit of each Party an...|            OTHER|
|Activity that is in direct competition with the Company's business, including...|NON_COMPETE_ITEMS|
+--------------------------------------------------------------------------------+-----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legclf_nda_non_compete_items_bert|
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
label              precision  recall  f1-score  support 
NON_COMPETE_ITEMS  1.00       1.00    1.00      10      
OTHER              1.00       1.00    1.00      64      
accuracy           -          -       1.00      74      
macro avg          1.00       1.00    1.00      74      
weighted avg       1.00       1.00    1.00      74  
```
