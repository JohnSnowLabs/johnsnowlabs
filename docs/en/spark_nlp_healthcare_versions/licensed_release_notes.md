---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/licensed_release_notes
key: docs-licensed-release-notes
modify_date: 2026-06-26
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 6.4.1

#### Highlights

We are delighted to announce notable enhancements and updates in Healthcare NLP 6.4.1. The headline addition is **LLM-Based Structured Clinical Entity Extraction** module, an end-to-end LLM-powered entity extraction annotator for healthcare and clinical text, built on top of the `MedicalLLM` models. This module enables unified extraction of structured clinical entities directly from unstructured medical text, streamlining clinical NLP workflows by removing the need for task-specific pipelines.

This release also introduces important improvements in CDA de-identification through enhancements to the CDA DeIdentification module, featuring a table-aware, dual-model de-identification framework designed to jointly handle structured tabular data and unstructured clinical text, improving PHI detection accuracy in complex real-world CDA documents. 

In addition, StructuredDeIdentification has been extended with native support for TIMESTAMP and TIMESTAMP_WITH_TIMEZONE entities, enabling deterministic time shifting in structured medical tables with configurable seconds-based offsets and flexible timestamp format parsing.

This release also delivers a comprehensive UMLS 2026AA Metathesaurus refresh, encompassing 7 updated Entity Resolver models and an expanded ChunkMapper suite of 36 models — including 17 new mappers extending coverage to 8 additional medical coding systems — enabling broader and more current clinical concept mapping across standardized terminologies.

This release is further complemented by new benchmarking results and applied research contributions across clinical NLP and LLM-based healthcare extraction. Internal benchmarks demonstrate improved domain-specific PHI detection performance and CPU efficiency compared to general-purpose privacy filters. New notebooks introduce end-to-end workflows for LLM-based structured extraction, oncology entity recognition, and large-scale Spark NLP benchmarking on Databricks, leveraging MedicalLLM models and Medallion architecture (a bronze/silver/gold lakehouse pattern) for production-grade Healthcare NLP pipelines.


