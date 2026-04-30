---
layout: model
title: ZeroShot Multitask Base
author: John Snow Labs
name: zeroshot_multitask_base
date: 2026-04-10
tags: [en, licensed, clinical, medical, ner, classification, relation_extraction, assertion, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.3.0
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_multitask_base_en_6.3.0_3.0_1775814855432.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_multitask_base_en_6.3.0_3.0_1775814855432.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setEntities(["problem", "treatment", "test", "body_part", "drug_dosage", "severity", "date"])\
    .setStructures([
        ("problem_info", [
            "text::str::medical condition, symptom, or diagnosis",
            "assertion::[present|absent|hypothetical|possible|conditional|associated_with_someone_else]",
        ]),
        ("treatment_info", [
            "text::str::drug, medication, procedure, or therapy",
            "assertion::[present|absent|hypothetical|possible|conditional|associated_with_someone_else]",
        ]),
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

text = f"""
Jennifer Smith is 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, and associated with an acute hepatitis, presented with a one-week history of polyuria, poor appetite, and vomiting.
"""

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
    .setEntities(["problem", "treatment", "test", "body_part", "drug_dosage", "severity", "date"])\
    .setStructures([
        ("problem_info", [
            "text::str::medical condition, symptom, or diagnosis",
            "assertion::[present|absent|hypothetical|possible|conditional|associated_with_someone_else]",
        ]),
        ("treatment_info", [
            "text::str::drug, medication, procedure, or therapy",
            "assertion::[present|absent|hypothetical|possible|conditional|associated_with_someone_else]",
        ]),
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

text = f"""
Jennifer Smith is 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, and associated with an acute hepatitis, presented with a one-week history of polyuria, poor appetite, and vomiting.
"""

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
    .setEntities(Array("problem", "treatment", "test", "body_part", "drug_dosage", "severity", "date"))
    .setStructures(Array(
        ("problem_info", Array(
            "text::str::medical condition, symptom, or diagnosis",
            "assertion::[present|absent|hypothetical|possible|conditional|associated_with_someone_else]"
        )),
        ("treatment_info", Array(
            "text::str::drug, medication, procedure, or therapy",
            "assertion::[present|absent|hypothetical|possible|conditional|associated_with_someone_else]"
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

val  text = f"""
Jennifer Smith is 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, and associated with an acute hepatitis, presented with a one-week history of polyuria, poor appetite, and vomiting.
"""

val data = Seq(text).toDF("text")

val results = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                         extractions|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[{chunk, 62, 64, $99, {sentence -> 0, entity -> drug_dosage, confidence -> 0.54619294}, []}, {category, 0, 91, other, {sentence -> 0, confidence -> 0.4580742, task -> cancer_typ...|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_multitask_base|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|844.4 MB|