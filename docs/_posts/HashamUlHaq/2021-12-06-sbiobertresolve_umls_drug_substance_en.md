---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes (Drug & Substance)
author: John Snow Labs
name: sbiobertresolve_umls_drug_substance
date: 2021-12-06
tags: [entity_resolution, en, clinical, licensed]
task: Entity Resolution
language: en
nav_key: models
edition: Healthcare NLP 3.3.3
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities to UMLS CUI codes. It is trained on `2021AB` UMLS dataset. The complete dataset has 127 different categories, and this model is trained on the `Clinical Drug`, `Pharmacologic Substance`, `Antibiotic`, `Hazardous or Poisonous Substance` categories using `sbiobert_base_cased_mli` embeddings.

## Predicted Entities

`Predicts UMLS codes for Drugs & Substances medical concepts`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/24.Improved_Entity_Resolvers_in_SparkNLP_with_sBert.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_drug_substance_en_3.3.3_3.0_1638802613409.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_drug_substance_en_3.3.3_3.0_1638802613409.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_posology_greedy","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("posology_ner")

ner_model_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","posology_ner"])\
    .setOutputCol("posology_ner_chunk")\
    .setWhiteList(["DRUG"])

chunk2doc = Chunk2Doc()\
    .setInputCols("posology_ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli",'en','clinical/models')\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_drug_substance","en", "clinical/models") \
     .setInputCols(["sbert_embeddings"]) \
     .setOutputCol("resolution")\
     .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_model_converter,
    chunk2doc,
    sbert_embedder,
    resolver
])


data = spark.createDataFrame([["She was immediately given hydrogen peroxide 30 mg to treat the infection on her leg, and has been advised Neosporin Cream for 5 days. She has a history of taking magnesium hydroxide 100mg/1ml and metformin 1000 mg."]]).toDF("text")

result = pipeline.fit(data).transform(data)
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

val ner_model = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")
      .setInputCols(Array("sentence", "token", "embeddings"))
      .setOutputCol("posology_ner")

val ner_model_converter = new NerConverterInternal()
      .setInputCols(Array("sentence", "token", "posology_ner"))
      .setOutputCol("posology_ner_chunk")
      .setWhiteList(["DRUG"])

val chunk2doc = new Chunk2Doc()
      .setInputCols("posology_ner_chunk")
      .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en","clinical/models")
      .setInputCols(Array("ner_chunk_doc"))
      .setOutputCol("sbert_embeddings")
      .setCaseSensitive(False)
    
val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_drug_substance", "en", "clinical/models")
      .setInputCols(Array("sbert_embeddings"))
      .setOutputCol("resolution")
      .setDistanceFunction("EUCLIDEAN")

val p_model = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_model_converter,
    chunk2doc,
    sbert_embedder,
    resolver))
    
val data = Seq("She was immediately given hydrogen peroxide 30 mg to treat the infection on her leg, and has been advised Neosporin Cream for 5 days. She has a history of taking magnesium hydroxide 100mg/1ml and metformin 1000 mg.").toDF("text")  

val res = p_model.fit(data).transform(data)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.resolve.umls_drug_substance").predict("She was immediately given hydrogen peroxide 30 mg to treat the infection on her leg, and has been advised Neosporin Cream for 5 days. She has a history of taking magnesium hydroxide 100mg/1ml and metformin 1000 mg.")
```

</div>

## Results

```bash
+-----------------------------+-----+---+------+---------+--------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                    ner_chunk|begin|end|entity|umls_code|               description|                                               all_k_results|                                           all_k_resolutions|
+-----------------------------+-----+---+------+---------+--------------------------+------------------------------------------------------------+------------------------------------------------------------+
|      hydrogen peroxide 30 mg|   26| 48|  DRUG| C1126248|hydrogen peroxide 30 MG/ML|C1126248:::C0304655:::C1605252:::C0304656:::C1154260:::C2...|hydrogen peroxide 30 MG/ML:::Hydrogen peroxide solution 3...|
|              Neosporin Cream|  106|120|  DRUG| C0132149|           Neosporin Cream|C0132149:::C0306959:::C4722788:::C0704071:::C0698988:::C1...|Neosporin Cream:::Neosporin Ointment:::Neomycin Sulfate C...|
|magnesium hydroxide 100mg/1ml|  162|190|  DRUG| C1134402|magnesium hydroxide 100 MG|C1134402:::C1126785:::C4317023:::C4051486:::C4047137:::C1...|magnesium hydroxide 100 MG:::magnesium hydroxide 100 MG/M...|
|            metformin 1000 mg|  196|212|  DRUG| C0987664|         metformin 1000 MG|C0987664:::C2719784:::C0978482:::C2719786:::C4282269:::C2...|metformin 1000 MG:::metFORMIN hydrochloride 1000 MG:::MET...|
+-----------------------------+-----+---+------+---------+--------------------------+------------------------------------------------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_drug_substance|
|Compatibility:|Healthcare NLP 3.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_chunk_embeddings]|
|Output Labels:|[output]|
|Language:|en|
|Case sensitive:|false|

## Data Source

Trained on `2021AB` UMLS dataset’s `Clinical Drug`, `Pharmacologic Substance`, `Antibiotic`, `Hazardous or Poisonous Substance` categories. https://www.nlm.nih.gov/research/umls/index.html
