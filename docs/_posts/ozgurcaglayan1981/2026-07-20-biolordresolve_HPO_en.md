---
layout: model
title: Sentence Entity Resolver for HPO (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_HPO
date: 2026-07-20
tags: [en, entity_resolution, licensed, clinical, hpo, biolord]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps phenotypic abnormalities and medical terms associated with hereditary diseases to Human Phenotype Ontology (HPO) codes using `mpnet_embeddings_biolord_2023_c` embeddings. It also returns associated codes from SNOMEDCT_US, UMLS, ORPHA, EPCC, and Fyler vocabularies in the `all_k_aux_labels` metadata field. Trained on the Human Phenotype Ontology (HPO) 2026-06-23 release.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_HPO_en_6.4.0_3.4_1784590890095.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_HPO_en_6.4.0_3.4_1784590890095.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("word_embeddings")

ner_model = MedicalNerModel.pretrained("ner_human_phenotype_gene_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["HP"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("biolordresolve_HPO","en","clinical/models")\
    .setInputCols(["embeddings"])\
    .setOutputCol("hpo")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
])

data = spark.createDataFrame([["She is followed by Dr. X in our office and has a history of severe tricuspid regurgitation. On 05/12/08, preserved left and right ventricular systolic function, aortic sclerosis with apparent mild aortic stenosis. She has previously had a Persantine Myoview nuclear rest-stress test scan completed at ABCD Medical Center in 07/06 that was negative. She has had significant mitral valve regurgitation in the past being moderate, but on the most recent echocardiogram on 05/12/08, that was not felt to be significant. She does have a history of significant hypertension in the past. She has had dizzy spells and denies clearly any true syncope. She has had bradycardia in the past from beta-blocker therapy."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("word_embeddings")

ner_model = medical.NerModel.pretrained("ner_human_phenotype_gene_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["HP"])

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_HPO","en","clinical/models")\
    .setInputCols(["embeddings"])\
    .setOutputCol("hpo")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
])

data = spark.createDataFrame([["She is followed by Dr. X in our office and has a history of severe tricuspid regurgitation. On 05/12/08, preserved left and right ventricular systolic function, aortic sclerosis with apparent mild aortic stenosis. She has previously had a Persantine Myoview nuclear rest-stress test scan completed at ABCD Medical Center in 07/06 that was negative. She has had significant mitral valve regurgitation in the past being moderate, but on the most recent echocardiogram on 05/12/08, that was not felt to be significant. She does have a history of significant hypertension in the past. She has had dizzy spells and denies clearly any true syncope. She has had bradycardia in the past from beta-blocker therapy."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("word_embeddings")

val ner_model = MedicalNerModel
    .pretrained("ner_human_phenotype_gene_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("HP"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val embedder = MPNetEmbeddings
    .pretrained("mpnet_embeddings_biolord_2023_c", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("biolordresolve_HPO", "en", "clinical/models")
    .setInputCols(Array("embeddings"))
    .setOutputCol("hpo")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
))

val data = Seq("She is followed by Dr. X in our office and has a history of severe tricuspid regurgitation. On 05/12/08, preserved left and right ventricular systolic function, aortic sclerosis with apparent mild aortic stenosis. She has previously had a Persantine Myoview nuclear rest-stress test scan completed at ABCD Medical Center in 07/06 that was negative. She has had significant mitral valve regurgitation in the past being moderate, but on the most recent echocardiogram on 05/12/08, that was not felt to be significant. She does have a history of significant hypertension in the past. She has had dizzy spells and denies clearly any true syncope. She has had bradycardia in the past from beta-blocker therapy.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                  | entity   | hpo_code   | resolution                                              | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   | all_k_aux_labels                                                                    |
|:---------------------------|:---------|:-----------|:--------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| tricuspid regurgitation    | HP       | HP:0005180 | tricuspid valve regurgitation [tricuspid regurgitation] | HP:0005180:::HP:0001702:::HP:0001704:::HP:0031651:::HP:0034376:::HP:0030732:::HP... | 0.0318:::0.1703:::0.1997:::0.2508:::0.2583:::0.2671:::0.2762:::0.2863:::0.3045::... | tricuspid valve regurgitation [tricuspid regurgitation]:::abnormality of the tri... | Fyler:1161||SNOMEDCT_US:111287006||UMLS:C0040961:::EPCC:06.01.00||UMLS:C4025753:... |
| aortic stenosis            | HP       | HP:0001650 | aortic stenosis [aortic valve stenosis]                 | HP:0001650:::HP:0001680:::HP:0001682:::HP:0012397:::HP:0001659:::HP:0001679:::HP... | 0.0229:::0.0903:::0.1693:::0.1763:::0.1966:::0.2117:::0.2125:::0.2189:::0.2232      | aortic stenosis [aortic valve stenosis]:::narrowing of the aorta [coarctation of... | Fyler:1411||SNOMEDCT_US:60573004||UMLS:C0003507:::PMID:23909637||SNOMEDCT_US:730... |
| mitral valve regurgitation | HP       | HP:0001653 | mitral valve regurgitation [mitral regurgitation]       | HP:0001653:::HP:0001633:::HP:0031481:::HP:0001634:::HP:0001718:::HP:0034376:::HP... | 0.0049:::0.1483:::0.1707:::0.2393:::0.2420:::0.2552:::0.2809:::0.2921:::0.2968::... | mitral valve regurgitation [mitral regurgitation]:::abnormality of the mitral va... | Fyler:1151||SNOMEDCT_US:48724000||UMLS:C0026266||UMLS:C3551535:::UMLS:C4025759::... |
| hypertension               | HP       | HP:0000822 | hypertension [hypertension]                             | HP:0000822:::HP:0100735:::HP:0032263:::HP:0100817:::HP:6000321:::HP:0000875:::HP... | 0.0088:::0.1680:::0.1913:::0.2054:::0.2201:::0.2393:::0.2534:::0.2540:::0.2642::... | hypertension [hypertension]:::hypertensive crisis [hypertensive crisis]:::increa... | SNOMEDCT_US:24184005||SNOMEDCT_US:38341003||UMLS:C0020538||UMLS:C0497247:::SNOME... |
| dizzy spells               | HP       | HP:0002321 | dizzy spell [vertigo]                                   | HP:0002321:::HP:4000033:::HP:0010532:::HP:0001279:::HP:5200066:::HP:0025229:::HP... | 0.0348:::0.2809:::0.3412:::0.3516:::0.4048:::0.4180:::0.4322:::0.4366:::0.4444::... | dizzy spell [vertigo]:::non-spinning vertigo [non-spinning vertigo]:::paroxysmal... | SNOMEDCT_US:271789005||SNOMEDCT_US:399090003||SNOMEDCT_US:399153001||SNOMEDCT_US... |
| bradycardia                | HP       | HP:0001662 | bradycardia [bradycardia]                               | HP:0001662:::HP:0001688:::HP:0033992:::HP:0011675:::HP:5200038:::HP:0031843:::HP... | 0.0551:::0.1935:::0.2446:::0.3437:::0.3797:::0.3834:::0.3878:::0.4167:::0.4231::... | bradycardia [bradycardia]:::sinus bradycardia [sinus bradycardia]:::chronotropic... | SNOMEDCT_US:48867003||UMLS:C0428977:::Fyler:7013||SNOMEDCT_US:49710005||UMLS:C00... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_HPO|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[mpnet_embeddings]|
|Output Labels:|[hpo_code]|
|Language:|en|
|Size:|130.4 MB|
|Case sensitive:|false|
