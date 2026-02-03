# John Snow Labs’ Native Integrations with LangChain and HayStack
John Snow Labs' Native Integrations with LangChain and HayStack

<https://www.johnsnowlabs.com/watch-webinar-john-snow-labs-native-integrations-with-langchain-and-haystack/>

<https://youtu.be/stdFL7nRdFE>

<img src="/media/image.jpg" title="Video titled: Watch the Webinar: John Snow Labs' Native Integrations with LangChain and HayStack" style="width:6.3125in;height:3.65625in" />

The speech provided in the sources, delivered by Mmed, a data scientist in the healthcare team at John Snow Labs, focuses on the challenges of implementing Generative AI (GenAI) into production and how John Snow Labs' native integrations with LangChain and HayStack, leveraging Spark NLP, provide solutions, particularly within the Retrieval-Augmented Generation (RAG) architecture.

Below is a detailed summary of the speech:

### **1. Generative AI Challenges and Context**

GenAI is currently the most popular topic in the AI world, with most executives planning to build their own AI models and implement them in production. Seventy-five percent of CEOs believe GenAI provides a significant competitive advantage and increases employee performance.

However, implementation is difficult due to a lack of control over data and models, high costs at scale, and difficulty in monitoring GenAI in production. A major problem is **hallucination**, especially in clinical domains. When a question related to the clinical domain is asked, popular models like GPT-4 try to answer using their own knowledge base, leading to hallucinations. Because of this, the complete integration of GPT-4 into clinical healthcare productions is not yet possible.

### **2. The RAG Architecture**

The RAG architecture addresses the challenge of hallucination by ensuring the LLM answers questions using the organization's **internal data** rather than the LLM's intrinsic knowledge base. In this model, the role of the LLM is minimized, serving primarily as an orchestration tool.

The RAG architecture comprises five main stages:

1.  **Data Gathering/Splitting:** Internal data (source documents) must first be gathered and pre-processed (e.g., converting PDFs/images to plain text).

2.  **Splitting:** The data is split into smaller parts called "splits".

3.  **Embedding/Vectorization:** The splits are vectorized. This is noted as the **most expensive stage** of the RAG architecture.

4.  **Vector Database Storage/Retrieval:** The vector embeddings are saved in a vector database. Queries are also vectorized, and the retrieval part compares similarities to return the top K most similar splits.

5.  **LLM Generation:** The retrieved splits and the query are combined using a custom prompt and sent to the LLM, which generates an answer based *only* on the provided splits.

While the process sounds easy, the resulting accuracy heavily depends on choosing the correct algorithms, strategies, and models for each stage.

### **3. Crucial Stages and Strategy Considerations**

The speech highlights several stages where developers can modify strategies to enhance performance:

- **Document Splitting Strategy:** This is crucial and must be bounded to the specific domain (e.g., medical data).

  - For granular tasks (like keyword extraction), smaller chunk sizes should be used.

  - For holistic tasks (like summarization or Q&A), larger chunk sizes are appropriate.

  - Choosing a chunk size that is too large risks losing context.

- **Embedding Model Selection:** The embedding model must be compatible with the chosen chunk size. If a model can only handle 300 tokens but the data is split into 1,000 tokens, context will be lost. Factors like model size, speed, scalability, and resources must be considered.

- **Vector Database & Retrieval Strategy:** A retrieval strategy (e.g., recursive KNN or BM25) must be chosen based on the use case and resources. Post-processing techniques like diversity or reranking can be applied to the retrieved splits before sending them to the LLM.

- **LLM Selection:** Considerations include whether the solution is enterprise or open source, model performance, context sizes, and the design of the prompt templates.

### **4. John Snow Labs Solutions: Spark NLP Integration**

Spark NLP replaces the **document splitting** and the **split and metadata augmentation** stages in the RAG architecture. John Snow Labs supports LangChain and HayStack frameworks.

