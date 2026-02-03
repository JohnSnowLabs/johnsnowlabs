# Automated Summarization of Clinical Notes
Automated Summarization of Clinical Notes

<https://www.johnsnowlabs.com/watch-automated-summarization-of-clinical-notes/>

<https://youtu.be/noQPqgHm4yk>

<img src="/media/image.jpg" title="Video titled: Automated Summarization of Clinical Notes" style="width:6.3125in;height:3.65625in" />

The source material is a detailed transcript from a webinar titled **"Automated Summarization of Clinical Notes,"** presented by the Head of Data Science and Healthcare NLP lead at John Snow Labs. The presentation covers why automated summarization is needed in healthcare, how it is implemented, and introduces the latest pre-trained clinical summarization models released by John Snow Labs.

Below is a detailed summary extracted from the speech:

### **1. Definition and Techniques of Text Summarization**

Text summarization is identified as one of the main NLP tasks. The goal is **condensing original, lengthy text into a shorter, more compact, and dense version** while still retaining the most important concepts, information, and meaning.

There are two primary techniques in NLP for text summarization:

- **Extractive Methods:** These methods are typically statistical, relying on keywords and key phrases. They identify and extract the most important sentences and phrases from the document to build a summary without losing much context.

- **Abstractive Methods:** This is considered the harder problem because it involves **generating entirely new text** based on the original content. Abstractive methods may rephrase and combine sentences to create a new summary. The capability for abstractive summarization has significantly advanced with **Transformer architectures** like BERT and especially **GPT**, which is generative.

The webinar focuses primarily on **abstractive methods**, as John Snow Labs already has existing models for extractive methods.

### **2. The Need for Summarization in Clinical Settings**

Summarization of patient notes and clinical context is critical for improving communication among healthcare providers.

**Benefits of Clinical Summarization:**

- **Improves Communication:** Healthcare providers often use different templates, schema, and content, making condensed, standardized summaries easier to understand.

- **Facilitates Decision Making:** Providers often do not have time to read five pages of clinical reports, necessitating fast reading and understanding.

- **Reduces Manual Time:** It reduces the time spent on manual documentation.

- **Identifies Patterns:** Summarization helps physicians find key threads and patterns that should not be missed.

- **Reduces Errors:** Automated summarization reduces human error and lack of consistency, as human summaries can vary day-to-day and may not be representative for another physician.

**Challenges in Clinical Summarization:**

- **Patient Privacy:** Algorithms must maintain patient privacy (PHI data).

- **Medical Terminology:** Healthcare utilizes its own language, including medical terminologies and abbreviations, which must be handled correctly during summarization.

- **Information Retention:** It is challenging to develop algorithms that reflect all required context while avoiding the loss of key points, which could be more costly than reading the full document.

### **3. State-of-the-Art Architectures and Benchmarks**

Summarization is an active research area. Current leading architectures for general text summarization are **T5-based models** and **BART-based models**. **Pegasus** (developed by Google) is also one of the top leading summarization methods. These models are mostly based on deep learning.

For visualization, the speaker provided examples of GPT-4 summarizing a radiology report and a clinical discharge report, noting that while developing their solutions, they compared their models against GPT-4.

### **4. Evaluation Metrics and Quality Dimensions**

Evaluation of summarization is subjective and depends on the specific use case.

**Common Analytic Metrics:**

- **Rogue (Recall-Oriented Gisting Evaluation):** Counts overlapping textual units. It is often insufficient for abstractive summarization because abstractive models may use different words while retaining the same meaning, resulting in a low overlap score.

- **BERT Score:** Calculates similarity using contextual embeddings of tokens. It measures the contextual distance between the generated and reference summaries. It requires penalization for repetitiveness to be fully effective.

- **BLEU Score**.

**Quality Dimensions (Subjective Criteria):** Researchers often seek correlation between analytic metrics and human-rated quality dimensions.

- **Coherence:** Checks if the summary is well-structured and organized.

- **Consistency (Factual Alignment):** Ensures the summary does not hallucinate or produce garbage; the factuality between the ground truth and the summary must align.

- **Fluency:** Requires no typos, formatting problems, or grammatical errors; the summary must be easy to read.

- **Relevance:** Focuses on keeping only the important/salient phrases and avoiding useless information.

### **5. Spark NLP for Healthcare Summarization Models**

Spark NLP for Healthcare, which includes over 1,000 pre-trained clinical models, has released **five summarization models**.

**Model Architecture and Training:**

- The models are based on the **Flatified (Flan-T5) base version**, which has 250 million parameters.

- The base version was chosen so that the models can run within the Spark NLP ecosystem (JVM-based) on machines with lower memory (e.g., 12 GB), allowing them to function within a pipeline alongside other complex NLP algorithms (NER, tokenizers, etc.).

- The models were fine-tuned using noisy augmentation and were repeatedly checked and fixed by human physicians on the team.

**The Five Summarization Models:**

1.  **Clinical:** Summarizes core clinical documentation, such as discharge notes and radiology reports.

2.  **Augmented:** Uses open-source datasets (like Samsung, CNN news) to augment the backbone before fine-tuning with John Snow Labs' internal datasets.

3.  **Clinical Question:** Summarizes patient questions, useful for condensing long inquiries from call centers or social media platforms to quickly grasp the core issue (e.g., "what is the patient asking about?").

4.  **Biomedical:** Designed to summarize PubMed abstracts, assisting researchers by providing a quick overview.

5.  **Generic:** A non-clinical model added primarily for comparison purposes.

### **6. Performance and Implementation Details**

**Performance Comparison:** When tested on a clinical context (using documents from the MIMIC data set) and compared against state-of-the-art models like Pegasus, Bart, and T5, the clinical GSL models (base and augmented) performed better on **Rogue and BLEU scores** because they were specifically trained on clinical data.

In a BERT score comparison against GPT-4 generated summaries (used as a reference or "grant root"), the **Spark NLP base clinical GSL** model achieved a BERT score of **95**, showing near parity with GPT-4 for summarization on radiology text.

The main risk in clinical summarization is skipping important concepts. Since the information is generated based on the source document, the models do not suffer heavily from **hallucination**.

**Implementation:**

- Spark NLP models are run in a pipeline using the DocumentAssembler and the specific summarizer.

- The models can accept up to **1024 tokens of input** (about two full pages) and generate an output summary up to **512 tokens**; users can shorten the output token limit if needed (e.g., 100 tokens).

- The Augmented version usually returns a longer summary, while the slim/base version (summarizer_clinical_GSL) returns a shorter, more concise summary, which may be preferable for physicians who need immediate key points.

- The models can be deployed using the LightPipeline to avoid Spark overhead.

- Open-source models like Flan-T5 base and Pegasus, despite doing well in non-clinical contexts, did not perform well on clinical text during testing, often losing the entire context or returning only a single sentence.