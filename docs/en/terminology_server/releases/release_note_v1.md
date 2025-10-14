---
layout: docs
header: true
seotitle: Terminology Server | John Snow Labs
title: Terminology Server 
permalink: /docs/en/terminology_server/release_notes/release_notes_v1
key: docs-term-server
modify_date: "2025-04-01"
show_nav: true
sidebar:
    nav: term-server

---

## Terminology Server v1 Release Notes


<p style="text-align:center;">Release date: {{ page.modify_date | date: '%m-%d-%Y' }}</p>


**V1 Key Features:**
* Term Search - associated synonyms and employing both string matching and embedding matches for similarity searches.
* Code Search - Search for specific Code and filter by specific available Code System
* Code Seach with Code mapping results - Search for specific Code and show similar code results in other vocabularies 
* Spell checker - Account for misspellings, allowing the user to retain original string or apply correction
* Filter search results by:
    *  Domain: Specifies the general topic area of a concept (e.g., Condition/Device, Condition/Meas, Drug, Gender). The available options for this filter are pre-populated in the dropdown list.
    *  OMOP Standards Concepts Only: Limits the search results to concepts that are flagged as “Standard” in the OMOP CDM.
    *  Only Valid Concepts: Filters out concepts that have been invalidated due to deletion or being superseded.
    *  Confidence Score: Allows refining results based on their confidence score.
    *  Value Set
*  Value Set Management:
    * Craft custom Value Sets and apply them as filters to refine search outcomes based on data from a specific version of the chosen Value Set.
    * Generate new versions of an existing Value Set through the upload feature.
    * Access and review the data of any selected Value Set within the application.
*  API service: 

Allows seamless integration with your applications, enabling you to leverage our platform’s capabilities. By obtaining an API key, developers can interact with various endpoints to retrieve and manipulate data, ensuring smooth connectivity with external systems. Detailed documentation is available to guide you through authentication, rate limits, and usage examples, making the integration process straightforward.
