# Matching Patients with Clinical Guidelines
Matching Patients with Clinical Guidelines

<https://www.johnsnowlabs.com/matching-patients-with-clinical-guidelines/>

<https://youtu.be/wbIlQi9EyNg>

The speech extracted from the YouTube transcript details the challenge of matching patients with Clinical Practice Guidelines (CPGs) and presents an automated, multimodal solution developed by John Snow Labs.

Here is a detailed summary of the content:

### **I. The Role and Complexity of Clinical Practice Guidelines (CPGs)**

The session begins by establishing the role of CPGs in healthcare. CPGs are one of the most important pillars of any clinical decision support system.

- **Definition and Purpose:** CPGs are **systematically developed statements, documents, brochures, or catalogs** designed to optimize patient care by offering **evidence-based recommendations**. They compile years of experience, resources, articles, clinical trials, and best practices gathered by experts. CPGs are essential resources, especially for physicians early in their careers, acting as a "handbook" before they develop enough personal experience and intuition.

- **Principles:** CPGs must be standardized, multidisciplinary, evidence-based, and promote evidence-based practices to support clinical decision-making.

- **Accessibility and Volume:** CPGs are numerous; statistics from 2022 show there are **more than 3,700 CPGs**. Most CPGs are **paid resources** and are usually behind paywalls, requiring membership in certain associations or institutions to access.

- **Format Challenge:** CPGs are complex documents full of text, but also rich in **visuals, charts, diagrams, and flow charts**. These visual elements, often featuring "if-then-else" logic, are included because practitioners in a clinical setting do not have time to read pages of information; they need to quickly follow a diagram to make a decision. The core challenge is that practitioners must manually turn pages to find the relevant information, which is a non-trivial process.

### **II. The Need for an Automated Solution and Initial Demonstration**

The speaker proposes an automated solution where CPGs are indexed, allowing a practitioner to query the system with a specific patient case and receive treatment options.

- **Demo 1 (Multimodal vs. Vanilla RAG):** A live demo was conducted using a patient case involving **Type A Aortic Dissection**.

  - The **multimodal tool** successfully found the relevant flowchart and precisely returned the answer: **immediate Ascending Aortic Arch Surgery**.

  - If a **vanilla approach** (based purely on text retrieval, often leveraging Retrieval Augmented Generation/RAG) was used, it returned a less precise answer ("urgent surgical intervention") because it failed to understand the critical information contained within the chart. This highlights that traditional text-heavy RAG fails when answers are embedded in diagrams.

### **III. Modern Approaches to Querying CPGs**

The presentation then reviewed various techniques for leveraging CPGs using Gen AI and automated tools, noting the opportunities and pitfalls of each:

| **Approach** | **Description** | **Pitfalls / Limitations** |
|:---|:---|:---|
| **Vanilla Search Engine** | Keyword, exact, or fuzzy match search. | Information is spread over pages, lacks semantic search, and requires manual synthesis of answers. |
| **Fit Entire CPG into LLM** | Ingesting the whole document into the model's context window. | Expensive, slow, and LLMs' generalization capability deteriorates past 32,000 tokens (due to the "lost in the middle" phenomenon). |
| **Fine-tune LLM over Q&A Pairs (SFT)** | Supervised training using input/output pairs derived from CPGs (e.g., using Laura). | High risk of **hallucination** and lack of reasoning across multiple pages. |
| **Continual Pre-training** | Showing PDFs to the LLM for ongoing training. | Non-trivial, expensive, very slow, and risks losing generalization capability. |
| **Convert CPGs to Structured Format** | Using techniques like Knowledge Graphs or Business Process Mining. | Expensive, laborious, requires expertise, and risks hallucination during conversion. |
| **Build a RAG Framework** | Using retrieval augmented generation. | Requires special attention to the **multimodal nature** of CPGs, not just blind splitting/chunking of text. |

### **IV. The Flow for Matching Patients with CPGs**

The webinar's most important section covered the detailed flow required to match a complex patient profile to the correct CPGs.

**1. Building the Unified Patient Journey:** Before matching, the system must create a **unified view of the patient**. This means augmenting the patient's admission complaints with all available EHR records, patient history, unstructured notes, and table data (using standards like FHIR or OMOP schema). John Snow Labs has a **Patient Journey** solution that synthesizes this data from multiple resources.

**2. Finding the Appropriate CPGs (Agentic Flow):** Given the large number of CPGs (3,700), a **smart agentic flow** is used as the first step to pick the right set of guidelines-narrowing the scope down from thousands to a handful of applicable CPGs (e.g., six).

**3. The Multimodal CPG RAG Flow (Architecture):** Once the CPGs are narrowed down, the Multimodal CPG Retrieval Augmented Generation flow is utilized:

- **Processing:** Source PDFs, diagrams, and flowcharts are processed using the JSL Multimodal LLM to convert them into **hierarchical JSON** and flatten text.

- **Indexing:** The system generates rich descriptions for non-text modalities (images, tables, charts). These descriptions are chunked and written into a Vector DB. The descriptions are used only for finding the right page via embedding similarity.

- **Retrieval:** When RAG retrieves a relevant chunk, the system looks up the metadata and retrieves the entire **parent page information (including the original charts/tables and the JSON representation)**.

- **Generation:** This rich, condensed JSON information (containing the precise visual context) is sent to the LLM, enabling it to answer complex questions based on diagrams and flowcharts precisely.

### **V. Evaluation of Multimodal Tools**

The speaker evaluated several tools for their ability to handle the diagrams, scanned text, and tables found in CPGs.

- **Tesseract OCR/Simple PDF Extraction:** Fails miserably on low-quality or scanned text and cannot utilize charts, often returning "garbage".

- **Docling:** Highly efficient and promising for unstructured-to-structured conversion, returning granular objects with coordinate information, but requires extensive, non-trivial post-processing logic.

- **MarkDown by Microsoft:** Only extracts text and misses the content within charts and tables themselves.

- **Lama 3.2 11 Billion Vision Instruct:** A promising, but heavy Vision LLM (requiring 30GB GPU memory). It returns document hierarchy and can extract text from charts but can hallucinate and is dependent on precise prompting.

- **JSL Multimodal LLM (mms):** This proprietary model, around 10 billion parameters in size, is designed to extract precise page JSON. It successfully handles printed text, scanned text, table detection, chart/flowchart conversion to JSON, and preserves document hierarchy.

The multimodal approach is shown to be superior because it ensures that the final LLM sees all artifacts on the page, preventing hallucinations that occur when the model must synthesize answers based only on vague text descriptions.