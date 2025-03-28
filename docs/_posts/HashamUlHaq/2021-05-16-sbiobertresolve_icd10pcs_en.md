---
layout: model
title: Sentence Entity Resolver for ICD10-PCS (sbiobert_base_cased_mli embeddings)
author: John Snow Labs
name: sbiobertresolve_icd10pcs
date: 2021-05-16
tags: [entity_resolution, clinical, licensed, en]
task: Entity Resolution
language: en
nav_key: models
edition: Healthcare NLP 3.0.4
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted medical entities to ICD10-PCS codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings, and has faster load time, with a speedup of about 6X when compared to previous versions. Also the load process now is more memory friendly meaning that the maximum memory required during load time is smaller, reducing the chances of OOM exceptions, and thus relaxing hardware requirements.

## Predicted Entities

Predicts ICD10-PCS Codes and their normalized definitions.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/demos){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10pcs_en_3.0.4_3.0_1621189710474.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10pcs_en_3.0.4_3.0_1621189710474.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use


```sbiobertresolve_icd10pcs``` resolver model must be used with ```sbiobert_base_cased_mli``` as embeddings ```ner_jsl``` as NER model. ```Procedure``` set in ```.setWhiteList()```.

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
...
chunk2doc = Chunk2Doc().setInputCols("ner_chunk").setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings\
.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
.setInputCols(["ner_chunk_doc"])\
.setOutputCol("sbert_embeddings")

icd10pcs_resolver = SentenceEntityResolverModel\  
.pretrained("sbiobertresolve_icd10pcs","en", "clinical/models") \
.setInputCols(["ner_chunk", "sbert_embeddings"]) \
.setOutputCol("resolution")\
.setDistanceFunction("EUCLIDEAN")

nlpPipeline = Pipeline(stages=[document_assembler, sentence_detector, tokenizer, word_embeddings, clinical_ner, ner_converter, chunk2doc, sbert_embedder, icd10pcs_resolver])

data = spark.createDataFrame([["This is an 82 - year-old male with a history of prior tobacco use , hypertension , chronic renal insufficiency , COPD , gastritis , and TIA who initially presented to Braintree with a non-ST elevation MI and Guaiac positive stools , transferred to St . Margaret\'s Center for Women & Infants for cardiac catheterization with PTCA to mid LAD lesion complicated by hypotension and bradycardia requiring Atropine , IV fluids and transient dopamine possibly secondary to vagal reaction , subsequently transferred to CCU for close monitoring , hemodynamically stable at the time of admission to the CCU ."]]).toDF("text")

results = nlpPipeline.fit(data).transform(data)
```
```scala
...
chunk2doc = Chunk2Doc().setInputCols("ner_chunk").setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
.pretrained("sbiobert_base_cased_mli","en","clinical/models")
.setInputCols(Array("ner_chunk_doc"))
.setOutputCol("sbert_embeddings")

val icd10pcs_resolver = SentenceEntityResolverModel
.pretrained("sbiobertresolve_icd10pcs","en", "clinical/models")
.setInputCols(Array("ner_chunk", "sbert_embeddings"))
.setOutputCol("resolution")
.setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, clinical_ner, ner_converter, chunk2doc, sbert_embedder, icd10pcs_resolver))

val data = Seq("This is an 82 - year-old male with a history of prior tobacco use , hypertension , chronic renal insufficiency , COPD , gastritis , and TIA who initially presented to Braintree with a non-ST elevation MI and Guaiac positive stools , transferred to St . Margaret\'s Center for Women & Infants for cardiac catheterization with PTCA to mid LAD lesion complicated by hypotension and bradycardia requiring Atropine , IV fluids and transient dopamine possibly secondary to vagal reaction , subsequently transferred to CCU for close monitoring , hemodynamically stable at the time of admission to the CCU .").toDF("text")

val result = pipeline.fit(data).transform(data)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.resolve.icd10pcs").predict("""This is an 82 - year-old male with a history of prior tobacco use , hypertension , chronic renal insufficiency , COPD , gastritis , and TIA who initially presented to Braintree with a non-ST elevation MI and Guaiac positive stools , transferred to St . Margaret\'s Center for Women & Infants for cardiac catheterization with PTCA to mid LAD lesion complicated by hypotension and bradycardia requiring Atropine , IV fluids and transient dopamine possibly secondary to vagal reaction , subsequently transferred to CCU for close monitoring , hemodynamically stable at the time of admission to the CCU .""")
```

</div>

## Results

```bash
+--------------------+-----+---+---------+-------+----------+--------------------+--------------------+
|               chunk|begin|end|   entity|   code|confidence|         resolutions|               codes|
+--------------------+-----+---+---------+-------+----------+--------------------+--------------------+
|        hypertension|   68| 79|  PROBLEM|DWY18ZZ|    0.0626|Hyperthermia of H...|DWY18ZZ:::6A3Z1ZZ...|
|chronic renal ins...|   83|109|  PROBLEM|DTY17ZZ|    0.0722|Contact Radiation...|DTY17ZZ:::04593ZZ...|
|                COPD|  113|116|  PROBLEM|2W04X7Z|    0.0765|Change Intermitte...|2W04X7Z:::0J063ZZ...|
|           gastritis|  120|128|  PROBLEM|04723Z6|    0.0826|Dilation of Gastr...|04723Z6:::04724Z6...|
|                 TIA|  136|138|  PROBLEM|00F5XZZ|    0.1074|Fragmentation in ...|00F5XZZ:::00F53ZZ...|
|a non-ST elevatio...|  182|202|  PROBLEM|B307ZZZ|    0.0750|Plain Radiography...|B307ZZZ:::2W59X3Z...|
|Guaiac positive s...|  208|229|  PROBLEM|3E1G38Z|    0.0886|Irrigation of Upp...|3E1G38Z:::3E1G38X...|
|cardiac catheteri...|  295|317|     TEST|4A0234Z|    0.0783|Measurement of Ca...|4A0234Z:::4A02X4A...|
|                PTCA|  324|327|TREATMENT|03SG3ZZ|    0.0507|Reposition Intrac...|03SG3ZZ:::0GCQ3ZZ...|
|      mid LAD lesion|  332|345|  PROBLEM|02H73DZ|    0.0490|Insertion of Intr...|02H73DZ:::02163Z7...|
+--------------------+-----+---+---------+-------+----------+--------------------+--------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd10pcs|
|Compatibility:|Healthcare NLP 3.0.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk, sbert_embeddings]|
|Output Labels:|[icd10pcs_code]|
|Language:|en|
|Case sensitive:|false|

## Data Source

Trained on ICD10 Procedure Coding System dataset with ``sbiobert_base_cased_mli`` sentence embeddings.
https://www.icd10data.com/ICD10PCS/Codes