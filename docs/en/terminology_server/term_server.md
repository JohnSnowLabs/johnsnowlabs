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

The **Medical Terminology Server** offers users the ability to look up standard medical codes from text phrases. It uses both **string matching** and **embeddings** to efficiently search for concepts across **multiple vocabularies**, with filters that can constrain results to meet your specific needs. 

The Medical Terminology Server combines **up-to-date editions of a wide range of terminologies** with extensive supplementary datasets of synonyms, common misspellings, and colloquialisms to provide code mappings for input text, whether it is from the clinical record, patient statements, or other sources of written information about health. 

In addition to being to select from many standard vocabularies, the Medical Terminology Server is also **aware of OMOP CDM conventions**. It can also be constrained to only return codes that are OMOP Standard concepts and is able to check any concept for current validity. Batch transaction support makes efficient use of network calls.


## Highlights
* **Tailored for healthcare**, the Medical Terminology Server allows uses data created by using state of the art **John Snow Labs models** that understands the nuances of clinical language and medical terminologies, ensuring that the information it generates is accurate and highly relevant.
* The Medical Terminology Server comes **pre-loaded with all widely used medical terminologies**; it offers a **robust API** and user interface that enable advanced concept search, mapping, and normalization.
* The Medical Terminology Server addresses challenges often faced by traditional terminology servers in healthcare: identifying concepts without exact matches by correcting spelling errors and using synonyms; finding the **most relevant concept** based on **clinical context** for accurate coding of diagnoses, drugs, treatments, or adverse events; identifying semantically close concepts for terms that may vary in expression, such as ICD-10 descriptions or prescriptions.
