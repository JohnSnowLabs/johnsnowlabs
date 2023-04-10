---
layout: model
title: Legal NER for NDA (Definition of Confidential Information Clauses)
author: John Snow Labs
name: legner_nda_def_conf_info
date: 2023-04-10
tags: [en, licensed, legal, ner, nda, definition]
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

This is a NER model, aimed to be run **only** after detecting the `DEF_OF_CONF_INFO` clause with a proper classifier (use `legmulticlf_mnda_sections_paragraph_other` model for that purpose). It will extract the following entities: `CONF_INFO_FORM`, and `CONF_INFO_TYPE`.

## Predicted Entities

`CONF_INFO_FORM`, `CONF_INFO_TYPE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_nda_def_conf_info_en_1.0.0_3.0_1681152951608.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_nda_def_conf_info_en_1.0.0_3.0_1681152951608.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = legal.NerModel.pretrained("legner_nda_def_conf_info", "en", "legal/models")\
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
        ner_converter
])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

text = [""""Confidential Information" shall mean all written or oral information of a proprietary, intellectual, or similar nature relating to GT Solar's business, projects, operations, activities, or affairs whether of a technical or financial nature or otherwise (including, without limitation, reports, financial information, business plans and proposals, ideas, concepts, trade secrets, know-how, processes, and other technical or business information, whether concerning GT Solar' businesses or otherwise) which has not been publicly disclosed and which the Recipient acquires directly or indirectly from GT Solar, its officers, employees, affiliates, agents or representatives."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))


```

</div>

## Results

```bash
+-------------+--------------+
|chunk        |ner_label     |
+-------------+--------------+
|written      |CONF_INFO_FORM|
|oral         |CONF_INFO_FORM|
|reports      |CONF_INFO_TYPE|
|information  |CONF_INFO_TYPE|
|plans        |CONF_INFO_TYPE|
|proposals    |CONF_INFO_TYPE|
|ideas        |CONF_INFO_TYPE|
|concepts     |CONF_INFO_TYPE|
|trade secrets|CONF_INFO_TYPE|
|know-how     |CONF_INFO_TYPE|
|processes    |CONF_INFO_TYPE|
|information  |CONF_INFO_TYPE|
+-------------+--------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_nda_def_conf_info|
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
label           precision  recall  f1-score  support 
CONF_INFO_FORM  1.00       0.95    0.97      20      
CONF_INFO_TYPE  0.87       0.93    0.90      163     
micro-avg       0.88       0.93    0.90      183     
macro-avg       0.93       0.94    0.94      183     
weighted-avg    0.88       0.93    0.90      183
```