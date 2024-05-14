---
layout: model
title: Brazilian Portuguese NER for Laws (Bert, Base)
author: John Snow Labs
name: legner_pt_bert_base
date: 2024-05-14
tags: [pt, legal, licensed, ner, laws, tensorflow]
task: Named Entity Recognition
language: pt
edition: Legal NLP 1.0.0
spark_version: 3.2
supported: true
engine: tensorflow
annotator: BertForTokenClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a Deep Learning Portuguese Named Entity Recognition model for the legal domain, trained using Base Bert Embeddings, and is able to predict the following entities:

- ORGANIZACAO (Organizations)
- JURISPRUDENCIA (Jurisprudence)
- PESSOA (Person)
- TEMPO (Time)
- LOCAL (Location)
- LEGISLACAO (Laws)
- O (Other)

You can find different versions of this model in Models Hub:
- With a Deep Learning architecture (non-transformer) and Base Embeddings;
- With a Deep Learning architecture (non-transformer) and Large Embeddings;
- With a Transformers Architecture and Base Embeddings;
- With a Transformers Architecture and Large Embeddings;

## Predicted Entities

`PESSOA`, `ORGANIZACAO`, `LEGISLACAO`, `JURISPRUDENCIA`, `TEMPO`, `LOCAL`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_pt_bert_base_pt_1.0.0_3.2_1715673044681.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_pt_bert_base_pt_1.0.0_3.2_1715673044681.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = nlp.DocumentAssembler() \
        .setInputCol("text") \
        .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")\
       .setInputCols(["document"])\
       .setOutputCol("sentence")

tokenizer = nlp.Tokenizer() \
    .setInputCols("sentence") \
    .setOutputCol("token")

tokenClassifier = nlp.BertForTokenClassification.pretrained("legner_pt_bert_base","pt", "legal/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("ner")

pipeline = nlp.Pipeline(
  stages=[
    documentAssembler, 
    sentenceDetector, 
    tokenizer, 
    tokenClassifier])

example = spark.createDataFrame(pd.DataFrame({'text': ["""Mediante do exposto , com fundamento nos artigos 32 , i , e 33 , da lei 8.443/1992 , submetem-se os autos à consideração superior , com posterior encaminhamento ao ministério público junto ao tcu e ao gabinete do relator , propondo : a ) conhecer do recurso e , no mérito , negar-lhe provimento ; b ) comunicar ao recorrente , ao superior tribunal militar e ao tribunal regional federal da 2ª região , a fim de fornecer subsídios para os processos judiciais 2001.34.00.024796-9 e 2003.34.00.044227-3 ; e aos demais interessados a deliberação que vier a ser proferida por esta corte ” ."""]}))

result = pipeline.fit(example).transform(example)
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_pt_bert_base|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|pt|
|Size:|406.7 MB|
|Case sensitive:|true|
|Max sentence length:|128|

## References

Original texts available in https://paperswithcode.com/sota?task=Token+Classification&dataset=lener_br and in-house data augmentation with weak labelling