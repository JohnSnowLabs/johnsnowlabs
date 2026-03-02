---
layout: docs
header: true
seotitle: Release Notes  | Terminology Server | John Snow Labs
title: Terminology Server Release Notes
permalink: /docs/en/terminology_server/release/latest_release
key: docs-term-server
modify_date: "2026-03-01"
show_nav: true
sidebar:
    nav: term-server
---

<div class="h3-box" markdown="1">

<p style="text-align:center;" markdown="1">Release date: {{ page.modify_date | date: '%m-%d-%Y' }}</p>

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

## Agent Integration via MCP Server
- Agents (automation bots, clinical support tools, data analytics platforms) can connect directly to the Terminology Server using the Model Context Protocol (MCP) Server and register its search functions as tools for seamless integration.
- All major Terminology Server search features—Concept Search, Context Resolution, Code Search, Document Search—are accessible as programmable modules for automating workflows and powering decision-support engines.
- The tool registration framework enables flexible, scalable workflow orchestration: medical concept lookup, code mapping, entity extraction, compliance checks, and more.
- This empowers organizations to leverage real-time terminology intelligence, mapping, and regulatory compliance through agent-driven access, ensuring both operational consistency and interoperability.

- API access is secured through API keys linked to user accounts, ensuring that only authorized users can interact with the API endpoints.

## Expanded Available Code Systems

The platform has been expanded to include these Code Systems.

