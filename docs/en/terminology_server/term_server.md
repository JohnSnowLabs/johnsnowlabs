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

🚀 The super power of John Snow Lab's Terminology Server is **search**: its use of associated synonyms, misspellings, the use of both string matching as well as embedding matches (similarity search). 

🚀 Choose between **exact text match** and **semantic search** or combine this two options together - **default** behaviour.

🚀 **Custom Value Sets Management**: 
* Create custom Value Sets and use them to filter the search results using the data for the specific version of the selected Value Set.
* Create new versions of existing Value Set using Upload mechanism.
* View data of selected Value Set whitin the application.  

🚀 **Concept Maps**: 
For any Code System selected as the data source when searching for a term, the Terminology Server application allows the selection of one or more "connected" Code System for the selected one.
This method will display results of equivalent concept codes in differnet systems, when data exists.   

🚀 **Additional Filters**:
Optimie the search results by usinf additional filters like: 
* Domain - describes the basic topic area of a concept (Condition/Device, Condition/Meas, Drug, Gender, etc.). The actual values of this filter are pre-populated in the drop down list for this filter
* OMOP Standards Concpets only - constrains concepts returned to those with the "Standard" flag in the OMOP CDM
* Include Only Valid Concepts - a concept can become invalid if deleted or superceded
* Filter by Confidence Score

 🚀 **API service**:
The API service allows seamless integration with your applications, enabling you to leverage our platform's capabilities. By obtaining an API key, developers can interact with various endpoints to retrieve and manipulate data, ensuring smooth connectivity with external systems. Detailed documentation is available to guide you through authentication, rate limits, and usage examples, making the integration process straightforward.


**Main Page**

Overview of Terminology Server's main page and features:


![Terminology Service by John Snow Labs](/assets/images/TS1.png)


**Concepts maps**

Concept code mappings shown in the grid results, together with additional filters: 

![Terminology Service by John Snow Labs](/assets/images/TS2.png)


**Manage Value Sets**

Create, Add new or Update (new version), View data of custom Value Sets:  

![Terminology Service by John Snow Labs](/assets/images/TS3.png)
