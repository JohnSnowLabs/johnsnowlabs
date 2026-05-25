---
layout: model
title: ZeroShot Multitask Generic
author: John Snow Labs
name: zeroshot_multitask_base
date: 2026-05-25
tags: [en, licensed, clinical, medical, ner, classification, relation_extraction, assertion, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.0
supported: true
engine: onnx
annotator: PretrainedZeroShotMultiTask
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This ZeroShot model is trained to extract and link entities in a document. Users needs to define entitit labels or an input schema as explained in the example section.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_multitask_base_en_6.4.0_3.0_1779745323440.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_multitask_base_en_6.4.0_3.0_1779745323440.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

zero_shot = PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_base", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("extractions")\
    .setEntityThreshold(0.4)\
    .setEntities(["medical_condition", "treatment", "test", "body_part", "drug_dosage", "severity", "date"])\
    .setStructures([
        ("medication_info", [
            "drug::str::Medication name",
            "dosage::str::Dosage of the medication",
        ])
    ])\
    .setClassifications([
        ("cancer_type",  ["lung", "breast", "colorectal", "other", "not_cancer"]),
        ("urgency",      ["routine", "urgent", "emergent"]),
    ])\
    .setRelations([
        "treatment_improves_problem",
        "treatment_causes_problem",
        "treatment_administered_for_problem",
        "test_reveals_problem",
        "test_conducted_for_problem",
    ])

pipeline = Pipeline(
    stages = [
        document_assembler,
        zero_shot
])

text = f"""The patient was diagnosed with stage III breast cancer. She started tamoxifen 20 mg daily. Her sister also had breast cancer. CT chest showed no metastasis."""

data = spark.createDataFrame([[text]]).toDF("text")

results = pipeline.fit(data).transform(data)

results.select("completions").show(truncate=False)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

zero_shot = medical.PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_base", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("extractions")\
    .setEntityThreshold(0.4)\
    .setEntities(["medical_condition", "treatment", "test", "body_part", "drug_dosage", "severity", "date"])\
    .setStructures([
        ("medication_info", [
            "drug::str::Medication name",
            "dosage::str::Dosage of the medication",
        ])
    ])\
    .setClassifications([
        ("cancer_type",  ["lung", "breast", "colorectal", "other", "not_cancer"]),
        ("urgency",      ["routine", "urgent", "emergent"]),
    ])\
    .setRelations([
        "treatment_improves_problem",
        "treatment_causes_problem",
        "treatment_administered_for_problem",
        "test_reveals_problem",
        "test_conducted_for_problem",
    ])

pipeline = nlp.Pipeline(
    stages = [
        document_assembler,
        zero_shot
])

text = f"""The patient was diagnosed with stage III breast cancer. She started tamoxifen 20 mg daily. Her sister also had breast cancer. CT chest showed no metastasis."""

data = spark.createDataFrame([[text]]).toDF("text")

results = pipeline.fit(data).transform(data)

results.select("completions").show(truncate=False)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val zero_shot = PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_base", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("extractions")
    .setEntityThreshold(0.4)
    .setEntities(Array("medical_condition", "treatment", "test", "body_part", "drug_dosage", "severity", "date"))
    .setStructures(Array(
        ("medication_info", Array(
            "drug::str::Medication name",
            "dosage::str::Dosage of the medication"
        ))
    ))
    .setClassifications(Array(
        ("cancer_type",  Array("lung", "breast", "colorectal", "other", "not_cancer")),
        ("urgency",      Array("routine", "urgent", "emergent"))
    ))
    .setRelations(Array(
        "treatment_improves_problem",
        "treatment_causes_problem",
        "treatment_administered_for_problem",
        "test_reveals_problem",
        "test_conducted_for_problem"
    ))

val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    zero_shot
))

val  text = f"""The patient was diagnosed with stage III breast cancer. She started tamoxifen 20 mg daily. Her sister also had breast cancer. CT chest showed no metastasis."""

val data = Seq(text).toDF("text")

val results = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                         extractions|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[{chunk, 31, 39, stage III, {sentence -> 0, entity -> severity, confidence -> 0.9939043, ner_source -> extractions}, []}, {chunk, 68, 76, tamoxifen, {sentence -> 0, entity -> tr...|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_multitask_base|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|844.5 MB|