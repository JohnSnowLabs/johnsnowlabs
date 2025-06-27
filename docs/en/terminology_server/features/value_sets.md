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

📤 **Uploading a Custom Value Set in Terminology Server**

Uploading a custom Value Set is simple and intuitive:
1. In the **left navigation panel**, click on the **Value Sets** node.
2. Use the "**Browse Files**" button or drag your Excel/CSV file into the upload area, then click **Upload** to import your custom Value Set.

![Terminology Service by John Snow Labs](/assets/images/term_server/Upload_VS_firsttime.png)

3. Once uploaded, the new Value Set will appear in the **left panel** under the Value Sets section..

![Terminology Service by John Snow Labs](/assets/images/term_server/Upload_VS_consecutive.png)

4. To **create a new Value Set** or **add a new version** to an existing one, click the **"Upload"** link on the right-hand side.

![Terminology Service by John Snow Labs](/assets/images/term_server/Upload_VS_consecutive_newVersion.png)

5. Each **new version** will appear as a child node under the corresponding Value Set.   

![Terminology Service by John Snow Labs](/assets/images/term_server/VS_Versions.png)

6. To **view**, **download**, or **delete** a version, use the icons next to it.
🔴 Note: Deleting the last remaining version will remove the entire Value Set from the system.

**Filter search results using Value Sets**
