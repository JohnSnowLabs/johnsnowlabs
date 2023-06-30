---
layout: model
title: Sentence Entity Resolver for ICD-10-GM
author: John Snow Labs
name: robertaresolve_icd10gm
date: 2023-06-30
tags: [icd10gm, sbertresolver, de, clinical, licensed]
task: Entity Resolution
language: de
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted medical entities to ICD10-GM codes for the German language using `xlmroberta_embeddings_paraphrase_mpnet_base_v2` (xx) embeddings.

## Predicted Entities

`ICD10GM Codes`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_ICD10_GM_DE/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/ER_ICD10_GM_DE.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/robertaresolve_icd10gm_de_4.4.4_3.0_1688102195448.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/robertaresolve_icd10gm_de_4.4.4_3.0_1688102195448.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = Tokenizer() \
    .setInputCols("document") \
    .setOutputCol("token")

roberta_embeddings = XlmRoBertaEmbeddings.pretrained("xlmroberta_embeddings_paraphrase_mpnet_base_v2", "xx")\
    .setInputCols(["document",'token'])\
    .setOutputCol("word_embeddings")\
    .setCaseSensitive(True)

sentence_embeddings = SentenceEmbeddings()\
    .setInputCols("document", "word_embeddings")\
    .setOutputCol("sentence_embeddings")

icd10gm_resolver = SentenceEntityResolverModel.pretrained("robertaresolve_icd10gm", "de", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("icd10gm_code")

icd10gm_pipeline = Pipeline(
    stages = [
        documentAssembler,
        tokenizer,
        roberta_embeddings,
        sentence_embeddings,
        icd10gm_resolver])

icd10gm_model = icd10gm_pipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

icd10gm_lp = LightPipeline(icd10gm_model)

icd_lp.fullAnnotate("Dyspnoe")
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val roberta_embeddings = XlmRoBertaEmbeddings.pretrained("xlmroberta_embeddings_paraphrase_mpnet_base_v2", "xx")
    .setInputCols(Array("document",'token'))
    .setOutputCol("word_embeddings")
    .setCaseSensitive(True)

val sentence_embeddings = new SentenceEmbeddings()
    .setInputCols(array("document", "word_embeddings"))
    .setOutputCol("sentence_embeddings")

val icd10gm_resolver = SentenceEntityResolverModel.pretrained("robertaresolve_icd10gm", "de", "clinical/models")
    .setInputCols(Array("sentence_embeddings"))
    .setOutputCol("icd10gm_code")

val icd10gm_pipeline = new Pipeline(
    stages = Array(
        documentAssembler,
        tokenizer,
        roberta_embeddings,
        sentence_embeddings,
        icd10gm_resolver))

val icd10gm_model = icd10gm_pipeline.fit(Seq("").toDS.toDF("text"))

val icd10gm_lp = LightPipeline(icd10gm_model)

val icd_lp.fullAnnotate("Dyspnoe")
```
</div>

## Results

```bash
|    | chunks  | code    | resolutions                                                            | all_codes                                       | all_distances                                             |
|---:|:--------|:--------|:----------------------------------------------------------------------:|------------------------------------------------:|:----------------------------------------------------------|
|  0 | Dyspnoe | R06.0   |Dyspnoe:::Dysphagie:::Dysurie:::Dyspareunie:::Dysthymia:::Dystonie:::...| R06.0:::R13:::R30.0:::N94.1:::F34.1:::G24:::... | 0.0000:::1.0966:::1.1766:::1.2127:::1.2228:::1.3126:::... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|robertaresolve_icd10gm|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[icd10gm_code]|
|Language:|de|
|Size:|49.1 MB|
|Case sensitive:|true|