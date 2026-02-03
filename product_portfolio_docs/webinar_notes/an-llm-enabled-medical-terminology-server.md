# An LLM-enabled Medical Terminology Server
An LLM-enabled Medical Terminology Server

https://www.johnsnowlabs.com/an-llm-enabled-medical-terminology-server/

<https://youtu.be/7FKjOojyeB4>

<img src="/media/image.jpg" title="Video titled: An LLM-enabled Medical Terminology Server" style="width:6.3125in;height:3.65625in" />

The following is a detailed summary of the speech presented in the source, which describes the **Large Language Model (LLM)-enabled Medical Terminology Server** developed by John Snow Labs (JSL). The presentation was given by Kate Weber, a data scientist at JSL specializing in data standards in healthcare and Natural Language Processing (NLP).

The goal of the service is to provide a significant improvement over current methods for searching for medical codes in a terminology server.

## **I. Context and Purpose of Medical Coding Systems**

Medical coding systems arose from the need to ensure consistency and precision in healthcare communication and data handling. They address the chaos of nonspecific human language.

**Key Purposes of Coding Systems:**

- **Billing:** Ensuring financial partners recognize and standardize codes for specific procedures.

- **Precision:** Standardizing values from laboratory panels so that different users mean the same specific test and resulting values.

- **Translation:** Translating concepts across literal languages (e.g., the Mesh code 5360 translates to the word *fibula* in a user's native language).

- **Reporting and Research:** Providing hierarchical relationships that allow researchers to roll up thousands of specific codes into broader concepts (e.g., finding all patients taking any drug containing codeine using the RxNorm vocabulary).

### **Common Coding Systems Discussed:**

- **Medical Subject Headings (MeSH):** Used for classifying research papers in specific, reproducible terms.

- **CPT (Current Procedural Terminology):** The American Medical Association's system for describing different procedure codes.

- **LOINC (Logical Observation Identifiers Names and Codes):** Focused mainly on laboratory results, but also organizes documents, quizzes, questions, and answers.

- **ICD-10 (International Classification of Diseases, 10th Revision):** The most commonly used version for listing diagnoses. It was founded on insurers' needs to understand and report specific afflictions and claim payments, leading it to sometimes be **"ridiculously specific"**.

- **SNOMED CT (Systematized Nomenclature of Medicine-Clinical Terms):** A global, broad vocabulary that connects relationships across concepts like body parts and procedures.

- **RxNorm:** A standard hierarchy of drug products.

## **II. Challenges in Medical Coding**

Despite their intended purpose, coding systems can sometimes cause their own chaos due to the complexities of human language and the varying needs that drove their development.

- **Synonymy:** The need to treat related terms, like **"hypertension and high blood pressure,"** as similar concepts.

- **Varying Levels of Detail:** Different systems have different granularity. For example, ICD-10 creates a **single, specific code** by bolting together small ideas (e.g., differentiating three-wheel vs. four-wheel motor vehicle accidents). In contrast, SNOMED CT asks the user to **stack multiple codes** together to convey the same complex meaning (e.g., codes for accident, driver, and fracture).

- **Mapping Difficulty:** Translating concepts between vocabularies, especially those with different levels of detail, is difficult.

### **Approaches to Vocabulary Mapping:**

1.  **Unified Medical Language System (UMLS):** A product of the US National Library of Medicine that attempts to create one central collection of concepts (a meta-vocabulary) and map those concepts out to 35 different vocabularies.

2.  **The OHDSI Initiative:** Focuses on bringing health data together from different sources (like Epic and Cerner) for observational research. It maps many vocabularies into specific OHDSI standard concepts.

### **Fire Standards and Terminology Management**

The **FHIR (Fast Healthcare Interoperability Resources) standards** address some of this chaos by introducing two key ideas utilized by the terminology server:

1.  **Value Set:** A subset or collection of concepts drawn from *any* vocabulary (ICD-10, LOINC, SNOMED CT, etc.). It allows users to define a collection of concepts for specific purposes, such as billing, reporting, or identifying a patient population (e.g., all patients positive for leukemia).

2.  **Concept Map:** Allows for mapping between vocabularies. Users can build **custom concept maps** using FHIR, mapping a standard code (e.g., a SNOMED code) to a custom in-house code system.

## **III. John Snow Labs' LLM-Enabled Terminology Server**

JSL's new server leverages LLMs to overcome the limitations of traditional, string-focused code lookup tools.

### **Core Technology: Semantic Matching**

Traditional tools rely on exact or fuzzy string searches (e.g., Tu\*bercul\*o\*w\*). The JSL server uses an LLM to determine the **semantic meaning**-the core understanding-between a word typed in the search and the terms in the vocabulary.

- This allows the server to correctly match layman terms (e.g., typing **"high blood pressure"** and getting back **"hypertension"**), correct spelling errors, and handle different cultural words for the same thing.

- The server performs an **exact text search** first, and if that fails, it proceeds to **semantic matching**.

### **Key Features and Capabilities**

- **Vocabulary Coverage:** The server has **24 common vocabularies** loaded and kept up to date.

- **OMOP Support:** It identifies when presented concepts are **OMOP standard concepts**, which is critical for those working on mappings in the OMOP world.

- **Multilingual Support:** The server is not specific to English; a Chinese LOINC dataset is loaded, enabling semantic matching for non-English terms.

- **Concept Mapping:** It maintains mappings between vocabularies (e.g., mapping SNOMED CT concepts to their equivalent UMLS concept codes or KUIs).

- **Custom Value Sets:** Users can upload their own **custom value sets** to constrain searches or filter results. The server supports **version control** for updating value sets.

- **Interface:** It offers both a **graphic user interface (GUI)** and an **API-based interaction**.

- **API Functionality:** The API endpoint is designed for high-volume use. It allows filtering by vocabulary ID, controlling the number of returns, filtering by value sets, and providing detailed output including a **confidence score** and information about standard concepts.

- **Deployment and Security:** The server is designed for deployment **within the user's own environment** (their security perimeter/infrastructure), ensuring data privacy and preventing external calls.

### **Integration with JSL Patient Journeys**

The terminology server is a critical part of the **John Snow Labs' Patient Journeys product**. Patient Journeys takes various inputs (EHR, FHIR messaging, clinical notes) and converts the information into the **OMOP standard common data model**, allowing LLMs to properly search and understand the longitudinal patient story.