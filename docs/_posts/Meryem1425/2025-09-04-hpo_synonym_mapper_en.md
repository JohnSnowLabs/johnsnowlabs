---
layout: model
title: HPO Term Synonym Mapping
author: John Snow Labs
name: hpo_synonym_mapper
date: 2025-09-04
tags: [licensed, en, synonym, hpo, mapping, exact, broad, related]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.1.0
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps HPO terms to their exact, related, and broad synonyms, enabling standardized recognition and linking of phenotypic concepts across clinical and biomedical text.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_synonym_mapper_en_6.1.0_3.0_1756998808734.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_synonym_mapper_en_6.1.0_3.0_1756998808734.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

tokenizer= Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

entityExtractor = TextMatcherInternalModel().pretrained("hpo_matcher","en","clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("ner_chunk")\
    .setCaseSensitive(False)\
    .setMergeOverlapping(False)
 
mapperModel = ChunkMapperModel.pretrained("hpo_synonym_mapper","en","clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["synonym"])

mapper_pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    entityExtractor,
    mapperModel
])

model = mapper_pipeline.fit(spark.createDataFrame([['']]).toDF("text"))

result = model.transform(spark.createDataFrame([["""The patient, a 62-year-old male, presented with a neoplasm in the lung. He also reported progressive fatigue over the past three months and episodes of shortness of breath. On examination, hepatomegaly was noted, and laboratory results confirmed anemia."""]]).toDF("text"))


```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer= nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

entityExtractor = medical.TextMatcherModel().pretrained("hpo_matcher","en","clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("ner_chunk")\
    .setCaseSensitive(False)\
    .setMergeOverlapping(False)
 
mapperModel = medical.ChunkMapperModel.pretrained("hpo_synonym_mapper","en","clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["synonym"])

mapper_pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    entityExtractor,
    mapperModel
])

model = mapper_pipeline.fit(spark.createDataFrame([['']]).toDF("text"))

result = model.transform(spark.createDataFrame([["""The patient, a 62-year-old male, presented with a neoplasm in the lung. He also reported progressive fatigue over the past three months and episodes of shortness of breath. On examination, hepatomegaly was noted, and laboratory results confirmed anemia."""]]).toDF("text"))
                

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer= new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val entityExtractor = TextMatcherInternalModel().pretrained("hpo_matcher","en","clinical/models")
    .setInputCols(Array("document", "token"))
    .setOutputCol("ner_chunk")
    .setCaseSensitive(False)
    .setMergeOverlapping(False)
 
val mapperModel = ChunkMapperModel.pretrained("hpo_synonym_mapper","en","clinical/models")
    .setInputCols("ner_chunk")
    .setOutputCol("mappings")
    .setRels(Array("synonym"))

val mapper_pipeline = new Pipeline().setStages(Array(
    document_assembler,
    tokenizer,
    entityExtractor,
    mapperModel
))
    
val sample_texts = Seq("""The patient, a 62-year-old male, presented with a neoplasm in the lung. He also reported progressive fatigue over the past three months and episodes of shortness of breath. On examination, hepatomegaly was noted, and laboratory results confirmed anemia.""").toDF("text")

val result = mapper_pipeline.fit(sample_texts).transform(sample_texts)

```
</div>

## Results

```bash

+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|term               |synonym                                                                                                                                                                                                                 |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|shortness of breath|{'exact_synonym': ['dyspnea', 'abnormal breathing', 'breathing difficulty', 'difficult to breathe', 'difficulty breathing', 'dyspnoea', 'trouble breathing'], 'related_synonym': ['panting'], 'broad_synonym': []}      |
|fatigue            |{'exact_synonym': ['fatigue', 'tired', 'tiredness'], 'related_synonym': [], 'broad_synonym': []}                                                                                                                        |
|neoplasm           |{'exact_synonym': ['neoplasia', 'oncological abnormality', 'tumor', 'tumour'], 'related_synonym': ['cancer', 'oncology'], 'broad_synonym': ['abnormal tissue mass']}                                                    |
|anemia             |{'exact_synonym': ['anaemia', 'low number of red blood cells or haemoglobin', 'low number of red blood cells or hemoglobin'], 'related_synonym': ['decreased haemoglobin', 'decreased hemoglobin'], 'broad_synonym': []}|
|progressive        |{'exact_synonym': ['worsens with time'], 'related_synonym': ['progressive disorder'], 'broad_synonym': []}                                                                                                              |
|hepatomegaly       |{'exact_synonym': ['enlarged liver'], 'related_synonym': [], 'broad_synonym': []}                                                                                                                                       |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_synonym_mapper|
|Compatibility:|Healthcare NLP 6.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|1.6 MB|