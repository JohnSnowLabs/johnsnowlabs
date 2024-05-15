---
layout: model
title: Brazilian Portuguese NER for Laws (Bert, Base)
author: John Snow Labs
name: legner_pt_bert_base
date: 2024-05-15
tags: [lener, pt, laws, tensorflow, licensed, legal]
task: Named Entity Recognition
language: pt
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: LegalBertForTokenClassification
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_pt_bert_base_pt_1.0.0_3.0_1715763482236.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_pt_bert_base_pt_1.0.0_3.0_1715763482236.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained()\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols("sentence")\
  .setOutputCol("token")

tokenClassifier = legal.BertForTokenClassification.load("legner_pt_bert_base","pt", "legal/models")\
  .setInputCols("token", "sentence")\
  .setOutputCol("label")\
  .setCaseSensitive(True)

ner_converter = nlp.NerConverter()\
  .setInputCols(["sentence","token","label"])\
  .setOutputCol("ner_chunk")


pipeline =  nlp.Pipeline(
    stages=[
  documentAssembler,
  sentenceDetector,
  tokenizer,
  tokenClassifier,
  ner_converter
    ]
)

example = spark.createDataFrame(pd.DataFrame({'text': ["""Mediante do exposto , com fundamento nos artigos 32 , i , e 33 , da lei 8.443/1992 , submetem-se os autos à consideração superior , com posterior encaminhamento ao ministério público junto ao tcu e ao gabinete do relator , propondo : a ) conhecer do recurso e , no mérito , negar-lhe provimento ; b ) comunicar ao recorrente , ao superior tribunal militar e ao tribunal regional federal da 2ª região , a fim de fornecer subsídios para os processos judiciais 2001.34.00.024796-9 e 2003.34.00.044227-3 ; e aos demais interessados a deliberação que vier a ser proferida por esta corte ” ."""]}))

result = pipeline.fit(example).transform(example)
```

</div>

## Results

```bash
+--------------+---------+----------+
|         token|ner_label|confidence|
+--------------+---------+----------+
|      Mediante|        O|0.99998605|
|            do|        O| 0.9999868|
|       exposto|        O|0.99998623|
|             ,|        O|  0.999987|
|           com|        O|0.99998677|
|    fundamento|        O| 0.9999863|
|           nos|        O|0.99998486|
|       artigos|  I-TEMPO| 0.9995784|
|            32|  B-LOCAL| 0.9998317|
|             ,|  B-LOCAL|0.99983853|
|             i|  B-LOCAL| 0.9998391|
|             ,|  B-LOCAL|  0.999842|
|             e|  B-LOCAL| 0.9998447|
|            33|  B-LOCAL| 0.9998419|
|             ,|  B-LOCAL| 0.9998423|
|            da|  B-LOCAL| 0.9998431|
|           lei|  B-LOCAL| 0.9998434|
|    8.443/1992|  B-LOCAL|0.99982893|
|             ,|        O| 0.9999863|
|   submetem-se|        O|0.99998677|
|            os|        O| 0.9999873|
|         autos|        O|0.99998647|
|             à|        O|0.99998707|
|  consideração|        O| 0.9999871|
|      superior|        O| 0.9999868|
|             ,|        O|0.99998736|
|           com|        O| 0.9999876|
|     posterior|        O|0.99998707|
|encaminhamento|        O|0.99998724|
|            ao|        O|0.99998707|
|    ministério|        O| 0.9999853|
|       público|        O| 0.9999854|
|         junto|        O|0.99998665|
|            ao|        O|0.99998516|
|           tcu|        O| 0.9993648|
|             e|        O|0.99998665|
|            ao|        O|0.99998677|
|      gabinete|        O| 0.9999856|
|            do|        O| 0.9999865|
|       relator|        O|0.99998575|
|             ,|        O| 0.9999872|
|      propondo|        O|0.99998724|
|             :|        O|0.99998707|
|             a|        O| 0.9999873|
|             )|        O| 0.9999873|
|      conhecer|        O|0.99998724|
|            do|        O| 0.9999872|
|       recurso|        O| 0.9999867|
|             e|        O| 0.9999872|
|             ,|        O| 0.9999869|
|            no|        O|0.99998695|
|        mérito|        O| 0.9999872|
|             ,|        O| 0.9999873|
|     negar-lhe|        O| 0.9999875|
|    provimento|        O|0.99998724|
|             ;|        O| 0.9999865|
|             b|        O|0.99998635|
|             )|        O| 0.9999871|
|     comunicar|        O| 0.9999869|
|            ao|        O| 0.9999872|
|    recorrente|        O| 0.9999854|
|             ,|        O|  0.999987|
|            ao|        O|  0.999987|
|      superior|        O| 0.9999805|
|      tribunal|        O|0.99998057|
|       militar|        O| 0.9999655|
|             e|        O|0.99998677|
|            ao|        O|0.99998665|
|      tribunal|        O|0.99996954|
|      regional|        O| 0.9999731|
|       federal|        O| 0.9999361|
|            da|        O| 0.9999758|
|            2ª|        O| 0.9999704|
|        região|        O|0.99994576|
|             ,|        O|  0.999987|
|             a|        O| 0.9999872|
|           fim|        O|0.99998724|
|            de|        O|  0.999987|
|      fornecer|        O|0.99998724|
|     subsídios|        O| 0.9999871|
|          para|        O| 0.9999867|
|            os|        O| 0.9999863|
|     processos|        O| 0.9999849|
|     judiciais|        O| 0.9999815|
|          2001|        O|0.99994475|
|             .|        O|0.99998444|
|34.00.024796-9|        O| 0.9999273|
|             e|        O| 0.9999757|
|          2003|        O| 0.9908976|
|             .|        O|0.99998164|
|34.00.044227-3|        O| 0.9999851|
|             ;|        O| 0.9999866|
|             e|        O|0.99998695|
|           aos|        O| 0.9999869|
|        demais|        O|0.99998677|
|  interessados|        O| 0.9999867|
|             a|        O|0.99998707|
|   deliberação|        O|0.99998724|
|           que|        O| 0.9999871|
|          vier|        O| 0.9999868|
|             a|        O| 0.9999867|
|           ser|        O| 0.9999872|
|     proferida|        O| 0.9999871|
|           por|        O|0.99998695|
|          esta|        O|0.99998677|
|         corte|        O|0.99998224|
|             ”|        O| 0.9999714|
|             .|        O|0.99998647|
+--------------+---------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_pt_bert_base|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[ner]|
|Language:|pt|
|Size:|403.3 MB|
|Case sensitive:|true|
|Max sentence length:|128|

## References

Original texts available in https://paperswithcode.com/sota?task=Token+Classification&dataset=lener_br and in-house data augmentation with weak labelling