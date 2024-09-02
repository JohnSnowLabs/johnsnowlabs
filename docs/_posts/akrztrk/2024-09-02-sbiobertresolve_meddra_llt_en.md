---
layout: model
title: Sentence Entity Resolver for MedDRA LLT (Lowest Level Term)
author: John Snow Labs
name: sbiobertresolve_meddra_llt
date: 2024-09-02
tags: [licensed, en, llt, meddra, resolver]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.4.1
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_meddra_llt_en_5.4.1_3.0_1725297611629.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_meddra_llt_en_5.4.1_3.0_1725297611629.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
                     "Disease_Syndrome_Disorder", "Symptom", "VS_Finding",
                     "EKG_Findings", "Communicable_Disease",
                     "Internal_organ_or_component","External_body_part_or_region",
                     "Triglycerides","Alcohol","Smoking","Pregnancy","Hypertension","Obesity",
                     "Injury_or_Poisoning","Test","Hyperlipidemia","Oncological",
                     "Psychological_Condition","LDL","Diabetes"])

ner_ade_clinical = MedicalNerModel.pretrained("ner_ade_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ade_clinica_ner")

ner_ade_clinical_converter = NerConverterInternal()\
      .setInputCols(["sentence", "token", "ade_clinica_ner"])\
      .setOutputCol("ner_ade_clinical_chunk")\
      .setWhiteList(["ADE"])

chunk_merger = ChunkMergeApproach()\
    .setInputCols('ner_ade_clinical_chunk',"ner_jsl_chunk")\
    .setOutputCol('merged_ner_chunk')

chunk2doc = Chunk2Doc() \
      .setInputCols("merged_ner_chunk") \
      .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
     .setInputCols(["ner_chunk_doc"])\
     .setOutputCol("sbert_embeddings")\
     .setCaseSensitive(False)

meddra_resolver = SentenceEntityResolverModel.load("sbiobertresolve_meddra_llt") \
     .setInputCols(["sbert_embeddings"]) \
     .setOutputCol("meddra_llt_code")\
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

text= """This is an 82-year-old male with a history of prior tobacco use, benign hypertension, chronic renal insufficiency, chronic bronchitis, gastritis, and ischemic attack. He initially presented to Braintree with ST elevation and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of the left main coronary artery stenosis, which was complicated by hypotension and bradycardia. We describe the side effects of 5-FU in a colon cancer patient who suffered mucositis and dermatitis."""

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
	.setWhiteList(Array("Procedure","Kidney_Disease","Cerebrovascular_Disease","Heart_Disease", "Disease_Syndrome_Disorder","Symptom","VS_Finding", "EKG_Findings","Communicable_Disease", "Internal_organ_or_component","External_body_part_or_region", "Triglycerides","Alcohol","Smoking","Pregnancy","Hypertension","Obesity", "Injury_or_Poisoning","Test","Hyperlipidemia","Oncological", "Psychological_Condition","LDL","Diabetes"))
	
val ner_ade_clinical = MedicalNerModel.pretrained("ner_ade_clinical","en","clinical/models")
	.setInputCols(Array("sentence","token","embeddings"))
	.setOutputCol("ade_clinica_ner")
	
val ner_ade_clinical_converter = new NerConverterInternal()
	.setInputCols(Array("sentence","token","ade_clinica_ner"))
	.setOutputCol("ner_ade_clinical_chunk")
	.setWhiteList(Array("ADE"))
	
val chunk_merger = new ChunkMergeApproach()
	.setInputCols("ner_ade_clinical_chunk","ner_jsl_chunk")
	.setOutputCol("merged_ner_chunk")
	
val chunk2doc = new Chunk2Doc()
	.setInputCols("merged_ner_chunk")
	.setOutputCol("ner_chunk_doc")
	
val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
	.setInputCols(Array("ner_chunk_doc"))
	.setOutputCol("sbert_embeddings")
	.setCaseSensitive(false)
  
val meddra_resolver = new SentenceEntityResolverModel.load("sbiobertresolve_meddra_llt")
	.setInputCols(Array("sbert_embeddings"))
	.setOutputCol("meddra_llt_code")
	.setDistanceFunction("EUCLIDEAN")
 
 nlpPipeline= new Pipeline().setStages(Array( documentAssembler, 
                                              sentenceDetector,
                                              tokenizer,
                                              word_embeddings,
                                              ner_jsl,
                                              ner_jsl_converter,
                                              ner_ade_clinical,
                                              ner_ade_clinical_converter,
                                              chunk_merger,
                                              chunk2doc,
                                              sbert_embedder,
                                              meddra_resolver))
 
 text= """This is an 82-year-old male with a history of prior tobacco use,benign hypertension,chronic renal insufficiency,chronic bronchitis,gastritis,and ischemic attack. He initially presented to Braintree with ST elevation and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of the left main coronary artery stenosis,which was complicated by hypotension and bradycardia. We describe the side effects of 5-FU in a colon cancer patient who suffered mucositis and dermatitis."""

