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
                              ner_ade_clinical,
                              ner_ade_clinical_converter,
                              chunk_merger,
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
	
val meddra_resolver = new SentenceEntityResolverModel.load("sbiobertresolve_meddra_preferred_term")
	.setInputCols(Array("sbert_embeddings"))
	.setOutputCol("meddra_pt_code")
	.setDistanceFunction("EUCLIDEAN")
 
nlpPipeline= new Pipeline().setStages(Array(documentAssembler,
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
 
text= """This is an 82-year-old male with a history of prior tobacco use, benign hypertension, chronic renal insufficiency, chronic bronchitis, gastritis, and ischemic attack. He initially presented to Braintree with ST elevation and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of the left main coronary artery stenosis,which was complicated by hypotension and bradycardia. We describe the side effects of 5-FU in a colon cancer patient who suffered mucositis and dermatitis."""
 
df= Seq(text).toDF("text")

resolver_pipeline= nlpPipeline.fit(df)
	
val result = resolver_pipeline.transform(df)
```
</div>

## Results

```bash
+----------------------------------+-----+---+-------------------------+--------------+------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                         ner_chunk|begin|end|                   entity|meddra_pt_code|              resolution|                                               all_k_results|                                           all_k_resolutions|
+----------------------------------+-----+---+-------------------------+--------------+------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                           tobacco|   52| 58|                  Smoking|      10067622|     tobacco interaction|10067622:::10057581:::10082288:::10043903:::10069201:::10...|tobacco interaction:::tobacco user:::exposure to tobacco:...|
|                      hypertension|   72| 83|             Hypertension|      10020772|            hypertension|10020772:::10015488:::10039834:::10012758:::10000358:::10...|hypertension:::essential hypertension:::secondary hyperte...|
|       chronic renal insufficiency|   86|112|           Kidney_Disease|      10038435|           renal failure|10038435:::10062237:::10038428:::10050335:::10083522:::10...|renal failure:::renal impairment:::renal disorder:::renal...|
|                        bronchitis|  123|132|Disease_Syndrome_Disorder|      10006451|              bronchitis|10006451:::10006448:::10061736:::10069394:::10044314:::10...|bronchitis:::bronchiolitis:::bronchitis bacterial:::bronc...|
|                         gastritis|  135|143|Disease_Syndrome_Disorder|      10017853|               gastritis|10017853:::10070814:::10008882:::10084296:::10057969:::10...|gastritis:::corrosive gastritis:::chronic gastritis:::imm...|
|                   ischemic attack|  150|164|  Cerebrovascular_Disease|      10061216|              infarction|10061216:::10028596:::10008118:::10044390:::10060840:::10...|infarction:::myocardial infarction:::cerebral infarction:...|
|           cardiac catheterization|  280|302|                Procedure|      10007815| catheterisation cardiac|10007815:::10053451:::10088292:::10053438:::10085366:::10...|catheterisation cardiac:::cardiac imaging procedure:::car...|
|left main coronary artery stenosis|  319|352|            Heart_Disease|      10011089|coronary artery stenosis|10011089:::10011105:::10078431:::10077334:::10050180:::10...|coronary artery stenosis:::coronary ostial stenosis:::cor...|
|                       hypotension|  380|390|               VS_Finding|      10021097|             hypotension|10021097:::10066077:::10062300:::10031127:::10084013:::10...|hypotension:::diastolic hypotension:::procedural hypotens...|
|                       bradycardia|  396|406|               VS_Finding|      10006093|             bradycardia|10006093:::10040741:::10078310:::10090651:::10006100:::10...|bradycardia:::sinus bradycardia:::central bradycardia:::s...|
|                      colon cancer|  451|462|              Oncological|      10009944|            colon cancer|10009944:::10061451:::10009953:::10001167:::10009956:::10...|colon cancer:::colorectal cancer:::colon cancer stage i::...|
|                         mucositis|  485|493|                      ADE|      10028128|    mucositis management|10028128:::10066992:::10028116:::10037763:::10082980:::10...|mucositis management:::mucosal induration:::mucosal infla...|
|                        dermatitis|  499|508|                      ADE|      10012431|              dermatitis|10012431:::10048768:::10012470:::10083156:::10030012:::10...|dermatitis:::dermatosis:::dermatitis infected:::immune-me...|
+----------------------------------+-----+---+-------------------------+--------------+------------------------+------------------------------------------------------------+------------------------------------------------------------++
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
