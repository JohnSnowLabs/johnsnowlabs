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


**Main Page**

Overview of Terminology Server's main page and features:


![Terminology Service by John Snow Labs](/assets/images/TS1.png)


**Concepts maps**

Concept code mappings shown in the grid results, together with additional filters: 

![Terminology Service by John Snow Labs](/assets/images/TS2.png)


**Manage Value Sets**

Create, Add new or Update (new version), View data of custom Value Sets:  

![Terminology Service by John Snow Labs](/assets/images/TS3.png)
