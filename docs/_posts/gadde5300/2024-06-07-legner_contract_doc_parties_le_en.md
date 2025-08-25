---
layout: model
title: Legal NER (Parties, Dates, Alias, Former names, Document Type)
author: John Snow Labs
name: legner_contract_doc_parties_le
date: 2024-06-07
tags: [document, agreement, contract, type, parties, aliases, former, names, effective, dates, licensed, en]
task: Named Entity Recognition
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
recommended: true
annotator: LegalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

IMPORTANT: Don't run this model on the whole legal agreement. Instead:
- Split by paragraphs. You can use [notebook 1](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/tutorials/Certification_Trainings) in Finance or Legal as inspiration;
- Use the `legclf_introduction_clause` Text Classifier to select only these paragraphs; 

This is a Legal NER Model, aimed to process the first page of the agreements when information can be found about:
- Parties of the contract/agreement;
- Their former names;
- Aliases of those parties, or how those parties will be called further on in the document;
- Document Type;
- Effective Date of the agreement;
- Other organizations;

This model can be used all along with its Relation Extraction model to retrieve the relations between these entities, called `legre_contract_doc_parties`

## Predicted Entities

`EFFDATE`, `PARTY`, `DOC`, `FORMER_NAME`, `ALIAS`, `ORG`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_contract_doc_parties_le_en_1.0.0_3.0_1717749001756.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_contract_doc_parties_le_en_1.0.0_3.0_1717749001756.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = nlp.DocumentAssembler()\
        .setInputCol("text")\
        .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
        .setInputCols(["document"])\
        .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
        .setInputCols(["sentence"])\
        .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("legal_word_embeddings", "en", "legal/models")\
            .setInputCols(["sentence","token"])\
            .setOutputCol("embeddings")

ner_model = legal.NerModel.pretrained("legner_contract_doc_parties_le", "en", "legal/models")\
        .setInputCols(["sentence", "token", "embeddings"])\
        .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
        .setInputCols(["sentence","token","ner"])\
        .setOutputCol("ner_chunk")

nlpPipeline = nlp.Pipeline(stages=[
        documentAssembler,
        sentenceDetector,
        tokenizer,
        embeddings,
        ner_model,
        ner_converter])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

text = ["""
INTELLECTUAL PROPERTY AGREEMENT

This INTELLECTUAL PROPERTY AGREEMENT (this "Agreement"), dated as of December 31, 2018 (the "Effective Date") is entered into by and between Armstrong Flooring, Inc., a Delaware corporation ("Seller") and AFI Licensing LLC, a Delaware limited liability company ("Licensing" and together with Seller, "Arizona") and AHF Holding, Inc. (formerly known as Tarzan HoldCo, Inc.), a Delaware corporation ("Buyer") and Armstrong Hardwood Flooring Company, a Tennessee corporation (the "Company" and together with Buyer the "Buyer Entities") (each of Arizona on the one hand and the Buyer Entities on the other hand, a "Party" and collectively, the "Parties").
"""]

res = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+-----------------------------------+-----------+
|chunk                              |label      |
+-----------------------------------+-----------+
|INTELLECTUAL PROPERTY AGREEMENT    |DOC        |
|INTELLECTUAL PROPERTY AGREEMENT    |DOC        |
|December 31, 2018                  |EFFDATE    |
|Armstrong Flooring, Inc            |PARTY      |
|Seller                             |ALIAS      |
|AFI Licensing LLC                  |PARTY      |
|Licensing                          |ALIAS      |
|Seller                             |PARTY      |
|Arizona                            |ALIAS      |
|AHF Holding, Inc                   |PARTY      |
|Tarzan HoldCo, Inc                 |FORMER_NAME|
|Buyer                              |ALIAS      |
|Armstrong Hardwood Flooring Company|PARTY      |
|Company                            |ALIAS      |
|Buyer                              |PARTY      |
|Buyer Entities                     |ALIAS      |
|Arizona                            |PARTY      |
|Buyer Entities                     |PARTY      |
|Party                              |ALIAS      |
|Parties                            |ALIAS      |
+-----------------------------------+-----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_contract_doc_parties_le|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.7 MB|

## References

Manual annotations on CUAD dataset

## Benchmarking

```bash
              precision    recall  f1-score   support
ALIAS             0.86      0.94      0.90       118
DOC               0.82      0.81      0.82        79
EFFDATE           0.87      0.93      0.90        56
FORMER_NAME       0.80      0.80      0.80         5
ORG       	  0.76      0.75      0.76       122
PARTY             0.84      0.81      0.82       209
micro-avg         0.83      0.83      0.83       589
macro-avg         0.83      0.84      0.83       589
weighted-avg      0.83      0.83      0.83       589
```