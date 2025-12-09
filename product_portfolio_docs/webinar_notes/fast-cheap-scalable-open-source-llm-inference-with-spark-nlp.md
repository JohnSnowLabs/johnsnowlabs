# Fast, Cheap, Scalable Open-Source LLM Inference with Spark NLP
Fast, Cheap, Scalable Open-Source LLM Inference with Spark NLP

<https://www.johnsnowlabs.com/watch-webinar-fast-cheap-scalable-open-source-llm-inference-with-spark-nlp/>

https://youtu.be/vtDt9YINW74

The source you shared is an excerpt from a webinar presentation titled "Fast, Cheap, Scalable: Open-Source LLM Inference with Spark NLP.mp4". The speaker is **Danilo Gorbano**, a software engineer and machine learning engineer at Jon Snow Labs.

The speech serves as a technical deep dive and persuasive argument for using the open-source library Spark NLP to handle large-scale document understanding, focusing specifically on scaling with embeddings and Large Language Models (LLMs) via Retrieval Augmented Generation (RAG).

Below is a detailed summary of the speech content, organized by topic:

### **I. Introduction and Webinar Overview**

The webinar focuses on using **Spark NLP** to achieve fast, cheap, and scalable open-source document understanding. The presented components are crucial for building **semantic search systems** and advanced **generation solutions**.

The presentation outlined the following agenda points:

1.  **Retrieval Augmented Generation (RAG):** Discussing this approach which combines retrieval and generation techniques for more contextually relevant answers.

2.  **Spark NLP Overview:** Exploring its features, capabilities, and use for Natural Language Processing (NLP).

3.  **Data Processing Efficiency:** Covering techniques for optimizing speed and scalability in NLP workflows.

4.  **Semantic Search Comparison:** Comparing approaches like SMI Ray with Hack and Spark NLP.

5.  **Llama 2 Integration:** Showcasing practical examples and use cases demonstrating the benefits of combining Llama 2 and Spark NLP.

### **II. Large Language Model Limitations**

LLMs, such as GPT-4, have several notable limitations:

- **Hallucinations:** LLMs can generate outputs that are incorrect, illogical, irrelevant, or do not fit the input context. The speaker showed an image where GPT-4 incorrectly selected Presley, demonstrating a reliability issue.

- **Outdated Knowledge:** Models are trained on data available up to a certain point and are not updated in real-time, meaning their knowledge can become outdated, limiting usefulness for recent events.

- **Context Limitation:** LLMs do not have access to proprietary or context-specific data unless explicitly provided during the session.

Users are advised to be aware of these limitations and validate and cross-check information provided by these models.

### **III. Vector Databases and Retrieval Augmented Generation (RAG)**

**Vector Databases (VDBs)** are crucial because they enable fast and accurate retrieval of documents by comparing **vector embeddings**. VDBs are fundamental for grounding application responses in semantically relevant data, facilitating advanced capabilities like semantic search and RAG beyond simple keyword matching.

The mechanism involves:

1.  Transforming content (data or documents) into vector embeddings (using models like BERT or DistilBERT) to capture semantic meaning.

2.  Storing these embeddings in a VDB for efficient querying.

3.  Processing a user query, converting it to an embedding, and performing a similarity search to determine the most relevant results.

**RAG** involves indexing documents based on their semantic representation (embeddings). The retrieved documents then provide context for the LLM input, ensuring the LLM generates **more accurate and contextually relevant responses**.

**The RAG Process involves two main phases**:

1.  **Pre-processing (Batch Process):** Documents are divided into smaller chunks \$\rightarrow\$ Each chunk is converted into embeddings \$\rightarrow\$ Chunks and embeddings are stored in a vector database (often run overnight).

2.  **Runtime:** A user query is converted into an embedding \$\rightarrow\$ Similarity is computed between the query embedding and stored document embeddings (e.g., using cosine similarity) \$\rightarrow\$ The retrieved chunks are ranked based on relevance \$\rightarrow\$ These chunks provide context for the pre-trained LLM \$\rightarrow\$ The LLM generates the final output.

The challenges addressed by this system include managing the speed, scale, and accuracy required to handle real-time queries and large volumes of data.

### **IV. Spark NLP Features and Adoption**

