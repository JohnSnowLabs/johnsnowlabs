---
layout: model
title: Sentence Entity Resolver for RxNorm (sbiobert_base_cased_mli embeddings)
author: John Snow Labs
name: sbiobertresolve_rxnorm
date: 2021-10-10
tags: [rxnorm, entity_resolution, licensed, clinical, en]
task: Entity Resolution
language: en
nav_key: models
edition: Healthcare NLP 3.2.3
spark_version: 2.4
supported: true
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using `sbiobert_base_cased_mli ` Sentence Bert Embeddings.

## Predicted Entities

`RxNorm Codes`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_RXNORM/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_rxnorm_en_3.2.3_2.4_1633875017884.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_rxnorm_en_3.2.3_2.4_1633875017884.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
		.setInputCol("text")\
		.setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
		.setInputCols(["document"]) \
		.setOutputCol("sentence")

tokenizer = Tokenizer()\
		.setInputCols(["sentence"])\
		.setOutputCol("token")
	
word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
		.setInputCols(["sentence", "token"])\
		.setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models") \
		.setInputCols(["sentence", "token", "embeddings"]) \
		.setOutputCol("jsl_ner")

ner_converter = NerConverter() \
		.setInputCols(["sentence", "token", "jsl_ner"]) \
		.setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")

rxnorm_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm","en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

nlpPipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector, 
    tokenizer, 
    word_embeddings, 
    clinical_ner, 
    ner_converter, 
    chunk2doc, 
    sbert_embedder, 
    rxnorm_resolver])

data = spark.createDataFrame([["""She is given Fragmin 5000 units subcutaneously daily , Xenaderm to wounds topically b.i.d., lantus 40 units subcutaneously at bedtime , OxyContin 30 mg p.o.q. , folic acid 1 mg daily , levothyroxine 0.1 mg 
p.o. daily , Prevacid 30 mg daily , Avandia 4 mg daily , norvasc 10 mg daily , lexapro 20 mg daily , aspirin 81 mg daily , Neurontin 400 mg ."""]]).toDF("text")

result = nlpPipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")
	
val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
	.setInputCols(Array("document"))
	.setOutputCol("sentence")
	
val tokenizer = new Tokenizer()
	.setInputCols(Array("sentence"))
	.setOutputCol("token")
	
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
	.setInputCols(Array("sentence","token"))
	.setOutputCol("embeddings")
	
val clinical_ner = MedicalNerModel.pretrained("ner_posology_greedy","en","clinical/models")
	.setInputCols(Array("sentence","token","embeddings"))
	.setOutputCol("jsl_ner")
	
val ner_converter = new NerConverter()
	.setInputCols(Array("sentence","token","jsl_ner"))
	.setOutputCol("ner_chunk")
	.setWhiteList(Array("DRUG"))
	
val chunk2doc = new Chunk2Doc()
	.setInputCols("ner_chunk")
	.setOutputCol("ner_chunk_doc")
	
val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
	.setInputCols(Array("ner_chunk_doc"))
	.setOutputCol("sbert_embeddings")
	
val rxnorm_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm","en","clinical/models")
	.setInputCols(Array("sbert_embeddings"))
	.setOutputCol("resolution")
	.setDistanceFunction("EUCLIDEAN")
	
val nlpPipeline = new Pipeline().setStages(Array( 
    document_assembler, 
    sentence_detector, 
    tokenizer, 
    word_embeddings, 
    clinical_ner, 
    ner_converter, 
    chunk2doc, 
    sbert_embedder, 
    rxnorm_resolver))
	
val data = Seq("""She is given Fragmin 5000 units subcutaneously daily ,Xenaderm to wounds topically b.i.d.,lantus 40 units subcutaneously at bedtime ,OxyContin 30 mg p.o.q. ,folic acid 1 mg daily ,levothyroxine 0.1 mg p.o. daily ,Prevacid 30 mg daily ,Avandia 4 mg daily ,norvasc 10 mg daily ,lexapro 20 mg daily ,aspirin 81 mg daily ,Neurontin 400 mg .""").toDF("text")
	
val results = nlpPipeline.fit(data).transform(data)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.resolve.rxnorm").predict("""She is given Fragmin 5000 units subcutaneously daily , Xenaderm to wounds topically b.i.d., lantus 40 units subcutaneously at bedtime , OxyContin 30 mg p.o.q. , folic acid 1 mg daily , levothyroxine 0.1 mg 
p.o. daily , Prevacid 30 mg daily , Avandia 4 mg daily , norvasc 10 mg daily , lexapro 20 mg daily , aspirin 81 mg daily , Neurontin 400 mg .""")
```

</div>

## Results

```bash
+---------------------------------+-----+---+---------+-------+---------------------------+------------------------------------------------------------+
|                            chunk|begin|end|ner_label|   code|                description|                                                 resolutions|
+---------------------------------+-----+---+---------+-------+---------------------------+------------------------------------------------------------+
|Fragmin 5000 units subcutaneously|   13| 45|     DRUG| 334595|           dipyrone 5000 mg|dipyrone 5000 mg:::thiamylal 5000 mg injectable solution:...|
|                  OxyContin 30 mg|  136|150|     DRUG| 353342|           cevimeline 30 mg|cevimeline 30 mg:::ubidecarenone 30 mg:::moxisylyte 30 mg...|
|                  folic acid 1 mg|  161|175|     DRUG| 315966|            folic acid 1 mg|folic acid 1 mg:::folic acid 1.1 mg:::folic acid 1 mg/ml:...|
|       levothyroxine 0.1 mg \np.o|  185|209|     DRUG| 892245|levothyroxine sodium 0.1 mg|levothyroxine sodium 0.1 mg:::thyroxine 0.1 mg [levo-t]::...|
|                   Prevacid 30 mg|  220|233|     DRUG| 450952|            prifinium 30 mg|prifinium 30 mg:::almitrine 30 mg:::fumarate 30 mg:::prot...|
|                     Avandia 4 mg|  243|254|     DRUG| 446939|            reproterol 4 mg|reproterol 4 mg:::vindesine 4 mg:::pridinol 4 mg:::guanab...|
|                    norvasc 10 mg|  264|276|     DRUG| 446896|         norfenefrine 10 mg|norfenefrine 10 mg:::bamethan 10 mg:::amezinium 10 mg:::a...|
|                    lexapro 20 mg|  286|298|     DRUG|1433226|      levomilnacipran 20 mg|levomilnacipran 20 mg:::propinox 20 mg:::fenproporex 20 m...|
|                    aspirin 81 mg|  308|320|     DRUG| 315431|              aspirin 81 mg|aspirin 81 mg:::aspirin 81 mg [bayer]:::aspirin 81 mg [ys...|
|                 Neurontin 400 mg|  330|345|     DRUG| 700854|       ubidecarenone 400 mg|ubidecarenone 400 mg:::niacin 400 mg:::tribenoside 400 mg...|
+---------------------------------+-----+---+---------+-------+---------------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_rxnorm|
|Compatibility:|Healthcare NLP 3.2.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[rxnorm_code]|
|Language:|en|
|Case sensitive:|false|

## Data Source

Trained on 02 August 2021 RxNorm dataset.
