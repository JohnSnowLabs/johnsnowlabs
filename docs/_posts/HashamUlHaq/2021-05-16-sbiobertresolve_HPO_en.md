---
layout: model
title: Entity Resolver for Human Phenotype Ontology
author: John Snow Labs
name: sbiobertresolve_HPO
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

This model  maps phenotypic abnormalities, medical terms associated with hereditary diseases, encountered in human to Human Phenotype Ontology (HPO) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings, and has faster load time, with a speedup of about 6X when compared to previous versions. Also the load process now is more memory friendly meaning that the maximum memory required during load time is smaller, reducing the chances of OOM exceptions, and thus relaxing hardware requirements.

## Predicted Entities

This model returns Human Phenotype Ontology (HPO) codes for phenotypic abnormalities encountered in human diseases. It also returns associated codes from the following vocabularies for each HPO code: - MeSH (Medical Subject Headings)- SNOMED- UMLS (Unified Medical Language System ) - ORPHA (international reference resource for information on rare diseases and orphan drugs) - OMIM (Online Mendelian Inheritance in Man)

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_MSH/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_HPO_en_3.0.4_3.0_1621189482944.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_HPO_en_3.0.4_3.0_1621189482944.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
	.setInputCol("text")\
	.setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
	.setInputCols(["document"])\
	.setOutputCol("sentence")

tokenizer = Tokenizer()\
	.setInputCols(["sentence"])\
	.setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
	.setInputCols(["sentence", "token"])\
	.setOutputCol("word_embeddings")

ner = MedicalNerModel.pretrained("ner_human_phenotype_gene_clinical", "en", "clinical/models") \
	.setInputCols(["sentence", "token", "word_embeddings"]) \
	.setOutputCol("ner")\

ner_converter = NerConverterInternal()\
	.setInputCols(["sentence", "token", "ner"])\
	.setOutputCol("ner_chunk")\
  	.setWhiteList(["HP"])

chunk2doc = Chunk2Doc()\
	.setInputCols("ner_chunk")\
	.setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli",'en','clinical/models')\
  	.setInputCols(["ner_chunk_doc"])\
  	.setOutputCol("sbert_embeddings")\
  	.setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_HPO", "en", "clinical/models") \
  	.setInputCols(["sbert_embeddings"]) \
  	.setOutputCol("resolution")\
  	.setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages = [
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner,
    ner_converter,
    chunk2doc,
    sbert_embedder,
    resolver])

text = """She is followed by Dr. X in our office and has a history of severe tricuspid regurgitation. On 05/12/08, preserved left and right ventricular systolic function, aortic sclerosis with apparent mild aortic stenosis. She has previously had a Persantine Myoview nuclear rest-stress test scan completed at ABCD Medical Center in 07/06 that was negative. She has had significant mitral valve regurgitation in the past being moderate, but on the most recent echocardiogram on 05/12/08, that was not felt to be significant. She does have a history of significant hypertension in the past. She has had dizzy spells and denies clearly any true syncope. She has had bradycardia in the past from beta-blocker therapy."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)
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
  .setOutputCol("word_embeddings") 

val ner = MedicalNerModel.pretrained("ner_human_phenotype_gene_clinical","en","clinical/models")
  .setInputCols(Array("sentence","token","word_embeddings")) 
  .setOutputCol("ner") 

val ner_converter = new NerConverterInternal()
  .setInputCols(Array("sentence","token","ner")) 
  .setOutputCol("ner_chunk") 
  .setWhiteList(Array("HP")) 

val chunk2doc = new Chunk2Doc()
  .setInputCols("ner_chunk") 
  .setOutputCol("ner_chunk_doc") 

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
  .setInputCols(Array("ner_chunk_doc")) 
  .setOutputCol("sbert_embeddings") 
  .setCaseSensitive(false) 

val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_HPO","en","clinical/models")
  .setInputCols(Array("sbert_embeddings")) 
  .setOutputCol("resolution") 
  .setDistanceFunction("EUCLIDEAN") 

val pipeline = new Pipeline(stages = new Array(
  document_assembler, 
  sentence_detector, 
  tokenizer, 
  word_embeddings, 
  ner, 
  ner_converter, 
  chunk2doc, 
  sbert_embedder, 
  resolver)) 

val text = """She is followed by Dr. X in our office and has a history of severe tricuspid regurgitation. On 05/12/08,preserved left and right ventricular systolic function,aortic sclerosis with apparent mild aortic stenosis. She has previously had a Persantine Myoview nuclear rest-stress test scan completed at ABCD Medical Center in 07/06 that was negative. She has had significant mitral valve regurgitation in the past being moderate,but on the most recent echocardiogram on 05/12/08,that was not felt to be significant. She does have a history of significant hypertension in the past. She has had dizzy spells and denies clearly any true syncope. She has had bradycardia in the past from beta-blocker therapy.""" 
val data = Seq(text).toDF("text") 
val result = pipeline.fit(data).transform(data)
```


{:.nlu-block}
```python
import nlu

nlu.load("en.resolve.HPO").predict("""She is followed by Dr. X in our office and has a history of severe tricuspid regurgitation. On 05/12/08, preserved left and right ventricular systolic function, aortic sclerosis with apparent mild aortic stenosis. She has previously had a Persantine Myoview nuclear rest-stress test scan completed at ABCD Medical Center in 07/06 that was negative. She has had significant mitral valve regurgitation in the past being moderate, but on the most recent echocardiogram on 05/12/08, that was not felt to be significant. She does have a history of significant hypertension in the past. She has had dizzy spells and denies clearly any true syncope. She has had bradycardia in the past from beta-blocker therapy.""")
```

</div>

## Results

```bash
+--------------------------+-----+---+---------+----------+--------------------------+------------------------------------------------------------+
|                     chunk|begin|end|ner_label|resolution|               description|                                                   all_codes|
+--------------------------+-----+---+---------+----------+--------------------------+------------------------------------------------------------+
|   tricuspid regurgitation|   67| 89|       HP|HP:0005180|   tricuspid regurgitation|MSH:D014262||SNOMED:111287006||UMLS:C0040961||ORPHA:22841...|
|           aortic stenosis|  197|211|       HP|HP:0001650|           aortic stenosis|MSH:D001024||SNOMED:60573004||UMLS:C0003507||ORPHA:536471...|
|mitral valve regurgitation|  373|398|       HP|HP:0001653|mitral valve regurgitation|MSH:D008944||SNOMED:48724000||UMLS:C0026266,C3551535||ORP...|
|              hypertension|  555|566|       HP|HP:0000822|              hypertension|MSH:D006973||SNOMED:24184005,38341003||UMLS:C0020538,C049...|
|               bradycardia|  655|665|       HP|HP:0001662|               bradycardia|MSH:D001919||SNOMED:48867003||UMLS:C0428977||ORPHA:330001...|
+--------------------------+-----+---+---------+----------+--------------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_HPO|
|Compatibility:|Healthcare NLP 3.0.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[hpo_code]|
|Language:|en|
|Case sensitive:|false|
