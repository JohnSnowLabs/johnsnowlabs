---
layout: model
title: Pipeline for Human Phenotype Ontology (HPO) Sentence Entity Resolver
author: John Snow Labs
name: hpo_resolver_pipeline
date: 2024-01-18
tags: [licensed, en, entity_resolution, clinical, pipeline, hpo]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This advanced pipeline extracts human phenotype entities from clinical texts and utilizes the `sbiobert_base_cased_mli` Sentence Bert Embeddings to map these entities to their corresponding Human Phenotype Ontology (HPO) codes. It also returns associated codes from the following vocabularies for each HPO code: - MeSH (Medical Subject Headings)- SNOMED- UMLS (Unified Medical Language System ) - ORPHA (international reference resource for information on rare diseases and orphan drugs) - OMIM (Online Mendelian Inheritance in Man).

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_resolver_pipeline_en_5.2.1_3.2_1705566426908.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_resolver_pipeline_en_5.2.1_3.2_1705566426908.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("hpo_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""She is followed by Dr. X in our office and has a history of severe tricuspid regurgitation. On 05/12/08, preserved left and right ventricular systolic function, aortic sclerosis with apparent mild aortic stenosis. She has previously had a Persantine Myoview nuclear rest-stress test scan completed at ABCD Medical Center in 07/06 that was negative. She has had significant mitral valve regurgitation in the past being moderate, but on the most recent echocardiogram on 05/12/08, that was not felt to be significant. She does have a history of significant hypertension in the past. She has had dizzy spells and denies clearly any true syncope. She has had bradycardia in the past from beta-blocker therapy.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("hpo_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""She is followed by Dr. X in our office and has a history of severe tricuspid regurgitation. On 05/12/08, preserved left and right ventricular systolic function, aortic sclerosis with apparent mild aortic stenosis. She has previously had a Persantine Myoview nuclear rest-stress test scan completed at ABCD Medical Center in 07/06 that was negative. She has had significant mitral valve regurgitation in the past being moderate, but on the most recent echocardiogram on 05/12/08, that was not felt to be significant. She does have a history of significant hypertension in the past. She has had dizzy spells and denies clearly any true syncope. She has had bradycardia in the past from beta-blocker therapy.""")

```
</div>

## Results

```bash
|    | chunks                     |   begin |   end | entities   | resolutions   | description                | all_codes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---:|:---------------------------|--------:|------:|:-----------|:--------------|:---------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | tricuspid regurgitation    |      67 |    89 | HP         | HP:0005180    | tricuspid regurgitation    | MSH:D014262||SNOMED:111287006||UMLS:C0040961||ORPHA:228410:::MSH:D014264||SNOMED:49915006||UMLS:C0040963||ORPHA:391641:::MSH:D014263||SNOMED:253383003||UMLS:C0040962||ORPHA:1101:::UMLS:C4025753||ORPHA:1759:::UMLS:C4255215||ORPHA:1724::::::MSH:D018785||SNOMED:253455004,63042009||UMLS:C0243002||ORPHA:391641::::::::::::UMLS:C4023292||ORPHA:1880:::MSH:D008944||SNOMED:48724000||UMLS:C0026266,C3551535||ORPHA:363700:::MSH:D004437||SNOMED:204357006||UMLS:C0013481||ORPHA:466791:::MSH:D001022||SNOMED:60234000||UMLS:C0003504||ORPHA:2181::::::MSH:C562388||SNOMED:72352009||UMLS:C0149630||ORPHA:1772:::UMLS:C4023294||ORPHA:2255                                                                                                                                                                                                                                                                                                              |
|  1 | aortic stenosis            |     197 |   211 | HP         | HP:0001650    | aortic stenosis            | MSH:D001024||SNOMED:60573004||UMLS:C0003507||ORPHA:536471:::MSH:D001020||SNOMED:204368006||UMLS:C0340375||ORPHA:1052:::MSH:D021921||SNOMED:268185002||UMLS:C0003499||ORPHA:391665:::UMLS:C1848978||ORPHA:3191:::UMLS:C3887554||OMIM:229310:::MSH:D023921||SNOMED:233970002||UMLS:C0242231||ORPHA:75565:::SNOMED:218728005||UMLS:C0152419||ORPHA:2255:::SNOMED:68109007||UMLS:C0038449||ORPHA:565:::MSH:D001022||SNOMED:60234000||UMLS:C0003504||ORPHA:2181:::MSH:D016893||SNOMED:64586002||UMLS:C0007282||ORPHA:536532:::SNOMED:54160000||UMLS:C2239253||ORPHA:1054:::MSH:D001014||SNOMED:67362008||UMLS:C0003486||ORPHA:1777:::SNOMED:81817003||UMLS:C0155733||ORPHA:412:::MSH:D017545||SNOMED:433068007||UMLS:C0162872||ORPHA:536467:::MSH:C562942||SNOMED:250978003||UMLS:C0428791||ORPHA:2072:::SNOMED:251036003||UMLS:C0238669||ORPHA:231160:::                                                                                                      |
|  2 | mitral valve regurgitation |     373 |   398 | HP         | HP:0001653    | mitral valve regurgitation | MSH:D008944||SNOMED:48724000||UMLS:C0026266,C3551535||ORPHA:363700:::MSH:D008946||SNOMED:79619009||UMLS:C0026269||ORPHA:2248:::UMLS:C4025759||ORPHA:1724:::MSH:D008945||SNOMED:409712001,8074002||UMLS:C0026267||ORPHA:536467:::::::::MSH:D001022||SNOMED:60234000||UMLS:C0003504||ORPHA:2181::::::MSH:D014262||SNOMED:111287006||UMLS:C0040961||ORPHA:228410:::SNOMED:473372009||UMLS:C0919718||ORPHA:363618::::::UMLS:C1835130||OMIM:154700:::SNOMED:23063005||UMLS:C0344760||ORPHA:2248::::::SNOMED:253402005||UMLS:C0344770:::UMLS:C4021142                                                                                                                                                                                                                                                                                                                                                                                                           |
|  3 | hypertension               |     555 |   566 | HP         | HP:0000822    | hypertension               | MSH:D006973||SNOMED:24184005,38341003||UMLS:C0020538,C0497247||ORPHA:231160:::SNOMED:112222000||UMLS:C0234708||ORPHA:280921:::UMLS:C1857175||OMIM:171300:::SNOMED:706882009||UMLS:C0020546||ORPHA:94093:::MSH:D006975||SNOMED:34742003||UMLS:C0020541||ORPHA:228426:::MSH:D006976,D065627||SNOMED:11399002,697898008,70995007||UMLS:C0020542,C2973725,C3203102||ORPHA:79282:::MSH:D006978||SNOMED:123799005||UMLS:C0020545||ORPHA:3472:::MSH:D019586||SNOMED:271719001||UMLS:C0151740||ORPHA:247525:::MSH:D006983||SNOMED:271607001,29966009||UMLS:C0020555||ORPHA:79277:::SNOMED:288250001||UMLS:C0565599||ORPHA:439167:::UMLS:C3277940||ORPHA:93400:::MSH:D006937||SNOMED:13644009,166830008||UMLS:C0020443,C0595929||ORPHA:79237:::UMLS:C1846345,C3150267||ORPHA:89938:::UMLS:C1504382||OMIM:178600:::UMLS:C2265792||ORPHA:99736:::SNOMED:253920006||UMLS:C0431810||ORPHA:2346:::MSH:D058437||SNOMED:6962006||UMLS:C0152132||ORPHA:94080:::ORPHA:79259 |
|  4 | bradycardia                |     655 |   665 | HP         | HP:0001662    | bradycardia                | MSH:D001919||SNOMED:48867003||UMLS:C0428977||ORPHA:330001:::SNOMED:49710005||UMLS:C0085610||ORPHA:439232:::MSH:D018476||SNOMED:399317006||UMLS:C0233565||ORPHA:33069::::::MSH:D007007||SNOMED:45004005||UMLS:C0020620||ORPHA:69085:::ORPHA:2388::::::::::::MSH:D007022||SNOMED:45007003||UMLS:C0020649||ORPHA:556030:::MSH:D012021||SNOMED:103254005||UMLS:C0151572||ORPHA:280071:::MSH:D007024||SNOMED:28651003||UMLS:C0020651||ORPHA:556030:::SNOMED:405946002||UMLS:C0700078||ORPHA:370079:::MSH:D018476||SNOMED:255385008,43994002||UMLS:C0086439||ORPHA:280071:::ORPHA:300373:::SNOMED:3006004||UMLS:C0234428||ORPHA:29822                                                                                                                                                                                                                                                                                                                           |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.2 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel