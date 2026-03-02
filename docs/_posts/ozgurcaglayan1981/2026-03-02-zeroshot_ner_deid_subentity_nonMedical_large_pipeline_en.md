---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_deid_subentity_nonMedical_large) - Pipeline
author: John Snow Labs
name: zeroshot_ner_deid_subentity_nonMedical_large_pipeline
date: 2026-03-02
tags: [en, ner, deid, licensed, clinical, zeroshot, subentity, pipeline]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.3.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline implements Zero-shot Named Entity Recognition (NER) using a pre-trained language model with contextual understanding. It enables entity extraction across different domains without task-specific fine-tuning.

Unlike fully flexible zero-shot setups, this pipeline operates with a fixed label schema to ensure consistent and standardized outputs. The supported entity labels are:

"ACCOUNTNUM", "AGE", "CITY", "COUNTRY", "DATE", "DEVICE", "DLN", "DOCTOR", "EMAIL", "GENDER", "HOSPITAL", "IDNUM", "IP", "LOCATION_OTHER", "MEDICALRECORD", "NAME", "ORGANIZATION", "PATIENT", "PHONE", "PLATE", "PROFESSION", "SSN", "STATE", "STREET", "TIME", "URL", "USERNAME", "VIN", "ZIP"

All predictions are restricted to this predefined set of labels. This design ensures production stability, output consistency, and reliable performance within the defined entity scope.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_subentity_nonMedical_large_pipeline_en_6.3.0_3.4_1772490618581.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_subentity_nonMedical_large_pipeline_en_6.3.0_3.4_1772490618581.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("zeroshot_ner_deid_subentity_nonMedical_large_pipeline", "en", "clinical/models")

sample_text = """ 
On February 14, 2024, patient Sarah Mitchell, a 42-year-old female (SSN: 456-78-9012, MRN: MRN-2024-78945), was admitted to St.Mary's Regional Hospital at 1500 Healthcare Boulevard, Boston, MA 02108.

Dr. Robert Chen, MD (License: DL-12345678), examined the patient in the Cardiology Department. Contact: phone +1-617-555-2468, E-mail: sarah.mitchell@techmail.com. She resides at 789 Maple Avenue, Apt 3C, Cambridge, MA 02139.

Emergency contact: James Mitchell (+1-617-555-2469). Insurance: Policy HLTH-987654321, BlueCross BlueShield. Discharged February 15, 2024. Follow-up: March 1, 2024, at 11:00 AM.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("zeroshot_ner_deid_subentity_nonMedical_large_pipeline", "en", "clinical/models")

sample_text = """ 
On February 14, 2024, patient Sarah Mitchell, a 42-year-old female (SSN: 456-78-9012, MRN: MRN-2024-78945), was admitted to St.Mary's Regional Hospital at 1500 Healthcare Boulevard, Boston, MA 02108.

Dr. Robert Chen, MD (License: DL-12345678), examined the patient in the Cardiology Department. Contact: phone +1-617-555-2468, E-mail: sarah.mitchell@techmail.com. She resides at 789 Maple Avenue, Apt 3C, Cambridge, MA 02139.

Emergency contact: James Mitchell (+1-617-555-2469). Insurance: Policy HLTH-987654321, BlueCross BlueShield. Discharged February 15, 2024. Follow-up: March 1, 2024, at 11:00 AM.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("zeroshot_ner_deid_subentity_nonMedical_large_pipeline", "en", "clinical/models")

val sample_text = """ 
On February 14, 2024, patient Sarah Mitchell, a 42-year-old female (SSN: 456-78-9012, MRN: MRN-2024-78945), was admitted to St.Mary's Regional Hospital at 1500 Healthcare Boulevard, Boston, MA 02108.

Dr. Robert Chen, MD (License: DL-12345678), examined the patient in the Cardiology Department. Contact: phone +1-617-555-2468, E-mail: sarah.mitchell@techmail.com. She resides at 789 Maple Avenue, Apt 3C, Cambridge, MA 02139.

Emergency contact: James Mitchell (+1-617-555-2469). Insurance: Policy HLTH-987654321, BlueCross BlueShield. Discharged February 15, 2024. Follow-up: March 1, 2024, at 11:00 AM.
"""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk                                                             | begin | end | ner_label      | confidence |
| :---------------------------------------------------------------- | ----: | --: | :------------- | ---------: |
| February 14, 2024                                                 |     4 |  20 | DATE           |  0.9978829 |
| Sarah Mitchell                                                    |    31 |  44 | PATIENT        |  0.9996172 |
| 42-year-old                                                       |    49 |  59 | AGE            |  0.9977164 |
| female                                                            |    61 |  66 | GENDER         |  0.9453571 |
| 456-78-9012                                                       |    74 |  84 | SSN            | 0.99576294 |
| MRN-2024-78945                                                    |    92 | 105 | MEDICALRECORD  |  0.9977089 |
| 1500 Healthcare Boulevard                                         |   156 | 180 | STREET         | 0.99362284 |
| Boston                                                            |   183 | 188 | CITY           |  0.9986701 |
| MA                                                                |   191 | 192 | STATE          |   0.999084 |
| 02108                                                             |   194 | 198 | ZIP            | 0.99330926 |
| Robert Chen                                                       |   206 | 216 | DOCTOR         |  0.9995503 |
| DL-12345678                                                       |   232 | 242 | DLN            |  0.9995552 |
| Cardiology                                                        |   274 | 283 | HOSPITAL       | 0.76555896 |
| +1-617-555-2468                                                   |   312 | 326 | PHONE          | 0.99838436 |
| sarah.mitchell@techmail.com                                       |   337 | 363 | EMAIL          |  0.5817241 |
| She                                                               |   366 | 368 | NAME           |  0.7062193 |
| 789 Maple Avenue                                                  |   381 | 396 | STREET         | 0.99547416 |
| Apt 3C                                                            |   399 | 404 | LOCATION_OTHER |  0.9998995 |
| Cambridge                                                         |   407 | 415 | CITY           |  0.9983443 |
| MA                                                                |   418 | 419 | STATE          |   0.999726 |
| 02139                                                             |   421 | 425 | ZIP            |  0.9982576 |
| James Mitchell                                                    |   448 | 461 | NAME           | 0.89618254 |
| +1-617-555-2469                                                   |   464 | 478 | PHONE          | 0.99610525 |
| HLTH-987654321                                                    |   500 | 513 | IDNUM          |  0.9831487 |
| BlueCross BlueShield                                              |   516 | 535 | ORGANIZATION   | 0.95677435 |
| February 15, 2024                                                 |   549 | 565 | DATE           |   0.992326 |
| March 1, 2024                                                     |   579 | 591 | DATE           | 0.94422466 |
| 11:00 AM                                                          |   597 | 604 | TIME           |  0.9995034 |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_deid_subentity_nonMedical_large_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- PretrainedZeroShotNER
- NerConverterInternalModel