---
layout: model
title: Sentence Entity Resolver for ICD10GM Codes (German) - Augmented (sent_xlm_roberta_biolord_2023_m embeddings)
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

This model maps Spanish medical entities and concepts to ICD10GM codes using the `sent_xlm_roberta_biolord_2023_m` Sentence Embeddings.

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

text = """Patient: 67-jährige weibliche Patientin
Diagnose: Invasives duktales Karzinom der linken Brust
Klinische Präsentation:
Die Patientin stellte sich mit einer schmerzlosen, palpablen Verhärtung im oberen äußeren Quadranten der linken Brust vor. Zudem berichtete sie über eine leichte Rötung der Haut sowie eine eingezogene Mamille. Axilläre Lymphknoten waren bei der klinischen Untersuchung tastbar vergrößert.

Histopathologie:
Die Biopsie ergab ein invasives duktales Karzinom (G3) mit positiven Hormonrezeptoren (ER+, PR+). HER2/neu-Expression war negativ. Der Ki-67-Proliferationsindex lag bei 35 %.

Bildgebung:

Mammographie: 2,8 cm große suspekte Läsion in der linken Brust mit Mikroverkalkungen
MRT: Tumorausdehnung 3,1 cm mit Infiltration des Drüsengewebes
PET-CT: Kein Anhalt für Fernmetastasen
Therapieempfehlung:

Neoadjuvante Chemotherapie (EC-T Schema)
Anschließend brusterhaltende Operation mit Sentinel-Lymphknotenbiopsie
Adjuvante Strahlentherapie
Hormontherapie mit Letrozol für 5 Jahre
Beurteilung:
Fortgeschrittenes, aber lokalisierbares Mammakarzinom mit günstigem Hormonrezeptorstatus. Therapie gemäß interdisziplinärer Tumorkonferenz empfohlen.
"""

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

text = """Patient: 67-jährige weibliche Patientin
Diagnose: Invasives duktales Karzinom der linken Brust
Klinische Präsentation:
Die Patientin stellte sich mit einer schmerzlosen, palpablen Verhärtung im oberen äußeren Quadranten der linken Brust vor. Zudem berichtete sie über eine leichte Rötung der Haut sowie eine eingezogene Mamille. Axilläre Lymphknoten waren bei der klinischen Untersuchung tastbar vergrößert.

Histopathologie:
Die Biopsie ergab ein invasives duktales Karzinom (G3) mit positiven Hormonrezeptoren (ER+, PR+). HER2/neu-Expression war negativ. Der Ki-67-Proliferationsindex lag bei 35 %.

Bildgebung:

Mammographie: 2,8 cm große suspekte Läsion in der linken Brust mit Mikroverkalkungen
MRT: Tumorausdehnung 3,1 cm mit Infiltration des Drüsengewebes
PET-CT: Kein Anhalt für Fernmetastasen
Therapieempfehlung:

Neoadjuvante Chemotherapie (EC-T Schema)
Anschließend brusterhaltende Operation mit Sentinel-Lymphknotenbiopsie
Adjuvante Strahlentherapie
Hormontherapie mit Letrozol für 5 Jahre
Beurteilung:
Fortgeschrittenes, aber lokalisierbares Mammakarzinom mit günstigem Hormonrezeptorstatus. Therapie gemäß interdisziplinärer Tumorkonferenz empfohlen.
"""

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

val data = Seq("""Patient: 67-jährige weibliche Patientin
Diagnose: Invasives duktales Karzinom der linken Brust
Klinische Präsentation:
Die Patientin stellte sich mit einer schmerzlosen, palpablen Verhärtung im oberen äußeren Quadranten der linken Brust vor. Zudem berichtete sie über eine leichte Rötung der Haut sowie eine eingezogene Mamille. Axilläre Lymphknoten waren bei der klinischen Untersuchung tastbar vergrößert.

Histopathologie:
Die Biopsie ergab ein invasives duktales Karzinom (G3) mit positiven Hormonrezeptoren (ER+, PR+). HER2/neu-Expression war negativ. Der Ki-67-Proliferationsindex lag bei 35 %.

Bildgebung:

Mammographie: 2,8 cm große suspekte Läsion in der linken Brust mit Mikroverkalkungen
MRT: Tumorausdehnung 3,1 cm mit Infiltration des Drüsengewebes
PET-CT: Kein Anhalt für Fernmetastasen
Therapieempfehlung:

Neoadjuvante Chemotherapie (EC-T Schema)
Anschließend brusterhaltende Operation mit Sentinel-Lymphknotenbiopsie
Adjuvante Strahlentherapie
Hormontherapie mit Letrozol für 5 Jahre
Beurteilung:
Fortgeschrittenes, aber lokalisierbares Mammakarzinom mit günstigem Hormonrezeptorstatus. Therapie gemäß interdisziplinärer Tumorkonferenz empfohlen.
""").toDF("text")

