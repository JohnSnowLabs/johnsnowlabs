---
layout: model
title: Sentence Entity Resolver for SNOMED (sbiobertresolve_snomed_drug)
author: John Snow Labs
name: sbiobertresolve_snomed_drug
date: 2024-03-06
tags: [licensed, en, resolver, snomed, drug]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps detected drug entities to SNOMED codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_drug_en_5.3.0_3.0_1709717736012.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_drug_en_5.3.0_3.0_1709717736012.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", 'clinical/models') \
  .setInputCols(["document"]) \
  .setOutputCol("sentence")

tokenizer = Tokenizer()\
  .setInputCols(["sentence"])\
  .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
  .setInputCols(["sentence", "token"])\
  .setOutputCol("word_embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_posology", "en", "clinical/models") \
  .setInputCols(["sentence", "token", "word_embeddings"]) \
  .setOutputCol("ner")

ner_converter = NerConverterInternal() \
  .setInputCols(["sentence", "token", "ner"]) \
  .setOutputCol("ner_chunk")\
  .setWhiteList(['DRUG'])

c2doc = Chunk2Doc()\
  .setInputCols("ner_chunk")\
  .setOutputCol("ner_chunk_doc")

sentence_chunk_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
  .setInputCols(["ner_chunk_doc"])\
  .setOutputCol("sentence_embeddings")


snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_drug", "en", "clinical/models") \
  .setInputCols(["sentence_embeddings"]) \
  .setOutputCol("snomed_code")\
  .setDistanceFunction("EUCLIDEAN")\


resolver_pipeline = Pipeline(
    stages = [
          document_assembler,
          sentenceDetectorDL,
          tokenizer,
          word_embeddings,
          clinical_ner,
          ner_converter,
          c2doc,
          sentence_chunk_embeddings,
          snomed_resolver
          ])

model = resolver_pipeline.fit(spark.createDataFrame([[""]]).toDF("text"))
result = model.transform(spark.createDataFrame([["John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and lansoprazole for his GORD on 2023-12-01."]]).toDF("text"))
```
```scala
val document_assembler = DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("word_embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_posology", "en", "clinical/models")
  .setInputCols(Array("sentence", "token", "word_embeddings"))
  .setOutputCol("ner")

val ner_converter = NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")
  .setWhiteList(Array("DRUG"))

val c2doc = Chunk2Doc()
  .setInputCols("ner_chunk")
  .setOutputCol("ner_chunk_doc")

val sentence_chunk_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("sentence_embeddings")


val snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_drug", "en", "clinical/models")
  .setInputCols(Array("sentence_embeddings"))
  .setOutputCol("snomed_code")
  .setDistanceFunction("EUCLIDEAN")


resolver_pipeline = new Pipeline().setStages(
    document_assembler,
    sentenceDetectorDL,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    c2doc,
    sentence_chunk_embeddings,
    snomed_resolver)

data = Seq("John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and lansoprazole for his GORD on 2023-12-01.").toDF("text")

result = resolver_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------+-----+-----------+------------+--------------------------------------------------+--------------------------------------------------+
|       chunk|label|snomed_code|  resolution|                                         all_codes|                                   all_resolutions|
+------------+-----+-----------+------------+--------------------------------------------------+--------------------------------------------------+
|     aspirin| DRUG|    7947003|     aspirin|7947003:::358427004:::426365001:::412566001:::2...|aspirin:::oral aspirin:::aspirin, buffered:::bu...|
| paracetamol| DRUG|  387517004| paracetamol|387517004:::90332006:::437876006:::437818001:::...|paracetamol:::paracetamol product:::oral form p...|
| amoxicillin| DRUG|   27658006| amoxicillin|27658006:::350162003:::427483001:::350164002:::...|amoxicillin:::oral amoxicillin:::amoxicillin so...|
|lansoprazole| DRUG|  108666007|lansoprazole|108666007:::437961004:::441863009:::716069007::...|lansoprazole:::oral form lansoprazole:::dexlans...|
+------------+-----+-----------+------------+--------------------------------------------------+--------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_drug|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|283.0 MB|
|Case sensitive:|false|

## References

This model is trained with the augmented version of NIH September 2023 SNOMED CT United States (US) Edition.