---
layout: model
title: Mapping Phenotype Entities to HPO Parent Terms with Descriptions
author: John Snow Labs
name: hpo_parent_mapper
date: 2025-08-02
tags: [hpo, mapper, parent, en, licensed, clinical]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.0.4
spark_version: 3.4
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted phenotype entity codes to their corresponding parent terms in the Human Phenotype Ontology (HPO). For each parent term, it returns the HPO code, label, and official ontology description.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_parent_mapper_en_6.0.4_3.4_1754146291074.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_parent_mapper_en_6.0.4_3.4_1754146291074.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol('text')\
    .setOutputCol('document')

sentence_detector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols("sentence")\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_human_phenotype_gene_clinical_langtest","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")\

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\

hpo_mapper = ChunkMapperModel().pretrained("hpo_mapper","en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("hpo_code")\
    .setLowerCase(False)\

mapper_to_chunk = Mapper2Chunk()\
    .setInputCols(["hpo_code"])\
    .setOutputCol("hpo_code_chunk")

hpo_parent_mapper = ChunkMapperModel().pretrained("hpo_parent_mapper","en","clinical/models")\
    .setInputCols(["hpo_code_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["parents"]) #or resolution

pipeline = Pipeline().setStages([document_assembler,
                                 sentence_detector,
                                 tokenizer,
                                 word_embeddings,
                                 clinical_ner,
                                 ner_converter,
                                 hpo_mapper,
                                 mapper_to_chunk,
                                 hpo_parent_mapper])

text = ["""The patient presented with intellectual disability, accompanied by seizures that began in resolution.
Physical examination revealed microcephaly, hypotonia, and joint hypermobility. Additionally, there were signs
of abnormal facial shape, including a long philtrum and low-set ears. Cardiac assessment indicated a ventricular septal defect,
while brain MRI showed evidence of hypoplasia of the corpus callosum."""]

test_data = spark.createDataFrame([text]).toDF("text")

model = pipeline.fit(test_data)
res= model.transform(test_data)
```
```scala
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel
  .pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val clinicalNer = MedicalNerModel
  .pretrained("ner_human_phenotype_gene_clinical_langtest", "en", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")

val nerConverter = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")

val hpoMapper = ChunkMapperModel
  .pretrained("hpo_mapper", "en", "clinical/models")
  .setInputCols(Array("ner_chunk"))
  .setOutputCol("hpo_code")
  .setLowerCase(false)

val mapperToChunk = new Mapper2Chunk()
  .setInputCols(Array("hpo_code"))
  .setOutputCol("hpo_code_chunk")

val hpoParentMapper = ChunkMapperModel
  .pretrained("hpo_parent_mapper", "en", "clinical/models")
  .setInputCols(Array("hpo_code_chunk"))
  .setOutputCol("mappings")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  wordEmbeddings,
  clinicalNer,
  nerConverter,
  hpoMapper,
  mapperToChunk,
  hpoParentMapper
))

val data = Seq("""
  The patient presented with intellectual disability, accompanied by seizures that began in resolution.
  Physical examination revealed microcephaly, hypotonia, and joint hypermobility. Additionally, there were signs
  of abnormal facial shape, including a long philtrum and low-set ears. Cardiac assessment indicated a ventricular septal defect,
  while brain MRI showed evidence of hypoplasia of the corpus callosum.
""").toDF("text")

val model = pipeline.fit(data)
val res = model.transform(data)
```
</div>

## Results

```bash
+---------------------------------+--------------+------------------------------------------------------------------------------------------------------------------------+
|                        ner_chunk|hpo_code_chunk|                                                                                                          mapping_result|
+---------------------------------+--------------+------------------------------------------------------------------------------------------------------------------------+
|          intellectual disability|    HP:0001249|HP:0011446: Abnormality of mental function ## This includes abnormalities in speech, mood, emotions, behavior, and co...|
|                         seizures|    HP:0001250|HP:0012638: Abnormal nervous system physiology ## A functional anomaly of the nervous system. => HP:0000707: Abnormal...|
|                     microcephaly|    HP:0000252|HP:0007364: Aplasia/Hypoplasia of the cerebrum ## Absent/small cerebrum => HP:0002060: Abnormal cerebral morphology #...|
|                     low-set ears|    HP:0000369|HP:0000357: Abnormal location of ears ## Abnormal location of the ear. => HP:0000377: Abnormal pinna morphology ## Th...|
|        ventricular septal defect|    HP:0001629|HP:0010438: Abnormal ventricular septum morphology ## A structural abnormality of the interventricular septum. => HP:...|
|hypoplasia of the corpus callosum|    HP:0002079|HP:0007370: Aplasia/Hypoplasia of the corpus callosum ## Absence or underdevelopment of the corpus callosum. => HP:00...|
+---------------------------------+--------------+------------------------------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_parent_mapper|
|Compatibility:|Healthcare NLP 6.0.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[hpo_code_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|9.4 MB|