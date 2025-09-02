---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Medical Small LLMs
permalink: /docs/en/medical-small-llms
key: docs-medical-small-llms
modify_date: "2025-09-02"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

## Medical Small LLMs

<div class="h3-box" markdown="1">

{:.table-model-big.db}
| Model Name             | Disk Size | Model Size | Modality   | Available quantizations | Gpu memory required | Token/sec | Max Context Window **\*** | Tasks                                                         |
|-------------------------|-----------|-------------|------------|-------------------------|---------------------|-----------|--------------------|---------------------------------------------------------------|
| JSL_MedM_v3            | 8.2G      | 14B         | text-only  | [q4](https://nlp.johnsnowlabs.com/2024/10/06/jsl_medm_q4_v3_en.html) | 24GB | 79  | 32,768  | Summarization, Q&A, RAG, and Chat |
|                         | 14G       | 14B         | text-only  | [q8](https://nlp.johnsnowlabs.com/2024/10/08/jsl_medm_q8_v3_en.html) | 24GB | 84  | 32,768  | Summarization, Q&A, RAG, and Chat |
|                         | 21.9G     | 14B         | text-only  | [q16](https://nlp.johnsnowlabs.com/2024/10/23/jsl_medm_q16_v3_en.html) | 24GB | 253 | 32,768  | Summarization, Q&A, RAG, and Chat |
| JSL_MedS_v3            | 2.2G      | 3.5B        | text-only  | [q4](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_q4_v3_en.html) | 10GB | 28.5 | 131,072 | Summarization, Q&A, RAG |
|                         | 3.7G      | 3.5B        | text-only  | [q8](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_q8_v3_en.html) | 10GB | 18.7 | 131,072 | Summarization, Q&A, RAG |
|                         | 5.6G      | 3.5B        | text-only  | [q16](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_q16_v3_en.html) | 10GB | 50.2 | 131,072 | Summarization, Q&A, RAG |
| JSL_MedS_8B_v4         | 4.6G      | 8B          | text-only  | [q4](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_8b_q4_v4_en.html) | 16GB | 83  | 32,768  | Summarization, Q&A, RAG |
|                         | 7.8G      | 8B          | text-only  | [q8](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_8b_q8_v4_en.html) | 16GB | 84  | 32,768  | Summarization, Q&A, RAG |
|                         | 12.2G     | 8B          | text-only  | [q16](https://nlp.johnsnowlabs.com/2025/08/05/jsl_meds_8b_q16_v4_en.html) | 16GB | 272 | 32,768  | Summarization, Q&A, RAG |
| JSL_MedS_NER_v4        | 2.2G      | 3.5B        | text-only  | [q4](https://nlp.johnsnowlabs.com/2025/07/01/jsl_meds_ner_q4_v4_en.html) | 10GB | 28.5 | 131,072 | Extract and link medical named entities |
|                         | 3.7G      | 3.5B        | text-only  | [q8](https://nlp.johnsnowlabs.com/2025/07/01/jsl_meds_ner_q8_v4_en.html) | 10GB | 18.7 | 131,072 | Extract and link medical named entities |
| JSL_MedS_RAG_v1        | 2.2G      | 3B          | text-only  | [q4](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_rag_q4_v1_en.html) | 10GB | 30  | 32,768  | LLM component of Retrieval Augmented Generation (RAG) |
|                         | 3.7G      | 3B          | text-only  | [q8](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_rag_q8_v1_en.html) | 10GB | 20  | 32,768  | LLM component of Retrieval Augmented Generation (RAG) |
|                         | 5.6G      | 3B          | text-only  | [q16](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_rag_q16_v1_en.html) | 10GB | 53  | 32,768  | LLM component of Retrieval Augmented Generation (RAG) |
| JSL_MedS_Text2SOAP_v1  | 2.2G      | 3B          | text-only  | [base](https://nlp.johnsnowlabs.com/2025/04/09/jsl_meds_text2soap_v1_en.html) | 10GB | 53  | 32,768  | Generate structured SOAP (Subjective, Objective, Assessment, Plan) summaries |
| JSL_MedS_VLM_3B_v1     | 2.5G      | 3B          | multimodal | [q4](https://nlp.johnsnowlabs.com/2025/08/08/jsl_meds_vlm_3b_q4_v1_en.html) | 10GB | 8   | 128,000 | Extract and link structured medical named entities |
|                         | 3.6G      | 3B          | multimodal | [q8](https://nlp.johnsnowlabs.com/2025/08/08/jsl_meds_vlm_3b_q8_v1_en.html) | 10GB | 11  | 128,000 | Extract and link structured medical named entities |
|                         | 5.6G      | 3B          | multimodal | [q16](https://nlp.johnsnowlabs.com/2025/08/08/jsl_meds_vlm_3b_q16_v1_en.html) | 10GB | 40.1| 128,000 | Extract and link structured medical named entities |
| JSL_MedS_NER_VLM_2B_v2 | 1.5G      | 2B          | multimodal | [q4](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q4_v2_en.html) | 10GB | 25.5| 32,768  | Extract and link structured medical named entities |
|                         | 2.1G      | 2B          | multimodal | [q8](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q8_v2_en.html) | 10GB | 13.7| 32,768  | Extract and link structured medical named entities |
|                         | 3.3G      | 2B          | multimodal | [q16](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q16_v2_en.html) | 10GB | 48.9| 32,768  | Extract and link structured medical named entities |

> **\*** Larger context window requires larger GPU Memory

</div>
