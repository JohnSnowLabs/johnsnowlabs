---
layout: model
title: Legal NER for NDA (Confidential Information-Restricted)
author: John Snow Labs
name: legner_nda_confidential_information_restricted
date: 2023-04-11
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

This is a NER model, aimed to be run **only** after detecting the `USE_OF_CONF_INFO ` clause with a proper classifier (use legmulticlf_mnda_sections_paragraph_other for that purpose). It will extract the following entities: `RESTRICTED_ACTION`, `RESTRICTED_SUBJECT`, `RESTRICTED_OBJECT`, and `RESTRICTED_IND_OBJECT`.

## Predicted Entities

`RESTRICTED_ACTION`, `RESTRICTED_SUBJECT`, `RESTRICTED_OBJECT`, `RESTRICTED_IND_OBJECT`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_nda_confidential_information_restricted_en_1.0.0_3.0_1681210372591.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_nda_confidential_information_restricted_en_1.0.0_3.0_1681210372591.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = legal.NerModel.pretrained("legner_nda_confidential_information_restricted", "en", "legal/models")\
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

text = ["""The recipient may use the proprietary information solely for the purpose of performing its obligations under a separate agreement with the disclosing party, and may not disclose such information to any third party without the prior written consent of the disclosing party."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+-----------+---------------------+
|chunk      |ner_label            |
+-----------+---------------------+
|recipient  |RESTRICTED_SUBJECT   |
|disclose   |RESTRICTED_ACTION    |
|information|RESTRICTED_OBJECT    |
|third party|RESTRICTED_IND_OBJECT|
+-----------+---------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_nda_confidential_information_restricted|
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
RESTRICTED_ACTION      0.92       0.94    0.93      36      
RESTRICTED_IND_OBJECT  1.00       0.93    0.97      15      
RESTRICTED_OBJECT      0.74       1.00    0.85      26      
RESTRICTED_SUBJECT     0.72       0.90    0.80      29      
micro-avg              0.82       0.94    0.88      106     
macro-avg              0.85       0.94    0.89      106     
weighted-avg           0.83       0.94    0.88      106 
```
