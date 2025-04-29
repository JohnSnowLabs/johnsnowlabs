---
layout: model
title: Sentence Entity Resolver for ICD-10-GM Codes (German) - Augmented (sent_xlm_roberta_biolord_2023_m embeddings)
author: John Snow Labs
name: biolordresolve_icd10gm_augmented
date: 2025-02-28
tags: [licensed, de, biolord, xlm_roberta, icd10gm, entity_resolution, clinical]
task: Entity Resolution
language: de
edition: Healthcare NLP 5.5.2
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps German medical entities and concepts to ICD-10-GM codes using the `sent_xlm_roberta_biolord_2023_m` Sentence Embeddings.  It also returns the official resolution text within the brackets inside the metadata.

## Predicted Entities

`icd10gm code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_icd10gm_augmented_de_5.5.2_3.0_1740782131210.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_icd10gm_augmented_de_5.5.2_3.0_1740782131210.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d", "de", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_oncology_wip", "de", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Cancer_Dx", "Tumor_Finding", "Radiotherapy", "Immunotherapy", "Metastasis"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

biolord_embeddings = XlmRoBertaSentenceEmbeddings.pretrained("sent_xlm_roberta_biolord_2023_m","xx")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("biolord_embeddings")

icd_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_icd10gm_augmented", "de", "clinical/models") \
    .setInputCols(["biolord_embeddings"]) \
    .setOutputCol("icd_code")\
    .setDistanceFunction("EUCLIDEAN")

icd_pipeline = Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter,
    chunk2doc,
    biolord_embeddings,
    icd_resolver])

text = """Patientin: 67 Jahre, weiblich

Diagnose: Invasives duktales Mammakarzinom links (G3)

Histologie:

ER + , PR + , HER2-negativ, Ki-67 bei 35 %
Bildgebung:

Mammographie: Tumor 2,8 cm, Mikroverkalkungen
PET-CT: Keine Fernmetastasen
Therapie:

Neoadjuvante Chemotherapie
Brusterhaltende Operation mit Sentinel-Lymphknotenbiopsie
Adjuvante Strahlentherapie
Hormontherapie mit Letrozol (5 Jahre)
Beurteilung:
Fortgeschrittenes lokal begrenztes Mammakarzinom, günstiger Hormonrezeptorstatus. Therapie gemäß Tumorkonferenz empfohlen."""

data = spark.createDataFrame([[text]]).toDF("text")

result_resolver = icd_pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("w2v_cc_300d", "de", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained("ner_oncology_wip", "de", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Cancer_Dx", "Tumor_Finding", "Radiotherapy", "Immunotherapy", "Metastasis"])

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

biolord_embeddings = nlp.XlmRoBertaSentenceEmbeddings.pretrained("sent_xlm_roberta_biolord_2023_m","xx")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("biolord_embeddings")

icd_resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_icd10gm_augmented", "de", "clinical/models") \
    .setInputCols(["biolord_embeddings"]) \
    .setOutputCol("icd_code")\
    .setDistanceFunction("EUCLIDEAN")

icd_pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter,
    chunk2doc,
    biolord_embeddings,
    icd_resolver])

text = """Patientin: 67 Jahre, weiblich

Diagnose: Invasives duktales Mammakarzinom links (G3)

Histologie:

ER + , PR + , HER2-negativ, Ki-67 bei 35 %
Bildgebung:

Mammographie: Tumor 2,8 cm, Mikroverkalkungen
PET-CT: Keine Fernmetastasen
Therapie:

Neoadjuvante Chemotherapie
Brusterhaltende Operation mit Sentinel-Lymphknotenbiopsie
Adjuvante Strahlentherapie
Hormontherapie mit Letrozol (5 Jahre)
Beurteilung:
Fortgeschrittenes lokal begrenztes Mammakarzinom, günstiger Hormonrezeptorstatus. Therapie gemäß Tumorkonferenz empfohlen."""

data = spark.createDataFrame([[text]]).toDF("text")

result_resolver = icd_pipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d", "de", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_oncology_wip", "de", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Cancer_Dx", "Tumor_Finding", "Radiotherapy", "Immunotherapy", "Metastasis"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

biolord_embeddings = XlmRoBertaSentenceEmbeddings.pretrained("sent_xlm_roberta_biolord_2023_m","xx")
    .setInputCols("ner_chunk_doc")
    .setOutputCol("biolord_embeddings")

val icd_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_icd10gm_augmented", "de", "clinical/models")
    .setInputCols("biolord_embeddings")
    .setOutputCol("icd_code")
    .setDistanceFunction("EUCLIDEAN")

val icd_pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter,
    chunk2doc,
    biolord_embeddings,
    icd_resolver))

val data = Seq("""Patientin: 67 Jahre, weiblich

Diagnose: Invasives duktales Mammakarzinom links (G3)

Histologie:

ER + , PR + , HER2-negativ, Ki-67 bei 35 %
Bildgebung:

Mammographie: Tumor 2,8 cm, Mikroverkalkungen
PET-CT: Keine Fernmetastasen
Therapie:

Neoadjuvante Chemotherapie
Brusterhaltende Operation mit Sentinel-Lymphknotenbiopsie
Adjuvante Strahlentherapie
Hormontherapie mit Letrozol (5 Jahre)
Beurteilung:
Fortgeschrittenes lokal begrenztes Mammakarzinom, günstiger Hormonrezeptorstatus. Therapie gemäß Tumorkonferenz empfohlen.""").toDF("text")

val result_resolver = icd_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
|chunk                     |begin|end|ner_label    |icd  |resolution                                                                                              |all_resolution                                                                                                                                                                                                                                                                                                                                                                                                                         |all_result                                             |
|--------------------------|-----|---|-------------|-----|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
|Mammakarzinom links       |60   |78 |Cancer_Dx    |C50  |Brustdrüsenkarzinom [Bösartige Neubildung der Brustdrüse [Mamma]]                                       |Brustdrüsenkarzinom [Bösartige Neubildung der Brustdrüse [Mamma]]:::Krebs in der Brustdrüse, nicht näher klassifiziert [Brustdrüse, nicht näher bezeichnet]:::Mammakarzinom [Brustdrüse [Mamma]]:::Neoplasma malignum: UQ der Brustdrüse [Unterer äußerer Quadrant der Brustdrüse]:::Bösartige Mammaerkrankung [Bösartige Neubildung der Brustdrüse [Mamma] in der Familienanamnese]:::Bösartige Tumoren der Brustregion [Thorax]      |C50:::C50.9:::D48.6:::C50.5:::Z80.3:::C76.1            |
|Tumor                     |169  |173|Tumor_Finding|D36.9|Neubildung ohne spezifische Lokalisation [Gutartige Neubildung an nicht näher bezeichneter Lokalisation]|Neubildung ohne spezifische Lokalisation [Gutartige Neubildung an nicht näher bezeichneter Lokalisation]:::Neubildung ohne spezifische Angaben zu Lokalisationen [Neubildung unsicheren oder unbekannten Verhaltens an sonstigen und nicht näher bezeichneten Lokalisationen]:::Neubildung unspezifischen Verhaltens, ohne weitere Angaben [Neubildung unsicheren oder unbekannten Verhaltens, nicht näher bezeichnet]:::Neubildung... |D36.9:::D48:::D48.9:::D48.7:::D36.7:::C80:::C80.9:::D36|
|Adjuvante Strahlentherapie|326  |351|Radiotherapy |Z51.0|Radiotherapie-Sitzung [Strahlentherapie-Sitzung]                                                        |Radiotherapie-Sitzung [Strahlentherapie-Sitzung]:::Nachsorge nach Radiotherapie [Nachuntersuchung nach Strahlentherapie wegen anderer Krankheitszustände]:::Nachsorge nach Strahlentherapie bei malignen Tumoren [Nachuntersuchung nach Strahlentherapie wegen bösartiger Neubildung]:::Rehabilitation nach Strahlentherapie [Rekonvaleszenz nach Strahlentherapie]:::Strahlen- und Chemotherapie bei bösartigen Tumoren...            |Z51.0:::Z09.1:::Z08.1:::Z54.1:::Z51.82                 |
|Mammakarzinom             |439  |451|Cancer_Dx    |D48.6|Mammakarzinom [Brustdrüse [Mamma]]                                                                      |Mammakarzinom [Brustdrüse [Mamma]]:::Mamma-Karzinom [Bösartige Neubildung der Brustdrüse [Mamma]]:::Bösartige Mammaerkrankung [Bösartige Neubildung der Brustdrüse [Mamma] in der Familienanamnese]:::Krebs in der Brustdrüse, nicht näher klassifiziert [Brustdrüse, nicht näher bezeichnet]:::Bösartige Tumoren der Brustregion [Thorax]:::Neoplasma malignum: UQ der Brustdrüse [Unterer äußerer Quadrant der Brustdrüse]           |D48.6:::C50:::Z80.3:::C50.9:::C76.1:::C50.5            |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_icd10gm_augmented|
|Compatibility:|Healthcare NLP 5.5.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[icd_code]|
|Language:|de|
|Size:|488.6 MB|
|Case sensitive:|true|
