---
layout: model
title: Sentence Entity Resolver for SNOMED Concepts (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_snomed_findings_aux_concepts
date: 2024-05-07
tags: [licensed, en, biolord, auxconcepts, entity_resolution, clinical, findings, snomed]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts to SNOMED codes using `mpnet_embeddings_biolord_2023_c` Sentence Embeddings. This is also capable of extracting `Clinical Findings `, `Morph Abnormality`, `Clinical Drug`, `Clinical Drug Form`, `Procedure`, `Substance`, `Physical Object`, and `Body Structure` concepts of SNOMED codes.


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_snomed_findings_aux_concepts_en_5.3.1_3.4_1715097558209.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_snomed_findings_aux_concepts_en_5.3.1_3.4_1715097558209.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
                     "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                     "EKG_Findings", "Communicable_Disease","Substance","Drug_Ingredient",
                     "Internal_organ_or_component","External_body_part_or_region","Modifier",
                     "Triglycerides","Alcohol","Smoking","Pregnancy","Hypertension","Obesity",
                     "Injury_or_Poisoning","Test","Hyperlipidemia","BMI","Oncological","Psychological_Condition","LDL","Diabetes"])

chunk2doc = Chunk2Doc()\
      .setInputCols("ner_jsl_chunk")\
      .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
     .setInputCols(["ner_chunk_doc"])\
     .setOutputCol("sbert_embeddings")\
     .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_snomed_findings_aux_concepts", "en", "clinical/models")\
      .setInputCols(["sbert_embeddings"])\
     .setOutputCol("snomed_code")\
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
                              snomed_resolver
])