val result_resolver = icd_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
| chunk                      | begin | end   | ner_label     | icd       | resolution                                                                                                              | all_resolution                                                                                                                                                                                          | all_result                                                                            |
| -------------------------- | ----- | ----- | ------------- | --------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Karzinom der linken Brust  | 69    | 93    | Cancer_Dx     | C50       | Karzinom der Brustdrüse [Bösartige Neubildung der Brustdrüse [Mamma]]                                                   | Karzinom der Brustdrüse [Bösartige Neubildung der Brustdrüse [Mamma]]:::Krebs in der Brustdrüse, nicht näher klassifiziert [Brustdrüse, nicht näher bezeichnet]:::Mammakarzinom [Brustdrüse [Mamma]]... | C50:::C50.9:::D48.6:::C50.5:::Z80.3:::C76.1                                           |
| Karzinom                   | 467   | 474   | Cancer_Dx     | C80.9     | Bösartige Geschwulst, nicht näher klassifiziert [Bösartige Neubildung, nicht näher bezeichnet]                          | Bösartige Geschwulst, nicht näher klassifiziert [Bösartige Neubildung, nicht näher bezeichnet]:::Bösartige Neubildung, Ort nicht angegeben [Bösartige Neubildung ohne Angabe der Lokalisation]:::Mal... | C80.9:::C80:::C76:::C80.0:::Z85.8:::C76.7                                             |
| Läsion                     | 651   | 656   | Tumor_Finding | T14.9     | Verletzung, ohne genaue Bezeichnung [Verletzung, nicht näher bezeichnet]                                                | Verletzung, ohne genaue Bezeichnung [Verletzung, nicht näher bezeichnet]:::offene Läsion [offen]:::Näher bezeichnete Verletzungen [Sonstige näher bezeichnete Verletzungen mit Beteiligung mehrerer ... | T14.9:::T08.1:::T06.8:::N00.9:::N00.8:::N02.1:::D36.7:::T07:::D36.9:::D36:::T14.01    |
| Tumorausdehnung            | 705   | 719   | Tumor_Finding | C76       | Krebsartige Veränderungen an ungenauen Stellen [Bösartige Neubildung sonstiger und ungenau bezeichneter Lokalisationen] | Krebsartige Veränderungen an ungenauen Stellen [Bösartige Neubildung sonstiger und ungenau bezeichneter Lokalisationen]:::Maligne Tumoren: Unpräzise Lokalisationen [Sonstige ungenau bezeichnete Lo... | C76:::C76.7:::C80.9:::C79:::C79.9:::C80.0:::C79.8:::D36.7:::D09.7:::Z12:::U62.0:::D09 |
| Adjuvante Strahlentherapie | 935   | 960   | Radiotherapy  | Z51.0     | Radiotherapie-Sitzung [Strahlentherapie-Sitzung]                                                                        | Radiotherapie-Sitzung [Strahlentherapie-Sitzung]:::Nachsorge nach Radiotherapie [Nachuntersuchung nach Strahlentherapie wegen anderer Krankheitszustände]:::Nachsorge nach Strahlentherapie bei mali... | Z51.0:::Z09.1:::Z08.1:::Z54.1:::Z51.82                                                |
| Mammakarzinom              | 1055  | 1067  | Cancer_Dx     | D48.6     | Mammakarzinom [Brustdrüse [Mamma]]                                                                                      | Mammakarzinom [Brustdrüse [Mamma]]:::Mamma-Karzinom [Bösartige Neubildung der Brustdrüse [Mamma]]:::Bösartige Mammaerkrankung [Bösartige Neubildung der Brustdrüse [Mamma] in der Familienanamnese]:... | D48.6:::C50:::Z80.3:::C50.9:::C76.1:::C50.5                                           |
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