{:.table-model-big}
| Vocabulary | Name | Version |
|--------------|-----------------|--------------------|
| [ABMS](http://www.abms.org/member-boards/specialty-subspecialty-certificates) | Provider Specialty (American Board of Medical Specialties) | 2018-06-26 ABMS |
|[AMT](https://www.nehta.gov.au/implementation-resources/terminology-access)| Australian Medicines Terminology (NEHTA) | Clinical Terminology v20210630 |
|[APC](http://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/HospitalOutpatientPPS/Hospital-Outpatient-Regulations-and-Notices.html)| Ambulatory Payment Classification (CMS) | 2018-January-Addendum-A |
|[ATC](http://www.whocc.no/atc_ddd_index/)| WHO Anatomic Therapeutic Chemical Classification | ATC 2024-12-29 |
|[BDPM](http://base-donnees-publique.medicaments.gouv.fr/telechargement.php)| Public Database of Medications (Social-Sante) | BDPM 20191006 |
|[CDM](https://github.com/OHDSI/CommonDataModel)| OMOP Common DataModel | CDM v6.0.0 |
|[CMS Place of Service](http://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/PhysicianFeeSched/downloads//Website_POS_database.pdf)| Place of Service Codes for Professional Claims (CMS) | 2009-01-11 |
|[CPT4](http://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html)| Current Procedural Terminology version 4 (AMA) | 2025 Release |
|[CVX](https://www2a.cdc.gov/vaccines/iis/iisstandards/vaccines.asp?rpt=cvx)| CDC Vaccine Administered CVX (NCIRD) | CVX 20250703 |
|Cancer Modifier| Diagnostic Modifiers of Cancer (OMOP) | Cancer Modifier 20220909 |
|Concept Class| OMOP Concept Class |  |
|Condition Status| OMOP Condition Status |  |
|Condition Type| OMOP Condition Occurrence Type |  |
|Cost| OMOP Cost |  |
|Cost Type| OMOP Cost Type |  |
|[Currency](http://www.iso.org/iso/home/standards/currency_codes.htm)| International Currency Symbol (ISO 4217) | 2008 |
|[DRG](http://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/AcuteInpatientPPS/Acute-Inpatient-Files-for-Download.html)| Diagnosis-related group (CMS) | 2011-18-02 |
|Death Type| OMOP Death Type |  |
|Device Type| OMOP Device Type |  |
|Domain| OMOP Domain |  |
|Drug Type| OMOP Drug Exposure Type |  |
|[EORTC QLQ](https://itemlibrary.eortc.org/)| EORTC Quality of Life questionnaires | EORTC QLQ defined by Core version 2023_11 |
|[EphMRA ATC](http://www.ephmra.org/Anatomical-Classification)| Anatomical Classification of Pharmaceutical Products (EphMRA) | EphMRA ATC 2016 |
|Episode| OMOP Episode | Episode 20201014 |
|Episode Type| OMOP Episode Type |  |
|Ethnicity| OMOP Ethnicity | Ethnicity 20250807 |
|[GGR](http://www.bcfi.be/nl/download)| Commented Drug Directory (BCFI) | GGR 20210901 |
|Gender| OMOP Gender |  |
|[HCPCS](http://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html)| Healthcare Common Procedure Coding System (CMS) | 20250701 Alpha Numeric HCPCS File |
|[HES Specialty](http://www.datadictionary.nhs.uk/data_dictionary/attributes/m/main_specialty_code_de.asp?shownav=0)| Hospital Episode Statistics Specialty (NHS) | 2018-06-26 HES Specialty |
|HGNC| HUGO Gene Nomenclature Committee |  |
|HPO| Human Phenotype Ontology |  |
|[HemOnc](https://hemonc.org)| HemOnc | HemOnc 2024-12-19 |
|[ICD10](http://www.who.int/classifications/icd/icdonlineversions/en/)| International Classification of Diseases, Tenth Revision (WHO) | 2021 Release |
|[ICD10CM](https://www.cdc.gov/nchs/icd/icd-10-cm.htm)| International Classification of Diseases, Tenth Revision, Clinical Modification (NCHS) | ICD10CM FY2026 code descriptions |
|[ICD10PCS](http://www.cms.gov/Medicare/Coding/ICD10/index.html)| ICD-10 Procedure Coding System (CMS) | ICD10PCS 2026 |
|[ICD9CM](http://www.cms.gov/Medicare/Coding/ICD9ProviderDiagnosticCodes/codes.html)| International Classification of Diseases, Ninth Revision, Clinical Modification, Volume 1 and 2 (NCHS) | ICD9CM v32 master descriptions |
|[ICD9Proc](http://www.cms.gov/Medicare/Coding/ICD9ProviderDiagnosticCodes/codes.html)| International Classification of Diseases, Ninth Revision, Clinical Modification, Volume 3 (NCHS) | ICD9CM v32 master descriptions |
|[ICDO3](https://seer.cancer.gov/icd-o-3/)| International Classification of Diseases for Oncology, Third Edition (WHO) | ICDO3 SEER Site/Histology Released 06/2020 |
|JMDC| Japan Medical Data Center Drug Code (JMDC) | JMDC 2020-04-30 |
|[KDC](https://www.hira.or.kr/eng/)| Korean Drug Code (HIRA) | KDC 2020-07-31 |
|Korean Revenue Code| Korean Revenue Code (KNHIS) |  |
|[LOINC](http://loinc.org/downloads/loinc)| Logical Observation Identifiers Names and Codes (Regenstrief Institute) | LOINC 2.80 |
|Language| OMOP Language | Language 20221030 |
|[MDC](http://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/AcuteInpatientPPS/Acute-Inpatient-Files-for-Download.html)| Major Diagnostic Categories (CMS) | 2013-01-06 |
|MMI| Modernizing Medicine (MMI) |  |
|[MeSH](http://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html)| Medical Subject Headings (NLM) | 2025 Release |
|MeSH Veterinary| MeSH Veterinary |  |
|Meas Type| OMOP Measurement Type |  |
|MedDRA_LLT| Medical Dictionary for Regulatory Activities |  |
|MedDRA_PT| Medical Dictionary for Regulatory Activities |  |
|[Medicare Specialty](http://www.cms.gov/Medicare/Provider-Enrollment-and-Certification/MedicareProviderSupEnroll/Taxonomy.html)| Medicare provider/supplier specialty codes (CMS) | 2018-06-26 Specialty |
|[Metadata]| OMOP Metadata |  |
|[Multum](http://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html)| Cerner Multum (Cerner) | 2013-07-10 |
|[NAACCR](http://datadictionary.naaccr.org/?c=10)| Data Standards & Data Dictionary Volume II (NAACCR) | NAACCR v18 |
|[NCIt](http://evs.nci.nih.gov/ftp1/NCI_Thesaurus)| NCI Thesaurus (National Cancer Institute) | NCIt 20220509 |
|[NDC](http://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html)| National Drug Code (FDA and manufacturers) | NDC 20250817 |
|[NFC](http://www.ephmra.org/New-Form-Codes-Classification)| New Form Code (EphMRA) | NFC 20160704 |
|[NUCC](http://www.nucc.org/index.php?option=com_content&view=article&id=107&Itemid=132)| National Uniform Claim Committee Health Care Provider Taxonomy Code Set (NUCC) | NUCC 25.0 |
|[Nebraska Lexicon](https://www.unmc.edu/pathology-research/bioinformatics/campbell/tdc.html)| Nebraska Lexicon (UNMC) | Nebraska Lexicon 20190816 |
|Note Type| OMOP Note Type |  |
|OMOP Extension| OMOP Extension (OHDSI) | OMOP Extension 20240716 |
|OMOP Genomic| OMOP Genomic vocabulary of known variants involved in disease | OMOP Genomic 20240216 |
|[OMOP Invest Drug](https://gsrs.ncats.nih.gov/, https://gsrs.ncats.nih.gov/#/release)| OMOP Investigational Drugs | OMOP Invest Drug version 2024-06-03 |
|[OPCS4](http://systems.hscic.gov.uk/data/clinicalcoding/codingstandards/opcs4)| OPCS Classification of Interventions and Procedures version 4 (NHS) | 2021 Release |
|[OSM](https://www.openstreetmap.org/copyright/en)| OpenStreetMap (OSMF) | OSM Release 2019-02-21 |
|Obs Period Type| OMOP Observation Period Type |  |
|Observation Type| OMOP Observation Type |  |
|PCORNet| National Patient-Centered Clinical Research Network (PCORI) |  |
|[PPI](http://terminology.pmi-ops.org/CodeSystem/ppi)| AllOfUs_PPI (Columbia) | Codebook Version 0.4.43 + COVID + MHWB + SDOH + PFH + BHP + EHH |
|Plan| OMOP Health Plan |  |
|Plan Stop Reason| OMOP Plan Stop Reason |  |
|Procedure Type| OMOP Procedure Occurrence Type |  |
|Provider| OMOP Provider |  |
|[Race](http://www.cdc.gov/nchs/data/dvs/Race_Ethnicity_CodeSet.pdf)| Race and Ethnicity Code Set (USBC) | Version 1.0 |
|Relationship| OMOP Relationship |  |
|[Revenue Code](http://www.mpca.net/?page=ERC_finance)| UB04/CMS1450 Revenue Codes (CMS) | 2010 Release |
|[RxNorm](http://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html)| RxNorm (NLM) | RxNorm 20250602 |
|RxNorm Extension| OMOP RxNorm Extension | RxNorm Extension 2025-08-12 |
|[SMQ](http://www.meddramsso.com/secure/smq/SMQ_Spreadsheet_14_0_English_update.xlsx)| Standardised MedDRA Queries (MSSO) | Version 14.0 |
|[SNOMED](http://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html)| Systematic Nomenclature of Medicine - Clinical Terms (IHTSDO) | 2025-02-01 SNOMED CT International Edition; 2025-03-01 SNOMED CT US Edition; 2025-04-09 SNOMED CT UK Edition |
|[SNOMED Veterinary](https://vtsl.vetmed.vt.edu/extension/)| SNOMED Veterinary Extension (VTSL) | SNOMED Veterinary 20250101 |
|[SOPT](https://www.nahdo.org/sopt)| Source of Payment Typology (PHDSC) | SOPT Version 9.2 |
|[SPL](http://www.fda.gov/Drugs/InformationOnDrugs/ucm142438.htm)| Structured Product Labeling (FDA) | NDC 20250817 |
|Specimen Type| OMOP Specimen Type |  |
|Sponsor| OMOP Sponsor |  |
|Supplier| OMOP Supplier |  |
|Type Concept| OMOP Type Concept | Type Concept 20221030 |
|[UB04 Point of Origin](https://www.resdac.org/cms-data/variables/Claim-Source-Inpatient-Admission-Code)| UB04 Claim Source Inpatient Admission Code (CMS) |  |
|[UB04 Pri Typ of Adm](https://www.resdac.org/cms-data/variables/Claim-Inpatient-Admission-Type-Code)| UB04 Claim Inpatient Admission Type Code (CMS) |  |
|[UB04 Pt dis status](https://www.resdac.org/cms-data/variables/patient-discharge-status-code)| UB04 Patient Discharge Status Code (CMS) |  |
|[UB04 Typ bill](https://ushik.ahrq.gov/ViewItemDetails?&system=apcd&itemKey=196987000)| UB04 Type of Bill - Institutional (USHIK) |  |
|[UCUM](http://aurora.regenstrief.org/~ucum/ucum.html#section-Alphabetic-Index)| Unified Code for Units of Measure (Regenstrief Institute) | Version 1.8.2 |
|UMLS| Unified Medical Language System |  |
|[US Census](https://www.census.gov/geo/maps-data/data/tiger-cart-boundary.html)| Census regions of the United States (USCB) | US Census 2017 Release |
|[VANDF](http://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html)| Veterans Health Administration National Drug File (VA)) | RxNorm 20240603 |
|Visit| OMOP Visit | Visit 20211216 |
|Visit Type| OMOP Visit Type |  |
|Vocabulary| OMOP Vocabulary |  |
|[dm+d](https://isd.hscic.gov.uk/trud3/user/authenticated/group/0/pack/1/subpack/24/releases)| Dictionary of Medicines and Devices (NHS) | DMD 2025-06-02 |

## Licenses Page

A dedicated Licenses page has been introduced to streamline license management and feature activation:

- **License Overview**: View detailed information about your John Snow Labs (JSL) license, including expiration dates
- **Document Search Activation**: Enable or disable the premium Document Search feature directly from the interface with a simple toggle
- **License Status**: Display of license validity and feature availability
- **Self-Service Management**: Reduce dependency on administrative support by allowing users to manage premium features independently

This enhancement provides greater transparency and control over your Terminology Server licensing and premium feature access.

## Improvements

* UI Facelift: The Terminology Server UI has been modernized with an improved layout, refreshed color palette, and enhanced navigation. The update brings a more intuitive, responsive design, better accessibility, and a cleaner interface for users.
  ![Term-To-Code-Search](/assets/images/term_server/term-to-code-search.png)
* Added endpoint to generate embeddings for medical terms.
* Added a TopK slider input in the Filters panel.
* Enhanced query performance for faster search results.


![License-Management](/assets/images/term_server/license_management.png)
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


<ul class="pagination pagination_big">
  <li class="active"><a href="release_note_v4">v4</a></li>
  <li><a href="release_note_v3">v3</a></li>
  <li><a href="release_note_v2">v2</a></li>
  <li><a href="release_note_v1">v1</a></li>
</ul>
