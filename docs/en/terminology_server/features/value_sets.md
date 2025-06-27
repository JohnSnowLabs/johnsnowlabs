---
layout: docs
header: true
seotitle: Terminology Server | John Snow Labs
title: Terminology Server 
permalink: /docs/en/terminology_server/features/value_sets
key: docs-term-server
modify_date: "2025-04-01"
show_nav: true
sidebar:
    nav: term-server
---

## Custom Value Sets

A custom Value Set in the context of medical terminology is a user-defined collection of medical codes and terms selected from one or more standard coding systems (such as SNOMED CT, ICD-10, LOINC, RxNorm, etc.), created to meet a specific need, use case, or organizational requirement.

**Key Characteristics of Custom Value Sets**:
* Tailored: Designed to include only the codes relevant to a specific clinical, research, or operational goal
* Flexible: May draw from multiple coding systems and be modified over time.
* Not standardized: Unlike predefined or published Value Sets from regulatory bodies, custom Value Sets are not universally agreed upon and are typically used internally or within a specific application or workflow.

**Common Use Cases:**
* A hospital may define a custom Value Set for "medications used in cardiology".
* A research team may create one for "cancer-related diagnoses" using a mix of SNOMED and ICD-10 codes.
* A public health agency may define a custom Value Set for "reportable diseases" specific to its jurisdiction.

In Terminology Server Tools, custom Value Sets can often be:
* Created manually or programmatically
* Versioned and updated
* Used in conjunction with concept search, validation, and filtering features

John Snow Labs' Terminology Server supports the use of custom Value Sets, offering the following capabilities:
* Upload custom Value Sets created externally in Excel or CSV format using the built-in Upload feature.
* View, create new versions, delete
* Filter search results based on the codes included in a selected Value Set.

Uploading a Custom Value Set into Terminology Server is straight forward: 
1. In the left navigation bar, click on **Value Sets** node
2. Drag or choose "Browse Files" then click Upload your file representinng the custom Value set

3. 

