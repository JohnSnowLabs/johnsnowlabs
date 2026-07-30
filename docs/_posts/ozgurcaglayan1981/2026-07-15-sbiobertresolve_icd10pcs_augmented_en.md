---
layout: model
title: Sentence Entity Resolver for ICD-10-PCS (Augmented)
author: John Snow Labs
name: sbiobertresolve_icd10pcs_augmented
date: 2026-07-15
tags: [entity_resolution, icd10pcs, clinical, en, licensed]
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

This model maps extracted medical entities to ICD10-PCS codes using `sbiobert_base_cased_mli_onnx` Sentence Bert Embeddings. It is trained on the augmented version of the dataset which is used in the previous ICD-10-PCS resolver model. Trained on the ICD-10-PCS 20260401 (FY2026, effective April 1, 2026) code set.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10pcs_augmented_en_6.4.0_3.4_1784124403150.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10pcs_augmented_en_6.4.0_3.4_1784124403150.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setOutputCol("word_embeddings")

ner_model = MedicalNerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(['Procedure', 'Test', 'Test_Result', 'Treatment', 'Pulse', 'Imaging_Technique', 'Labour_Delivery', 'Blood_Pressure', 'Oxygen_Therapy', 'Weight', 'LDL', 'O2_Saturation', 'BMI', 'Vaccine', 'Respiration', 'Temperature', 'Birth_Entity', 'Triglycerides'])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10pcs_augmented","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("icd10pcs_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
])

data = spark.createDataFrame([["As part of the rehabilitation and behavioral health plan, the patient received acupuncture for chronic pain management and participated in group psychotherapy sessions. A pain assessment was performed, followed by a course of therapeutic massage and biofeedback for stress reduction. The patient also underwent voice treatment for a speech disorder, and traction of the neck was applied for cervical strain."]]).toDF("text")
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
    .setOutputCol("word_embeddings")

ner_model = medical.NerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(['Procedure', 'Test', 'Test_Result', 'Treatment', 'Pulse', 'Imaging_Technique', 'Labour_Delivery', 'Blood_Pressure', 'Oxygen_Therapy', 'Weight', 'LDL', 'O2_Saturation', 'BMI', 'Vaccine', 'Respiration', 'Temperature', 'Birth_Entity', 'Triglycerides'])

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10pcs_augmented","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("icd10pcs_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
])

data = spark.createDataFrame([["As part of the rehabilitation and behavioral health plan, the patient received acupuncture for chronic pain management and participated in group psychotherapy sessions. A pain assessment was performed, followed by a course of therapeutic massage and biofeedback for stress reduction. The patient also underwent voice treatment for a speech disorder, and traction of the neck was applied for cervical strain."]]).toDF("text")
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
    .setOutputCol("word_embeddings")

val ner_model = MedicalNerModel
    .pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Procedure", "Test", "Test_Result", "Treatment", "Pulse", "Imaging_Technique", "Labour_Delivery", "Blood_Pressure", "Oxygen_Therapy", "Weight", "LDL", "O2_Saturation", "BMI", "Vaccine", "Respiration", "Temperature", "Birth_Entity", "Triglycerides"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli_onnx", "en","clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_icd10pcs_augmented", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("icd10pcs_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
))

val data = Seq("As part of the rehabilitation and behavioral health plan, the patient received acupuncture for chronic pain management and participated in group psychotherapy sessions. A pain assessment was performed, followed by a course of therapeutic massage and biofeedback for stress reduction. The patient also underwent voice treatment for a speech disorder, and traction of the neck was applied for cervical strain.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk              | entity    | icd10pcs_code   | resolution                                | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:-----------------------|:----------|:----------------|:------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| acupuncture            | Treatment | 8E0H30Z         | acupuncture [acupuncture]                 | 8E0H30Z:::8E0KX1Z:::8E0H300:::GZFZZZZ:::F14Z5ZZ:::F0CZ0ZZ:::8E0ZXY5:::F08Z6ZZ:::... | 0.0000:::0.1753:::0.2091:::0.2162:::0.2217:::0.2296:::0.2374:::0.2551:::0.2585::... | acupuncture [acupuncture]:::therapeutic massage [therapeutic massage]:::acupunct... |
| psychotherapy sessions | Treatment | GZHZZZZ         | group psychotherapy [group psychotherapy] | GZHZZZZ:::F08Z6ZZ:::GZ54ZZZ:::GZ53ZZZ:::GZ55ZZZ:::GZ59ZZZ:::GZ72ZZZ:::GZ58ZZZ:::... | 0.0679:::0.1189:::0.1437:::0.1446:::0.1475:::0.1545:::0.1520:::0.1649:::0.1686::... | group psychotherapy [group psychotherapy]:::psychosocial skills treatment [psych... |
| therapeutic massage    | Treatment | 8E0KX1Z         | therapeutic massage [therapeutic massage] | 8E0KX1Z:::8E0H30Z:::8E0ZXY5:::GZFZZZZ:::8E0VX1D:::8E0ZXY4:::GZJZZZZ:::F09Z3ZZ:::... | 0.0000:::0.1753:::0.1925:::0.2251:::0.2536:::0.2501:::0.2485:::0.2762:::0.2754::... | therapeutic massage [therapeutic massage]:::acupuncture [acupuncture]:::meditati... |
| stress reduction       | Procedure | GZJZZZZ         | light therapy [light therapy]             | GZJZZZZ:::F00ZRZZ:::GZFZZZZ:::8E0ZXY5:::2W5MX7Z:::2W5LX7Z:::F08Z6ZZ:::6A4Z1ZZ:::... | 0.2214:::0.2330:::0.2430:::0.2468:::0.2746:::0.2798:::0.2685:::0.2743:::0.2766::... | light therapy [light therapy]:::brief tone stimuli assessment [brief tone stimul... |
| voice treatment        | Procedure | F06ZCZZ         | voice treatment [voice treatment]         | F06ZCZZ:::F00ZFZZ:::F06ZCSZ:::F06Z7SZ:::F00ZMZZ:::F06ZCKZ:::F06ZCTZ:::F0CZ1SZ:::... | 0.0000:::0.0883:::0.0947:::0.1217:::0.1298:::0.1294:::0.1309:::0.1338:::0.1325::... | voice treatment [voice treatment]:::voice assessment [voice assessment]:::voice ... |
| traction of the neck   | Procedure | 2W62XZZ         | traction of neck [traction of neck]       | 2W62XZZ:::2W60XZZ:::2W62X0Z:::2W61XZZ:::2W02X7Z:::2W02X2Z:::2W12X7Z:::F01D6ZZ:::... | 0.0047:::0.0827:::0.0841:::0.1078:::0.1164:::0.1229:::0.1240:::0.1378:::0.1405::... | traction of neck [traction of neck]:::traction of head [traction of head]:::trac... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd10pcs_augmented|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sbert_embeddings]|
|Output Labels:|[icd10pcs_code]|
|Language:|en|
|Size:|628.1 MB|
|Case sensitive:|false|