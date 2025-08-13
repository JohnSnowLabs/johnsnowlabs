---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP v6.1.0 Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_6_1_0
key: docs-licensed-release-notes
modify_date: 2025-08-13
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 6.1.0

#### Highlights

We are delighted to announce remarkable enhancements and updates in our latest release of Healthcare NLP. **This release comes with a brand new Medical multimodal LLMs,text-only small LLMs that could run on commodity hardware, speed and performance optimizations for popular healthcare NLP tools (NER, assertion, etc.) via Onnx, as well as 37 new and updated clinical pretrained models and pipelines**. 

- **Medical Vision LLM module to run multiomodal LLMs**: Advancing clinical AI with integrated visual language understanding via popular multimodal LLMs specifically finetuned for medical tasks
- **Small size multimodal LLMs (VLMs) for text and visual entity extraction** — 6 newly released lightweight Vision Language Models for efficient structured medical entity extraction from documents and images
- **JSL Medical LLM Collection Expansion with recent popluar model families** — Addition of v4 and v5 models in 4B and 8B parameter sizes, available in q4, q8, and q16 quantization formats for optimal deployment flexibility
- **LLM Architecture Upgrade** — Refined architecture built on llama.cpp, delivering improved inference efficiency, scalability, and accuracy to support the latest generation of LLM families enabling faster performance and broader model compatibility
- **Continuous Performance Optimization & Benchmarking for Healthcare Modules** — Ongoing speed enhancements and comparative analysis of machine learning model architectures across CPU/GPU platforms
- **Mapper Model Additions** — 7 new medical terminology mapper models supporting HPO, gene, disease, and biomedical concept analysis
- **Pretrained Clinical Pipelines** — One-Liner, domain-specific pipelines for targeted clinical document analysis
- **Various core improvements** - Bug fixes, enhanced overall robustness and reliability of Healthcare NLP
  - **Model Size Display**: Added the ability to display the model size when using `pretrained` functions, providing better insight into resource requirements before loading.
  - **AssertionLogRegModel Enhancements**: Introduced new metadata fields to `AssertionLogRegModel`, aligning it with other assertion annotators and enabling improved traceability of processed chunks.
  - **DeIdentificationModel Save/Load Fix**: Resolved a persistence issue that affected saving and loading in `DeIdentificationModel`.
+ Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
    - New [Deidentification Model Evaluation](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.12.Deidentification_Model_Evaluation.ipynb) Notebook
    - New [Metadata Annotation Converter](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/MetadataAnnotationConverter.ipynb) MOOC Notebook
    - New [Multi Modal LLMs](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.1.Multi_Modal_LLMs.ipynb) Notebook
    - Updated [Chunk Mapping](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb) Notebook
    - Updated [Clinical Deidentification Improvement](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.4.Clinical_Deidentification_Improvement.ipynb) Notebook
    - Updated [Loading Medical and Open Souce LLMs](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb) Notebook
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will further elevate your experience with Spark NLP for Healthcare, delivering more efficient, accurate, and streamlined analysis of healthcare-related natural language data across a wide range of clinical and research applications.


</div><div class="h3-box" markdown="1">

#### **Medical Vision LLM Module to Run Multiomodal LLMs**: Advancing Clinical AI with Integrated Visual Language Understanding via Popular Multimodal LLMs Specifically Finetuned for Medical Tasks

We are introducing `MedicalVisionLLM`, a significant advancement in our model suite that extends large language model capabilities with integrated visual understanding. This annotator is designed to process and analyze multimodal data — combining textual and image inputs — enabling more comprehensive clinical analysis.
Leveraging the latest innovations in multimodal AI, MedicalVisionLLM can interpret medical images alongside corresponding clinical narratives, supporting more informed decision-making in healthcare workflows. With 9 newly released Vision-Language Models (VLMs), it offers robust performance for tasks such as diagnostic image interpretation, image-to-text summarization, and integrated clinical documentation analysis.

