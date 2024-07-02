---
layout: model
title: Legal Clauses Multilabel Classifier
author: John Snow Labs
name: legmulticlf_edgar_le
date: 2024-07-02
tags: [clauses, edgar, ledgar, en, licensed, legal, tensorflow]
task: Text Classification
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MultiClassifierDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a Multilabel Document Classification model, which can be used to identify up to 15 classes in texts. The classes are the following:

- terminations
- assigns
- notices
- amendments
- waivers
- survival
- successors
- governing laws
- severability
- expenses
- assignments
- warranties
- representations
- entire agreements
- counterparts

## Predicted Entities

`terminations`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legmulticlf_edgar_le_en_1.0.0_3.0_1719935035558.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legmulticlf_edgar_le_en_1.0.0_3.0_1719935035558.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

embeddings = nlp.E5Embeddings.pretrained("finembedding_e5_large", "en", "finance/models")\
  .setInputCols(["document"])\
  .setOutputCol("sentence_embeddings")


multiClassifier = nlp.MultiClassifierDLModel.pretrained("legmulticlf_edgar_le", "en", "legal/models") \
  .setInputCols(["document", "sentence_embeddings"]) \
  .setOutputCol("class")

ledgar_pipeline = nlp.Pipeline(
    stages=[document, 
            embeddings,
            multiClassifier])


light_pipeline = LightPipeline(ledgar_pipeline.fit(spark.createDataFrame([['']]).toDF("text")))

result = light_pipeline.annotate("""(a) No failure or delay by the Administrative Agent or any Lender in exercising any right or power hereunder shall operate as a waiver thereof, nor shall any single or partial exercise of any such right or power, or any abandonment or discontinuance of steps to enforce such a right or power, preclude any other or further exercise thereof or the exercise of any other right or power. The rights and remedies of the Administrative Agent and the Lenders hereunder are cumulative and are not exclusive of any rights or remedies that they would otherwise have. No waiver of any provision of this Agreement or consent to any departure by the Borrower therefrom shall in any event be effective unless the same shall be permitted by paragraph (b) of this Section, and then such waiver or consent shall be effective only in the specific instance and for the purpose for which given. Without limiting the generality of the foregoing, the making of a Loan shall not be construed as a waiver of any Default, regardless of whether the Administrative Agent or any Lender may have had notice or knowledge of such Default at the time.""")

result["class"]
```

</div>

## Results

```bash
['waivers', 'amendments']
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legmulticlf_edgar_le|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|en|
|Size:|15.0 MB|

## References

Ledgar dataset, available at https://metatext.io/datasets/ledgar, with in-house data augmentation

## Benchmarking

```bash
Classification report: 
               precision    recall  f1-score   support

           0       0.89      0.89      0.89      1066
           1       0.83      0.65      0.73       333
           2       0.80      0.81      0.80       537
           3       0.99      0.99      0.99       918
           4       0.98      0.98      0.98      1049
           5       0.99      0.97      0.98       339
           6       1.00      0.99      0.99      1274
           7       0.98      0.98      0.98       926
           8       0.91      0.92      0.91       437
           9       0.98      0.97      0.98       922
          10       0.89      0.88      0.88       674
          11       0.95      0.96      0.95       566
          12       0.92      0.79      0.85       354
          13       0.89      0.87      0.88       725
          14       0.88      0.78      0.83       365

   micro avg       0.94      0.92      0.93     10485
   macro avg       0.93      0.89      0.91     10485
weighted avg       0.94      0.92      0.93     10485
 samples avg       0.93      0.94      0.93     10485

F1 micro averaging: 0.9300510646497736
ROC:  0.9578155732480869

```