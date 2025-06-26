---
layout: docs
header: true
seotitle: Terminology Server | John Snow Labs
title: Terminology Server 
permalink: /docs/en/terminology_server/features/code_systems
key: docs-term-server
modify_date: "2025-04-01"
show_nav: true
sidebar:
    nav: term-server
---

## Code Systems

In healthcare, **medical coding systems** are standardized sets of codes used to classify diseases, treatments, medications, lab results, and clinical concepts.
Each system serves a specific purpose:
* ICD10: Classifies diseases and health conditions.
* CPT4: Used to describe medical procedures and services.
* LOINC: Codes for lab tests and clinical measurements.
* RxNorm: Normalized names for drugs and medications.
* SNOMED CT: A comprehensive system for clinical terms used in electronic health records.
* UMLS: A unifying system that connects terms across multiple vocabularies.
* MeSH: Medical subject headings used in biomedical literature indexing.

Each system uses codes (e.g., E11 for Type 2 Diabetes in ICD10) to represent a specific medical concept.

Different healthcare roles and use cases require different systems:

* A physician documents diagnoses using ICD10.
* A lab uses LOINC to record test results.
* A pharmacist references RxNorm to prescribe medications.
* A clinical researcher might use MeSH to search publications.

This diversity improves accuracy and efficiency within each domain—but it also creates fragmentation.

⚠️ The Challenge
When data is spread across different coding systems, it becomes difficult to:

* Exchange information across systems or institutions.
* Analyze data uniformly.
* Integrate clinical and administrative workflows.

For example, one system may document a condition as “Essential Hypertension” (SNOMED), while another uses the ICD10 code I10.

✅ The Solution: Search and Map Across Systems
Terminology Server application solves this problem by:

* Letting users search for medical concepts (e.g., “diabetes,” “hypertension”) across multiple systems at once.
* Returning the corresponding codes in each system.
* Showing mappings—links between equivalent or related codes across systems.

This means users can see how E11 in ICD10 (Type 2 diabetes) maps to 10067585 in MEDDRA_PT( standardized, single medical concepts used to represent a symptom, sign, disease, diagnosis, etc) and how to E11 in ICD10CM (coding diseases, conditions, and injuries for statistical and billing purposes) maps to C0011847 in UMLS.

![Terminology Service by John Snow Labs](/assets/images/code_to_code_search.png)
