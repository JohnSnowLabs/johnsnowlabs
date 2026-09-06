---
layout: model
title: Sentence Entity Resolver for LOINC (sbiobert_base_cased_mli_onnx embeddings)
author: John Snow Labs
name: sbiobertresolve_loinc_numeric_augmented_2_83
date: 2026-09-06
tags: [en, entity_resolution, licensed, clinical, loinc, sbiobert]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted clinical NER entities to Logical Observation Identifiers Names and Codes (LOINC) codes using `sbiobert_base_cased_mli_onnx` Sentence Bert Embeddings. It is trained on the augmented version of the LOINC 2.83 dataset (LOINC 2.83 official data plus an in-house curated dataset), scoped to numeric LOINC codes, without the inclusion of LOINC's non-numeric Part, Answer, Panel, Survey, and other auxiliary/document codes.

If you also need LOINC's non-numeric auxiliary codes, use `sbiobertresolve_loinc_augmented_2_83` instead.

It also provides the official resolution of the codes within the brackets.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_loinc_numeric_augmented_2_83_en_6.4.1_3.4_1788724011444.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_loinc_numeric_augmented_2_83_en_6.4.1_3.4_1788724011444.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

ner_radiology = MedicalNerModel.pretrained("ner_radiology","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_radiology")

ner_converter_radiology = NerConverterInternal()\
    .setInputCols(["sentence","token","ner_radiology"])\
    .setOutputCol("ner_chunk_radiology")\
    .setWhiteList(["Test"])

ner_jsl = MedicalNerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_jsl")

ner_converter_jsl = NerConverterInternal()\
    .setInputCols(["sentence","token","ner_jsl"])\
    .setOutputCol("ner_chunk_jsl")\
    .setWhiteList(["Test"])

chunk_merger = ChunkMergeApproach()\
    .setInputCols("ner_chunk_jsl", "ner_chunk_radiology")\
    .setOutputCol("ner_chunk")

chunk2doc = Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc_numeric_augmented_2_83","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,\
    ner_radiology, ner_converter_radiology, ner_jsl, ner_converter_jsl,\
    chunk_merger, chunk2doc,\
    embedder, resolver\
])

data = spark.createDataFrame([["The patient's glucose and hemoglobin A1c levels were checked, along with a basic metabolic panel including sodium and potassium, and a complete blood count."]]).toDF("text")
result = pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

ner_radiology = medical.NerModel.pretrained("ner_radiology","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_radiology")

ner_converter_radiology = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner_radiology"])\
    .setOutputCol("ner_chunk_radiology")\
    .setWhiteList(["Test"])

ner_jsl = medical.NerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_jsl")

ner_converter_jsl = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner_jsl"])\
    .setOutputCol("ner_chunk_jsl")\
    .setWhiteList(["Test"])

chunk_merger = medical.ChunkMergeApproach()\
    .setInputCols("ner_chunk_jsl", "ner_chunk_radiology")\
    .setOutputCol("ner_chunk")

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc_numeric_augmented_2_83","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,\
    ner_radiology, ner_converter_radiology, ner_jsl, ner_converter_jsl,\
    chunk_merger, chunk2doc,\
    embedder, resolver\
])

