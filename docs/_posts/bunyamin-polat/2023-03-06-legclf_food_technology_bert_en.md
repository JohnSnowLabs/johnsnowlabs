---
layout: model
title: Legal Food Technology Document Classifier (EURLEX)
author: John Snow Labs
name: legclf_food_technology_bert
date: 2023-03-06
tags: [en, legal, classification, clauses, food_technology, licensed, tensorflow]
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

Given a document, the legclf_food_technology_bert model, it is a Bert Sentence Embeddings Document Classifier, classifies if the document belongs to the class Food_Technology or not (Binary Classification) according to EuroVoc labels.

## Predicted Entities

`Food_Technology`, `Other`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_food_technology_bert_en_1.0.0_3.0_1678111847548.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_food_technology_bert_en_1.0.0_3.0_1678111847548.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

doc_classifier = legal.ClassifierDLModel.pretrained("legclf_food_technology_bert", "en", "legal/models")\
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
|[Food_Technology]|
|[Other]|
|[Other]|
|[Food_Technology]|

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legclf_food_technology_bert|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|en|
|Size:|21.8 MB|

## References

Train dataset available [here](https://huggingface.co/datasets/lex_glue)

## Benchmarking

```bash

          label precision recall  f1-score  support
Food_Technology      0.87   0.86      0.86      221
          Other      0.83   0.84      0.84      181
       accuracy         -      -      0.85      402
      macro-avg      0.85   0.85      0.85      402
   weighted-avg      0.85   0.85      0.85      402
```