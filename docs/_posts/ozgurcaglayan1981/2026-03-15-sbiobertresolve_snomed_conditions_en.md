---
layout: model
title: Sentence Entity Resolver for SNOMED (sbiobertresolve_snomed_conditions)
author: John Snow Labs
name: sbiobertresolve_snomed_conditions
date: 2026-03-15
tags: [en, snomed, resolver, licensed, clinical, conditions]
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

This model maps clinical conditions to their corresponding SNOMED (domain: Conditions) codes using sbiobert_base_cased_mli Sentence Bert Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/05.0.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_conditions_en_6.3.0_3.4_1773616386212.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_conditions_en_6.3.0_3.4_1773616386212.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")


ner_jsl_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Kidney_Disease", "Cerebrovascular_Disease", "Heart_Disease","Disease_Syndrome_Disorder",
                  "ImagingFindings", "Symptom", "VS_Finding","EKG_Findings", "Communicable_Disease","Pregnancy",
                  "Obesity","Hypertension","Overweight","Hyperlipidemia","Triglycerides","Diabetes","Oncological",
                  "Psychological_Condition","ImagingFindings","Injury_or_Poisoning"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_conditions", "en", "clinical/models") \
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


sample_text = """Medical professionals rushed in the bustling emergency room to attend to the patient with alarming symptoms.
            The attending physician immediately noted signs of respiratory distress, including stridor, a high-pitched sound indicative of upper respiratory tract obstruction.
            The patient, struggling to breathe, exhibited dyspnea. Concern heightened when they began experiencing syncope,
            a sudden loss of consciousness likely stemming from inadequate oxygenation. Further examination revealed a respiratory tract hemorrhage."""

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
      .setOutputCol("ner")

ner_jsl_converter = medical.NerConverterInternal()\
      .setInputCols(["sentence", "token", "ner"])\
      .setOutputCol("ner_chunk")\
      .setWhiteList(["Kidney_Disease", "Cerebrovascular_Disease", "Heart_Disease","Disease_Syndrome_Disorder",
                  "ImagingFindings", "Symptom", "VS_Finding","EKG_Findings", "Communicable_Disease","Pregnancy",
                  "Obesity","Hypertension","Overweight","Hyperlipidemia","Triglycerides","Diabetes","Oncological",
                  "Psychological_Condition","ImagingFindings","Injury_or_Poisoning"])

chunk2doc = nlp.Chunk2Doc() \
      .setInputCols("ner_chunk") \
      .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
     .setInputCols(["ner_chunk_doc"])\
     .setOutputCol("sbert_embeddings")\
     .setCaseSensitive(False)

snomed_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_conditions", "en", "clinical/models") \
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

sample_text = """"Medical professionals rushed in the bustling emergency room to attend to the patient with alarming symptoms.
            The attending physician immediately noted signs of respiratory distress, including stridor, a high-pitched sound indicative of upper respiratory tract obstruction.
            The patient, struggling to breathe, exhibited dyspnea. Concern heightened when they began experiencing syncope,
            a sudden loss of consciousness likely stemming from inadequate oxygenation. Further examination revealed a respiratory tract hemorrhage."""

df= spark.createDataFrame([[sample_text]]).toDF("text")

result= nlpPipeline.fit(df).transform(df)


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
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Kidney_Disease", "Cerebrovascular_Disease", "Heart_Disease","Disease_Syndrome_Disorder",
                  "ImagingFindings", "Symptom", "VS_Finding","EKG_Findings", "Communicable_Disease","Pregnancy",
                  "Obesity","Hypertension","Overweight","Hyperlipidemia","Triglycerides","Diabetes","Oncological",
                  "Psychological_Condition","ImagingFindings","Injury_or_Poisoning"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(False)

val snomed_resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_snomed_conditions", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val nlpPipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentenceDetectorDL,
    tokenizer,
    word_embeddings,
    ner_jsl,
    ner_jsl_converter,
    chunk2doc,
    sbert_embedder,
    snomed_resolver))


val sample_text = """The patient is a 30-year-old female with a long history of insulin-dependent diabetes, type 2; coronary artery disease; chronic renal insufficiency; peripheral vascular disease, also secondary to diabetes; who was originally admitted to an outside hospital for what appeared to be acute paraplegia, lower extremities. She did receive a course of Bactrim for 14 days for UTI."""

val df= Seq(sample_text).toDF("text")

val result= nlpPipeline.fit(df).transform(df)

```
</div>

## Results

```bash

| sent_id | ner_chunk                           | entity                    | snomed_code | resolutions                         | all_codes                                          | all_resolutions                                    |
|---------|-------------------------------------|---------------------------|-------------|-------------------------------------|----------------------------------------------------|----------------------------------------------------|
| 1       | respiratory distress                | VS_Finding                | 271825005   | respiratory distress                | ['271825005', '418092006', '75483001', '3738950... | ['respiratory distress', 'respiratory tract con... |
| 1       | stridor                             | Symptom                   | 70407001    | stridor                             | ['70407001', '301826004', '58596002', '30128700... | ['stridor', 'intermittent stridor', 'inhalatory... |
| 1       | high-pitched sound                  | Symptom                   | 271661003   | heart sounds exaggerated            | ['271661003', '405495005', '300211002', '248615... | ['heart sounds exaggerated', 'high airway press... |
| 1       | upper respiratory tract obstruction | Disease_Syndrome_Disorder | 68372009    | upper respiratory tract obstruction | ['68372009', '79688008', '73342002', '301252002... | ['upper respiratory tract obstruction', 'respir... |
| 2       | struggling to breathe               | Symptom                   | 230145002   | difficulty breathing                | ['230145002', '289116005', '386813002', '271825... | ['difficulty breathing', 'difficulty coughing',... |
| 2       | dyspnea                             | Symptom                   | 267036007   | dyspnea                             | ['267036007', '60845006', '25209001', '34560001... | ['dyspnea', 'exertional dyspnea', 'inspiratory ... |
| 3       | syncope                             | Symptom                   | 271594007   | syncope                             | ['271594007', '234167006', '90129003', '4455350... | ['syncope', 'situational syncope', 'tussive syn... |
| 3       | loss of consciousness               | Symptom                   | 44077006    | loss of sensation                   | ['44077006', '249845008', '68158006', '24656200... | ['loss of sensation', 'loss of sense of positio... |
| 3       | inadequate oxygenation              | Symptom                   | 238161004   | impaired oxygen delivery            | ['238161004', '70944005', '238162006', '1238260... | ['impaired oxygen delivery', 'impaired gas exch... |
| 4       | respiratory tract hemorrhage        | Disease_Syndrome_Disorder | 95431003    | respiratory tract hemorrhage        | ['95431003', '233783005', '15238002', '78144005... | ['respiratory tract hemorrhage', 'tracheal hemo... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_conditions|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|593.3 MB|
|Case sensitive:|false|
