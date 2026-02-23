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

| Vocabulary | Name | Reference | Version |
|--------------|-----------------|---------------------|--------------------|
| ABMS | Provider Specialty (American Board of Medical Specialties) | http://www.abms.org/member-boards/specialty-subspecialty-certificates | 2018-06-26 ABMS |
| AMT | Australian Medicines Terminology (NEHTA) | https://www.nehta.gov.au/implementation-resources/terminology-access | Clinical Terminology v20210630 |
| APC | Ambulatory Payment Classification (CMS) | http://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/HospitalOutpatientPPS/Hospital-Outpatient-Regulations-and-Notices.html | 2018-January-Addendum-A |
| ATC | WHO Anatomic Therapeutic Chemical Classification | http://www.whocc.no/atc_ddd_index/ | ATC 2024-12-29 |
| BDPM | Public Database of Medications (Social-Sante) | http://base-donnees-publique.medicaments.gouv.fr/telechargement.php | BDPM 20191006 |
| CDM | OMOP Common DataModel | https://github.com/OHDSI/CommonDataModel | CDM v6.0.0 |
| CMS Place of Service | Place of Service Codes for Professional Claims (CMS) | http://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/PhysicianFeeSched/downloads//Website_POS_database.pdf | 2009-01-11 |
| CPT4 | Current Procedural Terminology version 4 (AMA) | http://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html | 2025 Release |
| CVX | CDC Vaccine Administered CVX (NCIRD) | https://www2a.cdc.gov/vaccines/iis/iisstandards/vaccines.asp?rpt=cvx | CVX 20250703 |
| Cancer Modifier | Diagnostic Modifiers of Cancer (OMOP) | OMOP generated | Cancer Modifier 20220909 |
| Concept Class | OMOP Concept Class | OMOP generated |  |
| Condition Status | OMOP Condition Status | OMOP generated |  |
| Condition Type | OMOP Condition Occurrence Type | OMOP generated |  |
| Cost | OMOP Cost | OMOP generated |  |
| Cost Type | OMOP Cost Type | OMOP generated |  |
| Currency | International Currency Symbol (ISO 4217) | http://www.iso.org/iso/home/standards/currency_codes.htm | 2008 |
| DRG | Diagnosis-related group (CMS) | http://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/AcuteInpatientPPS/Acute-Inpatient-Files-for-Download.html | 2011-18-02 |
| Death Type | OMOP Death Type | OMOP generated |  |
| Device Type | OMOP Device Type | OMOP generated |  |
| Domain | OMOP Domain | OMOP generated |  |
| Drug Type | OMOP Drug Exposure Type | OMOP generated |  |
| EORTC QLQ | EORTC Quality of Life questionnaires | https://itemlibrary.eortc.org/ | EORTC QLQ defined by Core version 2023_11 |
| EphMRA ATC | Anatomical Classification of Pharmaceutical Products (EphMRA) | http://www.ephmra.org/Anatomical-Classification | EphMRA ATC 2016 |
| Episode | OMOP Episode | OMOP generated | Episode 20201014 |
| Episode Type | OMOP Episode Type | OMOP generated |  |
| Ethnicity | OMOP Ethnicity | OMOP generated | Ethnicity 20250807 |
| GGR | Commented Drug Directory (BCFI) | http://www.bcfi.be/nl/download | GGR 20210901 |
| Gender | OMOP Gender | OMOP generated |  |
| HCPCS | Healthcare Common Procedure Coding System (CMS) | http://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html | 20250701 Alpha Numeric HCPCS File |
| HES Specialty | Hospital Episode Statistics Specialty (NHS) | http://www.datadictionary.nhs.uk/data_dictionary/attributes/m/main_specialty_code_de.asp?shownav=0 | 2018-06-26 HES Specialty |
| HGNC | HUGO Gene Nomenclature Committee |  |  |
| HPO | Human Phenotype Ontology |  |  |
| HemOnc | HemOnc | https://hemonc.org | HemOnc 2024-12-19 |
| ICD10 | International Classification of Diseases, Tenth Revision (WHO) | http://www.who.int/classifications/icd/icdonlineversions/en/ | 2021 Release |
| ICD10CM | International Classification of Diseases, Tenth Revision, Clinical Modification (NCHS) | https://www.cdc.gov/nchs/icd/icd-10-cm.htm | ICD10CM FY2026 code descriptions |
| ICD10PCS | ICD-10 Procedure Coding System (CMS) | http://www.cms.gov/Medicare/Coding/ICD10/index.html | ICD10PCS 2026 |
| ICD9CM | International Classification of Diseases, Ninth Revision, Clinical Modification, Volume 1 and 2 (NCHS) | http://www.cms.gov/Medicare/Coding/ICD9ProviderDiagnosticCodes/codes.html | ICD9CM v32 master descriptions |
| ICD9Proc | International Classification of Diseases, Ninth Revision, Clinical Modification, Volume 3 (NCHS) | http://www.cms.gov/Medicare/Coding/ICD9ProviderDiagnosticCodes/codes.html | ICD9CM v32 master descriptions |
| ICDO3 | International Classification of Diseases for Oncology, Third Edition (WHO) | https://seer.cancer.gov/icd-o-3/ | ICDO3 SEER Site/Histology Released 06/2020 |
| JMDC | Japan Medical Data Center Drug Code (JMDC) | OMOP generated | JMDC 2020-04-30 |
| KDC | Korean Drug Code (HIRA) | https://www.hira.or.kr/eng/ | KDC 2020-07-31 |
| Korean Revenue Code | Korean Revenue Code (KNHIS) | OMOP generated |  |
| LOINC | Logical Observation Identifiers Names and Codes (Regenstrief Institute) | http://loinc.org/downloads/loinc | LOINC 2.80 |
| Language | OMOP Language | OMOP generated | Language 20221030 |
| MDC | Major Diagnostic Categories (CMS) | http://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/AcuteInpatientPPS/Acute-Inpatient-Files-for-Download.html | 2013-01-06 |
| MMI | Modernizing Medicine (MMI) | MMI proprietary |  |
| MeSH | Medical Subject Headings (NLM) | http://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html | 2025 Release |
| MeSH Veterinary | MeSH Veterinary |  |  |
| Meas Type | OMOP Measurement Type | OMOP generated |  |
| MedDRA_LLT | Medical Dictionary for Regulatory Activities |  |  |
| MedDRA_PT | Medical Dictionary for Regulatory Activities |  |  |
| Medicare Specialty | Medicare provider/supplier specialty codes (CMS) | http://www.cms.gov/Medicare/Provider-Enrollment-and-Certification/MedicareProviderSupEnroll/Taxonomy.html | 2018-06-26 Specialty |
| Metadata | OMOP Metadata | OMOP generated |  |
| Multum | Cerner Multum (Cerner) | http://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html | 2013-07-10 |
| NAACCR | Data Standards & Data Dictionary Volume II (NAACCR) | http://datadictionary.naaccr.org/?c=10 | NAACCR v18 |
| NCIt | NCI Thesaurus (National Cancer Institute) | http://evs.nci.nih.gov/ftp1/NCI_Thesaurus | NCIt 20220509 |
| NDC | National Drug Code (FDA and manufacturers) | http://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html, http://www.fda.gov/downloads/Drugs/DevelopmentApprovalProcess/UCM070838.zip | NDC 20250817 |
| NFC | New Form Code (EphMRA) | http://www.ephmra.org/New-Form-Codes-Classification | NFC 20160704 |
| NUCC | National Uniform Claim Committee Health Care Provider Taxonomy Code Set (NUCC) | http://www.nucc.org/index.php?option=com_content&view=article&id=107&Itemid=132 | NUCC 25.0 |
| Nebraska Lexicon | Nebraska Lexicon (UNMC) | https://www.unmc.edu/pathology-research/bioinformatics/campbell/tdc.html | Nebraska Lexicon 20190816 |
| Note Type | OMOP Note Type | OMOP generated |  |
| OMOP Extension | OMOP Extension (OHDSI) | OMOP generated | OMOP Extension 20240716 |
| OMOP Genomic | OMOP Genomic vocabulary of known variants involved in disease | OMOP generated | OMOP Genomic 20240216 |
| OMOP Invest Drug | OMOP Investigational Drugs | https://gsrs.ncats.nih.gov/, https://gsrs.ncats.nih.gov/#/release | OMOP Invest Drug version 2024-06-03 |
| OPCS4 | OPCS Classification of Interventions and Procedures version 4 (NHS) | http://systems.hscic.gov.uk/data/clinicalcoding/codingstandards/opcs4 | 2021 Release |
| OSM | OpenStreetMap (OSMF) | https://www.openstreetmap.org/copyright/en, https://wambachers-osm.website/boundaries/ | OSM Release 2019-02-21 |
| Obs Period Type | OMOP Observation Period Type | OMOP generated |  |
| Observation Type | OMOP Observation Type | OMOP generated |  |
| PCORNet | National Patient-Centered Clinical Research Network (PCORI) | OMOP generated |  |
| PPI | AllOfUs_PPI (Columbia) | http://terminology.pmi-ops.org/CodeSystem/ppi | Codebook Version 0.4.43 + COVID + MHWB + SDOH + PFH + BHP + EHH |
| Plan | OMOP Health Plan | OMOP generated |  |
| Plan Stop Reason | OMOP Plan Stop Reason | OMOP generated |  |
| Procedure Type | OMOP Procedure Occurrence Type | OMOP generated |  |
| Provider | OMOP Provider | OMOP generated |  |
| Race | Race and Ethnicity Code Set (USBC) | http://www.cdc.gov/nchs/data/dvs/Race_Ethnicity_CodeSet.pdf | Version 1.0 |
| Relationship | OMOP Relationship | OMOP generated |  |
| Revenue Code | UB04/CMS1450 Revenue Codes (CMS) | http://www.mpca.net/?page=ERC_finance | 2010 Release |
| RxNorm | RxNorm (NLM) | http://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html | RxNorm 20250602 |
| RxNorm Extension | OMOP RxNorm Extension | OMOP generated | RxNorm Extension 2025-08-12 |
| SMQ | Standardised MedDRA Queries (MSSO) | http://www.meddramsso.com/secure/smq/SMQ_Spreadsheet_14_0_English_update.xlsx | Version 14.0 |
| SNOMED | Systematic Nomenclature of Medicine - Clinical Terms (IHTSDO) | http://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html | 2025-02-01 SNOMED CT International Edition; 2025-03-01 SNOMED CT US Edition; 2025-04-09 SNOMED CT UK Edition |
| SNOMED Veterinary | SNOMED Veterinary Extension (VTSL) | https://vtsl.vetmed.vt.edu/extension/ | SNOMED Veterinary 20250101 |
| SOPT | Source of Payment Typology (PHDSC) | https://www.nahdo.org/sopt | SOPT Version 9.2 |
| SPL | Structured Product Labeling (FDA) | http://www.fda.gov/Drugs/InformationOnDrugs/ucm142438.htm | NDC 20250817 |
| Specimen Type | OMOP Specimen Type | OMOP generated |  |
| Sponsor | OMOP Sponsor | OMOP generated |  |
| Supplier | OMOP Supplier | OMOP generated |  |
| Type Concept | OMOP Type Concept | OMOP generated | Type Concept 20221030 |
| UB04 Point of Origin | UB04 Claim Source Inpatient Admission Code (CMS) | https://www.resdac.org/cms-data/variables/Claim-Source-Inpatient-Admission-Code |  |
| UB04 Pri Typ of Adm | UB04 Claim Inpatient Admission Type Code (CMS) | https://www.resdac.org/cms-data/variables/Claim-Inpatient-Admission-Type-Code |  |
| UB04 Pt dis status | UB04 Patient Discharge Status Code (CMS) | https://www.resdac.org/cms-data/variables/patient-discharge-status-code |  |
| UB04 Typ bill | UB04 Type of Bill - Institutional (USHIK) | https://ushik.ahrq.gov/ViewItemDetails?&system=apcd&itemKey=196987000 |  |
| UCUM | Unified Code for Units of Measure (Regenstrief Institute) | http://aurora.regenstrief.org/~ucum/ucum.html#section-Alphabetic-Index | Version 1.8.2 |
| UMLS | Unified Medical Language System |  |  |
| US Census | Census regions of the United States (USCB) | https://www.census.gov/geo/maps-data/data/tiger-cart-boundary.html | US Census 2017 Release |
| VANDF | Veterans Health Administration National Drug File (VA)) | http://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html | RxNorm 20240603 |
| Visit | OMOP Visit | OMOP generated | Visit 20211216 |
| Visit Type | OMOP Visit Type | OMOP generated |  |
| Vocabulary | OMOP Vocabulary | OMOP generated |  |
| dm+d | Dictionary of Medicines and Devices (NHS) | https://isd.hscic.gov.uk/trud3/user/authenticated/group/0/pack/1/subpack/24/releases | DMD 2025-06-02 |

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
