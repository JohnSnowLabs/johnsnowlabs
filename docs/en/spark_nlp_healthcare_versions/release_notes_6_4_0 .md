---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP v6.4.0 Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_6_4_0
key: docs-licensed-release-notes
modify_date: 2026-04-17
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 6.4.0

#### Highlights

We are delighted to announce notable enhancements and updates in Healthcare NLP 6.4.0. The headline addition is **Pretrained Zero Shot Multi Task** module, a unified annotator that enables **Named Entity Recognition**, **Text Classification**, **Relation Extraction**, and **Structured Extraction** in a **single forward pass**—eliminating the need for task-specific fine-tuning or labeled datasets while providing flexible, setter-based configuration.
This release also introduces an optional **Medical NER model** training setting to split multi-sentence rows before training and reduce peak memory usage on long documents; and enables configurable de-identification output wrapping via **markers** (prefix/suffix markers around target PHI entities).
In parallel, the release delivers **78 new pretrained models and pipelines**, further strengthening coverage across clinical entity recognition, structured extraction, and domain-specific use cases.  Notably, this includes **JSL_MedS NER (LLM — q16 — v5)**, a Medical LLM–based named entity recognition model for structured clinical trial eligibility parsing, and returning them in a standardized JSON format. In addition, we are happy to share new research/ publications spanning medical LLM safety evaluation and dual-level DICOM de-identification with Visual NLP.

- **Pretrained Zero Shot Multi Task** module: unified zero-shot NER, classification, relation, and structured extraction in one forward pass, with flexible configuration and a single output column for all tasks.
- `MedicalNerApproach` `explodeSentencesForTraining` (optional) to expand multi-sentence rows into sentence-level training examples before training, aimed at lower peak memory on long documents.
- `JSL_MedS NER (LLM — q16 — v5)` for Structured Clinical Trial Eligibility Parsing
- `DocumentHashCoder` Integration with Light Pipeline to Enable Consistent Hashing in Both Spark Pipeline Transforms and LightPipeline fullAnnotate-Style Inference.
- De-identification `setDeidMarkers` to wrap de-identified spans with configurable prefix/suffix markers in the deidentified text.
- Obfuscation evaluation: A new utility function to report leakage and success rates when comparing original vs obfuscated columns after structured data.
- Enhanced 14 New Entity Resolver Models for Mapping Clinical Terms to Standardized SNOMED CT Codes and LOINC
- New research publications, including a Text2Story 2026 paper on multi-domain red teaming for medical LLM safety evaluation and accepted work on dual-level DICOM de-identification using Visual NLP at **CVC 2026** and **ICHI 2026** (ICHI: *Beyond Metadata Scrubbing: Production-Scale Pixel-Level and Metadata-Level DICOM Anonymisation for Healthcare Workflows*).
- New Blog Posts & Technical Deep Dives
- Updated notebooks and demonstrations for making Healthcare NLP easier to navigate and understand
  - New [Pretrained Zero Shot Multi Task](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.8.PretrainedZeroShotMultiTask.ipynb) Notebook
- The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Healthcare NLP, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


<div class="h3-box" markdown="1">

#### PretrainedZeroShotMultiTask: Unified Zero-Shot Multi-Task Inference

`PretrainedZeroShotMultiTask` is a unified Spark NLP for Healthcare annotator that runs **Named Entity Recognition**, **Text Classification**, **Relation Extraction**, and **Structured Extraction** in a **single forward pass**, without task-specific fine-tuning or labeled training data. Configure tasks with `setEntities`, `setClassifications`, `setRelations`, and `setStructures`; all outputs are written to one output column (by default `extractions`) and are distinguished by `annotatorType` (`chunk`, `category`, `struct`).
Because outputs are mixed in one column, use **`MultiAnnotationSplitter`** (for example with `setSplitType("chunk")`) before downstream annotators that expect dedicated columns—such as **`DeIdentification`** for de-identification workflows.