#### **A. Performance and Distributed Systems**

Since Spark NLP sits on Apache Spark, it allows for effective resource usage by running jobs on distributed systems instead of a single node. For example, getting the embedding for 1 million nodes takes 43 minutes on a single node, but only 3 minutes when distributed across 16 workers using Spark NLP. John Snow Labs combines its eight different libraries (Spark NLP, Healthcare NLP, Finance, Legal, Visual NLP) into a single installable library called johnsnowlabs.

#### **B. Document Splitting and Context Awareness**

Splitting strategy must be document-specific and context-aware, especially in domains like medical, finance, or legal, which have unique document structures.

- **Handling Domain-Specific Content:** For table-heavy content, tools like TableText can convert tables to plain text.

- **Clinical Note Splitting:** For medical datasets, data should be split using **section headers** in the clinical note. Default splitters, like character splitters, do not consider these headers.

  - Splitting by section headers ensures that information related to specific sections (e.g., "Family History" vs. "Principal Diagnosis") remains distinct, preventing irrelevant data (like family members' diseases) from being retrieved for a patient-specific query.

  - Spark NLP helps extract these section headers using NLP processes. The DocumentSplitter annotator is flexible, allowing parameters like chunk size, chunk overlap, and regex split patterns.

#### **C. Metadata Augmentation (Enriching Splits)**

Metadata augmentation helps retrieve the most relevant results from the vector database and the LLM. When data is split, information from earlier parts of the document might be lost in later splits.

- **Injecting Context:** Information like patient IDs, document IDs, or publication names can be injected into each split's metadata. This helps the retrieval system filter irrelevant splits. An example showed the similarity score increasing from 0.78 to 0.8 after adding metadata.

- **Spark NLP for Healthcare:** This licensed library provides over 2,000 pre-trained models and pipelines to augment splits.

  - **Clinical Enrichment:** Models can perform entity recognition, relation extraction, assertion status (negation detection), Q&A, and summarization.

  - **Header Detection:** Specific models (ner_jsl_slim) can detect section headers in clinical data.

  - **Summarization:** For very large clinical notes, the clinical summarization model can summarize the note before splitting, saving cost and processing time.

  - **Mapping and Filtering:** Entities can be detected (e.g., drug entities) and mapped to standardized codes (e.g., ICD-10 CM for conditions, RxNorm for drugs). Assertion status models can filter entities, dropping those with negation statuses (like "past" or "family member") and keeping "present" entities.

### **5. Integration Demos (LangChain and HayStack)**

The johnsnowlabs library enables seamless integration of Spark NLP functionalities within existing LangChain and HayStack workflows.

#### **A. LangChain Integration**

Users can import specialized components, such as the JohnSnowLabsLongChainCharSplitter or JohnSnowLabsLongChainCustomDocumentSplitter, and JohnSnowLabsLongChainEmbedder. This allows leveraging all Spark NLP and LangChain capabilities under the same environment.

The speech addressed the **"lost in the middle"** issue, where LLMs tend to remember the first and last retrieved splits more than the ones in the middle. Since retrieved splits are sorted by similarity score, the solution is to reorder them using the long_context_reorder module in LangChain to ensure the most relevant splits are placed at both the beginning and the end of the input context.

The presentation also covered using custom prompts in the Q&A chain to restrict the LLM's behavior (e.g., forbidding it from using its internal knowledge base) or forcing a specific output format. Retrieval methods like BM25 (keyword extraction, cheaper but less accurate) can also be used, or assembled with other retrievers using weights.

#### **B. HayStack Integration**

HayStack integration follows a similar logic, using classes like JohnSnowLabsHayStackProcessor for splitting and JohnSnowLabsHayStackEmbedder for embedding. HayStack uses a modular pipeline approach where components are added node by node. HayStack also offers ranking modules, such as DiversityRanker and LostInTheMiddleRanker, to optimize the order of splits sent to the LLM.