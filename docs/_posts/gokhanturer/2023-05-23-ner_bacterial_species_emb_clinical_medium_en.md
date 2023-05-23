---
layout: model
title: Detect bacterial species (embedding_clinical_medium)
author: John Snow Labs
name: ner_bacterial_species_emb_clinical_medium
date: 2023-05-23
tags: [ner, clinical, bacterial_species, licensed, en]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.2
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Detect different types of species of bacteria in text using pretrained NER model.

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_BACTERIAL_SPECIES/){:.button.button-orange}
[Open in Colab](https://demo.johnsnowlabs.com/healthcare/NER_BACTERIAL_SPECIES/){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_bacterial_species_emb_clinical_medium_en_4.4.2_3.0_1684848483995.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_bacterial_species_emb_clinical_medium_en_4.4.2_3.0_1684848483995.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence") 

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_medium", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

species_ner = MedicalNerModel.pretrained("ner_bacterial_species_emb_clinical_medium", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("species_ner")
    
species_ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "species_ner"]) \
    .setOutputCol("species_ner_chunk")

species_ner_pipeline = Pipeline(stages=[
    documentAssembler, 
    sentenceDetector,
    tokenizer,
    word_embeddings,
    species_ner,
    species_ner_converter])

empty_data = spark.createDataFrame([[""]]).toDF("text")

species_ner_model = species_ner_pipeline.fit(empty_data)

results = species_ner_model.transform(spark.createDataFrame([[''' Proportions of Veillonella parvula and Prevotella melaninogenica were higher in saliva and on the lateral and dorsal surfaces of the tongue, while Streptococcus mitis and S. oralis were in significantly lower proportions in saliva and on the tongue dorsum. Cluster analysis resulted in the formation of 2 clusters with >85% similarity. Cluster 1 comprised saliva, lateral and dorsal tongue surfaces, while Cluster 2 comprised the remaining soft tissue locations. V. parvula, P. melaninogenica, Eikenella corrodens, Neisseria mucosa, Actinomyces odontolyticus, Fusobacterium periodonticum, F. nucleatum ss vincentii and Porphyromonas gingivalis were in significantly higher proportions in Cluster 1 and S. mitis, S. oralis and S. noxia were significantly higher in Cluster 2. These findings were confirmed using data from the 44 subjects providing plaque samples.''']]).toDF("text"))
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
    
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_large", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val species_ner_model = MedicalNerModel.pretrained("ner_bacterial_species_emb_clinical_medium", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("species_ner")

val species_ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "species_ner"))
    .setOutputCol("species_ner_chunk")

val species_pipeline = new PipelineModel().setStages(Array(document_assembler, 
                                                   sentence_detector,
                                                   tokenizer,
                                                   word_embeddings,
                                                   species_ner_model,
                                                   species_ner_converter))

val data = Seq(""" This is an 11-year-old female who comes in for two different things. 1. She was seen by the allergist. No allergies present, so she stopped her Allegra, but she is still real congested and does a lot of snorting. They do not notice a lot of snoring at night though, but she seems to be always like that. 2. On her right great toe, she has got some redness and erythema. Her skin is kind of peeling a little bit, but it has been like that for about a week and a half now.\nGeneral: Well-developed female, in no acute distress, afebrile.\nHEENT: Sclerae and conjunctivae clear. Extraocular muscles intact. TMs clear. Nares patent. A little bit of swelling of the turbinates on the left. Oropharynx is essentially clear. Mucous membranes are moist.\nNeck: No lymphadenopathy.\nChest: Clear.\nAbdomen: Positive bowel sounds and soft.\nDermatologic: She has got redness along the lateral portion of her right great toe, but no bleeding or oozing. Some dryness of her skin. Her toenails themselves are very short and even on her left foot and her left great toe the toenails are very short.""").toDS.toDF("text")

val result = model.fit(data).transform(data)
```
</div>

## Results

```bash
|    | chunks                      |   begin |   end | entities   |
|---:|:----------------------------|--------:|------:|:-----------|
|  0 | Veillonella parvula         |      16 |    34 | SPECIES    |
|  1 | Prevotella melaninogenica   |      40 |    64 | SPECIES    |
|  2 | Streptococcus mitis         |     148 |   166 | SPECIES    |
|  3 | S. oralis                   |     172 |   180 | SPECIES    |
|  4 | V. parvula                  |     464 |   473 | SPECIES    |
|  5 | P. melaninogenica           |     476 |   492 | SPECIES    |
|  6 | Eikenella corrodens         |     495 |   513 | SPECIES    |
|  7 | Neisseria mucosa            |     516 |   531 | SPECIES    |
|  8 | Actinomyces odontolyticus   |     534 |   558 | SPECIES    |
|  9 | Fusobacterium periodonticum |     561 |   587 | SPECIES    |
| 10 | F. nucleatum ss vincentii   |     590 |   614 | SPECIES    |
| 11 | Porphyromonas gingivalis    |     620 |   643 | SPECIES    |
| 12 | S. mitis                    |     703 |   710 | SPECIES    |
| 13 | S. oralis                   |     713 |   721 | SPECIES    |
| 14 | S. noxia                    |     727 |   734 | SPECIES    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_bacterial_species_emb_clinical_medium|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|2.8 MB|

## Benchmarking

```bash
       label      precision recall    f1-score  support
     SPECIES       0.80      0.82      0.81      1810
   micro-avg       0.80      0.82      0.81      1810
   macro-avg       0.80      0.82      0.81      1810
weighted-avg       0.80      0.82      0.81      1810
```
