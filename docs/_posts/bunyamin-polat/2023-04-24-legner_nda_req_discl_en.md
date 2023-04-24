---
layout: model
title: Legal NER for NDA (Required Disclosure Clauses)
author: John Snow Labs
name: legner_nda_req_discl
date: 2023-04-24
tags: [en, legal, licensed, ner, nda, disclosure]
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

This is a NER model, aimed to be run **only** after detecting the `REQ_DISCL` clause with a proper classifier (use `legmulticlf_mnda_sections_paragraph_other` model for that purpose). It will extract the following entities: `DISCLOSURE_BASIS`, `REQ_DISCLOSURE_CONFID`, `REQ_DISCLOSURE_COOPERATION`, `REQ_DISCLOSURE_LEGAL`, `REQ_DISCLOSURE_NOTICE`, `REQ_DISCLOSURE_PARTY`, `REQ_DISCLOSURE_REMEDY`,  and `REQ_OBLIGATION_ACTION`.

## Predicted Entities

`DISCLOSURE_BASIS`, `REQ_DISCLOSURE_CONFID`, `REQ_DISCLOSURE_COOPERATION`, `REQ_DISCLOSURE_LEGAL`, `REQ_DISCLOSURE_NOTICE`, `REQ_DISCLOSURE_PARTY`, `REQ_DISCLOSURE_REMEDY`, `REQ_OBLIGATION_ACTION`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_nda_req_discl_en_1.0.0_3.0_1682327765264.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_nda_req_discl_en_1.0.0_3.0_1682327765264.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = legal.NerModel.pretrained("legner_nda_req_discl", "en", "legal/models")\
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

text = ["""If the Discloser waives the Recipient’s compliance with the agreement or fails to obtain a protective order or other appropriate remedies, the Recipient will furnish only that portion of the Confidential Information that is legally required to be disclosed and will use its best efforts to obtain confidential treatment for such Confidential Information."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+----------------------+--------------------------+
|chunk                 |ner_label                 |
+----------------------+--------------------------+
|Discloser             |REQ_DISCLOSURE_PARTY      |
|obtain                |REQ_OBLIGATION_ACTION     |
|protective order      |REQ_DISCLOSURE_REMEDY     |
|appropriate remedies  |REQ_DISCLOSURE_REMEDY     |
|furnish               |REQ_OBLIGATION_ACTION     |
|legally required      |REQ_DISCLOSURE_LEGAL      |
|best efforts          |REQ_DISCLOSURE_COOPERATION|
|obtain                |REQ_OBLIGATION_ACTION     |
|confidential treatment|REQ_DISCLOSURE_CONFID     |
+----------------------+--------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_nda_req_discl|
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
label                       precision  recall  f1-score  support 
DISCLOSURE_BASIS            0.77       0.70    0.73      57      
REQ_DISCLOSURE_CONFID       0.96       0.93    0.95      29      
REQ_DISCLOSURE_COOPERATION  1.00       0.94    0.97      17      
REQ_DISCLOSURE_LEGAL        0.93       0.77    0.84      35      
REQ_DISCLOSURE_NOTICE       0.89       0.89    0.89      19      
REQ_DISCLOSURE_PARTY        1.00       0.89    0.94      38      
REQ_DISCLOSURE_REMEDY       1.00       1.00    1.00      52      
REQ_OBLIGATION_ACTION       0.95       0.86    0.90      121     
macro-avg                   0.94       0.86    0.90      368     
macro-avg                   0.94       0.87    0.90      368     
weighted-avg                0.93       0.86    0.90      368    
```