data = spark.createDataFrame([["The patient's glucose and hemoglobin A1c levels were checked, along with a basic metabolic panel including sodium and potassium, and a complete blood count."]]).toDF("text")
result = pipeline.fit(data).transform(data)
```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_radiology = MedicalNerModel
    .pretrained("ner_radiology", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner_radiology")

val ner_converter_radiology = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_radiology"))
    .setOutputCol("ner_chunk_radiology")
    .setWhiteList(Array("Test"))

val ner_jsl = MedicalNerModel
    .pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner_jsl")

val ner_converter_jsl = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_jsl"))
    .setOutputCol("ner_chunk_jsl")
    .setWhiteList(Array("Test"))

val chunk_merger = new ChunkMergeApproach()
    .setInputCols(Array("ner_chunk_jsl", "ner_chunk_radiology"))
    .setOutputCol("ner_chunk")

val chunk2doc = new Chunk2Doc()
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("ner_chunk_doc")

val embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_loinc_numeric_augmented_2_83", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner_radiology, ner_converter_radiology, ner_jsl, ner_converter_jsl,
    chunk_merger, chunk2doc,
    embedder, resolver
))

val data = Seq("The patient's glucose and hemoglobin A1c levels were checked, along with a basic metabolic panel including sodium and potassium, and a complete blood count.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk             | entity   | LOINC Code   | Resolution                                                      | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:----------------------|:---------|:-------------|:----------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| glucose               | Test     | 2345-7       | glucose [Glucose [Mass/volume] in Serum or Plasma]              | 2345-7:::74790-7:::51419-0:::81637-1:::47621-8:::32318-8:::104638-2:::50016-5:::... | 0.0000:::0.0666:::0.0713:::0.0763:::0.0738:::0.0781:::0.0824:::0.0880:::0.0952::... | glucose [Glucose [Mass/volume] in Serum or Plasma]:::Glucose HBT [Glucose challe... |
| hemoglobin A1c levels | Test     | 41995-2      | hemoglobin a1c [Hemoglobin A1c [Mass/volume] in Blood]          | 41995-2:::43150-2:::4548-4:::10486-9:::21687-9:::112870-1:::51196-4:::4593-0:::1... | 0.0227:::0.0727:::0.0987:::0.1004:::0.1010:::0.1161:::0.1237:::0.1290:::0.1311::... | hemoglobin a1c [Hemoglobin A1c [Mass/volume] in Blood]:::Hemoglobin A1c measurem... |
| basic metabolic panel | Test     | 51990-0      | basic metabolic panel [Basic metabolic panel - Blood]           | 51990-0:::101655-9:::89044-2:::9350-0:::50042-1:::79531-0:::43147-8:::24321-2:::... | 0.0000:::0.1401:::0.1417:::0.1533:::0.1772:::0.1913:::0.2036:::0.2081:::0.2056::... | basic metabolic panel [Basic metabolic panel - Blood]:::basic metabolic & hemato... |
| sodium                | Test     | 2951-2       | sodium [Sodium [Moles/volume] in Serum or Plasma]               | 2951-2:::32340-2:::50912-5:::81011-9:::9086-0:::16527-4:::2950-4:::9087-8:::2954... | 0.0000:::0.0504:::0.0815:::0.0820:::0.0910:::0.0981:::0.1062:::0.1114:::0.1137::... | sodium [Sodium [Moles/volume] in Serum or Plasma]:::Sodium, Specimen [Sodium [Mo... |
| potassium             | Test     | 2823-3       | potassium [Potassium [Moles/volume] in Serum or Plasma]         | 2823-3:::10322-6:::32336-0:::59733-6:::9073-8:::28003-2:::2821-7:::50902-6:::283... | 0.0000:::0.0583:::0.0662:::0.0821:::0.0882:::0.0966:::0.1032:::0.1048:::0.1101::... | potassium [Potassium [Moles/volume] in Serum or Plasma]:::potassium intake [Pota... |
| complete blood count  | Test     | 24358-4      | Complete Blood Count [Hemogram without Platelets panel - Blood] | 24358-4:::58410-2:::74412-8:::47288-6:::1335-9:::789-8:::51876-1:::786-4:::777-3... | 0.0000:::0.1068:::0.1309:::0.1352:::0.1489:::0.1658:::0.1671:::0.1761:::0.1936::... | Complete Blood Count [Hemogram without Platelets panel - Blood]:::complete blood... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_loinc_numeric_augmented_2_83|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sbert_embeddings]|
|Output Labels:|[loinc_code]|
|Language:|en|
|Size:|943.2 MB|
|Case sensitive:|false|