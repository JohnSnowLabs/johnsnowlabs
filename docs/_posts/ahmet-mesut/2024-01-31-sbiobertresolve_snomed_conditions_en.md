---
layout: model
title: Sentence Entity Resolver for SNOMED (sbiobertresolve_snomed_conditions)
author: John Snow Labs
name: sbiobertresolve_snomed_conditions
date: 2024-01-31
tags: [licensed, en, resolver, snomed, conditions]
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

This model maps clinical conditions to their corresponding SNOMED (domain: Conditions) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_conditions_en_5.2.1_3.0_1706721516745.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_conditions_en_5.2.1_3.0_1706721516745.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")\

ner_jsl_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Kidney_Disease", "Cerebrovascular_Disease", "Heart_Disease","Disease_Syndrome_Disorder",
                  "ImagingFindings", "Symptom", "VS_Finding","EKG_Findings", "Communicable_Disease","Pregnancy",
                  "Obesity","Hypertension","Overweight","Hyperlipidemia","Triglycerides","Diabetes","Oncological",
                  "Psychological_Condition","ImagingFindings","Injury_or_Poisoning"])\

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel\
    .pretrained("sbiobertresolve_snomed_conditions", "en", "clinical/models")\
    .setInputCols(["ner_chunk", "sbert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(
    stages = [
    document_assembler,
    sentenceDetectorDL,
    tokenizer,
    word_embeddings,
    ner_jsl,
    ner_jsl_converter,
    c2doc,
    sbert_embedder,
    resolver
    ])


text = [["""Medical professionals rushed in the bustling emergency room to attend to the patient with alarming symptoms.
            The attending physician immediately noted signs of respiratory distress, including stridor, a high-pitched sound indicative of upper respiratory tract obstruction.
            The patient, struggling to breathe, exhibited dyspnea, their chest heaving with each labored breath. Concern heightened when they began experiencing syncope,
            a sudden loss of consciousness likely stemming from inadequate oxygenation. Further examination revealed a respiratory tract hemorrhage."""]]


data= spark.createDataFrame(text).toDF('text')
model = resolver_pipeline.fit(data)
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

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Kidney_Disease", "Cerebrovascular_Disease", "Heart_Disease","Disease_Syndrome_Disorder",
                  "ImagingFindings", "Symptom", "VS_Finding","EKG_Findings", "Communicable_Disease","Pregnancy",
                  "Obesity","Hypertension","Overweight","Hyperlipidemia","Triglycerides","Diabetes","Oncological",
                  "Psychological_Condition","ImagingFindings","Injury_or_Poisoning"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(False)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_snomed_conditions", "en", "clinical/models")
    .setInputCols(Array("ner_chunk", "sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val nlpPipeline = new Pipeline().setStages=(Array(
    document_assembler,
    sentenceDetectorDL,
    tokenizer,
    word_embeddings,
    ner_jsl,
    ner_jsl_converter,
    chunk2doc,
    sbert_embedder,
    resolver))

val data = Seq("Medical professionals rushed in the bustling emergency room to attend to the patient with alarming symptoms.The attending physician immediately noted signs of respiratory distress, including stridor, a high-pitched sound indicative of upper respiratory tract obstruction.The patient, struggling to breathe, exhibited dyspnea, their chest heaving with each labored breath. Concern heightened when they began experiencing syncope, a sudden loss of consciousness likely stemming from inadequate oxygenation. Further examination revealed a respiratory tract hemorrhage.") .toDF("text")

data= spark.createDataFrame(text).toDF('text')

val result = nlpPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------------------+-------------------------+-----------+-----------------------------------+--------------------------------------------------+--------------------------------------------------+
|                              chunk|                    label|snomed_code|                         resolution|                                         all_codes|                                   all_resolutions|
+-----------------------------------+-------------------------+-----------+-----------------------------------+--------------------------------------------------+--------------------------------------------------+
|               respiratory distress|               VS_Finding|  271825005|               respiratory distress|271825005:::140109004:::418092006:::75483001:::...|respiratory distress:::o/e - respiratory distre...|
|                            stridor|                  Symptom|   70407001|                            stridor|70407001:::301826004:::301287002:::58596002:::3...|stridor:::intermittent stridor:::expiratory str...|
|                 high-pitched sound|                  Symptom|   51406002|                 high pitched voice|51406002:::271661003:::405495005:::23292001:::3...|high pitched voice:::heart sounds exaggerated::...|
|upper respiratory tract obstruction|Disease_Syndrome_Disorder|   68372009|upper respiratory tract obstruction|68372009:::79688008:::73342002:::301252002:::20...|upper respiratory tract obstruction:::respirato...|
|              struggling to breathe|                  Symptom|  289105003|   difficulty controlling breathing|289105003:::230145002:::289116005:::386813002::...|difficulty controlling breathing:::difficulty b...|
|                            dyspnea|                  Symptom|  267036007|                            dyspnea|267036007:::60845006:::25209001:::34560001:::16...|dyspnea:::exertional dyspnea:::inspiratory dysp...|
|                      chest heaving|                  Symptom|  248562002|         paradoxical chest movement|248562002:::78011002:::33847006:::274712006:::7...|paradoxical chest movement:::flail chest:::crus...|
|                     labored breath|                  Symptom|  248549001|                  labored breathing|248549001:::56505000:::386813002:::90480005:::5...|labored breathing:::breathiness:::breathing abn...|
|                            syncope|                  Symptom|  271594007|                            syncope|271594007:::234167006:::90129003:::445535007:::...|syncope:::situational syncope:::tussive syncope...|
|              loss of consciousness|                  Symptom|  127379000|              loss of consciousness|127379000:::44077006:::44564008:::443371007:::1...|loss of consciousness:::loss of sensation:::los...|
|             inadequate oxygenation|                  Symptom|  238161004|           impaired oxygen delivery|238161004:::70944005:::238162006:::123826004:::...|impaired oxygen delivery:::impaired gas exchang...|
|       respiratory tract hemorrhage|Disease_Syndrome_Disorder|   95431003|       respiratory tract hemorrhage|95431003:::233783005:::15238002:::78144005:::32...|respiratory tract hemorrhage:::tracheal hemorrh...|
+-----------------------------------+-------------------------+-----------+-----------------------------------+--------------------------------------------------+--------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_conditions|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|671.6 MB|
|Case sensitive:|false|