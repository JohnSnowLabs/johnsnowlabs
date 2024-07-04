---
layout: model
title: Multilabel Classification of NDA Clauses (paragraph, medium)
author: John Snow Labs
name: legmulticlf_mnda_sections_paragraph_other_le
date: 2024-07-04
tags: [en, legal, licensed, mnda, tensorflow]
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

This models is a version of `legmulticlf_mnda_sections_other` (sentence, medium) but expecting a bigger-than-sentence context, ideally between 2 and 4-5 sentences, or a small paragraph, to provide with more context.

It should be run on sentences of the NDA clauses, and will retrieve a series of 1..N labels for each of them. The possible clause types detected my this model in NDA / MNDA aggrements are:

1. Parties to the Agreement - Names of the Parties Clause  
2. Identification of What Information Is Confidential - Definition of Confidential Information Clause
3. Use of Confidential Information: Permitted Use Clause and Obligations of the Recipient
4. Time Frame of the Agreement - Termination Clause  
5. Return of Confidential Information Clause 
6. Remedies for Breaches of Agreement - Remedies Clause 
7. Non-Solicitation Clause
8. Dispute Resolution Clause  
9. Exceptions Clause  
10. Non-competition clause
11. Other: Nothing of the above (synonym to `[]`)-

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legmulticlf_mnda_sections_paragraph_other_le_en_1.0.0_3.0_1720071478051.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legmulticlf_mnda_sections_paragraph_other_le_en_1.0.0_3.0_1720071478051.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")\
  .setCleanupMode("shrink")

embeddings = (
    nlp.E5Embeddings.pretrained(
        "legembedding_e5_base", "en", "legal/models")
    .setInputCols(["document"])
    .setOutputCol("sentence_embeddings")
)

paragraph_classifier = (
    nlp.MultiClassifierDLModel.load("legmulticlf_mnda_sections_paragraph_other_le", "en", "legal/models")
    .setInputCols(["sentence_embeddings"])
    .setOutputCol("class")
)


sentence_pipeline = nlp.Pipeline(
    stages=[document, 
            embeddings,
            paragraph_classifier])




df = spark.createDataFrame([["'Destruction of Confidential Information. \xa0 Promptly (and in any event within five days) after the earlier of"]]).toDF("text")

model = sentence_pipeline.fit(df)

result = model.transform(df)

result.select("text", "class.result").show(truncate=False)
```

</div>

## Results

```bash
+-------------------------------------------------------------------------------------------------------------+---------------------+
|text                                                                                                         |result               |
+-------------------------------------------------------------------------------------------------------------+---------------------+
|'Destruction of Confidential Information.   Promptly (and in any event within five days) after the earlier of|[RETURN_OF_CONF_INFO]|
+-------------------------------------------------------------------------------------------------------------+---------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legmulticlf_mnda_sections_paragraph_other_le|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|en|
|Size:|14.0 MB|

## References

In-house MNDA

## Benchmarking

```bash
|               | precision | recall | f1-score | support |
|---------------|-----------|--------|----------|---------|
| APPLIC_LAW    | 0.91      | 0.91   | 0.91     | 58      |
| ASSIGNMENT    | 0.96      | 0.87   | 0.91     | 52      |
| DEF_OF_CONF_INFO | 0.91   | 0.83   | 0.87     | 89      |
| DISPUTE_RESOL | 0.90      | 0.72   | 0.80     | 64      |
| EXCEPTIONS    | 0.97      | 0.92   | 0.95     | 144     |
| NAMES_OF_PARTIES | 0.95  | 0.85   | 0.89     | 84      |
| NON_COMP      | 0.80      | 0.80   | 0.80     | 25      |
| NON_SOLIC     | 0.92      | 0.80   | 0.86     | 60      |
| PREAMBLE      | 0.79      | 0.82   | 0.80     | 186     |
| REMEDIES      | 0.91      | 0.79   | 0.85     | 76      |
| REQ_DISCL     | 0.88      | 0.86   | 0.87     | 73      |
| RETURN_OF_CONF_INFO | 0.91 | 0.89   | 0.90     | 83      |
| TERMINATION   | 0.98      | 0.86   | 0.92     | 96      |
| USE_OF_CONF_INFO | 0.85   | 0.85   | 0.85     | 47      |
| OTHER         | 0.86      | 0.77   | 0.81     | 87      |
| **micro avg** | **0.90**  | **0.84** | **0.87** | **1224**|
| **macro avg** | **0.90**  | **0.84** | **0.87** | **1224**|
| **weighted avg** | **0.90** | **0.84** | **0.87** | **1224**|
| **samples avg** | **0.85** | **0.85** | **0.85** | **1224**|

```