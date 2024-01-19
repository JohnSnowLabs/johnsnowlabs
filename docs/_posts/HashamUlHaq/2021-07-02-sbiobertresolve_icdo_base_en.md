---
layout: model
title: Sentence Entity Resolver for ICD-O (base)
author: John Snow Labs
name: sbiobertresolve_icdo_base
date: 2021-07-02
tags: [entity_resolution, licensed, en, clinical]
task: Entity Resolution
language: en
nav_key: models
edition: Healthcare NLP 3.1.0
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted medical entities to ICD-O codes (Topography & Morphology codes) using BioBert Sentence Embeddings.

Given an oncological entity found in the text (via NER models like ner_jsl), it returns top terms and resolutions along with the corresponding ICD-O codes to present more granularity with respect to body parts mentioned. It also returns the original `Topography` codes, `Morphology` codes comprising of `Histology` and `Behavior` codes, and descriptions in the aux metadata.


## Predicted Entities

ICD-O Codes and their normalized definition with `sbiobert_base_cased_mli` embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/24.Improved_Entity_Resolvers_in_SparkNLP_with_sBert.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icdo_base_en_3.1.0_3.0_1625252163641.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icdo_base_en_3.1.0_3.0_1625252163641.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

```sbiobertresolve_icdo_base``` resolver model must be used with ```sbiobert_base_cased_mli``` as embeddings ```ner_jsl``` as NER model. ```Oncologocal``` set in ```.setWhiteList()```.

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
  .setOutputCol("sbert_embeddings")\


resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icdo_base","en", "clinical/models") \
  .setInputCols(["sbert_embeddings"]) \
  .setOutputCol("resolution")\
  .setDistanceFunction("EUCLIDEAN")


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

data = spark.createDataFrame([["""The patient is a very pleasant 61-year-old female with a strong family history of colon polyps. The patient reports her first polyps noted at the age of 50. We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. She also has history of several malignancies in the family. Her father died of a brain tumor at the age of 81. Her sister died at the age of 65 acinar cell carcinoma of breast. She has two maternal aunts with history of Non-small cell carcinoma of lower lobe both of whom were smoker. Also a paternal grandmother who was diagnosed with leukemia at 86 and a paternal grandfather who had B-cell lymphoma."""]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)
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
 .setOutputCol("sbert_embeddings") 

val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icdo_base","en","clinical/models")
 .setInputCols(Array("sbert_embeddings")) 
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

val data = spark.createDataFrame(Array(Array("The patient is a very pleasant 61-year-old female with a strong family history of colon polyps. The patient reports her first polyps noted at the age of 50. We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. She also has history of several malignancies in the family. Her father died of a brain tumor at the age of 81. Her sister died at the age of 65 acinar cell carcinoma of breast. She has two maternal aunts with history of Non-small cell carcinoma of lower lobe both of whom were smoker. Also a paternal grandmother who was diagnosed with leukemia at 86 and a paternal grandfather who had B-cell lymphoma."))).toDF("text") 
val result = resolver_pipeline.fit(data).transform(data) 
```


{:.nlu-block}
```python
import nlu
nlu.load("en.resolve.icdo.base").predict("""The patient is a very pleasant 61-year-old female with a strong family history of colon polyps. The patient reports her first polyps noted at the age of 50. We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. She also has history of several malignancies in the family. Her father died of a brain tumor at the age of 81. Her sister died at the age of 65 acinar cell carcinoma of breast. She has two maternal aunts with history of Non-small cell carcinoma of lower lobe both of whom were smoker. Also a paternal grandmother who was diagnosed with leukemia at 86 and a paternal grandfather who had B-cell lymphoma.""")
```

</div>

## Results

```bash
+--------------------------------------+-----+---+-----------+------------+----------------------------------------+
|                                 chunk|begin|end|  ner_label|        code|                             resolutions|
+--------------------------------------+-----+---+-----------+------------+----------------------------------------+
|                          mesothelioma|  255|266|Oncological|      9050/3|Mesothelioma, malignant:::Epithelioid...|
|                          malignancies|  301|312|Oncological|      8000/3|Neoplasm, malignant:::Tumor cells, ma...|
|                           brain tumor|  350|360|Oncological|8001/3-C71.7|Tumor cells, malignant of brain stem:...|
|       acinar cell carcinoma of breast|  413|443|Oncological|8550/3-C50.1|Acinar cell carcinoma of central port...|
|Non-small cell carcinoma of lower lobe|  489|526|Oncological|8046/3-C34.3|Non-small cell carcinoma of lower lob...|
|                              leukemia|  605|612|Oncological|     980-994|Leukemias:::Lymphoid leukemias:::Myel...|
|                       B-cell lymphoma|  655|669|Oncological|     967-969|Mature B-cell lymphomas:::Splenic mar...|
+--------------------------------------+-----+---+-----------+------------+----------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icdo_base|
|Compatibility:|Healthcare NLP 3.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sbert_embeddings]|
|Output Labels:|[icdo_code]|
|Language:|en|
|Case sensitive:|false|

## Data Source

Trained on ICD-O Histology Behaviour dataset with `sbiobert_base_cased_mli` sentence embeddings. https://apps.who.int/iris/bitstream/handle/10665/96612/9789241548496_eng.pdf