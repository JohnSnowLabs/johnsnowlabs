---
layout: model
title: Sentence Entity Resolver for HPO (sbiobert_base_cased_mli_onnx embeddings)
author: John Snow Labs
name: sbiobertresolve_HPO
date: 2026-07-20
tags: [en, entity_resolution, licensed, clinical, hpo, sbiobert]
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

This model maps phenotypic abnormalities and medical terms associated with hereditary diseases to Human Phenotype Ontology (HPO) codes using `sbiobert_base_cased_mli_onnx` Sentence Bert Embeddings. It also returns associated codes from SNOMEDCT_US, UMLS, ORPHA, EPCC, and Fyler vocabularies in the `all_k_aux_labels` metadata field. Trained on the Human Phenotype Ontology (HPO) 2026-06-23 release.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_HPO_en_6.4.0_3.4_1784586607387.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_HPO_en_6.4.0_3.4_1784586607387.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_HPO","en","clinical/models")\
    .setInputCols(["sentence_embeddings"])\
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

embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_HPO","en","clinical/models")\
    .setInputCols(["sentence_embeddings"])\
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

val embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli_onnx", "en","clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sentence_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_HPO", "en", "clinical/models")
    .setInputCols(Array("sentence_embeddings"))
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
| tricuspid regurgitation    | HP       | HP:0005180 | tricuspid regurgitation [tricuspid regurgitation] | HP:0005180:::HP:0010446:::HP:0001704:::HP:0001702:::HP:0030732:::HP:0031444:::HP... | 0.0000:::0.0538:::0.0609:::0.0757:::0.0794:::0.0873:::0.0879:::0.0899:::0.0893::... | tricuspid regurgitation [tricuspid regurgitation]:::tricuspid stenosis [tricuspi... | Fyler:1161||SNOMEDCT_US:111287006||UMLS:C0040961:::EPCC:06.01.92||ICD-10:Q22.4||... |
| aortic stenosis            | HP       | HP:0001650 | aortic stenosis [aortic valve stenosis]           | HP:0001650:::HP:0001682:::HP:0004381:::HP:0005174:::HP:0001691:::HP:0005145:::HP... | 0.0000:::0.0296:::0.0412:::0.0618:::0.0677:::0.0751:::0.0762:::0.0770:::0.0816::... | aortic stenosis [aortic valve stenosis]:::subvalvular aortic stenosis [subvalvul... | Fyler:1411||SNOMEDCT_US:60573004||UMLS:C0003507:::SNOMEDCT_US:204368006||UMLS:C0... |
| mitral valve regurgitation | HP       | HP:0001653 | mitral valve regurgitation [mitral regurgitation] | HP:0001653:::HP:0001718:::HP:0001633:::HP:0001634:::HP:0031478:::HP:0031481:::HP... | 0.0000:::0.0495:::0.0573:::0.0682:::0.0687:::0.0700:::0.0706:::0.0706:::0.0757::... | mitral valve regurgitation [mitral regurgitation]:::mitral valve stenosis [mitra... | Fyler:1151||SNOMEDCT_US:48724000||UMLS:C0026266||UMLS:C3551535:::EPCC:06.02.92||... |
| hypertension               | HP       | HP:0000822 | hypertension [hypertension]                       | HP:0000822:::HP:6000321:::HP:0007906:::HP:0000875:::HP:0430034:::HP:0100735:::HP... | 0.0000:::0.0604:::0.0735:::0.0937:::0.0959:::0.1081:::0.1109:::0.1130:::0.1167::... | hypertension [hypertension]:::labile hypertension [labile hypertension]:::ocular... | SNOMEDCT_US:24184005||SNOMEDCT_US:38341003||UMLS:C0020538||UMLS:C0497247::::::SN... |
| dizzy spells               | HP       | HP:0002321 | dizzy spell [vertigo]                             | HP:0002321:::HP:0006961:::HP:0012668:::HP:6000456:::HP:0001279:::HP:0000975:::HP... | 0.0183:::0.1165:::0.1221:::0.1306:::0.1324:::0.1299:::0.1335:::0.1428:::0.1434::... | dizzy spell [vertigo]:::jerky head movements [jerky head movements]:::situationa... | SNOMEDCT_US:271789005||SNOMEDCT_US:399090003||SNOMEDCT_US:399153001||SNOMEDCT_US... |
| bradycardia                | HP       | HP:0001662 | bradycardia [bradycardia]                         | HP:0001662:::HP:0001688:::HP:0002067:::HP:0046507:::HP:0000966:::HP:0031843:::HP... | 0.0000:::0.0207:::0.0716:::0.0792:::0.1065:::0.1136:::0.1125:::0.1162:::0.1174::... | bradycardia [bradycardia]:::sinus bradycardia [sinus bradycardia]:::bradykinesia... | SNOMEDCT_US:48867003||UMLS:C0428977:::Fyler:7013||SNOMEDCT_US:49710005||UMLS:C00... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_HPO|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[hpo_code]|
|Language:|en|
|Size:|130.0 MB|
|Case sensitive:|false|