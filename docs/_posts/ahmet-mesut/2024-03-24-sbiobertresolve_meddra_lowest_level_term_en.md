---
layout: model
title: Sentence Entity Resolver for MedDRA LLT (Lowest Level Term)
author: John Snow Labs
name: sbiobertresolve_meddra_lowest_level_term
date: 2024-03-24
tags: [en, licensed, llt, meddra, resolver]
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

This model maps clinical terms to their corresponding MedDRA LLT (Lowest Level Term) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_meddra_lowest_level_term_en_5.3.0_3.0_1711295979685.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_meddra_lowest_level_term_en_5.3.0_3.0_1711295979685.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
	
```python
documentAssembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
      .setInputCols(["document"])\
      .setOutputCol("sentence")

tokenizer = Tokenizer()\
      .setInputCols(["sentence"])\
      .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en", "clinical/models")\
      .setInputCols(["sentence", "token"])\
      .setOutputCol("embeddings")

ner_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
      .setInputCols(["sentence", "token", "embeddings"])\
      .setOutputCol("ner_jsl")

ner_jsl_converter = NerConverter()\
      .setInputCols(["sentence", "token", "ner_jsl"])\
      .setOutputCol("ner_jsl_chunk")\
      .setWhiteList(["Procedure","Kidney_Disease","Cerebrovascular_Disease","Heart_Disease",
                     "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                     "EKG_Findings", "Communicable_Disease","Substance",
                     "Internal_organ_or_component","External_body_part_or_region","Modifier",
                     "Triglycerides","Alcohol","Smoking","Pregnancy","Hypertension","Obesity",
                     "Injury_or_Poisoning","Test","Hyperlipidemia","BMI","Oncological","Psychological_Condition","LDL","Diabetes"])

chunk2doc = Chunk2Doc() \
      .setInputCols("ner_jsl_chunk") \
      .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
     .setInputCols(["ner_chunk_doc"])\
     .setOutputCol("sbert_embeddings")\
     .setCaseSensitive(False)

meddra_resolver = SentenceEntityResolverModel.load("meddra_llt_model") \
     .setInputCols(["sbert_embeddings"]) \
     .setOutputCol("meddra_resolver")\
     .setDistanceFunction("EUCLIDEAN")

nlpPipeline= Pipeline(stages=[
                              documentAssembler,
                              sentenceDetector,
                              tokenizer,
                              word_embeddings,
                              ner_jsl,
                              ner_jsl_converter,
                              chunk2doc,
                              sbert_embedder,
                              meddra_resolver
])

text= """This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, chronic obstructive pulmonary disease, gastritis, and transient ischemic attack. He initially presented to Braintree with ST elevation and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of the left main coronary artery stenosis, which was complicated by hypotension and bradycardia."""

df= spark.createDataFrame([[text]]).toDF("text")

resolver_pipeline= nlpPipeline.fit(df)
result = resolver_pipeline.transform(df)
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

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
	.setInputCols(Array("sentence","token"))
	.setOutputCol("embeddings")

val ner_jsl = MedicalNerModel.pretrained("ner_jsl","en","clinical/models")
	.setInputCols(Array("sentence","token","embeddings"))
	.setOutputCol("ner_jsl")

val ner_jsl_converter = new NerConverter()
	.setInputCols(Array("sentence","token","ner_jsl"))
	.setOutputCol("ner_jsl_chunk")
	.setWhiteList(Array("Procedure","Kidney_Disease","Cerebrovascular_Disease","Heart_Disease", "Disease_Syndrome_Disorder","ImagingFindings","Symptom","VS_Finding", "EKG_Findings","Communicable_Disease","Substance", "Internal_organ_or_component","External_body_part_or_region","Modifier", "Triglycerides","Alcohol","Smoking","Pregnancy","Hypertension","Obesity", "Injury_or_Poisoning","Test","Hyperlipidemia","BMI","Oncological","Psychological_Condition","LDL","Diabetes"))

val chunk2doc = new Chunk2Doc()
	.setInputCols("ner_jsl_chunk")
	.setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
	.setInputCols(Array("ner_chunk_doc"))
	.setOutputCol("sbert_embeddings")
	.setCaseSensitive(false)

val meddra_resolver = new SentenceEntityResolverModel.load("meddra_llt_model")
	.setInputCols(Array("sbert_embeddings"))
	.setOutputCol("meddra_resolver")
	.setDistanceFunction("EUCLIDEAN")
 
nlpPipeline= new Pipeline().setStages(Array(
     documentAssembler,
     sentenceDetector,
     tokenizer,
     word_embeddings,
     ner_jsl,
     ner_jsl_converter,
     chunk2doc,
     sbert_embedder,
     meddra_resolver ))

text= """This is an 82-year-old male with a history of prior tobacco use,hypertension,chronic renal insufficiency,chronic obstructive pulmonary disease,gastritis,and transient ischemic attack. He initially presented to Braintree with ST elevation and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of the left main coronary artery stenosis,which was complicated by hypotension and bradycardia."""

df= Seq(text) .toDF("text") resolver_pipeline= nlpPipeline.fit(df)
val result = resolver_pipeline.transform(df)

```
</div>

