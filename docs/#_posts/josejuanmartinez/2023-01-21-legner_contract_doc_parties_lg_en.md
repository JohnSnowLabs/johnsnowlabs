---
layout: model
title: Legal NER (Parties, Dates, Alias, Former names, Document Type - lg)
author: John Snow Labs
name: legner_contract_doc_parties_lg
date: 2023-01-21
tags: [document, contract, agreement, type, parties, aliases, former, names, effective, dates, en, licensed]
task: Named Entity Recognition
language: en
nav_key: models
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

MPORTANT: Don't run this model on the whole legal agreement. Instead:
- Split by paragraphs. You can use [notebook 1](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/tutorials/Certification_Trainings_JSL) in Finance or Legal as inspiration;
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

`PARTY`, `EFFDATE`, `DOC`, `ALIAS`, `ORG`, `FORMER_NAME`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/finance/LEGALNER_PARTIES/){:.button.button-orange}
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_contract_doc_parties_lg_en_1.0.0_3.0_1674321394808.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_contract_doc_parties_lg_en_1.0.0_3.0_1674321394808.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base", "en") \
        .setInputCols("sentence", "token") \
        .setOutputCol("embeddings")\
        .setMaxSentenceLength(512)\
        .setCaseSensitive(True)

ner_model = legal.NerModel.pretrained('legner_contract_doc_parties_lg', 'en', 'legal/models')\
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
|chunk                              |ner_label  |
+-----------------------------------+-----------+
|INTELLECTUAL PROPERTY AGREEMENT    |DOC        |
|December 31, 2018                  |EFFDATE    |
|Armstrong Flooring, Inc            |PARTY      |
|Seller                             |ALIAS      |
|AFI Licensing LLC                  |PARTY      |
|Licensing                          |ALIAS      |
|Seller                             |PARTY      |
|Arizona                            |ALIAS      |
|AHF Holding, Inc.                  |ORG        |
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
|Model Name:|legner_contract_doc_parties_lg|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|16.3 MB|

## References

Manual annotations on CUAD dataset

## Benchmarking

```bash
label          precision  recall  f1-score  support 
B-ALIAS        0.95       0.95    0.95      193     
B-DOC          0.87       0.85    0.86      118     
I-DOC          0.92       0.83    0.87      245     
B-PARTY        0.83       0.79    0.81      246     
I-PARTY        0.90       0.88    0.89      630     
B-ORG          0.91       0.84    0.87      207     
I-ORG          0.93       0.87    0.90      355     
I-ALIAS        0.77       0.83    0.80      29      
B-EFFDATE      0.91       0.91    0.91      81      
I-EFFDATE      0.95       0.97    0.96      261     
B-FORMER_NAME  0.97       1.00    0.99      39      
I-FORMER_NAME  0.99       1.00    0.99      93      
micro-avg      0.91       0.88    0.90      2497    
macro-avg      0.91       0.89    0.90      2497    
weighted-avg   0.91       0.88    0.90      2497    
```
