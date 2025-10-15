# From GPT4 to Llama-2 Supercharging State-of-the-Art Embeddings for Vector Databases with Spark NLP
From GPT4 to Llama-2 Supercharging State-of-the-Art Embeddings for Vector Databases with Spark NLP

<https://www.johnsnowlabs.com/watch-from-gpt-4-to-llama-2-supercharging-state-of-the-art-embeddings-for-vector-databases-with-spark-nlp/>

<https://youtu.be/I_YpN3mgwqc>

<img src="/media/image.jpg" title="Video titled: [WEBINAR] From GPT-4 to Llama-2: Supercharging State-of-the-Art Embeddings for Vector Databases" style="width:6.3125in;height:3.65625in" />

This response provides a detailed summary of the speech presented in the webinar transcript excerpts, covering the agenda, the technical challenges, the solution via Spark NLP and RAG, and the demonstrations of various cloud technologies and LLMs.

The speaker, Mazier Panahi, who leads the team behind the **Spark NLP Library**, served as the guide for the webinar, which explored the topic of **vector databases and text embeddings**.

### **Webinar Agenda and Overview**

The agenda included several key areas:

1.  Learning the importance of **Retrieval Augmented Generation (RAG)** for Large Language Models (LLMs) like ChatGPT and Llama.

2.  An overview of Spark NLP, focusing on why **accuracy, speed, and scale** are critical for RAG.

3.  Two hands-on demonstrations:

    1.  Using **AWS Glue and EMR** with Spark NLP to transform PubMed articles into vectors.

    2.  Using **Databricks** to ingest the resulting documents and vectors into **Elasticsearch**.

4.  Demonstrating how the entire RAG system integrates using **LangChain** with GPT-4 and Llama 2.

### **Limitations of LLMs and the RAG Solution**

LLMs, while possessing a vast amount of knowledge, are not databases. Their knowledge is **static** and does not update in real time, making them unreliable for new or recent data. Furthermore, they cannot access private or use case-specific information. This leads to the problem of **"hallucination,"** where the LLM is confidently wrong, and the lack of a reliable source, reference, or citation makes the information problematic for applications where credibility is crucial.

To overcome these limitations, the solution is turning to **Vector Databases**. These databases store documents indexed by vector representations, enabling efficient similarity searches. This capability is crucial for **grounding the LLM** using RAG techniques to ensure the provided information is relevant and accurate.

A typical RAG architecture involves:

1.  A user triggers a query/instruction.

2.  A retrieval function turns the query into a vector.

3.  The vector is sent to a vector database, which returns a set of documents.

4.  These documents form a context, which is then passed along with the prompt (e.g., "based on the provided information, please try to answer...") to the LLM.

The **embedding model** used is critical because it captures the meaning of a text. Techniques for ensuring embedding quality include dimensionality reduction (like PCA, t-SNE, UMAP) and clustering algorithms (like k-means). Entity extraction from returned documents is another method to check the quality and connectivity of the retrieved information.

### **Spark NLP: Focus on Accuracy, Speed, and Scale**

The RAG architecture's first half is purely NLP (pre-processing, chunking, managing overlap), and the most expensive part is calculating the embeddings. Contextual embeddings, like those from models such as BERT, require extensive computation and are about 10 times faster when using GPUs.

**Spark NLP** is an open-source NLP Library, initially built on top of Apache Spark (specifically a Spark ML extension) and first released in July 2017. It is noted as being a unified solution for NLP problems and has been voted the **most widely used NLP library in Industry Enterprise** for the last five years.

Three core tenets of Spark NLP are:

1.  **Accuracy:** Achieving state-of-the-art results for all released models.

2.  **Speed:** Being the fastest, even on a single machine.

3.  **Scalability:** Achieving a nearly linear correlation when adding more machines to a cluster.

In terms of performance, Spark NLP is between **three to seven times faster** than Hugging Face on a single server using the exact same model. Furthermore, Spark NLP's reliance on the JVM and Java's memory management proved **much more efficient** than Python, as Hugging Face failed with "out of memory error" when tested against 100,000 and 1 million documents. The library supports optimized hardware, including Nvidia GPUs, Intel, and experimental support for Apple silicon in v5, and uses **Onyx runtime** as a deep learning engine to improve speed and scalability.

Spark NLP v5 introduced top-of-the-leaderboard text embeddings like **E5 and Instructor**, which outperform the text embedding offered by OpenAI, reinforcing the importance of accessible, open-source, and scalable embeddings.

### **Hands-on Demos: Vectorization and Ingestion**

**1. Transforming PubMed Articles (AWS Glue vs. EMR):** The first demo focused on transforming about 100,000 full-metadata PubMed articles into vectors using the **E5 embedding model**.

| **Service** | **Characteristics** | **Outcome** | **Time** |
|:---|:---|:---|:---|
| **AWS Glue** | Serverless, resources available, incredibly fast startup time (around one minute). Used for time-sensitive, ad hoc, small batch jobs. Dependencies are less flexible. | Succeeded. | Almost **five minutes** total to transform and save the vectors. |
| **AWS EMR** | Simple EC2, cheaper (can use spot instances), flexible for complex codes/dependencies. Has provisioning time. | Terminated/Finished. | Took **12 minutes** total; the startup/bootstrapping time was 4.5 to 5 minutes. The actual processing time was about six minutes, similar to Glue. |

**2. Ingesting Vectors into Elasticsearch:** The next step involved using Databricks to ingest 21 million vectorized articles into an Elasticsearch cluster. The setup was a hybrid situation: Databricks servers in the US region connected to an on-premise Elasticsearch cluster in Paris, France, via a reverse proxy (nginx).

- The data was loaded into Databricks (21 million articles, vectors already present).

- The native **Elasticsearch Spark connector** was used to connect to the cluster.

- The ingestion process was **parallel and distributed** across 10 workers and 320 partitions.

- During the live demo, a sample of two percent (almost half a million) documents was ingested into a new index in approximately **2 minutes and 46 seconds**.

### **RAG Implementation with LangChain and LLMs**

The demonstration then shifted to using the newly ingested data for Retrieval Augmented Generation using LangChain.

**Zero-Shot LLM Issues:** LLMs lack knowledge of recent concepts (like LangChain) and provide serious answers (e.g., about red meat and heart attacks) without references, leading to trust issues.

**RAG Querying:** Although Spark NLP was used to transform the bulk data, the querying step utilized another library (Hugging Face's sentence transformers) to vectorize the input query. This was done to demonstrate that users are not locked into using Spark NLP for querying, as the model weights (E5 base) are the same across platforms.

The query system performed a **k-Nearest Neighbors (kNN) search** in Elasticsearch, combining it with lexical filtering. A custom retriever (**My Own PubMed Retriever**) was created in LangChain to interface with this search function.

**LLM Comparison (GPT-4 vs. Llama 2):** The RAG chain was tested with different LLMs:

- **GPT-4:** Used for RAG Q&A, but noted to be **slow and expensive**.

- **Llama 2 (13B and 70B):** Open-source models were used via TGI (Text Generation Inference). The 13B version was favored over the 70B because it was faster and required less GPU memory, while still providing comprehensive answers.

- The RAG output showed that LLMs (like Llama 2) provided more nuanced answers, acknowledging complexity and external factors, compared to zero-shot answers.

**Agents Demonstration:** The final part showcased LangChain Agents, which use an LLM to decide which tool to employ (PubMed RAG, Wikipedia, or Calculator) based on the user's question. The demonstration also showed the ability to **mix LLMs**, using Llama 2 for the content generation tool (PubMed RAG chain) and Open AI for the final "thought" and summarized answer.