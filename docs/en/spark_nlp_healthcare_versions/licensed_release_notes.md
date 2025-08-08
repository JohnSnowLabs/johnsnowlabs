---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/licensed_release_notes
key: docs-licensed-release-notes
modify_date: 2025-07-22
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 6.0.4

#### Highlights

We are delighted to announce remarkable enhancements and updates in our latest release of Healthcare NLP. **This release introduces a series of performance improvements for sentence embeddings, zero-shot NER, and assertion classification tasks in Healthcare NLP via ONNX-optimized models and native batching support across multiple components.**

+ ONNX model optimizations and batch inference improvements (GPU & CPU)
+ Batch inference and OpenVINO support for `PretrainedZeroShotNER`, our most capable and preferred medical NER framework
+ New MedS-NER LLM for structured medical entity extraction via 3B size small LLMs
+ Advanced clinical one-liner pretrained pipelines for PHI detection and extraction
+ Clinical code resolution via one-liner pretrained pipelines for medical terminology mapping
+ Clinical document explanation, one-liner pretrained pipelines for comprehensive clinical entity analysis
+ New NER model and pipeline about vaccinations and infectious diseases
+ New blog posts on various topics
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Healthcare NLP
    - Improved memory management for ONNX in ML-based transformers
    - Fixed an issue in `TextMatcherInternal` where `null` values could appear in the output due to race conditions during parallel processing.
    - Resolved a bug in `PretrainedZeroShotNER` that caused an `emptyIterator` exception in certain edge cases when processing empty or malformed input.
    - Enhanced geo-consistency algorithm in `Deidentification` to reliably process previously skipped geographic entities.
+ Updated notebooks and demonstrations for making Healthcare NLP easier to navigate and understand
    - New [Deidentification NER Profiling Pipeline](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/04.12.Deidentification_NER_Profiling_Pipeline.ipynb) Notebook
    - New [Annotation Converter](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/50.Annotation_Converter.ipynb) Notebook 
    - Updated [Pretrained NER Profiling Pipelines](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.1.Pretrained_NER_Profiling_Pipelines.ipynb) Notebook
    - Updated [Clinical Deidentification Improvement](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/04.4.Clinical_Deidentification_Improvement.ipynb) Notebook
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Healthcare NLP, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


</div><div class="h3-box" markdown="1">

#### ONNX Model Optimizations and Batch Inference Improvements (GPU & CPU)

This release delivers powerful runtime improvements for `BertSentenceEmbeddings` and `BertForAssertionClassification` in JohnSnowLabs. With the introduction of ONNX-optimized models and native batch inference, users can achieve significant speedups on both CPU and GPU, all without sacrificing model accuracy or requiring changes to existing pipelines.

- Key Highlights:
    - ONNX-Accelerated Embeddings for BertSentenceEmbeddings and BertSentenceChunkEmbeddings, yielding up to 109× faster (100+ times faster) inference on GPU.
    - End-to-End Pipeline Speedup: Using ONNX models in SentenceEntityResolver pipelines improves performance up to 5.5×, with minimal changes.
    - Optimized Assertion Classification: ONNX models for BertForAssertionClassification offer up to 28× faster inference on GPU, with native batching support for scalable performance.

All ONNX models maintain original output quality and are drop-in compatible with existing workflows.
These enhancements make clinical NLP tasks in production environments faster, leaner, and more deployable across diverse hardware platforms.

- Test Environment:
    + Instance Type:
        - CPU: Colab V6e-1 TPU, 173.0 GB RAM, 44 CPUs
        - GPU: Colab A100, 83.5 GB RAM, 40.0 GB GPU RAM, 12 Cores
    + Datasets:
        - 1000 rows MTSamples dataset (~500 tokens per row)
        - 7500 rows Assertion test dataset


- **ONNX Optimization for `BertSentenceEmbeddings` and `BertSentenceChunkEmbeddings`**: We benchmarked both `BertSentenceEmbeddings` (for full-text sentence-level embeddings) and `BertSentenceChunkEmbeddings` (for NER-extracted chunks) using their ONNX-optimized versions.

    + CPU Performance:
      
        | Component       | TensorFlow | ONNX        | Speedup |
        |-----------------|------------|-------------|---------|
        | `BertSentenceEmbeddings` | 6 min 18 s | 2 min 57 s | ~ 2.1× |

    + ⚡GPU Performance:
      
        | Component       | TensorFlow | ONNX        | Speedup     |
        |-----------------|------------|-------------|-------------|
        | `BertSentenceEmbeddings` | 20 min | 11 s   | ~ 109×      |

    **Notes:**

        - ONNX models significantly accelerate inference, particularly on GPUs.
        - Embedding quality, dimensionality, and behavior remain unchanged.
        - Suitable for both full-text and chunk-level sentence embeddings.