**Pretrained models**
{:.table-model-big}
| Model Name  |      Description            |
|-------------|-----------------------------|
| [`zeroshot_multitask_generic`](https://nlp.johnsnowlabs.com/2026/04/09/zeroshot_multitask_generic_en.html) | Zero-shot multitask model for customizable entity extraction, structure filling, classification, and relation prediction over clinical documents. |
| [`zeroshot_multitask_base`](https://nlp.johnsnowlabs.com/2026/04/10/zeroshot_multitask_base_en.html) | Base variant of the zero-shot multitask model with the same task surface (entities, structures, classifications, relations). |

**Key parameters**
{:.table-model-big}
| Parameter | Description |
|----------|-------------|
| `setEntities(list)` | NER labels; optional `LABEL::description` for guided extraction (e.g., `"DRUG::medication name like aspirin"`). |
| `setClassifications(list)` | Tasks as `(task_name, [labels])` tuples; one label per document per task. |
| `setRelations(list)` | Relation types between entities (e.g., `"works_for"`, `"treatment_administered_for_problem"`). |
| `setStructures(list)` | Templates as `(name, [field_definitions])` with `field_name::type::description`. |
| `setEntityThreshold(float)` | Minimum entity confidence (default `0.4`). |


**Output annotation types**
{:.table-model-big}
| annotatorType | Task | Description |
|---------------|------|-------------|
| `chunk` | NER | Spans with entity, confidence, offsets |
| `category` | Classification / relation | Classification metadata includes `task` where applicable |
| `struct` | Structured extraction | Key-value style fields in metadata |


*Example*: basic four-task configuration (`zeroshot_multitask_base`)


```python
cancer_text = """The had previously undergone a left mastectomy and an axillary lymph node dissection for a left breast cancer twenty years ago.
The tumor was positive for ER and PR. Postoperatively, radiotherapy was administered to her breast.The cancer recurred as a right lung metastasis 13 years later.
The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses, as first line therapy."""

data = spark.createDataFrame([[cancer_text]]).toDF("text")

document_assembler = (
   DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)
model = PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_base", "en", "clinical/models")
zero_shot = (
    model
    .setInputCols(["document"])
    .setOutputCol("extractions")
    .setEntities([
            "Cancer_Dx::The exact cancer diagnosis phrase, such as 'left breast cancer' or 'lung cancer'. Extract only the diagnosis phrase itself.",
            "Site::The exact anatomical site phrase, including laterality when present, such as 'left breast' or 'right lung'. Extract only the site phrase itself.",
            "Biomarker::The exact biomarker name, such as 'ER', 'PR', 'HER2', or 'PD-L1'. Extract only the marker name itself.",
            "Biomarker_Result::The exact biomarker result term, such as 'positive', 'negative', 'amplified', 'high', or 'low'. Extract only the result term itself.",
            "Metastasis::The exact metastatic disease phrase including site when present, such as 'right lung metastasis' or 'bone metastasis'. Extract only the metastasis phrase itself.",
            "Cancer_Surgery::The exact cancer surgery phrase, including laterality when present, such as 'left mastectomy' or 'axillary lymph node dissection'. Extract only the procedure phrase itself.",
            "Chemotherapy::The exact chemotherapy drug name or treatment term, such as 'adriamycin', 'cyclophosphamide', or 'chemotherapy'. Extract only the drug or treatment term itself.",
            "Radiotherapy::The exact radiation treatment term, such as 'radiotherapy' or 'radiation therapy'. Extract only the treatment term itself, not surrounding action phrases, recipients, or body sites.",
            "Line_Of_Therapy::The exact treatment-line phrase, such as 'first line therapy' or 'second line treatment'. Extract only the treatment-line phrase itself.",
            "Response_To_Treatment::The exact response or progression term, such as 'recurred', 'progressed', 'improved', or 'stable disease'. Extract only the response term itself.",
            "Dosage::The exact dose expression, such as '60 mg/m2' or '400 mg'. Extract only the dose expression itself.",
            "Relative_Date::The exact relative time phrase, such as 'twenty years ago' or '13 years later'. Extract only the temporal phrase itself."
    ]
         )
    .setStructures([
    ("cancer_case", [
        "diagnosis::str::The exact cancer diagnosis phrase, such as 'left breast cancer' or 'lung cancer'. Extract only the diagnosis phrase itself.",
        "site::list::The exact anatomical site phrase related to the cancer, including laterality when present, such as 'left breast' or 'right lung'. Extract only the site phrase itself, not the diagnosis phrase.",
        "metastasis::list::The exact metastatic disease phrase, including site when present, such as 'right lung metastasis' or 'bone metastasis'. Extract only the metastasis phrase itself.",
        "surgery::list::The exact cancer-related surgery phrase, including laterality when present, such as 'left mastectomy' or 'axillary lymph node dissection'. Extract only the procedure phrase itself, not surrounding action phrases.",
        "radiotherapy::list::The exact radiation treatment term, such as 'radiotherapy' or 'radiation therapy'. Extract only the treatment term itself, not surrounding action phrases, recipients, or body sites.",
        "line_of_therapy::str::The exact treatment-line phrase, such as 'first line therapy' or 'second line therapy'. Extract only the treatment-line phrase itself.",
        "response::str::The exact response or progression term, such as 'recurred', 'progressed', 'improved', or 'stable disease'. Extract only the response term itself.",
        "relative_date::list::The exact relative time phrase, such as 'twenty years ago' or '13 years later'. Extract only the temporal phrase itself."
    ]),
    ("biomarker_item", [
        "name::str::The exact biomarker name, such as 'ER', 'PR', 'HER2', or 'PD-L1'. Extract only the biomarker name itself.",
        "result::str::The exact biomarker result term associated with that biomarker, such as 'positive', 'negative', 'amplified', 'high', or 'low'. Extract only the result term itself."
    ]),
    ("chemotherapy_item", [
        "drug::str::The exact chemotherapy drug name, such as 'adriamycin' or 'cyclophosphamide'. Extract only the drug name itself.",
        "dosage::str::The exact dose expression associated with the drug, such as '60 mg/m2' or '600 mg/m2'. Extract only the dosage expression itself."
    ])
])
    .setEntityThreshold(0.4)
)

results = Pipeline().setStages([document_assembler, zero_shot]).fit(data).transform(data)

```

*Result*:

```python
{
  "cancer_case": [
    {
      "diagnosis": "left breast cancer",
      "site": [
        "left breast"
      ],
      "metastasis": [
        "right lung metastasis"
      ],
      "surgery": [
        "left mastectomy",
        "axillary lymph node dissection"
      ],
      "radiotherapy": [
        "radiotherapy"
      ],
      "line_of_therapy": "first line therapy",
      "response": "recurred",
      "relative_date": [
        "13 years later",
        "twenty years ago"
      ]
    }
  ],
  "biomarker_item": [
    {
      "name": "ER",
      "result": "positive"
    },
    {
      "name": "PR",
      "result": "positive"
    }
  ],
  "chemotherapy_item": [
    {
      "drug": "adriamycin",
      "dosage": "60 mg/m2"
    },
    {
      "drug": "cyclophosphamide",
      "dosage": "600 mg/m2"
    }
  ]
}
```

  PretrainedZero-Shot Multi-Task models are designed to perform multiple tasks in one pass, but if you only want to run NER, for example, you can simply configure the model with `setEntities` and leave other task setters empty.  The output will still be in the same `extractions` column, but will only contain `chunk` annotations for the NER task. You can then use `MultiAnnotationSplitter` to split out the `chunk` annotations into a separate column for downstream processing.
This flexibility allows you to create De-Identification pipelines that leverage the zero-shot NER capabilities of `PretrainedZeroShotMultiTask` without needing to configure classification, relation, or structured extraction tasks if they are not needed for your use case.

```python
data = spark.createDataFrame(
    [["Dr. John Smith works at Google in New York. The product costs $99. Sentiment: very positive."]]
).toDF("text")

document_assembler = DocumentAssembler().setInputCol("text").setOutputCol("document")

zero_shot_multi_task = (
    PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_base", "en", "clinical/models")
    .setInputCols(["document"])
    .setOutputCol("extractions")
    .setEntities(["NAME::name of person", "LOCATION::city or place name", "ORGANIZATION::company name"])
    .setEntityThreshold(0.7)
)

multi_annotation_splitter = (
    MultiAnnotationSplitter()
    .setInputCols("extractions")
    .setOutputCol("ner_chunk")
    .setSplitType("chunk")
)

light_deid = LightDeIdentification().setInputCols("document", "ner_chunk").setOutputCol("deid")

full_pipe = Pipeline(stages=[document_assembler, zero_shot_multi_task, multi_annotation_splitter, light_deid]).fit(data)
full_pipe.transform(data).select("deid").show(truncate=False)

```

*Result*:
```text
+------------------------------------------------------------------------------------------------+
|result                                                                                          |
+------------------------------------------------------------------------------------------------+
|[<NAME> works at <ORGANIZATION> in <LOCATION>. The product costs $99. Sentiment: very positive.]|
+------------------------------------------------------------------------------------------------+
```

Please check more detail explanations in the **Workshop notebook**
- [1.8.PretrainedZeroShotMultiTask](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.8.PretrainedZeroShotMultiTask.ipynb)


</div><div class="h3-box" markdown="1">

#### JSL_MedS NER (LLM — q16 — v5) for Structured Clinical Trial Eligibility Parsing

This release adds **JSL_MedS NER (LLM — q16 — v5)**, a Medical LLM–based named entity recognition model that extracts structured entities from clinical trial eligibility criteria. Given unstructured inclusion and exclusion text, it returns JSON with **inclusion** and **exclusion** entity lists. The model supports four entity types — **age**, **lab**, **condition**, and **pregnancy** — each following a fixed schema with normalized values and numeric thresholds where applicable.

The model is intended for clinical trial eligibility parsing, patient matching, and structured medical information extraction workflows, and runs on the **llama.cpp** engine via the `MedicalLLM` family in Healthcare NLP.

{:.table-model-big}
| **Model Name**                                                                                | **Description** |
| --------------------------------------------------------------------------------------------- | ----------------- |
| [jsl_meds_ner_q16_v5](https://nlp.johnsnowlabs.com/2026/04/09/jsl_meds_ner_q16_v5_en.html)    |  This LLM model extracts structured entities from clinical trial eligibility criteria. Given unstructured text, it returns JSON with inclusion and exclusion entities. The model supports four entity types: age, lab, condition, and pregnancy. Each entity follows a fixed schema with normalized values and numeric thresholds where applicable. This model is intended for clinical trial eligibility parsing, patient matching, and structured medical information extraction workflows. |


*Example*: jsl_meds_ner_q16_v5

```python

documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

llm = MedicalLLM.pretrained("jsl_meds_ner_q16_v5", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("llm_output")

pipeline = Pipeline(stages=[documentAssembler, llm])

text = """
Inclusion Criteria:
Adults aged 18–75 with confirmed type 2 diabetes mellitus. HbA1c 7.0–10.5%.
Fasting plasma glucose ≥126 mg/dL. Negative pregnancy test required.

Exclusion Criteria:
Type 1 diabetes mellitus. HbA1c >10.5%. Fasting plasma glucose >300 mg/dL.
Pregnant or breastfeeding. Diabetic ketoacidosis. Uncontrolled thyroid disease.
"""
data = spark.createDataFrame([[text]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

```

Result:

```json

{
  "inclusion": [
    {"type":"age","min_years":18,"max_years":75},
    {"type":"condition","name":"type 2 diabetes mellitus"},
    {"type":"lab","name":"HbA1c","min_percent":7.0,"max_percent":10.5},
    {"type":"lab","name":"fasting plasma glucose","min_value":126},
    {"type":"pregnancy","status":"negative_pregnancy_test"}
  ],
  "exclusion": [
    {"type":"condition","name":"type 1 diabetes mellitus"},
    {"type":"lab","name":"HbA1c","max_percent":10.5},
    {"type":"lab","name":"fasting plasma glucose","max_value":300},
    {"type":"pregnancy","status":"pregnant_or_lactating"},
    {"type":"condition","name":"diabetic ketoacidosis"},
    {"type":"condition","name":"uncontrolled thyroid disease"}
  ]
}
```

Overall, this release extends our Medical LLM portfolio with a production-oriented model for structured eligibility parsing, helping teams move from free-text trial criteria to machine-readable JSON for downstream matching and analytics.

</div><div class="h3-box" markdown="1">

#### Lower-Memory NER Training via `explodeSentencesForTraining` Parameter
`MedicalNerApproach` now supports an optional training-time preprocessing step that splits multi-sentence rows into **one row per sentence** before training. This can reduce **peak memory usage** and improve training efficiency on long documents.
The new behavior is controlled by **`explodeSentencesForTraining`** and is **disabled by default** (`False`).


**Performance (example benchmark)**
*Dataset: 30 documents, ~30,000 characters.*
{:.table-model-big}
| **explodeSentencesForTraining** | **Approx. training time** | **Approx. peak RAM** |
|--------------------------------|--------------------------:|---------------------:|
| `True`                         | ~11 minutes               | ~9.3 GB              |
| `False`                        | ~24 minutes               | ~30 GB               |

*Note: Results may vary depending on hardware, Spark configuration, dataset characteristics, and model hyperparameters.*

**What changed**
- Added **`explodeSentencesForTraining`** to `MedicalNerApproach`.
- Kept validation splitting at **document level first**, then optionally **exploded each split into sentence rows** for training.
*Example*:

```python
nerTagger = (
    MedicalNerApproach()
    .setInputCols(["splitter", "token", "embeddings"])
    .setLabelColumn(LABEL_COLUMN)
    .setOutputCol("ner")
    .setMaxEpochs(30)
    .setBatchSize(8)
    .setRandomSeed(0)
    .setVerbose(1)
    .setValidationSplit(0.2)
    .setEvaluationLogExtended(True)
    .setEnableOutputLogs(True)
    .setIncludeConfidence(True)
    .setOutputLogsPath("ner_logs")
    .setEarlyStoppingCriterion(0.01)
    .setEarlyStoppingPatience(5)
    .setUseBestModel(False)
    .setExplodeSentencesForTraining(True)  # default: False; set to True to enable sentence explosion
)
training_pipeline = Pipeline(stages=[nerDLGraphChecker, nerTagger])
ner_model_nosplit = training_pipeline.fit(train_df)

```


<div class="h3-box" markdown="1">

#### DocumentHashCoder Integration with Light Pipeline to Enable Consistent Hashing in Both Spark Pipeline Transforms and LightPipeline fullAnnotate-Style Inference

DocumentHashCoder has been updated to be compatible with LightPipeline.
With this enhancement, the same hashing behavior is preserved across both standard Spark Pipeline flows and low-latency LightPipeline inference.


*Example*: DocumentHashCoder with transform()

```python
from pyspark.ml import Pipeline
from sparknlp.base import DocumentAssembler, LightPipeline
from sparknlp_jsl.annotator import DocumentHashCoder


data = spark.createDataFrame(
    [
        (1, "Patient has diabetes and hypertension."),
        (2, "No acute cardiopulmonary process detected."),
    ],
    ["id", "text"],
)

document_assembler = (
    DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

document_hasher = (
    DocumentHashCoder()
    .setInputCols("document")
    .setOutputCol("hashed_document")
    .setPatientIdColumn("id")
    .setRangeDays(100)
    .setNewDateShift("shift_days")
    .setSeed(42)
)

pipeline = Pipeline(stages=[document_assembler, document_hasher])
model = pipeline.fit(data)

# Spark pipeline output
transformed = model.transform(data)
transformed.select("id", "hashed_document").show(truncate=False)

```
*Result*:

```text
+---+----------------------------------------------------------------------------------------------------------------------+
|id |hashed_document                                                                                                       |
+---+----------------------------------------------------------------------------------------------------------------------+
|1  |[{document, 0, 37, Patient has diabetes and hypertension., {sentence -> 0, patientId -> 1, dateshift -> 47}, []}]     |
|2  |[{document, 0, 41, No acute cardiopulmonary process detected., {sentence -> 0, patientId -> 2, dateshift -> -26}, []}]|
+---+----------------------------------------------------------------------------------------------------------------------+
```

*Example*: DocumentHashCoder with fullAnnotate()

```python
# LightPipeline output
texts = [
    "Patient has diabetes and hypertension.",
    "No acute cardiopulmonary process detected.",
]

light = LightPipeline(model)
light_out = light.fullAnnotate(texts, metadata={"id": ["1", "2"]})

print(light_out[0]["hashed_document"])
print(light_out[1]["hashed_document"])

```

*Result*:

```text
[Annotation(document, 0, 37, Patient has diabetes and hypertension., {'sentence': '0', 'patientId': '1', 'dateshift': '47'}, [])]
[Annotation(document, 0, 41, No acute cardiopulmonary process detected., {'sentence': '0', 'patientId': '2', 'dateshift': '-26'}, [])]
```



</div><div class="h3-box" markdown="1">

#### De-identification setDeidMarkers to wrap de-identified spans with configurable prefix/suffix markers in the deidentified text.
`DeIdentification` now supports **`setDeidMarkers`**, which defines the **prefix and suffix markers** used to wrap de-identified entity spans in the output text.
- The **first** value is the **prefix** marker and the **second** is the **suffix** marker.  
  Example: `("[START]", "[END]")` can wrap sensitive spans so the output reads like `[START]...entity text...[END]` (depending on mode and pipeline configuration).

**Parameter formats**
- **List or tuple:** `(prefix, suffix)` — e.g. `("<DEID>", "</DEID>")`
- **Dict:** keys **`start`** (prefix) and/or **`end`** (suffix). If only one key is provided, the other defaults to `""`. Valid keys are **`start`** and **`end`** only.

*Example*:
```python
light_de_identification = (
    LightDeIdentification()
    .setInputCols(["ner_chunk", "document"])
    .setOutputCol("dei")
    .setMode("obfuscate")
    .setObfuscateRefSource("faker")
    .setSeed(10)
    .setDeidMarkers({"start": "[S]", "end": "[E]"})
)

```

*Result*:


Original document text:
```text
Patient John Doe was seen in the clinic.
```

De-identified text (obfuscated), with markers:
```text
Patient [S]Valerie Aho[E] was seen in the clinic.
```

</div><div class="h3-box" markdown="1"><div class="h3-box" markdown="1">

#### Obfuscation evaluation: A new utility function to report leakage and success rates when comparing original vs obfuscated columns after structured data.

A new helper, **`evaluate_obfuscation`**, is available to measure **obfuscation quality** on a Spark `DataFrame` by comparing **original** and **obfuscated** column values. It reports **leakage** (rows where sensitive values were unchanged) and **success rate** (complement of leakage rate among evaluated rows).

**Behavior**

- Compares `original_col` vs `obfuscated_col` row-wise.
- **`null_handling`**: `ignore` (skip rows where both sides are null/empty), `equal` (treat null as empty string before compare), or `strict` (no null normalization). Default: `ignore`.
- **`normalize_strings`**: optional whitespace trim before comparison; comparison remains **case-sensitive**. Default: `True`.

**Returns**

A `dict` with:

- `total_rows` — rows included after filtering  
- `leakage_count` — rows where original equals obfuscated  
- `leakage_rate` — `leakage_count / total_rows`  
- `success_rate` — `1 - leakage_rate` (for evaluated rows)

*Example* (with `StructuredDeidentification`):

```python
from sparknlp_jsl.utils import evaluate_obfuscation
from sparknlp_jsl.structured_deidentification import StructuredDeidentification

obfuscator = StructuredDeidentification(
    spark=spark,
    columns={"NAME": "NAME"},
    obfuscateRefSource="faker",
)

obfuscated_df = obfuscator.obfuscateColumns(
    df,
    outputAsArray=False,
    overwrite=False,
    suffix="_OBFUSCATED",
)

eval_result = evaluate_obfuscation(
    obfuscated_df,
    original_col="NAME",
    obfuscated_col="NAME_OBFUSCATED",
    null_handling="strict",
    normalize_strings=True,
)

print(eval_result)

```

*Result*:

```python
{
  "total_rows": 1000,
  "leakage_count": 0,
  "leakage_rate": 0.0,
  "success_rate": 1.0,
}
```

#### Enhanced 14 New Entity Resolver Models for Mapping Clinical Terms to Standardized SNOMED CT Codes and LOINC

We are updating our **SentenceEntityResolver** (resolving named entities to medical terminologies) lineup with **four LOINC ** and **ten SNOMED CT ** models, covering laboratory and clinical observation coding (LOINC) and  SNOMED CT concept resolution across multiple semantic slices.

**LOINC resolvers** map extracted clinical entities to **Logical Observation Identifiers Names and Codes (LOINC)** using sentence embeddings; resolutions include the official LOINC description in brackets where applicable. The family is trained against **LOINC v2.81** and follows the same NER → chunk → `BertSentenceEmbeddings` → resolver pattern as our existing LOINC resolvers, with variants for **augmented** and **numeric-augmented** training, a **base** SBioBERT-cased model, and an **uncased BlueBERT** (`sbluebertresolve_loinc_uncased`) option for case-insensitive matching.

**SNOMED resolvers** map clinical entities and concepts to **SNOMED CT** codes using **`sbiobert_base_cased_mli`** sentence embeddings (and **`mpnet_embeddings_biolord_2023_c`** for [`biolordresolve_snomed_findings_aux_concepts`](https://nlp.johnsnowlabs.com/2026/03/16/biolordresolve_snomed_findings_aux_concepts_en.html)), with models specialized by domain (e.g. conditions, drugs, body structure, findings, procedures and measurements, veterinary, auxiliary concepts).

**LOINC models**
{:.table-model-big}
| Model Name | Description |
|------------|-------------|
| [`sbiobertresolve_loinc_augmented`](https://nlp.johnsnowlabs.com/2026/02/02/sbiobertresolve_loinc_augmented_en.html) | Maps medical entities to LOINC codes (augmented variant) |
| [`sbiobertresolve_loinc`](https://nlp.johnsnowlabs.com/2026/02/02/sbiobertresolve_loinc_en.html) | Maps extracted medical entities to LOINC codes using `sbiobert_base_cased_mli` |
| [`sbiobertresolve_loinc_numeric_augmented`](https://nlp.johnsnowlabs.com/2026/02/02/sbiobertresolve_loinc_numeric_augmented_en.html) | Maps medical entities to LOINC codes (numeric-augmented variant) |
| [`sbluebertresolve_loinc_uncased`](https://nlp.johnsnowlabs.com/2026/03/05/sbluebertresolve_loinc_uncased_en.html) | Uncased BlueBERT-based LOINC sentence resolver |

**SNOMED models**
{:.table-model-big}
| Model Name | Description |
|------------|-------------|
| [`sbiobertresolve_snomed_auxConcepts`](https://nlp.johnsnowlabs.com/2026/03/15/sbiobertresolve_snomed_auxConcepts_en.html) | Maps clinical entities and concepts to SNOMED CT (auxiliary concepts scope) |
| [`sbiobertresolve_snomed_bodyStructure`](https://nlp.johnsnowlabs.com/2026/03/15/sbiobertresolve_snomed_bodyStructure_en.html) | Maps entities to SNOMED CT for body structure concepts |
| [`sbiobertresolve_snomed_conditions`](https://nlp.johnsnowlabs.com/2026/03/15/sbiobertresolve_snomed_conditions_en.html) | Maps entities to SNOMED CT for clinical conditions |
| [`sbiobertresolve_snomed_drug`](https://nlp.johnsnowlabs.com/2026/03/15/sbiobertresolve_snomed_drug_en.html) | Maps entities to SNOMED CT for drug-related concepts |
| [`biolordresolve_snomed_findings_aux_concepts`](https://nlp.johnsnowlabs.com/2026/03/16/biolordresolve_snomed_findings_aux_concepts_en.html) | SNOMED findings / auxiliary concepts using Biolord sentence embeddings |
| [`sbiobertresolve_snomed_findings_aux_concepts`](https://nlp.johnsnowlabs.com/2026/03/16/sbiobertresolve_snomed_findings_aux_concepts_en.html) | SNOMED findings with auxiliary concepts (SBioBERT) |
| [`sbiobertresolve_snomed_findings`](https://nlp.johnsnowlabs.com/2026/03/16/sbiobertresolve_snomed_findings_en.html) | Maps clinical findings to SNOMED CT |
| [`sbiobertresolve_snomed_no_class`](https://nlp.johnsnowlabs.com/2026/03/16/sbiobertresolve_snomed_no_class_en.html) | SNOMED resolution without a fixed semantic-class constraint |
| [`sbiobertresolve_snomed_procedures_measurements`](https://nlp.johnsnowlabs.com/2026/03/16/sbiobertresolve_snomed_procedures_measurements_en.html) | Maps procedures and measurements to SNOMED CT |
| [`sbiobertresolve_snomed_veterinary`](https://nlp.johnsnowlabs.com/2026/03/16/sbiobertresolve_snomed_veterinary_en.html) | Maps entities to SNOMED CT in a veterinary-focused setting |

*Example* (LOINC — `sbiobertresolve_loinc`):

```python

document_assembler = nlp.DocumentAssembler()\
	.setInputCol("text")\
	.setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
	.setInputCols(["document"]) \
	.setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
	.setInputCols(["sentence"])\
	.setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
	.setInputCols(["sentence", "token"])\
	.setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models") \
	.setInputCols(["sentence", "token", "embeddings"]) \
	.setOutputCol("ner")

ner_converter = medical.NerConverterInternal() \
 	.setInputCols(["sentence", "token", "ner"]) \
	.setOutputCol("ner_chunk")\
	.setWhiteList(["Test"])

chunk2doc = medical.Chunk2Doc()\
  .setInputCols("ner_chunk")\
  .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
	.setInputCols(["ner_chunk_doc"])\
	.setOutputCol("sbert_embeddings")\
	.setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc","en", "clinical/models") \
	.setInputCols(["sbert_embeddings"]) \
	.setOutputCol("resolution")\
	.setDistanceFunction("EUCLIDEAN")

nlpPipeline = nlp.Pipeline(stages=[document_assembler,
                               sentence_detector,
                               tokenizer,
                               word_embeddings,
                               ner_model,
                               ner_converter,
                               chunk2doc,
                               sbert_embedder,
                               resolver])

data = spark.createDataFrame([["""A 65-year-old woman presents to the office with generalized fatigue for the last 4 months.
  She used to walk 1 mile each evening but now gets tired after 1-2 blocks. She has a history of Crohn disease and hypertension
  for which she receives appropriate medications. She is married and lives with her husband. She eats a balanced diet that
  includes chicken, fish, pork, fruits, and vegetables. She rarely drinks alcohol and denies tobacco use. A physical examination
  is unremarkable. Laboratory studies show the following: Hemoglobin: 9.8g/dL, Hematocrit: 32%, Mean Corpuscular Volume: 110 μm3"""]]).toDF("text")

result = nlpPipeline.fit(data).transform(data)

```

Result (LOINC):

{:.table-model-big}

| chunk                     | begin | end | ner_label | loinc_code | description                                                                 | resolutions                                                                 | all_codes                                                                 | aux_labels                                                                 |
|--------------------------|-------|-----|-----------|------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| physical examination     | 450   | 469 | Test      | 29544-4    | Physical findings [Physical findings]                                         | Physical findings [Physical findings]:::Physical findings...                 | 29544-4:::29545-1:::55286-9:::11435-5:::11384-5:::8709-8:...                | ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACT...                |
| Laboratory studies       | 490   | 507 | Test      | 26436-6    | Laboratory studies (set) [Laboratory studies (set)]                           | Laboratory studies (set) [Laboratory studies (set)]:::Lab...                 | 26436-6:::52482-7:::11502-2:::34075-2:::100455-5:::85069-...               | ACTIVE:::DISCOURAGED:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:...               |
| Hemoglobin               | 529   | 538 | Test      | 10346-5    | Hemoglobin [Hemoglobin A [Units/volume] in Blood by Elect...]                | Hemoglobin [Hemoglobin A [Units/volume] in Blood by Elect...]               | 10346-5:::109592-6:::11559-2:::2030-5:::34618-9:::38896-7...               | ACTIVE:::TRIAL:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTI...               |
| Hematocrit               | 550   | 559 | Test      | 11559-2    | Fractional hemoglobin [Fractional oxyhemoglobin in Blood]                    | Fractional hemoglobin [Fractional oxyhemoglobin in Blood]...                | 11559-2:::10346-5:::41986-1:::48703-3:::55103-6:::8478-0:...               | ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACT...               |
| Mean Corpuscular Volume  | 567   | 589 | Test      | 30386-7    | Erythrocyte mean corpuscular diameter [Length] [Erythrocy...]                | Erythrocyte mean corpuscular diameter [Length] [Erythrocy...]               | 30386-7:::101864-7:::20161-6:::18033-1:::19853-1:::101150...               | ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACT...               |

*Example* (SNOMED — sbiobertresolve_snomed_auxConcepts):

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

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en", "clinical/models")\
      .setInputCols(["sentence", "token"])\
      .setOutputCol("embeddings")

ner_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
      .setInputCols(["sentence", "token", "embeddings"])\
      .setOutputCol("ner_jsl")

ner_jsl_converter = NerConverterInternal()\
      .setInputCols(["sentence", "token", "ner_jsl"])\
      .setOutputCol("ner_jsl_chunk")\
      .setWhiteList(["Procedure","Substance","Drug_Ingredient","Internal_organ_or_component","Modifier","BMI","LDL","External_body_part_or_region","Alcohol","Treatment","Test","Smoking"])

chunk2doc = Chunk2Doc()\
      .setInputCols("ner_jsl_chunk")\
      .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
     .setInputCols(["ner_chunk_doc"])\
     .setOutputCol("sbert_embeddings")\
     .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_auxConcepts","en","clinical/models")\
     .setInputCols(["sbert_embeddings"])\
     .setOutputCol("snomed_code")\
     .setDistanceFunction("EUCLIDEAN")

nlpPipeline= Pipeline(stages=[
                              documentAssembler,
                              sentenceDetector,
                              tokenizer,
                              word_embeddings,
                              ner_jsl,
                              ner_jsl_converter,
                              chunk2doc,
                              sbert_embedder,
                              snomed_resolver
])

sample_text = """This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction. He was subsequently transferred to the CCU for close monitoring. He was hemodynamically stable at the time of admission to the CCU."""

df= spark.createDataFrame([[sample_text]]).toDF("text")

result= nlpPipeline.fit(df).transform(df)

```

Result (SNOMED):

{:.table-model-big}


| sent_id | ner_chunk               | entity          | snomed_code | resolution              | all_codes                                                                                            | all_resolutions                                                                                      | aux_list                                                                                                 |
| ------- | ----------------------- | --------------- | ----------- | ----------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| 0       | tobacco                 | Smoking         | 57264008    | tobacco                 | [57264008, 102407002, 39953003, 159882006, 230491000087101, 102408007, 722496004, 38402001, 7110...] | [tobacco, tobacco smoke, tobacco - substance, tobacco processor, shisha tobacco, cigarette smoke...] | [Organism, Substance, Substance, Social Context, No_Concept_Class, Substance, Physical Object, ...]      |
| 1       | nonspecific             | Modifier        | 10003008    | non-specific            | [10003008, 261992003, 863956004, 300844001, 278001007, 863967003, 236821005, 276119007, 12170110...] | [non-specific, non-biological, non-sterile, non-resonant, nonspecific site, non-absorbable, ...]     | [Qualifier Value, Qualifier Value, Qualifier Value, Qualifier Value, Body Structure, Qualifier Value...] |
| 2       | cardiac catheterization | Procedure       | 41976001    | cardiac catheterization | [41976001, 705923009, 721968000, 467735004, 129085009, 425315000, 128956009, 467525008, 12895700...] | [cardiac catheterization, cardiac catheter, cardiac catheterization report, ...]                     | [Procedure, Physical Object, Record Artifact, Physical Object, Qualifier Value, Procedure, ...]          |
| 3       | atropine                | Drug_Ingredient | 73949004    | atropine                | [73949004, 105075009, 349945006, 410493009, 74237004, 50507004, 109207004, 349946007, 34013000...]   | [atropine, atropine measurement, oral atropine, atropinization, atropine sulfate, ...]               | [Pharma/Biol Product, Procedure, Clinical Drug Form, Procedure, Substance, Substance, ...]               |
| 3       | fluids                  | Drug_Ingredient | 255765007   | fluid                   | [255765007, 246498002, 258442002, 251851008, 32457005, 396276007, 406142009, 251840008, 33463005...] | [fluid, fluid used, fluid sample, fluid input, body fluid, fluid appearance, ...]                    | [Qualifier Value, Attribute, Specimen, Observable Entity, Substance, Observable Entity, ...]             |
| 3       | dopamine                | Drug_Ingredient | 59187003    | dopamine                | [59187003, 412383006, 37484001, 32779004, 412845004, 713493000, 418222008, 12307008, 384952006...]   | [dopamine, dopamine agent, dopamine receptor, dopamine measurement, serum dopamine level, ...]       | [Pharma/Biol Product, Substance, Substance, Procedure, Procedure, Substance, ...]                        |

</div><div class="h3-box" markdown="1">


#### New Research Publications

-  ***A Multi-Domain Red Teaming Framework for Safety, Robustness, and Fairness Evaluation of Medical Large Language Models*** Presented at **Text2Story 2026**, this work introduces a multi-domain red teaming framework evaluating medical LLMs across hundreds of clinically grounded scenarios spanning multiple domains and subcategories, combining adversarial transformations with a seven-dimension rubric, LLM-assisted scoring, and human-in-the-loop validation. The findings highlight substantial performance variance across models, meaningful worst-case failures even among high aggregate scores, equity-related sensitivity under demographic modifications, and the importance of hybrid (automated + clinician) evaluation for credible safety assessment.

- ***Comprehensive DICOM Deidentification Using Visual NLP: A Dual-Level Approach to Privacy-Preserving Medical Imaging*** Accepted at the **Computer Vision Conference (CVC) 2026**, this paper describes a dual-level DICOM de-identification methodology using John Snow Labs Visual NLP to address PHI in both pixel-level image content and DICOM metadata. Evaluated on the MIDI-B dataset, the approach reports strong validation outcomes—including high accuracy for text processing and consistent handling of key metadata operations—while aiming to preserve clinical utility for research-oriented use cases.

- ***Beyond Metadata Scrubbing: Production-Scale Pixel-Level and Metadata-Level DICOM Anonymisation for Healthcare Workflows*** Accepted at the **2026 IEEE 14th International Conference on Healthcare Informatics (ICHI)** under this title, covering production-scale DICOM anonymisation at both pixel and metadata levels for healthcare workflows. This entry corresponds to the full contribution summarized under *Comprehensive DICOM Deidentification Using Visual NLP: A Dual-Level Approach to Privacy-Preserving Medical Imaging*.

</div><div class="h3-box" markdown="1">

#### New Blog Posts & Technical Deep Dives

- [Running the Latest LLMs on Spark: Llama.cpp Integration Gets a Major Upgrade](https://medium.com/john-snow-labs/running-the-latest-llms-on-spark-llama-cpp-integration-gets-a-major-upgrade-209afc1449aa) This blog post describes how Spark NLP’s Llama.cpp stack was upgraded (including Spark NLP and a newer upstream Llama.cpp release) to support a broader set of modern LLM families—quantized GGUF models and multimodal variants—with faster, more memory-efficient inference on CPUs and typical hardware. It explains how **AutoGGUFModel** and related annotators plug into Spark ML pipelines, how to use pretrained GGUF checkpoints or load your own `.gguf` files, and why keeping pace with Llama.cpp helps teams run the latest open models at Spark scale with minimal extra infrastructure.

- [Multilingual Clinical NER with ONNX: New Models for Entity Extraction Across Languages](https://medium.com/john-snow-labs/multilingual-clinical-ner-with-onnx-new-models-for-entity-extraction-across-languages-fbd7d0d249ad) This blog post introduces new ONNX-based clinical Named Entity Recognition models for English, Italian, and Spanish in John Snow Labs Healthcare NLP, aimed at extracting core medical entities such as diseases, procedures, medications, and symptoms with production-ready performance. It outlines why ONNX is a practical deployment format for clinical NLP, how these models fit into Spark NLP–style pipelines, and how multilingual coverage supports structured extraction from non-English clinical narratives alongside the existing English foundation.

</div><div class="h3-box" markdown="1">


#### Updated Notebooks And Demonstrations For making Healthcare NLP Easier To Navigate And Understand

- New [Pretrained Zero Shot Multi Task](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.8.PretrainedZeroShotMultiTask.ipynb) Notebook

</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.


+ `jsl_meds_ner_q16_v5`
+ `sbiobertresolve_loinc_augmented`
+ `sbiobertresolve_loinc`
+ `sbiobertresolve_loinc_numeric_augmented`
+ `sbluebertresolve_loinc_uncased`
+ `zeroshot_multitask_generic`
+ `zeroshot_multitask_base`
+ `sbiobertresolve_snomed_auxConcepts`
+ `sbiobertresolve_snomed_bodyStructure`
+ `sbiobertresolve_snomed_conditions`
+ `sbiobertresolve_snomed_drug`
+ `biolordresolve_snomed_findings_aux_concepts`
+ `sbiobertresolve_snomed_findings_aux_concepts`
+ `sbiobertresolve_snomed_findings`
+ `sbiobertresolve_snomed_no_class`
+ `sbiobertresolve_snomed_procedures_measurements`
+ `sbiobertresolve_snomed_veterinary`
+ `rxnorm_umls_mapper`
+ `umls_rxnorm_mapper`
+ `umls_cpt_mapper`
+ `cpt_umls_mapper`
+ `snomed_umls_mapper`
+ `umls_snomed_mapper`
+ `account_parser_pipeline`
+ `age_parser_pipeline`
+ `bgeresolve_cpt_pipeline`
+ `bgeresolve_icd10cm_pipeline`
+ `bgeresolve_rxnorm_pipeline`
+ `bgeresolve_snomed_pipeline`
+ `cpt_mapper_pipeline`
+ `cpt_parser_pipeline`
+ `date_of_birth_parser_pipeline`
+ `date_of_death_parser_pipeline`
+ `date_regex_matcher_pipeline`
+ `dln_parser_pipeline`
+ `drug_form_matcher_pipeline`
+ `drug_route_matcher_pipeline`
+ `drug_strength_parser_pipeline`
+ `email_regex_matcher_pipeline`
+ `generic_classifier_measurement_pipeline`
+ `icd10_parser_pipeline`
+ `icd10cm_mapper_pipeline`
+ `icd10cm_umls_mapping`
+ `ip_regex_matcher_pipeline`
+ `license_parser_pipeline`
+ `loinc_umls_mapping`
+ `med_parser_pipeline`
+ `medical_device_matcher_pipeline`
+ `mesh_umls_mapping`
+ `ner_deid_generic_nonMedical_pipeline`
+ `ner_deid_subentity_nonMedical_pipeline`
+ `ner_drugs_large_v2_pipeline`
+ `phone_parser_pipeline`
+ `plate_parser_pipeline`
+ `procedure_matcher_pipeline`
+ `rxnorm_mapper_pipeline`
+ `rxnorm_umls_mapping`
+ `snomed_umls_mapping`
+ `specimen_parser_pipeline`
+ `ssn_parser_pipeline`
+ `symptom_matcher_pipeline`
+ `umls_clinical_drugs_mapping`
+ `umls_clinical_findings_mapping`
+ `umls_disease_syndrome_mapping`
+ `umls_drug_substance_mapping`
+ `umls_icd10cm_mapping`
+ `umls_loinc_mapping`
+ `umls_major_concepts_mapping`
+ `umls_mesh_mapping`
+ `umls_rxnorm_mapping`
+ `umls_snomed_mapping`
+ `url_regex_matcher_pipeline`
+ `vin_parser_pipeline`
+ `zeroshot_ner_deid_generic_nonMedical_large_pipeline`
+ `zeroshot_ner_deid_generic_nonMedical_medium_pipeline`
+ `zeroshot_ner_deid_subentity_nonMedical_large_pipeline`
+ `zeroshot_ner_deid_subentity_nonMedical_medium_pipeline`
+ `zip_regex_matcher_pipeline`

</div><div class="h3-box" markdown="1">

## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
