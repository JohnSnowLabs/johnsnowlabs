---
layout: model
title: Sentence Entity Resolver for SNOMED (biolordresolve_snomed_findings_aux_concepts)
author: John Snow Labs
name: biolordresolve_snomed_findings_aux_concepts
date: 2026-03-16
tags: [en, snomed, biolord, resolver, licensed, clinical, findings, auxconcepts]
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

This model maps clinical entities and concepts to SNOMED codes using mpnet_embeddings_biolord_2023_c Sentence Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_snomed_findings_aux_concepts_en_6.3.0_3.4_1773693935983.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_snomed_findings_aux_concepts_en_6.3.0_3.4_1773693935983.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
      .setWhiteList(["Procedure","Kidney_Disease","Cerebrovascular_Disease","Heart_Disease",
                     "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                     "EKG_Findings", "Communicable_Disease","Substance","Drug_Ingredient",
                     "Internal_organ_or_component","External_body_part_or_region","Modifier",
                     "Triglycerides","Alcohol","Smoking","Pregnancy","Hypertension","Obesity",
                     "Injury_or_Poisoning","Test","Hyperlipidemia","BMI","Oncological","Psychological_Condition","LDL","Diabetes"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_jsl_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("mpnet_embeddings")\
    .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_snomed_findings_aux_concepts", "en", "clinical/models") \
    .setInputCols(["mpnet_embeddings"]) \
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


sample_text = """This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction. He was subsequently transferred to the CCU for close monitoring. He was hemodynamically stable at the time of admission to the CCU."""

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
      .setWhiteList(["Procedure","Kidney_Disease","Cerebrovascular_Disease","Heart_Disease",
                     "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                     "EKG_Findings", "Communicable_Disease","Substance","Drug_Ingredient",
                     "Internal_organ_or_component","External_body_part_or_region","Modifier",
                     "Triglycerides","Alcohol","Smoking","Pregnancy","Hypertension","Obesity",
                     "Injury_or_Poisoning","Test","Hyperlipidemia","BMI","Oncological","Psychological_Condition","LDL","Diabetes"])

chunk2doc = nlp.Chunk2Doc() \
      .setInputCols("ner_jsl_chunk") \
      .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("mpnet_embeddings")\
    .setCaseSensitive(False)

snomed_resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_snomed_findings_aux_concepts", "en", "clinical/models") \
     .setInputCols(["mpnet_embeddings"]) \
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

sample_text = """This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction. He was subsequently transferred to the CCU for close monitoring. He was hemodynamically stable at the time of admission to the CCU."""

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
  .setWhiteList(["Procedure","Kidney_Disease","Cerebrovascular_Disease","Heart_Disease",
                     "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                     "EKG_Findings", "Communicable_Disease","Substance","Drug_Ingredient",
                     "Internal_organ_or_component","External_body_part_or_region","Modifier",
                     "Triglycerides","Alcohol","Smoking","Pregnancy","Hypertension","Obesity",
                     "Injury_or_Poisoning","Test","Hyperlipidemia","BMI","Oncological","Psychological_Condition","LDL","Diabetes"])

val chunk2doc = new Chunk2Doc()
  .setInputCols(Array("ner_jsl_chunk"))
  .setOutputCol("ner_chunk_doc")

val sbertEmbedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")
    .setInputCols(["ner_chunk_doc"])
    .setOutputCol("mpnet_embeddings")
    .setCaseSensitive(False)

val snomedResolver = SentenceEntityResolverModel.pretrained("biolordresolve_snomed_findings_aux_concepts", "en", "clinical/models")
  .setInputCols(Array("mpnet_embeddings"))
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


val sample_text = """This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction. He was subsequently transferred to the CCU for close monitoring. He was hemodynamically stable at the time of admission to the CCU."""

val df= Seq(sample_text).toDF("text")

val result= nlpPipeline.fit(df).transform(df)

```
</div>

## Results

```bash

| sent_id | ner_chunk                                          | entity                    | snomed_code | resolution                                         | all_codes                                          | all_resolutions                                    | aux_list                                           |
|---------|----------------------------------------------------|---------------------------|-------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|
| 0       | tobacco                                            | Smoking                   | 57264008    | tobacco                                            | ['57264008', '159882006', '39953003', '10240700... | ['tobacco', 'tobacco processor', 'tobacco - sub... | ['Organism', 'Social Context', 'Substance', 'Su... |
| 0       | hypertension                                       | Hypertension              | 38341003    | hypertension                                       | ['38341003', '64715009', '59621000', '10725009'... | ['hypertension', 'hypertensive cardiovascular d... | ['Disorder', 'Disorder', 'Disorder', 'Disorder'... |
| 0       | chronic renal insufficiency                        | Kidney_Disease            | 425369003   | chronic progressive renal insufficiency            | ['425369003', '90688005', '709044004', '7231900... | ['chronic progressive renal insufficiency', 'ch... | ['Disorder', 'Disorder', 'Disorder', 'Disorder'... |
| 0       | COPD                                               | Disease_Syndrome_Disorder | 13645005    | copd                                               | ['13645005', '702839006', '195951007', '2704730... | ['copd', 'chronic obstructive pulmonary disease... | ['Disorder', 'Location', 'Disorder', 'Context-d... |
| 0       | gastritis                                          | Disease_Syndrome_Disorder | 4556007     | gastritis                                          | ['4556007', '50874004', '235656001', '196731005... | ['gastritis', 'nonerosive nonspecific gastritis... | ['Disorder', 'Disorder', 'Disorder', 'Disorder'... |
| 0       | TIA                                                | Cerebrovascular_Disease   | 266257000   | tia                                                | ['266257000', '161511000', '463921000124102', '... | ['tia', 'h/o: tia', 'tiamastus', 'fh: tia', 'tt... | ['Disorder', 'Context-dependent', 'Organism', '... |
| 1       | nonspecific                                        | Modifier                  | 278001007   | nonspecific site                                   | ['278001007', '10003008', '225413008', '2603900... | ['nonspecific site', 'non-specific', 'nominal o... | ['Body Structure', 'Qualifier Value', 'Procedur... |
| 1       | ST-T abnormality                                   | EKG_Findings              | 428750005   | nonspecific st-t abnormality                       | ['428750005', '428549008', '164930006', '164934... | ['nonspecific st-t abnormality', 'secondary st-... | ['Clinical Finding', 'Clinical Finding', 'Clini... |
| 2       | cardiac catheterization                            | Procedure                 | 41976001    | cardiac catheterization                            | ['41976001', '721968000', '40403005', '12895700... | ['cardiac catheterization', 'cardiac catheteris... | ['Procedure', 'Record Artifact', 'Procedure', '... |
| 2       | occlusion of the mid left anterior descending c... | Symptom                   | 840313007   | occlusion of mid left anterior descending coron... | ['840313007', '44771000087108', '1255266003', '... | ['occlusion of mid left anterior descending cor... | ['Disorder', 'Disorder', 'Disorder', 'Disorder'... |
| 2       | hypotension                                        | VS_Finding                | 45007003    | hypotension                                        | ['45007003', '67763001', '12763006', '945010001... | ['hypotension', 'hypotensive episode', 'finding... | ['Disorder', 'Disorder', 'Clinical Finding', 'D... |
| 2       | bradycardia                                        | VS_Finding                | 48867003    | bradycardia                                        | ['48867003', '42177007', '421869004', '69046100... | ['bradycardia', 'bradycardia - pulse', 'bradyar... | ['Clinical Finding', 'Clinical Finding', 'Disor... |
| 3       | atropine                                           | Drug_Ingredient           | 73949004    | atropine                                           | ['73949004', '74237004', '294076004', '34994500... | ['atropine', 'atropine sulfate', 'atropine alle... | ['Pharma/Biol Product', 'Substance', 'Clinical ... |
| 3       | fluids                                             | Drug_Ingredient           | 255765007   | fluid                                              | ['255765007', '264312008', '406142009', '441841... | ['fluid', 'liquid', 'type of fluid', 'watery fl... | ['Qualifier Value', 'Clinical Finding', 'Attrib... |
| 3       | dopamine                                           | Drug_Ingredient           | 59187003    | dopamine                                           | ['59187003', '412383006', '30581005', '41822200... | ['dopamine', 'dopamine agent', 'urine dopamine'... | ['Pharma/Biol Product', 'Substance', 'Procedure... |
| 3       | vagal reaction                                     | Symptom                   | 128968000   | vagal stimulation                                  | ['128968000', '386719008', '29894000', '2764860... | ['vagal stimulation', 'vasomotor reaction', 'va... | ['Procedure', 'Observable Entity', 'Disorder', ... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_snomed_findings_aux_concepts|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[mpnet_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|2.3 GB|
|Case sensitive:|false|