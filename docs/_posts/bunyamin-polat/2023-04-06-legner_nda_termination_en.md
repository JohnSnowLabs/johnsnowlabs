---
layout: model
title: Legal NER for NDA (Termination Clause)
author: John Snow Labs
name: legner_nda_termination
date: 2023-04-06
tags: [en, licensed, legal, ner, nda, termination]
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

This is a NER model, aimed to be run **only** after detecting the `TERMINATION ` clause with a proper classifier (use legmulticlf_mnda_sections_paragraph_other for that purpose). It will extract the following entities: `TERM_DATE `, and `REF_TERM_DATE`.

## Predicted Entities

`TERM_DATE`, `REF_TERM_DATE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_nda_termination_en_1.0.0_3.0_1680816697135.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_nda_termination_en_1.0.0_3.0_1680816697135.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = legal.NerModel.pretrained("legner_nda_termination", "en", "legal/models")\
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

text = ["""Except as otherwise specified herein, the obligations of the parties set forth in this Agreement shall terminate and be of no further force and effect eighteen months from the date hereof."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+---------------+-------------+
|chunk          |ner_label    |
+---------------+-------------+
|eighteen months|TERM_DATE    |
|date hereof    |REF_TERM_DATE|
+---------------+-------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_nda_termination|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|16.2 MB|

## References

In-house annotations on the Non-disclosure Agreements

## Benchmarking

```bash
label            precision  recall  f1-score  support 
B-TERM_DATE      1.00       0.92    0.96      12      
I-TERM_DATE      0.97       1.00    0.98      28      
B-REF_TERM_DATE  0.91       0.91    0.91      11      
I-REF_TERM_DATE  1.00       0.90    0.95      10      
micro-avg        0.97       0.95    0.96      61      
macro-avg        0.97       0.93    0.95      61      
weighted-avg     0.97       0.95    0.96      61 
```