---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/licensed_release_notes
key: docs-licensed-release-notes
modify_date: 2026-01-27
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 6.3.0

#### Highlights

We are delighted to announce remarkable enhancements and updates in our latest major release of Healthcare NLP. This release expands broader cloud environment support with Scala 2.13 and Java 17 compatibility, extends support for the latest LLM families, and delivers 9 new Medical Vision LLMs that advance clinical AI with multimodal text and image understanding, alongside 67 new one-liner pretrained pipelines and models for end-to-end clinical document understanding.
The release also introduces scalable and flexible HL7 CDA (XML) de-identification and a new De-identification MCP Server (Preview) for seamless integration with external AI agents and IDE clients. Comprehensive benchmark evaluations are included, featuring large-scale clinical de-identification speed–accuracy benchmarks across infrastructures and comparative Medical Vision LLM benchmark results against leading foundation models.
In addition, this version delivers memory-optimized MedicalNer training for large-scale datasets, enhanced entity resolution with new UMLS CUI and LOINC models, expanded rule-based and neural NER coverage, core robustness improvements across the pipeline ecosystem, newly created notebooks, and published technical blog posts and deep dives to further strengthen Healthcare NLP.

- Scala 2.13 & Java 17 Compatibility with Broader Cloud Environment Support
- 9 Medical Vision LLMs Extending Clinical AI to Multimodal Text and Image Understanding
- Scalable and Flexible CDA (HL7) De-identification Support for XML Clinical Documents
- De-identification MCP Server (Preview) for Clinical Text De-identification via External AI Agents and IDE Clients
- Upgraded Llama.cpp Backend with Expanded Compatibility for the Latest LLM Families
- Memory-Optimized MedicalNer Training for Large-Scale Datasets
- Clinical De-Identification at Scale: Pipeline Design and Speed–Accuracy Benchmarks Across Infrastructures
- Comparative Medical Vision LLM Benchmark Results Against Leading Foundation Models
- Advanced clinical one-liner pretrained pipelines for PHI detection and extraction
- Enhanced 8 new entity resolver models for mapping clinical terms to standardized UMLS CUI codes and LOINC
- Introduced 17 new rule-based entity extraction models for identifying structured codes and patterns in clinical texts
- Introduced 7 new NER models for PHI deidentification and drug entity extraction
- Enhanced 8 new contextual assertion models to classify clinical entities by assertion status
- Added new ONNX-based multilingual clinical NER models for Italian, Spanish, and Romanian, covering disease, procedure, medication, and symptom entity extraction
- New Blog Posts & Technical Deep Dives
- Various core improvements, bug fixes, enhanced overall robustness and reliability of Healthcare NLP
    - Improved PipelineTracer coverage by adding support for PretrainedZeroShotNERChunker, ContextualEntityRuler, ContextualEntityFilterer
    - Added replaceDict to AssertionMerger to allow custom replacement of assertion labels.
    - PipelineOutputParser improvements to support mappings output in clinical_deidentification pipelines
- Updated notebooks and demonstrations for making Healthcare NLP easier to navigate and understand
    - New [CDA DeIdentification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.14.CDA_DeIdentification.ipynb) Notebook
- The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Healthcare NLP, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


<div class="h3-box" markdown="1">

#### Scala 2.13 & Java 17 Compatibility with Broader Cloud Environment Support

With Healthcare NLP **6.3.0**, we introduce official support for **Scala 2.13** while continuing to support **Scala 2.12** through a dual-JAR distribution strategy. **Scala 2.13** JAR is built and tested against **Java 17**, enabling smoother adoption of modern JVM runtimes and reducing friction when deploying on managed cloud Spark platforms.

**Databricks**
- Recommended runtimes: **Databricks Runtime 16.4 LTS (Scala 2.13 image / Spark 3.5.2)**.  
  Databricks provides both **Scala 2.12 and Scala 2.13 images** for this runtime, allowing customers to validate and migrate at their own pace.
- Fully compatible with Databricks Runtime 16.x (Spark 3.5.x) environments running either Scala 2.12 or Scala 2.13.

**Google Cloud (Dataproc)**
- **Cluster-based Dataproc**: Compatible with Dataproc **2.x image families (including 2.2 and 2.3)** that provide Scala 2.13 and Java 17.
- **Dataproc Serverless for Spark**: Supported on **2.2 and newer runtimes**, which include **Scala 2.13** and **Java 17** in their execution environment.

These updates significantly broaden support across cloud environments, enabling Healthcare NLP to run on a wider range of instance types and managed runtime configurations on both AWS and GCP.

**Practical notes**
- Use the **Scala 2.13** JAR on environments that provide Scala 2.13 (e.g. Databricks Scala 2.13 images, Dataproc 2.x runtimes).
- Use the **Scala 2.12** JAR on environments that are still based on Scala 2.12.
- **Spark 4 is not supported in 6.3.0** and will be addressed in a future release.


</div><div class="h3-box" markdown="1">

#### 9 Medical Vision LLMs Extending Clinical AI to Multimodal Text and Image Understanding

In this release, we are expanding our Medical Vision LLM (VLM) family with additional models specifically finetuned for medical tasks. These models extend large language model capabilities with integrated visual language understanding, enabling multimodal clinical analysis by combining textual and image inputs.

The new VLMs provide strong performance for tasks such as diagnostic image interpretation, image-to-text summarization, and integrated documentation analysis — continuing our mission to advance clinical AI with robust, domain-specific multimodal solutions.


