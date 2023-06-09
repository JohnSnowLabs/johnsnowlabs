---
layout: model
title: Understanding Non-compete Items in Non-Compete Clauses
author: John Snow Labs
name: legclf_nda_non_compete_items
date: 2023-04-07
tags: [en, licensed, legal, classification, nda, non_compete, tensorflow]
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

Given a clause classified as `NON_COMP` using the `legmulticlf_mnda_sections_paragraph_other` classifier, you can subclassify the sentences as `NON_COMPETE_ITEMS`, or `OTHER` from it using the `legclf_nda_non_compete_items` model.

## Predicted Entities

`NON_COMPETE_ITEMS`, `OTHER`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_nda_non_compete_items_en_1.0.0_3.0_1680900015288.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_nda_non_compete_items_en_1.0.0_3.0_1680900015288.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

classifier = legal.ClassifierDLModel.pretrained("legclf_nda_non_compete_items", "en", "legal/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("category")

nlpPipeline = nlp.Pipeline(stages=[
      document_assembler, 
      sentence_embeddings,
      classifier
])

empty_data = spark.createDataFrame([[""]]).toDF("text")
                  
model = nlpPipeline.fit(empty_data)

text_list = ["""This Agreement will be binding upon and inure to the benefit of each Party and its respective heirs, successors and assigns""",
                   """Activity that is in direct competition with the Company's business, including but not limited to developing, marketing, or selling products or services that are similar to those of the Company."""]

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
|Model Name:|legclf_nda_non_compete_items|
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
label              precision  recall  f1-score  support 
NON_COMPETE_ITEMS  0.95       1.00    0.97      18      
OTHER              1.00       0.95    0.97      20      
accuracy           -          -       0.97      38      
macro-avg          0.97       0.97    0.97      38      
weighted-avg       0.98       0.97    0.97      38   
```