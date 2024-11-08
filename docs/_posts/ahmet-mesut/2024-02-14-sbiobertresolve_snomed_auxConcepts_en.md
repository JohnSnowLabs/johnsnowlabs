---
layout: model
title: Sentence Entity Resolver for SNOMED Concepts
author: John Snow Labs
name: sbiobertresolve_snomed_auxConcepts
date: 2024-02-14
tags: [en, licensed, resolver, auxconcepts]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts to Snomed codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. This is also capable of extracting `Morph Abnormality`, `Clinical Drug`, `Clinical Drug Form`, `Procedure`, `Substance`, `Physical Object`, and `Body Structure` concepts of Snomed codes.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_auxConcepts_en_5.2.1_3.0_1707938389782.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_auxConcepts_en_5.2.1_3.0_1707938389782.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
documentAssembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
      .setInputCols(["document"])\
      .setOutputCol("sentence")

tokenizer = Tokenizer() \
      .setInputCols(["sentence"]) \
      .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en", "clinical/models")\
      .setInputCols(["sentence", "token"])\
      .setOutputCol("embeddings")

ner_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models") \
      .setInputCols(["sentence", "token", "embeddings"]) \
      .setOutputCol("ner_jsl")

ner_jsl_converter = NerConverter() \
      .setInputCols(["sentence", "token", "ner_jsl"]) \
      .setOutputCol("ner_jsl_chunk")\
      .setWhiteList(["Procedure","Substance","Drug_Ingredient","Internal_organ_or_component","Modifier","BMI","LDL","External_body_part_or_region","Alcohol","Treatment","Test","Smoking"])

chunk2doc = Chunk2Doc() \
      .setInputCols("ner_jsl_chunk") \
      .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
     .setInputCols(["ner_chunk_doc"])\
     .setOutputCol("sbert_embeddings")\
     .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_auxConcepts","en","clinical/models") \
     .setInputCols(["sbert_embeddings"]) \
     .setOutputCol("snomed_code")\
     .setDistanceFunction("EUCLIDEAN")

nlpPipeline= Pipeline(stages=[
                              documentAssembler,
                              sentenceDetector,
                              tokenizer,
                              word_embeddings,
                              ner_jsl,
                              ner_jsl_converter,
                              chunk2doc,
                              sbert_embedder,
                              snomed_resolver
])

text= """This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction. He was subsequently transferred to the CCU for close monitoring. He was hemodynamically stable at the time of admission to the CCU."""

df= spark.createDataFrame([[text]]).toDF("text")

result= nlpPipeline.fit(df).transform(df)
```
```scala
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val nerJsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner_jsl")

val nerJslConverter = new NerConverter()
  .setInputCols(Array("sentence", "token", "ner_jsl"))
  .setOutputCol("ner_jsl_chunk")
  .setWhiteList(Array("Procedure","Substance","Drug_Ingredient","Internal_organ_or_component","Modifier","BMI","LDL","External_body_part_or_region","Alcohol","Treatment","Test","Smoking"))

val chunk2doc = new Chunk2Doc()
  .setInputCols(Array("ner_jsl_chunk"))
  .setOutputCol("ner_chunk_doc")

val sbertEmbedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("sbert_embeddings")
  .setCaseSensitive(False)

val snomedResolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_auxConcepts", "en", "clinical/models")
  .setInputCols(Array("sbert_embeddings"))
  .setOutputCol("snomed_code")
  .setDistanceFunction("EUCLIDEAN")

val nlpPipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  wordEmbeddings,
  nerJsl,
  nerJslConverter,
  chunk2doc,
  sbertEmbedder,
  snomedResolver
))

val text= """This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction. He was subsequently transferred to the CCU for close monitoring. He was hemodynamically stable at the time of admission to the CCU."""

val df = Seq(text).toDF("text")

val result = nlpPipeline.fit(df).transform(df)

```
</div>

## Results

```bash
+-----------------------+---------------+-----------+-----------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|                  chunk|          label|snomed_code|             resolution|                                         all_codes|                                   all_resolutions|                                    all_aux_labels|
+-----------------------+---------------+-----------+-----------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|                tobacco|        Smoking|   57264008|                tobacco|57264008:::102407002:::39953003:::159882006:::1...|tobacco:::tobacco smoke:::tobacco - substance::...|Organism:::Substance:::Substance:::Social Conte...|
|            nonspecific|       Modifier|   10003008|           non-specific|10003008:::261992003:::863956004:::300844001:::...|non-specific:::non-biological:::non-sterile:::n...|Qualifier Value:::Qualifier Value:::Qualifier V...|
|cardiac catheterization|      Procedure|   41976001|cardiac catheterization|41976001:::705923009:::721968000:::467735004:::...|cardiac catheterization:::cardiac catheter:::ca...|Procedure:::Physical Object:::Record Artifact::...|
|               atropine|Drug_Ingredient|   73949004|               atropine|73949004:::105075009:::349945006:::410493009:::...|atropine:::atropine measurement:::oral atropine...|Pharma/Biol Product:::Procedure:::Clinical Drug...|
|                 fluids|Drug_Ingredient|  255765007|                  fluid|255765007:::246498002:::258442002:::251851008::...|fluid:::fluid used:::fluid sample:::fluid input...|Qualifier Value:::Attribute:::Specimen:::Observ...|
|               dopamine|Drug_Ingredient|   59187003|               dopamine|59187003:::412383006:::37484001:::32779004:::41...|dopamine:::dopamine agent:::dopamine receptor::...|Pharma/Biol Product:::Substance:::Substance:::P...|
+-----------------------+---------------+-----------+-----------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_auxConcepts|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|1.5 GB|
|Case sensitive:|false|
