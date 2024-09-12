---
layout: model
title: Sentence Entity Resolver for NDC (sbiobert_base_cased_mli embeddings)
author: John Snow Labs
name: sbiobertresolve_ndc
date: 2024-09-12
tags: [clinical, en, licensed, ndc, entity_resolution]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts (like drugs/ingredients) to [National Drug Codes](https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory) using `sbiobert_base_cased_mli` Sentence Bert Embeddings. It also returns package options and alternative drugs in the `all_k_aux_label` column.

## Predicted Entities

`NDC codes`, `package options`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_NDC/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_ndc_en_5.4.1_3.0_1726129988440.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_ndc_en_5.4.1_3.0_1726129988440.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

ner = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")\

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

ndc_resolver = SentenceEntityResolverModel..pretrained("sbiobertresolve_ndc", "en", "clinical/models")\ \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("ndc_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages = [document_assembler,
                                       sentenceDetectorDL,
                                       tokenizer,
                                       word_embeddings,
                                       ner,
                                       ner_converter,
                                       c2doc,
                                       sbert_embedder,
                                       ndc_resolver])

text= "The patient was prescribed Amlodopine Vallarta 10-320mg, Eviplera. aspirin 81 mg and metformin 500 mg. The other patient is given Lescol 40 MG and Everolimus 1.5 mg tablet."
data = spark.createDataFrame([[text]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList("DRUG")

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols("ner_chunk_doc")
    .setOutputCol("sbert_embeddings")

val ndc_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_ndc", "en", "clinical/models")
    .setInputCols("sbert_embeddings")
    .setOutputCol("ndc_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(document_assembler,
                               sentence_detector,
                               tokenizer,
                               word_embeddings,
                               ner,
                               ner_converter,
                               chunk2doc,
                               sbert_embedder,
                               ndc_resolver))

val data = Seq("The patient was prescribed Amlodopine Vallarta 10-320mg, Eviplera. aspirin 81 mg and metformin 500 mg. The other patient is given Lescol 40 MG and Everolimus 1.5 mg tablet.").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
|    | ner_chunk                    | entity   | ndc_code   | aux_list                                                                                            |
|---:|:-----------------------------|:---------|:-----------|:----------------------------------------------------------------------------------------------------|
|  0 | Amlodopine Vallarta 10-320mg | DRUG     | 72483-0100 | '{'packages': "['1 BOTTLE in 1 BOX (72483-100-04)  / 120 mL in 1 BOTTLE\']", \'alternatives\': [ ...|
|  1 | aspirin 81 mg                | DRUG     | 41250-0780 | '{'packages': "['1 BOTTLE, PLASTIC in 1 PACKAGE (41250-780-01)  / 120 TABLET, DELAYED RELEASE in ...|
|  2 | metformin 500 mg             | DRUG     | 62207-0491 | '{'packages': "['5000 TABLET in 1 POUCH (62207-491-31)\', \'25000 TABLET in 1 CARTON (62207-491- ...|
|  3 | Lescol 40 MG                 | DRUG     | 0713-0862  | '{'packages': "['30 TABLET, FILM COATED in 1 BOTTLE, PLASTIC (0713-0862-30)\']", \'alternatives\ ...|
|  4 | Everolimus 1.5 mg tablet     | DRUG     | 0054-0604  | '{'packages': "['60 TABLET in 1 BOTTLE (0054-0604-21)\']", \'alternatives\': [\'67877-721\', \'4 ...|
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_ndc|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[ndc_code]|
|Language:|en|
|Size:|724.6 MB|
|Case sensitive:|false|

## References

It is trained on U.S. FDA 2024-NDC Codes dataset