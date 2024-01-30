---
layout: model
title: Sentence Entity Resolver for SNOMED codes (procedures and measurements)
author: John Snow Labs
name: sbiobertresolve_snomed_procedures_measurements
date: 2024-01-30
tags: [en, licensed, procedure, resolver, snomed, measurements]
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

This model maps Procedure and Measurements entities to their corresponding SNOMED codes using sbiobert_base_cased_mli Sentence Bert Embeddings

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_procedures_measurements_en_5.2.1_3.0_1706636035503.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_procedures_measurements_en_5.2.1_3.0_1706636035503.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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


text = [["""Based on the severity of her abdominal examination and the persistence of her symptoms,
            it has been determined that she requires a laparoscopic jejunectomy, possible appendectomy, and
            cholecystectomy.Laboratory values indicate a white blood cell count of 15.3,
            hemoglobin level of 12.8, and normal platelet count. Alkaline phosphatase is elevated at 184,
            while liver function tests are otherwise normal. Electrolyte levels are within the normal range.
            Glucose levels are at 134, BUN is 4, and creatinine is 0.7."""]]


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

val data = Seq("Based on the severity of her abdominal examination and the persistence of her symptoms, it has been determined that she requires a laparoscopic jejunectomy, possible appendectomy, and cholecystectomy.Laboratory values indicate a white blood cell count of 15.3, hemoglobin level of 12.8, and normal platelet count. Alkaline phosphatase is elevated at 184, while liver function tests are otherwise normal. Electrolyte levels are within the normal range. Glucose levels are at 134, BUN is 4, and creatinine is 0.7.") .toDF("text")
data= spark.createDataFrame(text).toDF('text')

val result = nlpPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------------+---------+-----------+--------------------------------------------------+--------------------------------------------------+
|                   chunk|    label|snomed_code|                                         all_codes|                                       resolutions|
+------------------------+---------+-----------+--------------------------------------------------+--------------------------------------------------+
|laparoscopic jejunectomy|Procedure| 1220546008|1220546008:::6025007:::307195003:::1220549001::...|laparoscopic excision of jejunum:::laparoscopic...|
|            appendectomy|Procedure|   80146002|80146002:::17041004:::149412002:::82730006:::17...|appendectomy:::appendicotomy:::appendicectomy::...|
|         cholecystectomy|Procedure|   38102005|38102005:::6402000:::44337006:::45595009:::3413...|cholecystectomy:::choledochectomy:::cholecystot...|
|  white blood cell count|     Test|     767002|767002:::252305002:::142922003:::44190001:::391...|white blood cell count:::white blood cell test:...|
|        hemoglobin level|     Test|  313995005|313995005:::104142005:::407705000:::143073002::...|hemoglobin a level:::plasma hemoglobin level:::...|
|          platelet count|     Test|   61928009|61928009:::250314004:::8574009:::75672003:::803...|platelet count:::plateletcrit:::platelet estima...|
|    Alkaline phosphatase|     Test|   88810008|88810008:::45745006:::143948004:::166625007:::2...|alkaline phosphatase measurement:::alkaline pho...|
|    liver function tests|     Test|  143927001|143927001:::26958001:::166601004:::269992001:::...|liver function tests:::liver function test:::li...|
|      Electrolyte levels|     Test|   79301008|79301008:::276025008:::144342002:::401142008:::...|electrolytes measurement:::electrolyte regulati...|
|          Glucose levels|     Test|  144323001|144323001:::167094009:::144184004:::36048009:::...|serum glucose level:::plasma glucose level:::bl...|
|                     BUN|     Test|  105011006|105011006:::16227009:::85651007:::1431002:::467...|bun measurement:::cinching:::bost operation:::p...|
|              creatinine|     Test|   70901006|70901006:::166729007:::166713004:::144658009:::...|creatinine measurement:::plasma creatinine leve...|
+------------------------+---------+-----------+--------------------------------------------------+--------------------------------------------------+
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
|Size:|329.2 MB|
|Case sensitive:|false|

## References

Trained on SNOMED code dataset with sbiobert_base_cased_mli sentence embeddings.
