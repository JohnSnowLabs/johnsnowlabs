---
layout: model
title: Sentence Entity Resolver for SNOMED (sbiobertresolve_snomed_no_class)
author: John Snow Labs
name: sbiobertresolve_snomed_no_class
date: 2024-03-05
tags: [licensed, en, resolver, snomed, no_class]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model utilizes BERT sentence embeddings from `sbiobert_base_cased_mli` to map extracted medical entities (no concept class) to SNOMED codes.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_no_class_en_5.3.0_3.0_1709629048666.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_no_class_en_5.3.0_3.0_1709629048666.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = Tokenizer()\
  .setInputCols(["sentence"])\
  .setOutputCol("token")\

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
  .setInputCols(["sentence", "token"])\
  .setOutputCol("embeddings")

ner_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models") \
  .setInputCols(["sentence", "token", "embeddings"]) \
  .setOutputCol("ner_jsl")

ner_jsl_converter = NerConverterInternal() \
  .setInputCols(["sentence", "token", "ner_jsl"]) \
  .setOutputCol("ner_chunk")\
  .setWhiteList(["Drug",
                 "Drug_Ingredient",
                 "Drug_BrandName",
                 "Disease_Syndrome_Disorder",
                 "Kidney_Disease",
                 "Heart_Disease",
                 "Diabetes",
                 "Oncological"])\

chunk2doc = Chunk2Doc()\
  .setInputCols("ner_chunk")\
  .setOutputCol("ner_chunk_doc")

sbert_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
  .setInputCols(["ner_chunk_doc"])\
  .setOutputCol("sbert_embeddings")\
  .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_no_class", "en", "clinical/models")\
  .setInputCols(["sbert_embeddings"]) \
  .setOutputCol("snomed_code")\
  .setDistanceFunction("EUCLIDEAN")

snomed_pipeline = Pipeline(stages = [
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_jsl,
    ner_jsl_converter,
    chunk2doc,
    sbert_embeddings,
    snomed_resolver
])

data = spark.createDataFrame([["""John's doctor prescribed ofloxacin for his secondary conjunctivitis, cefixime for his cystic urethritis, ibuprofen for his inflammation, and cilnidipine for his hypertension on 2023-12-01."""]]).toDF("text")

model = snomed_pipeline.fit(data)
result = model.transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings")

val ner_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner_chunk")

val ner_jsl_converter = new NerConverter()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Drug",
                       "Drug_Ingredient",
                       "Drug_BrandName",
                       "Disease_Syndrome_Disorder",
                       "Kidney_Disease",
                       "Heart_Disease",
                       "Diabetes",
                       "Oncological"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(False)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_snomed_no_class", "en", "clinical/models")
    .setInputCols(Array("ner_chunk", "sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val nlpPipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_jsl,
    ner_jsl_converter,
    chunk2doc,
    sbert_embeddings,
    snomed_resolver
    ))

val data = Seq("John's doctor prescribed ofloxacin for his secondary conjunctivitis, cefixime for his cystic urethritis, ibuprofen for his inflammation, and cilnidipine for his hypertension on 2023-12-01.") .toDF("text")

val model = snomed_pipeline.fit(data)

val result = model.transform(data)
```
</div>

## Results

```bash
+-----------------+-------------------------+-----------+---------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|            chunk|                    label|snomed_code|                                   resolution|                                         all_codes|                                   all_resolutions|
+-----------------+-------------------------+-----------+---------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|        ofloxacin|          Drug_Ingredient| 1252718003|   cefixime- and ofloxacin-containing product|1252718003:::1172759009:::1162766006:::11725730...|cefixime- and ofloxacin-containing product:::of...|
|   conjunctivitis|Disease_Syndrome_Disorder| 1217666006|                     secondary conjunctivitis|1217666006:::15680761000119102:::1177057009:::1...|secondary conjunctivitis:::left infectious conj...|
|         cefixime|          Drug_Ingredient| 1217570005|                          cefixime trihydrate|1217570005:::1162766006:::1252718003:::50020121...|cefixime trihydrate:::fropenem:::cefixime- and ...|
|cystic urethritis|Disease_Syndrome_Disorder| 1259233009|                            cystic urethritis|1259233009:::1259241009:::1259225008:::11792350...|cystic urethritis:::stricture of membranous ure...|
|        ibuprofen|          Drug_Ingredient| 1172854008|ibuprofen- and paracetamol-containing product|1172854008:::1269077005:::1217598008:::11728570...|ibuprofen- and paracetamol-containing product::...|
|      cilnidipine|          Drug_Ingredient| 1177123004|                                  cilnidipine|1177123004:::1179035008:::1217308000:::11936630...|cilnidipine:::cilnidipine-containing product:::...|
+-----------------+-------------------------+-----------+---------------------------------------------+--------------------------------------------------+--------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_no_class|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|104.0 MB|
|Case sensitive:|false|

## References

This model is trained with the augmented version of NIH September 2023 SNOMED CT United States (US) Edition.
