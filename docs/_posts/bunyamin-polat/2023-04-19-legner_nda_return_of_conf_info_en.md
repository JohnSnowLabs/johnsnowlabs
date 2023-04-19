---
layout: model
title: Legal NER for NDA (Return of Confidential Information Clauses)
author: John Snow Labs
name: legner_nda_return_of_conf_info
date: 2023-04-19
tags: [en, legal, licensed, ner, nda]
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

This is a NER model, aimed to be run **only** after detecting the `RETURN_OF_CONF_INFO` clause with a proper classifier (use `legmulticlf_mnda_sections_paragraph_other` model for that purpose). It will extract the following entities: `ARCHIVAL_PURPOSE`, and `LEGAL_PURPOSE`.

## Predicted Entities

`ARCHIVAL_PURPOSE`, `LEGAL_PURPOSE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_nda_return_of_conf_info_en_1.0.0_3.0_1681936414470.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_nda_return_of_conf_info_en_1.0.0_3.0_1681936414470.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = legal.NerModel.pretrained("legner_nda_return_of_conf_info", "en", "legal/models")\
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

text = ["""Notwithstanding the foregoing, the Recipient and its Representatives may retain copies of the Confidential Information to the extent that such retention is required to demonstrate compliance with applicable law or governmental rule or regulation, to the extent included in any board or executive documents relating to the proposed business relationship, and in its archives for backup purposes subject to the confidentiality provisions of this Agreement."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))


```

</div>

## Results

```bash
+--------------+----------------+
|chunk         |ner_label       |
+--------------+----------------+
|applicable law|LEGAL_PURPOSE   |
|governmental  |LEGAL_PURPOSE   |
|regulation    |LEGAL_PURPOSE   |
|archives      |ARCHIVAL_PURPOSE|
|backup        |ARCHIVAL_PURPOSE|
+--------------+----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_nda_return_of_conf_info|
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
label             precision  recall  f1-score  support 
ARCHIVAL_PURPOSE  0.94       1.00    0.97      16      
LEGAL_PURPOSE     0.78       0.85    0.81      33      
micro-avg         0.83       0.90    0.86      49      
macro-avg         0.86       0.92    0.89      49      
weighted-avg      0.83       0.90    0.86      49  
```