---
layout: model
title: Sentence Entity Resolver for SNOMED Concepts
author: John Snow Labs
name: sbiobertresolve_snomed_findings_auxConcepts
date: 2024-02-14
tags: [en, licensed, resolver, auxconcepts, findings]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts to SNOMED codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. This is also capable of extracting `Clinical Findings `, `Morph Abnormality`, `Clinical Drug`, `Clinical Drug Form`, `Procedure`, `Substance`, `Physical Object`, and `Body Structure` concepts of SNOMED codes.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_findings_auxConcepts_en_5.2.1_3.0_1707933775763.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_findings_auxConcepts_en_5.2.1_3.0_1707933775763.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
documentAssembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained()\
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

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_findings_aux_concepts","en","clinical/models") \
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

text= """This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction. He was subsequently transferred to the CCU for close monitoring. He was hemodynamically stable at the time of admission to the CCU."""

df= spark.createDataFrame([[text]]).toDF("text")

result= nlpPipeline.fit(df).transform(df)
```
```scala
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val nerJsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner_jsl")

val nerJslConverter = new NerConverter()
  .setInputCols(Array("sentence", "token", "ner_jsl"))
  .setOutputCol("ner_jsl_chunk")
  .setWhiteList(Array("Procedure","Kidney_Disease","Cerebrovascular_Disease","Heart_Disease",
                     "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                     "EKG_Findings", "Communicable_Disease","Substance","Drug_Ingredient",
                     "Internal_organ_or_component","External_body_part_or_region","Modifier",
                     "Triglycerides","Alcohol","Smoking","Pregnancy","Hypertension","Obesity",
                     "Injury_or_Poisoning","Test","Hyperlipidemia","BMI","Oncological","Psychological_Condition","LDL","Diabetes"))

val chunk2doc = new Chunk2Doc()
  .setInputCols(Array("ner_jsl_chunk"))
  .setOutputCol("ner_chunk_doc")

val sbertEmbedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("sbert_embeddings")
  .setCaseSensitive(false)

val snomedResolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_findings_aux_concepts", "en", "clinical/models")
  .setInputCols(Array("sbert_embeddings"))
  .setOutputCol("snomed_code")
  .setDistanceFunction("EUCLIDEAN")

val nlpPipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  wordEmbeddings,
  nerJsl,
  nerJslConverter,
  chunk2doc,
  sbertEmbedder,
  snomedResolver
))

val text = """This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction. He was subsequently transferred to the CCU for close monitoring. He was hemodynamically stable at the time of admission to the CCU."""

val df = Seq(text).toDF("text")

val result = nlpPipeline.fit(df).transform(df)

```
</div>

## Results

```bash
+--------------------------------------------------+-------------------------+-----------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|                                             chunk|                    label|snomed_code|                                        resolution|                                         all_codes|                                   all_resolutions|                                    all_aux_labels|
+--------------------------------------------------+-------------------------+-----------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|                                           tobacco|                  Smoking|   57264008|                                           tobacco|57264008:::102407002:::39953003:::110483000:::2...|tobacco:::tobacco smoke:::tobacco - substance::...|Organism:::Substance:::Substance:::Clinical Fin...|
|                                      hypertension|             Hypertension|   38341003|                                      hypertension|38341003:::59621000:::270440008:::31992008:::16...|hypertension:::essential hypertension:::hyperte...|Clinical Finding:::Clinical Finding:::Clinical ...|
|                       chronic renal insufficiency|           Kidney_Disease|  723190009|                       chronic renal insufficiency|723190009:::709044004:::90688005:::425369003:::...|chronic renal insufficiency:::chronic renal imp...|Clinical Finding:::Clinical Finding:::Clinical ...|
|                                              COPD|Disease_Syndrome_Disorder|   13645005|                                              copd|13645005:::414400006:::223821008:::60349006:::2...|copd:::coning:::cos:::ump:::ling:::chive:::caev...|Clinical Finding:::Clinical Finding:::Location:...|
|                                         gastritis|Disease_Syndrome_Disorder|    4556007|                                         gastritis|4556007:::235656001:::1086791000119100:::425410...|gastritis:::chemical gastritis:::erosive gastri...|Clinical Finding:::Clinical Finding:::Clinical ...|
|                                               TIA|  Cerebrovascular_Disease|  266257000|                                               tia|266257000:::31597007:::160363004:::396145008:::...|tia:::tui:::fh: tia:::tidac:::tu:::trna:::timor...|Clinical Finding:::Organism:::Context-dependent...|
|                                       nonspecific|                 Modifier|   10003008|                                      non-specific|10003008:::261992003:::863956004:::300844001:::...|non-specific:::non-biological:::non-sterile:::n...|Qualifier Value:::Qualifier Value:::Qualifier V...|
|                                  ST-T abnormality|             EKG_Findings|  428750005|                      nonspecific st-t abnormality|428750005:::399504009:::55930002:::455721000124...|nonspecific st-t abnormality:::clinical t categ...|Clinical Finding:::Observable Entity:::Clinical...|
|                           cardiac catheterization|                Procedure|   41976001|                           cardiac catheterization|41976001:::705923009:::721968000:::467735004:::...|cardiac catheterization:::cardiac catheter:::ca...|Procedure:::Physical Object:::Record Artifact::...|
|occlusion of the mid left anterior descending c...|                  Symptom|  840313007|occlusion of mid left anterior descending coron...|840313007:::44771000087108:::840315000:::447810...|occlusion of mid left anterior descending coron...|Clinical Finding:::No_Concept_Class:::Clinical ...|
|                                       hypotension|               VS_Finding|   45007003|                                       hypotension|45007003:::241727003:::19721008:::28651003:::67...|hypotension:::induced hypotension:::globe hypot...|Clinical Finding:::Procedure:::Clinical Finding...|
|                                       bradycardia|               VS_Finding|   48867003|                                       bradycardia|48867003:::49710005:::44273001:::42177007:::426...|bradycardia:::sinus bradycardia:::reflex bradyc...|Clinical Finding:::Clinical Finding:::Clinical ...|
|                                          atropine|          Drug_Ingredient|   73949004|                                          atropine|73949004:::105075009:::349945006:::410493009:::...|atropine:::atropine measurement:::oral atropine...|Pharma/Biol Product:::Procedure:::Clinical Drug...|
|                                            fluids|          Drug_Ingredient|  255765007|                                             fluid|255765007:::246498002:::258442002:::251851008::...|fluid:::fluid used:::fluid sample:::fluid input...|Qualifier Value:::Attribute:::Specimen:::Observ...|
|                                          dopamine|          Drug_Ingredient|   59187003|                                          dopamine|59187003:::412383006:::37484001:::32779004:::41...|dopamine:::dopamine agent:::dopamine receptor::...|Pharma/Biol Product:::Substance:::Substance:::P...|
|                                    vagal reaction|                  Symptom|  128968000|                                 vagal stimulation|128968000:::398665005:::106160007:::88882009:::...|vagal stimulation:::vaso vagal episode:::vagus ...|Procedure:::Clinical Finding:::Clinical Finding...|
+--------------------------------------------------+-------------------------+-----------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_findings_auxConcepts|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|2.1 GB|
|Case sensitive:|false|