- LLM-Based Structured Clinical Entity Extraction with Constrained Decoding
- Table-Aware, Free-Text Extended CDA De-Identification with Improved PHI Accuracy in CDA Tables
- Pretrained Zero-Shot Multi-Task Named Entity Recognition (NER) Speed Comparison on GPU vs CPU Benchmark
- StructuredDeIdentification – Timestamp Support & Time Shift Enhancement
- Updated 7 UMLS Entity Resolver Models and 19 ChunkMapper Models to the UMLS 2026AA Metathesaurus and Introduced 17 New ChunkMapper Models Covering 8 Additional Medical Coding Systems
- New Blog Posts & Technical Deep Dives
- Updated notebooks and demonstrations for making Healthcare NLP easier to navigate and understand
  - New [MedicalLLMEntityExtractor](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.2.MedicalLLMEntityExtractor.ipynb) Notebook
  - New [LLM-Based Oncology Entity Extraction](https://dbc-f4eb4bcb-4ef3.cloud.databricks.com/marketplace/provider/listings/8711812a-c05d-4246-bd90-dabc7f7a0073?o=5522619299734643) Databricks Solution Accelerator Notebook
  - New [Benchmarking John Snow Labs Healthcare NLP Pipelines for Optimal Spark Config at Million-Doc Scale](https://dbc-f4eb4bcb-4ef3.cloud.databricks.com/marketplace/provider/listings/99415605-a24c-4bd8-b4da-892a70b71769?o=5522619299734643) Databricks Solution Accelerator Notebook
- The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Healthcare NLP, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


<div class="h3-box" markdown="1">

#### LLM-Based Structured Clinical Entity Extraction with Constrained Decoding

`MedicalLLMEntityExtractor` is an end-to-end **LLM-powered entity extraction annotator for healthcare and clinical text**, built on top of the `MedicalLLM` models. It leverages **GGUF-format Large Language Models** (via llama.cpp backend) and enforces **strict structured Spark NLP outputs using BNF grammars**, ensuring deterministic and schema-compliant extraction results.

The annotator follows:

* Few-shot prompting for domain adaptation
* Constrained decoding via grammar rules (BNF)
* Post-processing alignment using string matching for accurate character offsets (`begin`, `end`)

This enables reliable extraction of clinically relevant entities such as **DRUG, DOSAGE, ROUTE, FREQUENCY, DURATION**, and other configurable entity types, with precise span alignment back to the source document.

Unlike traditional NER models, `MedicalLLMEntityExtractor` is **model-agnostic within the Medical LLM ecosystem**, meaning it can load and run **any compatible Medical LLM annotator model (GGUF-based)** from the Healthcare NLP model hub. Users can simply select a pretrained model, configure inference parameters, and define extraction schema dynamically.

This makes it suitable for:

* Rapid prototyping of clinical extraction pipelines
* Custom entity schema design without retraining
* Replacement or augmentation of traditional NER pipelines

**Pretrained Model Example**

MedicalLLMEntityExtractor can be used with any compatible MedicalLLM model.

{:.table-model-big}

| Model Name                                            | Description                                                                                                                                               |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`jsl_meds_4b_q16_v5`](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_4b_q16_v5_en.html) | General-purpose medical LLM (4B quantized) optimized for clinical entity extraction, summarization, and structured information retrieval tasks. |


**Example Pipeline**

```python
document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

entity_extractor = MedicalLLMEntityExtractor.pretrained(
    "jsl_meds_4b_q16_v5", "en", "clinical/models"
) \
    .setInputCols(["document"]) \
    .setOutputCol("entities") \
    .setNGpuLayers(99) \
    .setNCtx(4096) \
    .setNPredict(500) \
    .setTemperature(0.1) \
    .setBatchSize(4) \
    .setTopK(40) \
    .setTopP(0.9)
```

**Few-Shot Configuration Example**

```python
medication_few_shot = [
    (
        "Patient prescribed amoxicillin 500mg PO TID for 10 days.",
        '{"extractions": [{"entity": "DRUG", "text": "amoxicillin"}, '
        '{"entity": "DOSAGE", "text": "500mg"}, '
        '{"entity": "ROUTE", "text": "PO"}, '
        '{"entity": "FREQUENCY", "text": "TID"}, '
        '{"entity": "DURATION", "text": "10 days"}]}'
    ),
    (
        "Vancomycin 1.25g IV Q12H x 7 days for MRSA bacteremia.",
        '{"extractions": [{"entity": "DRUG", "text": "Vancomycin"}, '
        '{"entity": "DOSAGE", "text": "1.25g"}, '
        '{"entity": "ROUTE", "text": "IV"}, '
        '{"entity": "FREQUENCY", "text": "Q12H"}, '
        '{"entity": "DURATION", "text": "7 days"}]}'
    ),
    (
        "Metformin 1000mg PO twice daily with meals and lisinopril 10mg PO once daily.",
        '{"extractions": [{"entity": "DRUG", "text": "Metformin"}, '
        '{"entity": "DOSAGE", "text": "1000mg"}, '
        '{"entity": "ROUTE", "text": "PO"}, '
        '{"entity": "FREQUENCY", "text": "twice daily"}, '
        '{"entity": "DRUG", "text": "lisinopril"}, '
        '{"entity": "DOSAGE", "text": "10mg"}, '
        '{"entity": "ROUTE", "text": "PO"}, '
        '{"entity": "FREQUENCY", "text": "once daily"}]}'
    ),
]

entity_extractor.setFewShotExamples(medication_few_shot)
```

**Entity Schema Definition**

```python
entity_extractor.setEntityTypes([
  "DRUG::The exact medication or drug name as written in the text. Examples: aspirin, metformin, vancomycin.",
  "DOSAGE::The exact dose amount including units. Examples: 500mg, 1.25g, 40mg, 0.1 mcg/kg/min.",
  "ROUTE::The administration route. Examples: PO, IV, SQ, IM, inhaled, sublingual, topical.",
  "FREQUENCY::The dosing schedule or timing. Examples: BID, TID, Q12H, daily, PRN, twice daily.",
  "DURATION::The treatment duration. Examples: 7 days, 6 weeks, 3 months, until follow-up.",
]) 
```

**Result**:

```text
+-----+-------------+---------+
|begin|chunk        |label    |
+-----+-------------+---------+
|26   |Metformin    |DRUG     |
|36   |1000mg       |DOSAGE   |
|43   |PO           |ROUTE    |
|46   |BID          |FREQUENCY|
|65   |Lisinopril   |DRUG     |
|76   |10mg         |DOSAGE   |
|81   |PO           |ROUTE    |
|84   |daily        |FREQUENCY|
|94   |Atorvastatin |DRUG     |
|107  |40mg         |DOSAGE   |
|112  |PO           |ROUTE    |
|115  |at bedtime   |FREQUENCY|
|130  |Aspirin      |DRUG     |
|138  |81mg         |DOSAGE   |
|143  |PO           |ROUTE    |
|146  |daily        |FREQUENCY|
|156  |Empagliflozin|DRUG     |
|170  |10mg         |DOSAGE   |
+-----+-------------+---------+
```

</div><div class="h3-box" markdown="1">


#### Table-Aware, Free-Text Extended CDA De-Identification with Improved PHI Accuracy in CDA Tables
`CDADeIdentification` is a **CDA (Clinical Document Architecture) de-identification transformer for Healthcare NLP pipelines**, designed to anonymize both **structured XML nodes and embedded free-text narratives such as `section.text`** using Healthcare NLP models and pretrained de-identification pipelines.

The new generation of `CDADeIdentification` introduces **a context-aware table processing mechanism with header-aware semantics**, where structured elements such as HTML tables and definition lists are no longer treated as isolated text nodes. Instead, cell values are enriched with their corresponding headers (e.g., `"header : value"`) before being sent to the de-identification pipeline, enabling significantly better entity recognition in compact clinical fields.

This approach substantially improves **PHI detection accuracy in structured clinical tables**, particularly in cases where traditional de-identification methods fail due to the absence of contextual signals in short text cells (e.g., lab values, patient attributes, billing records).

By combining:

* header-aware table parsing
* structured XML path de-identification
* free-text NLP pipeline integration

`CDADeIdentification` achieves **higher recall and more consistent PHI masking across mixed structured and unstructured CDA documents**, while preserving the original clinical document structure and readability.


**New Pretrained Models**

{:.table-model-big}

| Model Name                              | Description                                                                                                                                                                                 |
| --------------------------------------- |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cda_deidentification_patient`          | De-identifies patient-related CDA XML paths including identifiers, demographics, and structured patient metadata while preserving CDA schema integrity.                                     |
| `cda_deidentification_extend_free_text` | Extends de-identification to CDA free-text sections (e.g., `section.text`, narrative blocks) by applying a full Healthcare NLP de-identification pipeline to unstructured clinical content. |



**Table-Aware De-Identification (Major Enhancement)**

**Table Handling Control**

With `setTableHandling(True)` (default behavior), CDA tables are processed using **semantic header-value pairing** instead of independent node processing.

- How it works:

Instead of treating each `<td>` independently, the system constructs:

```
"<header> : <cell value>"
```

and sends it through the Healthcare NLP de-identification pipeline.

**Free-Text Exclusion Control**

| Parameter                      | Description                                                                                                                                                                             |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `setExcludeFreeTextTags(list)` | Defines XML tags whose subtree is fully excluded from NLP processing (no tokenization or inference). Useful for preserving footnotes, superscripts, or custom clinical metadata blocks. |

**Backward Compatibility**
* Disable table-aware processing:
```python
.setTableHandling(False)
```

**Pipeline Integration Example**

```python
deid_pipeline = PretrainedPipeline(
    "clinical_deidentification_docwise_benchmark_medium_v2",
    "en",
    "clinical/models"
)

cda_deidentification = (
    CdaDeIdentification
    .pretrained("cda_deidentification_extend_free_text", "en", "clinical/models")
    .setSeed(42)
    .setDays(2)
    .setTableHandling(True)
    .setPipeline(spark, deid_pipeline, "masked")
)
```

**Example Input**

```xml
<?xml version="1.0" encoding="UTF-8"?><ClinicalDocument xmlns="urn:hl7-org:v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:hl7-org:v3 CDA.xsd">
    <!-- ===================== BODY ===================== -->
    <component>
        <structuredBody>
            <component>
                <section>
                    <code code="10164-2" codeSystem="2.16.840.1.113883.6.1" displayName="History of Present Illness"/>
                    <title>History of Present Illness</title>
                    <text>
                      <table>
                        <thead>
                          <tr>
                            <th>Patient Name</th>
                            <th>Patient ID</th>
                            <th>Primary Diagnosis</th>
                            <th>Date of Birth</th>
                            <th>Contact Number</th>
                            <th>Home Address</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <td>Michael Thompson</td>
                            <td>458921</td>
                            <td>Type 2 Diabetes Mellitus</td>
                            <td>08/14/1975</td>
                            <td>+1 212-555-0198</td>
                            <td>45 Park Avenue, New York, NY 10016</td>
                          </tr>
                          <tr>
                            <td>Emily Rodriguez</td>
                            <td>771204</td>
                            <td>Hypertension</td>
                            <td>11/22/1980</td>
                            <td>+1 415-555-0133</td>
                            <td>78 Sunset Blvd, Los Angeles, CA 90028</td>
                          </tr>
                          <tr>
                            <td>David Chen</td>
                            <td>993817</td>
                            <td>Chronic Kidney Disease</td>
                            <td>03/09/1972</td>
                            <td>+1 646-555-0177</td>
                            <td>1200 Market Street, San Francisco, CA 94102</td>
                          </tr>
                          <tr>
                            <td>Sophia Patel</td>
                            <td>224581</td>
                            <td>Asthma</td>
                            <td>07/30/1990</td>
                            <td>+1 770-900-0455</td>
                            <td>22 Baker Street, London NW1 6XE</td>
                          </tr>
                          <tr>
                            <td>James Wilson</td>
                            <td>665432</td>
                            <td>Coronary Artery Disease</td>
                            <td>01/18/1965</td>
                            <td>+61 412 345 678</td>
                            <td>89 George Street, Sydney NSW 2000</td>
                          </tr>
                        </tbody>
                      </table>
                    </text>
                </section>
            </component>
        </structuredBody>
    </component>
</ClinicalDocument>"""
```

**Result**:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?><ClinicalDocument xmlns="urn:hl7-org:v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:hl7-org:v3 CDA.xsd">
    <!-- ===================== BODY ===================== -->
    <component>
        <structuredBody>
            <component>
                <section>
                    <code code="10164-2" codeSystem="2.16.840.1.113883.6.1" displayName="History of Present Illness"/>
                    <title>History of Present Illness</title>
                    <text>
                      <table>
                        <thead>
                          <tr>
                            <th>Patient Name</th>
                            <th>Patient ID</th>
                            <th>Primary Diagnosis</th>
                            <th>Date of Birth</th>
                            <th>Contact Number</th>
                            <th>Home Address</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <td>PATIENT</td>
                            <td>IDNUM</td>
                            <td>Type 2 Diabetes Mellitus</td>
                            <td>DATE</td>
                            <td>PHONE</td>
                            <td>STREET, STATE, STATE ZIP</td>
                          </tr>
                          <tr>
                            <td>PATIENT</td>
                            <td>IDNUM</td>
                            <td>Hypertension</td>
                            <td>DATE</td>
                            <td>PHONE</td>
                            <td>STREET, CITY, STATE ZIP</td>
                          </tr>
                          <tr>
                            <td>PATIENT</td>
                            <td>IDNUM</td>
                            <td>Chronic Kidney Disease</td>
                            <td>DATE</td>
                            <td>PHONE</td>
                            <td>STREET, CITY, STATE ZIP</td>
                          </tr>
                          <tr>
                            <td>PATIENT</td>
                            <td>IDNUM</td>
                            <td>Asthma</td>
                            <td>DATE</td>
                            <td>PHONE</td>
                            <td>STREET, CITY ZIP</td>
                          </tr>
                          <tr>
                            <td>PATIENT</td>
                            <td>IDNUM</td>
                            <td>Coronary Artery Disease</td>
                            <td>DATE</td>
                            <td>PHONE</td>
                            <td>STREET, CITY STATE ZIP</td>
                          </tr>
                        </tbody>
                      </table>
                    </text>
                </section>
            </component>
        </structuredBody>
    </component>
</ClinicalDocument>
```

</div><div class="h3-box" markdown="1">

#### Pretrained Zero-Shot Multi-Task Named Entity Recognition (NER) Speed Comparison on GPU vs CPU Benchmark

We benchmarked the **PretrainedZeroShotMultiTask** architecture using the **zeroshot_multitask_base** model on a dataset of ~500 tokens per row.

**Hardware setup:**

- **CPU**: 8 cores, 52 GB System RAM
- **GPU**: NVIDIA T4, 24 GB VRAM

The workload was tested on two dataset sizes (1k rows and 100 rows), each with 48 repartitions.

**Spark NLP Pipeline**

```
pipeline = Pipeline(
    stages = [
        document_assembler,
        sentence_detector,
        pretrained_zeroshot_multitask
])
```

**Summary**

- The **GPU significantly reduced wall time** compared to CPU.
- On the 1k dataset, GPU reduced total runtime from **8h 45m → 42m** (~12× faster).
- On the 100-row dataset, GPU reduced runtime from **51m → 4m** (~12× faster).
- GPU acceleration scales consistently across dataset sizes.


**Benchmark Results**

| Hardware               | Dataset Size | Repartition | CPU Time (user+sys) | Wall Time   |
|------------------------|--------------|-------------|---------------------|--------------|
| CPU (8 core, 52GB RAM) | 1k rows (~500 tokens)  | 48 | 5.93 s  | 8h 45m 46s |
| CPU (8 core, 52GB RAM) | 100 rows (~500 tokens) | 48 | 625 ms  | 51m 43s    |
| GPU (NVIDIA T4, 24GB)  | 1k rows (~500 tokens)  | 48 | 400 ms  | 42m 35s    |
| GPU (NVIDIA T4, 24GB)  | 100 rows (~500 tokens) | 48 | 52 ms   | 4m 12s     |


</div><div class="h3-box" markdown="1">

#### StructuredDeIdentification – Timestamp Support & Time Shift Enhancement

**Overview**

The `StructuredDeIdentification` module has been enhanced to support **timestamp-based de-identification for structured medical tables**, enabling more realistic temporal obfuscation in clinical datasets.

This improvement allows clients to safely shift temporal information in structured healthcare data while preserving schema consistency and analytical usability.

**Timestamp Entity Support**

`StructuredDeIdentification` now supports the following timestamp entity types:

* `TIMESTAMP`
* `TIMESTAMP_WITH_TIMEZONE`

This enables time-based obfuscation for structured medical records such as admissions, lab events, prescriptions, and encounter logs.

**Time Shifting Capability**

Timestamp values can now be shifted forward or backward in time using a configurable offset.

This is particularly useful for:

* De-identifying medical timelines
* Preserving temporal relationships without exposing real dates
* Enabling synthetic cohort generation with realistic time progression


**New Parameters**

**timeStampFormats: list[str]**

Optional list of timestamp patterns used to parse string-based `TIMESTAMP` or `TIMESTAMP_WITH_TIMEZONE` entities.

* If provided, formats are evaluated sequentially in order
* The first matching format is used for both parsing and formatting
* If empty, a predefined set of common timestamp formats is applied automatically

**Example formats:**

* `"yyyy-MM-dd HH:mm:ss"`
* `"yyyy-MM-dd'T'HH:mm:ss"`
* `"yyyy-MM-dd HH:mm:ss.SSS"`

**seconds: int**

Defines the number of seconds used to shift timestamp entities during obfuscation. Seconds-based offset provides the finest granularity while supporting all larger units via conversion.

* Positive values shift timestamps forward in time
* Negative values shift timestamps backward in time
* Default value: `0` (no shift applied)

**Medical Use Case Enhancement**

This feature significantly improves support for **clinical structured tables**, where timestamp fields such as:

* Admission time
* Discharge time
* Medication administration time
* Lab sampling time

must be preserved structurally while being anonymized.

**Example Usage**

```python
from sparknlp_jsl.structured_deidentification import StructuredDeIdentification

data = [
    (1001, "2026-06-01 08:15:22"),
    (1002, "2026-06-01 14:42:10"),
    (1003, "N/A"),
    (1004, "2026-06-02 18:27:31"),
    (1005, "2026-06-03 11:58:04"),
]

df = spark.createDataFrame(data, ["patient_id", "admission_timestamp"])

obfuscator = StructuredDeIdentification(
    spark=spark,
    columns={"admission_timestamp": "TIMESTAMP"},
    obfuscateRefSource="faker",
    timeStampFormats=["yyyy-MM-dd HH:mm:ss"],
    seconds=43200
)

result = obfuscator.obfuscateColumns(
    df,
    outputAsArray=False,
    overwrite=False,
    suffix="_deid"
)

result.show(truncate=False)
```

**Result**:

```text
+----------+-------------------+------------------------+
|patient_id|admission_timestamp|admission_timestamp_deid|
+----------+-------------------+------------------------+
|1001      |2026-06-01 08:15:22|2026-06-01 20:15:22     |
|1002      |2026-06-01 14:42:10|2026-06-02 02:42:10     |
|1003      |N/A                |N/A                     |
|1004      |2026-06-02 18:27:31|2026-06-03 06:27:31     |
|1005      |2026-06-03 11:58:04|2026-06-03 23:58:04     |
+----------+-------------------+------------------------+
```

</div><div class="h3-box" markdown="1">

#### Updated 7 UMLS Entity Resolver Models and 19 ChunkMapper Models to the UMLS 2026AA Metathesaurus and Introduced 17 New ChunkMapper Models Covering 8 Additional Medical Coding Systems

We are delivering a full refresh of our UMLS model suite, now trained on the **UMLS 2026AA Metathesaurus**. This includes updated versions of all 7 UMLS Entity Resolver models and a significantly expanded ChunkMapper suite — 19 updated models retrained on 2026AA data and 17 new models covering 8 additional medical coding systems.

**Updated UMLS 2026AA Entity Resolver Models**

These models map clinical entities to **UMLS Concept Unique Identifiers (CUI)** using `sbiobert_base_cased_mli_onnx` sentence embeddings (ONNX, CPU-compatible), retrained on the UMLS 2026AA Metathesaurus. The `biolordresolve_umls_general_concepts` model uses `mpnet_embeddings_biolord_2023_c` embeddings.

{:.table-model-big}
| Model Name | Description |
|---|---|
| `sbiobertresolve_umls_findings` | Maps clinical finding entities to their corresponding UMLS CUI codes |
| `sbiobertresolve_umls_clinical_drugs` | Maps drug entities to UMLS CUI codes |
| `sbiobertresolve_umls_disease_syndrome` | Maps clinical entities ("Disease or Syndrome") to UMLS CUI codes |
| `sbiobertresolve_umls_drug_substance` | Maps drug and substance entities to UMLS CUI codes |
| `sbiobertresolve_umls_general_concepts` | Maps clinical entities and concepts to the following 4 UMLS CUI code categories: `Disease`, `Symptom`, `Medication` and `Procedure` |
| `sbiobertresolve_umls_major_concepts` | Maps clinical entities and concepts to 4 major categories of UMLS CUI codes: `Clinical Findings`, `Medical Devices`, `Anatomical Structures`, `Injuries & Poisoning` terms |
| `biolordresolve_umls_general_concepts` | Maps clinical entities to 4 UMLS CUI code categories using `mpnet_embeddings_biolord_2023_c` embeddings: `Disease`, `Symptom`, `Medication`, and `Procedure` |


**Updated UMLS 2026AA ChunkMapper Models (19 Models)**

These models are retrained on UMLS 2026AA data. The bidirectional code mappers use a `DocumentAssembler → Doc2Chunk → ChunkMapper` pipeline. The NER-based mappers apply a full NER pipeline before mapping.

> ⚠️ CPT mapper models are available only to users with a valid AMA license. Contact support@johnsnowlabs.com for access.

{:.table-model-big}
| UMLS → Code | Code → UMLS | Coding System |
|---|---|---|
| `umls_rxnorm_mapper` | `rxnorm_umls_mapper` | RxNorm |
| `umls_snomed_mapper` | `snomed_umls_mapper` | SNOMED CT (US Edition) |
| `umls_loinc_mapper` | `loinc_umls_mapper` | LOINC |
| `umls_mesh_mapper` | `mesh_umls_mapper` | MeSH |
| `umls_icd10cm_mapper` | `icd10cm_umls_mapper` | ICD-10-CM |
| `umls_hpo_mapper` | `hpo_umls_mapper` | Human Phenotype Ontology |
| `umls_cpt_mapper` ⚠️ | `cpt_umls_mapper` ⚠️ | CPT |

{:.table-model-big}
| Model Name | NER Model | Description |
|---|---|---|
| `umls_clinical_findings_mapper` | `ner_clinical_large` | Maps clinical findings (PROBLEM, TEST, TREATMENT) to UMLS CUI codes |
| `umls_disease_syndrome_mapper` | `ner_clinical_large` | Maps disease and syndrome entities to UMLS CUI codes |
| `umls_drug_substance_mapper` | `ner_posology_greedy` | Maps drug substance entities to UMLS CUI codes |
| `umls_clinical_drugs_mapper` | `ner_posology_greedy` | Maps clinical drug entities to UMLS CUI codes |
| `umls_major_concepts_mapper` | `ner_medmentions_coarse` | Maps body parts, devices, injuries, and findings to UMLS CUI codes |


**New UMLS 2026AA ChunkMapper Models (17 Models)**

These models are introduced for the first time, covering 8 additional medical coding systems and one new NER-based domain.

> ⚠️ MedDRA mapper models are available only to users with a valid license. Contact support@johnsnowlabs.com for access.

{:.table-model-big}
| UMLS → Code | Code → UMLS | Coding System |
|---|---|---|
| `umls_icd10pcs_mapper` | `icd10pcs_umls_mapper` | ICD-10-PCS |
| `umls_nci_mapper` | `nci_umls_mapper` | NCI Thesaurus |
| `umls_icd9cm_mapper` | `icd9cm_umls_mapper` | ICD-9-CM |
| `umls_hgnc_mapper` | `hgnc_umls_mapper` | HGNC Gene Nomenclature |
| `umls_atc_mapper` | `atc_umls_mapper` | WHO ATC |
| `umls_hcpcs_mapper` | `hcpcs_umls_mapper` | HCPCS |
| `umls_snomedvet_mapper` | `snomedvet_umls_mapper` | SNOMED CT Veterinary |
| `umls_meddra_mapper` ⚠️ | `meddra_umls_mapper` ⚠️ | MedDRA |

{:.table-model-big}
| Model Name | NER Model | Description |
|---|---|---|
| `umls_general_concepts_mapper` | `ner_clinical` | Maps general clinical concepts (Disease, Symptom, Device, Procedure) to UMLS CUI codes |

*Example* (entity resolution — `sbiobertresolve_umls_disease_syndrome`):

```python
documentAssembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner_jsl")

ner_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner_jsl"]) \
    .setOutputCol("ner_chunk") \
    .setWhiteList(["Disease_Syndrome_Disorder", "Symptom"])

chunk2doc = Chunk2Doc() \
    .setInputCols("ner_chunk") \
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models") \
    .setInputCols(["ner_chunk_doc"]) \
    .setOutputCol("sbert_embeddings") \
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_disease_syndrome", "en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("resolution") \
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([[
    "The patient has a history of systemic lupus erythematosus, multiple sclerosis, and fibromyalgia. "
    "She was admitted with sepsis secondary to bacterial pneumonia and developed acute respiratory distress syndrome. "
    "Imaging showed findings consistent with pulmonary sarcoidosis and Crohn's disease."
]]).toDF("text")

result = pipeline.fit(data).transform(data)
```

*Result*
{:.table-model-big}
| ner_chunk | entity | umls_code | resolution | all_k_results | all_k_distances | all_k_cosine_distances | all_k_resolutions |
|---|---|---|---|---|---|---|---|
| systemic lupus erythematosus | Disease_Syndrome_Disorder | C0024141 | systemic lupus erythematosus | C0024141:::C0409974:::C0024137:::C1274838:::C6022675:::C0409977:::C0409976:::C07... | 0.0067:::3.4325:::4.0055:::4.4309:::4.4907:::4.5642:::4.5922:::4.6192:::4.6675::... | 0.0000:::0.0184:::0.0251:::0.0308:::0.0317:::0.0322:::0.0328:::0.0336:::0.0334::... | systemic lupus erythematosus:::lupus erythematosus:::cutaneous lupus erythematos... |
| sclerosis | Disease_Syndrome_Disorder | C0036412 | sclera disease | C0036412:::C0263009:::C0036421:::C0007795:::C0237854:::C0004712:::C0036416:::C00... | 6.4563:::6.5690:::6.7129:::6.8109:::6.8550:::6.9680:::7.2263:::7.5483:::7.5862::... | 0.0689:::0.0695:::0.0752:::0.0738:::0.0762:::0.0792:::0.0860:::0.0915:::0.0957::... | sclera disease:::sclerosis skin:::system; sclerosis:::diffuse sclerosis:::sclero... |
| fibromyalgia | Disease_Syndrome_Disorder | C0016053 | fibromyalgia | C0016053:::C0751153:::C0751152:::C0015674:::C4703320 | 0.0070:::3.9297:::4.7923:::6.1085:::7.4228 | 0.0000:::0.0242:::0.0364:::0.0572:::0.0843 | fibromyalgia:::secondary fibromyalgia:::fibromyalgia primary:::chronic fatigue-f... |
| sepsis | Disease_Syndrome_Disorder | C0036690 | sepsis | C0036690:::C3164780:::C0242966:::C0152965:::C1141927:::C0684256:::C1141926:::C17... | 0.0084:::4.0589:::4.4404:::4.9625:::5.2109:::5.7252:::5.8590:::5.9812:::5.9983::... | 0.0000:::0.0260:::0.0316:::0.0396:::0.0428:::0.0522:::0.0539:::0.0546:::0.0564::... | sepsis:::clinical sepsis:::syndrome sepsis:::staph sepsis:::wound sepsis:::sepsi... |
| bacterial pneumonia | Disease_Syndrome_Disorder | C0004626 | bacterial pneumonia | C0004626:::C0339952:::C0276523:::C0339951:::C1443238:::C0264386:::C0155860:::C05... | 0.0078:::4.8777:::6.3237:::6.3566:::6.6580:::6.8243:::6.8403:::6.8537:::6.8800::... | 0.0000:::0.0377:::0.0640:::0.0656:::0.0706:::0.0734:::0.0762:::0.0770:::0.0777::... | bacterial pneumonia:::bacterial pneumonia secondary:::aids with bacterial pneumo... |
| respiratory distress syndrome | Disease_Syndrome_Disorder | C0035220 | respiratory distress syndrome | C0035220:::C0852283:::C0035222:::C0158940:::C0877339:::C5420230:::C3810183:::C54... | 0.0062:::4.0045:::4.1765:::5.1745:::6.0413:::6.2379:::6.2459:::6.4251:::6.4578::... | 0.0000:::0.0239:::0.0259:::0.0397:::0.0535:::0.0576:::0.0574:::0.0608:::0.0607::... | respiratory distress syndrome:::respiratory distress syndromes:::acquired respir... |
| pulmonary sarcoidosis | Disease_Syndrome_Disorder | C0036205 | pulmonary sarcoidosis | C0036205:::C0036202:::C0406396:::C1302844:::C0396073:::C0036206:::C0340201:::C13... | 0.0074:::4.8495:::5.0965:::5.2098:::5.3056:::5.3212:::5.4128:::5.4719:::5.5281::... | 0.0000:::0.0373:::0.0412:::0.0433:::0.0452:::0.0452:::0.0470:::0.0479:::0.0488::... | pulmonary sarcoidosis:::sarcoidosis:::nodular sarcoidosis:::skin sarcoidosis:::l... |
| Crohn's disease | Disease_Syndrome_Disorder | C0010346 | crohn's disease | C0010346:::C0399497:::C0156147:::C1301260:::C0941042:::C1301261:::C5686651:::C60... | 0.0071:::4.6627:::5.2420:::5.2609:::5.6188:::5.6324:::5.6705:::5.6709:::6.0026 | 0.0000:::0.0340:::0.0424:::0.0428:::0.0487:::0.0486:::0.0508:::0.0501:::0.0560 | crohn's disease:::orofacial crohn's disease:::crohn's colitis:::gastrointestinal... |


*Example* (code-level mapping — `umls_rxnorm_mapper`):

```python
document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("doc")

doc2chunk = Doc2Chunk() \
    .setInputCols(["doc"]) \
    .setOutputCol("ner_chunk")

mapper = ChunkMapperModel.pretrained("umls_rxnorm_mapper", "en", "clinical/models") \
    .setInputCols(["ner_chunk"]) \
    .setOutputCol("mappings")

pipeline = Pipeline(stages=[document_assembler, doc2chunk, mapper])

data = spark.createDataFrame([["C1126248"], ["C0978482"], ["C0691677"]]).toDF("text")

result = pipeline.fit(data).transform(data)
```

*Result*
{:.table-model-big}
| umls_code | rxnorm_code |
|---|---|
| C1126248 | 330565 |
| C0978482 | 861004 |
| C0691677 | 198776 |

*Example* (NER-based mapping — `umls_general_concepts_mapper`):

```python
document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentence_detector = SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("clinical_ner")

ner_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "clinical_ner"]) \
    .setOutputCol("ner_chunk")

mapper = ChunkMapperModel.pretrained("umls_general_concepts_mapper", "en", "clinical/models") \
    .setInputCols(["ner_chunk"]) \
    .setOutputCol("mappings") \
    .setRels(["umls_code"]) \
    .setLowerCase(True)

pipeline = Pipeline(stages=[
    document_assembler, sentence_detector, tokenizer,
    word_embeddings, ner_model, ner_converter, mapper
])

data = spark.createDataFrame([[
    "The patient presents with dyspnea and fever due to pneumonia. "
    "Treatment includes bronchoscopy, catheter placement, and chemotherapy."
]]).toDF("text")

result = pipeline.fit(data).transform(data)
```

*Result*
{:.table-model-big}
| ner_chunk | umls_code |
|---|---|
| dyspnea | C0013404 |
| fever | C0015967 |
| pneumonia | C0032285 |
| bronchoscopy | C5979970 |
| catheter placement | C0883301 |
| chemotherapy | C0013216 |

</div><div class="h3-box" markdown="1">

#### New Blog Posts & Technical Deep Dives

- [John Snow Labs detects 54% more clinical PHI than OpenAI’s Privacy Filter, at 5.8× the speed on CPU](https://medium.com/john-snow-labs/john-snow-labs-detects-54-more-clinical-phi-than-openais-privacy-filter-at-5-8-the-speed-on-cpu-d460df795eb1) : This blog post benchmarks the OpenAI Privacy Filter against a healthcare-specific de-identification pipeline from John Snow Labs on nearly 382K tokens of real clinical text. It explains how the John Snow Labs pipeline achieved substantially higher PHI detection accuracy (0.95 F1 vs. 0.55) while also running 5.8× faster on CPU, highlighting the importance of domain-specific clinical NLP over general-purpose PII detection. The article also covers strict label-mapping methodology, benchmark design, CPU-optimized deployment pipelines, and practical challenges in healthcare de-identification such as identifying hospital names, medical IDs, and clinical abbreviations in real-world notes.


</div><div class="h3-box" markdown="1">


#### Updated Notebooks And Demonstrations For Making Healthcare NLP Easier To Navigate And Understand

- New [MedicalLLMEntityExtractor](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.2.MedicalLLMEntityExtractor.ipynb) Notebook
  
  This notebook introduces JSL’s LLM-based clinical NER annotator with grammar-enforced JSON, runtime-defined entity types, and CHUNK outputs with character offsets. Five end-to-end examples: default clinical NER, medication fields, PHI de-identification, oncology few-shot, and custom ADR prompts. Requires Spark NLP Healthcare license and supported JSL MedS/MedM GGUF models.

- New [Benchmarking John Snow Labs Healthcare NLP Pipelines for Optimal Spark Config at Million-Doc Scale](https://dbc-f4eb4bcb-4ef3.cloud.databricks.com/marketplace/provider/listings/99415605-a24c-4bd8-b4da-892a70b71769?o=5522619299734643) Databricks Solution Accelerator Notebook
  - This accelerator benchmarks five pretrained John Snow Labs Healthcare NLP pipelines to identify the most efficient Apache Spark configurations for large-scale document processing.
  - The notebook performs million-document throughput testing across multiple Healthcare NLP pipelines, evaluating how different Spark settings impact performance, scalability, and resource utilization.
  - By comparing execution times, parallelism strategies, and cluster tuning parameters, this benchmark helps users determine the optimal Spark configuration for maximum NLP throughput in enterprise-scale healthcare and clinical text processing workloads.
  - Utilizing a Medallion architecture (Bronze, Silver, Gold layers) and crash-safe checkpoints, the accelerator demonstrates how to efficiently fine-tune key Spark parameters across various complex clinical NLP tasks. Its main benefit is enabling data teams to significantly reduce processing times and compute costs when deploying healthcare NLP models on Databricks clusters.
  - Use cases
    - Optimizing Apache Spark configurations (shuffle_partitions, default_parallelism, and repartition_count) for high-throughput clinical NLP processing.
    - Benchmarking the performance, execution time, and stability of John Snow Labs Healthcare NLP pipelines at varying data scales (10 to 1,000,000 rows).
    - Fast and balanced Protected Health Information (PHI) de-identification for massive volumes of medical documents.
    - Granular clinical Named Entity Recognition (NER) and specialized oncology entity extraction from clinical text.
    - High-volume, large-scale ICD-10-CM code resolution from raw medical transcriptions.

- New [LLM-Based Oncology Entity Extraction](https://dbc-f4eb4bcb-4ef3.cloud.databricks.com/marketplace/provider/listings/8711812a-c05d-4246-bd90-dabc7f7a0073?o=5522619299734643) Databricks Solution Accelerator Notebook
  - This solution accelerator demonstrates an end-to-end LLM-based oncology entity extraction pipeline built on the Databricks Lakehouse using Spark NLP Healthcare by John Snow Labs.
  - It ingests raw clinical oncology notes, extracts 43 structured entity types using a locally running LLM (qwen3_4b), resolves extracted entities to ICD-O codes via biomedical sentence embeddings, and publishes curated Delta tables following the Medallion architecture (Bronze → Silver → Gold).
  - All inference runs on-cluster with no external API calls, ensuring full data privacy and HIPAA-aligned processing.
  - Use cases
    - Automated cancer registry abstraction from unstructured clinical notes
    - Structured oncology entity extraction (diagnoses, treatments, biomarkers, staging, tumor findings) for downstream analytics
    - ICD-O code assignment to free-text oncology concepts using semantic similarity
    - PHI-safe clinical NLP pipeline with optional de-identification before LLM processing
    - Foundation for real-world evidence (RWE) generation from electronic health records

</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `clinical_deidentification_docwise_benchmark_multitask`
+ `clinical_deidentification_subentity_optimized_scala3`
+ `zeroshot_multitask_oncology`
+ `zeroshot_multitask_oncology_generic`
+ `cda_deidentification_extend_free_text`
+ `cda_deidentification_patient`
+ `sbiobertresolve_umls_findings`
+ `sbiobertresolve_umls_clinical_drugs`
+ `sbiobertresolve_umls_disease_syndrome`
+ `sbiobertresolve_umls_drug_substance`
+ `sbiobertresolve_umls_general_concepts`
+ `sbiobertresolve_umls_major_concepts`
+ `biolordresolve_umls_general_concepts`
+ `umls_rxnorm_mapper`
+ `rxnorm_umls_mapper`
+ `umls_snomed_mapper`
+ `snomed_umls_mapper`
+ `umls_snomedvet_mapper`
+ `snomedvet_umls_mapper`
+ `umls_loinc_mapper`
+ `loinc_umls_mapper`
+ `umls_mesh_mapper`
+ `mesh_umls_mapper`
+ `umls_icd10cm_mapper`
+ `icd10cm_umls_mapper`
+ `umls_icd10pcs_mapper`
+ `icd10pcs_umls_mapper`
+ `umls_icd9cm_mapper`
+ `icd9cm_umls_mapper`
+ `umls_nci_mapper`
+ `nci_umls_mapper`
+ `umls_hpo_mapper`
+ `hpo_umls_mapper`
+ `umls_hgnc_mapper`
+ `hgnc_umls_mapper`
+ `umls_atc_mapper`
+ `atc_umls_mapper`
+ `umls_hcpcs_mapper`
+ `hcpcs_umls_mapper`
+ `umls_cpt_mapper`
+ `cpt_umls_mapper`
+ `umls_meddra_mapper`
+ `meddra_umls_mapper`
+ `umls_clinical_findings_mapper`
+ `umls_disease_syndrome_mapper`
+ `umls_drug_substance_mapper`
+ `umls_clinical_drugs_mapper`
+ `umls_major_concepts_mapper`
+ `umls_general_concepts_mapper`

</div><div class="h3-box" markdown="1">


## Previous versions

</div>
{%- include docs-healthcare-pagination.html -%}
