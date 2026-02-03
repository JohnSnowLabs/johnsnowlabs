# Regulatory-Grade Multimodal Medical Data De-Identification and Tokenization
Regulatory-Grade Multimodal Medical Data De-Identification and Tokenization

This response summarizes the content of the recording, which details John Snow Labs' (JSL) native integrations with LangChain and HayStack, focusing on how Spark NLP and Healthcare NLP enhance the Retrieval-Augmented Generation (RAG) architecture, especially for complex medical data.

## **1. Generative AI Context and Challenges**

Generative AI (Gen AI) is the most popular topic in the AI world. Many executives plan to build and implement their own AI models, believing that Gen AI offers a **significant competitive advantage** and increases employee performance.

However, integrating Gen AI into production is challenging:

1.  **Lack of Control:** There is no control over the data or the models themselves.

2.  **Cost and Monitoring:** Bringing Gen AI to production is difficult without built-in monitoring, and it is **too expensive at scale**.

3.  **Hallucination in Healthcare:** Popular models like GPT-4 still face medical domain challenges. When questioned about clinical topics, they tend to **hallucinate** or answer using their own internal knowledge base, making them unreliable for complete integration into healthcare clinical production environments.

## **2. The Retrieval-Augmented Generation (RAG) Architecture**

The RAG architecture is presented as the primary solution to mitigate hallucination and ensure LLMs communicate using proprietary, internal data. The LLM's role in RAG is minimized to that of an **orchestrator**.

The RAG architecture consists of five main stages:

1.  **Data Gathering:** Curated data is gathered internally.

2.  **Document Splitting:** Documents are split into smaller parts, known as "splits".

3.  **Vectorization & Storage:** Splits are vectorized (turned into embeddings) using an embedding model and saved in a vector database.

4.  **Query Vectorization & Retrieval:** The query is vectorized using the same embedding model. The retrieval component checks the similarity between the query embedding and the splits saved in the vector database, returning the **Top K most similar splits**.

5.  **Generation:** The retrieved splits and the query are combined using a \*\* custom prompt\*\*, which is then sent to the LLM. The LLM returns an answer based **only** on the provided splits.

## **3. Crucial Stages and Challenges in RAG Implementation**

While RAG can be implemented with a few lines of code, the underlying choice of algorithms and strategies directly affects the final result. Developers must strategically modify key stages for their use cases:

- **Data Preparation (Preprocessing):** Input data (PDFs, images) must be converted to plain text. For medical data, preprocessing must include **metadata extraction** (like entity linking or keyword extraction).

- **Document Splitting Strategy:** This is crucial and must be **domain-bounded**.

  - Chunk size depends on the task: smaller for granular tasks (keyword extraction) and larger for holistic tasks (summarization/Q&A).

  - Choosing a chunk size that is too large can lead to **context loss** if the embedding model is not capable of handling that token length.

  - The split strategy must be context-aware, handling elements like tables and charts by converting them to plain text.

- **Embedding Model Selection:** This is the **most expensive stage** of the RAG architecture. When choosing a model, developers must consider compatibility with the chunk size, model size, speed, scalability, and available resources.

- **Metadata Augmentation:** Injecting specific information into each split (like patient ID, document ID, or article title) is essential. This helps the retrieval component eliminate irrelevant splits and can **increase the similarity score** (e.g., from 0.78 to 0.8 in one example).

## **4. Spark NLP and JSL's Solution for Medical RAG**

John Snow Labs (JSL) provides solutions primarily addressing the **document splitting** and **metadata augmentation** stages of RAG.

### **A. Context-Aware Document Splitting**

In clinical RAG architectures, default splitters (like LangChain's recursive text splitter) fail because they **do not consider section headers**.

- **The Clinical Header Problem:** Clinical notes contain crucial section headers (e.g., "Family History," "Principal Diagnosis"). If a document is split without considering these headers, diseases belonging to a family member might be returned as relevant information related to the patient.

- **Spark NLP Solution:** JSL's Document Splitter Annotator is highly flexible, supporting regex patterns and various split modes. It integrates with **Spark NLP for Healthcare NER models** (like NR GSS slim model) to extract these section headers. The document is then split using these headers as regex patterns, ensuring each split represents a coherent section (e.g., "Family History" becomes one split, "Principal Diagnosis" becomes another).

### **B. High-Speed Distributed Embedding**

Since the embedding stage is the most expensive, JSL leverages the distributed nature of Spark.

- **Scalability Benefit:** Spark NLP allows running data sets on distributed systems instead of a single node. Processing **1 million notes** for embedding takes 43 minutes on a single node but only **3 minutes using 16 workers** in a distributed environment with Spark NLP.

### **C. Advanced Metadata Augmentation with Healthcare NLP**

Spark NLP for Healthcare provides more than 2,000 pre-trained models and pipelines to augment document splits with rich medical metadata:

- **Entity Recognition:** Models can recognize various entities, including oncological labels, specific conditions, diseases, or drug entities.

- **Assertion Status Filtering:** Models can check the assertion status (negation status) of entities. A **white list** can be applied to filter only "present" entities, dropping those related to family members, past conditions, or negations.

- **Code Mapping and Action Linking:** Entities can be mapped to external codes like **ICD-10 CM** (for clinical conditions) or **RxNORM codes** (for drugs). Mappers, such as the Drug Action Mapper, link drugs to their actions and treatments, allowing the system to answer specific, complex queries (e.g., "what kind of drugs can be used for anticoagulant action").

- **Summarization:** If the corpus is too large and expensive to process entirely, clinical summarization models can summarize the clinical notes, and the resulting summary can be used as the split.

## **5. Native Integration with LangChain and HayStack**

John Snow Labs provides a unified library that bundles all its capabilities (Spark NLP, Healthcare, Finance, Legal, Visual NLP). JSL supports native integrations with popular RAG frameworks like LangChain and HayStack.

- **Seamless Workflow:** Users can use the JSL library (johnsnowlabs) to access all the functionalities of Spark NLP and the RAG frameworks simultaneously within the same environment.

- **Integration Components:** JSL provides wrappers for core framework components, such as JohnsonsLongchainChartSplitter (which mirrors LangChain functionality) and JohnsLongchainCustomDocumentSplitter (allowing users to integrate Spark NLP's custom splitting capabilities). JSL also provides JohnsLLMEmbeddingRetriever for embedding models.

- **Post-Processing for LLMs:** The webinar addresses the LLM limitation known as **"lost in the middle,"** where the LLM forgets the middle parts of the context provided. Solutions include:

  - **Reordering:** Using modules like LangChain's long context reorder to shuffle the splits (which are initially sorted by similarity) to place the most relevant splits at the beginning and end.

  - **Retrieval Assembly:** Combining vector retrieval (FAISS) with keyword retrieval (BM25), which is cheaper but potentially less accurate, using weighted assembly.

- **Prompt Customization:** Users can define **custom prompt templates** to strictly limit the LLM's behavior (e.g., instructing it not to use its own knowledge base or enforcing specific response phrasing).