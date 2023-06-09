---
layout: model
title: Demographic Entities in Medical Files
author: John Snow Labs
name: ner_demographic_extended
date: 2023-05-02
tags: [en, licensed, tensorflow]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.2.4
spark_version: 3.2
supported: true
engine: tensorflow
annotator: NerDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts patient's demographic characteristics, such as race, ethnicity, gender, age, socioeconomic status, or geographic location, influence the quality of care they receive and unhealthy habits. It has been trained based on internal John Snow Labs Dataset.

## Predicted Entities

`Gender`, `Age`, `Race_ethnicity`, `Employment_status`, `Job_title`, `Marital_Status`, `Political_affiliation`, `Union_membership`, `Sexual_orientation`, `Religion`, `Height`, `Weight`, `Obesity`, `Unhealthy_habits`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_demographic_extended_en_4.2.4_3.2_1683038343266.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_demographic_extended_en_4.2.4_3.2_1683038343266.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = WordEmbeddingsModel.pretrained('glove_100d') \ 
   .setInputCols(['document', 'token']) \ 
   .setOutputCol('embeddings')

ner_model = MedicalNerModel.pretrained("ner_demographic_extended", "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
    ])

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_demographic_extended|
|Type:|ner|
|Compatibility:|Healthcare NLP 4.2.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|2.8 MB|
|Dependencies:|glove_100d|

## References

Trained on data gathered and manually annotated by John Snow Labs.

## Benchmarking

```bash
| label                   | tp    | fp          | fn   | total       | precision | recall     | f1       |
|-------------------------|-------|-------------|------|-------------|-----------|------------|----------|
| B-Age                   | 168   | 6.0         | 9    | 177         | 0.965517  | 0.949153   | 0.957265 |
| I-Age                   | 112   | 6.0         | 3    | 115         | 0.949153  | 0.973913   | 0.961373 |
| B-Employment_status     | 114   | 4.0         | 19   | 133         | 0.966102  | 0.857143   | 0.908367 |
| I-Employment_status     | 8     | 0.0         | 10   | 18          | 1         | 0.444444   | 0.615385 |
| B-Gender                | 162   | 9.0         | 31   | 193         | 0.947368  | 0.839378   | 0.890110 |
| I-Gender                | 0     | 0.0         | 2    | 2           | 0.000000  | 0.000000   | 0.000000 |
| B-Height                | 63    | 5.0         | 2    | 65          | 0.926471  | 0.969231   | 0.947368 |
| I-Height                | 89    | 11.0        | 0    | 89          | 0.890000  | 1          | 0.941799 |
| B-Job_title             | 73    | 21.0        | 18   | 91          | 0.776596  | 0.802198   | 0.789189 |
| I-Job_title             | 30    | 13.0        | 10   | 40          | 0.697674  | 0.750000   | 0.722892 |
| B-Marital_Status        | 115   | 3.0         | 8    | 123         | 0.974576  | 0.934959   | 0.954357 |
| B-Obesity               | 63    | 7.0         | 6    | 69          | 0.900000  | 0.913043   | 0.906475 |
| I-Obesity               | 4     | 2.0         | 3    | 7           | 0.666667  | 0.571429   | 0.615385 |
| B-Political_affiliation | 46    | 0.0         | 0    | 46          | 1         | 1          | 1        |
| I-Political_affiliation | 2     | 0.0         | 0    | 2           | 1         | 1          | 1        |
| B-Race_ethnicity        | 153   | 7.0         | 7    | 160         | 0.956250  | 0.956250   | 0.956250 |
| I-Race_ethnicity        | 26    | 3.0         | 4    | 30          | 0.896552  | 0.866667   | 0.881356 |
| B-Religion              | 88    | 5.0         | 3    | 91          | 0.946237  | 0.967033   | 0.956522 |
| I-Religion              | 3     | 3.0         | 1    | 4           | 0.500000  | 0.750000   | 0.600000 |
| B-Sexual_orientation    | 79    | 0.0         | 0    | 79          | 1         | 1          | 1        |
| B-Unhealthy_habits      | 373   | 94.0        | 74   | 447         | 0.798715  | 0.834452   | 0.816193 |
| I-Unhealthy_habits      | 198   | 38.0        | 44   | 242         | 0.838983  | 0.818182   | 0.828452 |
| B-Union_membership      | 12    | 2.0         | 4    | 16          | 0.857143  | 0.750000   | 0.800000 |
| I-Union_membership      | 44    | 2.0         | 1    | 45          | 0.956522  | 0.977778   | 0.967033 |
| B-Weight                | 69    | 1.0         | 0    | 69          | 0.985714  | 1          | 0.992806 |
| I-Weight                | 69    | 1.0         | 0    | 69          | 0.985714  | 1          | 0.992806 |
| tp:2163                 | fp:   | 243.0       | fn:  | 259         | labels:   | 26         |          |
| Macro-average           | prec: | 0.86084436, | rec: | 0.84327893, | f1:       | 0.85197112 |          |
| Micro-average           | prec: | 0.89900249, | rec: | 0.89306358, | f1:       | 0.89602319 |          |
```