- **`BertSentenceEmbeddings` in Entity Resolver Pipeline**: We also evaluated `BertSentenceEmbeddings` inside a complete `SentenceEntityResolver` pipeline on a 1K clinical dataset using a GPU.

    *Example*:

    ```python
    pipeline = nlp.Pipeline(stages=[
        DocumentAssembler
        SentenceDetectorDL
        Tokenizer
        WordEmbeddingsModel
        MedicalNerModel
        NerConverter
        Chunk2Doc
        BertSentenceEmbeddings (TF or ONNX)
        SentenceEntityResolver
    ])
    ```

    *Results*:

    | Pipeline Scope   | TensorFlow | ONNX  | Speedup |
    |------------------|------------|-------|---------|
    | Without Resolver | 661 s      | 121 s | ~ 5.5×  |
    | With Resolver    | 6397 s     | 5758 s| ~ 10% faster|

    **Notes:**

        - ONNX version delivers a 5–6× speedup in pipelines without resolver stages.
        - Including resolver still yields a ~10% runtime improvement.
        - No pipeline logic needs to be changed to benefit from ONNX speedups.


- **ONNX Models & Batch Inference for BertForAssertionClassification**: We’ve introduced ONNX-optimized versions of the `BertForAssertionClassification` model, along with internal batching support for improved performance across CPU and GPU environments.

    - CPU Performance:

        | Framework     | Inference Time | Speedup |
        |---------------|----------------|---------|
        | TensorFlow    | 56.9 s         | —       |
        | ONNX          | 33 s           | ~ 1.7×  |

    - ⚡GPU Performance:

        | Framework     | Inference Time | Speedup   |
        |---------------|----------------|-----------|
        | TensorFlow    | 3 min 24 s     | —         |
        | ONNX          | 7.35 s         | ~ 27.8×   |


    Available ONNX Models:

    {:.table-model-big}
    | Model Name | Predicted Entities |
    |------------|--------------------|
    | [`assertion_bert_classification_clinical_onnx`](https://nlp.johnsnowlabs.com/2025/07/15/assertion_bert_classification_clinical_onnx_en.html) | `absent`, `present`, `conditional`, `associated_with_someone_else`, `hypothetical`, `possible` |
    | [`assertion_bert_classification_jsl_onnx`](https://nlp.johnsnowlabs.com/2025/07/15/assertion_bert_classification_jsl_onnx_en.html) | `Present`, `Planned`, `SomeoneElse`, `Past`, `Family`, `Absent`, `Hypothetical`, `Possible` |
    | [`assertion_bert_classification_oncology_onnx`](https://nlp.johnsnowlabs.com/2025/07/15/assertion_bert_classification_oncology_onnx_en.html) | `Present`, `Past`, `Family`, `Absent`, `Hypothetical`, `Possible` |
    | [`assertion_bert_classification_radiology_onnx`](https://nlp.johnsnowlabs.com/2025/07/15/assertion_bert_classification_radiology_onnx_en.html) | `Confirmed`, `Suspected`, `Negative` |



</div><div class="h3-box" markdown="1">

#### Batch Inference and OpenVINO Support for `PretrainedZeroShotNER`, Our Most Capable and preferred Medical NER Framework

The `PretrainedZeroShotNER` model now supports efficient batch inference, dramatically reducing GPU runtime.

- **Batch Inference**: Native support for batchSize significantly reduces GPU runtime.
    - At batchSize = 32, inference is up to 4× faster compared to legacy (non-batched) execution.
    - Output quality and accuracy remain unchanged.
    - Flexible batch size tuning allows adaptation to different hardware.

        | Configuration                 | Inference Time | Speedup |
        |-------------------------------|----------------|---------|
        | No batching (legacy)          | 2 min 51 s     | —       |
        | With batching (`batchSize=32`)| 43.3 s         | ~ 4×    |
    
- **OpenVINO Integration**: The model is now compatible with OpenVINO for optimized CPU inference,

    **Notes:**

        - The model now includes native batching (tested with `batchSize = 32`).
        - Users can tune `batchSize` to suit their hardware ("spot tuning").
        - Model accuracy and outputs remain unchanged.



</div><div class="h3-box" markdown="1">
    
####  New MedS-NER LLM for Structured Medical Entity Extraction via 3B Size Small LLMs

These schema-driven LLMs extract structured medical entities with various quantization options (Q4, Q8, Q16), including OpenVINO-optimized versions for high-speed, resource-efficient deployment.

{:.table-model-big}
| Model Name | Quantization Options | Description |
| ---------- | -------------------- | ------------ |
| **jsl_meds_ner_v4 (OpenVINO)** | [q4](https://nlp.johnsnowlabs.com/2025/06/30/jsl_meds_ner_openvino_q4_v4_en.html), [q8](https://nlp.johnsnowlabs.com/2025/07/01/jsl_meds_ner_openvino_q8_v4_en.html), [q16](https://nlp.johnsnowlabs.com/2025/07/01/jsl_meds_ner_openvino_q16_v4_en.html) | OpenVINO-optimized models for fast, efficient schema-based medical entity extraction on edge devices. |
| **jsl_meds_ner_v4** | [q4](https://nlp.johnsnowlabs.com/2025/07/01/jsl_meds_ner_q4_v4_en.html), [q8](https://nlp.johnsnowlabs.com/2025/07/01/jsl_meds_ner_q8_v4_en.html), [q16](https://nlp.johnsnowlabs.com/2025/07/01/jsl_meds_ner_q16_v4_en.html) | Standard quantized models for flexible deployment, balancing accuracy and performance in clinical text mining. |



*Example*:

```python
phi3 = Phi3Transformer.pretrained(f"jsl_meds_ner_openvino_q4_v4", "en", "clinical/models")\
    .setInputCols(["documents"])\
    .setOutputCol("generation")\
    .setMaxOutputLength(500)

text = """
### Template:
{
    "drugs": [
        {
            "name": "",
            "reactions": []
        }
    ]
}
### Text:
I feel a bit drowsy & have a little blurred vision , and some gastric problems .
I 've been on Arthrotec 50 for over 10 years on and off , only taking it when I needed it .
Due to my arthritis getting progressively worse , to the point where I am in tears with the agony.
Gp 's started me on 75 twice a day and I have to take it every day for the next month to see how I get on , here goes .
So far its been very good , pains almost gone , but I feel a bit weird , did n't have that when on 50.
"""

data = spark.createDataFrame([[text]]).toDF("text")
```

*Result*:

```bash
{
    "drugs": [
        {
            "name": "Arthrotec 50",
            "reactions": [
                "drowsy",
                "blurred vision",
                "gastric problems"
            ]
        },
        {
            "name": "75",
            "reactions": [
                "weird"
            ]
        }
    ]
}
```

</div><div class="h3-box" markdown="1">

#### Advanced Clinical One-Liner Pretrained Pipelines for PHI Detection and Extraction

We introduce specialized pretrained pipelines designed specifically for Protected Health Information (PHI) detection and de-identification in clinical documents. These pipelines leverage state-of-the-art Named Entity Recognition (NER) models to automatically identify and extract sensitive medical information, ensuring compliance with healthcare privacy regulations.

Our de-identification pipelines eliminate the complexity of building custom PHI detection systems from scratch. Healthcare organizations and researchers can now deploy robust privacy protection measures with simple one-liner implementations, streamlining the process of sanitizing clinical documents while maintaining high accuracy standards.

{:.table-model-big}
| Model Name  |      Description            |
|-------------|-----------------------------|
| [`ner_deid_docwise_benchmark_optimized`](https://nlp.johnsnowlabs.com/2025/06/17/ner_deid_docwise_benchmark_optimized_en.html) | Extract PHI information such as `LOCATION`, `CONTACT`, `PROFESSION`, `NAME`, `DATE`, `AGE`, `MEDICALRECORD`, `ORGANIZATION`, `HEALTHPLAN`, `DOCTOR`, `USERNAME`, `LOCATION-OTHER`, `URL`, `DEVICE`, `CITY`, `ZIP`, `STATE`, `PATIENT`, `STREET`, `PHONE`, `HOSPITAL`, `EMAIL`, `IDNUM`, `BIOID`, `FAX`, `LOCATION_OTHER`, `DLN`, `SSN`, `ACCOUNT`, `PLATE`, `VIN`, `LICENSE`, `IP` entities. |
| [`ner_profiling_deidentification`](https://nlp.johnsnowlabs.com/2025/06/16/ner_profiling_deidentification_en.html) | Comprehensive PHI de‑identification pipeline that combines ~40 pretrained NER models, matchers, and parsers to detect entities such as `ACCOUNT`, `AGE`, `BIOID`, `CITY`, `CONTACT`, `COUNTRY`, `DATE`, `DEVICE`, `DLN`, `DOCTOR`, `EMAIL`, `FAX`, `HEALTHPLAN`, `HOSPITAL`, `ID`, `IDNUM`, `LICENSE`, `LOCATION`, `LOCATION_OTHER`, `MEDICALRECORD`, `NAME`, `ORGANIZATION`, `PATIENT`, `PHONE`, `PROFESSION`, `SSN`, `STATE`, `STREET`, `URL`, `USERNAME`, and `ZIP`. |


*Example*:

```python
deid_pipeline = PretrainedPipeline("ner_deid_docwise_benchmark_optimized", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024. 
The patient’s medical record number is 56467890. 
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890."""
```

*Result*:

{:.table-model-big}
|    | chunks               |   begin |   end | entities   |
|----|----------------------|---------|-------|------------|
|  0 | John Lee             |       4 |    11 | DOCTOR     |
|  1 | Royal Medical Clinic |      19 |    38 | HOSPITAL   |
|  2 | Chicago              |      43 |    49 | CITY       |
|  3 | 11/05/2024           |      79 |    88 | DATE       |
|  4 | 56467890             |     131 |   138 | ID         |
|  5 | Emma Wilson          |     155 |   165 | PATIENT    |
|  6 | 50 years old         |     171 |   182 | AGE        |
|  7 | 444-456-7890         |     205 |   216 | PHONE      |




</div><div class="h3-box" markdown="1">

#### Clinical Code Resolution One-Liner Pretrained Pipelines for Medical Terminology Mapping

We introduce a comprehensive suite of specialized pretrained pipelines designed for automated medical terminology extraction and code resolution. These pipelines leverage state-of-the-art Named Entity Recognition (NER) models to identify clinical entities and map them to standardized medical coding systems, enabling seamless integration with healthcare information systems and ensuring coding compliance.

Our resolver pipelines eliminate the complexity of building custom medical terminology extraction systems. Healthcare organizations can now deploy robust clinical coding solutions with simple one-liner implementations, streamlining the process of converting unstructured clinical text into standardized medical codes across multiple coding systems.

{:.table-model-big}
| Model Name |      Description | Model Name |      Description |
|------------|------------------|------------|------------------|
| [`ner_atc_pipeline`](https://nlp.johnsnowlabs.com/2025/06/24/ner_atc_pipeline_en.html) | Maps to ATC codes | [`ner_cpt_pipeline`](https://nlp.johnsnowlabs.com/2025/06/24/ner_cpt_pipeline_en.html) | Maps to CPT codes |
| [`ner_hcc_pipeline`](https://nlp.johnsnowlabs.com/2025/06/24/ner_hcc_pipeline_en.html) | Maps to HCC codes | [`ner_hgnc_pipeline`](http://nlp.johnsnowlabs.com/2025/06/24/ner_hgnc_pipeline_en.html) | Maps to HGNC codes |
| [`ner_icd10cm_pipeline`](https://nlp.johnsnowlabs.com/2025/06/24/ner_icd10cm_pipeline_en.html) | Maps to ICD-10CM codes | [`ner_icd10pcs_pipeline`](https://nlp.johnsnowlabs.com/2025/06/24/ner_icd10pcs_pipeline_en.html) | Maps to ICD-10-PCS codes |
| [`ner_icdo_pipeline`](https://nlp.johnsnowlabs.com/2025/06/24/ner_icdo_pipeline_en.html) | Maps to ICD-O codes | [`ner_loinc_pipeline`](https://nlp.johnsnowlabs.com/2025/06/24/ner_loinc_pipeline_en.html) | Maps to LOINC codes |
| [`ner_mesh_pipeline`](https://nlp.johnsnowlabs.com/2025/06/24/ner_mesh_pipeline_en.html) | Maps to MESH codes | [`ner_ncit_pipeline`](https://nlp.johnsnowlabs.com/2025/06/24/ner_ncit_pipeline_en.html) | Maps to NCI-t codes |
| [`ner_ndc_pipeline`](https://nlp.johnsnowlabs.com/2025/06/24/ner_ndc_pipeline_en.html) | Maps to NDC codes | [`ner_rxcui_pipeline`](https://nlp.johnsnowlabs.com/2025/06/24/ner_rxcui_pipeline_en.html) | Maps to RxCUI codes |
| [`ner_rxnorm_pipeline`](https://nlp.johnsnowlabs.com/2025/06/24/ner_rxnorm_pipeline_en.html) | Maps to RxNorm codes | [`ner_hcpcs_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_hcpcs_pipeline_en.html) | Maps to HCPCS codes |
| [`ner_hpo_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_hpo_pipeline_en.html) | Maps to HPO codes | [`ner_meddra_llt_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_meddra_llt_pipeline_en.html) | Maps to MedDRA - Lowest Level Term (LLT) codes |
| [`ner_meddra_pt_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_meddra_pt_pipeline_en.html) | Maps to MedDRA PT (Preferred Term) codes | [`ner_snomed_auxConcepts_findings_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_snomed_auxConcepts_findings_pipeline_en.html) | Maps to SNOMED (Findings and Concepts) codes |
| [`ner_snomed_auxConcepts_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_snomed_auxConcepts_pipeline_en.html) | Maps to SNOMED Concept codes | [`ner_snomed_bodyStructure_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_snomed_bodyStructure_pipeline_en.html) | Maps to SNOMED (Body Structure) codes |
| [`ner_snomed_conditions_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_snomed_conditions_pipeline_en.html) | Maps to SNOMED Conditions codes | [`ner_snomed_drug_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_snomed_drug_pipeline_en.html) | Maps to SNOMED Drug codes |
| [`ner_snomed_findings_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_snomed_findings_pipeline_en.html) | Maps to SNOMED (Clinical Findings) codes | [`ner_snomed_procedures_measurements_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_snomed_procedures_measurements_pipeline_en.html) | Maps to SNOMED (Procedures and Measurements) codes |
| [`ner_snomed_term_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_snomed_term_pipeline_en.html) | Maps to SNOMED (Findings and Concepts) codes | [`ner_umls_clinical_drugs_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_umls_clinical_drugs_pipeline_en.html) | Maps to UMLS CUI (Clinical Drug) codes |
| [`ner_umls_clinical_findings_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_umls_clinical_findings_pipeline_en.html) | Maps to UMLS CUI codes | [`ner_umls_disease_syndrome_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_umls_disease_syndrome_pipeline_en.html) | Maps to UMLS CUI (Disease or Syndrome) codes |
| [`ner_umls_drug_substance_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_umls_drug_substance_pipeline_en.html) | Maps to UMLS CUI (Drug & Substance) codes | [`ner_umls_major_concepts_pipeline`](https://nlp.johnsnowlabs.com/2025/06/25/ner_umls_major_concepts_pipeline_en.html) | Maps to 4 major categories of UMLS CUI codes |
| [`ner_ade_age_meddra_test_pipeline`](https://nlp.johnsnowlabs.com/2025/06/29/ner_ade_age_meddra_test_pipeline_en.html) | Extracts Age, Age Groups, ADE, MedDRA codes, Laboratory Tests and Results, Medical History, and Administory information |


*Example*:

```python
ner_pipeline = PretrainedPipeline("ner_atc_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
The patient was prescribed Albuterol inhaler when needed. She was seen by the endocrinology service, prescribed Avandia 4 mg at nights,
Coumadin 5 mg with meals, Metformin 100 mg two times a day, and a daily dose of Lisinopril 10 mg.
""")
```

*Result*:

{:.table-model-big}
|   | chunks            | begin | end | entities |
|---|-------------------|-------|-----|----------|
| 0 | Albuterol inhaler |    28 |  44 | DRUG     |
| 1 | Avandia 4 mg      |   113 | 124 | DRUG     |
| 2 | Coumadin 5 mg     |   137 | 149 | DRUG     |
| 3 | Metformin 100 mg  |   163 | 178 | DRUG     |
| 4 | Lisinopril 10 mg  |   217 | 232 | DRUG     |



</div><div class="h3-box" markdown="1">

#### Clinical Document Explanation One-Liner Pretrained Pipelines for Comprehensive Clinical Entity Analysis

We introduce a sophisticated suite of domain-specific pretrained pipelines designed for comprehensive clinical document explanation and entity extraction. These advanced pipelines combine multiple state-of-the-art NER models and text matchers to provide detailed analysis and interpretation of clinical narratives across various medical specialties and use cases.

Our explanation pipelines transform complex clinical documents into structured, interpretable data by automatically identifying and categorizing clinical entities, relationships, and contextual information. This enables healthcare professionals and researchers to quickly understand and analyze clinical content without manual review, significantly improving efficiency in clinical documentation processing.

{:.table-model-big}
| Model Name |      Description            |
|------------|-----------------------------|
| [`explain_clinical_doc_generic_light`](https://nlp.johnsnowlabs.com/2025/06/26/explain_clinical_doc_generic_light_en.html) | Extracts PROBLEM, TEST, and TREATMENT entities with four clinical NER models. |
| [`explain_clinical_doc_biomarker_light`](https://nlp.johnsnowlabs.com/2025/06/27/explain_clinical_doc_biomarker_light_en.html) | Extracts the biomarkers and their results with 3 NER models and a text matcher. |
| [`explain_clinical_doc_medication_generic_light`](https://nlp.johnsnowlabs.com/2025/06/27/explain_clinical_doc_medication_generic_light_en.html) | Extract medication entities with 2 NER models and a text matcher. |
| [`explain_clinical_doc_medication_light`](https://nlp.johnsnowlabs.com/2025/06/27/explain_clinical_doc_medication_light_en.html) | Extract medication entities with 2 NER models and a text matcher. |
| [`explain_clinical_doc_mental_health_light`](https://nlp.johnsnowlabs.com/2025/06/27/explain_clinical_doc_mental_health_light_en.html) | Extract mental health-related clinical/medical entities with 2 NER models and a text matcher. |
| [`explain_clinical_doc_oncology_light`](https://nlp.johnsnowlabs.com/2025/06/27/explain_clinical_doc_oncology_light_en.html) | Extract oncology-related clinical/medical entities with 4 NER models and 2 text matchers. |
| [`explain_clinical_doc_public_health_light`](https://nlp.johnsnowlabs.com/2025/06/27/explain_clinical_doc_public_health_light_en.html) | Extract public health-related clinical/medical entities with 3 NER models and a text matcher. |
| [`explain_clinical_doc_radiology_light`](https://nlp.johnsnowlabs.com/2025/06/27/explain_clinical_doc_radiology_light_en.html) | Extract radiology-related clinical/medical entities with 3 NER models. |
| [`explain_clinical_doc_risk_factors_light`](https://nlp.johnsnowlabs.com/2025/06/27/explain_clinical_doc_risk_factors_light_en.html) | Extract entities that may be considered as risk factors with 3 NER models and 2 text matchers. |
| [`explain_clinical_doc_sdoh_light`](https://nlp.johnsnowlabs.com/2025/06/27/explain_clinical_doc_sdoh_light_en.html) | Extract social determinants of health-related clinical/medical entities with 3 NER models and 2 text matchers. |
| [`explain_clinical_doc_vop_light`](https://nlp.johnsnowlabs.com/2025/06/27/explain_clinical_doc_vop_light_en.html) | Extract clinical/medical entities with 3 NER models and 2 text matchers. |
| [`explain_clinical_doc_ade_light`](https://nlp.johnsnowlabs.com/2025/06/30/explain_clinical_doc_ade_light_en.html) | Extract `ADE` and `DRUG` entities, and establish relations between the extracted `DRUG` and `ADE` results from the clinical documents. |
| [`explain_clinical_doc_granular_light`](https://nlp.johnsnowlabs.com/2025/06/30/explain_clinical_doc_granular_light_en.html) | Extract clinical entities and establish relations between the extracted entities. |


*Example*:

```python
ner_pipeline = PretrainedPipeline("explain_clinical_doc_generic_light", "en", "clinical/models")

text = """A 65-year-old woman had a history of debulking surgery, bilateral oophorectomy with omentectomy, total anterior hysterectomy with radical pelvic lymph nodes dissection due to ovarian carcinoma (mucinous-type carcinoma, stage Ic) 1 year ago.
 The patient's medical compliance was poor and failed to complete her chemotherapy (cyclophosphamide 750 mg/m2, carboplatin 300 mg/m2). 
 Recently, she noted a palpable right breast mass, 15 cm in size which nearly occupied the whole right breast in 2 months. Core needle biopsy revealed metaplastic carcinoma.
 """

result = ner_pipeline.annotate(text)
```

*Result*:

{:.table-model-big}
|    | chunks                                |begin | end | entities       |
|----|---------------------------------------|------|-----|----------------|
|  0 | debulking surgery                     |   37 |  53 | TREATMENT      |
|  1 | bilateral oophorectomy                |   56 |  77 | CANCER_SURGERY |
|  2 | omentectomy                           |   84 |  94 | TREATMENT      |
|  3 | total anterior hysterectomy           |   98 | 124 | TREATMENT      |
|  4 | radical pelvic lymph nodes dissection |  131 | 167 | TREATMENT      |
|  5 | ovarian carcinoma                     |  176 | 192 | PROBLEM        |
|  6 | mucinous-type carcinoma               |  195 | 217 | PROBLEM        |
|  7 | stage Ic                              |  220 | 227 | PROBLEM        |
|  8 | her chemotherapy                      |  308 | 323 | TREATMENT      |
|  9 | cyclophosphamide                      |  326 | 341 | TREATMENT      |
| 10 | carboplatin                           |  354 | 364 | TREATMENT      |
| 11 | a palpable right breast mass          |  400 | 427 | PROBLEM        |
| 12 | Core needle biopsy                    |  504 | 521 | TREATMENT      |
| 13 | metaplastic carcinoma                 |  532 | 552 | PROBLEM        |





</div><div class="h3-box" markdown="1">

#### New NER Model and Pipeline About Vaccinations and Infectious Diseases

The new vaccination NER models are specialized for extracting comprehensive vaccine-related information from clinical and medical texts. These models go beyond basic vaccine identification to capture the full vaccination context, including disease relationships and vaccine characteristics.

{:.table-model-big}
| Model Name |      Description            |
|------------|-----------------------------|
| [`ner_vaccine_types`](https://nlp.johnsnowlabs.com/2025/07/14/ner_vaccine_types_en.html) | Extract vaccine and related disease/symptom entities from clinical/medical texts. |
| [`ner_vaccine_types_pipeline`](https://nlp.johnsnowlabs.com/2025/07/14/ner_vaccine_types_pipeline_en.html) | Extract types of vaccines and related disease/symptom entities from clinical/medical texts. |



*Example*:

```python
ner_model = MedicalNerModel.pretrained("ner_vaccine_types", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

sample_texts = ["""
On May 14, 2023, a 57-year-old female presented with fever, joint pain, and fatigue three days after receiving her third dose of the Shingrix vaccine.
Her history includes rheumatoid arthritis, managed with immunosuppressants, and prior breast cancer in remission. 
She previously received Gardasil 9, an HPV vaccine, and the hepatitis B recombinant vaccine series in 2020. 
Notably, she developed mild aches following her annual influenza shot, which is an inactivated vaccine."""
]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")
```

*Result*:

{:.table-model-big}
|sent_id|chunk               |begin|end|entities              |
|-------|--------------------|-----|---|----------------------|
|0      |May 14, 2023        |4    |15 |Date                  |
|0      |57-year-old         |20   |30 |Age                   |
|0      |fever               |54   |58 |Sign_Symptom          |
|0      |joint pain          |61   |70 |Sign_Symptom          |
|0      |fatigue             |77   |83 |Sign_Symptom          |
|0      |third dose          |116  |125|Vax_Dose              |
|0      |Shingrix            |134  |141|Viral_Vax             |
|0      |vaccine             |143  |149|Adaptive_Immunity     |
|1      |rheumatoid arthritis|174  |193|Other_Disease_Disorder|
|1      |breast cancer       |239  |251|Other_Disease_Disorder|
|2      |Gardasil            |292  |301|Viral_Vax             |
|2      |HPV                 |307  |309|Infectious_Disease    |
|2      |vaccine             |311  |317|Adaptive_Immunity     |
|2      |hepatitis B         |328  |338|Infectious_Disease    |
|2      |recombinant         |340  |350|Other_Vax             |
|2      |vaccine             |352  |358|Adaptive_Immunity     |
|2      |2020                |370  |373|Date                  |
|3      |aches               |405  |409|Sign_Symptom          |
|3      |influenza           |432  |440|Infectious_Disease    |
|3      |inactivated         |460  |470|Inactivated           |
|3      |vaccine             |472  |478|Adaptive_Immunity     |


</div><div class="h3-box" markdown="1">

#### New Blog Posts on Various Topics

- [Beyond Named Entity Recognition: A Comprehensive NLP Framework for HPO Phenotype Classification](https://www.johnsnowlabs.com/beyond-named-entity-recognition-a-comprehensive-nlp-framework-for-hpo-phenotype-classification/) Human phenotypes, observable traits, and clinical abnormalities like “short stature” or “muscle weakness” are crucial in diagnosing diseases, especially in rare and genetic conditions. However, these phenotypes are often buried in unstructured clinical text. To address this, we built an NLP pipeline using John Snow Labs’ Healthcare NLP & LLM library that automatically extracts phenotype mentions, determines their assertion status (e.g., present, absent, etc.), and maps them to standardized Human Phenotype Ontology (HPO) codes, which provides a structured vocabulary used worldwide in genomics and precision medicine. This pipeline enables scalable, accurate phenotypic data extraction for research and clinical applications.

</div><div class="h3-box" markdown="1">

#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, and Reliability of Healthcare NLP

- Closed ONNX tensors for better memory management in `BertForAssertionClassification`  
- Fixed an issue in `TextMatcherInternal` where `null` values could appear in the output due to race conditions during parallel processing.
- Resolved a bug in `PretrainedZeroShotNER` that caused an `emptyIterator` exception in certain edge cases when processing empty or malformed input.
- Improved Geo-consistency algorithm in `Deidentification` to handle geo entities if skipped

</div><div class="h3-box" markdown="1">

#### Updated Notebooks and Demonstrations for making Healthcare NLP Easier to Navigate and Understand

- New [Deidentification NER Profiling Pipeline](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/04.12.Deidentification_NER_Profiling_Pipeline.ipynb) Notebook
- New [Annotation Converter](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/50.Annotation_Converter.ipynb) Notebook 
- Updated [Pretrained NER Profiling Pipelines](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.1.Pretrained_NER_Profiling_Pipelines.ipynb) Notebook
- Updated [Clinical Deidentification Improvement](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/04.4.Clinical_Deidentification_Improvement.ipynb) Notebook


</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `jsl_meds_ner_openvino_q4_v4`
+ `jsl_meds_ner_openvino_q8_v4`
+ `jsl_meds_ner_openvino_q16_v4`
+ `jsl_meds_ner_q4_v4`
+ `jsl_meds_ner_q8_v4`
+ `jsl_meds_ner_q16_v4`
+ `ner_deid_docwise_benchmark_optimized`
+ `ner_profiling_deidentification`
+ `ner_atc_pipeline`
+ `ner_cpt_pipeline`
+ `ner_hcc_pipeline`
+ `ner_hgnc_pipeline`
+ `ner_icd10cm_pipeline`
+ `ner_icd10pcs_pipeline`
+ `ner_icdo_pipeline`
+ `ner_loinc_pipeline`
+ `ner_mesh_pipeline`
+ `ner_ncit_pipeline`
+ `ner_ndc_pipeline`
+ `ner_rxcui_pipeline`
+ `ner_rxnorm_pipeline`
+ `ner_hcpcs_pipeline`
+ `ner_hpo_pipeline`
+ `ner_meddra_llt_pipeline`
+ `ner_meddra_pt_pipeline`
+ `ner_snomed_auxConcepts_findings_pipeline`
+ `ner_snomed_auxConcepts_pipeline`
+ `ner_snomed_bodyStructure_pipeline`
+ `ner_snomed_conditions_pipeline`
+ `ner_snomed_drug_pipeline`
+ `ner_snomed_findings_pipeline`
+ `ner_snomed_procedures_measurements_pipeline`
+ `ner_snomed_term_pipeline`
+ `ner_umls_clinical_drugs_pipeline`
+ `ner_umls_clinical_findings_pipeline`
+ `ner_umls_disease_syndrome_pipeline`
+ `ner_umls_drug_substance_pipeline`
+ `ner_umls_major_concepts_pipeline`
+ `explain_clinical_doc_generic_light`
+ `explain_clinical_doc_biomarker_light`
+ `explain_clinical_doc_medication_generic_light`
+ `explain_clinical_doc_medication_light`
+ `explain_clinical_doc_mental_health_light`
+ `explain_clinical_doc_oncology_light`
+ `explain_clinical_doc_public_health_light`
+ `explain_clinical_doc_radiology_light`
+ `explain_clinical_doc_risk_factors_light`
+ `explain_clinical_doc_sdoh_light`
+ `explain_clinical_doc_vop_light`
+ `explain_clinical_doc_ade_light`
+ `explain_clinical_doc_granular_light`
+ `ner_ade_age_meddra_test_pipeline`
+ `ner_vaccine_types`
+ `ner_vaccine_types_pipeline`
+ `assertion_bert_classification_clinical_onnx`
+ `assertion_bert_classification_jsl_onnx`
+ `assertion_bert_classification_oncology_onnx`
+ `assertion_bert_classification_radiology_onnx`


</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">


## Previous versions

</div>
{%- include docs-healthcare-pagination.html -%}
