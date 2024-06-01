---
layout: model
title: Brazilian Portuguese NER for Laws (Bert, Large)
author: John Snow Labs
name: legner_lener_large
date: 2024-05-15
tags: [laws, ner, licensed, legal, tensorflow, lener, pt]
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_lener_large_pt_1.0.0_3.0_1715772900343.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_lener_large_pt_1.0.0_3.0_1715772900343.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

tokenClassifier = legal.BertForTokenClassification.pretrained("legner_lener_large","pt", "legal/models")\
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
+--------------+-------------+----------+
|         token|    ner_label|confidence|
+--------------+-------------+----------+
|      Mediante|            O|0.99998903|
|            do|            O|0.99999386|
|       exposto|            O|0.99999356|
|             ,|            O|0.99998516|
|           com|            O| 0.9999937|
|    fundamento|            O|0.99998814|
|           nos|            O|0.99998933|
|       artigos|      I-TEMPO| 0.9768946|
|            32|      B-LOCAL| 0.9833129|
|             ,|      B-LOCAL| 0.9897361|
|             i|      B-LOCAL| 0.9860687|
|             ,|      B-LOCAL|0.99019605|
|             e|      B-LOCAL|  0.988641|
|            33|      B-LOCAL|0.98958844|
|             ,|      B-LOCAL|  0.989682|
|            da|      B-LOCAL|0.97983617|
|           lei|      B-LOCAL| 0.9777896|
|    8.443/1992|      B-LOCAL|0.94548935|
|             ,|            O| 0.9997625|
|   submetem-se|            O|0.99999225|
|            os|            O|0.99999356|
|         autos|            O|0.99999285|
|             à|            O| 0.9999936|
|  consideração|            O| 0.9999945|
|      superior|            O| 0.9999938|
|             ,|            O|0.99999297|
|           com|            O| 0.9999949|
|     posterior|            O|0.99999535|
|encaminhamento|            O|0.99999404|
|            ao|            O| 0.9999939|
|    ministério|            O|0.99998385|
|       público|            O|0.99997985|
|         junto|            O| 0.9999902|
|            ao|            O| 0.9999913|
|           tcu|            O| 0.9961068|
|             e|            O| 0.9999804|
|            ao|            O|0.99999124|
|      gabinete|            O| 0.9999747|
|            do|            O| 0.9999911|
|       relator|            O|0.99999297|
|             ,|            O|0.99998975|
|      propondo|            O| 0.9999942|
|             :|            O|0.99999416|
|             a|            O| 0.9999926|
|             )|            O|  0.999994|
|      conhecer|            O|0.99999493|
|            do|            O|0.99999475|
|       recurso|            O|0.99999416|
|             e|            O|  0.999994|
|             ,|            O| 0.9999923|
|            no|            O| 0.9999945|
|        mérito|            O|0.99999404|
|             ,|            O| 0.9999926|
|     negar-lhe|            O|0.99999475|
|    provimento|            O|0.99999505|
|             ;|            O| 0.9999914|
|             b|            O| 0.9999917|
|             )|            O| 0.9999943|
|     comunicar|            O|0.99999446|
|            ao|            O| 0.9999935|
|    recorrente|            O| 0.9999941|
|             ,|            O| 0.9999869|
|            ao|            O|0.99999243|
|      superior|            O| 0.9933063|
|      tribunal|            O|0.83631223|
|       militar|            O|0.76226306|
|             e|            O| 0.9988131|
|            ao|            O| 0.9999895|
|      tribunal|B-ORGANIZACAO|0.94998056|
|      regional| I-LEGISLACAO|0.91478646|
|       federal| I-LEGISLACAO| 0.9775761|
|            da| I-LEGISLACAO| 0.9674108|
|            2ª| I-LEGISLACAO| 0.9871655|
|        região| I-LEGISLACAO|0.99471426|
|             ,|            O| 0.9999918|
|             a|            O|0.99999434|
|           fim|            O|0.99999356|
|            de|            O| 0.9999942|
|      fornecer|            O| 0.9999948|
|     subsídios|            O|0.99999213|
|          para|            O| 0.9999924|
|            os|            O| 0.9999925|
|     processos|            O|0.99998784|
|     judiciais|            O|  0.999987|
|          2001|            O|0.99967766|
|             .|            O|  0.998813|
|34.00.024796-9|            O| 0.9933802|
|             e|            O|  0.999508|
|          2003|I-ORGANIZACAO|0.51847184|
|             .|            O|   0.99998|
|34.00.044227-3|            O| 0.9999412|
|             ;|            O| 0.9999937|
|             e|            O| 0.9999936|
|           aos|            O| 0.9999932|
|        demais|            O| 0.9999952|
|  interessados|            O|0.99999493|
|             a|            O|  0.999994|
|   deliberação|            O| 0.9999939|
|           que|            O| 0.9999942|
|          vier|            O| 0.9999944|
|             a|            O| 0.9999935|
|           ser|            O| 0.9999951|
|     proferida|            O| 0.9999954|
|           por|            O| 0.9999936|
|          esta|            O|0.99999356|
|         corte|            O|0.99992704|
|             ”|            O| 0.9994554|
|             .|            O| 0.9993955|
+--------------+-------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_lener_large|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[ner]|
|Language:|pt|
|Size:|1.2 GB|
|Case sensitive:|true|
|Max sentence length:|128|

## References

Original texts available in https://paperswithcode.com/sota?task=Token+Classification&dataset=lener_br and in-house data augmentation with weak labelling
