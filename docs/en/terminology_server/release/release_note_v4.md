---
layout: docs
header: true
seotitle: Release Notes  | Terminology Server | John Snow Labs
title: Terminology Server Release Notes
permalink: /docs/en/terminology_server/release/release_note_v4
key: docs-term-server
modify_date: "2026-02-23"
show_nav: true
sidebar:
    nav: term-server
---

## Terminology Server v4 Release Notes

<p style="text-align:center;">Release date: {{ page.modify_date | date: '%m-%d-%Y' }}</p>

## Document Search Functionality

Added document search capabilities, allowing users to search and extract medical terminlogies from medical entities in different file types, including PDF, TXT, DOCX, and DOC. More details available [here](/docs/en/terminology_server/features/search#document-search)

**Fast Search**
Uses a schema-aligned Named Entity Recognition (NER) model. It extracts predefined clinical entities according to a fixed schema, producing consistent and deterministic results. Entities found in documents are mapped directly to well-defined, official code systems—the output is reliable and repeatable for the same input.

![Fast Document Search](/assets/images/term_server/fast-doc-search.png)

**Accurate Search**

Operates with a pretrained clinical zero-shot entity recognition model. Rather than using only fixed labels, users can define or modify entity labels at runtime, allowing the model to interpret text more flexibly. Entities can be mapped to different code systems based on user mappings, supporting customized and probabilistic extraction tuned to specific workflows or organizational needs.

![Accurate Document Search](/assets/images/term_server/accurate-doc-search.png)

## Public ValueSets Availability

Public ValueSets from the TUVA projects are now available in the Terminology Server.

These comprehensive public ValueSets enable standardized mapping and interoperability across healthcare systems, support regulatory compliance, and accelerate clinical and analytics workflows by providing consistent reference terminologies out-of-the-box.

![Public Value Sets](/assets/images/term_server/public_valuesets.png)

## More Code Systems(Vocabulary)

All available Code Systems available via the platform.

- ABMS
- AMT
- APC
- ATC
- BDPM
- CDM
- CMS Place of Service
- CPT4
- CVX
- Cancer Modifier
- Concept Class
- Condition Status
- Condition Type
- Cost
- Cost Type
- Currency
- DRG
- Death Type
- Device Type
- Domain
- Drug Type
- EORTC QLQ
- EphMRA ATC
- Episode
- Episode Type
- Ethnicity
- GGR
- Gender
- HCPCS
- HES Specialty
- HGNC
- HPO
- HemOnc
- ICD10
- ICD10CM
- ICD10PCS
- ICD9CM
- ICD9Proc
- ICDO3
- JMDC
- KDC
- Korean Revenue Code
- LOINC
- Language
- MDC
- MMI
- MeSH
- MeSH Veterinary
- Meas Type
- MedDRA_LLT
- MedDRA_PT
- Medicare Specialty
- Metadata
- Multum
- NAACCR
- NCIt
- NDC
- NFC
- NUCC
- Nebraska Lexicon
- Note Type
- OMOP Extension
- OMOP Genomic
- OMOP Invest Drug
- OPCS4
- OSM
- Obs Period Type
- Observation Type
- PCORNet
- PPI
- Plan
- Plan Stop Reason
- Procedure Type
- Provider
- Race
- Relationship
- Revenue Code
- RxNorm
- RxNorm Extension
- SMQ
- SNOMED
- SNOMED Veterinary
- SOPT
- SPL
- Specimen Type
- Sponsor
- Supplier
- Type Concept
- UB04 Point of Origin
- UB04 Pri Typ of Adm
- UB04 Pt dis status
- UB04 Typ bill
- UCUM
- UMLS
- US Census
- VANDF
- Visit
- Visit Type
- Vocabulary
- dm+d


## Agent Integration via MCP Server
- Agents (automation bots, clinical support tools, data analytics platforms) can connect directly to the Terminology Server using the Model Context Protocol (MCP) Server and register its search functions as tools for seamless integration.
- All major Terminology Server search features—Concept Search, Context Resolution, Code Search, Document Search—are accessible as programmable modules for automating workflows and powering decision-support engines.
- The tool registration framework enables flexible, scalable workflow orchestration: medical concept lookup, code mapping, entity extraction, compliance checks, and more.
- This empowers organizations to leverage real-time terminology intelligence, mapping, and regulatory compliance through agent-driven access, ensuring both operational consistency and interoperability.

- API access is secured through API keys linked to user accounts, ensuring that only authorized users can interact with the API endpoints.

## Improvements

* UI Facelift: The Terminology Server UI has been modernized with an improved layout, refreshed color palette, and enhanced navigation. The update brings a more intuitive, responsive design, better accessibility, and a cleaner interface for users.
  ![Term-To-Code-Search](/assets/images/term_server/term-to-code-search.png)
* Added endpoint to generate embeddings for medical terms.
* Added a TopK slider input in the Filters panel.
* Enhanced query performance for faster search results.


## Bugfixes

* Fixed issue when downloading valueset for certain user roles
* Fixed issue where duplicate entries were shown on the search results grid.
* Fixed issue where there was problem to connecting to Terminology Server Database stored on AWS RDS.

<div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-terminology-pagination.html -%}
