---
layout: docs
header: true
seotitle: Terminology Server | John Snow Labs
title: Terminology Server 
permalink: /docs/en/terminology_server/features/search
key: docs-term-server
modify_date: "2025-04-01"
show_nav: true
sidebar:
    nav: term-server
---

## Search

Terminology Server provides two distinct search modes:

* **Code Search** – Enables users to locate a specific medical code within the Terminology Server's curated set of medical coding systems.
* **Concept Search** – Allows users to search for medical terms or concepts using a combination of <ins>**exact text**</ins> matching and <ins>**semantic search**</ins> techniques to return similar or related concepts, as described in the section below.


## Code Search (code to code mapping)

Searching for a specific medical code is simple:
Just enter the code you want to find and press Enter. 

The results are displayed in a clear table format, which includes:

* Source Code System - The coding system where the searched code originates 
* Source Code - The original code entered by the user  
* Target Code System -  The coding system(s) where the source code is mapped 
* Target Codes - The equivalent or related codes in the target system(s)  

This means users can see how, for example E11 in ICD10 (Type 2 diabetes) maps to 10067585 in MEDDRA_PT( standardized, single medical concepts used to represent a symptom, sign, disease, diagnosis, etc) and how to E11 in ICD10CM (coding diseases, conditions, and injuries for statistical and billing purposes) maps to C0011847 in UMLS.

![Terminology Service by John Snow Labs](/assets/images/term_server/code_to_code_search_table.png)

A single medical code from a **Source Code System** may be mapped to one or more codes across multiple **Target Code Systems**.
In the left panel, the **Concept Maps** tree structure visually represents the medical coding systems where the searched code is present. Each **Concept Map** node displays child nodes corresponding to the target systems where mapped codes have been identified

To narrow down the search results to one or more Code Maps (Code Systems), follow these steps:

1. Locate the Concept Maps panel on the left side of the screen.
2. Identify the parent node that represents the source medical coding system where your searched code exists.
3. Under this parent node, you will see one or more child nodes—each representing a target coding system where mapped codes are available.
4. Click on a child node to filter the search results and display only the mappings between the source code and that specific target system.

This filtering helps streamline the results, allowing you to focus only on the coding systems relevant to your task.

![Terminology Service by John Snow Labs](/assets/images/term_server/MapCodes_MainPage.png)

## Concept Search (Semantic search & Exact match search)

Terminology Server **concept search** capability excels by leveraging associated synonyms, accounting for **misspellings**, and employing both <ins>**string matching**</ins> and <ins>**semantic search**</ins> when seeking **similarity searches** results and when the system returns the best matching concept from the terminology embedding database.

The user can opt for either of the search types, or utilize both in tandem — this is the default setting.
Terminology Server offers stable and deterministic results. The same term(concept) will always return the same code, thanks to its **reliance on official terminology datasets and carefully curated in-house augmentations**.

Terminology Server performs term-level mapping: searching a term will return the best matching concept from the terminology database.

* It does not infer additional context or concepts beyond the input
* It does not perform document-level analysis.
* Providing an entire document as search input might lead to the embeddings becoming diluted, and potential nonsensical results.

 It is straight forward to choose between the type of search:
 1. Click on the Filters icon in the top right corner of the application
 2. Select the search type from the options from the Filters panel
 3. Exit the Filters panel by clicking anywhere outside


![Terminology Service by John Snow Labs](/assets/images/term_server/filter_panel.png)


## Context Based Search

THis search modality employs **context-aware search** that **considers surrounding text** to find more accurate medical codes by **analyzing the clinical context in which terms appear**. It is a powerful feature that enhances the accuracy and relevance of search results by allowing users to include additional context when searching for medical terms.

Instead of relying solely on the keyword or phrase entered, this feature enables users to specify additional information like intended domain, clinical setting, diagnosis, procedure, medication, etc. By incorporating this context, the system can intelligently prioritize and rank results that are most relevant to the user's specific intent.

This functionality is especially useful when dealing with ambiguous or multi-use terms, helping to
* Reduce irrelevant results
* Improve precision for specialized domains
* Streamline workflows by surfacing the most applicable codes faster

**Context-Based Search** is ideal for clinicians, coders, and researchers who need to retrieve highly specific coding information tailored to their unique healthcare scenarios.

Narrow the search results by filtering by **Term Weight** and/or **Scope** using the User Interface tools as shown in the figure below.

![Terminology Service by John Snow Labs](/assets/images/term_server/context_resolution_search.png)


💡 **Tips for Effective Use**

* Use higher term weights when you're confident in your terminology
* Use lower term weights when context is critical for disambiguation
* Adjust scope based on how much surrounding context affects meaning
* Combine with vocabulary filters for more precise results

![Terminology Service by John Snow Labs](/assets/images/term_server/ContextBasedSearch.png)

![Terminology Service by John Snow Labs](/assets/images/term_server/ContextBasedSearchSamples.png)


## Boolean Search
  
When selecting the **Exact Text Search** option in the Filter panel, the query will allow the use of ```AND``` and ```OR``` operators to refine results:

**Using the ```AND``` operator**:

* Returns results where the document field contains all specified keywords, regardless of their order or position within the text.
* More than two terms can be inculded, for example: "leg ```AND``` tendons ```AND``` muscle" will return results that contain all three terms.

**Using the ```OR``` operator**:

* Returns results that contain any one or more of the specified keywords.
* The query supports multiple terms, for example: "diclofenac ```OR``` Eliquis ```OR``` clopidogrel" will return results containing any of the listed medications.

![Terminology Service by John Snow Labs](/assets/images/term_server/OR_operator.png)


