---
layout: model
title: Understanding Restriction level of NDA Assignment Clauses
author: John Snow Labs
name: legclf_nda_assigments
date: 2023-04-07
tags: [en, licensed, legal, classification, nda, assigments, tensorflow]
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

Given a clause classified as `ASSIGNMENT ` using the `legmulticlf_mnda_sections_paragraph_other` classifier, you can subclassify the sentences as `PERMISSIVE_ASSIGNMENT`, `RESTRICTIVE_ASSIGNMENT` or `OTHER` from it using the `legclf_nda_assigments` model.

## Predicted Entities

`PERMISSIVE_ASSIGNMENT`, `RESTRICTIVE_ASSIGNMENT`, `OTHER`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_nda_assigments_en_1.0.0_3.0_1680898751373.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_nda_assigments_en_1.0.0_3.0_1680898751373.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

classifier = legal.ClassifierDLModel.pretrained("legclf_nda_assigments", "en", "legal/models")\
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
                   """All notices and other communications provided for in this Agreement and the other Loan Documents shall be in writing and may (subject to paragraph (b) below) be telecopied (faxed), mailed by certified mail return receipt requested, or delivered by hand or overnight courier service to the intended recipient at the addresses specified below or at such other address as shall be designated by any party listed below in a notice to the other parties listed below given in accordance with this Section.""",
                   """This Agreement is a personal contract for XCorp, and the rights and interests of XCorp hereunder may not be sold, transferred, assigned, pledged or hypothecated except as otherwise expressly permitted by the Company"""]

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
|Model Name:|legclf_nda_assigments|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|en|
|Size:|22.4 MB|

## References

In-house annotations on the Non-disclosure Agreements

## Benchmarking

```bash
label                   precision  recall  f1-score  support 
OTHER                   0.88       1.00    0.94      29      
PERMISSIVE_ASSIGNMENT   1.00       0.85    0.92      13      
RESTRICTIVE_ASSIGNMENT  0.95       0.86    0.90      22      
accuracy                -          -       0.92      64      
macro-avg               0.94       0.90    0.92      64      
weighted-avg            0.93       0.92    0.92      64   
```
