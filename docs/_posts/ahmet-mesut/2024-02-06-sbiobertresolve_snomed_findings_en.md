---
layout: model
title: Sentence Entity Resolver for Snomed Concepts, Findings version (sbiobert_base_cased_mli embeddings)
author: John Snow Labs
name: sbiobertresolve_snomed_findings
date: 2024-02-06
tags: [en, licensed, resolver, findings, snomed]
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

The model maps extracted medical entities to their corresponding Snomed codes (Clinical Findings) using `sbiobert_base_cased_mli` BERT sentence embeddings.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_findings_en_5.2.1_3.0_1707244267455.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_findings_en_5.2.1_3.0_1707244267455.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

data = spark.createDataFrame([["""The patient exhibited recurrent upper respiratory tract infections, subjective fevers, weight loss, and  night sweats. Clinically, they appeared cachectic and with  hepatosplenomegaly. Laboratory results confirmed pancytopenia."""]]).toDF("text")

model = snomed_pipeline.fit(data)
result = model.transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
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

val nerJslConverter = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner_jsl"))
  .setOutputCol("ner_jsl_chunk")
  .setWhiteList(Array("Kidney_Disease", "Cerebrovascular_Disease", "Heart_Disease",
    "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
    "EKG_Findings", "Communicable_Disease"))

val chunk2doc = new Chunk2Doc()
  .setInputCols("ner_jsl_chunk")
  .setOutputCol("ner_chunk_doc")

val sbertEmbeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("sbert_embeddings")
  .setCaseSensitive(false)

val snomedResolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_findings", "en", "clinical/models")
  .setInputCols(Array("sbert_embeddings"))
  .setOutputCol("snomed_code")

val snomedPipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  wordEmbeddings,
  nerJsl,
  nerJslConverter,
  chunk2doc,
  sbertEmbeddings,
  snomedResolver
))

val data = Seq("""The patient exhibited recurrent upper respiratory tract infections, subjective fevers, weight loss, and  night sweats. Clinically, they appeared cachectic and with  hepatosplenomegaly. Laboratory results confirmed pancytopenia.""").toDF("text")

val model = snomedPipeline.fit(data)
val result = model.transform(data)

```
</div>

## Results

```bash
+----------------------------------+-------------------------+-----------+---------------------------------+--------------------------------------------------+--------------------------------------------------+
|                             chunk|                    label|snomed_code|                       resolution|                                         all_codes|                                   all_resolutions|
+----------------------------------+-------------------------+-----------+---------------------------------+--------------------------------------------------+--------------------------------------------------+
|upper respiratory tract infections|Disease_Syndrome_Disorder|   54150009|upper respiratory tract infection|54150009:::312118003:::54398005:::275498002:::1...|upper respiratory tract infection:::upper respi...|
|                            fevers|               VS_Finding|  386661006|                            fever|386661006:::77957000:::52715007:::12579009:::27...|fever:::intermittent fever:::cyclic fever:::per...|
|                       weight loss|                  Symptom|   89362005|                      weight loss|89362005:::416528001:::161832001:::426977000:::...|weight loss:::intentional weight loss:::losing ...|
|                      night sweats|                  Symptom|   42984000|                     night sweats|42984000:::67233009:::423052008:::36163009:::89...|night sweats:::night waking:::frequent night wa...|
|                         cachectic|                  Symptom|  238108007|                        cachectic|238108007:::422003001:::284529003:::788876001::...|cachectic:::cachexia associated with aids:::car...|
|                hepatosplenomegaly|                  Symptom|   36760000|               hepatosplenomegaly|36760000:::16294009:::19058002:::191382009:::80...|hepatosplenomegaly:::splenomegaly:::congestive ...|
|                      pancytopenia|                  Symptom|  127034005|                     pancytopenia|127034005:::736024007:::5876000:::124961001:::4...|pancytopenia:::drug induced pancytopenia:::panc...|
+----------------------------------+-------------------------+-----------+---------------------------------+--------------------------------------------------+--------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_findings|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|641.0 MB|
|Case sensitive:|false|