---
layout: model
title: Detect Problems, Tests, and Treatments (Spanish)
author: John Snow Labs
name: ner_clinical
date: 2023-08-30
tags: [licensed, clinical, ner, es]
task: Named Entity Recognition
language: es
edition: Healthcare NLP 5.0.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms in Spanish. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state-of-the-art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/){:.button.button-orange}
[Open in Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CLINICAL_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_es_5.0.1_3.0_1693370988290.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_es_5.0.1_3.0_1693370988290.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","es") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "es", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol('ner_chunk')

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
    ])



sample_text = """El KCNJ9 humano (Kir 3.3, GIRK3) es un miembro de la familia de canales de potasio rectificadores internos activados por proteínas G (GIRK). Aquí describimos la organización genómica del locus KCNJ9 en el cromosoma 1q21-23 como un gen candidato para la diabetes mellitus tipo II en la población india Pima. El gen abarca aproximadamente 7,6 kb y contiene un exón no codificante y dos exones codificantes separados por intrones de aproximadamente 2,2 y aproximadamente 2,6 kb, respectivamente. Identificamos 14 polimorfismos de un solo nucleótido (SNP), incluido uno que predice una sustitución Val366Ala, y una inserción/deleción de 8 pares de bases (bp). Nuestros estudios de expresión revelaron la presencia del transcrito en varios tejidos humanos, incluidos el páncreas y dos tejidos importantes sensibles a la insulina: grasa y músculo esquelético. La caracterización del gen KCNJ9 debería facilitar más estudios sobre la función de la proteína KCNJ9 y permitir la evaluación del posible papel del locus en la diabetes tipo II. CONTEXTO: En la actualidad, uno de los aspectos más importantes para el tratamiento del cáncer de mama es desarrollar la terapia estándar para pacientes tratados previamente con antraciclinas y taxanos."""


data = spark.createDataFrame([[sample_text]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","es")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_clinical", "es", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
))

sample_data = Seq("""El KCNJ9 humano (Kir 3.3, GIRK3) es un miembro de la familia de canales de potasio rectificadores internos activados por proteínas G (GIRK). Aquí describimos la organización genómica del locus KCNJ9 en el cromosoma 1q21-23 como un gen candidato para la diabetes mellitus tipo II en la población india Pima. El gen abarca aproximadamente 7,6 kb y contiene un exón no codificante y dos exones codificantes separados por intrones de aproximadamente 2,2 y aproximadamente 2,6 kb, respectivamente. Identificamos 14 polimorfismos de un solo nucleótido (SNP), incluido uno que predice una sustitución Val366Ala, y una inserción/deleción de 8 pares de bases (bp). Nuestros estudios de expresión revelaron la presencia del transcrito en varios tejidos humanos, incluidos el páncreas y dos tejidos importantes sensibles a la insulina: grasa y músculo esquelético. La caracterización del gen KCNJ9 debería facilitar más estudios sobre la función de la proteína KCNJ9 y permitir la evaluación del posible papel del locus en la diabetes tipo II. CONTEXTO: En la actualidad, uno de los aspectos más importantes para el tratamiento del cáncer de mama es desarrollar la terapia estándar para pacientes tratados previamente con antraciclinas y taxanos.""").toDS.toDF("text")


val result = pipeline.fit(sample_data).transform(sample_data)
```
</div>

## Results

```bash
+-----------------------------------------------+-----+----+---------+
|chunk                                          |begin|end |ner_label|
+-----------------------------------------------+-----+----+---------+
|potasio rectificadores                         |75   |96  |TREATMENT|
|proteínas G                                    |121  |131 |TREATMENT|
|organización genómica del locus                |161  |191 |TEST     |
|un gen candidato                               |228  |243 |PROBLEM  |
|diabetes mellitus tipo II en la población india|253  |299 |PROBLEM  |
|intrones                                       |418  |425 |TEST     |
|SNP                                            |547  |549 |PROBLEM  |
|estudios de expresión                          |665  |685 |TEST     |
|grasa                                          |825  |829 |PROBLEM  |
|músculo esquelético                            |833  |851 |PROBLEM  |
|caracterización del gen                        |857  |879 |TEST     |
|proteína                                       |941  |948 |TEST     |
|evaluación                                     |970  |979 |TEST     |
|diabetes tipo II                               |1015 |1030|PROBLEM  |
|cáncer de mama                                 |1121 |1134|PROBLEM  |
|terapia                                        |1154 |1160|TREATMENT|
|antraciclinas                                  |1211 |1223|TREATMENT|
|taxanos                                        |1227 |1233|TREATMENT|
+-----------------------------------------------+-----+----+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical|
|Compatibility:|Healthcare NLP 5.0.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|es|
|Size:|2.9 MB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
     PROBLEM       0.80      0.84      0.82      1036
   TREATMENT       0.83      0.74      0.78       473
        TEST       0.93      0.76      0.84       544
   micro-avg       0.83      0.80      0.81      2053
   macro-avg       0.85      0.78      0.81      2053
weighted-avg       0.84      0.80      0.81      2053
```
