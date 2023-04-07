---
layout: model
title: Understanding Perpetuity in "Return of Confidential Information" Clauses
author: John Snow Labs
name: legclf_nda_perpetuity
date: 2023-04-07
tags: [en, legal, licensed, classification, nda, perpetuity, tensorflow]
task: Text Classification
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: LegalClassifierDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Given a clause classified as `RETURN_OF_CONF_INFO` using the `legmulticlf_mnda_sections_paragraph_other` classifier, you can subclassify the sentences as `PERPETUITY` or `OTHER` from it using the `legclf_nda_perpetuity` model.

## Predicted Entities

`PERPETUITY`, `OTHER`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_nda_perpetuity_en_1.0.0_3.0_1680880224296.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_nda_perpetuity_en_1.0.0_3.0_1680880224296.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
    
sentence_embeddings = nlp.UniversalSentenceEncoder.pretrained()\
    .setInputCols("document")\
    .setOutputCol("sentence_embeddings")

classifier = legal.ClassifierDLModel.pretrained("legclf_nda_perpetuity", "en", "legal/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("category")

nlpPipeline = nlp.Pipeline(stages=[
      document_assembler, 
      sentence_embeddings,
      classifier
])

empty_data = spark.createDataFrame([[""]]).toDF("text")
                  
model = nlpPipeline.fit(empty_data)

text_list = ["""Notwithstanding the return or destruction of all Evaluation Material, you or your Representatives shall continue to be bound by your obligations of confidentiality and other obligations hereunder.""",
             """There are no intended third party beneficiaries to this Agreement."""]


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
|Model Name:|legclf_nda_perpetuity|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|en|
|Size:|22.5 MB|

## References

In-house annotations on the Non-disclosure Agreements

## Benchmarking

```bash
label         precision  recall  f1-score  support 
OTHER         0.87       1.00    0.93      13      
PERPETUITY    1.00       0.86    0.92      14      
accuracy      -          -       0.93      27      
macro-avg     0.93       0.93    0.93      27      
weighted-avg  0.94       0.93    0.93      27  
```
