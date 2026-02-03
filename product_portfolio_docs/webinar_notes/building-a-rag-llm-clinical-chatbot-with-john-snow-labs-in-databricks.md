# Building a RAG LLM Clinical Chatbot with John Snow Labs in Databricks
Building a RAG LLM Clinical Chatbot with John Snow Labs in Databricks

https://www.johnsnowlabs.com/building-a-rag-llm-clinical-chatbot-with-john-snow-labs-in-databricks/

<https://youtu.be/Q35kk-9opcw>

<img src="/media/image.jpg" title="Video titled: Building a RAG LLM Clinical Chatbot with John Snow Labs in Databricks" style="width:6.3125in;height:3.65625in" />

The YouTube source provides a comprehensive webinar transcript titled "Building a RAG LLM Clinical Chatbot with John Snow Labs in Databricks". The presentation is led by **Amir Kanan** (Director of Industry Solutions at Databricks) and **Vessel** (Head of Data Science, leading the Healthcare NLP team at John Snow Labs).

The presentation covers the strategic importance of generative AI in the enterprise, the challenges of moving Gen AI projects into production, the specific solutions offered by Databricks, the technical architecture of Retrieval Augmented Generation (RAG) systems, and a live demonstration of building a RAG clinical chatbot using open-source tools.

## **Detailed Summary of the Speech Content**

### **I. Generative AI in the Enterprise and the Databricks Platform (Amir's Segment)**

**The Gen AI Landscape and Use Cases:** Generative AI is transforming the working landscape. A survey by MIT Technology Review found that **71% of executives plan to build their own generative AI models** or have already started initiatives. Organizations recognize that their **proprietary data is their competitive edge** (their "moat"), and training Gen AI models on this data translates directly into valuable Intellectual Property (IP).

Initial workloads focus on improving workforce productivity. LLMs are capable of automating tasks requiring human comprehension of natural language and basic reasoning, such as **summarization and entity extraction**.

Within **Healthcare and Life Sciences**, Gen AI is being applied to:

- Biomedical information retrieval and document synthesis.

- Increasing productivity in R&D teams by implementing **RAG systems** over internal and external research corpora.

- Clinical support and decision systems, and improving patient engagement through member/customer chatbots.

- Advanced applications like **drug discovery**, involving the training of non-human language models for proteins or DNA sequences.

**Challenges Moving to Production:** Moving Gen AI applications from experimentation to reliable production is a significant challenge. Key hurdles include:

1.  **Risk and Compliance:** This is paramount in regulated industries. Concerns arise over using proprietary data for model training, regulatory compliance, and the risk of **exposing proprietary or PHI (Protected Health Information) data** when interacting with external SAS model APIs. Security risks also include prompt injection attacks.

2.  **Hallucination and Toxicity:** Monitoring and controlling for these factors are essential in a production environment.

3.  **Data and LLM Ops Integration:** Gen AI applications are extensions of traditional ML/AI applications; therefore, integrating LLM Ops within the existing **data stack** is crucial, especially due to the large amount of **data movement required in RAG systems**.

4.  **Cost:** Using SAS models can become expensive quickly because charges are often based on tokens processed, and RAG models send large corpora of data to API endpoints. Training or fine-tuning custom models is also a high-cost solution.

**Databricks Data Intelligence Platform Solution:** Amir positions the Databricks platform as addressing these challenges through three main advantages:

1.  **Complete Control and Ownership:** Customers can **own their models** the same way they own their data, ensuring better governance and privacy. For RAG, data is stored in the Lakehouse (e.g., millions of documents), and custom models are served internally as API endpoints. Access controls and governance are managed using Unity Catalog.

2.  **Production Quality and Reliability:** The integrated stack streamlines deployment by building the Gen AI solution on top of the data solution. The system supports an iterative process of data ingestion, model deployment, monitoring feedback (like RLHF), and retraining to improve accuracy and control issues like toxicity.

3.  **Lowering Cost:** Databricks (following the Mosaic ML acquisition) offers cost-effective solutions for training and fine-tuning models. For instance, the cost to train Stable Diffusion was reduced from \$600,000 to around \$20,000.

### **II. Implementing RAG Architecture (Vessel's Segment)**

