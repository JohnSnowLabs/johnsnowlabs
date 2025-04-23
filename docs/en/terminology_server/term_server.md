---
layout: docs
header: true
seotitle: Terminology Server | John Snow Labs
title: Terminology Server 
permalink: /docs/en/terminology_server/term_server
key: docs-term-server
modify_date: "2025-04-01"
show_nav: true
sidebar:
    nav: term-server
---

The Medical Terminology Server offers users the ability to look up standard medical codes from text phrases. It uses both string matching and embeddings to efficiently search for concepts across multiple vocabularies, with filters that can constrain results to meet your specific needs. 

The Medical Terminology Server combines up-to-date editions of a wide range of terminologies with extensive supplementary datasets of synonyms, common misspellings, and colloquialisms to provide code mappings for input text, whether it is from the clinical record, patient statements, or other sources of written information about health. In addition to being to select from many standard vocabularies, the Medical Terminology Server is also aware of OMOP CDM conventions. It can also be constrained to only return codes that are OMOP Standard concepts and is able to check any concept for current validity. Batch transaction support makes efficient use of network calls.


## Highlights
* Tailored for healthcare, the Medical Terminology Server allows the use on state of the art JSL models that understands the nuances of clinical language and medical terminologies, ensuring that the information it generates is accurate and highly relevant. The Medical Terminology Server comes pre-loaded with all widely used medical terminologies; it offers a robust API and user interface that enable advanced concept search, mapping, and normalization

* The Medical Terminology Server addresses challenges often faced by traditional terminology servers in healthcare: identifying concepts without exact matches by correcting spelling errors and using synonyms; finding the most relevant concept based on clinical context for accurate coding of diagnoses, drugs, treatments, or adverse events; identifying semantically close concepts for terms that may vary in expression, such as ICD-10 descriptions or prescriptions.


## Features

🚀 The standout feature of John Snow Lab's Terminology Server is its **search** capability: it excels by leveraging associated synonyms, accounting for misspellings, and employing both string matching and embedding matches for similarity searches.

🚀 Opt for either exact text match or semantic search, or utilize both in tandem — the default setting.

🚀 **Custom Value Sets Management**:

* Craft custom Value Sets and apply them as filters to refine search outcomes based on data from a specific version of the chosen Value Set.
* Generate new versions of an existing Value Set through the upload feature.
* Access and review the data of any selected Value Set within the application.  

🚀 **Concept Maps**: 
When searching for a term in the Terminology Server application from a chosen Code System, users have the option to select one or more "connected" Code Systems. This feature allows for the display of corresponding concept codes across various systems, assuming such data is accessible.  

🚀 **Additional Filters**:
Improve your search outcomes by utilizing a variety of additional filters:

* **Domain**: Specifies the general topic area of a concept (e.g., Condition/Device, Condition/Meas, Drug, Gender). The available options for this filter are pre-populated in the dropdown list.
* **OMOP Standards Concepts Only**: Limits the search results to concepts that are flagged as "Standard" in the OMOP CDM.
* **Include Only Valid Concepts**: Filters out concepts that have been invalidated due to deletion or being superseded.
* **Filter by Confidence Score**: Allows refining results based on their confidence score.

 🚀 **API service**:
The API service allows seamless integration with your applications, enabling you to leverage our platform's capabilities. By obtaining an API key, developers can interact with various endpoints to retrieve and manipulate data, ensuring smooth connectivity with external systems. Detailed documentation is available to guide you through authentication, rate limits, and usage examples, making the integration process straightforward.

🔍 **Core capabilities, strengths, and limitations**

The following section compares the core capabilities, strengths, and limitations of John Snow Labs’ Medical Terminology Server (TS) with OpenAI’s large language models (LLMs) with , focusing on terminology mapping use cases in healthcare and life sciences.

1. **Deterministic Output vs. Generative Variability:**
    * **TS** offers stable and deterministic results. The same term will always return the same code, thanks to its reliance on official terminology datasets and carefully curated in-house augmentations.
    * **OpenAI LLMs**, such as GPT-4, are non-deterministic by design. The same prompt may yield different outputs across calls. Since LLMs do not have direct access to up-to-date, structured medical terminologies like SNOMED, ICD-10, RxNorm, etc., their accuracy is typically lower in structured terminology mapping.
For a comparative benchmark, see our blog post: State-of-the-Art RxNorm Code Mapping with NLP, where we evaluated JSL's resolver models against GPT-4 and Amazon for RxNorm mapping.

2. **Pricing and Licensing**
   * **TS** operates on a fixed licensing model. There are no usage-based charges or unexpected costs regardless of query volume.
   * **OpenAI LLMs** are priced per token, which can become expensive with large-scale usage or high-frequency requests.
  
3. **Deployment and Security**
   * **TS** can be deployed on-premises or in air-gapped environments with no internet connection, making it fully compliant with strict data privacy regulations (e.g., HIPAA, GDPR).
   * **OpenAI LLMs** can only be accessed via cloud APIs, which introduces compliance and security concerns in regulated environments.
     
4. **Interface and Integration**
   * **TS** comes with a user-friendly UI and a remote-accessible API, making it easy to use both as a standalone tool or as an embedded service in other systems.
   * **OpenAI models** are accessible only via API, with no native UI for terminology mapping use cases.
5. **Terminology Coverage and Customization**
    * **TS** supports:
        * **Value set mapping** (predefined or user-defined collections of concepts),
        * **Concept mapping across vocabularies** (e.g., mapping SNOMED terms to ICD-10),
        * **Hierarchy navigation** within and across terminologies.
        * **OpenAI LLMs** offer no native support for value sets, concept hierarchies, or controlled vocabularies.
6. **Up-to-Date Terminologies**
    * **TS** ensures that its terminology databases are continuously updated in sync with changes made by official regulatory bodies (e.g., WHO, UMLS).
    * **OpenAI LLMs** are trained on static datasets and may take months or years to reflect terminology updates.
7. **Rate Limiting and Performance**
    * **TS** has no rate limitations. Users can process as many terms as needed under an active license.
    * **OpenAI LLMs** may impose rate limits depending on the subscription plan and system load
8. **Document-Level Understanding vs. Term-Level Mapping**

    This is a **critical distinction** and often the source of confusion when comparing TS and LLMs.

    * **TS** performs **term-level mapping**: You input a term, and it returns the best matching concept from the terminology database.
        * It **does not** infer additional context or concepts beyond the input
        * It **does not** perform document-level analysis.
        * If a user inputs an entire document, the embeddings become diluted, and results may be nonsensical.
    * **OpenAI LLMs** excel at **document-level analysis**:
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
   
🚦**Recommendation**

Before choosing between TS and OpenAI LLMs for terminology mapping, clearly define your goal:
* If you need accurate, up-to-date, and secure mapping for individual terms or structured applications—TS is the better choice.
* If you want AI-driven abstraction from unstructured clinical text (e.g., coding a discharge summary)—LLMs might be more appropriate, though at the cost of accuracy and explainability.

For hybrid use cases, John Snow Labs offers modular and extensible solutions to support both deterministic terminology mapping and generative document understanding, as needed


**Overview of Terminology Server's main page and features:**

Main Page


![Terminology Service by John Snow Labs](/assets/images/TS1.png)


**Concepts maps**

Concept code mappings shown in the grid results, together with additional filters: 

![Terminology Service by John Snow Labs](/assets/images/TS2.png)


**Manage Value Sets**

Create, Add new or Update (new version), View data of custom Value Sets:  

![Terminology Service by John Snow Labs](/assets/images/TS3.png)
