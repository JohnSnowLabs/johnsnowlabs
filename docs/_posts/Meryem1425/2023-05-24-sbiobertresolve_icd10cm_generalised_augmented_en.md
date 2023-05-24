---
layout: model
title: Sentence Entity Resolver for ICD10-CM (general 3 character codes)
author: John Snow Labs
name: sbiobertresolve_icd10cm_generalised_augmented
date: 2023-05-24
tags: [licensed, en, clinical, entity_resolution]
task: Entity Resolution
language: en
edition: Healthcare NLP 4.4.2
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted medical entities to ICD10-CM codes using sbiobert_base_cased_mli Sentence Bert Embeddings. It predicts ICD codes up to 3 characters (according to ICD10 code structure the first three characters represent general type of the injury or disease).

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_ICD10_CM/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/24.Improved_Entity_Resolvers_in_SparkNLP_with_sBert.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_generalised_augmented_en_4.4.2_3.0_1684930238103.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_generalised_augmented_en_4.4.2_3.0_1684930238103.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

sbiobertresolve_icd10cm_generalised resolver model must be used with sbiobert_base_cased_mli as embeddings ner_clinical as NER model. PROBLEM set in .setWhiteList().

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverter()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(['PROBLEM'])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")

icd10_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_generalised_augmented","en", "clinical/models")\
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

nlpPipeline = Pipeline(stages=[document_assembler, 
                               sentence_detector, 
                               tokenizer, 
                               word_embeddings, 
                               clinical_ner, 
                               ner_converter, 
                               chunk2doc, 
                               sbert_embedder, 
                               icd10_resolver])

data = spark.createDataFrame([["This is an 82 - year-old male with a history of prior tobacco use , hypertension , chronic renal insufficiency , COPD , gastritis , and TIA who initially presented to Braintree with a non-ST elevation MI and Guaiac positive stools , transferred to St . Margaret\'s Center for Women & Infants for cardiac catheterization with PTCA to mid LAD lesion complicated by hypotension and bradycardia requiring Atropine , IV fluids and transient dopamine possibly secondary to vagal reaction , subsequently transferred to CCU for close monitoring , hemodynamically stable at the time of admission to the CCU ."]]).toDF("text")

results = nlpPipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList("PROBLEM")

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols("ner_chunk_doc")
    .setOutputCol("sbert_embeddings")

val icd10_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_generalised_augmented","en", "clinical/models")
    .setInputCols("sbert_embeddings") 
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(document_assembler, 
                               sentence_detector, 
                               tokenizer, 
                               word_embeddings, 
                               clinical_ner, 
                               ner_converter, 
                               chunk2doc, 
                               sbert_embedder, 
                               icd10_resolver))

val data = Seq("This is an 82 - year-old male with a history of prior tobacco use , hypertension , chronic renal insufficiency , COPD , gastritis , and TIA who initially presented to Braintree with a non-ST elevation MI and Guaiac positive stools , transferred to St . Margaret\'s Center for Women & Infants for cardiac catheterization with PTCA to mid LAD lesion complicated by hypotension and bradycardia requiring Atropine , IV fluids and transient dopamine possibly secondary to vagal reaction , subsequently transferred to CCU for close monitoring , hemodynamically stable at the time of admission to the CCU .").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
| ner_chunk                   | entity   | icd10_code   | all_codes                                                                        | resolutions                                                                                                                                                                                                                                                                                                                           |
|-----------------------------|----------|--------------|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| hypertension                | PROBLEM  | I10          | I10, Z86, I15, Z87, P29, Z82, I11, Z13                                           | hypertension, hypertension monitored, secondary hypertension, h/o: hypertension, diastolic hypertension, fh: hypertension, hypertensive heart disease, suspected hypertension                                                                                                                                                         |
| chronic renal insufficiency | PROBLEM  | N18          | N18, P29, N19, P96, D63, N28, E79, N13                                           | chronic renal insufficiency, chronic renal failure, chronic progressive renal insufficiency, renal insufficiency, anaemia of chronic renal insufficiency, impaired renal function disorder, chronic renal failure syndrome, post-renal renal failure                                                                                  |
| COPD                        | PROBLEM  | J44          | J44, J98, J62, Z76, J81, J96, I27                                                | copd - chronic obstructive pulmonary disease, chronic lung disease (disorder), chronic lung disease, chronic obstructive pulmonary disease leaflet given, chronic pulmonary congestion (disorder), chronic respiratory failure (disorder), chronic pulmonary heart disease (disorder)                                                 |
| gastritis                   | PROBLEM  | K29          | K29, Z13, K52, A09, B96                                                          | gastritis, suspicion of gastritis, toxic gastritis, suppurative gastritis, bacterial gastritis                                                                                                                                                                                                                                        |
| TIA                         | PROBLEM  | S06          | S06, G45, I63, G46, G95                                                          | cerebral concussion, transient ischemic attack (disorder), thalamic stroke, occipital cerebral infarction (disorder), spinal cord stroke                                                                                                                                                                                              |
| a non-ST elevation MI       | PROBLEM  | I21          | I21, I24, I25, I63, I5A, M62, I60                                                | silent myocardial infarction (disorder), acute nontransmural infarction, mi - silent myocardial infarction, silent cerebral infarct, non-ischemic myocardial injury (non-traumatic)                                                                                                                                                   |
| Guaiac positive stools      | PROBLEM  | K92          | K92, R19, R15, P54, K38, R29, R85                                                | guaiac-positive stools, acholic stool (finding), fecal overflow, fecal occult blood positive, appendicular fecalith, slump test positive, anal swab culture positive (finding)                                                                                                                                                        |
| mid LAD lesion              | PROBLEM  | I21          | I21, Q24, Q21, I49, I51, Q28, Q20, I25                                           | stemi involving left anterior descending coronary artery, overriding left ventriculoarterial valve, double outlet left atrium, left atrial rhythm (finding), disorder of left atrium, left dominant coronary system, abnormality of left atrial appendage, aneurysm of patch of left ventricular outflow tract                        |
| hypotension                 | PROBLEM  | I95          | I95, H44, T50, G96, O26                                                          | hypotension, globe hypotension, drug-induced hypotension, intracranial hypotension, supine hypotensive syndrome                                                                                                                                                                                                                       |
| bradycardia                 | PROBLEM  | O99          | O99, P29, R00, R94, R25, I49, R41, R06                                           | bradycardia, bradycardia (finding), sinus bradycardia, ecg: bradycardia, bradykinesia, nodal escape bradycardia, bradykinesis, bradypnea                                                                                                                                                                                              |
| vagal reaction              | PROBLEM  | R55          | R55, G52, I73, R06, R09, R19, I44, Z59, R29, K59, I87, R45, I99, O33             | vaso vagal episode, vagus nerve finding, vasomotor reaction, agonal respiration, peripheral vasoconstriction (finding), abdominal muscle tone - finding, parasystolic beat, vagabond, galant reflex finding, reflex dilation of anus (finding), jugular venous distension, agonizing state, circulation reacts, midpelvic contraction |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd10cm_generalised_augmented|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|1.5 GB|
|Case sensitive:|false|