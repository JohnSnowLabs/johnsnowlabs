---
layout: model
title: Clinical Deidentification Pipeline (Document Wise)
author: John Snow Labs
name: ner_deid_docwise_benchmark_optimized_zeroshot_partial
date: 2025-06-17
tags: [deidentification, deid, en, licensed, pipeline, docwise, zeroshot]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text.
The pipeline can mask and obfuscate `LOCATION`, `CONTACT`, `PROFESSION`, `NAME`, `DATE`, `AGE`, `MEDICALRECORD`, `ORGANIZATION`, `HEALTHPLAN`, `DOCTOR`, `USERNAME`,
`LOCATION-OTHER`, `URL`, `DEVICE`, `CITY`, `ZIP`, `STATE`, `PATIENT`, `STREET`, `PHONE`, `HOSPITAL`, `EMAIL`, `IDNUM`, `BIOID`, `FAX`, `LOCATION_OTHER`, `DLN`,
`SSN`, `ACCOUNT`, `PLATE`, `VIN`, `LICENSE`, `IP` entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_docwise_benchmark_optimized_zeroshot_partial_en_6.0.2_3.4_1750197733762.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_docwise_benchmark_optimized_zeroshot_partial_en_6.0.2_3.4_1750197733762.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_deid_pipeline = PretrainedPipeline("ner_deid_docwise_benchmark_optimized", "en", "clinical/models")

zeroshot_partial_pipeline = PretrainedPipeline(("ner_deid_docwise_benchmark_optimized_zeroshot_partial", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

samples_df = spark.createDataFrame([[text]]).toDF("text")

ner_result = ner_deid_pipeline.transform(samples_df).cache()
final_result = zeroshot_partial_pipeline.transform(ner_result)

final_result.selectExpr("text", "masked.result").show()


final_result.selectExpr("explode(final_ner_chunk) as ner_chunk")\
            .selectExpr("ner_chunk.result as chunk", 
                        "ner_chunk.begin as begin",
                        "ner_chunk.end as end",
                        "ner_chunk.metadata.entity as entity",
                        ).show()

```

{:.jsl-block}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_deid_pipeline = nlp.PretrainedPipeline("ner_deid_docwise_benchmark_optimized", "en", "clinical/models")

zeroshot_partial_pipeline = nlp.PretrainedPipeline(("ner_deid_docwise_benchmark_optimized_zeroshot_partial", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

samples_df = spark.createDataFrame([[text]]).toDF("text")

ner_result = ner_deid_pipeline.transform(samples_df).cache()
final_result = zeroshot_partial_pipeline.transform(ner_result)

final_result.selectExpr("text", "masked.result").show()


final_result.selectExpr("explode(final_ner_chunk) as ner_chunk")\
            .selectExpr("ner_chunk.result as chunk", 
                        "ner_chunk.begin as begin",
                        "ner_chunk.end as end",
                        "ner_chunk.metadata.entity as entity",
                        ).show()

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_deid_pipeline = PretrainedPipeline("ner_deid_docwise_benchmark_optimized", "en", "clinical/models")

val zeroshot_partial_pipeline = PretrainedPipeline(("ner_deid_docwise_benchmark_optimized_zeroshot_partial", "en", "clinical/models")

val text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

val samples_df = Seq(text).toDF("text")

val ner_result = ner_deid_pipeline.transform(samples_df)
val final_result = zeroshot_partial_pipeline.transform(ner_result)

```
</div>

## Results

```bash

|    | chunk                |   begin |   end | entity   | ner_source     |
|---:|:---------------------|--------:|------:|:---------|:---------------|
|  0 | John Lee             |       4 |    11 | DOCTOR   | zeroshot_chunk |
|  1 | Royal Medical Clinic |      19 |    38 | HOSPITAL | zeroshot_chunk |
|  2 | Chicago              |      43 |    49 | CITY     | zeroshot_chunk |
|  3 | 11/05/2024           |      79 |    88 | DATE     | zeroshot_chunk |
|  4 | 56467890             |     130 |   137 | IDNUM    | zeroshot_chunk |
|  5 | Emma Wilson          |     153 |   163 | PATIENT  | zeroshot_chunk |
|  6 | 50 years old         |     169 |   180 | AGE      | entity_age     |
|  7 | 444-456-7890         |     203 |   214 | PHONE    | entity_phone   |

|index|text|result|
|---|---|---|
|0|Dr\. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024\.
The patient’s medical record number is 56467890\.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 \.|Dr\. \<DOCTOR\>, from \<HOSPITAL\> in \<CITY\>, attended to the patient on \<DATE\>\.
The patient’s medical record number is \<IDNUM\>\.
The patient, \<PATIENT\>, is \<AGE\>, her Contact number: \<PHONE\> \.|

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_docwise_benchmark_optimized_zeroshot_partial|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|712.9 MB|

## Included Models

- PretrainedZeroShotNER
- NerConverterInternalModel
- ChunkMergeModel
- ChunkMergeModel
- LightDeIdentification