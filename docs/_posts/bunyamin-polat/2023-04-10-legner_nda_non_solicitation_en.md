---
layout: model
title: Legal NER for NDA (Non-solicitation Clauses)
author: John Snow Labs
name: legner_nda_non_solicitation
date: 2023-04-10
tags: [en, legal, licensed, ner, nda, non_solicitation]
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

This is a NER model, aimed to be run **only** after detecting the `NON_SOLIC` clause with a proper classifier (use `legmulticlf_mnda_sections_paragraph_other` model for that purpose). It will extract the following entities: `NON_SOLIC_ACTION`, `NON_SOLIC_OBJECT`, `NON_SOLIC_IND_OBJECT`, and `NON_SOLIC_SUBJECT`.

## Predicted Entities

`NON_SOLIC_ACTION`, `NON_SOLIC_OBJECT`, `NON_SOLIC_IND_OBJECT`, `NON_SOLIC_SUBJECT`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_nda_non_solicitation_en_1.0.0_3.0_1681096605002.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_nda_non_solicitation_en_1.0.0_3.0_1681096605002.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = legal.NerModel.pretrained("legner_nda_non_solicitation", "en", "legal/models")\
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

text = ["""During the 12-month period commencing on the date of this Agreement, each Party agrees that it will not permit any of its officers, directors, or employees or any direct or indirect subsidiary or any employment agency retained by a Party or any such subsidiary, in each case who is or becomes aware of the negotiation of a possible Transaction between the Parties, to solicit for employment with such Party or with any of its direct or indirect subsidiaries any employee of the other Party or any of its direct or indirect subsidiaries;"""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+----------+--------------------+
|chunk     |ner_label           |
+----------+--------------------+
|Party     |NON_SOLIC_SUBJECT   |
|officers  |NON_SOLIC_IND_OBJECT|
|directors |NON_SOLIC_IND_OBJECT|
|employees |NON_SOLIC_IND_OBJECT|
|agency    |NON_SOLIC_SUBJECT   |
|solicit   |NON_SOLIC_ACTION    |
|employment|NON_SOLIC_OBJECT    |
|employee  |NON_SOLIC_IND_OBJECT|
+----------+--------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_nda_non_solicitation|
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
label                 precision  recall  f1-score  support 
NON_SOLIC_ACTION      1.00       0.95    0.98      22      
NON_SOLIC_IND_OBJECT  0.67       0.90    0.76      29      
NON_SOLIC_OBJECT      0.81       0.94    0.87      18      
NON_SOLIC_SUBJECT     0.86       0.86    0.86      21      
micro-avg             0.80       0.91    0.85      90      
macro-avg             0.83       0.91    0.87      90      
weighted-avg          0.82       0.91    0.86      90   
```