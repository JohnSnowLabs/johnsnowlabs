---
layout: model
title: Sentence Entity Resolver for ICD-O (sbiobert_base_cased_mli embeddings)
author: John Snow Labs
name: sbiobertresolve_icdo
language: en
nav_key: models
repository: clinical/models
date: 2020-11-27
task: Entity Resolution
edition: Healthcare NLP 2.6.4
spark_version: 2.4
tags: [clinical,entity_resolution,en]
supported: true
annotator: SentenceEntityResolverModel
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description
This model maps extracted medical entities to ICD-O codes using Bert Sentence Embeddings.

Given an oncological entity found in the text (via NER models like ner_jsl), it returns top terms and resolutions along with the corresponding `Morphology` codes comprising of `Histology` and `Behavior` codes.

## Predicted Entities 
ICD-O Codes and their normalized definition with ``sbiobert_base_cased_mli`` embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/24.Improved_Entity_Resolvers_in_SparkNLP_with_sBert.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}{:target="_blank"}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icdo_en_2.6.4_2.4_1606235766320.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icdo_en_2.6.4_2.4_1606235766320.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}


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
.setOutputCol("embeddings")

ner = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
.setInputCols(["sentence", "token", "embeddings"])\
.setOutputCol("ner")\

ner_converter = NerConverterInternal()\
.setInputCols(["sentence", "token", "ner"])\
.setOutputCol("ner_chunk")\
.setWhiteList(["Oncological"])

c2doc = Chunk2Doc()\
.setInputCols("ner_chunk")\
.setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
.setInputCols(["ner_chunk_doc"])\
.setOutputCol("sentence_embeddings")\


resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icdo", "en", "clinical/models") \
.setInputCols(["sentence_embeddings"]) \
.setOutputCol("resolution")\
.setDistanceFunction("EUCLIDEAN")\


resolver_pipeline = Pipeline(stages = [
  document_assembler,
  sentenceDetectorDL,
  tokenizer,
  word_embeddings,
  ner,
  ner_converter,
  c2doc,
  sbert_embedder,
  resolver
  ])

empty_data = spark.createDataFrame([[""]]).toDF("text")
model = resolver_pipeline.fit(empty_data)

text="""In our patient experiencing intestinal bleeding and complaining of chest swelling, samples were taken, revealing the presence of adenomyoepitelioma and mucinous adenocarcinoma."""

lmodel = LightPipeline(model)
result = lmodel.fullAnnotate(text)
```
```scala
val document_assembler = new DocumentAssembler()
  .setInputCol("text") 
  .setOutputCol("document") 

val sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
  .setInputCols(Array("document")) 
  .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence")) 
  .setOutputCol("token") 

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
  .setInputCols(Array("sentence","token")) 
  .setOutputCol("embeddings") 

val ner = MedicalNerModel.pretrained("ner_jsl","en","clinical/models")
  .setInputCols(Array("sentence","token","embeddings")) 
  .setOutputCol("ner") 

val ner_converter = new NerConverterInternal()
  .setInputCols(Array("sentence","token","ner")) 
  .setOutputCol("ner_chunk") 
  .setWhiteList(Array("Oncological")) 

val c2doc = new Chunk2Doc()
  .setInputCols("ner_chunk") 
  .setOutputCol("ner_chunk_doc") 

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
  .setInputCols(Array("ner_chunk_doc")) 
  .setOutputCol("sentence_embeddings") 

val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icdo","en","clinical/models")
  .setInputCols(Array("sentence_embeddings")) 
  .setOutputCol("resolution") 
  .setDistanceFunction("EUCLIDEAN") 

val resolver_pipeline = val Pipeline(stages = new Array(
    document_assembler, 
    sentenceDetectorDL,
    tokenizer, 
    word_embeddings,
    ner,
    ner_converter,
    c2doc, 
    sbert_embedder, 
    resolver )) 

val empty_data = Seq("") .toDF("text") 
val model = resolver_pipeline.fit(empty_data) 
val text="In our patient experiencing intestinal bleeding and complaining of chest swelling,samples were taken,revealing the presence of adenomyoepitelioma and mucinous adenocarcinoma." 
val lmodel = new LightPipeline(model)
val result = lmodel.fullAnnotate(text) 
```

</div>

## Results

```bash
|   |                  chunks | begin | end |      entity |   code | confidence |                                                                        all_codes |                                                                                                                                                                                                                                                                            resolutions |
|--:|------------------------:|------:|----:|------------:|-------:|-----------:|---------------------------------------------------------------------------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| 0 |      adenomyoepitelioma |   129 | 146 | Oncological | 8983/3 |     0.9049 |                                         [8983/3, 8562/3, 8413/3, 9522/3, 9523/3] |                                                                                                                                  [Adenomyoepithelioma with carcinoma, Epithelial-myoepithelial carcinoma, Eccrine adenocarcinoma, Olfactory neuroblastoma, Olfactory neuroepithelioma] |
| 1 | mucinous adenocarcinoma |   152 | 174 | Oncological | 8480/3 |    0.74355 | [8480/3, 8481/3, 8420/3, 8253/2, 8550/3, 8290/3, 8262/3, 8253/3, 8323/3, 8213/3] | [Mucinous adenocarcinoma , Mucin-producing adenocarcinoma, Ceruminous adenocarcinoma, Adenocarcinoma in situ, mucinous, Acinar cell carcinoma, Oxyphilic adenocarcinoma, Villous adenocarcinoma, Invasive mucinous adenocarcinoma, Mixed cell adenocarcinoma, Serrated adenocarcinoma] |
```

{:.model-param}
## Model Information

{:.table-model}
|---------------|---------------------|
| Name:         | sbiobertresolve_icdo        |
| Type:          | SentenceEntityResolverModel     |
| Compatibility: | Spark NLP 2.6.4 +               |
| License:       | Licensed            |
| Edition:       | Official          |
|Input labels:        | [ner_chunk, chunk_embeddings]     |
|Output labels:       | [resolution]                 |
| Language:      | en                  |
| Dependencies: | sbiobert_base_cased_mli |


## Data Source
Trained on ICD-O Histology Behaviour dataset with ``sbiobert_base_cased_mli`` sentence embeddings.
https://apps.who.int/iris/bitstream/handle/10665/96612/9789241548496_eng.pdf