Spark NLP is an **open-source Natural Language Processing library** built on top of **Apache Spark and Spark ML**. It was first released in July 2017.

**Key Highlights of Spark NLP:**

- **Unified Solution:** Provides a single, unified solution for all NLP and Natural Language Understanding (NLU) needs, including a comprehensive suite of pre-trained models and pipelines.

- **Industry Recognition:** It has been the **most widely used NLP library in the industry for five consecutive years** and is recognized as the most popular NLP tool in enterprises.

- **Performance:** It is recognized as the **most accurate, fastest, and scalable open-source NLP library** with Zero code deployment. It achieves the highest accuracy on 20 benchmarks in peer-reviewed papers.

- **Resources:** Offers **18,000+ free, open-source** pre-trained pipelines and models for various tasks like entity recognition, text classification, and image classification.

- **Integration:** It supports multiple programming languages, including Java, Python, and Scala, and benefits from the same optimizations and testing as Spark itself. It is available under the Apache 2.0 license.

### **V. Speed and Scale Optimizations**

**1. Effective Partitioning Techniques (Spark NLP is built on Spark):** To optimize parallelism, it is suggested to have **at least two to three times as many partitions as there are cores** in the Spark cluster. This multiplier helps balance parallelization, load balancing, and fault tolerance. Having more partitions than cores ensures that workloads are evenly spread, data skew is managed, and new tasks can immediately utilize free cores when others finish early, maintaining high utilization rates.

**2. OpenVINO Integration (Spark NLP 5.4.0):** Spark NLP 5.4.0 includes enhanced support for **Intel's OpenVINO toolkit**, complementing NNX runtime. OpenVINO optimizes deep learning inference on Intel hardware, significantly reducing latency and increasing throughput, which is crucial for real-time processing.

### **VI. Benchmarks and Hands-On Demonstration**

The hands-on section utilized a Databricks cluster setup (Spark 3.4.1) using Ice Lake processors (M6id.xlarge) with 64 cores and a 120,000-row news data set.

**1. Semantic Search & Pre-processing:**

- Initial semantic search processing involved using **MPNET embeddings**.

- The computation of embeddings took 38 seconds. The similarity calculation (the vector database cross-join) took 658 seconds.

- A key finding was that MPNET embeddings led to **low accuracy** in retrieving relevant documents.

**2. Horizontal Scaling (Spark NLP vs. Ray/Haystack):**

- Benchmarks showed that **Spark NLP excels in seamless integration, serialization, and parallelization**, demonstrating significantly superior performance speed and scalability compared to Ray and Haystack.

- The speaker noted that Spark NLP's native integration with the Spark engine makes implementing RAG tasks **easier and more streamlined** than solutions using Ray/Haystack, which may require complex optimization.

**3. Llama 2 Inference Comparison (ONNX vs. OpenVINO):** Benchmarking Llama 2 question and answer tasks revealed:

- **CPU Usage:** OpenVINO uses **significantly fewer CPU resources** compared to ONNX, allowing for higher parallelism.

- **Speed:** OpenVINO was **4 to 7 times faster** than ONNX for query processing, critical for providing captive responses.

**4. Llama 2 Inference Comparison (Spark NLP OpenVINO vs. Spark Hugging Face UDF):** Spark NLP OpenVINO demonstrated significant performance benefits over wrapping Hugging Face transformers functionality in a Spark User Defined Function (UDF):

- For processing 100 rows, Spark NLP completed the task in 330 seconds, while Spark Hugging Face took 2,700 seconds. This means Spark NLP was approximately **eight times faster**.

- The Spark Hugging Face UDF also suffered from serialization issues and **multiple task failures** at larger scales, highlighting its limitations in handling large datasets efficiently.

**5. Runtime RAG Application Example:**

- For the final RAG demonstration, **E5 embeddings** were used instead of MPNET to improve accuracy.

- The runtime process took 216 seconds and resulted in **accuracy that was twice as good** as the MPNET embeddings.

- The Llama 2 transformer within Spark NLP was used to enrich the retrieved documents, successfully performing tasks such as translating text to Spanish and running sentiment analysis.

- The speaker contrasted this seamless use with the complexity of using a pure Spark UDF for Llama 2, which requires manually dealing with tokenizers, attention masks, and input IDs.