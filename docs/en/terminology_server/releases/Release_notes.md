---
layout: docs
header: true
seotitle: Terminology Server | John Snow Labs
title: Terminology Server 
permalink: /docs/en/terminology_server/release_notes
key: docs-term-server
modify_date: "2025-04-01"
show_nav: true
sidebar:
    nav: term-server
---
## June 02, 2025

**V2 Key Features:**

* Hierarchy Display - View the hierarchy of a concept, including its ancestors and descendants, to understand its context within the broader terminology structure.

  The following image explains how the hierarchy information is displayed when a code is clicked inside the results table:

  ![Screenshot of hierarchy](/assets/images/term_server/CodeHierarchy.png)
  
* Context Based Search - Perform searches that consider the context of the query, allowing for more relevant results based on the specific domain or use case.

**Improvements:** 
* Improved initial setup time for the On Premise Deployment of Terminology Server, reducing the time it takes to get started with the application.
* Merged backend services into a single service, simplifying the architecture and improving maintainability.


## May 03, 2025

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
