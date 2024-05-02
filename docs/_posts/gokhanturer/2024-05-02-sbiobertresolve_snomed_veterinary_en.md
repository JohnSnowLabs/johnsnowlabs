---
layout: model
title: Sentence Entity Resolver for SNOMED Veterinary
author: John Snow Labs
name: sbiobertresolve_snomed_veterinary
date: 2024-05-02
tags: [en, licenced, resolver, snomed, veterinary, licensed]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps veterinary-related entities and concepts to SNOMED codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_veterinary_en_5.3.1_3.4_1714649246051.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_veterinary_en_5.3.1_3.4_1714649246051.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("ner_chunk")

bert_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_veterinary", "en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")


snomed_pipeline = PipelineModel(stages = [
    documentAssembler,
    bert_embeddings,
    snomed_resolver])

text= ["lymphoblastic lymphoma", "Arthritis", "mink distemper"]

test_df= spark.createDataFrame(pd.DataFrame(text, columns=["text"]))

result= snomed_pipeline.transform(test_df)
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("ner_chunk")

val bert_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

val snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_veterinary")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("snomed_code")
    .setDistanceFunction("EUCLIDEAN")

val snomed_pipeline =new PipelineModel().setStages(Array(documentAssembler,
                                                         bert_embeddings,
                                                         snomed_resolver))

val text= Seq("lymphoblastic lymphoma","Arthritis", "mink distemper").toDF("text")


val result= snomed_pipeline.transform(test_df)
```
</div>

## Results

```bash
+----------------------+---------------+-------------------------+------------------------------------------------------------+------------------------------------------------------------+
|             ner_chunk|    snomed_code|              description|                                                   all_codes|                                                 resolutions|
+----------------------+---------------+-------------------------+------------------------------------------------------------+------------------------------------------------------------+
|lymphoblastic lymphoma|312281000009102|   lymphoblastic lymphoma|312281000009102:::360351000009103:::91857003:::302841002:...|lymphoblastic lymphoma:::cutaneous epitheliotropic lympho...|
|             Arthritis|309181000009103|immune-mediated arthritis|309181000009103:::298162008:::35771000009105:::3519007:::...|immune-mediated arthritis:::arthritis of shoulder joint::...|
|        mink distemper|348361000009108|           mink distemper|348361000009108:::86031000009108:::207191000009103:::1901...|mink distemper:::dendropicos obsoletus:::xenops minutus o...|
+----------------------+---------------+-------------------------+------------------------------------------------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_veterinary|
|Compatibility:|Healthcare NLP 5.3.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|167.8 MB|
|Case sensitive:|false|

## References

This model is trained with the Veterinary Extension to SNOMED CT(R): April 1, 2024 Release version, available at the website https://vtsl.vetmed.vt.edu/extension/