data = spark.createDataFrame([["""This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction. He was subsequently transferred to the CCU for close monitoring. He was hemodynamically stable at the time of admission to the CCU."""]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
      .setInputCols(["document"])
      .setOutputCol("sentence")

val tokenizer = new Tokenizer()
      .setInputCols(["sentence"])
      .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en", "clinical/models")
      .setInputCols(Array("sentence", "token"))
      .setOutputCol("embeddings")

val ner_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
      .setInputCols(Array("sentence", "token", "embeddings"))
      .setOutputCol("ner_jsl")

val ner_jsl_converter = new NerConverter()
      .setInputCols(Array("sentence", "token", "ner_jsl"))
      .setOutputCol("ner_jsl_chunk")
      .setWhiteList(Array("Procedure","Kidney_Disease","Cerebrovascular_Disease","Heart_Disease",
                     "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                     "EKG_Findings", "Communicable_Disease","Substance","Drug_Ingredient",
                     "Internal_organ_or_component","External_body_part_or_region","Modifier",
                     "Triglycerides","Alcohol","Smoking","Pregnancy","Hypertension","Obesity",
                     "Injury_or_Poisoning","Test","Hyperlipidemia","BMI","Oncological","Psychological_Condition","LDL","Diabetes"))

val chunk2doc = new Chunk2Doc()
      .setInputCols("ner_jsl_chunk")
      .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
     .setInputCols(["ner_chunk_doc"])
     .setOutputCol("sbert_embeddings")
     .setCaseSensitive(False)

val snomed_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_snomed_findings_aux_concepts", "en", "clinical/models")
     .setInputCols(["sbert_embeddings"])
     .setOutputCol("snomed_code")
     .setDistanceFunction("EUCLIDEAN")

val nlpPipeline= new PipelineModel().setStages(Array(
                              documentAssembler,
                              sentenceDetector,
                              tokenizer,
                              word_embeddings,
                              ner_jsl,
                              ner_jsl_converter,
                              chunk2doc,
                              sbert_embedder,
                              snomed_resolver
])

val data = Seq([["""This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction. He was subsequently transferred to the CCU for close monitoring. He was hemodynamically stable at the time of admission to the CCU."""]]).toDF("text")

val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+--------------------------------------------------------------------+-------------------------+-----------+---------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|                                                           ner_chunk|                   entity|snomed_code|                                               resolution|                                                                   all_k_results|                                                                 all_k_distances|                                                          all_k_cosine_distances|                                                              all_k_resolutions |                                                                all_k_aux_labels|
+--------------------------------------------------------------------+-------------------------+-----------+---------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|                                                             tobacco|                  Smoking|   57264008|                                                  tobacco|57264008:::159882006:::39953003:::110483000:::102407002:::89765005:::26663004...|0.1070:::0.2268:::0.3980:::0.4179:::0.4232:::0.4947:::0.4970:::0.5265:::0.533...|0.0057:::0.0257:::0.0792:::0.0873:::0.0895:::0.1224:::0.1235:::0.1386:::0.142...|tobacco:::tobacco processor:::tobacco - substance:::tobacco use:::tobacco smo...|Organism:::Social Context:::Substance:::Clinical Finding:::Substance:::Clinic...|
|                                                        hypertension|             Hypertension|   38341003|                                             hypertension|38341003:::64715009:::59621000:::10725009:::31992008:::24184005:::50490005:::...|  0.3600:::0.4373:::0.4850:::0.5022:::0.5474:::0.5538:::0.5594:::0.5792:::0.5838|  0.0648:::0.0956:::0.1176:::0.1261:::0.1498:::0.1533:::0.1565:::0.1677:::0.1704|hypertension:::hypertensive cardiovascular disease:::primary hypertension:::b...|Clinical Finding:::Clinical Finding:::Clinical Finding:::Clinical Finding:::C...|
|                                         chronic renal insufficiency|           Kidney_Disease|   90688005|                                    chronic renal failure|90688005:::425369003:::723190009:::709044004:::431856006:::472953006:::236542...|0.4124:::0.4157:::0.4386:::0.5075:::0.6407:::0.6532:::0.6707:::0.6785:::0.692...|0.0851:::0.0864:::0.0962:::0.1288:::0.2053:::0.2134:::0.2249:::0.2302:::0.239...|chronic renal failure:::chronic progressive renal insufficiency:::chronic ren...|Clinical Finding:::Clinical Finding:::Clinical Finding:::Clinical Finding:::C...|
|                                                                COPD|Disease_Syndrome_Disorder|   13645005|                                                     copd|13645005:::195951007:::79688008:::68372009:::270473001:::473223004:::42728600...|0.3151:::0.7223:::0.7460:::0.7629:::0.7712:::0.7751:::0.7840:::0.7862:::0.786...|0.0496:::0.2609:::0.2783:::0.2910:::0.2974:::0.3004:::0.3074:::0.3090:::0.309...|copd:::acute exacerbation of copd:::airway obstruction:::airway obstruction, ...|Clinical Finding:::Clinical Finding:::Clinical Finding:::Clinical Finding:::C...|
|                                                           gastritis|Disease_Syndrome_Disorder|    4556007|                                                gastritis|4556007:::196731005:::50874004:::235656001:::235655002:::723096000:::39633700...|0.0942:::0.4291:::0.4426:::0.4761:::0.5037:::0.5288:::0.5290:::0.5368:::0.536...|0.0044:::0.0921:::0.0979:::0.1133:::0.1269:::0.1398:::0.1399:::0.1441:::0.144...|gastritis:::gastroduodenitis:::nonerosive nonspecific gastritis:::chemical ga...|Clinical Finding:::Clinical Finding:::Clinical Finding:::Clinical Finding:::C...|
|                                                                 TIA|  Cerebrovascular_Disease|  266257000|                                                      tia|266257000:::161511000:::463921000124102:::257976002:::417963007:::160363004::...|0.6973:::0.7551:::0.8816:::0.8968:::0.9031:::0.9240:::0.9344:::0.9349:::0.937...|0.2431:::0.2851:::0.3886:::0.4022:::0.4078:::0.4269:::0.4365:::0.4370:::0.439...|tia:::h/o: tia:::tiamastus:::t:::tta:::fh: tia:::t.a.o.:::tiadenol:::titr:::t...|Clinical Finding:::Context-dependent:::Organism:::Qualifier Value:::Clinical ...|
|                                                         nonspecific|                 Modifier|   10003008|                                             non-specific|10003008:::1491000:::278001007:::225413008:::1186687002:::261992003:::2776400...|0.8149:::0.8580:::0.8607:::0.8675:::0.8749:::0.8814:::0.8877:::0.8878:::0.894...|0.3320:::0.3681:::0.3704:::0.3763:::0.3827:::0.3884:::0.3940:::0.3941:::0.399...|non-specific:::unclassified:::nonspecific site:::nominal observation:::unfami...|Qualifier Value:::Qualifier Value:::Body Structure:::Procedure:::Clinical Fin...|
|                                                    ST-T abnormality|             EKG_Findings|  428549008|          secondary st-t abnormality on electrocardiogram|428549008:::428750005:::164930006:::164934002:::55930002:::428418001:::164861...|0.4570:::0.5346:::0.6139:::0.6302:::0.7367:::0.7480:::0.7769:::0.7989:::0.803...|0.1044:::0.1429:::0.1885:::0.1985:::0.2714:::0.2798:::0.3018:::0.3191:::0.323...|secondary st-t abnormality on electrocardiogram:::nonspecific st-t abnormalit...|Clinical Finding:::Clinical Finding:::Clinical Finding:::Clinical Finding:::C...|
|                                             cardiac catheterization|                Procedure|   41976001|                                  cardiac catheterization|41976001:::721968000:::129085009:::40403005:::67629009:::705923009:::12895900...|  0.1410:::0.2253:::0.4484:::0.4516:::0.4814:::0.5182:::0.5197:::0.5268:::0.5268|  0.0099:::0.0254:::0.1005:::0.1020:::0.1159:::0.1343:::0.1350:::0.1387:::0.1388|cardiac catheterization:::cardiac catheterization report:::cardiac catheteriz...|Procedure:::Record Artifact:::Qualifier Value:::Procedure:::Procedure:::Physi...|
|occlusion of the mid left anterior descending coronary artery lesion|                  Symptom|  840313007|occlusion of mid left anterior descending coronary artery|840313007:::44771000087108:::1255266003:::868219001:::44781000087105:::840608...|0.2971:::0.4492:::0.6153:::0.6680:::0.6837:::0.6896:::0.6930:::0.6983:::0.702...|0.0441:::0.1009:::0.1893:::0.2231:::0.2337:::0.2378:::0.2401:::0.2438:::0.246...|occlusion of mid left anterior descending coronary artery:::occlusion of mid ...|Clinical Finding:::Clinical Finding:::No_Concept_Class:::Clinical Finding:::C...|
|                                                         hypotension|               VS_Finding|   45007003|                                              hypotension|45007003:::67763001:::12763006:::94501000119106:::255329004:::429561008:::271...|0.1618:::0.4915:::0.5522:::0.5797:::0.5918:::0.5982:::0.6189:::0.6334:::0.663...|0.0131:::0.1208:::0.1525:::0.1681:::0.1751:::0.1789:::0.1915:::0.2006:::0.220...|hypotension:::hypotensive episode:::finding of decreased blood pressure:::tra...|Clinical Finding:::Clinical Finding:::Clinical Finding:::Clinical Finding:::Q...|
|                                                         bradycardia|               VS_Finding|   48867003|                                              bradycardia|48867003:::42177007:::421869004:::74615001:::690461000119106:::426627000:::11...|0.0356:::0.4672:::0.5074:::0.5581:::0.5716:::0.5737:::0.6261:::0.6418:::0.650...|0.0006:::0.1092:::0.1287:::0.1557:::0.1633:::0.1646:::0.1960:::0.2059:::0.211...|bradycardia:::bradycardia - pulse:::bradyarrhythmia:::bradycardia-tachycardia...|Clinical Finding:::Clinical Finding:::Clinical Finding:::Clinical Finding:::C...|
|                                                            atropine|          Drug_Ingredient|   73949004|                                                 atropine|73949004:::74237004:::34013000:::349945006:::391795000:::1268950007:::3499460...|0.0901:::0.4836:::0.5341:::0.5451:::0.5642:::0.5842:::0.6645:::0.6656:::0.666...|0.0041:::0.1169:::0.1426:::0.1485:::0.1592:::0.1707:::0.2208:::0.2215:::0.222...|atropine:::atropine sulfate:::atropa:::oral atropine:::atropine methonitrate:...|Pharma/Biol Product:::Substance:::Organism:::Clinical Drug Form:::Substance::...|
|                                                              fluids|          Drug_Ingredient|  255765007|                                                    fluid|255765007:::789022006:::264312008:::441841000124109:::161844003:::33463005:::...|0.2773:::0.3752:::0.4071:::0.4141:::0.4539:::0.4892:::0.5327:::0.5578:::0.566...|0.0384:::0.0704:::0.0829:::0.0857:::0.1030:::0.1196:::0.1419:::0.1556:::0.160...|fluid:::refusing fluids:::liquid:::watery fluid:::taking some fluids:::liquid...|Qualifier Value:::Clinical Finding:::Clinical Finding:::Substance:::Clinical ...|
|                                                            dopamine|          Drug_Ingredient|   59187003|                                                 dopamine|59187003:::412383006:::16257000:::30581005:::418222008:::384952006:::41284500...|0.0449:::0.2705:::0.4550:::0.4795:::0.5036:::0.5395:::0.5464:::0.5606:::0.568...|0.0010:::0.0366:::0.1035:::0.1150:::0.1268:::0.1455:::0.1493:::0.1571:::0.161...|dopamine:::dopamine agent:::dopamine hydrochloride:::urine dopamine:::dopamin...|Pharma/Biol Product:::Substance:::Substance:::Procedure:::Substance:::Pharma/...|
|                                                      vagal reaction|                  Symptom|  128968000|                                        vagal stimulation|128968000:::271137009:::29894000:::83544006:::167195007:::7524009:::417343009...|0.6265:::0.7792:::0.8089:::0.8155:::0.8668:::0.8682:::0.8689:::0.8724:::0.880...|0.1962:::0.3036:::0.3272:::0.3325:::0.3757:::0.3769:::0.3775:::0.3805:::0.387...|vagal stimulation:::vasomotor reaction:::vagal bradycardia:::vagal gastric fu...|Procedure:::Clinical Finding:::Clinical Finding:::Observable Entity:::Procedu...|
+--------------------------------------------------------------------+-------------------------+-----------+---------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_snomed_findings_aux_concepts|
|Compatibility:|Healthcare NLP 5.3.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[mpnet_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|2.2 GB|
|Case sensitive:|false|

## Dependency

This model can be used with spark v3.4.0 and above versions.

## References

This model is trained with the augmented version of NIH September 2023 SNOMED CT United States (US) Edition.
