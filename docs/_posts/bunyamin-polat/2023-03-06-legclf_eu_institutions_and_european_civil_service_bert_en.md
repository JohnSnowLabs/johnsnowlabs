---
layout: model
title: Legal Eu Institutions And European Civil Service Document Classifier (EURLEX)
author: John Snow Labs
name: legclf_eu_institutions_and_european_civil_service_bert
date: 2023-03-06
tags: [en, legal, classification, clauses, eu_institutions_and_european_civil_service, licensed, tensorflow]
task: Text Classification
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: LegalClassifierDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

European Union (EU) legislation is published in the EUR-Lex portal. All EU laws are annotated by the EU's Publications Office with multiple concepts from the EuroVoc thesaurus, a multilingual thesaurus maintained by the Publications Office.

Given a document, the legclf_eu_institutions_and_european_civil_service_bert model, it is a Bert Sentence Embeddings Document Classifier, classifies if the document belongs to the class Eu_Institutions_and_European_Civil_Service or not (Binary Classification) according to EuroVoc labels.

## Predicted Entities

`Eu_Institutions_and_European_Civil_Service`, `Other`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_eu_institutions_and_european_civil_service_bert_en_1.0.0_3.0_1678111712438.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_eu_institutions_and_european_civil_service_bert_en_1.0.0_3.0_1678111712438.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

embeddings = nlp.BertSentenceEmbeddings.pretrained("sent_bert_base_cased", "en")\
    .setInputCols("document")\
    .setOutputCol("sentence_embeddings")

doc_classifier = legal.ClassifierDLModel.pretrained("legclf_eu_institutions_and_european_civil_service_bert", "en", "legal/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("category")

nlpPipeline = nlp.Pipeline(stages=[
    document_assembler, 
    embeddings,
    doc_classifier])

df = spark.createDataFrame([["YOUR TEXT HERE"]]).toDF("text")

model = nlpPipeline.fit(df)

result = model.transform(df)

```

</div>

## Results

```bash

+-------+
|result|
+-------+
|[Eu_Institutions_and_European_Civil_Service]|
|[Other]|
|[Other]|
|[Eu_Institutions_and_European_Civil_Service]|

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legclf_eu_institutions_and_european_civil_service_bert|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|en|
|Size:|21.6 MB|

## References

Train dataset available [here](https://huggingface.co/datasets/lex_glue)

## Benchmarking

```bash

                                     label precision recall  f1-score  support
Eu_Institutions_and_European_Civil_Service      0.85   1.00      0.92       45
                                     Other      1.00   0.83      0.91       47
                                  accuracy         -      -      0.91       92
                                 macro-avg      0.92   0.91      0.91       92
                              weighted-avg      0.93   0.91      0.91       92
```