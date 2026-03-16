---
layout: model
title: Sentence Entity Resolver for SNOMED (sbiobertresolve_snomed_findings)
author: John Snow Labs
name: sbiobertresolve_snomed_findings
date: 2026-03-16
tags: [en, snomed, resolver, licensed, clinical, findings]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.3.0
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The model maps extracted medical entities to their corresponding Snomed codes (Clinical Findings) using sbiobert_base_cased_mli BERT sentence embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_findings_en_6.3.0_3.4_1773690208747.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_findings_en_6.3.0_3.4_1773690208747.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
      .setOutputCol("embeddings")

ner_jsl  = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
      .setInputCols(["sentence", "token", "embeddings"])\
      .setOutputCol("ner_jsl")


ner_jsl_converter  = NerConverterInternal()\
      .setInputCols(["sentence", "token", "ner_jsl"])\
      .setOutputCol("ner_jsl_chunk")\
      .setWhiteList(["Kidney_Disease", "Cerebrovascular_Disease", "Heart_Disease",
                 "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                 "EKG_Findings", "Communicable_Disease"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_jsl_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_findings", "en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("snomed_code")

snomed_pipeline = Pipeline(stages = [
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_jsl,
    ner_jsl_converter,
    chunk2doc,
    sbert_embedder,
    snomed_resolver
])


sample_text = """The patient exhibited recurrent upper respiratory tract infections, subjective fevers, weight loss, and  night sweats. Clinically, they appeared cachectic and with  hepatosplenomegaly. Laboratory results confirmed pancytopenia."""

df= spark.createDataFrame([[sample_text]]).toDF("text")

result= nlpPipeline.fit(df).transform(df)

```

{:.jsl-block}
```python


documentAssembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
      .setInputCols(["document"])\
      .setOutputCol("sentence")

tokenizer = nlp.Tokenizer() \
      .setInputCols(["sentence"]) \
      .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en", "clinical/models")\
      .setInputCols(["sentence", "token"])\
      .setOutputCol("embeddings")

ner_jsl = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models") \
      .setInputCols(["sentence", "token", "embeddings"]) \
      .setOutputCol("ner_jsl")

ner_jsl_converter   = medical.NerConverterInternal()\
      .setInputCols(["sentence", "token", "ner_jsl"])\
      .setOutputCol("ner_jsl_chunk")\
      .setWhiteList(["Kidney_Disease", "Cerebrovascular_Disease", "Heart_Disease",
                 "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                 "EKG_Findings", "Communicable_Disease"])

chunk2doc = nlp.Chunk2Doc() \
      .setInputCols("ner_jsl_chunk") \
      .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
     .setInputCols(["ner_chunk_doc"])\
     .setOutputCol("sbert_embeddings")\
     .setCaseSensitive(False)

snomed_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_findings", "en", "clinical/models") \
     .setInputCols(["sbert_embeddings"]) \
     .setOutputCol("snomed_code")\
     .setDistanceFunction("EUCLIDEAN")

nlpPipeline= nlp.Pipeline(stages = [
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

sample_text = """The patient exhibited recurrent upper respiratory tract infections, subjective fevers, weight loss, and  night sweats. Clinically, they appeared cachectic and with  hepatosplenomegaly. Laboratory results confirmed pancytopenia."""

df= spark.createDataFrame([[sample_text]]).toDF("text")

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
  .setWhiteList(["Kidney_Disease", "Cerebrovascular_Disease", "Heart_Disease",
                 "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                 "EKG_Findings", "Communicable_Disease"])

val chunk2doc = new Chunk2Doc()
  .setInputCols(Array("ner_jsl_chunk"))
  .setOutputCol("ner_chunk_doc")

val sbertEmbedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("sbert_embeddings")
  .setCaseSensitive(false)

val snomedResolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_findings", "en", "clinical/models")
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


val sample_text = """The patient exhibited recurrent upper respiratory tract infections, subjective fevers, weight loss, and  night sweats. Clinically, they appeared cachectic and with  hepatosplenomegaly. Laboratory results confirmed pancytopenia."""

val df= Seq(sample_text).toDF("text")

val result= nlpPipeline.fit(df).transform(df)

```
</div>

## Results

```bash

| sent_id | ner_chunk                          | entity                    | snomed_code | resolution                        | all_codes                                          | all_resolutions                                    |
|---------|------------------------------------|---------------------------|-------------|-----------------------------------|----------------------------------------------------|----------------------------------------------------|
| 0       | upper respiratory tract infections | Disease_Syndrome_Disorder | 413585005   | aspiration into respiratory tract | ['413585005', '301186004', '422376000', '301273... | ['aspiration into respiratory tract', 'upper re... |
| 0       | fevers                             | VS_Finding                | 386661006   | fever                             | ['386661006', '77957000', '52715007', '27175100... | ['fever', 'intermittent fever', 'cyclic fever',... |
| 0       | weight loss                        | Symptom                   | 416528001   | intentional weight loss           | ['416528001', '448765001', '267024001', '359649... | ['intentional weight loss', 'involuntary weight... |
| 0       | night sweats                       | Symptom                   | 42984000    | night sweats                      | ['42984000', '423052008', '36163009', '10254900... | ['night sweats', 'frequent night waking', 'nigh... |
| 1       | cachectic                          | Symptom                   | 238108007   | cachectic                         | ['238108007', '422003001', '284529003', '788876... | ['cachectic', 'cachexia associated with aids', ... |
| 1       | hepatosplenomegaly                 | Symptom                   | 94701003    | mottled spleen                    | ['94701003', '169149008', '124961001', '1666430... | ['mottled spleen', 'isotope scan spleen abnorma... |
| 2       | pancytopenia                       | Symptom                   | 124961001   | reticulocytopenia                 | ['124961001', '415116008', '721119004', '165517... | ['reticulocytopenia', 'thrombocytopenia', 'pseu... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_findings|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|183.0 MB|
|Case sensitive:|false|