Vessel emphasizes that even highly capable LLMs like GPT-4 can answer **40% of questions incorrectly** (hallucination), and the worst part is often not knowing which answers are correct.

**RAG Overview:** RAG (Retrieval Augmented Generation) is the solution, acting as a method to **introduce context from proprietary knowledge bases** (internal documents gathered over decades) into the LLM. In a RAG architecture, the LLM serves primarily as an **orchestrator or smart assistant** to synthesize an answer based on the provided context, rather than using its own internal knowledge.

**The Five Stages of RAG:**

1.  **Ingestion:** Data (PDF, TXT, audio, video) must be **split into meaningful chunks**. How data is split is crucial and domain-dependent; for example, splitting by section, sentence, or extracting tables first.

2.  **Embedding:** Generating embeddings (vector representations) for each split. The embedding model must have a **context window** compatible with the split size.

3.  **Vector DB:** Stores the embeddings along with necessary **metadata** (document name, date, path).

4.  **Retrieval:** The query is embedded, and the query embedding is mapped to the context embeddings in the Vector DB to return the **top K most similar splits**.

5.  **LLM:** The retrieved context, along with the user query and a **system prompt** (instructing the LLM to only use the provided context and not hallucinate), is sent to the LLM to generate a synthesized answer.

**Enhancing RAG Performance:** While basic RAG can be built quickly using wrapper libraries (LangChain, Haystack), optimization is necessary:

- **Splitting Strategies:** JSL offers multiple splitting modules (section by section, token by token). Customized splitting (like JSL's licensed Custom Document Splitter for medical context) allows handling patterns, sections, or preventing sentence cuts.

- **Embeddings Scaling:** Open-source embedding models are highly capable. JSL offers integration to run embedding collection on Spark clusters, dramatically reducing processing time. Processing 1 million documents on a 16-worker Spark cluster took **3 minutes** using Spark NLP, compared to 43 minutes on a single machine (over 10x faster). The demo used **Instructor Base Embeddings**.

- **Retrieval Tuning:** Basic K-Nearest Neighbor (KNN) retrieval is naive. Techniques to enhance retrieval include **BM25** (keyword statistics) and **Hybrid Approach** (combining vector search like FAISS with BM25).

- **Post-processing/Ranking:** Retrieval results need post-processing to ensure quality. Techniques include:

  - **Diversity enhancement** (e.g., Lambda-Mold) to return dissimilar but relevant splits.

  - **Reordering documents** to prevent the "lost in the middle" problem (where LLMs forget information in the middle of a large context) by placing the most important splits at the beginning and end of the prompt sequence.

  - **Metadata filtering** (e.g., filtering based on journal name or similarity score).

**LLM Selection for RAG:** LLMs are evaluated on their **Context Adherence Score** (how well they stick to the context provided).

- Open-source models like **Zafire 7B** show strong performance in RAG architecture, sometimes outperforming much larger models like Llama 2 70B in context relevancy.

- The demonstration used quantized (4-bit C++ based) versions of **Llama 2** and **Zafire** locally via C Transformers library.

**Clinical NLP Augmentation and Compliance:** Since simple RAG architecture can struggle with complex, specific clinical questions (e.g., "treatment for a patient with a specific profile"), JSL augments the splits by running pre-trained **Clinical NLP models** (Name Entity Recognition, summarization, assertion classification) over the text and writing the extracted entities as metadata. This injected intelligence helps the retriever find relevant splits even if naive embedding similarity is low.

Regarding **PHI/HIPAA compliance**, JSL's medical chatbot is designed to be shipped as a **containerized, on-prem application** run behind the customer's firewall. This air-gapped environment minimizes the risk of exposing sensitive data, especially when using open-source LLMs hosted internally via services like Databricks serving.

## **Q&A Highlights**

- **Data Format:** When working with distributed data in Databricks, data (even CSV) must be written as a **Delta or Parquet table** so that it can be spread over the Spark workers.

- **Split Definition:** A "split" is a meaningful subtext or chunk of a document; the goal is high granularity, as large splits lead to diluted embeddings.

- **LLM Serving:** It is suggested to collect embeddings once and then reuse them while experimenting with different LLMs. LLMs can be served using Databricks endpoints and registered within the LangChain pipeline.