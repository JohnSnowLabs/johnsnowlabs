---
layout: model
title: Few-Shot Assertion Model ( i2b2 )
author: John Snow Labs
name: fewhot_assertion_i2b2_e5_base_v2_i2b2
date: 2024-07-13
tags: [en, licensed, clinical, e5, medical, assertion, i2b2, fewshot]
task: Assertion Status
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.0
supported: true
annotator: FewShotAssertionClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Assign assertion status to clinical entities extracted by NER based on their context in the text.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/fewhot_assertion_i2b2_e5_base_v2_i2b2_en_5.3.3_3.0_1720879694320.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/fewhot_assertion_i2b2_e5_base_v2_i2b2_en_5.3.3_3.0_1720879694320.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
    .setInputCols("document")\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")
    #.setWhiteList(["PROBLEM"])

few_shot_assertion_converter = FewShotAssertionSentenceConverter()\
    .setInputCols(["sentence", "ner_chunk"])\
    .setOutputCol("assertion_sentence")

e5_embeddings = E5Embeddings\
    .pretrained("e5_base_v2_embeddings_medical_assertion_i2b2", "en", "clinical/models")\
    .setInputCols(["assertion_sentence"])\
    .setOutputCol("assertion_embedding")

few_shot_assertion_classifier = FewShotAssertionClassifierModel()\
    .pretrained("fewhot_assertion_i2b2_e5_base_v2_i2b2", "en", "clinical/models")\
    .setInputCols(["assertion_embedding"])\
    .setOutputCol("assertion")


pipeline = Pipeline(
    stages = [
        document_assembler,
        sentence_detector,
        tokenizer,
        embeddings,
        ner,
        ner_converter,
        few_shot_assertion_converter,
        e5_embeddings,
        few_shot_assertion_classifier
])

data = spark.createDataFrame([["""The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."""]]).toDF("text")

result = pipeline.fit(data).transform(data)

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

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")
    .setCaseSensitive(False)

val ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    //.setWhiteList("PROBLEM")

val few_shot_assertion_converter = new FewShotAssertionSentenceConverter()
    .setInputCols(Array("sentence", "ner_chunk"))
    .setOutputCol("assertion_sentence")

val e5_embeddings = E5Embeddings
    .pretrained("e5_base_v2_embeddings_medical_assertion_i2b2", "en", "clinical/models")
    .setInputCols("assertion_sentence")
    .setOutputCol("assertion_embedding")

val few_shot_assertion_classifier = FewShotAssertionClassifierModel()
    .pretrained("fewhot_assertion_i2b2_e5_base_v2_i2b2", "en", "clinical/models")
    .setInputCols("assertion_embedding")
    .setOutputCol("assertion")


val pipeline = new Pipeline().setStages(Array(
        document_assembler,
        sentence_detector,
        tokenizer,
        embeddings,
        ner,
        ner_converter,
        few_shot_assertion_converter,
        e5_embeddings,
        few_shot_assertion_classifier
))

val data = Seq(Array("""The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature.""")).toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| chunks                                |   begin |   end | entities   | assertion                    |   confidence |
|:--------------------------------------|--------:|------:|:-----------|:-----------------------------|-------------:|
| congestion                            |      63 |    72 | PROBLEM    | present                      |     0.952448 |
| suctioning yellow discharge           |      89 |   115 | TREATMENT  | associated_with_someone_else |     0.379236 |
| some mild problems with his breathing |     164 |   200 | PROBLEM    | present                      |     0.950967 |
| any perioral cyanosis                 |     234 |   254 | PROBLEM    | absent                       |     0.955528 |
| retractions                           |     259 |   269 | PROBLEM    | absent                       |     0.955448 |
| a tactile temperature                 |     303 |   323 | PROBLEM    | present                      |     0.954495 |
| Tylenol                               |     346 |   352 | TREATMENT  | present                      |     0.953851 |
| his respiratory congestion            |     489 |   514 | PROBLEM    | present                      |     0.952367 |
| more tired                            |     546 |   555 | PROBLEM    | present                      |     0.95374  |
| albuterol treatments                  |     638 |   657 | TREATMENT  | present                      |     0.954199 |
| His urine output                      |     676 |   691 | TEST       | present                      |     0.952049 |
| 4 wet diapers                         |     794 |   806 | TREATMENT  | present                      |     0.953411 |
| any diarrhea                          |     833 |   844 | PROBLEM    | absent                       |     0.954902 |
| yellow colored                        |     871 |   884 | PROBLEM    | present                      |     0.9547   |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|fewhot_assertion_i2b2_e5_base_v2_i2b2|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[assertion_embedding]|
|Output Labels:|[assertion]|
|Language:|en|
|Size:|25.4 KB|