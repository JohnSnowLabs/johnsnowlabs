---
layout: model
title: Sentence Entity Resolver for Snomed Concepts, Findings version (sbiobert_base_cased_mli embeddings)
author: John Snow Labs
name: sbiobertresolve_snomed_findings
date: 2024-01-24
tags: [en, licensed, entity_resolution, clinical, snomed, findings]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.2
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The model maps extracted medical entities to their corresponding Snomed codes (Clinical Findings) using `sbiobert_base_cased_mli` BERT sentence embeddings.

## Predicted Entities

`Snomed Codes and their normalized definitions`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_findings_en_5.2.1_3.2_1706098966876.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_findings_en_5.2.1_3.2_1706098966876.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

`sbiobertresolve_snomed_findings` resolver model must be used with `sbiobert_base_cased_mli` as embeddings and NER models that can extract clinical findings.

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = Tokenizer()\
  .setInputCols(["sentence"])\
  .setOutputCol("token")\

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
  .setInputCols(["sentence", "token"])\
  .setOutputCol("embeddings")

ner_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models") \
  .setInputCols(["sentence", "token", "embeddings"]) \
  .setOutputCol("ner_jsl")

ner_jsl_converter = NerConverterInternal() \
  .setInputCols(["sentence", "token", "ner_jsl"]) \
  .setOutputCol("ner_jsl_chunk")\
  .setWhiteList(["Kidney_Disease", "Cerebrovascular_Disease", "Heart_Disease",
                 "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                 "EKG_Findings", "Communicable_Disease"])\

chunk2doc = Chunk2Doc()\
  .setInputCols("ner_jsl_chunk")\
  .setOutputCol("ner_chunk_doc")

sbert_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
  .setInputCols(["ner_chunk_doc"])\
  .setOutputCol("sbert_embeddings")\
  .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_findings", "en", "clinical/models") \
  .setInputCols(["sbert_embeddings"]) \
  .setOutputCol("snomed_code")\

snomed_pipeline = Pipeline(stages = [
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_jsl,
    ner_jsl_converter,
    chunk2doc,
    sbert_embeddings,
    snomed_resolver
])

text = """The patient exhibited recurrent upper respiratory tract infections, subjective fevers, unintentional weight loss, and occasional night sweats. Clinically, they appeared cachectic and pale, with notable hepatosplenomegaly. Laboratory results confirmed pancytopenia."""

result = snomed_pipeline.fullAnnotate(text)
```
```scala
val documentAssembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained()
      .setInputCols(Array("document"))
      .setOutputCol("sentence")

val tokenizer = new Tokenizer()
      .setInputCols(Array("sentence"))
      .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en", "clinical/models")
      .setInputCols(Array("sentence", "token"))
      .setOutputCol("embeddings")

val ner_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
      .setInputCols(Array("sentence", "token", "embeddings"))
      .setOutputCol("ner_jsl")

val ner_jsl_converter = new NerConverterInternal()
      .setInputCols(Array("sentence", "token", "clinical_ner"))
      .setOutputCol("ner_jsl_chunk")
      .setWhiteList(Array("Kidney_Disease", "Cerebrovascular_Disease", "Heart_Disease",
                 "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                 "EKG_Findings", "Communicable_Disease"))

val chunk2doc = new Chunk2Doc()
      .setInputCols("ner_jsl_chunk")
      .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
      .setInputCols("ner_chunk_doc")
      .setOutputCol("sbert_embeddings")

val snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_findings", "en", "clinical/models")
     .setInputCols(Array("sbert_embeddings"))
     .setOutputCol("snomed_code")

val new nlpPipeine().setStages(Array(documentAssembler,
                                    sentenceDetector,
                                    tokenizer,
                                    word_embeddings,
                                    ner_jsl_clinical,
                                    ner_jsl_converter,
                                    chunk2doc,
                                    sbert_embedder,
                                    snomed_resolver))

val text= """The patient exhibited recurrent upper respiratory tract infections, subjective fevers, unintentional weight loss, and occasional night sweats. Clinically, they appeared cachectic and pale, with notable hepatosplenomegaly. Laboratory results confirmed pancytopenia."""

val df = Seq(text).toDF(text)

val result= nlpPipeline.fit(df).transform(df)
```
</div>

## Results

```bash
+--------------------------------------------+-----+---+---------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|                                      chunks|begin|end|     code|                                         all_codes|                                       resolutions|                                     all_distances|
+--------------------------------------------+-----+---+---------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|recurrent upper respiratory tract infections|   22| 65|195708003|[195708003, 308130008, 195746005, 54150009, 783...|[recurrent upper respiratory tract infection, r...|[0.0073, 0.0664, 0.0664, 0.0694, 0.0712, 0.0737...|
|                           subjective fevers|   68| 84|103001002|[103001002, 248425001, 186694006, 77957000, 271...|[feeling feverish (finding), feels feverish, sw...|[0.0494, 0.0514, 0.0535, 0.0552, 0.0661, 0.0674...|
|                   unintentional weight loss|   87|111|448765001|[448765001, 422868009, 699205002, 416528001, 16...|[unintentional weight loss, unexplained weight ...|[0.0000, 0.0400, 0.0472, 0.0564, 0.0666, 0.0666...|
|                     occasional night sweats|  118|140|161859009|[161859009, 42984000, 139115006, 423052008, 672...|[night sweats, night sweats, night sweats, freq...|[0.0480, 0.0480, 0.0480, 0.1043, 0.1100, 0.1256...|
|                                   cachectic|  169|177|238108007|[238108007, 28928000, 74633007, 422003001, 2845...|[cachectic, cachexia, aids with cachexia, cache...|[0.0000, 0.0619, 0.0651, 0.0965, 0.0961, 0.0986...|
|                                        pale|  183|186|274643008|[274643008, 139121005, 161865009, 398979000, 16...|[pale, pale color, pale color, pale complexion,...|[0.0000, 0.0733, 0.0733, 0.0812, 0.0812, 0.0892...|
|                  notable hepatosplenomegaly|  194|219| 36760000|[36760000, 19058002, 80378000, 16294009, 469330...|[hepatosplenomegaly, congestive splenomegaly, n...|[0.0225, 0.0835, 0.0857, 0.0875, 0.0928, 0.0959...|
|                                pancytopenia|  251|262|127034005|[127034005, 736024007, 191249008, 5876000, 1249...|[pancytopenia, drug induced pancytopenia, pancy...|[0.0000, 0.0407, 0.0425, 0.0425, 0.0493, 0.0495...|
+--------------------------------------------+-----+---+---------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_findings|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|715.9 MB|
|Case sensitive:|false|

## References

This model is trained with the augmented version of NIH September 2023 SNOMED CT United States (US) Edition.
