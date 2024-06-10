---
layout: model
title: Sentence Entity Resolver for SNOMED Veterinary
author: John Snow Labs
name: sbiobertresolve_snomed_veterinary
date: 2024-06-10
tags: [en, licenced, resolver, snomed, veterinary, licensed]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps veterinary-related entities and concepts to SNOMED codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_veterinary_en_5.3.3_3.0_1718025467339.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_veterinary_en_5.3.3_3.0_1718025467339.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setWhiteList(['PROBLEM'])

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_veterinary", "en", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages = [document_assembler,
                                       sentenceDetectorDL,
                                       tokenizer,
                                       word_embeddings,
                                       ner,
                                       ner_converter,
                                       c2doc,
                                       sbert_embedder,
                                       snomed_resolver])
text = [["The veterinary team, is closely monitoring the patient for signs of lymphoblastic lymphoma, a malignant neoplasm of lymphoid origin. They are also treating the patient's osteoarthritis, a degenerative joint disease. Additionally, the team is vigilantly observing the facility for potential outbreaks of mink distemper."]]

data = spark.createDataFrame(text, StringType()).toDF("text")

result = resolver_pipeline.fit(spark.createDataFrame([[""]]).toDF("text")).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
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
    .setWhiteList("PROBLEM")

val c2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
    .setInputCols("ner_chunk_doc")
    .setOutputCol("sentence_embeddings")
    .setCaseSensitive(False)

val snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_veterinary", "en", "clinical/models")
    .setInputCols("sentence_embeddings") 
    .setOutputCol("snomed_code")
    .setDistanceFunction("EUCLIDEAN")

val resolver_pipeline = new PipelineModel().setStages(Array(document_assembler,
                                       sentenceDetectorDL,
                                       tokenizer,
                                       word_embeddings,
                                       ner,
                                       ner_converter,
                                       c2doc,
                                       sbert_embedder,
                                       snomed_resolver))

val data= Seq("The veterinary team, is closely monitoring the patient for signs of lymphoblastic lymphoma, a malignant neoplasm of lymphoid origin. They are also treating the patient's osteoarthritis, a degenerative joint disease. Additionally, the team is vigilantly observing the facility for potential outbreaks of mink distemper.").toDF("text")

val result = resolver_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---------------------------------------+-------+---------------+----------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                              ner_chunk| entity|    snomed_code|                                         description|                                                   all_codes|                                                 resolutions|
+---------------------------------------+-------+---------------+----------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                 lymphoblastic lymphoma|PROBLEM|312281000009102|                              lymphoblastic lymphoma|312281000009102:::188675007:::109979007:::1217301006:::11...|lymphoblastic lymphoma:::lymphoblastic lymphosarcoma:::b-...|
|a malignant neoplasm of lymphoid origin|PROBLEM|      443495005|               neoplasm of lymphoid system structure|443495005:::1156403002:::277604002:::127220001:::26947500...|neoplasm of lymphoid system structure:::composite lymphom...|
|           the patient's osteoarthritis|PROBLEM|      201826000|                              erosive osteoarthrosis|201826000:::43829003:::1162304008:::1679003:::201819000::...|erosive osteoarthrosis:::chronic osteoarthritis:::oligoar...|
|           a degenerative joint disease|PROBLEM|      201819000|degenerative joint disease involving multiple joints|201819000:::363056008:::399269003:::362975008:::1679003::...|degenerative joint disease involving multiple joints:::de...|
|                         mink distemper|PROBLEM|348361000009108|                                      mink distemper|348361000009108:::86031000009108:::207191000009103:::1901...|mink distemper:::dendropicos obsoletus:::xenops minutus o...|
+---------------------------------------+-------+---------------+----------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_veterinary|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|743.1 MB|
|Case sensitive:|false|

## References

This model is trained with the Veterinary Extension to SNOMED CT(R): April 1, 2024 Release version (available at the website https://vtsl.vetmed.vt.edu/extension/  ) and the augmented version of NIH September 2023 SNOMED CT United States (US) Edition
