---
layout: model
title: Sentence Entity Resolver for SNOMED Codes (Spanish) - Augmented (sent_xlm_roberta_biolord_2023_m embeddings)
author: John Snow Labs
name: biolordresolve_snomed_augmented
date: 2025-02-14
tags: [es, licensed, biolord, xlm_roberta, snomed, enetity_resolution, clinical]
task: Entity Resolution
language: es
edition: Healthcare NLP 5.5.2
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps Spanish medical entities and concepts to SNOMED codes using the `sent_xlm_roberta_biolord_2023_m` Sentence Embeddings.

## Predicted Entities

`SNOMED codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_snomed_augmented_es_5.5.2_3.0_1739549427571.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_snomed_augmented_es_5.5.2_3.0_1739549427571.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols(["sentence"])\
  .setOutputCol("token")\

word_embeddings = nlp.WordEmbeddingsModel.pretrained("w2v_cc_300d","es")\
	  .setInputCols(["sentence","token"])\
	  .setOutputCol("embeddings")

ner_eu = medical.NerModel.pretrained("ner_eu_clinical_condition", "es", "clinical/models") \
  .setInputCols(["sentence", "token", "embeddings"]) \
  .setOutputCol("ner_eu")

ner_eu_converter = medical.NerConverterInternal() \
  .setInputCols(["sentence", "token", "ner_eu"]) \
  .setOutputCol("ner_eu_chunk")

chunk2doc = nlp.Chunk2Doc()\
  .setInputCols("ner_eu_chunk")\
  .setOutputCol("ner_chunk_doc")

biolord_embeddings = nlp.XlmRoBertaSentenceEmbeddings.pretrained("sent_xlm_roberta_biolord_2023_m","xx")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("biolord_embeddings")

snomed_resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_snomed_augmented","es", "clinical/models") \
      .setInputCols(["biolord_embeddings"]) \
      .setOutputCol("snomed_code")\
      .setDistanceFunction("EUCLIDEAN")

snomed_pipeline = Pipeline(stages = [
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_eu,
    ner_eu_converter,
    chunk2doc,
    biolord_embeddings,
    snomed_resolver
])


clinical_note = ("La paciente, con antecedente de diabetes mellitus gestacional evolucionada a tipo 2 y obesidad, presenta vómitos de una semana de evolución junto con dolorosa inflamación de sínfisis de pubis que dificulta la deambulación.")

data = spark.createDataFrame([[clinical_note]]).toDF("text")

snomed_result = snomed_pipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel
  .pretrained("sentence_detector_dl", "xx")
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel
  .pretrained("w2v_cc_300d", "es")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val nerEu = MedicalNerModel
  .pretrained("ner_eu_clinical_condition", "es", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner_eu")

val nerEuConverter = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner_eu"))
  .setOutputCol("ner_eu_chunk")

val chunk2doc = new Chunk2Doc()
  .setInputCols(Array("ner_eu_chunk"))
  .setOutputCol("ner_chunk_doc")

val biolordEmbeddings = XlmRoBertaSentenceEmbeddings
  .pretrained("sent_xlm_roberta_biolord_2023_m", "xx")
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("biolord_embeddings")

val snomedResolver = SentenceEntityResolverModel
  .pretrained("biolordresolve_snomed_augmented", "es", "clinical/models")
  .setInputCols(Array("biolord_embeddings"))
  .setOutputCol("snomed_code")
  .setDistanceFunction("EUCLIDEAN")

val snomedPipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  wordEmbeddings,
  nerEu,
  nerEuConverter,
  chunk2doc,
  biolordEmbeddings,
  snomedResolver
))


val clinicalNote = Seq("La paciente, con antecedente de diabetes mellitus gestacional evolucionada a tipo 2 y obesidad, presenta vómitos de una semana de evolución junto con dolorosa inflamación de sínfisis de pubis que dificulta la deambulación.").toDF("text")
val snomedResult = snomedPipeline.fit(clinicalNote).transform(clinicalNote)

```
</div>

## Results

```bash
|    | ner_chunk                     | entity             |   snomed_code | resolutions                                                   | all_codes                                                                             | all_resolutions                                                                                                                                                                  |
|---:|:------------------------------|:-------------------|--------------:|:--------------------------------------------------------------|:--------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | diabetes mellitus gestacional | clinical_condition |      11687002 | diabetes mellitus gestacional [diabetes mellitus gestacional] | ['11687002', '40801000119106', '16896421000119107', '721151003', '10753491000119101...| ['diabetes mellitus gestacional [diabetes mellitus gestacional]', 'diabetes mellitus gestacional que complica el embarazo [diabetes mellitus gestacional que complica el embar...|
|  1 | obesidad                      | clinical_condition |     414916001 | obesidad [obesidad]                                           | ['414916001', '414915002', '271590003', '414919008', '363247006', '238136002', '238...| ['obesidad [obesidad]', 'obeso [obeso]', 'constitución obesa [constitución obesa]', 'obesidad según factores contribuyentes [obesidad según factores contribuyentes]', 'enferm...|
|  2 | vómitos                       | clinical_condition |     422400008 | vómitos [vómitos]                                             | ['422400008', '249497008', '23971007', '16932000', '8579004', '300359004', '4225870...| ['vómitos [vómitos]', 'síntoma de vómito [síntoma de vómito]', 'vómito agudo [vómito agudo]', 'náuseas y vómitos [náuseas y vómitos]', 'vómito en chorro [vómito en chorro]', ...|
|  3 | dolorosa                      | clinical_condition |      71393004 | dolorimiento [dolorimiento]                                   | ['71393004', '22253000', '301371003', '102498003', '67849003', '6617009', '27909700...| ['dolorimiento [dolorimiento]', 'dolor [dolor]', 'dolor que corroe [dolor que corroe]', 'agonía [agonía]', 'dolor atroz (hallazgo) [dolor atroz]', 'sinalgia [sinalgia]', 'dol...|
|  4 | inflamación                   | clinical_condition |     128139000 | enfermedad inflamatoria [enfermedad inflamatoria]             | ['128139000', '409774005', '4532008', '733935006', '708039003', '363170005', '65761...| ['enfermedad inflamatoria [enfermedad inflamatoria]', 'morfología inflamatoria [morfología inflamatoria]', 'inflamación activa [inflamación activa]', 'parainflamación [parain...|
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_snomed_augmented|
|Compatibility:|Healthcare NLP 5.5.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[umls_code]|
|Language:|es|
|Size:|2.4 GB|
|Case sensitive:|true|

## References

This model is trained with the National Library of Medicine (NLM), September 2024 SNOMED CT Spanish Edition.