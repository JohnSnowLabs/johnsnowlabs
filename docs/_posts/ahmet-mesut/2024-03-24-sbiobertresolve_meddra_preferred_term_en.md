---
layout: model
title: Sentence Entity Resolver for MedDRA PT (Preferred Term)
author: John Snow Labs
name: sbiobertresolve_meddra_preferred_term
date: 2024-03-24
tags: [en, licensed, meddra, pt, resolver]
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

This model maps clinical terms to their corresponding MedDRA PT (Preferred Term) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.  It also returns the MedDRA System Organ Classes (SOCs) of each MedDRA PT code in the `all_k_aux_labels` in the metadata.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_meddra_preferred_term_en_5.3.0_3.0_1711296670895.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_meddra_preferred_term_en_5.3.0_3.0_1711296670895.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

meddra_resolver = SentenceEntityResolverModel.load("sbiobertresolve_meddra_preferred_term") \
     .setInputCols(["sbert_embeddings"]) \
     .setOutputCol("meddra_pt_code")\
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

val meddra_resolver = new SentenceEntityResolverModel.load("sbiobertresolve_meddra_preferred_term")
	.setInputCols(Array("sbert_embeddings"))
	.setOutputCol("meddra_pt_code")
	.setDistanceFunction("EUCLIDEAN") nlpPipeline= new Pipeline().setStages(Array(
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
+-------------------------------------+-------------------------+---------------+-------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|                                chunk|                    label| meddra_pt_code|                           resolution|                                         all_codes|                                   all_resolutions|                                    all_aux_labels|
+-------------------------------------+-------------------------+---------------+-------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|                              tobacco|                  Smoking|       10067622|                  tobacco interaction|10067622:::10057581:::10082288:::10043903:::100...|tobacco interaction:::tobacco user:::exposure t...|10018065:::10041244:::10022117:::10037175:::100...|
|                         hypertension|             Hypertension|       10020772|                         hypertension|10020772:::10015488:::10039834:::10012758:::100...|hypertension:::essential hypertension:::seconda...|10047065:::10047065:::10047065:::10047065:::100...|
|          chronic renal insufficiency|           Kidney_Disease|       10038435|                        renal failure|10038435:::10062237:::10038428:::10050335:::100...|renal failure:::renal impairment:::renal disord...|10038359:::10038359:::10038359:::10038359:::100...|
|chronic obstructive pulmonary disease|Disease_Syndrome_Disorder|       10009033|chronic obstructive pulmonary disease|10009033:::10061877:::10089961:::10061768:::100...|chronic obstructive pulmonary disease:::obstruc...|10038738:::10038738:::10038738:::10038738:::100...|
|                            gastritis|Disease_Syndrome_Disorder|       10017853|                            gastritis|10017853:::10070814:::10008882:::10084296:::100...|gastritis:::corrosive gastritis:::chronic gastr...|10017947:::10022117:::10017947:::10017947:::100...|
|            transient ischemic attack|  Cerebrovascular_Disease|       10044390|           transient ischaemic attack|10044390:::10061256:::10008118:::10060840:::100...|transient ischaemic attack:::ischaemic stroke::...|10029205:::10029205:::10029205:::10029205:::100...|
|              cardiac catheterization|                Procedure|       10007815|              catheterisation cardiac|10007815:::10053451:::10088292:::10053438:::100...|catheterisation cardiac:::cardiac imaging proce...|10022891:::10022891:::10042613:::10022891:::100...|
|   left main coronary artery stenosis|            Heart_Disease|       10011089|             coronary artery stenosis|10011089:::10011105:::10078431:::10077334:::100...|coronary artery stenosis:::coronary ostial sten...|10007541:::10007541:::10007541:::10022117:::100...|
|                          hypotension|               VS_Finding|       10021097|                          hypotension|10021097:::10066077:::10062300:::10031127:::100...|hypotension:::diastolic hypotension:::procedura...|10047065:::10047065:::10022117:::10047065:::100...|
|                          bradycardia|               VS_Finding|       10006093|                          bradycardia|10006093:::10040741:::10078310:::10090651:::100...|bradycardia:::sinus bradycardia:::central brady...|10007541:::10007541:::10007541:::10007541:::100...|
+-------------------------------------+-------------------------+---------------+-------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_meddra_preferred_term|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[meddra_pt_code]|
|Language:|en|
|Size:|76.2 MB|
|Case sensitive:|false|


## References

This model is trained with the January 2024 (v27) release of ICD-10 to MedDRA Map dataset.

**To utilize this model, possession of a valid MedDRA license is requisite. If you possess one and wish to use this model, kindly contact us at support@johnsnowlabs.com.**
