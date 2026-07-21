---
layout: model
title: Sentence Entity Resolver for HPO (bge_base_en_v1_5_onnx embeddings)
author: John Snow Labs
name: bgeresolve_HPO
date: 2026-07-20
tags: [en, entity_resolution, licensed, clinical, hpo, bge]
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

This model maps phenotypic abnormalities and medical terms associated with hereditary diseases to Human Phenotype Ontology (HPO) codes using `bge_base_en_v1_5_onnx` embeddings. It also returns associated codes from SNOMEDCT_US, UMLS, ORPHA, EPCC, and Fyler vocabularies in the `all_k_aux_labels` metadata field. Trained on the Human Phenotype Ontology (HPO) 2026-06-23 release.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_HPO_en_6.4.0_3.4_1784591893552.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_HPO_en_6.4.0_3.4_1784591893552.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("bgeresolve_HPO","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

embedder = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_HPO","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

val embedder = BGEEmbeddings
    .pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("bgeresolve_HPO", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
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
| ner_chunk                  | entity   | hpo_code   | resolution                                        | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   | all_k_aux_labels                                                                    |
|:---------------------------|:---------|:-----------|:--------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| tricuspid regurgitation    | HP       | HP:0005180 | tricuspid regurgitation [tricuspid regurgitation] | HP:0005180:::HP:0010446:::HP:0001702:::HP:0031651:::HP:0001653:::HP:0031444:::HP... | 0.0000:::0.1664:::0.1832:::0.1998:::0.2069:::0.2136:::0.2163:::0.2180:::0.2193::... | tricuspid regurgitation [tricuspid regurgitation]:::tricuspid stenosis [tricuspi... | Fyler:1161||SNOMEDCT_US:111287006||UMLS:C0040961:::EPCC:06.01.92||ICD-10:Q22.4||... |
| aortic stenosis            | HP       | HP:0001650 | aortic stenosis [aortic valve stenosis]           | HP:0001650:::HP:0001682:::HP:0100545:::HP:0001691:::HP:0004381:::HP:0034350:::HP... | 0.0000:::0.1484:::0.1852:::0.1854:::0.1982:::0.2149:::0.2162:::0.2178:::0.2226::... | aortic stenosis [aortic valve stenosis]:::subvalvular aortic stenosis [subvalvul... | Fyler:1411||SNOMEDCT_US:60573004||UMLS:C0003507:::SNOMEDCT_US:204368006||UMLS:C0... |
| mitral valve regurgitation | HP       | HP:0001653 | mitral valve regurgitation [mitral regurgitation] | HP:0001653:::HP:0001659:::HP:0010444:::HP:0034376:::HP:0005180:::HP:0001718:::HP... | 0.0000:::0.1583:::0.1617:::0.1639:::0.2041:::0.2129:::0.2305:::0.2416:::0.2463::... | mitral valve regurgitation [mitral regurgitation]:::aortic valve regurgitation [... | Fyler:1151||SNOMEDCT_US:48724000||UMLS:C0026266||UMLS:C3551535:::SNOMEDCT_US:602... |
| hypertension               | HP       | HP:0000822 | hypertension [hypertension]                       | HP:0000822:::HP:0032263:::HP:0007906:::HP:0004421:::HP:0100817:::HP:0008071:::HP... | 0.0000:::0.1955:::0.2147:::0.2155:::0.2183:::0.2213:::0.2262:::0.2368:::0.2489::... | hypertension [hypertension]:::increased blood pressure [increased blood pressure... | SNOMEDCT_US:24184005||SNOMEDCT_US:38341003||UMLS:C0020538||UMLS:C0497247:::PMID:... |
| dizzy spells               | HP       | HP:0002321 | dizzy spell [vertigo]                             | HP:0002321:::HP:0001279:::HP:0002121:::HP:4000033:::HP:0007185:::HP:0001250:::HP... | 0.0678:::0.2186:::0.2393:::0.2605:::0.2614:::0.2623:::0.2673:::0.2683:::0.2693::... | dizzy spell [vertigo]:::fainting spell [syncope]:::brief seizures with staring s... | SNOMEDCT_US:271789005||SNOMEDCT_US:399090003||SNOMEDCT_US:399153001||SNOMEDCT_US... |
| bradycardia                | HP       | HP:0001662 | bradycardia [bradycardia]                         | HP:0001662:::HP:0001688:::HP:0046507:::HP:0002067:::HP:0001649:::HP:0031843:::HP... | 0.0000:::0.0689:::0.1928:::0.2124:::0.2437:::0.2500:::0.2578:::0.2592:::0.2638::... | bradycardia [bradycardia]:::sinus bradycardia [sinus bradycardia]:::bradypnea [b... | SNOMEDCT_US:48867003||UMLS:C0428977:::Fyler:7013||SNOMEDCT_US:49710005||UMLS:C00... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_HPO|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[hpo_code]|
|Language:|en|
|Size:|130.3 MB|
|Case sensitive:|false|
