---
layout: model
title: Sentence Entity Resolver for RxNorm (sbiobert_base_cased_mli embeddings)
author: John Snow Labs
name: sbiobertresolve_rxnorm
language: en
nav_key: models
repository: clinical/models
date: 2020-11-27
task: Entity Resolution
edition: Healthcare NLP 2.6.4
spark_version: 2.4
tags: [clinical,entity_resolution,en]
supported: true
annotator: SentenceEntityResolverModel
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description
This model maps extracted medical entities to RxNorm codes using chunk embeddings.

## Predicted Entities 
RxNorm Codes and their normalized definition with ``sbiobert_base_cased_mli`` embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/24.Improved_Entity_Resolvers_in_SparkNLP_with_sBert.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}{:target="_blank"}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_rxnorm_en_2.6.4_2.4_1606235763316.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_rxnorm_en_2.6.4_2.4_1606235763316.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")\
  .setInputCols(["sentence", "token", "embeddings"])\
  .setOutputCol("ner")\

ner_converter = NerConverterInternal()\
  .setInputCols(["sentence", "token", "ner"])\
  .setOutputCol("ner_chunk")\
  .setWhiteList(["DRUG"])

c2doc = Chunk2Doc()\
  .setInputCols("ner_chunk")\
  .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
  .setInputCols(["ner_chunk_doc"])\
  .setOutputCol("sbert_embeddings")\


resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm","en", "clinical/models") \
  .setInputCols(["sbert_embeddings"]) \
  .setOutputCol("resolution")\
  .setDistanceFunction("EUCLIDEAN")


resolver_pipeline = Pipeline(stages = [
  document_assembler,
  sentenceDetectorDL,
  tokenizer,
  word_embeddings,
  ner,
  ner_converter,
  c2doc,
  sbert_embedder,
  resolver
  ])

data = spark.createDataFrame([["""This is an 82 - year-old male with a history of prior tobacco use , hypertension , chronic renal insufficiency , COPD , gastritis , and TIA who initially presented to Braintree with a non-ST elevation MI and Guaiac positive stools , transferred to St . Margaret\'s Center for Women & Infants for cardiac catheterization with PTCA to mid LAD lesion complicated by hypotension and bradycardia requiring Atropine , IV fluids and transient dopamine possibly secondary to vagal reaction , subsequently transferred to CCU for close monitoring , hemodynamically stable at the time of admission to the CCU."""]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)
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
	
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
	.setInputCols(Array("sentence","token"))
	.setOutputCol("embeddings")
	
val ner = MedicalNerModel.pretrained("ner_posology_greedy","en","clinical/models")
	.setInputCols(Array("sentence","token","embeddings"))
	.setOutputCol("ner")
	
val ner_converter = new NerConverterInternal()
	.setInputCols(Array("sentence","token","ner"))
	.setOutputCol("ner_chunk")
	.setWhiteList(Array("DRUG"))
	
val c2doc = new Chunk2Doc()
	.setInputCols("ner_chunk")
	.setOutputCol("ner_chunk_doc")
	
val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
	.setInputCols(Array("ner_chunk_doc"))
	.setOutputCol("sbert_embeddings")
	
val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm","en","clinical/models")
	.setInputCols(Array("sbert_embeddings"))
	.setOutputCol("resolution")
	.setDistanceFunction("EUCLIDEAN")
	
val resolver_pipeline = new Pipeline().setStages(Array( 
    document_assembler, 
    sentenceDetectorDL, 
    tokenizer, 
    word_embeddings, 
    ner, 
    ner_converter, 
    c2doc,
    sbert_embedder, 
    resolver ))
	
val data = Seq("""This is an 82 - year-old male with a history of prior tobacco use ,hypertension ,chronic renal insufficiency ,COPD ,gastritis ,and TIA who initially presented to Braintree with a non-ST elevation MI and Guaiac positive stools ,transferred to St . Margaret's Center for Women & Infants for cardiac catheterization with PTCA to mid LAD lesion complicated by hypotension and bradycardia requiring Atropine ,IV fluids and transient dopamine possibly secondary to vagal reaction ,subsequently transferred to CCU for close monitoring ,hemodynamically stable at the time of admission to the CCU.""").toDF("text")
	
val result = resolver_pipeline.fit(data).transform(data)
```
</div>
## Results

```bash
+---------+-----+---+---------+------+----------------------+--------------------------------------------------------------------------------+
|    chunk|begin|end|ner_label|  code|           description|                                                                     resolutions|
+---------+-----+---+---------+------+----------------------+--------------------------------------------------------------------------------+
| Atropine|  400|407|     DRUG|  1223|              atropine|atropine:::isopto atropine:::attane:::atropisol:::atropen:::atridine:::aramin...|
|IV fluids|  411|419|     DRUG|346168|intravenous suspension|intravenous suspension:::intravenous solution:::wal-four:::injectable suspens...|
| dopamine|  435|442|     DRUG|  3628|              dopamine|dopamine:::dopamine injection:::dopexamine:::dopa, dl:::dolophine:::distigmin...|
+---------+-----+---+---------+------+----------------------+--------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---------------|---------------------|
| Name:         | sbiobertresolve_rxnorm        |
| Type:          | SentenceEntityResolverModel     |
| Compatibility: | Spark NLP 2.6.4 +               |
| License:       | Licensed            |
| Edition:       | Official          |
|Input labels:        | [ner_chunk, chunk_embeddings]     |
|Output labels:       | [resolution]                 |
| Language:      | en                  |
| Dependencies: | sbiobert_base_cased_mli |

{:.h2_title}
## Data Source
Trained on November 2020 RxNorm Clinical Drugs ontology graph with ``sbiobert_base_cased_mli`` embeddings.
https://www.nlm.nih.gov/pubs/techbull/nd20/brief/nd20_rx_norm_november_release.html