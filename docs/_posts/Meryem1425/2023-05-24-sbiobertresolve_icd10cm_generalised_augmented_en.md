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

`sbiobertresolve_icd10cm_generalised` resolver model must be used with `sbiobert_base_cased_mli` as embeddings.


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
| ner_chunk                   | entity   | icd10_code | all_codes                                     | resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | -------- | ---------- | --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hypertension                | PROBLEM  | I10        | I10:::Z86:::I15:::Z87:::P29:::Z82:::I11:::Z13 | hypertension [hypertension]:::hypertension monitored [hypertension monitored]:::secondary hypertension [secondary hypertension]:::h/o: hypertension [h/o: hypertension]:::diastolic hypertension [diastolic hypertension]:::fh: hypertension [fh: hypertension]:::hypertensive heart disease [hypertensive heart disease]:::suspected hypertension [suspected hypertension]                                                                                                                                                                                                                                                                   |
| chronic renal insufficiency | PROBLEM  | N18        | N18:::P29:::N19:::P96:::D63:::N28:::E79:::N13 | chronic renal insufficiency [chronic renal insufficiency]:::chronic renal failure [chronic renal failure]:::chronic progressive renal insufficiency [chronic progressive renal insufficiency]:::renal insufficiency [renal insufficiency]:::anaemia of chronic renal insufficiency [anaemia of chronic renal insufficiency]:::impaired renal function disorder [impaired renal function disorder]:::chronic renal failure syndrome [chronic renal failure syndrome]:::post-renal renal failure [post-renal renal failure]                                                                                                                     |
| COPD                        | PROBLEM  | J44        | J44:::J98:::J62:::Z76:::J81:::J96:::I27       | copd - chronic obstructive pulmonary disease [copd - chronic obstructive pulmonary disease]:::chronic lung disease (disorder) [chronic lung disease (disorder)]:::chronic lung disease [chronic lung disease]:::chronic obstructive pulmonary disease leaflet given [chronic obstructive pulmonary disease leaflet given]:::chronic pulmonary congestion (disorder) [chronic pulmonary congestion (disorder)]:::chronic respiratory failure (disorder) [chronic respiratory failure (disorder)]:::chronic pulmonary heart disease (disorder) [chronic pulmonary heart disease (disorder)]                                                     |
| gastritis                   | PROBLEM  | K29        | K29:::Z13:::K52:::A09:::B96                   | gastritis [gastritis]:::suspicion of gastritis [suspicion of gastritis]:::toxic gastritis [toxic gastritis]:::suppurative gastritis [suppurative gastritis]:::bacterial gastritis [bacterial gastritis]                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TIA                         | PROBLEM  | S06        | S06:::G45:::I63:::G46:::G95                   | cerebral concussion [cerebral concussion]:::transient ischemic attack (disorder) [transient ischemic attack (disorder)]:::thalamic stroke [thalamic stroke]:::occipital cerebral infarction (disorder) [occipital cerebral infarction (disorder)]:::spinal cord stroke [spinal cord stroke]                                                                                                                                                                                                                                                                                                                                                   |    
| a non-ST elevation MI       | PROBLEM  | I21        | I21:::I24:::I25:::I63:::I5A:::M62:::I60       | silent myocardial infarction (disorder) [silent myocardial infarction (disorder)]:::acute nontransmural infarction [acute nontransmural infarction]:::mi - silent myocardial infarction [mi - silent myocardial infarction]:::silent cerebral infarct [silent cerebral infarct]:::non-ischemic myocardial injury (non-traumatic) [non-ischemic myocardial injury (non-traumatic)]:::nontraumatic ischemic infarction of muscle, unsp shoulder [nontraumatic ischemic infarction of muscle, unsp shoulder]:::nontraumatic ruptured cerebral aneurysm [nontraumatic ruptured cerebral aneurysm]                                                 |
| Guaiac positive stools      | PROBLEM  | K92        | K92:::R19:::R15:::P54:::K38:::R29:::R85       | guaiac-positive stools [guaiac-positive stools]:::acholic stool (finding) [acholic stool (finding)]:::fecal overflow [fecal overflow]:::fecal occult blood positive [fecal occult blood positive]:::appendicular fecalith [appendicular fecalith]:::slump test positive [slump test positive]:::anal swab culture positive (finding) [anal swab culture positive (finding)]                                                                                                                                                                                                                                                                   |
| mid LAD lesion              | PROBLEM  | I21        | I21:::Q24:::Q21:::I49:::I51:::Q28:::Q20:::I25 | stemi involving left anterior descending coronary artery [stemi involving left anterior descending coronary artery]:::overriding left ventriculoarterial valve [overriding left ventriculoarterial valve]:::double outlet left atrium [double outlet left atrium]:::left atrial rhythm (finding) [left atrial rhythm (finding)]:::disorder of left atrium [disorder of left atrium]:::left dominant coronary system [left dominant coronary system]:::abnormality of left atrial appendage [abnormality of left atrial appendage]:::aneurysm of patch of left ventricular outflow tract [aneurysm of patch of left ventricular outflow tract] |
| hypotension                 | PROBLEM  | I95        | I95:::H44:::T50:::G96:::O26                   | hypotension [hypotension]:::globe hypotension [globe hypotension]:::drug-induced hypotension [drug-induced hypotension]:::intracranial hypotension [intracranial hypotension]:::supine hypotensive syndrome [supine hypotensive syndrome]                                                                                                                                                                                                                                                                                                                                                                                                     |
| bradycardia                 | PROBLEM  | O99        | O99:::P29:::R00:::R94:::R25:::I49:::R41:::R06 | bradycardia [bradycardia]:::bradycardia (finding) [bradycardia (finding)]:::sinus bradycardia [sinus bradycardia]:::ecg: bradycardia [ecg: bradycardia]:::bradykinesia [bradykinesia]:::nodal escape bradycardia [nodal escape bradycardia]:::bradykinesis [bradykinesis]:::bradypnea [bradypnea]                                                                                                                                                                                                                                                                                                                                             |
| vagal reaction              | PROBLEM  | R55        | R55:::R29:::R00:::R94:::R25:::I49:::R41:::R06 | vagal reaction [vagal reaction]:::vasovagal reaction [vasovagal reaction]:::vasovagal syncope [vasovagal syncope]:::vagal stimulation effect [vagal stimulation effect]:::vagal stimulation (procedure) [vagal stimulation (procedure)]:::vasovagal shock [vasovagal shock]:::vasovagal attack [vasovagal attack]:::vasovagal symptoms [vasovagal symptoms]                                                                                                                                                                                                                                                                                   |
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
