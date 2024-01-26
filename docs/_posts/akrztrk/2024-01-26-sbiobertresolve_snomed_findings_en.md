---
layout: model
title: Sentence Entity Resolver for Snomed Concepts, Findings version (sbiobert_base_cased_mli embeddings)
author: John Snow Labs
name: sbiobertresolve_snomed_findings
date: 2024-01-26
tags: [en, licenced, entity_resolution, clinical, snomed, findings, licensed]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.2.0
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The model maps extracted medical entities to their corresponding Snomed codes (Clinical Findings) using sbiobert_base_cased_mli BERT sentence embeddings.

## Predicted Entities

`Snomed Codes and their normalized definitions`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_findings_en_5.2.0_3.0_1706290095370.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_findings_en_5.2.0_3.0_1706290095370.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
  .setOutputCol("ner_jsl_chunk")\
  .setWhiteList(["Kidney_Disease", "Cerebrovascular_Disease", "Heart_Disease",
                 "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                 "EKG_Findings", "Communicable_Disease"])\

chunk2doc = Chunk2Doc()\
  .setInputCols("ner_jsl_chunk")\
  .setOutputCol("ner_chunk_doc")

sbert_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
  .setInputCols(["ner_chunk_doc"])\
  .setOutputCol("sbert_embeddings")\
  .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_findings", "en", "clinical/models") \
  .setInputCols(["sbert_embeddings"]) \
  .setOutputCol("snomed_code")\

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

 
text = """The patient exhibited recurrent upper respiratory tract infections, subjective fevers, unintentional weight loss, and occasional night sweats. Clinically, they appeared cachectic and pale, with notable hepatosplenomegaly. Laboratory results confirmed pancytopenia."""

data = spark.createDataFrame([[text]]).toDF("text")
 
model = snomed_pipeline.fit(data).transform(data)

```
```scala
val documentAssembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained()
      .setInputCols(Array("document"))
      .setOutputCol("sentence")

val tokenizer = new Tokenizer()
      .setInputCols(Array("sentence"))
      .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en", "clinical/models")
      .setInputCols(Array("sentence", "token"))
      .setOutputCol("embeddings")

val ner_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
      .setInputCols(Array("sentence", "token", "embeddings"))
      .setOutputCol("ner_jsl")

val ner_jsl_converter = new NerConverterInternal()
      .setInputCols(Array("sentence", "token", "clinical_ner"))
      .setOutputCol("ner_jsl_chunk")
      .setWhiteList(Array("Kidney_Disease", "Cerebrovascular_Disease", "Heart_Disease",
                 "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                 "EKG_Findings", "Communicable_Disease"))

val chunk2doc = new Chunk2Doc()
      .setInputCols("ner_jsl_chunk")
      .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
      .setInputCols("ner_chunk_doc")
      .setOutputCol("sbert_embeddings")

val snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_findings", "en", "clinical/models")
     .setInputCols(Array("sbert_embeddings"))
     .setOutputCol("snomed_code")

val new nlpPipeine().setStages(Array(documentAssembler,
                                    sentenceDetector,
                                    tokenizer,
                                    word_embeddings,
                                    ner_jsl_clinical,
                                    ner_jsl_converter,
                                    chunk2doc,
                                    sbert_embedder,
                                    snomed_resolver))
                                    

val text= """The patient exhibited recurrent upper respiratory tract infections, subjective fevers, unintentional weight loss, and occasional night sweats. Clinically, they appeared cachectic and pale, with notable hepatosplenomegaly. Laboratory results confirmed pancytopenia."""

val df = Seq(text).toDF(text)

val result= nlpPipeline.fit(df).transform(df)
```
</div>

## Results

```bash
|   |                          ner_chunk | begin | end |                 ner_label | snomed_code |                       description |                                       resolutions |
|--:|-----------------------------------:|------:|----:|--------------------------:|------------:|----------------------------------:|--------------------------------------------------:|
| 0 | upper respiratory tract infections |    32 |  65 | Disease_Syndrome_Disorder |    54150009 | upper respiratory tract infection | upper respiratory tract infection:::upper resp... |
| 1 |                             fevers |    79 |  84 |                VS_Finding |   248425001 |                             fever | fever:::fever:::intermittent fever:::fever sym... |
| 2 |          unintentional weight loss |    87 | 111 |                   Symptom |   448765001 |         unintentional weight loss | unintentional weight loss:::unexplained weight... |
| 3 |                       night sweats |   129 | 140 |                   Symptom |   161859009 |                      night sweats | night sweats:::night sweats:::night sweats:::n... |
| 4 |                          cachectic |   169 | 177 |                   Symptom |   238108007 |                         cachectic | cachectic:::cachexia:::aids with cachexia:::ca... |
| 5 |                               pale |   183 | 186 |                   Symptom |   274643008 |                              pale | pale:::pale color:::pale color:::pale complexi... |
| 6 |                 hepatosplenomegaly |   202 | 219 |                   Symptom |    36760000 |                hepatosplenomegaly | hepatosplenomegaly:::splenomegaly:::congestive... |
| 7 |                       pancytopenia |   251 | 262 |                   Symptom |   127034005 |                      pancytopenia | pancytopenia:::drug induced pancytopenia:::pan... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_findings|
|Compatibility:|Healthcare NLP 5.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|715.9 MB|
|Case sensitive:|false|

## References

This model is trained with the augmented version of NIH September 2023 SNOMED CT United States (US) Edition.