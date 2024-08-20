---
layout: model
title: ICD10CM Sentence Entity Resolver (Slim, normalized)
author: John Snow Labs
name: sbiobertresolve_icd10cm_slim_normalized
date: 2024-08-19
tags: [licensed, clinical, en, entity_resolution, icd10cm]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts to ICD10 CM codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. In this model, synonyms having low cosine similarity to unnormalized terms are dropped, making the model slim. It also returns the official resolution text within the brackets inside the metadata

## Predicted Entities

`ICD-10-CM Codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_slim_normalized_en_5.4.0_3.4_1724073576316.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_slim_normalized_en_5.4.0_3.4_1724073576316.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")


sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")


tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")


word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")


ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")\


ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])


c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc") 


sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)
    
icd_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_slim_normalized", "en", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("icd_code")\
    .setDistanceFunction("EUCLIDEAN")\
    .setReturnCosineDistances(True)
    
resolver_pipeline = Pipeline(
    stages = [
        document_assembler,
        sentenceDetectorDL,
        tokenizer,
        word_embeddings,
        ner,
        ner_converter,
        c2doc,
        sbert_embedder,
        icd_resolver
  ])

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis and obesity , presented with a one-week history of polyuria, polydipsia, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."""]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")


val sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
      .setInputCols(Array("document"))
      .setOutputCol("sentence")


val tokenizer = new Tokenizer()
      .setInputCols(Array("sentence"))
      .setOutputCol("token")


val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
      .setInputCols(Array("sentence", "token"))
      .setOutputCol("word_embeddings")


val ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
      .setInputCols(Array("sentence", "token", "word_embeddings"))
      .setOutputCol("ner")


val ner_converter = new NerConverterInternal()
      .setInputCols(Array("sentence", "token", "ner"))
      .setOutputCol("ner_chunk")
      .setWhiteList(Array("PROBLEM"))


val c2doc = new Chunk2Doc()
      .setInputCols(Array("ner_chunk"))
      .setOutputCol("ner_chunk_doc") 


val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
      .setInputCols(Array("ner_chunk_doc"))
      .setOutputCol("sentence_embeddings")
      .setCaseSensitive(False)
    
val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_slim_normalized", "en", "clinical/models")
      .setInputCols(Array("sentence_embeddings"))
      .setOutputCol("icd_code")
      .setDistanceFunction("EUCLIDEAN")
      .setReturnCosineDistances(True)

val resolver_pipeline = new PipelineModel().setStages(Array(document_assembler, 
                                                            sentenceDetectorDL, 
                                                            tokenizer, 
                                                            word_embeddings, 
                                                            ner, 
                                                            ner_converter,  
                                                            c2doc, 
                                                            sbert_embedder, 
                                                            resolver))


val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis and obesity , presented with a one-week history of polyuria, polydipsia, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection.").toDS.toDF("text")

val results = resolver_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
|    |   sent_id | ner_chunk                             | entity   | icd10cm_code   | resolutions                                                           | all_codes                                                | all_resolutions                                                                                                                                                            |
|---:|----------:|:--------------------------------------|:---------|:---------------|:----------------------------------------------------------------------|:---------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 |         0 | gestational diabetes mellitus         | PROBLEM  | O24.4          | gestational diabetes mellitus [gestational diabetes mellitus]         | ['O24.4', 'O24.41', 'Z86.32', 'O24.11', 'O24.81', 'P70...| ['gestational diabetes mellitus [gestational diabetes mellitus]', 'gestational diabetes mellitus in pregnancy [gestational diabetes mellitus in pregnancy]', 'personal h...|
|  1 |         0 | subsequent type two diabetes mellitus | PROBLEM  | E11            | type 2 diabetes mellitus [type 2 diabetes mellitus]                   | ['E11', 'E11.62', 'E11.5', 'E11.69', 'E11.59', 'E09', ...| ['type 2 diabetes mellitus [type 2 diabetes mellitus]', 'type 2 diabetes mellitus with skin complications [type 2 diabetes mellitus with skin complications]', 'type 2 d...|
|  2 |         0 | obesity                               | PROBLEM  | E66            | overweight and obesity [overweight and obesity]                       | ['E66', 'E66.3', 'E66.8', 'E66.0', 'E66.1', 'E88.810',...| ['overweight and obesity [overweight and obesity]', 'overweight [overweight]', 'other obesity [other obesity]', 'obesity due to excess calories [obesity due to excess c...|
|  3 |         0 | a body mass index                     | PROBLEM  | Z68            | body mass index [bmi] [body mass index [bmi]]                         | ['Z68', 'E65', 'L02.221', 'Z96.81', 'Y92.81', 'Y93.75'...| ['body mass index [bmi] [body mass index [bmi]]', 'localized adiposity [localized adiposity]', 'furuncle of abdominal wall [furuncle of abdominal wall]', 'presence of a...|
|  4 |         0 | polyuria                              | PROBLEM  | R35            | polyuria [polyuria]                                                   | ['R35', 'R35.81', 'R35.89', 'R31', 'R30.0', 'E72.01', ...| ['polyuria [polyuria]', 'nocturnal polyuria [nocturnal polyuria]', 'other polyuria [other polyuria]', 'hematuria [hematuria]', 'dysuria [dysuria]', 'cystinuria [cystinu...|
|  5 |         0 | polydipsia                            | PROBLEM  | R63.1          | polydipsia [polydipsia]                                               | ['R63.1', 'O40', 'G47.5', 'R63.2', 'R00.2', 'G47.1', '...| ['polydipsia [polydipsia]', 'polyhydramnios [polyhydramnios]', 'parasomnia [parasomnia]', 'polyphagia [polyphagia]', 'palpitations [palpitations]', 'hypersomnia [hypers...|
|  6 |         0 | vomiting                              | PROBLEM  | R11.1          | vomiting [vomiting]                                                   | ['R11.1', 'G43.A', 'R11.0', 'R11', 'R11.14', 'R11.12',...| ['vomiting [vomiting]', 'cyclical vomiting [cyclical vomiting]', 'nausea [nausea]', 'nausea and vomiting [nausea and vomiting]', 'bilious vomiting [bilious vomiting]', ...|
|  7 |         1 | a respiratory tract infection         | PROBLEM  | T17            | foreign body in respiratory tract [foreign body in respiratory tract] | ['T17', 'T81.4', 'T81.81', 'J95.851', 'T17.8', 'Z87.0'...| ['foreign body in respiratory tract [foreign body in respiratory tract]', 'infection following a procedure [infection following a procedure]', 'complication of inhalati...|

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd10cm_slim_normalized|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|437.8 MB|
|Case sensitive:|false|

## References

This model is trained with the 2025 version of ICD-10-CM dataset. 
