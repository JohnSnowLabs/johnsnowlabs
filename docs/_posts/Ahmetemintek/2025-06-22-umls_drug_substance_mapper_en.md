---
layout: model
title: Mapping Entities (Drug Substances) with Corresponding UMLS CUI Codes
author: John Snow Labs
name: umls_drug_substance_mapper
date: 2025-06-22
tags: [umls, chunk_mapper, clinical, en, licensed]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps entities (Drug Substances) with their corresponding UMLS CUI codes.

## Predicted Entities

`umls_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_drug_substance_mapper_en_6.0.2_3.0_1750593298287.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_drug_substance_mapper_en_6.0.2_3.0_1750593298287.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\\
      .setInputCols(["sentence", "token"])\
      .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("clinical_ner")

ner_model_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "clinical_ner"])\
    .setOutputCol("ner_chunk")

chunkerMapper = ChunkMapperModel.pretrained("umls_drug_substance_mapper", "en", "clinical/models")\
      .setInputCols(["ner_chunk"])\
      .setOutputCol("mappings")\
      .setRels(["umls_code"])\
      .setLowerCase(True)

mapper_pipeline = Pipeline().setStages([
        document_assembler,
        sentence_detector,
        tokenizer,
        word_embeddings,
        ner_model,
        ner_model_converter,
        chunkerMapper])

data = spark.createDataFrame([["""The patient was given  metformin, lenvatinib and gallopamil 50 MG Oral Tablet."""]]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
document_assembler = nlp.DocumentAssembler()\
      .setInputCol('text')\
      .setOutputCol('document')

sentence_detector = nlp.SentenceDetector()\
      .setInputCols(["document"])\
      .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
      .setInputCols("sentence")\
      .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
      .setInputCols(["sentence", "token"])\
      .setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained("ner_posology_greedy", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("clinical_ner")

ner_model_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "clinical_ner"])\
    .setOutputCol("ner_chunk")

chunkerMapper = medical.ChunkMapperModel.pretrained("umls_drug_substance_mapper", "en", "clinical/models")\
      .setInputCols(["ner_chunk"])\
      .setOutputCol("mappings")\
      .setRels(["umls_code"])\
      .setLowerCase(True)

mapper_pipeline = Pipeline().setStages([
        document_assembler,
        sentence_detector,
        tokenizer,
        word_embeddings,
        ner_model,
        ner_model_converter,
        chunkerMapper])

data = spark.createDataFrame([["""The patient was given  metformin, lenvatinib and gallopamil 50 MG Oral Tablet."""]]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val sentence_detector = new SentenceDetector()
      .setInputCols(Array("document"))
      .setOutputCol("sentence")

val tokenizer = new Tokenizer()
      .setInputCols("sentence")
      .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel
      .pretrained("embeddings_clinical", "en", "clinical/models")
      .setInputCols(Array("sentence", "token"))
      .setOutputCol("embeddings")

val ner_model = MedicalNerModel
      .pretrained("ner_posology_greedy", "en", "clinical/models")
      .setInputCols(Array("sentence", "token", "embeddings"))
      .setOutputCol("clinical_ner")

val ner_model_converter = new NerConverterInternal()
      .setInputCols(Array("sentence", "token", "clinical_ner"))
      .setOutputCol("ner_chunk")

val chunkerMapper = ChunkMapperModel
      .pretrained("umls_drug_substance_mapper", "en", "clinical/models")
      .setInputCols(Array("ner_chunk"))
      .setOutputCol("mappings")
      .setRels(Array("umls_code"))

val mapper_pipeline = new Pipeline().setStages(Array(
                                                  document_assembler,
                                                  sentence_detector,
                                                  tokenizer,
                                                  word_embeddings,
                                                  ner_model,
                                                  ner_model_converter,
                                                  chunkerMapper))

val data = Seq("""The patient was given  metformin, lenvatinib and gallopamil 50 MG Oral Tablet.""").toDF("text")

val result = mapper_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------+---------+
|ner_chunk                   |umls_code|
+----------------------------+---------+
|metformin                   |C0025598 |
|lenvatinib                  |C2986924 |
|gallopamil 50 MG Oral Tablet|C0787234 |
+----------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_drug_substance_mapper|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|44.1 MB|

## References

2025AA UMLS dataset’s Clinical Drug, Pharmacologic Substance, Antibiotic, Hazardous or Poisonous Substance categories. https://www.nlm.nih.gov/research/umls/index.html