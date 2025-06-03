---
layout: model
title: Company Name Normalization (Edgar Database)
author: John Snow Labs
name: finel_edgar_company_name_fe
date: 2024-06-10
tags: [finance, edgar, licensed, en]
task: Entity Resolution
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
recommended: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is an Entity Linking / Entity Resolution model, which allows you to map an extracted Company Name from any NER model, to the name used by SEC in Edgar Database. This can come in handy to afterwards use Edgar Chunk Mappers with the output of this resolution, to carry out data augmentation and retrieve additional information stored in Edgar Database about a company. For more information about data augmentation, check `Chunk Mapping` task in Models Hub.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finel_edgar_company_name_fe_en_1.0.0_3.0_1718020983963.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finel_edgar_company_name_fe_en_1.0.0_3.0_1718020983963.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("ner_chunk")

embeddings = nlp.BGEEmbeddings.pretrained("finance_bge_base_embeddings", "en", "finance/models")\ 
      .setInputCols("ner_chunk") \
      .setOutputCol("sentence_embeddings")
    
resolver = finance.SentenceEntityResolverModel.pretrained("finel_edgar_company_name_fe", "en", "finance/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("normalized")\
    .setDistanceFunction("EUCLIDEAN")

pipelineModel = nlp.Pipeline(
      stages = [
          documentAssembler,
          embeddings,
          resolver
      ])

lp = LightPipeline(pipelineModel)

lp.fullAnnotate("AmeriCann Inc")
```

</div>

## Results

```bash
|   chunks   |   begin   |   end   |         code          |                                                                                                                                                                                                                                        all_codes                                                                                                                                                                                                                                         |                                                                                                                                                                                                           resolutions                                                                                                                                                                                                           |                                                                                                 all_distances                                                                                                 |
|:----------:|:---------:|:-------:|:---------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|     0      |   CONTACT GOLD  |    0    |    11   |  Contact Gold Corp.  |  [Contact Gold Corp., Contact Minerals Corp., Source Gold Corp., GENERAL GOLD CORP, Gold Alan D, INTERNET GOLD GOLDEN LINES LTD, METALINE CONTACT MINES, GOLD STEPHEN J, AuRico Gold Inc., ISHARES GOLD TRUST, GLOBAL GOLD CORP, Golden Minerals Co, Sprott Physical Gold Trust, FOCUS GOLD Corp, GOLDEN CYCLE GOLD CORP]  |  [Contact Gold Corp., Contact Minerals Corp., Source Gold Corp., GENERAL GOLD CORP, Gold Alan D, INTERNET GOLD GOLDEN LINES LTD, METALINE CONTACT MINES, GOLD STEPHEN J, AuRico Gold Inc., ISHARES GOLD TRUST, GLOBAL GOLD CORP, Golden Minerals Co, Sprott Physical Gold Trust, FOCUS GOLD Corp, GOLDEN CYCLE GOLD CORP]  |  [0.0684, 0.3294, 0.3476, 0.3541, 0.3548, 0.3635, 0.3698, 0.3879, 0.3902, 0.3916, 0.3933, 0.3958, 0.3964, 0.3969, 0.3974]  |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finel_edgar_company_name_fe|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[original_company_name]|
|Language:|en|
|Size:|1.2 GB|
|Case sensitive:|false|

## References

In-house scrapping and postprocessing of SEC Edgar Database