---
layout: model
title: Pipeline for Medical Subject Heading (MeSH) Sentence Entity Resolver
author: John Snow Labs
name: mesh_resolver_pipeline
date: 2024-01-25
tags: [licensed, en, entity_resolution, clinical, pipeline, mesh]
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

This advanced pipeline extracts clinical entities from clinical texts and utilizes the `sbiobert_base_cased_mli` Sentence Bert Embeddings to map these entities to their corresponding Medical Subject Heading (MeSH) codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/mesh_resolver_pipeline_en_5.2.1_3.0_1706187452795.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/mesh_resolver_pipeline_en_5.2.1_3.0_1706187452795.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("mesh_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy with fluid biopsies, which were performed, which revealed malignant mesothelioma.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("mesh_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy with fluid biopsies, which were performed, which revealed malignant mesothelioma.""")

```
</div>

## Results

```bash
|    | chunks                     |   begin |   end | entities   | mesh_code   | description             | resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---:|:---------------------------|--------:|------:|:-----------|:------------|:------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | chest pain                 |      38 |    47 | PROBLEM    | D002637     | Chest Pain              | Chest Pain:::Chronic Pain:::Neck Pain:::Shoulder Pain:::Abdominal Pain:::Cancer Pain:::Facial Pain:::Visceral Pain:::Back Pain:::Labor Pain:::Flank Pain:::Eye Pain:::Pain:::Breakthrough Pain:::Paroxysmal Extreme Pain Disorder:::Musculoskeletal Pain:::Pain, Referred:::Acute Pain:::Myofascial Pain Syndromes:::Pain, Intractable:::Pain Perception:::Complex Regional Pain Syndromes:::Pelvic Pain:::Pelvic Girdle Pain:::Flail Chest                                                                                                                                               |
|  1 | bilateral pleural effusion |      67 |    92 | PROBLEM    | D010996     | Pleural Effusion        | Pleural Effusion:::Pericardial Effusion:::Pulmonary Edema:::Empyema, Pleural:::Pleural Diseases:::Pleural Effusion, Malignant:::Pleuropneumonia:::Laryngeal Edema:::Pleural Cavity:::Empyema:::Hemoptysis:::Pulmonary Eosinophilia:::Pleurisy:::Pulmonary Atelectasis:::Pneumopericardium:::Pericardial Effusion, Chronic:::Bronchopulmonary Sequestration:::Pleurotus:::Hemothorax:::Pneumoconiosis:::Pneumoperitoneum:::Subdural Effusion:::Pleurotopsis subgrisea:::Pleuropneumonia, Contagious:::Pleura                                                                               |
|  2 | the pathology              |     140 |   152 | TEST       | D010336     | Pathology               | Pathology:::Pathologic Processes:::Anus Diseases:::Disease Attributes:::malformins:::Upington disease:::Disease:::Diagnostic Errors:::Tangier Disease:::Hooft disease:::Pathological Conditions, Signs and Symptoms:::Pathological Conditions, Anatomical:::Athetosis:::Trefoil Factors:::Contracture:::Iatrogenic Disease:::injurin:::Weil Disease:::Pathology, Clinical:::Toxicological Phenomena:::withaphysalin O:::Phortress:::Arosurf:::Precipitating Factors:::Vitis                                                                                                               |
|  3 | the pericardectomy         |     168 |   185 | TREATMENT  | D010492     | Pericardiectomy         | Pericardiectomy:::Pulpectomy:::Pleurodesis:::Colpotomy:::Pulpotomy:::Glossectomy:::Posterior Capsulotomy:::Cecostomy:::Pleurotus dryinus:::Pneumonectomy:::Pharyngectomy:::Tonsillectomy:::Ocellularia pertusariiformis:::phascolosomine:::Alveolectomy:::Planococcus plakortidis:::Penicillium tardochrysogenum:::Pleurotus calyptratus:::Pseudoplagiostoma eucalypti:::Pericardiocentesis:::Mastoidectomy:::Pleurotus placentodes:::Pallidotomy:::Foraminotomy:::Pleurocolla compressa                                                                                                  |
|  4 | mesothelioma               |     226 |   237 | PROBLEM    | D000086002  | Mesothelioma, Malignant | Mesothelioma, Malignant:::Malignant mesenchymal tumor:::Myoepithelioma:::Ganoderma:::Neoplasms, Mesothelial:::Mixed Tumor, Mesodermal:::Hemangiopericytoma, Malignant:::Hebeloma mesophaeum:::Carcinoma, Medullary:::Leiomyosarcoma:::Ganoderma mexicanum:::Myxosarcoma:::Sarcosoma mexicanum:::Plexosarcoma:::Myofibroma:::Ganoderma multipileum:::Dysgerminoma:::Leiomyomatosis:::Gliomastix murorum:::Fibroma:::aspergillomarasmine A:::Mucoepidermoid Tumor:::Melanoma:::Ampliotrema megalostoma:::Phoma mali                                                                         |
|  5 | chest tube placement       |     254 |   273 | TREATMENT  | D015505     | Chest Tubes             | Chest Tubes:::Thoracic Surgical Procedures:::Thoracic Diseases:::Respiratory Care Units:::Thoracoscopy:::Pulmonary Surgical Procedures:::Thoracoscopes:::Thoracic Cavity:::Thoracic Surgery:::Critical Care Outcomes:::Intubation:::Cardiac Catheters:::Thoracentesis:::Mediastinoscopy:::Thoracotomy:::Cardiovascular Surgical Procedures:::Respiratory System Agents:::Central Venous Catheters:::Tracheal Diseases:::Diagnostic Techniques, Respiratory System:::Airway Management:::Respiratory System Abnormalities:::Surgical Equipment:::Respiratory Center:::Mediastinal Diseases |
|  6 | drainage of the fluid      |     279 |   299 | PROBLEM    | D004322     | Drainage                | Drainage:::Fluid Shifts:::Bonain's liquid:::Liquid Ventilation:::Flowmeters:::Water Purification:::Fluids and Secretions:::Extravascular Lung Water:::Wetting Agents:::Body Water:::Suction:::Ultrafiltration:::Sack's solution:::Drainage, Sanitary:::Water Movements:::Bouin's solution:::Resuscitation:::Labyrinthine Fluids:::Extracellular Fluid:::Flushing:::Body Fluids:::Water Supply:::Filtration:::Osmoregulation:::Solutions                                                                                                                                                   |
|  7 | thoracoscopy               |     314 |   325 | TREATMENT  | D013906     | Thoracoscopy            | Thoracoscopy:::Thoracoscopes:::Thoracic Cavity:::Thoracoplasty:::Thoracic Wall:::Thoracic Duct:::Thoracica:::Thoracentesis:::Thorax:::Thoracic Nerves:::Thoracic Surgical Procedures:::Thoracotomy:::Laryngoscopy:::Mediastinoscopy:::Thoracic Surgery:::Laryngoscopes:::Radiography, Thoracic:::Bronchoscopy:::Thoracic Arteries:::Thoracic Vertebrae:::corynantheal:::Thoracic Diseases:::Chest Tubes:::Tracheotomy:::Trachea                                                                                                                                                           |
|  8 | fluid biopsies             |     332 |   345 | TEST       | D000073890  | Liquid Biopsy           | Liquid Biopsy:::Peritoneal Lavage:::Cyst Fluid:::Punctures:::Nasal Lavage Fluid:::Biopsy:::Fluids and Secretions:::Gastric Lavage:::Synovial Fluid:::Pericardial Fluid:::Follicular Fluid:::Labyrinthine Fluids:::Bronchoalveolar Lavage Fluid:::Aqueous Humor:::Bodily Secretions:::Subdural Effusion:::Saliva:::Salivary Calculi:::Nasal Lavage:::Punctal Plugs:::imacidins:::Sputum:::Arthrocentesis:::Spontaneous Perforation:::Splenosis                                                                                                                                             |
|  9 | malignant mesothelioma     |     385 |   406 | PROBLEM    | D000086002  | Mesothelioma, Malignant | Mesothelioma, Malignant:::Malignant mesenchymal tumor:::Hemangiopericytoma, Malignant:::Myxosarcoma:::Leiomyosarcoma:::Mast-Cell Sarcoma:::Myoepithelioma:::M-proteins (Myeloma):::Sarcosoma mexicanum:::Ampliotrema megalostoma:::Nielozyma melastomae:::Hebeloma mesophaeum:::Myeloma Proteins:::Mixed Tumor, Mesodermal:::Carcinoma, Medullary:::multiple myeloma M-proteins:::myeloma protein WIE:::myeloma protein Rou:::Myofibroma:::Histiocytoma, Malignant Fibrous:::Leiomyomatosis:::Myosarcoma:::Gliomastix murorum:::Sarcoma, Myeloid:::Multiple Myeloma                       |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|mesh_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.1 GB|

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