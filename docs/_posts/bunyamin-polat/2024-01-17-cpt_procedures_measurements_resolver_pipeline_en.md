---
layout: model
title: Pipeline for CPT Sentence Entity Resolver
author: John Snow Labs
name: cpt_procedures_measurements_resolver_pipeline
date: 2024-01-17
tags: [licensed, en, entity_resolution, clinical, pipeline, cpt]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline employs Sentence Bert Embeddings to map diverse medical entities, including diagnoses, treatments, tests, anatomical references, and demographic entities, to Current Procedural Terminology (CPT) codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/cpt_procedures_measurements_resolver_pipeline_en_5.2.1_3.0_1705493213071.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/cpt_procedures_measurements_resolver_pipeline_en_5.2.1_3.0_1705493213071.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("cpt_procedures_measurements_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. CT scan of the chest also revealed a large mediastinal lymph node.
We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma.
At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy, which were performed, which revealed epithelioid malignant mesothelioma.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("cpt_procedures_measurements_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. CT scan of the chest also revealed a large mediastinal lymph node.
We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma.
At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy, which were performed, which revealed epithelioid malignant mesothelioma.""")

```
</div>

## Results

```bash
|    | chunks               |   begin |   end | entities   |   cpt_code | resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | all_codes                                                                                                                                                   |
|---:|:---------------------|--------:|------:|:-----------|-----------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | pericardectomy       |     239 |   252 | Procedure  |      33030 | Pericardectomy [Pericardiectomy, subtotal or complete; without cardiopulmonary bypass]:::Pericardotomy [Pericardiotomy for removal of clot or foreign body (primary procedure)]:::Phrenicectomy [Transection or avulsion of; phrenic nerve]:::Omphalectomy [Umbilectomy, omphalectomy, excision of umbilicus (separate procedure)]:::Patellectomy [Patellectomy or hemipatellectomy]:::Dacryocystectomy [Excision of lacrimal sac (dacryocystectomy)]:::Parietal pleurectomy [Pleurectomy, parietal (separate procedure)]:::Excision, prepatellar bursa [Excision, prepatellar bursa]:::Partial resection of pericardium for drainage [Creation of pericardial window or partial resection for drainage]:::Pleurodesis (procedure) [Pleural scarification for repeat pneumothorax]:::Operculectomy, excision pericoronal tissues [Operculectomy, excision pericoronal tissues]:::Rhinectomy [Rhinectomy]:::Pericardiectomy, subtotal or complete [Pericardiectomy, subtotal or complete]:::Talectomy [Talectomy (astragalectomy)]:::Decortication and parietal pleurectomy [Decortication and parietal pleurectomy]:::Buccal frenectomy [Excision of frenum, labial or buccal (frenumectomy, frenulectomy, frenectomy)]:::Labyrinthectomy [Labyrinthectomy]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 33030:::33020:::64746:::49250:::27350:::68520:::32310:::27340:::33025:::32215:::41821:::1005708:::1006065:::28130:::32320:::40819:::1010234                 |
|  1 | chest tube placement |     321 |   340 | Procedure  |      39503 | Insertion of chest tube [Repair, neonatal diaphragmatic hernia, with or without chest tube insertion and with or without creation of ventral hernia]:::Chemotherapy administration into chest cavity requiring insertion of catheter [Chemotherapy administration into pleural cavity, requiring and including thoracentesis]:::Insertion of devices in chest cavity for radiation therapy guidance, accessed through the skin [Placement of interstitial device(s) for radiation therapy guidance (eg, fiducial markers, dosimeter), percutaneous, intra-thoracic, single or multiple]:::Incision of chest wall [Exploration for postoperative hemorrhage, thrombosis or infection; chest]:::Incision and exploration of chest cavity [Thoracotomy; with exploration]:::Insertion of catheter into chest artery for diagnosis or treatment including radiological supervision and interpretation [Selective catheter placement, vertebral artery, unilateral, with angiography of the ipsilateral vertebral circulation and all associated radiological supervision and interpretation, includes angiography of the cervicocerebral arch, when performed]:::Neck or chest procedure [Unlisted procedure, neck or thorax]:::Strapping of chest [Strapping; thorax]:::CAD CHEST RADIOGRAPH CONCURRENT W/INTERPRETATION [Computer-aided detection (CAD) (computer algorithm analysis of digital image data for lesion detection) with further physician review for interpretation and report, with or without digitization of film radiographic images, chest radiograph(s), performe...]:::Changing endotracheal tube [Tracheotomy tube change prior to establishment of fistula tract]:::Emergent surgical opening of windpipe for insertion of breathing tube [Tracheostomy, emergency procedure; cricothyroid membrane]:::VENTILATING TUBE RMVL REQUIRING GENERAL ANES [Ventilating tube removal requiring general anesthesia]:::Surgical Procedures on the Respiratory System [Surgical Procedures on the Respiratory System]:::Critical Care Services [Critical Care Services]:::Insertion of breathing sensor electrode or electrode array into chest wall [Insertion of chest wall respiratory sensor electrode or electrode array, including connection to pulse generator (List separately in addition to code for primary procedure)]:::Thoracoscopy, surgical; with control of traumatic hemorrhage | [Health Care Activity] - [Therapeutic or Preventive Procedure] [Thoracoscopy, surgical; with control of traumatic hemorrhage]:::Anesthesia for Intrathoracic Procedures [Anesthesia for Intrathoracic Procedures]:::Procedure on respiratory system [Unlisted respiratory procedure, diagnostic nuclear medicine]:::Pulmonary medical procedure [Intrapulmonary surfactant administration by a physician or other qualified health care professional through endotracheal tube] | 39503:::96440:::32553:::35820:::32100:::36226:::21899:::29200:::0174T:::31502:::31605:::69424:::1005690:::1013729:::0466T:::32654:::1002859:::78599:::94610 |
|  2 | thoracoscopy         |     381 |   392 | Procedure  |    1020900 | Thoracoscopy [Thoracoscopy]:::Thoracoscopy, surgical; with control of traumatic hemorrhage | [Health Care Activity] - [Therapeutic or Preventive Procedure] [Thoracoscopy, surgical; with control of traumatic hemorrhage]:::Thoracoscopy (procedure) [Thoracoscopy, surgical; with diagnostic wedge resection followed by anatomic lung resection (List separately in addition to code for primary procedure)]:::Thoracoscopy, surgical [Thoracoscopy, surgical]:::Thoracostomy [Exploration for postoperative hemorrhage, thrombosis or infection; chest]:::THORACOSCOPY DX MEDIASTINAL SPACE W/BIOPSY SPX [Thoracoscopy, diagnostic (separate procedure); mediastinal space, with biopsy]:::Thoracentesis (procedure) [Thoracentesis, needle or catheter, aspiration of the pleural space; with imaging guidance]:::EXC TRACHEAL STENOSIS&ANAST CERVICOTHORACIC [Excision tracheal stenosis and anastomosis; cervicothoracic]:::Tracheoscopy [Laryngoscopy direct, with or without tracheoscopy; for aspiration]:::Strapping of thorax (procedure) [Strapping; thorax]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 1020900:::32654:::32668:::1006014:::35820:::32606:::32555:::31781:::31515:::29200                                                                           |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|cpt_procedures_measurements_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.5 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel