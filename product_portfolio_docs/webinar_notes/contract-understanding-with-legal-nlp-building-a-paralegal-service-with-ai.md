# Contract Understanding with Legal NLP building a Paralegal Service with AI
Contract Understanding with Legal NLP building a Paralegal Service with AI

<https://www.johnsnowlabs.com/watch-contract-understanding-with-legal-nlp-building-a-paralegal-service-with-ai/>

<https://youtu.be/-mTveOXShwk>

<img src="/media/image.jpg" title="Video titled: [Webinar] Contract Understanding with Legal NLP: building a Paralegal Service with AI" style="width:6.3125in;height:3.65625in" />

The speech provided in the YouTube source transcript, delivered by **Juan Martinez**, Lead Data Scientist at Jon Snow Labs and leader of the finance and legal NLP libraries, focuses on highlighting the benefits and applications of **Legal NLP (Natural Language Processing)** for **contract understanding**.

The presentation defines legal contract understanding as the task of analyzing legal contracts or agreements using specific AI techniques, primarily NLP. Martinez reviews several key concepts and corresponding NLP tasks utilized in this process:

### **I. Core Legal NLP Tasks for Contract Understanding**

**1. Text Classification** This NLP task is responsible for classifying an input text by identifying a specific class. There are two main types relevant to contracts:

- **Document Classification:** This identifies the contract type or the type of agreement (e.g., credit agreement, asset purchase agreement, non-disclosure agreement (NDA)). The process retrieves *one class* (the document type) from the document. John Snow Labs provides about 800 different classifiers for this purpose.

- **Clause Classification:** This identifies the different specific clauses within an agreement (e.g., termination clause, dispute resolutions, applicable law clause, introductory clause, insolvency, intellectual property). This process retrieves *one class per section* of the document. The library contains several hundreds (around 500) of these clause classifiers.

**2. Information Extraction (Named Entity Recognition - NER)** This involves identifying and extracting information at the entity level. The NLP task is called **Name Entity Recognition (NER)**.

- **Entities of interest** include the parties involved, countries or U.S. states, the specific effective date, the termination date, the purpose of the agreement, and the law to be applied in case of dispute resolutions.

- John Snow Labs uses **clause-specific entity recognition** (looking for information in specific clauses rather than the whole document) to improve performance and reduce processing time.

- **Zero-Shot NER** is also available, which allows users to extract information that the primary model was not explicitly trained on by using questions or "tips" (e.g., extracting location or former names).

**3. Relation Extraction** Relation extraction (RE) involves understanding the **relations between the different entities** that have already been extracted.

- This process links entities together, clarifying specific roles (e.g., in a credit agreement, identifying who is the lender and who is the borrower) or linking people signing on behalf of companies.

- Legal relation extraction models utilize methods like **dependency parsing** and **Span BERT** to understand if two entities are semantically connected and referring to the same concept.

**4. Question Answering (QA)** This allows users to **write their own questions in natural language** and receive answers from the legal document.

- This uses **Large Language Models (LLMs)**, such as T5-based models, to process the natural language question and provide the answer. Examples include asking: "What is the purpose of the agreement?" or "Between whom was the agreement made?".

**5. Legal Summarization** This task provides **reduced versions of long legal documents or agreements**.

- State-of-the-art LLM models are used to achieve high accuracy.

- For generating a comprehensive document summary, the technique involves summarizing individual paragraphs first, and then sending all those paragraph summaries to the summarizer again to produce a coherent, shorter summary of the entire document (e.g., reducing a 40-page document to a few sentences).

### **II. Demonstration Workflow (Hands-On Examples)**

Martinez demonstrates these concepts using notebooks (available in a GitHub repo containing over 40 Legal NLP notebooks). The legal NLP process runs on top of **Spark**, making it cluster ready, and requires a Spark session.

**Document and Clause Classification:** The first demo uses a **credit agreement** (specifically, an amendment to a restated credit agreement). A pipeline is constructed using a Document Assembler and Sentence Embeddings (numerical representation of text). The classifier confirms the document is a credit agreement. Next, the document is split into paragraphs (sections divided by at least two new lines) to allow for **Clause Classification**.

**Extracting Entities and Relations from the Introductory Clause:** The demo focuses on identifying the **Introductory Clause** (or "Names of the Parties" clause), which contains basic information like the parties, their roles, and the agreement type.

- **NER Application:** A separate NER pipeline is used, which often works best at the sentence level, so the chosen section is first split into sentences. The model successfully extracts entities such as the specific document type (e.g., "twelfth amendment to amendment and restated credit agreement"), the effective date, the parties (e.g., Carpin and Wachovia Bank), and key **aliases** (e.g., Wachovia Bank being referred to as "Agent" or "Bank" later in the document).

- **Relation Extraction Application:** A Relation Extraction pipeline is run to link these entities. The results visually confirm who is who, for example: "Corp is the borrower" and "Wachovia Bank is the agent and the bank".

**NDA Notebook and Advanced Tasks:** A second, quicker demonstration focuses on an **NDA (Non-Disclosure Agreement)** to showcase question answering and summarization.

- The NDA notebook successfully classifies many sections (up to 24 sections were detected, including definition of confidential information and exceptions).

- **Question Answering Demo:** Shows immediate answers to questions like: "When did the agreement enter into effect?" or "What is the address of the company?".

- **Summarization Demo:** Illustrates the step-by-step approach of summarizing section-by-section and then combining those summaries to create a concise, informative overall summary of the legal agreement.