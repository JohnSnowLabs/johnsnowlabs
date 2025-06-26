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

Terminology Server offers two types of search mechanisms:
* **Code Search** - searching for specific medical code  inside Terminology's Server curated **medical coding systems**.
* **Concept Search** - searching for medical terms/concepts, employing both **string matching** and **semantic search** when seeking **similarity searches** results as explaned below.  

## Code Search

Searching for a specific medical is very easy: type in the medical code you need to search for and hit enter. 

The system returns results in a tabular format; the result table includes the following information:

* Source Code System - the medical code system where the code belongs 
* Source Code - original medical code, used as inout search  
* Target Code System - the medical code system where the original code maps 
* Target Codes - mapped medical codes in other medical systems  

This means users can see how, for example E11 in ICD10 (Type 2 diabetes) maps to 10067585 in MEDDRA_PT( standardized, single medical concepts used to represent a symptom, sign, disease, diagnosis, etc) and how to E11 in ICD10CM (coding diseases, conditions, and injuries for statistical and billing purposes) maps to C0011847 in UMLS.

![Terminology Service by John Snow Labs](/assets/images/term_server/code_to_code_search_table.png)

## Concept Search

Terminology Server **concept search** capability excels by leveraging associated synonyms, accounting for **misspellings**, and employing both **string matching** and **semantic search** when seeking **similarity searches** results and when the system returns the best matching concept from the terminology embedding database.

The user can opt for either of the search types, or utilize both in tandem — this is the default setting.
Terminology Server offers stable and deterministic results. The same term(concept) will always return the same code, thanks to its reliance on official terminology datasets and carefully curated in-house augmentations.

Terminology Server performs term-level mapping: searching a term will return the best matching concept from the terminology database.

* It does not infer additional context or concepts beyond the input
* It does not perform document-level analysis.
* Providing an entire document as search input might lead to the embeddings becoming diluted, and potential nonsensical results.

 It is straight forward to choose between the type of search:
 1. Click on the Filters icon in the top right corner of the application
 2. Select the search type from the options from the Filters panel
 3. Exit the Filters panel by clicking anywhere outside


![Terminology Service by John Snow Labs](/assets/images/term_server/filter_panel.png)


It is posible to improve your search outcomes by utilizing a variety of additional filters:
* Domain: Specifies the general topic area of a concept (e.g., Condition/Device, Condition/Meas, Drug, Gender).

Choose from one of the available options to apply this filter using **one or more** pre-populated options in the dropdown list:

![Terminology Service by John Snow Labs](/assets/images/term_server/filter_panel_domains.png)

* OMOP Standards Concepts Only: Limits the search results to concepts that are flagged as “Standard” in the OMOP CDM.
* Include Only Valid Concepts: Filters out concepts that have been invalidated due to deletion or being superseded.
* Filter by Confidence Score: Allows refining results based on their confidence score.