## Spell Checker

When searching for a medical term, the Terminology Server will present a prommpt if it notice a potential spelling mistake. The user has the option  to accept the suggestion/correction or ignore it. 
The search results will reflect the choice, retreiving results using the system's suggestion or the original user's input:

![Terminology Service by John Snow Labs](/assets/images/term_server/Spellchecker.png)


## Additional Filters 

Improve your search outcomes by utilizing additional available filters:

* Domain: Specifies the general topic area of a concept (e.g., Condition/Device, Condition/Meas, Drug, Gender).

Choose from one of the available options to apply this filter using **one or more** pre-populated options in the dropdown list:

![Terminology Service by John Snow Labs](/assets/images/term_server/filter_panel_domains.png)

* OMOP Standards Concepts Only: Limits the search results to concepts that are flagged as “Standard” in the OMOP CDM.
* Include Only Valid Concepts: Filters out concepts that have been invalidated due to deletion or being superseded.
* Filter by Confidence Score: Allows refining results based on their confidence score.


## Core capabilities, strengths, and limitations

The following section compares the core capabilities, strengths, and limitations of John Snow Labs’ **Medical Terminology Server** (TS) with OpenAI’s large language models (LLMs) with , focusing on terminology mapping use cases in healthcare and life sciences.

1. **Deterministic Output vs. Generative Variability:**
    * TS offers stable and deterministic results. The same term will always return the same code, thanks to its reliance on official terminology datasets and carefully curated in-house augmentations.
    * OpenAI LLMs, such as GPT-4, are non-deterministic by design. The same prompt may yield different outputs across calls. Since LLMs do not have direct access to up-to-date, structured medical terminologies like SNOMED, ICD-10, RxNorm, etc., their accuracy is typically lower in structured terminology mapping. For a comparative benchmark, see our blog post: State-of-the-Art RxNorm Code Mapping with NLP, where we evaluated JSL’s resolver models against GPT-4 and Amazon for RxNorm mapping.

2. **Pricing and Licensing**
    * TS operates on a fixed licensing model. There are no usage-based charges or unexpected costs regardless of query volume.
    * OpenAI LLMs are priced per token, which can become expensive with large-scale usage or high-frequency requests.

3. **Deployment and Security**
    * TS can be deployed on-premises or in air-gapped environments with no internet connection, making it fully compliant with strict data privacy regulations (e.g., HIPAA, GDPR).
    * OpenAI LLMs can only be accessed via cloud APIs, which introduces compliance and security concerns in regulated environments.

4. **Interface and Integration**
    * TS comes with a user-friendly UI and a remote-accessible API, making it easy to use both as a standalone tool or as an embedded service in other systems.
    * OpenAI models are accessible only via API, with no native UI for terminology mapping use cases.

5. **Terminology Coverage and Customization**
    * TS supports:
        * **Value set mapping** (predefined or user-defined collections of concepts),
        * * **Concept mapping across vocabularies** (e.g., mapping SNOMED terms to ICD-10),
        * **Hierarchy navigation** within and across terminologies.
        * OpenAI **LLMs offer no native support** for value sets, concept hierarchies, or controlled vocabularies.

6. **Up-to-Date Terminologies**
    * TS ensures that its terminology databases are continuously updated in sync with changes made by official regulatory bodies (e.g., WHO, UMLS).
    * OpenAI LLMs are trained on static datasets and may take months or years to reflect terminology updates.

7. **Rate Limiting and Performance**
    * TS has no rate limitations. Users can process as many terms as needed under an active license.
    * OpenAI LLMs may impose rate limits depending on the subscription plan and system load

8. **Document-Level Understanding vs. Term-Level Mapping**

This is a **critical distinction** and often the source of confusion when comparing TS and LLMs.

* TS performs term-level mapping: You input a term, and it returns the best matching concept from the terminology database.
    * It does not infer additional context or concepts beyond the input
    * It does not perform document-level analysis.
    * If a user inputs an entire document, the embeddings become diluted, and results may be nonsensical.
* OpenAI LLMs excel at document-level analysis:
    * They can extract key clinical findings, inferred diagnoses, and primary/secondary conditions by analyzing the full context of a clinical note or discharge summary.
    * LLMs can assign ICD-10 or SNOMED codes based on this inferred context—mimicking human coders.
    * This behavior makes LLMs appealing for use cases where document-level abstraction and coding are required.

**Example**:

Uploading a discharge summary to GPT-4 and prompting it to extract ICD-10 codes may result in:

* Primary diagnosis
* Secondary diagnoses
* Procedures
* Medications
* … all inferred from context.

In contrast, submitting the same text to TS:

* Will treat the whole input as a single term.
* Return a single code based on embedding similarity, which may be inaccurate if the document is lengthy or complex.

9. **Flexibility and Future Integration**
    * While TS is not designed for document-level LLM-style coding, it is possible to embed JSL’s proprietary small LLMs within TS to enable such capabilities—if there is demand.
    * This hybrid approach could provide the best of both worlds: deterministic, terminology-backed mapping with optional contextual inference.


🚦Recommendation

Before choosing between TS and OpenAI LLMs for terminology mapping, clearly define your goal:

* If you need accurate, up-to-date, and secure mapping for individual terms or structured applications—TS is the better choice.
* If you want AI-driven abstraction from unstructured clinical text (e.g., coding a discharge summary)—LLMs might be more appropriate, though at the cost of accuracy and explainability.

For hybrid use cases, John Snow Labs offers modular and extensible solutions to support both deterministic terminology mapping and generative document understanding, as needed
