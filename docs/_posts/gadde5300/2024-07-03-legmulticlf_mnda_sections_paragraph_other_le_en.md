---
layout: model
title: Multilabel Classification of NDA Clauses (paragraph, medium)
author: John Snow Labs
name: legmulticlf_mnda_sections_paragraph_other_le
date: 2024-07-03
tags: [en, legal, licensed, tensorflow]
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

`APPLIC_LAW`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legmulticlf_mnda_sections_paragraph_other_le_en_1.0.0_3.0_1720001077643.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legmulticlf_mnda_sections_paragraph_other_le_en_1.0.0_3.0_1720001077643.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = (
    nlp.DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

sentence_detector = (
    nlp.SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")
    .setExplodeSentences(True)
    .setCustomBounds(['\n'])
)


embeddings = (
    nlp.E5Embeddings.pretrained(
        "finembedding_e5_large", "en", "finance/models"
    )
    .setInputCols(["document"])
    .setOutputCol("sentence_embeddings")
)

paragraph_classifier = (
    nlp.MultiClassifierDLModel.pretrained("legmulticlf_mnda_sections_paragraph_other_le", "en", "legal/models")
    .setInputCols(["sentence_embeddings"])
    .setOutputCol("class")
)


sentence_pipeline = nlp.Pipeline(stages=[document_assembler, sentence_detector, embeddings, paragraph_classifier])


df = spark.createDataFrame([["There is therefore no doubt – and the Government do not contest – that the measures concerned in the present case ( the children 's continued placement in foster homes and the restrictions imposed on contact between the applicants and their children ) amounts to an “ interference ” with the applicants ' rights to respect for their family life ."]]).toDF("text")

model = sentence_pipeline.fit(df)

result = model.transform(df)

result.select("text", "class.result").show()
```

</div>

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