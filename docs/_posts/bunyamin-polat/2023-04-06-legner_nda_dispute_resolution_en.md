---
layout: model
title: Legal NER for NDA (Dispute Resolution Clause)
author: John Snow Labs
name: legner_nda_dispute_resolution
date: 2023-04-06
tags: [en, licensed, legal, ner, nda]
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

This is a NER model, aimed to be run **only** after detecting the `DISPUTE_RESOL ` clause with a proper classifier (use legmulticlf_mnda_sections_paragraph_other for that purpose). It will extract the following entities: `COURT_NAME`, `LAW_LOCATION `, and `RESOLUT_MEANS `.

## Predicted Entities

`COURT_NAME`, `LAW_LOCATION`, `RESOLUT_MEANS`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_nda_dispute_resolution_en_1.0.0_3.0_1680821390209.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_nda_dispute_resolution_en_1.0.0_3.0_1680821390209.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = legal.NerModel.pretrained("legner_nda_dispute_resolution", "en", "legal/models")\
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

text = ["""In case no settlement can be reached through consultation within thirty ( 30 ) days after such dispute is raised, each party can submit such matter to China International Economic and Trade Arbitration Commission ( the "CIETAC") in accordance with its rules."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+-------------------------------------------------------+-------------+
|chunk                                                  |ner_label    |
+-------------------------------------------------------+-------------+
|consultation                                           |RESOLUT_MEANS|
|China                                                  |LAW_LOCATION |
|International Economic and Trade Arbitration Commission|COURT_NAME   |
+-------------------------------------------------------+-------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_nda_dispute_resolution|
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
label          precision  recall  f1-score  support 
COURT_NAME     0.86       0.89    0.88      75      
LAW_LOCATION   0.79       0.85    0.82      79      
RESOLUT_MEANS  0.88       0.88    0.88      58      
micro-avg      0.84       0.87    0.85      212     
macro-avg      0.84       0.87    0.86      212     
weighted-avg   0.84       0.87    0.85      212 
```