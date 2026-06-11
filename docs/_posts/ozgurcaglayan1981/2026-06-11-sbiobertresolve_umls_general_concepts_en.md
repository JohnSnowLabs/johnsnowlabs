---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes (General Concepts)
author: John Snow Labs
name: sbiobertresolve_umls_general_concepts
date: 2026-06-11
tags: [en, entity_resolution, licensed, clinical, umls, general_concepts]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities to 4 general categories of UMLS CUI codes using `sbiobert_base_cased_mli_onnx` Sentence BERT Embeddings. It is trained on the 2026AA release of the Unified Medical Language System (UMLS) dataset. The training data covers "Disease or Syndrome" (T047), "Sign or Symptom" (T184), "Medical Device" (T074), and "Therapeutic or Preventive Procedure" (T061) semantic types, comprising approximately 1,170,000 name-CUI pairs.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_general_concepts_en_6.4.0_3.4_1781217567122.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_general_concepts_en_6.4.0_3.4_1781217567122.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_jsl")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner_jsl"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Injury_or_Poisoning","Hyperlipidemia","Kidney_Disease","Oncological","Cerebrovascular_Disease","Oxygen_Therapy","Heart_Disease","Obesity","Disease_Syndrome_Disorder","Symptom","Treatment","Diabetes","Procedure","Drug_Ingredient","VS_Finding","Communicable_Disease","Drug_BrandName","Hypertension","Imaging_Technique"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_general_concepts","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([["A 28-year-old female with a history of gestational diabetes mellitus diagnosed with a HTG-induced pancreatitis associated with acute hepatitis and obesity. She complains of a 2-week history of polyuria and vomiting."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_jsl")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner_jsl"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Injury_or_Poisoning","Hyperlipidemia","Kidney_Disease","Oncological","Cerebrovascular_Disease","Oxygen_Therapy","Heart_Disease","Obesity","Disease_Syndrome_Disorder","Symptom","Treatment","Diabetes","Procedure","Drug_Ingredient","VS_Finding","Communicable_Disease","Drug_BrandName","Hypertension","Imaging_Technique"])

chunk2doc = medical.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_general_concepts","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([["A 28-year-old female with a history of gestational diabetes mellitus diagnosed with a HTG-induced pancreatitis associated with acute hepatitis and obesity. She complains of a 2-week history of polyuria and vomiting."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel
    .pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner_jsl")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_jsl"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Injury_or_Poisoning", "Hyperlipidemia", "Kidney_Disease", "Oncological", "Cerebrovascular_Disease", "Oxygen_Therapy", "Heart_Disease", "Obesity", "Disease_Syndrome_Disorder", "Symptom", "Treatment", "Diabetes", "Procedure", "Drug_Ingredient", "VS_Finding", "Communicable_Disease", "Drug_BrandName", "Hypertension", "Imaging_Technique"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_umls_general_concepts", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
))

val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed with a HTG-induced pancreatitis associated with acute hepatitis and obesity. She complains of a 2-week history of polyuria and vomiting.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                     | entity                    | umls_code   | resolution                    | all_k_results                                                                       | all_k_distances                                                                     | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:------------------------------|:--------------------------|:------------|:------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| gestational diabetes mellitus | Diabetes                  | C0085207    | gestational diabetes mellitus | C0085207:::C0032969:::C2063017:::C1283034:::C0271663:::C3646651:::C0271662:::C38... | 0.0060:::4.1536:::4.7727:::4.8705:::4.8875:::5.1049:::5.1562:::5.3716:::5.4228::... | 0.0000:::0.0253:::0.0332:::0.0347:::0.0354:::0.0381:::0.0394:::0.0423:::0.0435::... | gestational diabetes mellitus:::pregnancy diabetes mellitus:::pregnancy complica... |
| HTG-induced pancreatitis      | Disease_Syndrome_Disorder | C0376670    | alcohol-induced pancreatitis  | C0376670:::C4302243:::C5208246:::C2350449:::C0030305:::C0267940:::C5197785:::C59... | 5.0375:::5.0869:::5.1019:::5.2261:::5.4597:::5.7266:::5.7849:::5.8438:::5.8674::... | 0.0405:::0.0415:::0.0414:::0.0442:::0.0478:::0.0522:::0.0537:::0.0543:::0.0551::... | alcohol-induced pancreatitis:::igg4-related pancreatitis:::immune-mediated pancr... |
| hepatitis                     | Disease_Syndrome_Disorder | C0019158    | hepatitis                     | C0019158:::C0019159:::C0814152:::C0042721:::C0011226:::C0854495:::C0854496:::C00... | 0.0067:::3.2405:::3.3068:::3.8887:::3.9117:::4.0492:::4.4444:::4.7608:::5.1820::... | 0.0000:::0.0168:::0.0176:::0.0242:::0.0246:::0.0263:::0.0318:::0.0367:::0.0436::... | hepatitis:::hepatitis a:::hepatitis g:::viral hepatitis:::hepatitis d:::hepatiti... |
| obesity                       | Obesity                   | C0028754    | obesity                       | C0028754:::C0342940:::C0342942:::C0857116:::C1561826:::C0694533:::C0028756:::C42... | 0.0063:::3.8691:::4.2499:::4.3088:::4.4608:::4.6134:::4.7044:::4.8436:::5.0790::... | 0.0000:::0.0218:::0.0268:::0.0272:::0.0290:::0.0316:::0.0327:::0.0344:::0.0378::... | obesity:::abdominal obesity:::generalized obesity:::obesity gross:::overweight a... |
| polyuria                      | Symptom                   | C0032617    | polyuria                      | C0032617:::C0848232:::C0011848:::C0016708:::C2830339:::C0018965:::C0271593:::C01... | 0.0083:::6.9422:::7.4260:::7.8673:::8.1199:::8.4068:::8.4652:::8.5287:::8.6550::... | 0.0000:::0.0751:::0.0870:::0.0970:::0.1063:::0.1103:::0.1137:::0.1126:::0.1175::... | polyuria:::nocturnal polyuria:::vasopressin-related polyuria:::frequency of urin... |
| vomiting                      | Symptom                   | C0042963    | vomiting                      | C0042963:::C0401157:::C0152165:::C0152164:::C0859028:::C0455040:::C4324485:::C07... | 0.0060:::3.6356:::5.4757:::5.7043:::5.8947:::6.1394:::6.1742:::6.2869:::6.2971::... | 0.0000:::0.0196:::0.0446:::0.0484:::0.0527:::0.0568:::0.0578:::0.0585:::0.0594::... | vomiting:::intermittent vomiting:::persistent vomiting:::periodic vomiting:::vom... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_general_concepts|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|3.4 GB|
|Case sensitive:|false|