---
layout: docs
header: true
seotitle: Medical Small LLMs| John Snow Labs
title: Medical Small LLMs 
permalink: /docs/en/LLMs/medical_small_llm
key: docs-medical-llm
modify_date: "2026-11-19"
show_nav: true
sidebar:
    nav: medical-llm
---

<div class="h3-box" markdown="1">

John Snow Labs offers a curated portfolio of **specialized small language models (1B-10B parameters), alongside larger, more capable models**. Designed for real-world deployment, these models are **quantized for efficiency and can run on standard CPU-based hardware without requiring a GPU**, while also supporting GPU acceleration for improved performance. They integrate seamlessly with the **Healthcare NLP library**, just like any other component, and are fully included under the **Healthcare NLP license**.

{:.table-model-big.db}
| Model Name   | Disk Size   | Model Size | Modality   | Available quantizations | GPU Memory <br> Required | Token/sec | Max Context <br> Window | Tasks |
| ------------ | ----------- | ---------- | ---------- | ------------------------| ------------------------ | --------- | ----------------------- | ----- |
| JSL_MedM_v3            | [8.2G, 14G, 21.9G]  | 14B        | text-only  | [[q4](https://nlp.johnsnowlabs.com/2024/10/06/jsl_medm_q4_v3_en.html), [q8](https://nlp.johnsnowlabs.com/2024/10/08/jsl_medm_q8_v3_en.html), [q16](https://nlp.johnsnowlabs.com/2024/10/23/jsl_medm_q16_v3_en.html)]                                  | 24GB                | [79, 84, 253]      | 32,768             | Summarization, Q&A, RAG, and Chat |
| JSL_MedS_v3            | [2.2G, 3.7G, 5.6G]  | 3.5B       | text-only  | [[q4](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_q4_v3_en.html), [q8](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_q8_v3_en.html), [q16](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_q16_v3_en.html)]                                  | 10GB                | [28.5, 18.7, 50.2] | 131,072            | Summarization, Q&A, RAG |
| JSL_MedS_4B_v5         | [2.4G, 4.0G, 6.1G]  | 4B         | text-only  | [[q4](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_4b_q4_v5_en.html), [q8](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_4b_q8_v5_en.html), [q16](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_4b_q16_v5_en.html)]                         | 16GB                | [40, 32, 95]       | 32,768             | Summarization, Q&A, RAG |
| JSL_MedS_8B_v4         | [4.6G, 7.8G, 12.2G] | 8B         | text-only  | [[q4](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_8b_q4_v4_en.html), [q8](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_8b_q8_v4_en.html), [q16](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_8b_q16_v4_en.html)]                         | 16GB                | [83, 84, 272]      | 32,768             | Summarization, Q&A, RAG |
| JSL_MedS_NER_v4        | [2.2G, 3.7G, 6.0]   | 3.5B       | text-only  | [[q4](https://nlp.johnsnowlabs.com/2025/07/01/jsl_meds_ner_q4_v4_en.html), [q8](https://nlp.johnsnowlabs.com/2025/07/01/jsl_meds_ner_q8_v4_en.html), [q16](https://nlp.johnsnowlabs.com/2025/07/01/jsl_meds_ner_q16_v4_en.html)]                      | 10GB                | [28.5, 18.7]       | 131,072            | Extract and link medical named entities |
| JSL_MedS_NER_v5        | 6.0G                | 3.5B       | text-only  | [q16](https://nlp.johnsnowlabs.com/2026/04/09/jsl_meds_ner_q16_v5_en.html)                                                                                                                                                                            | 10GB                | —                  | 131,072            | Clinical trial eligibility parsing |
| JSL_MedS_RAG_v1        | [2.2G, 3.7G, 5.6G]  | 3B         | text-only  | [[q4](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_rag_q4_v1_en.html), [q8](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_rag_q8_v1_en.html), [q16](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_rag_q16_v1_en.html)]                      | 10GB                | [30, 20, 53]       | 32,768             | LLM component of Retrieval Augmented Generation (RAG) |
| JSL_MedS_Text2SOAP_v1  | 2.2G                | 3B         | text-only  | [base](https://nlp.johnsnowlabs.com/2025/04/09/jsl_meds_text2soap_v1_en.html) | 10GB                | 53                 | 32,768             | Generate structured SOAP (Subjective, Objective, Assessment, Plan) summaries |
| JSL_MedS_VLM_3B_v1     | [2.5G, 3.6G, 5.6G]  | 3B         | multimodal | [[q4](https://nlp.johnsnowlabs.com/2025/08/08/jsl_meds_vlm_3b_q8_v1_en.html), [q8](https://nlp.johnsnowlabs.com/2025/08/08/jsl_meds_vlm_3b_q4_v1_en.html), [q16](https://nlp.johnsnowlabs.com/2025/08/08/jsl_meds_vlm_3b_q16_v1_en.html)]             | 10GB                | [8, 11, 40.1]      | 128,000            | Extract and link structured medical named entities |
| JSL_MedS_NER_VLM_2B_v2 | [1.5G, 2.1G, 3.3G]  | 2B         | multimodal | [[q4](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q4_v2_en.html), [q8](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q8_v2_en.html), [q16](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q16_v2_en.html)] | 10GB                | [25.5, 13.7, 48.9] | 32,768             | Extract and link structured medical named entities |

**You can explore these models on our** [Colab notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/36.0.Loading_Medical_and_Open_Source_LLMs.ipynb "https://colab.research.google.com/github/johnsnowlabs/spark-nlp-workshop/blob/master/healthcare-nlp/36.0.loading_medical_and_open_source_llms.ipynb") **and see how these models can enhance your healthcare workflows.**

