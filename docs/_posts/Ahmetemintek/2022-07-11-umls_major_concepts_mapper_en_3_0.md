---
layout: model
title: Mapping Entities (Major Clinical Concepts) with Corresponding UMLS CUI Codes
author: John Snow Labs
name: umls_major_concepts_mapper
date: 2022-07-11
tags: [umls, chunk_mapper, licensed, en]
task: Chunk Mapping
language: en
nav_key: models
edition: Healthcare NLP 4.0.0
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps entities (Major Clinical Concepts) with corresponding UMLS CUI codes.

`Important Note`: Mappers extract additional information such as extended descriptions and categories related to Concept codes (such as RxNorm, ICD10, CPT, MESH, NDC, UMLS, etc.). They generally take Concept Codes, which are the outputs of EntityResolvers, as input. When creating a pipeline that contains 'Mapper', it is necessary to use the ChunkMapperModel after an EntityResolverModel.


## Predicted Entities

`umls_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_major_concepts_mapper_en_4.0.0_3.0_1657579020337.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_major_concepts_mapper_en_4.0.0_3.0_1657579020337.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained("ner_medmentions_coarse", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("clinical_ner")

ner_model_converter = NerConverterInternal()\
    .setInputCols("sentence", "token", "clinical_ner")\
    .setOutputCol("ner_chunk")

chunkerMapper = ChunkMapperModel.pretrained("umls_major_concepts_mapper", "en", "clinical/models")\
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


test_data = spark.createDataFrame([["The patient complains of pustules after falling from stairs. Also,  she has a history of quadriceps tendon rupture"]]).toDF("text")

result = mapper_pipeline.fit(test_data).transform(test_data)

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
       .pretrained("ner_medmentions_coarse", "en", "clinical/models")
       .setInputCols(Array("sentence", "token", "embeddings"))
       .setOutputCol("clinical_ner")

val ner_model_converter = new NerConverterInternal()
       .setInputCols("sentence", "token", "clinical_ner")
       .setOutputCol("ner_chunk")

val chunkerMapper = ChunkMapperModel
       .pretrained("umls_major_concepts_mapper", "en", "clinical/models")
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


val test_data = Seq("The patient complains of pustules after falling from stairs. Also,  she has a history of quadriceps tendon rupture").toDF("text")

val result = mapper_pipeline.fit(test_data).transform(test_data) 
```


{:.nlu-block}
```python
import nlu
nlu.load("en.map_entity.umls_major_concepts_mapper").predict("""The patient complains of pustules after falling from stairs. Also,  she has a history of quadriceps tendon rupture""")
```

</div>

## Results

```bash
+-------------------------+---------+
|ner_chunk                |umls_code|
+-------------------------+---------+
|pustules                 |C0241157 |
|stairs                   |C4300351 |
|quadriceps tendon rupture|C0263968 |
+-------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_major_concepts_mapper|
|Compatibility:|Healthcare NLP 4.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|37.0 MB|

## References

Data sampled from https://www.nlm.nih.gov/research/umls/index.html