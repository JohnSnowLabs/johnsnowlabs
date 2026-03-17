---
layout: model
title: Sentence Entity Resolver for SNOMED (sbiobertresolve_snomed_findings_aux_concepts)
author: John Snow Labs
name: sbiobertresolve_snomed_findings_aux_concepts
date: 2026-03-16
tags: [en, snomed, resolver, licensed, clinical, findings, auxconcepts]
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

This model maps clinical conditions to their corresponding SNOMED codes using sbiobert_base_cased_mli Sentence Bert Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/05.0.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_findings_aux_concepts_en_6.3.0_3.4_1773620938102.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_findings_aux_concepts_en_6.3.0_3.4_1773620938102.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_findings_aux_concepts", "en", "clinical/models") \
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

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
     .setInputCols(["ner_chunk_doc"])\
     .setOutputCol("sbert_embeddings")\
     .setCaseSensitive(False)

snomed_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_findings_aux_concepts", "en", "clinical/models") \
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
  .setWhiteList(Array("Procedure","Kidney_Disease","Cerebrovascular_Disease","Heart_Disease",
                     "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                     "EKG_Findings", "Communicable_Disease","Substance","Drug_Ingredient",
                     "Internal_organ_or_component","External_body_part_or_region","Modifier",
                     "Triglycerides","Alcohol","Smoking","Pregnancy","Hypertension","Obesity",
                     "Injury_or_Poisoning","Test","Hyperlipidemia","BMI","Oncological","Psychological_Condition","LDL","Diabetes"))

val chunk2doc = new Chunk2Doc()
  .setInputCols(Array("ner_jsl_chunk"))
  .setOutputCol("ner_chunk_doc")

val sbertEmbedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("sbert_embeddings")
  .setCaseSensitive(false)

val snomedResolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_findings_aux_concepts", "en", "clinical/models")
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


val sample_text = """This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction. He was subsequently transferred to the CCU for close monitoring. He was hemodynamically stable at the time of admission to the CCU."""

val df= Seq(sample_text).toDF("text")

val result= nlpPipeline.fit(df).transform(df)

```
</div>

## Results

```bash

| sent_id | ner_chunk                                          | entity                    | snomed_code | resolution                                         | all_codes                                          | all_resolutions                                    | aux_list                                           |
|---------|----------------------------------------------------|---------------------------|-------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|
| 0       | tobacco                                            | Smoking                   | 57264008    | tobacco                                            | ['57264008', '102407002', '39953003', '11048300... | ['tobacco', 'tobacco smoke', 'tobacco - substan... | ['Organism', 'Substance', 'Substance', 'Clinica... |
| 0       | hypertension                                       | Hypertension              | 38341003    | hypertension                                       | ['38341003', '417312002', '59621000', '27044000... | ['hypertension', 'hypertension suspected', 'ess... | ['Disorder', 'Context-dependent', 'Disorder', '... |
| 0       | chronic renal insufficiency                        | Kidney_Disease            | 723190009   | chronic renal insufficiency                        | ['723190009', '709044004', '90688005', '4253690... | ['chronic renal insufficiency', 'chronic renal ... | ['Disorder', 'Disorder', 'Disorder', 'Disorder'... |
| 0       | COPD                                               | Disease_Syndrome_Disorder | 13645005    | copd                                               | ['13645005', '414400006', '223821008', '6034900... | ['copd', 'coning', 'cos', 'ump', 'ling', 'chive... | ['Disorder', 'Disorder', 'Location', 'Substance... |
| 0       | gastritis                                          | Disease_Syndrome_Disorder | 4556007     | gastritis                                          | ['4556007', '413241009', '235656001', '10867910... | ['gastritis', 'gastritis suspected', 'chemical ... | ['Disorder', 'Context-dependent', 'Disorder', '... |
| 0       | TIA                                                | Cerebrovascular_Disease   | 266257000   | tia                                                | ['266257000', '31597007', '160363004', '3961450... | ['tia', 'tui', 'fh: tia', 'tidac', 'tu', 'trna'... | ['Disorder', 'Organism', 'Context-dependent', '... |
| 1       | nonspecific                                        | Modifier                  | 10003008    | non-specific                                       | ['10003008', '261992003', '863956004', '3008440... | ['non-specific', 'non-biological', 'non-sterile... | ['Qualifier Value', 'Qualifier Value', 'Qualifi... |
| 1       | ST-T abnormality                                   | EKG_Findings              | 428750005   | nonspecific st-t abnormality                       | ['428750005', '399504009', '55930002', '4557210... | ['nonspecific st-t abnormality', 'clinical t ca... | ['Clinical Finding', 'Observable Entity', 'Clin... |
| 2       | cardiac catheterization                            | Procedure                 | 41976001    | cardiac catheterization                            | ['41976001', '705923009', '721968000', '4677350... | ['cardiac catheterization', 'cardiac catheter',... | ['Procedure', 'Physical Object', 'Record Artifa... |
| 2       | occlusion of the mid left anterior descending c... | Symptom                   | 840313007   | occlusion of mid left anterior descending coron... | ['840313007', '44771000087108', '840315000', '4... | ['occlusion of mid left anterior descending cor... | ['Disorder', 'Disorder', 'Disorder', 'Disorder'... |
| 2       | hypotension                                        | VS_Finding                | 45007003    | hypotension                                        | ['45007003', '241727003', '19721008', '28651003... | ['hypotension', 'induced hypotension', 'globe h... | ['Disorder', 'Procedure', 'Disorder', 'Disorder... |
| 2       | bradycardia                                        | VS_Finding                | 48867003    | bradycardia                                        | ['48867003', '49710005', '44273001', '42177007'... | ['bradycardia', 'sinus bradycardia', 'reflex br... | ['Clinical Finding', 'Disorder', 'Clinical Find... |
| 3       | atropine                                           | Drug_Ingredient           | 73949004    | atropine                                           | ['73949004', '105075009', '349945006', '4104930... | ['atropine', 'atropine measurement', 'oral atro... | ['Pharma/Biol Product', 'Procedure', 'Clinical ... |
| 3       | fluids                                             | Drug_Ingredient           | 255765007   | fluid                                              | ['255765007', '246498002', '258442002', '251851... | ['fluid', 'fluid used', 'fluid sample', 'fluid ... | ['Qualifier Value', 'Attribute', 'Specimen', 'O... |
| 3       | dopamine                                           | Drug_Ingredient           | 59187003    | dopamine                                           | ['59187003', '412383006', '37484001', '32779004... | ['dopamine', 'dopamine agent', 'dopamine recept... | ['Pharma/Biol Product', 'Substance', 'Substance... |
| 3       | vagal reaction                                     | Symptom                   | 128968000   | vagal stimulation                                  | ['128968000', '398665005', '106160007', '888820... | ['vagal stimulation', 'vaso vagal episode', 'va... | ['Procedure', 'Clinical Finding', 'Clinical Fin... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_findings_aux_concepts|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|2.3 GB|
|Case sensitive:|false|
