---
layout: model
title: Legal NER for NDA (Exceptions Clause)
author: John Snow Labs
name: legner_nda_exceptions
date: 2023-04-06
tags: [en, licensed, legal, ner, nda, exceptions]
task: Named Entity Recognition
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
annotator: LegalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a NER model, aimed to be run **only** after detecting the `EXCEPTIONS` clause with a proper classifier (use legmulticlf_mnda_sections_paragraph_other for that purpose). It will extract the following entities: `EXCLUDED_INFO `, and `EXCLUSION_GROUND`.

## Predicted Entities

`EXCLUDED_INFO`, `EXCLUSION_GROUND`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_nda_exceptions_en_1.0.0_3.0_1680796058978.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_nda_exceptions_en_1.0.0_3.0_1680796058978.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
        .setInputCol("text")\
        .setOutputCol("document")
        
sentence_detector = nlp.SentenceDetector()\
        .setInputCols(["document"])\
        .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
        .setInputCols(["sentence"])\
        .setOutputCol("token")

embeddings = nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en") \
        .setInputCols(["sentence", "token"]) \
        .setOutputCol("embeddings")\
        .setMaxSentenceLength(512)\
        .setCaseSensitive(True)

ner_model = legal.NerModel.pretrained("legner_nda_exceptions", "en", "legal/models")\
        .setInputCols(["sentence", "token", "embeddings"])\
        .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
        .setInputCols(["sentence", "token", "ner"])\
        .setOutputCol("ner_chunk")

nlpPipeline = nlp.Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        embeddings,
        ner_model,
        ner_converter])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

text = ["""( ii ) was within the Recipient’s or its Recipient Representatives possession prior to its being furnished to the Recipient or its Recipient Representatives by or on behalf of the Provider pursuant here to , provided that the source of such information was not bound by a confidentiality agreement with, or other contractual, legal or fiduciary obligation of confidentiality to, the Provider or any other party with respect to such information."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+----------+----------------+
|chunk     |ner_label       |
+----------+----------------+
|possession|EXCLUDED_INFO   |
|prior to  |EXCLUSION_GROUND|
+----------+----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_nda_exceptions|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|16.3 MB|

## References

In-house annotations on the Non-disclosure Agreements

## Benchmarking

```bash
label               precision  recall  f1-score  support 
B-EXCLUDED_INFO     0.84       0.91    0.87      34      
B-EXCLUSION_GROUND  0.85       0.91    0.88      32      
I-EXCLUSION_GROUND  0.91       0.76    0.83      51      
I-EXCLUDED_INFO     1.00       0.50    0.67      4       
micro-avg           0.87       0.83    0.85      121     
macro-avg           0.90       0.77    0.81      121     
weighted-avg        0.88       0.83    0.85      121     
```