## Results

```bash
+-------------------------------------+-------------------------+-----------+-------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
|                                chunk|                    label|meddra_code|                           resolution|                                                             all_codes|                                                       all_resolutions|                                                        all_aux_labels|
+-------------------------------------+-------------------------+-----------+-------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
|                              tobacco|                  Smoking|   10067622|                  tobacco interaction|10067622:::10086359:::10057581:::10082288:::10009180:::10048880:::1...|tobacco interaction:::tobaccoism:::tobacco user:::exposure to tobac...|10067622:::10057852:::10057581:::10082288:::10057581:::10057581:::1...|
|                         hypertension|             Hypertension|   10020772|                         hypertension|10020772:::10020790:::10088636:::10081425:::10015488:::10020775:::1...|hypertension:::hypertension secondary:::systemic hypertension:::art...|10020772:::10039834:::10020772:::10020772:::10015488:::10020772:::1...|
|          chronic renal insufficiency|           Kidney_Disease|   10050441|          chronic renal insufficiency|10050441:::10009122:::10009119:::10075441:::10038474:::10038444:::1...|chronic renal insufficiency:::chronic renal impairment:::chronic re...|10064848:::10062237:::10064848:::10072370:::10038435:::10064848:::1...|
|chronic obstructive pulmonary disease|Disease_Syndrome_Disorder|   10009033|chronic obstructive pulmonary disease|10009033:::10009032:::10009026:::10009025:::10025081:::10083002:::1...|chronic obstructive pulmonary disease:::chronic obstructive lung di...|10009033:::10009033:::10009033:::10009033:::10061877:::10061768:::1...|
|                            gastritis|Disease_Syndrome_Disorder|   10017853|                            gastritis|10017853:::10060703:::10076492:::10070814:::10088553:::10000769:::1...|gastritis:::verrucous gastritis:::antral gastritis:::corrosive gast...|10017853:::10017865:::10017853:::10070814:::10017853:::10017853:::1...|
|            transient ischemic attack|  Cerebrovascular_Disease|   10072760|            transient ischemic attack|10072760:::10044390:::10044391:::10072761:::10044375:::10044374:::1...|transient ischemic attack:::transient ischaemic attack:::transient ...|10044390:::10044390:::10044390:::10044390:::10044390:::10044390:::1...|
|              cardiac catheterization|                Procedure|   10048606|              cardiac catheterization|10048606:::10007527:::10054343:::10007815:::10053451:::10088292:::1...|cardiac catheterization:::cardiac catheterisation:::catheterization...|10007815:::10007815:::10007815:::10007815:::10053451:::10088292:::1...|
|   left main coronary artery stenosis|            Heart_Disease|   10090240|   left main coronary artery stenosis|10090240:::10072048:::10084343:::10011089:::10083430:::10011105:::1...|left main coronary artery stenosis:::left anterior descending coron...|10011089:::10011089:::10011086:::10011089:::10011089:::10011105:::1...|
|                          hypotension|               VS_Finding|   10021097|                          hypotension|10021097:::10021107:::10066331:::10066077:::10036433:::10049705:::1...|hypotension:::hypotensive:::arterial hypotension:::diastolic hypote...|10021097:::10021097:::10021097:::10066077:::10031127:::10021097:::1...|
|                          bradycardia|               VS_Finding|   10006093|                          bradycardia|10006093:::10040741:::10078310:::10064883:::10065585:::10085625:::1...|bradycardia:::sinus bradycardia:::central bradycardia:::reflex brad...|10006093:::10040741:::10078310:::10006093:::10029458:::10006093:::1...|
+-------------------------------------+-------------------------+-----------+-------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_meddra_lowest_level_term|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[meddra_code]|
|Language:|en|
|Size:|228.2 MB|
|Case sensitive:|false|
