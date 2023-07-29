---
layout: model
title: Detect Posology concepts (langtest)
author: John Snow Labs
name: ner_posology_langtest
date: 2023-07-28
tags: [licensed, clinical, en, posology, ner, langtest]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.0.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for posological entity detection in clinical notes. This NER model is an augmented version of [`ner_posology`](https://nlp.johnsnowlabs.com/2021/03/31/ner_posology_en.html) model and trained with the `embeddings_clinical` word embeddings model, so be sure to use the same embeddings in the pipeline.

## Predicted Entities

`DOSAGE`, `DRUG`, `DURATION`, `FORM`, `FREQUENCY`, `ROUTE`, `STRENGTH`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_POSOLOGY/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_POSOLOGY.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_posology_langtest_en_5.0.0_3.0_1690552227340.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_posology_langtest_en_5.0.0_3.0_1690552227340.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_posology_langtest", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

nlp_pipeline = Pipeline(
    stages=[
        document_assembler, 
        sentence_detector, 
        tokenizer, 
        word_embeddings, 
        clinical_ner, 
        ner_converter
    ])

text = """The patient is a 30-year-old female with a long history of insulin dependent diabetes, type 2; coronary artery disease; chronic renal insufficiency; peripheral vascular disease, also secondary to diabetes; who was originally admitted to an outside hospital for what appeared to be acute paraplegia, lower extremities. She did receive a course of Bactrim for 14 days for UTI. Evidently, at some point in time, the patient was noted to develop a pressure-type wound on the sole of her left foot and left great toe. She was also noted to have a large sacral wound; this is in a similar location with her previous laminectomy, and this continues to receive daily care. The patient was transferred secondary to inability to participate in full physical and occupational therapy and continue medical management of her diabetes, the sacral decubitus, left foot pressure wound, and associated complications of diabetes. She is given Fragmin 5000 units subcutaneously daily, Xenaderm to wounds topically b.i.d., Lantus 40 units subcutaneously at bedtime, OxyContin 30 mg p.o. q.12 h., folic acid 1 mg daily, levothyroxine 0.1 mg p.o. daily, Prevacid 30 mg daily, Avandia 4 mg daily, Norvasc 10 mg daily, Lexapro 20 mg daily, aspirin 81 mg daily, Senna 2 tablets p.o. q.a.m., Neurontin 400 mg p.o. t.i.d., Percocet 5/325 mg 2 tablets q.4 h. p.r.n., magnesium citrate 1 bottle p.o. p.r.n., sliding scale coverage insulin, Wellbutrin 100 mg p.o. daily, and Bactrim DS b.i.d."""

data = spark.createDataFrame([[text]]).toDF("text")

result = nlp_pipeline.nlp_pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")
    
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_large", "en", "clinical/models")\
    .setInputCols(Array("sentence", "token"))\
    .setOutputCol("embeddings")

val posology_ner_model = MedicalNerModel.pretrained('ner_posology_langtest' "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("posology_ner")

val posology_ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("posology_ner_chunk")

val posology_pipeline = new PipelineModel().setStages(Array(document_assembler, 
                                                   sentence_detector,
                                                   tokenizer,
                                                   word_embeddings,
                                                   posology_ner_model,
                                                   posology_ner_converter))

text = """The patient is a 30-year-old female with a long history of insulin dependent diabetes, type 2; coronary artery disease; chronic renal insufficiency; peripheral vascular disease, also secondary to diabetes; who was originally admitted to an outside hospital for what appeared to be acute paraplegia, lower extremities. She did receive a course of Bactrim for 14 days for UTI. Evidently, at some point in time, the patient was noted to develop a pressure-type wound on the sole of her left foot and left great toe. She was also noted to have a large sacral wound; this is in a similar location with her previous laminectomy, and this continues to receive daily care. The patient was transferred secondary to inability to participate in full physical and occupational therapy and continue medical management of her diabetes, the sacral decubitus, left foot pressure wound, and associated complications of diabetes. She is given Fragmin 5000 units subcutaneously daily, Xenaderm to wounds topically b.i.d., Lantus 40 units subcutaneously at bedtime, OxyContin 30 mg p.o. q.12 h., folic acid 1 mg daily, levothyroxine 0.1 mg p.o. daily, Prevacid 30 mg daily, Avandia 4 mg daily, Norvasc 10 mg daily, Lexapro 20 mg daily, aspirin 81 mg daily, Senna 2 tablets p.o. q.a.m., Neurontin 400 mg p.o. t.i.d., Percocet 5/325 mg 2 tablets q.4 h. p.r.n., magnesium citrate 1 bottle p.o. p.r.n., sliding scale coverage insulin, Wellbutrin 100 mg p.o. daily, and Bactrim DS b.i.d."""

val data = Seq(text).toDS.toDF("text")

val result = model.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------+---------+
|         chunk|ner_label|
+--------------+---------+
|       insulin|     DRUG|
|       Bactrim|     DRUG|
|   for 14 days| DURATION|
|       Fragmin|     DRUG|
|    5000 units|   DOSAGE|
|subcutaneously|    ROUTE|
|         daily|FREQUENCY|
|     topically|    ROUTE|
|         b.i.d|FREQUENCY|
|        Lantus|     DRUG|
|      40 units|   DOSAGE|
|subcutaneously|    ROUTE|
|    at bedtime|FREQUENCY|
|     OxyContin|     DRUG|
|         30 mg| STRENGTH|
|           p.o|    ROUTE|
|        q.12 h|FREQUENCY|
|    folic acid|     DRUG|
|          1 mg| STRENGTH|
|         daily|FREQUENCY|
+--------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_posology_langtest|
|Compatibility:|Healthcare NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|2.8 MB|

## References

trained by in-house dataset

## Benchmarking

```bash
    label      tp     fp     fn   total  precision  recall      f1
 DURATION   175.0   25.0   39.0   214.0      0.875  0.8178  0.8454
     DRUG  1373.0  153.0  167.0  1540.0     0.8997  0.8916  0.8956
   DOSAGE   153.0   52.0   71.0   224.0     0.7463   0.683  0.7133
    ROUTE   283.0   29.0   47.0   330.0     0.9071  0.8576  0.8816
FREQUENCY   744.0  109.0  108.0   852.0     0.8722  0.8732  0.8727
     FORM   556.0   83.0   76.0   632.0     0.8701  0.8797  0.8749
 STRENGTH   826.0  145.0  143.0   969.0     0.8507  0.8524  0.8515
    macro      -       -     -       -        -      -      0.8479
    micro      -       -     -       -        -      -      0.8680
```
