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
* **Concept Search** – Allows users to search for medical terms or concepts using a combination of exact text matching and semantic search techniques to return similar or related concepts, as described in the section below.


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

Terminology Server **concept search** capability excels by leveraging associated synonyms, accounting for **misspellings**, and employing both **string matching** and **semantic search** when seeking **similarity searches** results and when the system returns the best matching concept from the terminology embedding database.

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

Context-aware search that considers surrounding text to find more accurate medical codes by analyzing the clinical context in which terms appear.It is a powerful feature that enhances the accuracy and relevance of search results by allowing users to include additional context when searching for medical terms.

Instead of relying solely on the keyword or phrase entered, this feature enables users to specify additional information like intended domain, clinical setting, diagnosis, procedure, medication, etc. By incorporating this context, the system can intelligently prioritize and rank results that are most relevant to the user's specific intent.

This functionality is especially useful when dealing with ambiguous or multi-use terms, helping to
* Reduce irrelevant results
* Improve precision for specialized domains
* Streamline workflows by surfacing the most applicable codes faster

Context-Based Search is ideal for clinicians, coders, and researchers who need to retrieve highly specific coding information tailored to their unique healthcare scenarios.

Narrow the search results by filtering by **Term Weight** and/or **Scope**:

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

When searching for a medical term, the Terminology Server will present a prommpt if it notice a spelling mistake was done. The option is to accept the correction or ignore it. The results will reflect the choice to go with the system's suggestion or original input:

![Terminology Service by John Snow Labs](/assets/images/term_server/Spellchecker.png)


## Additional Filters 

Improve your search outcomes by utilizing additional available filters:

* Domain: Specifies the general topic area of a concept (e.g., Condition/Device, Condition/Meas, Drug, Gender).

Choose from one of the available options to apply this filter using **one or more** pre-populated options in the dropdown list:

![Terminology Service by John Snow Labs](/assets/images/term_server/filter_panel_domains.png)

* OMOP Standards Concepts Only: Limits the search results to concepts that are flagged as “Standard” in the OMOP CDM.
* Include Only Valid Concepts: Filters out concepts that have been invalidated due to deletion or being superseded.
* Filter by Confidence Score: Allows refining results based on their confidence score.

