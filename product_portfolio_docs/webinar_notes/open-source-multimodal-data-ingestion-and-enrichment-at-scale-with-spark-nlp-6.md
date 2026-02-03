# Open-Source Multimodal Data Ingestion and Enrichment at Scale with Spark NLP 6
Open-Source Multimodal Data Ingestion and Enrichment at Scale with Spark NLP 6

<https://www.johnsnowlabs.com/open-source-multimodal-data-ingestion-and-enrichment-at-scale-with-spark-nlp-6/>

<https://youtu.be/r0t5Q2AipXw>

<img src="/media/image.jpg" title="Video titled: Open-Source Multimodal Data Ingestion and Enrichment at Scale with Spark NLP 6" style="width:6.3125in;height:3.65625in" />

This response summarizes the speech provided in the source transcript, drawing on details and explanations contained within the material.

The webinar, led by Mazar, who heads the Spark NLP team, explores the new features added to **Spark NLP 6**, focusing specifically on **multimodal data ingestion at scale**.

### **Overview of Spark NLP**

Spark NLP is an **open-source Natural Language Processing (NLP) library** built natively on the Apache Spark ML module.

**Key Characteristics:**

- **Release and Goal:** First released in 2017, its initial idea was to provide a unified solution for all NLP and Natural Language Understanding (NLU) needs.

- **Industry Recognition:** It has been the most widely used NLP library in the industry for the last five years. It is cited as the most accurate, fastest, and "zero code to scale" open-source NLP library available.

- **Community Scale:** The library recently crossed **154 million downloads on pipi**.

- **Resources:** Spark NLP offers an extensive ecosystem, hosting over **135,000 free and open-source pre-trained models and pipelines** ready for use with one line of code.

- **Support and Integration:** The library uses the Apache 2 license and officially supports Python, Scala, and Java. It is optimized for integration with environments and tools like Jupiter, Anaconda, Docker, Kubernetes, Databricks, GCP, and Azure.

- **Development Principles:** Spark NLP development focuses on three main principles: **accuracy** (shaping the most accurate solution), **scalability** (must scale zero to linear, aiming for close to four times faster when adding four nodes), and **speed** (being fast even within a single-node situation).

Scaling is designed to achieve **nearly linear speed enhancement** when adding more executors, nodes, or workers on platforms like Databricks.

### **New Multimodal Data Ingestion in Spark NLP 6**

Spark NLP 6 introduces native, enterprise-focused support for **unstructured and semi-structured data** ingestion. This allows for a unified, seamless integration where ingestion features are part of the same pipeline, eliminating the need for outside libraries.

**The Spark NLP Reader:** The new spark NLP reader allows native ingestion and parsing of multiple formats, including:

- **PDF** (including encrypted files and bounding box extraction).

- **Excel**.

- **PowerPoints** (slides and notes).

- **Raw text and logs, CSVs, emails, and HTMLs**.

This capability supports use cases such as **automating legal document processing** (contracts, NDAs) by bulk ingestion and extracting structured data (clauses, dates) from sources stored in various formats. Ingesting PDFs is simple, requiring only pointing the spark.read.format("binaryFile") command to the directory. The output includes detailed metadata like page numbers, sections, and titles, which assists in data chunking for vectorization and search.

### **Vision Language Models (VLM) at Scale**

Spark NLP has natively integrated **Llama CPP**, an open-source project that runs Llama or other transformer-based Large Language Models (LLMs) efficiently on local devices using C++. Llama CPP is popular due to its **quantization feature**, which creates smaller models requiring less memory and enabling faster inference.

This integration provides native support for various hardware, including Intel processors, Nvidia graphics cards, and Apple silicon chips, offering deployment flexibility across single-node, multi-node, and cloud environments (AWS, Azure, GCP, Kubernetes).

**Quantized VLM Support:** Spark NLP 6 added support for **quantized vision language models (VLM)** at scale.

- **Native Integration:** These models, utilizing quantized GGF models from Llama CPP, are now "first class citizen\[s\]" inside a Spark data frame.

- **Capabilities:** They can describe, summarize, or reason over visual inputs entirely **on-premise and offline**. This unblocks tasks like **image captioning, visual question answering, and document analysis**.

- **Inference:** Native inference is available on common platforms, including CPU and GPU acceleration, allowing for massively parallel multimodal batch processing across large image datasets.

- **Code Example:** Using VLM involves setting up an image assembler, a document assembler, and an autogf vision model annotator, specifying the image column and an instruction (e.g., summarize, describe, or ask a question).

Benchmarks show that using cheap T4 GPUs handles 10 times more load than CPUs and finishes jobs 9 times faster. Scalability remains near linear when adding nodes, providing flexibility in hardware choice.

### **Retrieval Augmented Generation (RAG)**

Spark NLP's approach to RAG includes:

1.  **Multiformat Document Ingestion:** Easy processing of various documents (PDF, Word, HTML, text).

2.  **Flexible Embeddings:** Support for a wide range of embedding models, making the solution model agnostic.

3.  **Vector Database Compatibility:** Seamless integration with every vector database (via SDK or API calls).

Spark NLP manages the ingestion of multimodal data sources, processing, vectorization, and insertion into the vector database.

**RAG Challenges Addressed:**

- **Accuracy:** Spark NLP offers thousands of state-of-the-art models, preventing users from being stuck with a single model provider.

- **Speed and Scale:** Ingesting massive datasets (e.g., 50 million or 100 million documents) at enterprise grade requires **native distribution** using Apache Spark and Spark NLP to achieve reliable computation.

### **Hands-on Demonstrations**

The speaker provided two hands-on demonstrations showcasing Spark NLP 6 features:

#### **1. Multimodal RAG on Databricks and Vivviet**

This demo showed an end-to-end RAG pipeline:

1.  **Image Processing:** Images were read into a data frame, and a standardized instruction ("explain this image in one sentence") was added.

2.  **VLM Description:** The data was transformed using the pipeline, which included an autogf vision model (Lava 1.5, 7B parameter, 4-bit quantized) to generate a detailed textual description of each image.

3.  **Vectorization:** The resulting descriptions were fed into a second pipeline using text embeddings (Nomic embeddings were used) to generate vectors.

4.  **Database Insertion:** These vectors were converted to a Pandas DataFrame and inserted into a remotely available Vivviet vector database.

5.  **Querying:** Questions (e.g., asking for a spider, a group of people) were vectorized using the *exact same embedding model* and used to query the database, demonstrating successful contextual similarity search, retrieving accurate image descriptions and corresponding IDs. The process proved that scaling to millions of images simply requires adding more nodes with zero code change.

#### **2. Large Scale Text Embedding on AWS Glue**

This demonstration focused on scaling text ingestion and vectorization:

1.  **Job Setup:** A Scala job was run on AWS Glue (Glue 5, a serverless service) using 20 workers (80 DPUs).

2.  **Data Processing:** The job read approximately **100,000 documents and abstracts from a PubMet dataset** stored on S3.

3.  **Embedding:** It used BGE embeddings to vectorize the lengthy text documents and save the results back to disk.

4.  **Performance:** The entire process finished in about **4 minutes**. The efficiency was attributed to Spark NLP's native distribution and AWS Glue's fast startup time (20 to 40 seconds, compared to 10-15 minutes for traditional services), making it ideal for frequent batch jobs.

The speaker concluded by encouraging the audience to review the numerous available examples, check out the documentation on Llama CPP integration, and contribute to the library on GitHub.