{:.table-model-big}
| **Model Name**             | **Quantization Options**   |
| -------------------------- | -------------------------- |
| jsl_meds_vlm_7b_v1         | [q4](https://nlp.johnsnowlabs.com/2025/12/17/jsl_meds_vlm_7b_q4_v1_en.html), [q8](https://nlp.johnsnowlabs.com/2025/12/17/jsl_meds_vlm_7b_q8_v1_en.html), [q16](https://nlp.johnsnowlabs.com/2025/12/17/jsl_meds_vlm_7b_q16_v1_en.html) |
| jsl_meds_vlm_4b_v1         | [q4](https://nlp.johnsnowlabs.com/2026/01/08/jsl_meds_vlm_4b_q4_v1_en.html), [q8](https://nlp.johnsnowlabs.com/2026/01/08/jsl_meds_vlm_4b_q8_v1_en.html), [q16](https://nlp.johnsnowlabs.com/2026/01/08/jsl_meds_vlm_4b_q16_v1_en.html) |
| jsl_meds_vlm_reasoning_8b_v1  | [q4](https://nlp.johnsnowlabs.com/2026/01/09/jsl_meds_vlm_reasoning_8b_q4_v1_en.html), [q8](https://nlp.johnsnowlabs.com/2026/01/09/jsl_meds_vlm_reasoning_8b_q8_v1_en.html), [q16](https://nlp.johnsnowlabs.com/2026/01/09/jsl_meds_vlm_reasoning_8b_q16_v1_en.html) |

*Example*: jsl_meds_vlm_reasoning_8b_q4_v1 

<img src="https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/healthcare-nlp/data/ocr/prescription_02.png" 
     alt="Prescription Image" 
     width="400"/>

```python
prompt = """
Extract madication and demographic patient information from the document and return strictly as JSON:

{
  "patient": {"name": string, "age": string, "sex": string, "hospital_no": string, "episode_no": string, "episode_date": string},
  "diagnoses": [string],
  "symptoms": [string],
  "treatment": [{"med": string, "dose": string, "freq": string}]
}
"""

input_df = vision_llm_preprocessor(
    spark=spark,
    images_path="images",
    prompt=prompt,
    output_col_name="prompt"
)

document_assembler = DocumentAssembler() \
    .setInputCol("prompt") \
    .setOutputCol("caption_document")

image_assembler = ImageAssembler() \
    .setInputCol("image") \
    .setOutputCol("image_assembler")

medicalVisionLLM = (
    MedicalVisionLLM.pretrained("jsl_meds_vlm_reasoning_8b_q4_v1", "en", "clinical/models")
    .setInputCols(["caption_document", "image_assembler"])
    .setOutputCol("completions")
    .setNCtx(8*4096)
    .setNPredict(-1)
    .setTemperature(0.1)
)

pipeline = Pipeline().setStages([
    document_assembler,
    image_assembler,
    medicalVisionLLM
])

model = pipeline.fit(input_df)
result = model.transform(input_df)
```

*Result*:

```bash
{
  "patient": {
    "name": "Ms RUKHSANA SHAHEEN",
    "age": "56 yrs",
    "sex": "Female",
    "hospital_no": "MH005990453",
    "episode_no": "030000528270",
    "episode_date": "02/07/2021 08:31AM"
  },
  "diagnoses": [
    "systemic lupus erythematosus",
    "scleroderma overlap",
    "interstitial lung disease"
  ],
  "symptoms": [
    "tightness of skin of the fists",
    "ulcers on the pulp of the fingers"
  ],
  "treatment": [
    {
      "med": "Linezolid",
      "dose": "600 mg",
      "freq": "twice a day for 5 Days"
    },
    {
      "med": "Clopidogrel",
      "dose": "75 mg",
      "freq": "once a day after meals"
    },
    {
      "med": "Amlodipine",
      "dose": "5 mg",
      "freq": "once a day"
    },
    {
      "med": "Domperidone",
      "dose": "10 mg",
      "freq": "twice a day before meals"
    },
    {
      "med": "Omeprazole",
      "dose": "20 Mg",
      "freq": "Twice a Day before Meal"
    },
    {
      "med": "Bosentan",
      "dose": "62.5 mg",
      "freq": "twice a day after meals"
    },
    {
      "med": "Sildenafil Citrate",
      "dose": "0.5 mg",
      "freq": "twice a day after meals"
    },
    {
      "med": "Prednisolone",
      "dose": "5 mg",
      "freq": "once a day after breakfast"
    },
    {
      "med": "Mycophenolate mofetil",
      "dose": "500 mg 2 tablets",
      "freq": "twice a day"
    },
    {
      "med": "L-methylfolate calcium",
      "dose": "400 µg 1 tablet",
      "freq": "once a day"
    },
    {
      "med": "ciprofloxacin",
      "dose": "250 mg",
      "freq": "twice a day"
    }
  ]
}
```
Overall, this release strengthens our Medical Vision LLM portfolio by enabling robust, production-ready multimodal analysis for real-world clinical documents and images.


</div><div class="h3-box" markdown="1">

#### Scalable and Flexible CDA (HL7) De-identification Support for XML Clinical Documents

We’re introducing **native de-identification support for HL7 CDA (Clinical Document Architecture) reports in XML format** within Healthcare NLP.
This module enables secure, large-scale processing of CDA R2 documents by combining **structure-aware XML de-identification** with **NLP-based free-text anonymization**, all delivered through a single, scalable Spark transformer.

Unlike flat text approaches, CDA de-identification operates directly on the **XML document structure**, allowing precise targeting of sensitive fields using **XPath-like path expressions**, while preserving the integrity and schema of the original clinical document.

**Key Capabilities**

* **Path-based CDA de-identification**
  Target and de-identify specific CDA elements using dot (`.`) or slash (`/`) notation, enabling fine-grained control over clinical fields such as patient demographics, authors, organizations, and identifiers.

* **Attribute-level access**
  Seamlessly de-identify XML attributes (e.g. telecom values and identifiers) using intuitive attribute notation, without requiring manual XML parsing or preprocessing.

* **Namespace-aware processing**
  Automatically handles the HL7 v3 namespace, reducing configuration overhead and simplifying integration with existing CDA workflows.

* **Structured field obfuscation**
  Deterministically or randomly obfuscate structured fields such as names, dates, addresses, phone numbers, and identifiers while preserving XML validity and document structure.

* **NLP-powered free-text de-identification**
  Apply Spark NLP de-identification pipelines to narrative sections (e.g. clinical notes and section text) embedded within CDA documents, ensuring comprehensive PHI coverage across both structured and unstructured content.

* **Unified Spark execution model**
  Fully compatible with Spark pipelines and batch processing workflows, enabling de-identification at scale without separating structured XML processing from free-text NLP pipelines.

**Designed for Real-World CDA Workflows**

The CDA De-identification module allows organizations to process heterogeneous CDA documents—where structured XML fields and free-text clinical narratives coexist—using a **single, consistent configuration model**.
By combining XPath-style rules with reusable NLP pipelines, teams can adapt de-identification behavior across document types without rewriting logic or maintaining parallel processing systems.

This approach delivers **enterprise-grade performance, flexibility, and compliance**, making it ideal for large healthcare data platforms, analytics pipelines, and downstream AI workloads that rely on CDA-formatted clinical data.

*Example*:

```python
import sparknlp_jsl
from sparknlp_jsl.annotator import *
from sparknlp.pretrained import PretrainedPipeline

rules = {
    "recordTarget.patientRole.patient.name.given": "first_name",
    "recordTarget.patientRole.patient.name.family": "last_name",
    "recordTarget.patientRole.addr.streetAddressLine": "Address",
    "recordTarget.patientRole.telecom.value": "Phone",
    "author.assignedAuthor.assignedPerson.name.given": "first_name",
    "author.assignedAuthor.assignedPerson.name.family": "last_name",
}

deid_pipeline = PretrainedPipeline("clinical_deidentification_docwise_benchmark_optimized",
                                   "en",
                                   "clinical/models")


cda_deidentification = (
    CdaDeIdentification()
      .setInputCol("text")
      .setOutputCol("deid")
      .setMode("obfuscate")
      .setMappingRules(rules)
      .setFreeTextPaths([
          "component.structuredBody.component.section.text"
      ])
      .setPipeline(spark, deid_pipeline, "obfuscated")
      .setDays(20)
      .setSeed(88)
)

result = cda_deidentification.deidentify(cda_document)

```

*Original CDA*:
```bash
<?xml version="1.0" encoding="UTF-8"?>
<ClinicalDocument xmlns="urn:hl7-org:v3"
                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xsi:schemaLocation="urn:hl7-org:v3 CDA.xsd">

    <!-- ===================== AUTHOR ===================== -->
    <author>
        <time value="20240101113000"/>
        <assignedAuthor>
            <id root="2.16.840.1.113883.4.6" extension="111223333"/>
            <assignedPerson>
                <name>
                    <given>Emily</given>
                    <family>Clark</family>
                </name>
            </assignedPerson>
            <representedOrganization>
                <id root="2.16.840.1.113883.19.5" extension="ORG001"/>
                <name>Good Health Clinic</name>
            </representedOrganization>
        </assignedAuthor>
    </author>

    <!-- ===================== BODY ===================== -->
    <component>
        <structuredBody>
            <component>
                <section>
                    <code code="10164-2" codeSystem="2.16.840.1.113883.6.1" displayName="History of Present Illness"/>
                    <title>History of Present Illness</title>
                    <text>
                        Patient John Doe presented with chest pain and shortness of breath.
                        He lives at 456 Main Street, Istanbul. Contact number is +905551112233.
                    </text>
                </section>
            </component>
        </structuredBody>
    </component>
</ClinicalDocument>

```
*De-identified CDA*:
```bash
<?xml version="1.0" encoding="UTF-8" standalone="no"?><ClinicalDocument xmlns="urn:hl7-org:v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:hl7-org:v3 CDA.xsd">

    <!-- ===================== AUTHOR ===================== -->
    <author>
        <time value="20240101113000"/>
        <assignedAuthor>
            <id extension="111223333" root="2.16.840.1.113883.4.6"/>
            <assignedPerson>
                <name>
                    <given>Mayford</given>
                    <family>Rock</family>
                </name>
            </assignedPerson>
            <representedOrganization>
                <id extension="ORG001" root="2.16.840.1.113883.19.5"/>
                <name>Good Health Clinic</name>
            </representedOrganization>
        </assignedAuthor>
    </author>

    <!-- ===================== BODY ===================== -->
    <component>
        <structuredBody>
            <component>
                <section>
                    <code code="10164-2" codeSystem="2.16.840.1.113883.6.1" displayName="History of Present Illness"/>
                    <title>History of Present Illness</title>
                    <text>Patient Valerie Ates presented with chest pain and shortness of breath.
                        He lives at Pr-2 Ponce By Pass, 13218 Brook Lane Drive. Contact number is +127773334455.
                    </text>
                </section>
            </component>
        </structuredBody>
    </component>
</ClinicalDocument>

```


</div><div class="h3-box" markdown="1">

#### De-identification MCP Server (Preview) for Clinical Text De-identification via External AI Agents and IDE Clients

We are introducing a new Model Context Protocol (MCP) server that enables Spark NLP Healthcare clinical de-identification to be accessed directly from external AI agents and IDE clients.
This preview release exposes de-identification pipelines through a standardized MCP interface, enabling seamless integration with modern AI tooling and developer workflows.

**Key Features**
The following capabilities are included in the preview release:
- Enables clinical text de-identification via external AI agents and IDE clients using MCP
- Provides a standardized MCP interface for invoking Spark NLP Healthcare de-identification pipelines
- Supports configurable output modes:
    * Masked
    * Obfuscated
    * Masked and Obfuscated
- Delivered as a containerized, standalone service suitable for both local and remote deployments
- Designed for consistent integration across MCP-compatible clients

**Reference Implementation**

A reference implementation is available in the Spark NLP Workshop repository:

- Repository:
  [https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/agents/mcp_servers/deidentification](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/agents/mcp_servers/deidentification)
- Access the relevant blog here:
  [https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/agents/mcp_servers/deidentification/blog/deid-blog-mcp-server.md](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/agents/mcp_servers/deidentification/blog/deid-blog-mcp-server.md)

**Usage Overview**

1. Register the MCP Server in Your Client

In an MCP-compatible client (for example, Cursor, VS Code Copilot / Agent, or Claude CLI), register a new MCP server with the following configuration:

- URL: `http://localhost:8001/mcp`
- Transport: `streamable-http`

This registration pattern is consistent across MCP clients and requires only the server URL and transport type.

2. Send a Tool Request

Once connected, the client automatically discovers the tools exposed by the MCP server.

Example request:

> Use the `deidentify_text` tool to de-identify this clinical note with the output mode set to `masked` (or `obfuscated` or `both`) and return the transformed text.

</div><div class="h3-box" markdown="1">

#### Upgraded Llama.cpp Backend with Expanded Compatibility for the Latest LLM Families

With Healthcare NLP **6.3.0**, we deliver a major upgrade to the LLM backend based on a newer llama.cpp version, improving performance, stability, and compatibility for local and distributed LLM inference. This update enables smoother integration of the latest llama.cpp–compatible models into ingestion and enrichment pipelines, while strengthening support for large-scale, on-prem and cloud-based deployments.

**🚀 Key Improvements**

- **Upgraded LLM Backend (llama.cpp)**  
  The llama.cpp backend has been modernized to benefit from upstream performance optimizations, improved memory handling, and enhanced stability. This results in more efficient and reliable local LLM inference, especially in distributed Spark environments.

- **Expanded Model Compatibility**  
  Healthcare NLP now supports newer LLM families such as **Qwen3**, allowing customers to adopt the latest generation models with confidence. These models can be seamlessly loaded and used through **MedicalLLM**, **MedicalVisualLLM**, and **LLMLoader**, enabling both text and vision use cases within the same unified framework.

**Impact**

These enhancements provide faster startup times, improved inference stability, and greater flexibility when working with modern LLMs. Teams can more easily integrate the latest models into their NLP pipelines, build richer multimodal workflows, and scale local LLM inference without increasing operational complexity.

</div><div class="h3-box" markdown="1">

#### Memory-Optimized MedicalNer Training for Large-Scale Datasets

MedicalNer training is enhanced with additional memory-focused optimizations that improve scalability when working with large datasets. These improvements reduce peak memory usage and help training run more reliably on cloud clusters, enabling larger corpus training without requiring proportionally larger executors.

**Key additions include new training parameters:**

- setEnableMemoryOptimizer(True): Already available in previous versions, this setting activates memory optimization techniques during training to lower memory consumption.

- setOptimizePartitioning(True): Optionally repartitions the dataset before training to improve data distribution and performance, especially for large or skewed datasets.

- setPrefetchBatches(n): Number of batches to prefetch during training to improve data loading efficiency.

Together, these updates make MedicalNer training more efficient and better suited for large-scale production workflows.


</div><div class="h3-box" markdown="1">

#### Clinical De-Identification at Scale: Pipeline Design and Speed–Accuracy Benchmarks Across Infrastructures

To present a focused update on large-scale clinical de-identification benchmarks, emphasizing pipeline design, execution strategy, and infrastructure-aware performance, we benchmarked how different pipeline architectures - rule-augmented NER, hybrid NER + zero-shot, and zero-shot–centric approaches - behave under realistic Google Colab and Databricks–AWS deployments.

- Four complementary datasets are used to evaluate clinical de-identification pipelines from different perspectives;
  - Dataset 1: Paper Dataset - Expert-Annotated
  - Dataset 2: Curated Surrogate Clinical Dataset
  - Dataset 3: Document-Level Clinical De-Identification Context Dataset
  - Dataset 4: Large-Scale Aggregated Clinical NER and De-Identification Dataset

- Clinical De-identification – Most Up-to-Date Pipelines

    - Test Environment:
        - GPU Setup: Google Colab A100 GPU, 48 Spark partitions
        - CPU Setup: Google Colab CPU High-RAM, 32 Spark partitions
    - Datasets Used: 
        - Dataset 1, Dataset 2 for accuracy benchmark, and 
        - Dataset 3 for speed benchmark.

{:.table-model-big.db}
| pipeline                                                             | GPU<br>wall time | CPU<br>wall time | Paper<br>precision | Paper<br>recall | Paper<br>F1-score | Surrogate<br>precision | Surrogate<br>recall | Surrogate<br>F1-score | pipeline content |
|----------------------------------------------------------------------|------------------:|------------------:|-------------------:|----------------:|------------------:|----------------------:|-------------------:|---------------------:|-----------------|
| clinical_deidentification_docwise_benchmark_optimized                | 5 min 15 sec     | 8 min 55 sec     | 0.93               | 0.93            | 0.93              | 0.92                  | 0.96               | 0.94                 | 21 rule-based annotators<br>4 NER |
| clinical_deidentification_docwise_benchmark_medium                   | 4 min 38 sec     | 32 min 57 sec    | 0.90               | 0.97            | 0.93              | 0.87                  | 0.96               | 0.91                 | 21 rule-based annotators<br>3 NER + 1 Zero-shot (medium) |
| clinical_deidentification_docwise_benchmark_medium_v2                | 3 min 42 sec     | 37 min 56 sec    | 0.91               | 0.96            | 0.93              | 0.86                  | 0.93               | 0.90                 | 21 rule-based annotators<br>2 NER + Zero-shot Chunker |
| clinical_deidentification_docwise_zeroshot_medium                    | 26.7 sec         | 27 min           | 0.92               | 0.94            | 0.93              | 0.86                  | 0.90               | 0.88                 | 21 rule-based annotators<br>Zero-shot Chunker (medium) |
| clinical_deidentification_docwise_SingleStage_zeroshot_medium        | 33.1 sec         | 26 min 41 sec    | 0.92               | 0.91            | 0.92              | 0.87                  | 0.88               | 0.88                 | Zero-shot Chunker (medium) |
| clinical_deidentification_docwise_benchmark_large                    | 4 min 51 sec     | 2 h 10 min       | 0.90               | 0.97            | 0.94              | 0.88                  | 0.96               | 0.92                 | 21 rule-based annotators<br>3 NER + 1 Zero-shot (large) |
| clinical_deidentification_docwise_benchmark_large_v2                 | 3 min 46 sec     | 1 h 32 min       | 0.92               | 0.98            | 0.95              | 0.87                  | 0.94               | 0.91                 | 21 rule-based annotators<br>2 NER + Zero-shot Chunker |
| clinical_deidentification_docwise_zeroshot_large                     | 43.8 sec         | 1 h 18 min       | 0.93               | 0.97            | 0.95              | 0.87                  | 0.93               | 0.90                 | 21 rule-based annotators<br>Zero-shot Chunker (large) |
| clinical_deidentification_docwise_SingleStage_zeroshot_large         | 41.1 sec         | 1 h 15 min       | 0.93               | 0.95            | 0.94              | 0.88                  | 0.92               | 0.90                 | Zero-shot Chunker (large) |

This table reports end-to-end runtime and token-level precision, recall, and F1-score for the most up-to-date clinical de-identification pipelines.

This benchmark results also provide a clear foundation for understanding how modern clinical de-identification systems behave under realistic infrastructure and execution constraints.


- Deidentification Pipelines Speed Comparison on Databrics-AWS

    - Test Environment:
        - GPU Setup: Databricks - Worker Type: g4dn.2xlarge[T4] 32 GB Memory, 1 GPU, 8 Workers
        - CPU Setup: Databricks - Worker Type: m5d.2xlarge 32 GB Memory, 8 Cores, 8 Workers
    - Dataset Used: Dataset 4 for speed benchmark

    - CPU Runtime Comparison of Large, Medium and Optimized Pipelines

{:.table-model-big}
| Model |  Infrastructure | Runtime | Batch Size |
|-------|----------------:|--------:|-----------:|
| clinical_deidentification_docwise_benchmark_large_en | CPU  | 9h 23m 54s | 32 |
| clinical_deidentification_docwise_benchmark_medium_en | CPU  | 3h 7m 19s | 32 |
| clinical_deidentification_docwise_benchmark_optimized_en | CPU  | 26m 6s | 32 |

    - CPU & GPU Runtime Comparison of Medium Pipeline

{:.table-model-big}
| Model |  Infrastructure | Runtime | Batch Size |
|-------|----------------:|--------:|-----------:|
| clinical_deidentification_docwise_benchmark_medium_en | GPU  | 1h 2m 35s | 8 |
| clinical_deidentification_docwise_benchmark_medium_en | CPU  | 3h 7m 19s | 32 |

The findings emphasize that pipeline optimization yields greater performance gains than hardware scaling alone, while GPU resources provide additional, complementary speedups when applied to appropriately balanced pipeline configurations

- Pretrained Zero-Shot Named Entity Recognition (NER) Deidentification Subentity Speed Comparison on Databrics-AWS

    - Test Environment:
        - GPU Setup: Databricks - Worker Type: g4dn.2xlarge[T4] 32 GB Memory, 1 GPU, 8 Workers
        - CPU Setup: Databricks - Worker Type: m5d.2xlarge 32 GB Memory, 8 Cores, 8 Workers
    - Dataset Used: Dataset 4 for speed benchmark

    - Zero-shot Medium Model CPU & GPU Runtime Comparison

{:.table-model-big}
| Model | Infrastructure | Runtime | Batch Size |
|-------|---------------:|--------:|-----------:|
| zeroshot_ner_deid_subentity_merged_medium_en | CPU  | 2h 47m 24s | 32 |
| zeroshot_ner_deid_subentity_merged_medium_en | GPU  | 6m 26s | 32 |

    - Zero-shot Medium Model Batch Size Comparison via GPU Cluster

{:.table-model-big}
| Model | Infrastructure | Runtime | Batch Size |
|-------|---------------:|--------:|-----------:|
| zeroshot_ner_deid_subentity_merged_medium_en | GPU  | 6m 26s | 32 |
| zeroshot_ner_deid_subentity_merged_medium_en | GPU  | 12m 3s | 8 |

    - Zero-shot Medium & Large Models GPU Runtime Comparison

{:.table-model-big}
| Model | Infrastructure | Runtime | Batch Size |
|-------|---------------:|--------:|-----------:|
| zeroshot_ner_deid_subentity_merged_medium_en | GPU  | 12m 3s | 8 |
| zeroshot_ner_deid_subentity_merged_large_en | GPU  | 30m 23s | 8 |

The findings show that GPU usage is essential for production-scale runs, batch size optimization is critical for maximizing GPU efficiency, and model size should be selected based on the required balance between accuracy and runtime performance.

</div><div class="h3-box" markdown="1">

#### Comparative Medical Vision LLM Benchmark Results Against Leading Foundation Models

To provide a clear and comparative assessment of our Medical Vision LLMs, we report performance across a diverse set of **medical reasoning, safety, bias, and clinical knowledge benchmarks**, alongside leading proprietary foundation models.

These benchmarks evaluate capabilities spanning medical calculation, clinical QA, dialog understanding, hallucination resistance, bias robustness, and academic medical knowledge.


| **Benchmark** | **Gemini-2.5-Pro** | **Sonnet-4** | **JSL-MedicalVLM-30B** | **JSL-MedicalVLM-7B** |
|--------------|------------------:|------------:|----------------------:|---------------------:|
| MedCalc | 15.0 | 14.0 | 29.0 | 24.0 |
| MedBullets | 40.0 | 42.0 | 47.0 | 46.0 |
| ACI-Bench | 81.9 | 82.4 | 83.01 | 84.0 |
| MedicationQA | 72.56 | 72.4 | 76.8 | 77.1 |
| MedDialog | 75.1 | 75.3 | 77.1 | 77.5 |
| PubMedQA | 75.0 | 72.0 | 77.0 | 81.0 |
| RaceBias | 70.0 | 70.0 | 93.0 | 78.0 |
| MedHallu | 90.0 | 90.0 | 90.0 | 92.0 |
| College Biology | 95.0 | 98.6 | 99.3 | 92.4 |
| Medical Genetics | 95.0 | 94.0 | 95.0 | 93.0 |
| Average | **70.96** | **71.07** | **76.72** | **74.5** |


**Key takeaways**
- **JSL-MedicalVLM-30B** demonstrates strong and consistent performance across clinical reasoning, academic medical knowledge, and bias-sensitive evaluations, with particularly high scores in **RaceBias**, **College Biology**, and **Medical Genetics**.
- **JSL-MedicalVLM-7B** remains highly competitive relative to larger models, outperforming proprietary alternatives on multiple benchmarks while offering a more efficient deployment footprint.
- Both JSL MedicalVLM models show robust resistance to hallucinations and strong clinical dialog understanding, supporting their use in real-world medical and multimodal healthcare applications.

These results validate the reliability and clinical readiness of JSL Medical VLMs across a broad spectrum of medical evaluation tasks.

</div><div class="h3-box" markdown="1">


#### Advanced Clinical One-Liner Pretrained Pipelines for PHI Detection and Extraction

We introduce specialized pretrained pipelines designed specifically for Protected Health Information (PHI) detection and de-identification in clinical documents. These pipelines leverage state-of-the-art Named Entity Recognition (NER) models to automatically identify and extract sensitive medical information, ensuring compliance with healthcare privacy regulations.

Our de-identification pipelines eliminate the complexity of building custom PHI detection systems from scratch. Healthcare organizations and researchers can now deploy robust privacy protection measures with simple one-liner implementations, streamlining the process of sanitizing clinical documents while maintaining high accuracy standards.


{:.table-model-big}
| Model Name  |      Description            |
|-------------|-----------------------------|
| [`clinical_deidentification_docwise_benchmark_large_v2`](https://nlp.johnsnowlabs.com/2025/12/14/clinical_deidentification_docwise_benchmark_large_v2_en.html) | Mask and Obfuscate `DATE`, `LOCATION`, `PROFESSION`, `DOCTOR`, `EMAIL`, `PATIENT`, `URL`, `USERNAME`, `CITY`, `COUNTRY`, `DLN`, `HOSPITAL`, `IDNUM`, `MEDICALRECORD`, `STATE`, `STREET`, `ZIP`, `AGE`, `PHONE`, `ORGANIZATION`, `SSN`, `ACCOUNT`, `PLATE`, `VIN`, `LICENSE`, `IP` entities. |
| [`clinical_deidentification_docwise_benchmark_medium_v2`](https://nlp.johnsnowlabs.com/2025/12/14/clinical_deidentification_docwise_benchmark_medium_v2_en.html) | Mask and Obfuscate `DATE`, `LOCATION`, `PROFESSION`, `DOCTOR`, `EMAIL`, `PATIENT`, `URL`, `USERNAME`, `CITY`, `COUNTRY`, `DLN`, `HOSPITAL`, `IDNUM`, `MEDICALRECORD`, `STATE`, `STREET`, `ZIP`, `AGE`, `PHONE`, `ORGANIZATION`, `SSN`, `ACCOUNT`, `PLATE`, `VIN`, `LICENSE`, `IP` entities. |
| [`clinical_deidentification_docwise_benchmark_optimized_v2`](https://nlp.johnsnowlabs.com/2025/12/14/clinical_deidentification_docwise_benchmark_optimized_v2_en.html) | Mask and Obfuscate `NAME`, `DATE`, `LOCATION`, `PROFESSION`, `DOCTOR`, `EMAIL`, `PATIENT`, `URL`, `USERNAME`, `CITY`, `COUNTRY`, `DLN`, `HOSPITAL`, `IDNUM`, `MEDICALRECORD`, `STATE`, `STREET`, `ZIP`, `AGE`, `PHONE`, `ORGANIZATION`, `SSN`, `ACCOUNT`, `PLATE`, `VIN`, `LICENSE`, `IP` entities. |
| [`clinical_deidentification_docwise_zeroshot_large`](https://nlp.johnsnowlabs.com/2025/12/14/clinical_deidentification_docwise_zeroshot_large_en.html) | Mask and Obfuscate `DATE`, `PROFESSION`, `DOCTOR`, `EMAIL`, `PATIENT`, `URL`, `USERNAME`, `CITY`, `COUNTRY`, `DLN`, `HOSPITAL`, `IDNUM`, `MEDICALRECORD`, `STATE`, `STREET`, `ZIP`, `AGE`, `PHONE`, `ORGANIZATION`, `SSN`, `ACCOUNT`, `PLATE`, `VIN`, `LICENSE`, `IP` entities. |
| [`clinical_deidentification_docwise_zeroshot_medium`](https://nlp.johnsnowlabs.com/2025/12/14/clinical_deidentification_docwise_zeroshot_medium_en.html) | Mask and Obfuscate `DATE`, `PROFESSION`, `DOCTOR`, `EMAIL`, `PATIENT`, `URL`, `USERNAME`, `CITY`, `COUNTRY`, `DLN`, `HOSPITAL`, `IDNUM`, `MEDICALRECORD`, `STATE`, `STREET`, `ZIP`, `AGE`, `PHONE`, `ORGANIZATION`, `SSN`, `ACCOUNT`, `PLATE`, `VIN`, `LICENSE`, `IP` entities. |
| [`clinical_deidentification_docwise_SingleStage_zeroshot_large`](https://nlp.johnsnowlabs.com/2025/12/25/clinical_deidentification_docwise_SingleStage_zeroshot_large_en.html) | Mask and Obfuscate `DOCTOR`, `PATIENT`, `AGE`, `DATE`, `HOSPITAL`, `CITY`, `STREET`, `STATE`, `COUNTRY`, `PHONE`, `IDNUM`, `EMAIL`, `ZIP`, `ORGANIZATION`, `PROFESSION`, `USERNAME` entities. |
| [`clinical_deidentification_docwise_SingleStage_zeroshot_medium`](https://nlp.johnsnowlabs.com/2025/12/25/clinical_deidentification_docwise_SingleStage_zeroshot_medium_en.html) | Mask and Obfuscate `DOCTOR`, `PATIENT`, `AGE`, `DATE`, `HOSPITAL`, `CITY`, `STREET`, `STATE`, `COUNTRY`, `PHONE`, `IDNUM`, `EMAIL`, `ZIP`, `ORGANIZATION`, `PROFESSION`, `USERNAME` entities. |



*Example*:

```python
deid_pipeline = PretrainedPipeline("clinical_deidentification_docwise_zeroshot_medium", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)
```


*Result*:

{:.table-model-big}
| **text** | **result** | **result** |
|:---|:---|:---|
| Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024. The patient's medical record number is 56467890. The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 . | Dr. <DOCTOR>, from <HOSPITAL> in <CITY>, attended to the patient on <DATE>. The patient's medical record number is <IDNUM>. The patient, <PATIENT>, is <AGE>, her Contact number: <PHONE> . | Dr. Valerie Aho, from Mercy Hospital Aurora in Berea, attended to the patient on 05/07/2024. The patient's medical record number is 78689012. The patient, Johnathon Bunde, is 55 years old, her Contact number: 666-678-9012 . |



</div><div class="h3-box" markdown="1">

#### Enhanced 8 New Entity Resolver Models for Mapping Clinical Terms to Standardized UMLS CUI Codes and LOINC

These Entity Resolver models map clinical entities to standardized UMLS Concept Unique Identifiers (CUI) using `sbiobert_base_cased_mli` and `mpnet_embeddings_biolord_2023_c` sentence embeddings. Trained on the 2025AB UMLS Metathesaurus releases, they cover diverse semantic categories including diseases, syndromes, clinical drugs, pharmacologic substances, antibiotics, symptoms, procedures, clinical findings, anatomical structures, medical devices, and injuries & poisoning.
In addition to UMLS CUI mapping, we also introduce a model for mapping medical entities to Logical Observation Identifiers Names and Codes (LOINC), facilitating standardized representation of laboratory and clinical observations.

{:.table-model-big}
| Model Name  |      Description            |
|-------------|-----------------------------|
| [`sbiobertresolve_umls_findings`](https://nlp.johnsnowlabs.com/2025/12/18/sbiobertresolve_umls_findings_en.html) | Maps clinical findings to their corresponding UMLS CUI codes |
| [`sbiobertresolve_umls_clinical_drugs`](https://nlp.johnsnowlabs.com/2025/12/22/sbiobertresolve_umls_clinical_drugs_en.html) | Maps drug entities to UMLS CUI codes |
| [`sbiobertresolve_umls_disease_syndrome`](https://nlp.johnsnowlabs.com/2025/12/22/sbiobertresolve_umls_disease_syndrome_en.html) | Maps clinical entities(“Disease or Syndrome”) to UMLS CUI codes |
| [`sbiobertresolve_umls_drug_substance`](https://nlp.johnsnowlabs.com/2025/12/22/sbiobertresolve_umls_drug_substance_en.html) | Maps drug and substances to UMLS CUI codes |
| [`sbiobertresolve_umls_general_concepts`](https://nlp.johnsnowlabs.com/2025/12/22/sbiobertresolve_umls_general_concepts_en.html) | Maps clinical entities and concepts to the following 4 UMLS CUI code categories: `Disease`, `Symptom`, `Medication` and `Procedure` |
| [`sbiobertresolve_umls_major_concepts`](https://nlp.johnsnowlabs.com/2025/12/22/sbiobertresolve_umls_major_concepts_en.html) | Maps clinical entities and concepts to 4 major categories of UMLS CUI codes: `Clinical Findings`, `Medical Devices`, `Anatomical Structures`, `Injuries & Poisoning` terms |
| [`biolordresolve_umls_general_concepts`](https://nlp.johnsnowlabs.com/2025/12/23/biolordresolve_umls_general_concepts_en.html) | Maps clinical entities to 4 UMLS CUI code categories using mpnet_embeddings_biolord_2023_c embeddings: `Disease`, `Symptom`, `Medication`, and `Procedure` |
| [`sbiobertresolve_loinc`](https://nlp.johnsnowlabs.com/2026/01/08/sbiobertresolve_loinc_en.html) | Maps extracted medical entities to Logical Observation Identifiers Names and Codes (LOINC) |


*Example*:

```python
...
ner_model = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("posology_ner")

ner_model_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "posology_ner"])\
    .setOutputCol("posology_ner_chunk")\
    .setWhiteList(["DRUG"])

chunk2doc = Chunk2Doc().setInputCols("posology_ner_chunk").setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_clinical_drugs","en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages = [document_assembler, sentenceDetector, tokenizer, word_embeddings, ner_model, ner_model_converter, chunk2doc, sbert_embedder, resolver])

data = spark.createDataFrame([["""She was immediately given hydrogen peroxide 30 mg to treat the infection on her leg, and has been advised Neosporin Cream for 5 days. She has a history of taking magnesium hydroxide 100mg/1ml and metformin 1000 mg."""]]).toDF("text")
```


*Result*:

{:.table-model-big}
| ner_chunk                     | entity | umls_code | resolution                 | all_k_resolutions                                                                | all_k_results                                                                    | all_k_distances                                                                  | all_k_cosine_distances                                                           |
|-------------------------------|--------|-----------|----------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| hydrogen peroxide 30 mg       | DRUG   | C1126248  | hydrogen peroxide 30 mg/ml | hydrogen peroxide 30 mg/ml:::hydrogen peroxide solution 30%:::hydrogen peroxid... | C1126248:::C0304655:::C1605252:::C0304656:::C1154260:::C2242362:::C1724195:::... | 4.3731:::4.7154:::5.3302:::6.2122:::6.8675:::7.2770:::7.4682:::7.8312:::7.858... | 0.0323:::0.0369:::0.0483:::0.0649:::0.0807:::0.0890:::0.0957:::0.1018:::0.106... |
| Neosporin Cream               | DRUG   | C0132149  | neosporin cream            | neosporin cream:::neomycin sulfate cream:::neosporin topical ointment:::nasep... | C0132149:::C4722788:::C0704071:::C0698988:::C1252084:::C3833898:::C0698810:::... | 0.0000:::7.0688:::7.3112:::7.3482:::7.3820:::7.4605:::7.7285:::7.8918:::7.908... | 0.0000:::0.0888:::0.0953:::0.0934:::0.0964:::0.0941:::0.1052:::0.1113:::0.108... |
| magnesium hydroxide 100mg/1ml | DRUG   | C1134402  | magnesium hydroxide 100 mg | magnesium hydroxide 100 mg:::magnesium hydroxide 100 mg/ml:::magnesium sulph... | C1134402:::C1126785:::C4317023:::C4051486:::C4047137:::C1131100:::C1371187:::... | 4.9759:::5.1251:::5.8597:::6.5641:::6.5735:::6.8202:::6.8606:::6.9799:::7.007... | 0.0401:::0.0432:::0.0565:::0.0688:::0.0700:::0.0764:::0.0781:::0.0783:::0.079... |
| metformin 1000 mg             | DRUG   | C0987664  | metformin 1000 mg          | metformin 1000 mg:::metformin hydrochloride 1000 mg:::metformin hcl 1000mg ta... | C0987664:::C2719784:::C0978482:::C2719786:::C4282269:::C2719794:::C4282270:::... | 0.0000:::5.2988:::5.3783:::5.9071:::6.1034:::6.3066:::6.6597:::6.6626:::6.782... | 0.0000:::0.0445:::0.0454:::0.0553:::0.0586:::0.0632:::0.0698:::0.0707:::0.072... |




</div><div class="h3-box" markdown="1">

#### Introduced 17 New Rule-Based Entity Extraction Models for Identifying Structured Codes and Patterns in Clinical Texts

These rule-based extraction models identify structured entities and patterns within clinical texts using ContextualParser and RegexMatcherInternal annotators. The models cover a variety of entity types including ICD-10 codes, URLs, vehicle identification numbers (VIN), and other domain-specific patterns, enabling accurate extraction without requiring labeled training data.

{:.table-model-big}
| Model Name  |      Description            |
|-------------|-----------------------------|
| [`icd10_parser`](https://nlp.johnsnowlabs.com/2025/12/20/icd10_parser_en.html) | Extracts icd10 entities |
| [`account_parser`](https://nlp.johnsnowlabs.com/2025/12/21/account_parser_en.html) | Extracts account number entities |
| [`age_parser`](https://nlp.johnsnowlabs.com/2025/12/21/age_parser_en.html) | Extracts age entities |
| [`date_regex_matcher`](https://nlp.johnsnowlabs.com/2025/12/29/date_regex_matcher_en.html) | Extract date entities |
| [`dln_parser`](https://nlp.johnsnowlabs.com/2025/12/21/dln_parser_en.html) | Extracts drive license number entities |
| [`license_parser`](https://nlp.johnsnowlabs.com/2025/12/21/license_parser_en.html) | Extracts license number entities |
| [`phone_parser`](https://nlp.johnsnowlabs.com/2025/12/21/phone_parser_en.html) | Extracts phone number entities |
| [`plate_parser`](https://nlp.johnsnowlabs.com/2025/12/21/plate_parser_en.html) | Extracts plate number entities |
| [`ssn_parser`](https://nlp.johnsnowlabs.com/2025/12/21/ssn_parser_en.html) | Extracts SSN number entities |
| [`vin_parser`](https://nlp.johnsnowlabs.com/2025/12/21/vin_parser_en.html) | Extracts vehicle identifier number entities |
| [`cpt_parser`](https://nlp.johnsnowlabs.com/2025/12/22/cpt_parser_en.html) | Extracts cpt entities |
| [`email_regex_matcher`](https://nlp.johnsnowlabs.com/2025/12/22/email_regex_matcher_en.html) | Extracts emails |
| [`ip_regex_matcher`](https://nlp.johnsnowlabs.com/2025/12/22/ip_regex_matcher_en.html) | Extracts IPs |
| [`med_parser`](https://nlp.johnsnowlabs.com/2025/12/22/med_parser_en.html) | Extracts medical record entities |
| [`specimen_parser`](https://nlp.johnsnowlabs.com/2025/12/22/specimen_parser_en.html) | Extracts specimen entities |
| [`url_regex_matcher`](https://nlp.johnsnowlabs.com/2025/12/22/url_regex_matcher_en.html) | Extracts URLs |
| [`zip_regex_matcher`](https://nlp.johnsnowlabs.com/2025/12/29/zip_regex_matcher_en.html) | Extracts ZIP code entities |


*Example*:

```python
dln_contextual_parser = ContextualParserModel.pretrained("dln_parser","en","clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("chunk_dln")

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text ="""Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B. Driver's license# 12345678. MY DL# B324567 CDL bs34df45
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""
```


*Result*:

{:.table-model-big}
| chunk    |   begin |   end | label   |
|:---------|--------:|------:|:--------|
| A334455B |     271 |   278 | DLN     |
| 12345678 |     299 |   306 | DLN     |
| B324567  |     316 |   322 | DLN     |
| bs34df45 |     328 |   335 | DLN     |



</div><div class="h3-box" markdown="1">

#### Introduced 7 New NER Models for PHI Deidentification and Drug Entity Extraction

This release introduces 3 new NER models for clinical entity extraction. Two models focus on PHI (Protected Health Information) detection for deidentification: a generic model detecting broad entity types (DATE, NAME, LOCATION, ID, CONTACT, AGE, PROFESSION) and a subentity model with granular labels (PATIENT, DOCTOR, HOSPITAL, STREET, CITY, ZIP). The third model extracts drug entities by combining dosage, strength, form, and route into a unified Drug label.


{:.table-model-big}
| Model Name  |      Description            |
|-------------|-----------------------------|
| [`ner_deid_generic_nonMedical`](https://nlp.johnsnowlabs.com/2025/12/19/ner_deid_generic_nonMedical_en.html) | Model detects PHI entities such as DATE, NAME, LOCATION, ID, CONTACT, AGE, PROFESSION |
| [`ner_deid_subentity_nonMedical`](https://nlp.johnsnowlabs.com/2025/12/19/ner_deid_subentity_nonMedical_en.html) | Model detects PHI entities with granular labels such as PATIENT, DOCTOR, HOSPITAL, STREET, CITY, ZIP |
| [`ner_drugs_large_v2`](https://nlp.johnsnowlabs.com/2025/12/19/ner_drugs_large_v2_en.html) | Model combines dosage, strength, form, and route into a single entity: Drug |
| [`zeroshot_ner_deid_generic_nonMedical_large`](https://nlp.johnsnowlabs.com/2025/12/27/zeroshot_ner_deid_generic_nonMedical_large_en.html) | The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. |
| [`zeroshot_ner_deid_generic_nonMedical_medium`](https://nlp.johnsnowlabs.com/2025/12/28/zeroshot_ner_deid_generic_nonMedical_medium_en.html) | The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. |
| [`zeroshot_ner_deid_subentity_nonMedical_large`](https://nlp.johnsnowlabs.com/2025/12/28/zeroshot_ner_deid_subentity_nonMedical_large_en.html) | The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. |
| [`zeroshot_ner_deid_subentity_nonMedical_medium`](https://nlp.johnsnowlabs.com/2025/12/28/zeroshot_ner_deid_subentity_nonMedical_medium_en.html) | The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. |



*Example*:

```python
ner_model = MedicalNerModel.pretrained("ner_deid_generic_nonMedical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")


text = """
Mr. James Wilson is a 65-year-old male who presented to the emergency department at Boston General Hospital on 10/25/2023. 
He lives at 123 Oak Street, Springfield, IL 62704. He can be contacted at 555-0199. 
His SSN is 999-00-1234. Dr. Gregory House is the attending physician.
"""

data = spark.createDataFrame([[text]]).toDF("text")
```


*Result*:

{:.table-model-big}
|chunk                  |begin|end|ner_label|
|-----------------------|-----|---|---------|
|James Wilson           |5    |16 |NAME     |
|65-year-old            |23   |33 |AGE      |
|Boston General Hospital|85   |107|LOCATION |
|10/25/2023             |112  |121|DATE     |
|123 Oak Street         |137  |150|LOCATION |
|Springfield            |153  |163|LOCATION |
|IL                     |166  |167|LOCATION |
|555-0199               |199  |206|CONTACT  |
|999-00-1234            |221  |231|ID       |
|Gregory House          |238  |250|NAME     |


</div><div class="h3-box" markdown="1">

#### Enhanced 8 new contextual assertion models to classify clinical entities by assertion status

We introduced 8 new contextual assertion models that classify assertion context for clinical mentions—helping distinguish whether a condition applies to the patient, is denied, historical, conditional, hypothetical, planned, or attributed to someone else.

{:.table-model-big}
| Model Name  |      Description            |
|-------------|-----------------------------|
| [`contextual_assertion_absent`](https://nlp.johnsnowlabs.com/2026/01/14/contextual_assertion_absent_en.html) | Identifies medical conditions that are explicitly absent or denied in the patient |
| [`contextual_assertion_conditional`](https://nlp.johnsnowlabs.com/2026/01/14/contextual_assertion_conditional_en.html) | Identifies medical conditions that are conditional or dependent on certain circumstances |
| [`contextual_assertion_family`](https://nlp.johnsnowlabs.com/2026/01/14/contextual_assertion_family_en.html) | Identifies medical conditions that belong to family members rather than the patient |
| [`contextual_assertion_hypothetical`](https://nlp.johnsnowlabs.com/2026/01/14/contextual_assertion_hypothetical_en.html) | Identifies medical conditions mentioned in hypothetical or uncertain contexts |
| [`contextual_assertion_past`](https://nlp.johnsnowlabs.com/2026/01/14/contextual_assertion_past_en.html) | Identifies medical conditions that occurred in the patient's past medical history |
| [`contextual_assertion_planned`](https://nlp.johnsnowlabs.com/2026/01/14/contextual_assertion_planned_en.html) | Identifies medical procedures or treatments that are planned for the future |
| [`contextual_assertion_possible`](https://nlp.johnsnowlabs.com/2026/01/14/contextual_assertion_possible_en.html) | Identifies medical conditions that are possible or suspected but not confirmed |
| [`contextual_assertion_someoneelse`](https://nlp.johnsnowlabs.com/2026/01/14/contextual_assertion_someoneelse_en.html) | Identifies medical conditions that belong to someone other than the patient (not family) |



*Example*:

```python
contextual_assertion = ContextualAssertion\
    .pretrained("contextual_assertion_absent", "en", "clinical/models")\
    .setInputCols("sentence", "token", "ner_chunk")\
    .setOutputCol("assertion_absent")

text = """The patient denies any chest pain, shortness of breath, or fever. No history of diabetes or hypertension."""
data = spark.createDataFrame([[text]]).toDF('text')
```

*Result*:

{:.table-model-big}
|ner_chunk            |begin  |end  |ner_label  |result     |
|---------------------|-------|-----|-----------|-----------|
|any chest pain       |19     |32   |PROBLEM    |absent     |
|shortness of breath  |35     |53   |PROBLEM    |absent     |
|fever                |59     |63   |PROBLEM    |absent     |
|diabetes             |80     |87   |PROBLEM    |absent     |
|hypertension         |92     |103  |PROBLEM    |absent     |

</div><div class="h3-box" markdown="1">

#### Added new ONNX-based multilingual clinical NER models for Italian, Spanish, and Romanian, covering disease, procedure, medication, and symptom entity extraction

This release adds several new ONNX-exported NER models for multilingual clinical text mining, enabling faster and more efficient inference while extracting key medical entities from real-world clinical notes and records. The models cover Italian, Spanish, and Romanian medical text and support structured extraction of diseases, procedures, medications, and symptoms using BIO tagging.


{:.table-model-big}
| Model Name  |      Description            |
|-------------|-----------------------------|
| [`roberta_disease_ner_onnx`](https://nlp.johnsnowlabs.com/2025/12/26/roberta_disease_ner_onnx_en.html) | RoBERTa-based token classification model for identifying disease mentions in text |
| [`roberta_med_ner_onnx`](https://nlp.johnsnowlabs.com/2025/12/26/roberta_med_ner_onnx_en.html) | RoBERTa-based token classification model trained to identify medication mentions in clinical and biomedical text |
| [`roberta_procedure_ner_onnx`](https://nlp.johnsnowlabs.com/2025/12/27/roberta_procedure_ner_onnx_en.html) | RoBERTa-based token classification model for extracting symptom mentions from text |
| [`roberta_symptom_ner_onnx`](https://nlp.johnsnowlabs.com/2025/12/27/roberta_symptom_ner_onnx_en.html) | RoBERTa-based token classification model for extracting symptom mentions from text |
| [`vetclinical_bert_onnx`](https://nlp.johnsnowlabs.com/2025/12/29/vetclinical_bert_onnx_en.html) | Trained on large-scale real-world veterinary medical records, this model captures animal-health terminology and note structure to support accurate disease/syndrome classification, information extraction, and clinical text analysis |
| [`bert_token_classifier_disease_ner_it_onnx`](https://nlp.johnsnowlabs.com/2026/01/20/bert_token_classifier_disease_ner_it_onnx_it.html) | BERT-based NER model identifies disease mentions for Italian medical text |
| [`bert_token_classifier_medical_ner_it_onnx`](https://nlp.johnsnowlabs.com/2026/01/20/bert_token_classifier_medical_ner_it_onnx_it.html) | BERT-based NER model detects medication names for Italian medical text |
| [`bert_token_classifier_procedure_ner_it_onnx`](https://nlp.johnsnowlabs.com/2026/01/20/bert_token_classifier_procedure_ner_it_onnx_it.html) | BERT-based NER model identifies medical procedures for Italian medical text |
| [`roberta_disease_ner_es_onnx`](https://nlp.johnsnowlabs.com/2026/01/04/roberta_disease_ner_es_onnx_es.html) | BERT-based NER model identifies disease mentions for Spanish medical text |
| [`roberta_procedure_ner_es_onnx`](https://nlp.johnsnowlabs.com/2026/01/04/roberta_procedure_ner_es_onnx_es.html) | BERT-based NER model identifies medical procedures for Spanish medical text |
| [`roberta_symptom_ner_es_onnx`](https://nlp.johnsnowlabs.com/2026/01/04/roberta_symptom_ner_es_onnx_es.html) | BERT-based NER model identifies symptom mentions for Spanish medical text |
| [`xlmroberta_medical_ner_ro_onnx`](https://nlp.johnsnowlabs.com/2026/01/04/xlmroberta_medical_ner_ro_onnx_ro.html) | XLM-RoBERTa-based NER model identifies medication mentions for Romanian medical text |



*Example*:

```python
tokenClassifier = MedicalBertForTokenClassifier \
    .pretrained("bert_token_classifier_procedure_ner_it_onnx", "it", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("ner")

data = spark.createDataFrame([["Il paziente è stato sottoposto a risonanza magnetica e biopsia epatica."]]).toDF("text")
```



*Result*:

{:.table-model-big}
|text               |entity   |
|-------------------|---------|
|risonanza magnetica|PROCEDURE|
|biopsia epatica    |PROCEDURE|




</div><div class="h3-box" markdown="1">

#### New Blog Posts & Technical Deep Dives

- [From Clinical Text to Knowledge Graphs with John Snow Labs Healthcare NLP](https://medium.com/john-snow-labs/from-clinical-text-to-knowledge-graphs-with-john-snow-labs-healthcare-nlp-d4b9f62d13c7) This blog post shows how to build an end-to-end clinical knowledge graph from unstructured medical text using John Snow Labs Healthcare NLP library. We’ll start by extracting key clinical entities about medication with Named Entity Recognition, then connect them using Relation Extraction to capture medically meaningful links. Finally, we’ll convert these structured relationships into a knowledge graph that makes complex clinical narratives easier to search, analyze, and interpret.

- [Clinical De-Identification at Scale: Pipeline Design and Speed–Accuracy Trade-offs Across Infrastructures]( https://medium.com/john-snow-labs/clinical-de-identification-at-scale-pipeline-design-and-speed-accuracy-trade-offs-across-d77a4bbae6e0) This blog post presents a focused update on large-scale clinical de-identification benchmarks, emphasize pipeline design, execution strategy, and infrastructure-aware performance. Rather than treating accuracy as an isolated metric, we analyze how different pipeline architectures - rule-augmented NER, hybrid NER + zero-shot, and zero-shot–centric approaches - behave under realistic Google Colab and Databricks–AWS deployments.

</div><div class="h3-box" markdown="1">

#### Various core improvements, bug fixes, enhanced overall robustness and reliability of Healthcare NLP

- Improved Pipeline Tracer coverage by adding support for PretrainedZeroShotNERChunker (plus ChunkFilterer/CER/CEF) and correctly tracing AssertionMerger replaceDict behavior.
- Added replaceDict to AssertionMerger to allow custom replacement of assertion labels.
- PipelineOutputParser improvements to support mappings output in clinical_deidentification pipelines

</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Healthcare NLP Easier To Navigate And Understand
 
- New [CDA DeIdentification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.14.CDA_DeIdentification.ipynb) Notebook



</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.


+ `jsl_meds_vlm_7b_q4_v1_en`
+ `jsl_meds_vlm_7b_q8_v1_en`
+ `jsl_meds_vlm_7b_q16_v1_en`
+ `jsl_meds_vlm_4b_q4_v1_en`
+ `jsl_meds_vlm_4b_q8_v1_en`
+ `jsl_meds_vlm_4b_q16_v1_en`
+ `jsl_meds_vlm_reasoning_8b_q4_v1_en`
+ `jsl_meds_vlm_reasoning_8b_q8_v1_en`
+ `jsl_meds_vlm_reasoning_8b_q16_v1_en`
+ `clinical_deidentification_docwise_benchmark_large_v2`
+ `clinical_deidentification_docwise_benchmark_medium_v2`
+ `clinical_deidentification_docwise_benchmark_optimized_v2`
+ `clinical_deidentification_docwise_zeroshot_large`
+ `clinical_deidentification_docwise_zeroshot_medium`
+ `clinical_deidentification_docwise_SingleStage_zeroshot_large`
+ `clinical_deidentification_docwise_SingleStage_zeroshot_medium`          
+ `sbiobertresolve_umls_findings`
+ `sbiobertresolve_umls_clinical_drugs`
+ `sbiobertresolve_umls_disease_syndrome`
+ `sbiobertresolve_umls_drug_substance`
+ `sbiobertresolve_umls_general_concepts`
+ `sbiobertresolve_umls_major_concepts`
+ `biolordresolve_umls_general_concepts`
+ `sbiobertresolve_loinc`
+ `icd10_parser`
+ `account_parser`
+ `age_parser`
+ `date_regex_matcher`
+ `dln_parser`
+ `license_parser`
+ `phone_parser`
+ `plate_parser`
+ `ssn_parser`
+ `vin_parser`
+ `cpt_parser`
+ `email_regex_matcher`
+ `ip_regex_matcher`
+ `med_parser`
+ `specimen_parser`
+ `url_regex_matcher`
+ `zip_regex_matcher`
+ `ner_deid_generic_nonMedical`
+ `ner_deid_subentity_nonMedical`
+ `ner_drugs_large_v2`
+ `zeroshot_ner_deid_generic_nonMedical_large`
+ `zeroshot_ner_deid_generic_nonMedical_medium`
+ `zeroshot_ner_deid_subentity_nonMedical_large`
+ `zeroshot_ner_deid_subentity_nonMedical_medium`
+ `roberta_disease_ner_onnx`
+ `roberta_med_ner_onnx`
+ `roberta_procedure_ner_onnx`
+ `roberta_symptom_ner_onnx`
+ `vetclinical_bert_onnx`
+ `bert_token_classifier_disease_ner_it_onnx`
+ `bert_token_classifier_medical_ner_it_onnx`
+ `bert_token_classifier_procedure_ner_it_onnx`
+ `roberta_disease_ner_es_onnx`
+ `roberta_procedure_ner_es_onnx`
+ `roberta_symptom_ner_es_onnx`
+ `xlmroberta_medical_ner_ro_onnx`
+ `contextual_assertion_absent`
+ `contextual_assertion_conditional`
+ `contextual_assertion_family`
+ `contextual_assertion_hypothetical`
+ `contextual_assertion_past`
+ `contextual_assertion_planned`
+ `contextual_assertion_possible`
+ `contextual_assertion_someoneelse`



</div><div class="h3-box" markdown="1">

For all Healthcare NLP models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">


## Previous versions

</div>
{%- include docs-healthcare-pagination.html -%}
