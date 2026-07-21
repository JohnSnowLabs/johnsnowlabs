---
layout: model
title: Mapping Phenotype Terms with Their Corresponding Synonyms
author: John Snow Labs
name: hpo_synonym_mapper
date: 2026-07-21
tags: [en, chunk_mapper, licensed, clinical, hpo, synonym]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.4
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps HPO phenotype terms found in free text to their exact, related, broad, and narrow synonyms, enabling standardized recognition and linking of phenotypic concepts across clinical and biomedical text via the `synonym` field. Trained on the Human Phenotype Ontology (HPO) 2026-06-23 release.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_synonym_mapper_en_6.4.0_3.4_1784660133556.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_synonym_mapper_en_6.4.0_3.4_1784660133556.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

entity_extractor = TextMatcherInternalModel().pretrained("hpo_matcher", "en", "clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("ner_chunk")\
    .setCaseSensitive(False)\
    .setMergeOverlapping(False)

hpo_synonym_mapper = ChunkMapperModel.pretrained("hpo_synonym_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["synonym"])

pipeline = Pipeline(stages=[document_assembler, tokenizer, entity_extractor, hpo_synonym_mapper])
data = spark.createDataFrame([["""The patient presents with memory impairment and seizures. Physical exam notable for microcephaly, hypotonia, micrognathia, and low-set ears. Head shape assessment revealed plagiocephaly. Cardiac evaluation revealed a ventricular septal defect."""]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

entity_extractor = medical.TextMatcherModel().pretrained("hpo_matcher", "en", "clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("ner_chunk")\
    .setCaseSensitive(False)\
    .setMergeOverlapping(False)

hpo_synonym_mapper = medical.ChunkMapperModel.pretrained("hpo_synonym_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["synonym"])

pipeline = nlp.Pipeline(stages=[document_assembler, tokenizer, entity_extractor, hpo_synonym_mapper])
data = spark.createDataFrame([["""The patient presents with memory impairment and seizures. Physical exam notable for microcephaly, hypotonia, micrognathia, and low-set ears. Head shape assessment revealed plagiocephaly. Cardiac evaluation revealed a ventricular septal defect."""]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val entityExtractor = TextMatcherInternalModel().pretrained("hpo_matcher", "en", "clinical/models")
    .setInputCols(Array("document", "token"))
    .setOutputCol("ner_chunk")
    .setCaseSensitive(false)
    .setMergeOverlapping(false)

val hpoSynonymMapper = ChunkMapperModel
    .pretrained("hpo_synonym_mapper", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("synonym"))

val pipeline = new Pipeline().setStages(Array(documentAssembler, tokenizer, entityExtractor, hpoSynonymMapper))
val data = Seq("""The patient presents with memory impairment and seizures. Physical exam notable for microcephaly, hypotonia, micrognathia, and low-set ears. Head shape assessment revealed plagiocephaly. Cardiac evaluation revealed a ventricular septal defect.""").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| term                      | synonym                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:--------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| seizures                  | {'exact_synonym': ['epileptic seizure', 'seizure'], 'related_synonym': ['epilepsy'], 'broad_synonym': [], 'narrow_synonym': []}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| micrognathia              | {'exact_synonym': ['decreased size of lower jaw', 'decreased size of mandible', 'hypoplasia of lower jaw', 'hypoplasia of mandible', 'hypoplastic mandible', 'hypoplastic mandible condyle', 'hypotrophic lower jaw', 'hypotrophic mandible', 'little lower jaw', 'little mandible', 'lower jaw deficiency', 'lower jaw hypoplasia', 'mandibular deficiency', 'mandibular hypoplasia', 'mandibular micrognathia', 'micrognathia of lower jaw', 'micromandible', 'robin mandible', 'severe hypoplasia of mandible', 'small jaw', 'small lower jaw', 'small mandible', 'underdevelopment of lower jaw', 'underdevelopment ... |
| plagiocephaly             | {'exact_synonym': ['flat head syndrome', 'flattening of cranial vault', 'flattening of cranium', 'flattening of skull', 'rhomboid shaped cranium', 'rhomboid shaped skull'], 'related_synonym': [], 'broad_synonym': ['asymmetry of the posterior cranium', 'asymmetry of the posterior head', 'asymmetry of the posterior skull', 'flat head', 'rhomboid shaped head'], 'narrow_synonym': ['deformational plagiocephaly', 'flattening of head', 'positional plagiocephaly']}                                                                                                                                               |
| microcephaly              | {'exact_synonym': ['abnormally small cranium', 'abnormally small skull', 'decreased circumference of cranium', 'decreased size of cranium', 'decreased size of skull', 'reduced head circumference', 'small cranium', 'small head circumference'], 'related_synonym': [], 'broad_synonym': ['abnormally small head', 'decreased size of head', 'small head', 'small skull'], 'narrow_synonym': ['small calvarium']}                                                                                                                                                                                                         |
| ventricular septal defect | {'exact_synonym': ['hole in heart wall separating two lower heart chambers', 'ventricular septal defects', 'ventriculoseptal defect', 'vsd'], 'related_synonym': [], 'broad_synonym': [], 'narrow_synonym': []}                                                                                                                                                                                                                                                                                                                                                                                                             |
| memory impairment         | {'exact_synonym': ['amnesia', 'forgetfulness', 'memory impairment', 'memory loss', 'memory problems', 'poor memory'], 'related_synonym': [], 'broad_synonym': [], 'narrow_synonym': []}                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| hypotonia                 | {'exact_synonym': ['low muscle tone', 'low or weak muscle tone', 'muscle hypotonia', 'muscular hypotonia'], 'related_synonym': [], 'broad_synonym': [], 'narrow_synonym': ['central hypotonia', 'peripheral hypotonia']}                                                                                                                                                                                                                                                                                                                                                                                                    |
| low-set ears              | {'exact_synonym': ['low set ears', 'low-set ears', 'low-set pinnae', 'lowset ears', 'melotia'], 'related_synonym': [], 'broad_synonym': [], 'narrow_synonym': []}                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_synonym_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|2.0 MB|