| **Model Name**             | **Quantization Options**   | **Description**   |
| -------------------------- | -------------------------- | ----------------- |
| JSL_MedS_VLM_3B_v1         | [q4](https://nlp.johnsnowlabs.com/2025/08/08/jsl_meds_vlm_3b_q4_v1_en.html), [q8](https://nlp.johnsnowlabs.com/2025/08/08/jsl_meds_vlm_3b_q8_v1_en.html), [q16](https://nlp.johnsnowlabs.com/2025/08/08/jsl_meds_vlm_3b_q16_v1_en.html) | Extract and link structured medical named entities |
| JSL_MedS_VLM_2B_v1         | [q4](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q4_v1_en.html), [q8](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q8_v1_en.html), [q16](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q16_v1_en.html) | Extract and link structured medical named entities |
| JSL_MedS_VLM_2B_v2         | [q4](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q4_v2_en.html), [q8](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q8_v2_en.html), [q16](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q16_v2_en.html) | Extract and link structured medical named entities |

*Example*:

```python
prompt = """Extract demographics, clinical disease and medication informations"""

input_df = vision_llm_preprocessor(
    spark=spark,
    images_path="./images",
    prompt=prompt,
    output_col_name="prompt"
)

document_assembler = DocumentAssembler()\
    .setInputCol("prompt")\
    .setOutputCol("document")

image_assembler = ImageAssembler()\
    .setInputCol("image")\
    .setOutputCol("image_assembler")

medical_vision_llm = MedicalVisionLLM.pretrained("jsl_meds_vlm_3b_q4_v1", "en", "clinical/models")\
    .setInputCols(["document", "image_assembler"])\
    .setOutputCol("completions")\
    .setChatTemplate("vicuna")\
    .setBatchSize(4)\
    .setNPredict(-1)\
    .setTemperature(0)\
    .setNGpuLayers(99)\

pipeline = Pipeline(
    stages = [
        document_assembler,
        image_assembler,
        medical_vision_llm
])
```

input:

![Input of Medical Vision LLM](/assets/images/releases/6_1_0/medical_visual_llm.png)

*Result*:

```bash
{
    "Prescription Date": "2023-08-30",
    "Diagnosis": "Malaria",
    "Medicine Name": "TAB. ABCIXIMAB",
    "Dosage": "1 Morning",
    "Duration": "4 Days",
    "Follow-up Date": "2023-09-04",
    "Doctor Name": "Dr. Akshara",
    "Hospital Name": "SMS hospital"
}
```



  


Please check the [Multi Modal LLMs](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.1.Multi_Modal_LLMs.ipynb) Notebook


</div><div class="h3-box" markdown="1">

####  **Small Size Multimodal LLMs (VLMs) for Text and Visual Entity Extraction** — 6 Newly Released Lightweight Vision Language Models for Efficient Structured Medical Entity Extraction from Documents and Images

These small language models (LLMs) are trained to extract and link medical entities within a document. Users need to define an input schema, as explained in the example section. For instance, a drug field can be defined as a list to indicate that there may be multiple drugs in the document, and the model should extract all of them. Each drug has properties such as name and reaction. Since name contains only a single value, it is defined as a string, whereas reaction may include multiple values and is therefore defined as a list. Similarly, users can define any schema for any type of entity, allowing the model’s output to be structured according to specific requirements.

Also this same model family can extract entities given an image. 

**Example usage for text-only contents**

{:.table-model-big}
| Model Name         |Model Links|
|--------------------|-----------|
| JSL_MedS_VLM_2B_v1 | [q4](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q4_v1_en.html), [q8](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q8_v1_en.html), [q16](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q16_v1_en.html) | Extract and link structured medical named entities |
| JSL_MedS_VLM_2B_v2 | [q4](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q4_v2_en.html), [q8](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q8_v2_en.html), [q16](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q16_v2_en.html) | Extract and link structured medical named entities |


*Example*:

```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

medical_llm = MedicalLLM.pretrained("jsl_meds_ner_vlm_2b_q8_v1", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(100)\
    .setUseChatTemplate(True)\
    .setTemperature(0)

pipeline = Pipeline(
    stages = [
        document_assembler,
        medical_llm
])

med_ner_prompt = """
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

data = spark.createDataFrame([[med_ner_prompt]]).toDF("text")

results = pipeline.fit(data).transform(data)

results.select("completions").show(truncate=False)
```

*Result*:

```bash
{'drugs': [
    {
        'name': 'Arthrotec 50',
        'reactions': [
              'drowsy', 
              'blurred vision', 
              'gastric problems'
          ]
    },
    {
        'name': 'Gp 75', 
        'reactions': [
            'pains almost gone', 
            'weird'
        ]
    }]    
}
```



**Example usage for documents (PDFs, Word, Excel, PowerPoint, HTML, Text, Email, Markdown)**

Extracting structured medical entities from various document types. The workflow supports end-to-end PDF processing:

- Read PDFs with Reader2Doc to convert content into plain text.
- Add a custom prompt template with custom_llm_preprocessor_converter to define your desired entity schema.
- Run the VLM with MedicalLLM to extract and link entities according to the schema.

The result is a precise, structured NER output that works for both text-only and multimodal (text + image) content, enabling efficient integration into clinical data pipelines while keeping models small and inference fast.


Please check the [Loading Medical and Open-Source LLMs](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb) Notebook


</div><div class="h3-box" markdown="1">

####  **JSL Medical LLM Collection Expansion with Recent Popluar Model Families** — Addition of v4 and v5 Models in 4B and 8B Parameter Sizes, Available in q4, q8, and q16 Quantization Formats for Optimal Deployment Flexibility

The JSL_MedS LLM Collection is a set of advanced transformer-based medical language models developed by John Snow Labs, purpose-built for high-performance clinical NLP tasks such as question answering (Q&A), summarization, Retrieval-Augmented Generation (RAG), and medical chatbot interactions.
This release expands the collection with 9 new models, spanning two major versions (v4 and v5), two parameter sizes (4B and 8B), and three quantization levels (q4, q8, q16) to meet diverse requirements for speed, memory efficiency, and latency. Each model is optimized for accurate, context-aware understanding of clinical text, supporting use cases such as real-time doctor–patient conversation assistance, summarizing lengthy patient histories, and extracting insights from medical literature or electronic health records (EHRs). The availability of quantized variants ensures deployment flexibility — from high-performance GPU clusters to resource-constrained environments.

{:.table-model-big}
| Model Name            |            |
|-----------------------|------------|
| `jsl_meds_4b_v4` | [q16](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_4b_q16_v4_en.html), [q8](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_4b_q8_v4_en.html), [q4](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_4b_q4_v4_en.html)   |
| `jsl_meds_4b_v5` | [q16](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_4b_q16_v5_en.html), [q8](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_4b_q8_v5_en.html), [q4](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_4b_q4_v5_en.html)   |
| `jsl_meds_8b_v4` | [q16](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_8b_q16_v4_en.html), [q8](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_8b_q8_v4_en.html), [q4](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_8b_q4_v4_en.html)   |


*Example:*

```python
medical_llm = medical.MedicalLLM.pretrained("jsl_meds_4b_q16_v5", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(100)\
    .setUseChatTemplate(True)\
    .setTemperature(0)

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    medical_llm
])

prompt = """
A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus.
Which of the following is the best treatment for this patient?
A: Ampicillin
B: Ceftriaxone
C: Ciprofloxacin
D: Doxycycline
E: Nitrofurantoin
"""
```

*Result*:

```bash
The patient presents with symptoms suggestive of a urinary tract infection (UTI) during pregnancy. Given the gestational age (22 weeks), the most appropriate treatment option is E: Nitrofurantoin.
```


</div><div class="h3-box" markdown="1">

#### **LLM Architecture Upgrade** — Refined Architecture Built on llama.cpp, Delivering Improved Inference Efficiency, Scalability, and Accuracy to Support the Latest Generation of LLM Families Enabling Faster Performance and Broader Model Compatibility

The Large Language Model (LLM) architecture in Spark NLP for Healthcare has been upgraded to support the latest generation of LLM families, ensuring full compatibility with cutting-edge medical and general-purpose language models.

---
**🚀Key Improvements**
- **Optimized LLM Inference Performance** — Achieves approximately **~10% faster inference** on GPU for both `MedicalLLM` and `LLMLoader`, enhancing throughput in production environments.
- **Extended LLM Compatibility** — Adds support for the **newest LLM architectures**, enabling seamless integration with state-of-the-art models for advanced healthcare NLP applications.
---

**Impact:**  
These improvements ensure faster and more scalable deployment of LLM-based healthcare NLP pipelines, while also allowing teams to leverage the **latest advancements in large language model research** without sacrificing performance.


</div><div class="h3-box" markdown="1">

#### - **Continuous Performance Optimization & Benchmarking for Healthcare Modules** — Ongoing Speed Enhancements and Comparative Analysis of Machine Learning Model Architectures Across CPU/GPU Platforms

To evaluate the performance of different model architectures available in healthcare library, we benchmarked **TensorFlow**, **ONNX**, and **OpenVINO** implementations of the same model under identical conditions.  
Tests were run on both **CPU** and **GPU** with the same input dataset and batch configurations to ensure a fair comparison.

---
- Test Environment:
  + Instance Type:
    - CPU: Colab V6e-1 TPU, 173.0 GB RAM, 44 CPUs
    - GPU: Colab A100, 83.5 GB RAM, 40.0 GB GPU RAM, 12 Cores
  + Datasets:
    - 1000 rows MTSamples dataset (~500 tokens per row)
---

     🖥 CPU Performance

| Component                | TensorFlow | ONNX    | OpenVINO |
|--------------------------|------------|---------|----------|
| `BertSentenceEmbeddings` | 8 min 37 s | 4 min 46 s | 3 min 31 s |

---

    ⚡ GPU Performance:

| Component                | TensorFlow | ONNX    | OpenVINO |
|--------------------------|------------|---------|----------|
| `BertSentenceEmbeddings` | 28 min 50 s | 11.4 s  | 18 min 49 s |

---

**Notes:**
- ONNX consistently outperformed TensorFlow in both CPU and GPU tests, with **massive gains on GPU**.
- OpenVINO delivered the **fastest CPU performance**, but was slower than ONNX on GPU.
- All measurements were taken on the same hardware, with warm-up runs to avoid cold-start effects.

---

*Future Direction:*

Based on these benchmark results, future releases will **focus more on ONNX and OpenVINO model architectures**.  
These formats demonstrated **significant performance improvements** over TensorFlow, especially ONNX on GPU and OpenVINO on CPU.  
Our aim is to expand model coverage, add optimized pipelines, and ensure maximum compatibility with hardware acceleration backends.


</div><div class="h3-box" markdown="1">

####  **Mapper Model Additions** — 7 New Medical Terminology Mapper Models Supporting HPO, Gene, Disease, and Biomedical Concept Analysis

These 7 ChunkMapper models act as fast, lightweight lookup layers between key biomedical vocabularies—genes, diseases, Human Phenotype Ontology (HPO) terms, extra-ocular-movement (EOM) phenotypes, and UMLS concepts. 

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`gene_disease_mapper`](https://nlp.johnsnowlabs.com/2025/07/28/gene_disease_mapper_en.html) | Maps genes to their related diseases |
| [`gene_hpo_code_mapper`](https://nlp.johnsnowlabs.com/2025/07/28/gene_hpo_code_mapper_en.html) | Maps genes to their corresponding HPO codes |
| [`hpo_code_eom_mapper`](https://nlp.johnsnowlabs.com/2025/07/28/hpo_code_eom_mapper_en.html) | Maps HPO codes to their related extraocular movements (EOM) |
| [`hpo_code_gene_mapper`](https://nlp.johnsnowlabs.com/2025/07/28/hpo_code_gene_mapper_en.html) | Maps HPO codes to related genes |
| [`hpo_umls_mapper`](https://nlp.johnsnowlabs.com/2025/07/28/hpo_umls_mapper_en.html) | Maps HPO codes to corresponding UMLS codes |
| [`umls_hpo_mapper`](https://nlp.johnsnowlabs.com/2025/07/28/umls_hpo_mapper_en.html) | Maps UMLS codes to corresponding HPO codes |
| [`hpo_code_gene_disease_mapper`](https://nlp.johnsnowlabs.com/2025/08/05/hpo_code_gene_disease_mapper_en.html) | Maps HPO codes to their associated genes and further maps those genes to related diseases |


*Example*:

```python
mapperModel = ChunkMapperModel.pretrained("gene_disease_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["disease"])

model = nlp_pipeline.fit(spark.createDataFrame([['']]).toDF("text"))
result = model.transform(spark.createDataFrame([["We will systematically examine seven genes (CHN1, MDH1, and SNAP25) that are altered in the three neurodegenerative diseases."]]).toDF("text"))
```

*Result*:

{:.table-model-big}
|  gene| disease| all_k_resolutions|
|------|--------|----------------------------------------|
|  CHN1|preaxial hand polydactyly|preaxial hand polydactyly:::brachydactyly:::marcus gunn jaw winking synkinesis:::triphalangeal thumb:::duane anomaly:::seizure:::global developmental delay:::irregular hyperpigmentation:::ectopic k...|
|  MDH1|        hyperglutamatemia|hyperglutamatemia:::hypertonia:::seizure:::global developmental delay:::infra-orbital crease:::hypsarrhythmia:::partial agenesis of the corpus callosum:::autosomal recessive inheritance:::axial hyp...|
|SNAP25|              poor speech|poor speech:::poor head control:::proximal muscle weakness:::motor delay:::gait disturbance:::bulbar palsy:::areflexia:::seizure:::hypotonia:::ataxia:::intellectual disability:::hyporeflexia:::dysa...|





</div><div class="h3-box" markdown="1">

#### **Pretrained Clinical Pipelines** — One Liner, Domain Specific Pipelines for Targeted Clinical Document Analysis

This release introduces a suite of advanced, hybrid pretrained pipelines purpose-built to streamline clinical document analysis. Each pipeline integrates multiple state-of-the-art (SOTA) pretrained models, providing a ready-to-use solution for extracting key clinical information with minimal setup.

A key advantage of these pipelines is the removal of the complexity traditionally involved in building and chaining models manually. Users no longer need to experiment with different model combinations or invest time in constructing intricate workflows from scratch. Instead, these one-liner pipelines offer a seamless, efficient, and reliable approach — enabling rapid deployment for targeted clinical tasks and concepts while maintaining high accuracy and performance.

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`hpo_mapper_pipeline_v3`](https://nlp.johnsnowlabs.com/2025/08/07/hpo_mapper_pipeline_v3_en.html) | Designed to extract phenotype-related entities from clinical or biomedical text, map them to their corresponding Human Phenotype Ontology (HPO) codes, and determine their assertion status |
| [`ner_docwise_benchmark_medium`](https://nlp.johnsnowlabs.com/2025/07/31/ner_docwise_benchmark_medium_en.html) | This pipeline can be used to extract PHI information such as ‘CONTACT’, ‘DATE’, ‘ID’, ‘LOCATION’, ‘PROFESSION’, ‘DOCTOR’, ‘EMAIL’, ‘PATIENT’, ‘URL’, ‘USERNAME’, ‘CITY’, ‘COUNTRY’, ‘DLN’, ‘HOSPITAL’, ‘IDNUM’, ‘LOCATION_OTHER’, ‘MEDICALRECORD’, ‘STATE’, ‘STREET’, ‘ZIP’, ‘AGE’, ‘PHONE’, ‘ORGANIZATION’, ‘SSN’, ‘ACCOUNT’, ‘PLATE’, ‘VIN’, ‘LICENSE’, and ‘IP’ entities. |
| [`ner_docwise_benchmark_large`](https://nlp.johnsnowlabs.com/2025/07/31/ner_docwise_benchmark_large_en.html) | This pipeline can be used to extract PHI information such as ‘CONTACT’, ‘DATE’, ‘ID’, ‘LOCATION’, ‘PROFESSION’, ‘DOCTOR’, ‘EMAIL’, ‘PATIENT’, ‘URL’, ‘USERNAME’, ‘CITY’, ‘COUNTRY’, ‘DLN’, ‘HOSPITAL’, ‘IDNUM’, ‘LOCATION_OTHER’, ‘MEDICALRECORD’, ‘STATE’, ‘STREET’, ‘ZIP’, ‘AGE’, ‘PHONE’, ‘ORGANIZATION’, ‘SSN’, ‘ACCOUNT’, ‘PLATE’, ‘VIN’, ‘LICENSE’, and ‘IP’ entities. |
| [`clinical_deidentification_docwise_benchmark_medium`](https://nlp.johnsnowlabs.com/2025/07/31/clinical_deidentification_docwise_benchmark_medium_en.html) | This pipeline can be used to extract PHI information such as ‘CONTACT’, ‘DATE’, ‘ID’, ‘LOCATION’, ‘PROFESSION’, ‘DOCTOR’, ‘EMAIL’, ‘PATIENT’, ‘URL’, ‘USERNAME’, ‘CITY’, ‘COUNTRY’, ‘DLN’, ‘HOSPITAL’, ‘IDNUM’, ‘LOCATION_OTHER’, ‘MEDICALRECORD’, ‘STATE’, ‘STREET’, ‘ZIP’, ‘AGE’, ‘PHONE’, ‘ORGANIZATION’, ‘SSN’, ‘ACCOUNT’, ‘PLATE’, ‘VIN’, ‘LICENSE’, and ‘IP’ entities. |
| [`clinical_deidentification_docwise_benchmark_large`](https://nlp.johnsnowlabs.com/2025/07/25/clinical_deidentification_docwise_benchmark_large_en.html) | This pipeline can be used to extract PHI information such as ‘CONTACT’, ‘DATE’, ‘ID’, ‘LOCATION’, ‘PROFESSION’, ‘DOCTOR’, ‘EMAIL’, ‘PATIENT’, ‘URL’, ‘USERNAME’, ‘CITY’, ‘COUNTRY’, ‘DLN’, ‘HOSPITAL’, ‘IDNUM’, ‘LOCATION_OTHER’, ‘MEDICALRECORD’, ‘STATE’, ‘STREET’, ‘ZIP’, ‘AGE’, ‘PHONE’, ‘ORGANIZATION’, ‘SSN’, ‘ACCOUNT’, ‘PLATE’, ‘VIN’, ‘LICENSE’, and ‘IP’ entities. |



*Example*:

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("hpo_mapper_pipeline_v3", "en", "clinical/models")

result = pipeline.fullAnnotate("""APNEA: Presumed apnea of prematurity since < 34 wks gestation at birth.
HYPERBILIRUBINEMIA: At risk for hyperbilirubinemia d/t prematurity.
1/25-1/30: Received Amp/Gent while undergoing sepsis evaluation.
Mother is A+, GBS unknown, and infant delivered
for decreasing fetal movement and preeclampsia.
Long finger and toes detected.
he has a increased overbite expression.
""")
```

*Result*:

{:.table-model-big}
|           matched_text|                ner_chunk|begin|end|assertion|  hpo_code|                                                                                                                                            hpo_parent|umls_mapping|         eom_mapping|                                                                                                                                          gene_disease|
|-----------------------|-------------------------|-----|---|---------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------|------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
|      apnea prematurity|     apnea of prematurity|   16| 35|  present|HP:0034236|HP:0002104: Apnea ## Lack of breathing with no movement of the respiratory muscles and no exchange of air in the lungs. This term refers to a dispo...|        NONE|                NONE|                                                                                                                                                  NONE|
|     hyperbilirubinemia|       hyperbilirubinemia|  104|121|  present|HP:0002904|HP:0033479: Abnormal circulating bilirubin concentration ##  => HP:0010995: Abnormal circulating dicarboxylic acid concentration ## A dicarboxylic ...|    C1142335|                NONE|{"ADK": ["poor speech", "seizure", "hypotonia", "increased csf methionine concentration", "hepatic steatosis", "cholestasis", "muscle weakness", "a...|
|                 sepsis|                   sepsis|  186|191|  present|HP:0100806|HP:0010978: Abnormality of immune system physiology ## A functional abnormality of the immune system. => HP:0002715: Abnormality of the immune syst...|        NONE|                NONE|{"ABCA3": ["honeycomb lung", "ground-glass opacification", "nonspecific interstitial pneumonia", "bronchial wall thickening", "sepsis", "clubbing",...|
|decrease fetal movement|decreasing fetal movement|  257|281|  present|HP:0001558|HP:0001557: Prenatal movement abnormality ## Fetal movements generally become apparent during the second trimester of pregnancy around the 20th wee...|        NONE|                NONE|{"AARS1": ["distal muscle weakness", "limb dystonia", "bilateral sensorineural hearing impairment", "abnormality of prenatal development or birth",...|
|           preeclampsia|             preeclampsia|  287|298|  present|HP:0100602|HP:0100603: Toxemia of pregnancy ## Pregnancy-induced toxic reactions of the mother that can be as harmless as slight Maternal hypertension or as l...|        NONE|                NONE|{"SLC25A20": ["reduced circulating 6-pyruvoyltetrahydropterin synthase activity", "reduced tissue carnitine-acylcarnitine translocase activity", "e...|
|            Long finger|              Long finger|  301|311|  present|HP:0100807|HP:0001167: Abnormal finger morphology ## An anomaly of a finger. => HP:0001155: Abnormality of the hand ## An abnormality affecting one or both ha...|        NONE|EOM:41535e8ed3dc9076|{"BIN1": ["distal muscle weakness", "exercise-induced myalgia", "proximal muscle weakness", "generalized amyotrophy", "generalized hypotonia", "lon...|
|     increased overbite|       increased overbite|  341|358|  present|HP:0011094|HP:0000692: Tooth malposition ## Abnormal alignment, positioning, or spacing of the teeth, i.e., misaligned teeth. => HP:0000164: Abnormality of th...|        NONE|                NONE|{"EP300": ["adducted thumb", "syndactyly", "trichiasis", "simple ear", "spina bifida", "sporadic", "panic attack", "generalized hypotonia", "agenes...|


</div><div class="h3-box" markdown="1">

#### **Various core improvements** - Bug fixes, enhanced overall robustness and reliability of Healthcare NLP

- **Model Size Display**: Added the ability to display the model size when using `pretrained` functions, providing better insight into resource requirements before loading.
- **AssertionLogRegModel Enhancements**: Introduced `ner_chunk`, `ner_label`, and `confidence` metadata fields  to `AssertionLogRegModel`, aligning it with other assertion annotators and enabling improved traceability of processed chunks.
- **DeIdentificationModel Save/Load Fix**: Resolved a persistence issue that affected saving and loading in `DeIdentificationModel`, ensuring models can be reliably saved and restored without loss of functionality.

</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [Deidentification Model Evaluation](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.12.Deidentification_Model_Evaluation.ipynb) Notebook
- New [Metadata Annotation Converter](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/MetadataAnnotationConverter.ipynb) MOOC Notebook
- New [Multi Modal LLMs](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.1.Multi_Modal_LLMs.ipynb) Notebook
- Updated [Chunk Mapping](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb) Notebook
- Updated [Clinical Deidentification Improvement](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.4.Clinical_Deidentification_Improvement.ipynb) Notebook
- Updated [Loading Medical and Open Souce LLMs](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb) Notebook

</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `jsl_meds_vlm_2b_q16_v1`
+ `jsl_meds_vlm_2b_q8_v1`
+ `jsl_meds_vlm_2b_q4_v1`
+ `jsl_meds_vlm_2b_q16_v2`
+ `jsl_meds_vlm_2b_q8_v2`
+ `jsl_meds_vlm_2b_q4_v2`
+ `jsl_meds_4b_q16_v4`
+ `jsl_meds_4b_q8_v4`
+ `jsl_meds_4b_q4_v4`
+ `jsl_meds_4b_q16_v5`
+ `jsl_meds_4b_q8_v5`
+ `jsl_meds_4b_q4_v5`
+ `jsl_meds_8b_q16_v4`
+ `jsl_meds_8b_q8_v4`
+ `jsl_meds_8b_q4_v4`
+ `jsl_meds_vlm_3b_q16_v1`
+ `jsl_meds_vlm_3b_q8_v1`
+ `jsl_meds_vlm_3b_q4_v1`
+ `jsl_meds_vlm_2b_q16_v1`
+ `jsl_meds_vlm_2b_q8_v1`
+ `jsl_meds_vlm_2b_q4_v1`
+ `jsl_meds_vlm_2b_q16_v2`
+ `jsl_meds_vlm_2b_q8_v2`
+ `jsl_meds_vlm_2b_q4_v2`
+ `gene_disease_mapper`
+ `gene_hpo_code_mapper`
+ `hpo_code_eom_mapper`
+ `hpo_code_gene_mapper`
+ `hpo_umls_mapper`
+ `umls_hpo_mapper`
+ `hpo_code_gene_disease_mapper`
+ `hpo_mapper_pipeline_v3`
+ `ner_docwise_benchmark_medium`
+ `ner_docwise_benchmark_large`
+ `clinical_deidentification_docwise_benchmark_medium`
+ `clinical_deidentification_docwise_benchmark_large`


</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">

## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
