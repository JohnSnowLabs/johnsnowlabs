---
layout: model
title: Sentence Entity Resolver for SNOMED codes (procedures and measurements)
author: John Snow Labs
name: sbiobertresolve_snomed_procedures_measurements
date: 2024-02-08
tags: [licensed, en, resolver, procedure, snomed, measurements]
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

This model maps Procedure and Measurements (Tests) to their corresponding SNOMED codes using sbiobert_base_cased_mli Sentence Bert Embeddings

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_procedures_measurements_en_5.2.1_3.0_1707392348441.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_procedures_measurements_en_5.2.1_3.0_1707392348441.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverter()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(['Procedure','Test'])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings\
    .pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

snomed_pcs_resolver = SentenceEntityResolverModel\
    .pretrained("sbiobertresolve_snomed_procedures_measurements", "en", "clinical/models")\
    .setInputCols(["ner_chunk", "sbert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

nlpPipeline = Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    chunk2doc,
    sbert_embedder,
    snomed_pcs_resolver])


text = [["""Based on the severity of her abdominal examination and the persistence of her symptoms, it has been determined that she requires a laparoscopic jejunectomy, possible appendectomy, and cholecystectomy.Laboratory values indicate a white blood cell count of 15.3, plasma hemoglobin level of 12.8, and normal platelet count. Alkaline phosphatase is elevated at 184, while liver function tests are otherwise normal. Electrolyte levels are within the normal range. Glucose levels are at 134, BUN is 4, and creatinine is 0.7."""]]


data= spark.createDataFrame(text).toDF('text')
model = nlpPipeline.fit(data)
result = model.transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Procedure","Test"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(False)

val snomed_pcs_resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_snomed_procedures_measurements", "en", "clinical/models")
    .setInputCols(Array("ner_chunk", "sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val nlpPipeline = new Pipeline().setStages=(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    chunk2doc,
    sbert_embedder,
    snomed_pcs_resolver))

val data = Seq("Based on the severity of her abdominal examination and the persistence of her symptoms, it has been determined that she requires a laparoscopic jejunectomy, possible appendectomy, and cholecystectomy.Laboratory values indicate a white blood cell count of 15.3, plasma hemoglobin level of 12.8, and normal platelet count. Alkaline phosphatase is elevated at 184, while liver function tests are otherwise normal. Electrolyte levels are within the normal range. Glucose levels are at 134, BUN is 4, and creatinine is 0.7.") .toDF("text")

val result = nlpPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------------+---------+-----------+--------------------------------+--------------------------------------------------+--------------------------------------------------+
|                   chunk|    label|snomed_code|                      resolution|                                         all_codes|                                   all_resolutions|
+------------------------+---------+-----------+--------------------------------+--------------------------------------------------+--------------------------------------------------+
|laparoscopic jejunectomy|Procedure| 1220546008|laparoscopic excision of jejunum|1220546008:::6025007:::307195003:::1220549001::...|laparoscopic excision of jejunum:::laparoscopic...|
|            appendectomy|Procedure|   80146002|                    appendectomy|80146002:::17041004:::82730006:::174045003:::60...|appendectomy:::appendicotomy:::secondary append...|
|         cholecystectomy|Procedure|   38102005|                 cholecystectomy|38102005:::6402000:::44337006:::45595009:::3413...|cholecystectomy:::choledochectomy:::cholecystot...|
|  white blood cell count|     Test|     767002|          white blood cell count|767002:::252305002:::165511009:::44190001:::391...|white blood cell count:::white blood cell test:...|
| plasma hemoglobin level|     Test|  104142005|         plasma hemoglobin level|104142005:::271510004:::313995005:::271026005::...|plasma hemoglobin level:::hemoglobin s level:::...|
|          platelet count|     Test|   61928009|                  platelet count|61928009:::250314004:::8574009:::75672003:::803...|platelet count:::plateletcrit:::platelet estima...|
|    Alkaline phosphatase|     Test|   88810008|alkaline phosphatase measurement|88810008:::271234008:::390962007:::59518007:::2...|alkaline phosphatase measurement:::serum alkali...|
|    liver function tests|     Test|   26958001|            liver function tests|26958001:::269856004:::736164009:::287858000:::...|liver function tests:::liver enzyme levels:::mo...|
|      Electrolyte levels|     Test|   79301008|        electrolytes measurement|79301008:::276025008:::312474003:::401142008:::...|electrolytes measurement:::electrolyte regulati...|
|          Glucose levels|     Test|   36048009|             glucose measurement|36048009:::72191006:::302789003:::166888009:::3...|glucose measurement:::plasma glucose:::capillar...|
|                     BUN|     Test|   24509005|                 bun measurement|24509005:::16227009:::85651007:::174651007:::14...|bun measurement:::cinching:::bost operation:::e...|
|              creatinine|     Test|  113075003|                serum creatinine|113075003:::70901006:::313936008:::250745003:::...|serum creatinine:::creatinine measurement:::pla...|
+------------------------+---------+-----------+--------------------------------+--------------------------------------------------+--------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_procedures_measurements|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|322.6 MB|
|Case sensitive:|false|