df= Seq(text).toDF("text")

resolver_pipeline= nlpPipeline.fit(df)
	
val result = resolver_pipeline.transform(df)
```
</div>

## Results

```bash
+----------------------------------+-----+---+-------------------------+---------------+----------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                         ner_chunk|begin|end|                   entity|meddra_llt_code|                        resolution|                                               all_k_results|                                           all_k_resolutions|
+----------------------------------+-----+---+-------------------------+---------------+----------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                           tobacco|   52| 58|                  Smoking|       10067622|               tobacco interaction|10067622:::10086359:::10057581:::10082288:::10009180:::10...|tobacco interaction:::tobaccoism:::tobacco user:::exposur...|
|                      hypertension|   72| 83|             Hypertension|       10020772|                      hypertension|10020772:::10020790:::10088636:::10081425:::10015488:::10...|hypertension:::hypertension secondary:::systemic hyperten...|
|       chronic renal insufficiency|   86|112|           Kidney_Disease|       10050441|       chronic renal insufficiency|10050441:::10009122:::10009119:::10075441:::10038474:::10...|chronic renal insufficiency:::chronic renal impairment:::...|
|                        bronchitis|  123|132|Disease_Syndrome_Disorder|       10006451|                        bronchitis|10006451:::10006448:::10008841:::10085668:::10061736:::10...|bronchitis:::bronchiolitis:::chronic bronchitis:::capilla...|
|                         gastritis|  135|143|Disease_Syndrome_Disorder|       10017853|                         gastritis|10017853:::10060703:::10076492:::10070814:::10088553:::10...|gastritis:::verrucous gastritis:::antral gastritis:::corr...|
|                   ischemic attack|  150|164|  Cerebrovascular_Disease|       10072760|         transient ischemic attack|10072760:::10060848:::10060772:::10061216:::10055221:::10...|transient ischemic attack:::ischemic cerebral infarction:...|
|           cardiac catheterization|  280|302|                Procedure|       10048606|           cardiac catheterization|10048606:::10007527:::10054343:::10007815:::10053451:::10...|cardiac catheterization:::cardiac catheterisation:::cathe...|
|left main coronary artery stenosis|  319|352|            Heart_Disease|       10090240|left main coronary artery stenosis|10090240:::10072048:::10084343:::10011089:::10083430:::10...|left main coronary artery stenosis:::left anterior descen...|
|                       hypotension|  380|390|               VS_Finding|       10021097|                       hypotension|10021097:::10021107:::10066331:::10066077:::10036433:::10...|hypotension:::hypotensive:::arterial hypotension:::diasto...|
|                       bradycardia|  396|406|               VS_Finding|       10006093|                       bradycardia|10006093:::10040741:::10078310:::10064883:::10065585:::10...|bradycardia:::sinus bradycardia:::central bradycardia:::r...|
|                      colon cancer|  451|462|              Oncological|       10009944|                      colon cancer|10009944:::10009989:::10009957:::10061451:::10007330:::10...|colon cancer:::colonic cancer:::colon carcinoma:::colorec...|
|                         mucositis|  485|493|                      ADE|       10028127|                         mucositis|10028127:::10065880:::10065900:::10006525:::10021960:::10...|mucositis:::laryngeal mucositis:::tracheal mucositis:::bu...|
|                        dermatitis|  499|508|                      ADE|       10012431|                        dermatitis|10012431:::10048768:::10003639:::10012470:::10073737:::10...|dermatitis:::dermatosis:::atopic dermatitis:::dermatitis ...|
+----------------------------------+-----+---+-------------------------+---------------+----------------------------------+------------------------------------------------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_meddra_llt|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[meddra_code]|
|Language:|en|
|Size:|230.0 MB|
|Case sensitive:|false|

## References

This model is trained with the September 2024 (v27.1) release of MedDRA dataset.

**To utilize this model, possession of a valid MedDRA license is requisite. If you possess one and wish to use this model, kindly contact us at support@johnsnowlabs.com.**