---
layout: model
title: Detect Anatomical Regions ((embeddings_clinical_medium)
author: John Snow Labs
name: ner_anatomy_emb_clinical_medium
date: 2023-05-15
tags: [ner, clinical, licensed, en, anatomy]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for anatomy terms. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_anatomy_emb_clinical_medium_en_4.4.1_3.0_1684136633973.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_anatomy_emb_clinical_medium_en_4.4.1_3.0_1684136633973.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

anatomy_ner = MedicalNerModel.pretrained('ner_anatomy_emb_clinical_medium' "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("anatomy_ner")
    
anatomy_ner_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "anatomy_ner"]) \
    .setOutputCol("anatomy_ner_chunk")

posology_ner_pipeline = Pipeline(stages=[
    documentAssembler, 
    sentenceDetector,
    tokenizer,
    word_embeddings,
    anatomy_ner,
    anatomy_ner_converter])

empty_data = spark.createDataFrame([[""]]).toDF("text")

posology_ner_model = posology_ner_pipeline.fit(empty_data)

results = posology_ner_model.transform(spark.createDataFrame([['''This is an 11-year-old female who comes in for two different things. 1. She was seen by the allergist. No allergies present, so she stopped her Allegra, but she is still real congested and does a lot of snorting. They do not notice a lot of snoring at night though, but she seems to be always like that. 2. On her right great toe, she has got some redness and erythema. Her skin is kind of peeling a little bit, but it has been like that for about a week and a half now.\nGeneral: Well-developed female, in no acute distress, afebrile.\nHEENT: Sclerae and conjunctivae clear. Extraocular muscles intact. TMs clear. Nares patent. A little bit of swelling of the turbinates on the left. Oropharynx is essentially clear. Mucous membranes are moist.\nNeck: No lymphadenopathy.\nChest: Clear.\nAbdomen: Positive bowel sounds and soft.\nDermatologic: She has got redness along the lateral portion of her right great toe, but no bleeding or oozing. Some dryness of her skin. Her toenails themselves are very short and even on her left foot and her left great toe the toenails are very short.''']]).toDF("text"))
```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
​
val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")
​
val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")
    
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_medium", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")
​
val anatomy_ner_model = MedicalNerModel.pretrained("ner_anatomy_emb_clinical_medium", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("anatomy_ner")
​
val anatomy_ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("anatomy_ner_chunk")
​
val posology_pipeline = new PipelineModel().setStages(Array(document_assembler, 
                                                   sentence_detector,
                                                   tokenizer,
                                                   word_embeddings,
                                                   anatomy_ner_model,
                                                   anatomy_ner_converter))
​
val data = Seq(""" This is an 11-year-old female who comes in for two different things. 1. She was seen by the allergist. No allergies present, so she stopped her Allegra, but she is still real congested and does a lot of snorting. They do not notice a lot of snoring at night though, but she seems to be always like that. 2. On her right great toe, she has got some redness and erythema. Her skin is kind of peeling a little bit, but it has been like that for about a week and a half now.\nGeneral: Well-developed female, in no acute distress, afebrile.\nHEENT: Sclerae and conjunctivae clear. Extraocular muscles intact. TMs clear. Nares patent. A little bit of swelling of the turbinates on the left. Oropharynx is essentially clear. Mucous membranes are moist.\nNeck: No lymphadenopathy.\nChest: Clear.\nAbdomen: Positive bowel sounds and soft.\nDermatologic: She has got redness along the lateral portion of her right great toe, but no bleeding or oozing. Some dryness of her skin. Her toenails themselves are very short and even on her left foot and her left great toe the toenails are very short.""").toDS.toDF("text")
​
val result = model.fit(data).transform(data)
```
</div>

## Results

```bash
|    | chunks              |   begin |   end | entities               |
|---:|:--------------------|--------:|------:|:-----------------------|
|  0 | skin                |     374 |   377 | Organ                  |
|  1 | Extraocular muscles |     574 |   592 | Multi-tissue_structure |
|  2 | Nares               |     613 |   617 | Multi-tissue_structure |
|  3 | turbinates          |     659 |   668 | Multi-tissue_structure |
|  4 | Oropharynx          |     683 |   692 | Multi-tissue_structure |
|  5 | Mucous membranes    |     716 |   731 | Cellular_component     |
|  6 | Neck                |     744 |   747 | Organism_subdivision   |
|  7 | bowel               |     802 |   806 | Multi-tissue_structure |
|  8 | skin                |     956 |   959 | Organ                  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_anatomy_emb_clinical_medium|
|Compatibility:|Healthcare NLP 4.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|2.8 MB|

## References

Trained on the Anatomical Entity Mention (AnEM) corpus with  [https://www.nactem.ac.uk/anatomy/](https://www.nactem.ac.uk/anatomy/)

## Benchmarking

```bash
                          label     precision  recall   f1-score    support
               tissue_structure       0.81      0.67      0.73       130
                          Organ       0.87      0.79      0.83        52
                           Cell       0.89      1.00      0.94       118
           Organism_subdivision       0.69      0.50      0.58        22
         Pathological_formation       0.96      0.91      0.94        58
             Cellular_component       0.65      0.65      0.65        26
             Organism_substance       0.93      0.86      0.89        43
              Anatomical_system       1.00      0.50      0.67         6
   Immaterial_anatomical_entity       1.00      0.67      0.80         6
                         Tissue       0.88      0.88      0.88        32
Developing_anatomical_structure       1.00      0.20      0.33         5
                      micro-avg       0.86      0.80      0.83       498
                      macro-avg       0.88      0.69      0.75       498
                   weighted-avg       0.86      0.80      0.82       498
```