---
layout: model
title: Sentence Entity Resolver for SNOMED (sbiobertresolve_snomed_bodyStructure)
author: John Snow Labs
name: sbiobertresolve_snomed_bodyStructure
date: 2024-02-05
tags: [licensed, en, resolver, snomed, bodystructure]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted medical (anatomical structure) entities to SNOMED codes (body structure version) using `sbiobert_base_cased_mli` BERT sentence embeddings

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_bodyStructure_en_5.2.1_3.0_1707138980854.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_bodyStructure_en_5.2.1_3.0_1707138980854.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



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
    .setWhiteList(["External_body_part_or_region"])\
    .setReplaceLabels({"External_body_part_or_region": "BodyPart"})

ner_anatomy = MedicalNerModel.pretrained("ner_anatomy_coarse", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner_anatomy")

ner_anatomy_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner_anatomy"]) \
    .setOutputCol("ner_anatomy_chunk")\
    .setReplaceLabels({"Anatomy": "BodyPart"})

ner_oncology_anatomy = MedicalNerModel.pretrained("ner_oncology_anatomy_general", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner_oncology_anatomy")

ner_oncology_anatomy_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner_oncology_anatomy"]) \
    .setOutputCol("ner_oncology_anatomy_chunk")\
    .setReplaceLabels({"Anatomical_Site": "BodyPart"})

chunk_merger = ChunkMergeApproach() \
    .setInputCols("ner_jsl_chunk", "ner_anatomy_chunk", "ner_oncology_anatomy_chunk") \
    .setOutputCol("ner_chunk") \

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_bodyStructure", "en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("snomed_code")\

snomed_pipeline = Pipeline(stages = [
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_jsl,
    ner_jsl_converter,
    ner_anatomy,
    ner_anatomy_converter,
    ner_oncology_anatomy,
    ner_oncology_anatomy_converter,
    chunk_merger,
    chunk2doc,
    sbert_embeddings,
    snomed_resolver
])


data = spark.createDataFrame([["""The patient is a 30-year-old female with a long history of insulin-dependent diabetes, type 2; coronary artery disease; chronic renal insufficiency; peripheral vascular disease, also secondary to diabetes; who was originally admitted to an outside hospital for what appeared to be acute paraplegia, lower extremities. She did receive a course of Bactrim for 14 days for UTI."""]]).toDF("text")

model = snomed_pipeline.fit(data)
result = model.transform(data)
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

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings")

val ner_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner")

val ner_jsl_converter = new NerConverter()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_jsl_chunk")
    .setWhiteList(Array("External_body_part_or_region"))
    .setReplaceLabels({"Anatomical_Site": "BodyPart"})

val ner_anatomy = MedicalNerModel.pretrained("ner_anatomy_coarse", "en", "clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner_anatomy")

val ner_anatomy_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_anatomy"))
    .setOutputCol("ner_anatomy_chunk")
    .setReplaceLabels(Map{"Anatomy" -> "BodyPart"})

val ner_oncology_anatomy = MedicalNerModel.pretrained("ner_oncology_anatomy_general", "en", "clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner_oncology_anatomy")

val ner_oncology_anatomy_converter = new NerConverter()
    .setInputCols(Array("sentence","token","ner_oncology_anatomy"))
    .setOutputCol("ner_oncology_anatomy_chunk")
    .setWhiteList(Array("Anatomical_Site"))
    .setReplaceLabels(Map{"Anatomical_Site" -> "BodyPart"})

val chunk_merger = ChunkMergeApproach() \
    .setInputCols("ner_jsl_chunk", "ner_anatomy_chunk", "ner_oncology_anatomy_chunk")
    .setOutputCol("ner_chunk")

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(False)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_snomed_bodyStructure", "en", "clinical/models")
    .setInputCols(Array("ner_chunk", "sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val nlpPipeline = new Pipeline().setStages=(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_jsl,
    ner_jsl_converter,
    ner_anatomy,
    ner_anatomy_converter,
    ner_oncology_anatomy,
    ner_oncology_anatomy_converter,
    chunk_merger,
    chunk2doc,
    sbert_embeddings,
    snomed_resolver
    ))

val data = Seq("Medical professionals rushed in the bustling emergency room to attend to the patient with alarming symptoms.The attending physician immediately noted signs of respiratory distress, including stridor, a high-pitched sound indicative of upper respiratory tract obstruction.The patient, struggling to breathe, exhibited dyspnea, their chest heaving with each labored breath. Concern heightened when they began experiencing syncope, a sudden loss of consciousness likely stemming from inadequate oxygenation. Further examination revealed a respiratory tract hemorrhage.") .toDF("text")

val model = snomed_pipeline.fit(data)
    
val result = model.transform(data)
```
</div>

## Results

```bash
+-------------------+--------+-----------+--------------------------+--------------------------------------------------+--------------------------------------------------+
|              chunk|   label|snomed_code|                resolution|                                         all_codes|                                   all_resolutions|
+-------------------+--------+-----------+--------------------------+--------------------------------------------------+--------------------------------------------------+
|    coronary artery|BodyPart|   41801008|           coronary artery|41801008:::119204004:::360487004:::55537005:::1...|coronary artery:::coronary artery part:::segmen...|
|              renal|BodyPart|   64033007|           renal structure|64033007:::84924000:::303402001:::58471003:::28...|renal structure:::renal segment:::renal vessels...|
|peripheral vascular|BodyPart|   51833009|peripheral vascular system|51833009:::840581000:::3058005:::300054001:::28...|peripheral vascular system:::peripheral artery:...|
|  lower extremities|BodyPart|   61685007|           lower extremity|61685007:::127951001:::120575009:::119260005:::...|lower extremity:::lower extremity region:::lowe...|
+-------------------+--------+-----------+--------------------------+--------------------------------------------------+--------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_bodyStructure|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|189.8 MB|
|Case sensitive:|false|