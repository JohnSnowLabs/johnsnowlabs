---
layout: model
title: Legal NER for NDA (Confidential Information-Permissions)
author: John Snow Labs
name: legner_nda_confidential_information_permissions
date: 2023-04-06
tags: [en, licensed, legal, ner, nda, permission]
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

This is a NER model, aimed to be run **only** after detecting the `USE_OF_CONF_INFO ` clause with a proper classifier (use legmulticlf_mnda_sections_paragraph_other for that purpose). It will extract the following entities: `PERMISSION`, `PERMISSION_SUBJECT `, `PERMISSION_OBJECT `, and `PERMISSION_IND_OBJECT `.

## Predicted Entities

`PERMISSION`, `PERMISSION_SUBJECT`, `PERMISSION_OBJECT`, `PERMISSION_IND_OBJECT`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_nda_confidential_information_permissions_en_1.0.0_3.0_1680814300223.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_nda_confidential_information_permissions_en_1.0.0_3.0_1680814300223.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = legal.NerModel.pretrained("legner_nda_confidential_information_permissions", "en", "legal/models")\
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

text = ["""The interested party may disclose the information to its financing sources and potential financing sources provided that such financing sources are bound by the terms of this non-disclosure agreement and agree to keep the information confidential."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+---------------------------+---------------------+
|chunk                      |ner_label            |
+---------------------------+---------------------+
|interested party           |PERMISSION_SUBJECT   |
|disclose                   |PERMISSION           |
|information                |PERMISSION_OBJECT    |
|financing sources          |PERMISSION_IND_OBJECT|
|potential financing sources|PERMISSION_IND_OBJECT|
+---------------------------+---------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_nda_confidential_information_permissions|
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
label                  precision  recall  f1-score  support 
PERMISSION             1.00       1.00    1.00      9       
PERMISSION_IND_OBJECT  1.00       0.67    0.80      9       
PERMISSION_OBJECT      0.91       1.00    0.95      10      
PERMISSION_SUBJECT     0.90       1.00    0.95      9       
micro-avg              0.94       0.92    0.93      37      
macro-avg              0.95       0.92    0.92      37      
weighted-avg           0.95       0.92    0.93      37 
```