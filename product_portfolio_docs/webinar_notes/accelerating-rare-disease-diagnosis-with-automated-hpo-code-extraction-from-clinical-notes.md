# Accelerating Rare Disease Diagnosis with Automated HPO Code Extraction from Clinical Notes
Accelerating Rare Disease Diagnosis with Automated HPO Code Extraction from Clinical Notes

<https://www.johnsnowlabs.com/accelerating-rare-disease-diagnosis-with-automated-hpo-code-extraction-from-clinical-notes/>

<https://youtu.be/fITNL25ca6E>

<img src="/media/image.jpg" title="Video titled: Accelerating Rare Disease Diagnosis with Automated HPO Code Extraction from Clinical Notes" style="width:6.3125in;height:3.65625in" />

The content of the recording, which focuses on the **automation of Human Phenotype Ontology (HPO) code extraction** by Johnson Labs (GSL) for accelerating rare disease diagnosis, is summarized in detail below.

## **Detailed Summary of HPO Code Extraction Presentation**

The presentation defines phenotypes, highlights the importance of timely diagnosis for rare diseases, details the John Snow Labs (JSL) automated solution, and compares its performance against other methods, including LLMs and open-source libraries.

### **1. Phenotypes and the Challenge of Rare Diseases**

**Definition and Importance of Phenotypes:** Phenotypes are the observable clinical characteristics of an individual. They are manifestations influenced by genetic makeup and environmental factors (like diet, lifestyle, and climate). In medicine, phenotypes are clinically observable signs or symptoms (e.g., ataxia, sudden movements), clinical findings, lab results (e.g., glucose levels), or imaging results (e.g., MRI).

**Rare Disease Impact and Diagnosis:** Although called "rare," these diseases affect approximately 300 million people globally, impacting almost 6% of the human population. In the US, about one out of every 10 Americans has a rare disease.

The diagnostic process is severely protracted:

- It typically takes **around six years** to receive a diagnosis after symptoms begin.

- A patient often consults maybe **eight different doctors** before a diagnosis is reached.

- There are about 7,000 types of rare diseases/disorders.

- A major challenge is treatment; only **5% of these diseases have an FDA-approved drug treatment**. Furthermore, 80% of rare diseases are genetic.

### **2. Human Phenotype Ontology (HPO)**

The Human Phenotype Ontology (HPO) is the main subject used to standardize the description of abnormalities.

- HPO consists of **18,000 unique terms with unique codes**.

- These terms describe specific abnormalities or clinical features (phenotypes), but they do not describe diseases or syndromes themselves.

- HPO is hierarchical, meaning terms have immediate and higher parent terms.

- Examples of phenotypes include "muscle weakness" or "intellectual disability," which may be related to specific syndromes like Marfan syndrome.

### **3. Automation vs. Manual Diagnosis**

Extracting HPO codes is crucial for quick diagnosis, especially when working with vast amounts of unstructured text (hundreds of thousands or millions of clinical documents). Manual approaches by doctors or specialized nurses are slow, prone to human error, and difficult to scale.

Automation dramatically improves efficiency and coverage:

- **Time Required:** Manual processes take significantly longer (e.g., 100 time units) compared to automated processes (e.g., 40 time units) for diagnosis.

- **Expert Time:** Expert time required drops significantly (e.g., from 100 down to 30 time units).

- **Phenotype Coverage:** Automation extracts far more phenotypes. In one comparison, manual HPO coding extracted 7.3 phenotypes per document, while automated HPO coding extracted **27.8 phenotypes** (almost four times more).

### **4. John Snow Labs (JSL) HPO Extraction Solution**

JSL developed an advanced pipeline, currently in its fourth version, to address the complexity of extracting phenotypes from clinical text.

**Pipeline Architecture and Components:**

1.  **Initial Challenge:** Initial attempts to use traditional deep learning **NER (Named Entity Recognition) models failed** to achieve sufficient accuracy, specifically struggling to differentiate clearly between a phenotype and a general disease, sign, or symptom.

2.  **Current Hybrid Approach:** The successful pipeline utilizes **rule-based methods**, **fuzzy matching** (to handle doctor abbreviations and typos common in "messy" clinical data), and processes to identify the root of the word (lemma) to manage synonyms.

3.  **Assertion/Negation Handling:** This is a crucial step. The assertion model filters whether the phenotype is **present** in the patient (requiring an HPO code), **absent**, or associated with **someone else** (e.g., a family member), which means the HPO code must be excluded for the patient.

4.  **HPO Code Mapping:** Once the relevant phenotypes are filtered as "present," they are mapped to the HPO codes quickly and accurately.

5.  **Mappers for Utility:** The pipeline includes multiple mappers to enrich the output and provide structure:

    1.  **Synonym Mapper:** Finds exact, related, and broad synonyms for phenotypes.

    2.  **Parent Mapper:** Identifies the immediate parent and higher ancestors in the HPO hierarchy.

    3.  **Gene Mapper:** Links the HPO code to related genes and potential associated diseases (critical since 80% of rare diseases are genetic).

    4.  **UMLS Mapper:** Provides the primary UMLS code and candidate codes related to the specific HPO code.

**Output:** The solution transforms unstructured clinical text into structured data (like a data frame) containing the phenotype, its HPO code, synonyms, UMLS codes, and associated genes, making diagnosis easier. The entire pre-trained solution (**HPOM mapper pipeline version 4**) can be run using a single line of code.

### **5. Performance Comparison**

JSL compared its pipeline against the open-source **Clinfen** library and state-of-the-art **LLMs** (OpenAI GPT-4 and Gemini Pro).

| **Metric Evaluated** | **JSL Pipeline** | **Clinphen** | **Gemini Pro** | **OpenAI GPT-4** |
|:---|:---|:---|:---|:---|
| **Phenotype (Chunk) Extraction** | **~99%** | \< 5% | \> 84% | ~78% |
| **HPO Code Mapping Accuracy** | **98.84%** | ~40% | ~60% | \< 54% |

**Shortcomings of Competitors:**

- **LLMs:** While good at extracting the initial text chunk (84% or 78% accuracy), LLMs are not reliable for the crucial step of HPO code mapping, performing below 60% accuracy. They are also expensive, prone to hallucination, and struggle with correct assertion/negation handling.

- **Clinfen:** Clinphen performed poorly because it lacks the full HPO dataset (having \< 14,000 codes). It uses basic NLP and struggles with linguistic complexities, often failing to handle negation correctly (e.g., extracting an HPO code even when "no seizures observed" is stated) and struggling when a single adjective modifies multiple nouns (e.g., "fused nails and teeth").

The JSL pipeline achieved significantly higher accuracy in both phenotype extraction and, critically, the **accurate mapping to HPO codes** (98.84%).