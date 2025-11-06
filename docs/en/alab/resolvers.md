---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Entity Resolution 
permalink: /docs/en/alab/resolvers
key: docs-training
modify_date: "2024-03-24"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">

### Lookup Code/Terms in the Labeling Page
Generative AI Lab supports **Entity Resolution (ER)** for text-based annotation projects, enabling users to enrich entity labels with external lookup datasets.  
This feature enhances annotation accuracy and context by linking labeled text to structured terminology, such as medical codes or standardized identifiers.

Lookup functionality is available for text-based Named Entity Recognition (NER) projects and allows annotators to connect entities directly to relevant metadata — for example, mapping a medical **procedure** mention to a **CPT code**, or linking a diagnosis to an **ICD-10** code.

</div><div class="h3-box" markdown="1">

### Configuring Lookup

Configuring lookup datasets is straightforward through the **Customize Labels** page during project setup:

1. Click the specific label you want to associate with a lookup dataset.  
2. Select the desired lookup dataset from the dropdown list.  
3. Proceed to the Task page to apply lookup information to labeled entities.

![LookUpConfiguration](/assets/images/annotation_lab/5.9.0/1.gif)

</div><div class="h3-box" markdown="1">

### Identifying Entities with Lookup Data:
Once setup is done, it is easy to identify entities eligible for lookup by a small ⌄ icon displayed next to them. This icon signifies that lookup data can be added to those entities, providing users with clear guidance on annotation possibilities.

![ViewingIfLookupIsAvailable](/assets/images/annotation_lab/5.9.0/2.png)

</div><div class="h3-box" markdown="1">

### Adding/Viewing and Updating Lookup Data:
**Adding Lookup Data in Labeling Page:** Users can select the available lookup data from the list available for a particular label.

![AddLookup](/assets/images/annotation_lab/5.9.0/3.gif)

**Viewing Lookup Dataset:** Users can view the lookup data or metadata by clicking the gear icon in the labeling page and enabling the "Show Meta in Regions" setting.

![ShowhideMeta](/assets/images/annotation_lab/5.9.0/4.gif)

**Updating Lookup Dataset:** If users wish to change or edit the lookup data, they can simply right-click on the particular entity and choose the new lookup data.

![UpdateLookup](/assets/images/annotation_lab/5.9.0/5.gif)

This new feature enhances the annotation capabilities of Generative AI Lab, allowing users to enrich their annotations with relevant contextual information from lookup datasets. We're excited to see how this feature empowers users to create more accurate and comprehensive annotations in their projects.

</div><div class="h3-box" markdown="1">

## Pre-Annotate Metadata Using Resolvers

Generative AI Lab supports the use of **Healthcare Resolvers** for pre-annotating metadata, extending the platform’s capabilities to entity resolution tasks. Resolvers map recognized entities to standardized terminologies or knowledge bases, helping enrich annotations with meaningful metadata such as concept codes, canonical forms, or entity definitions.

Resolvers are available directly in the **NLP Models Hub** — users can easily locate them by applying the **“Entity Resolution”** filter. Once selected, these models can be deployed for pre-annotation like other model types, automatically linking identified entities to their corresponding concepts.

This enhancement allows annotation teams to:
- **Enrich Annotations Automatically:** Add structured metadata such as concept IDs and synonyms to labeled entities.  
- **Leverage Domain Knowledge:** Use domain-specific resolvers (e.g., Healthcare, Finance, Legal) to ensure high-quality entity linking.  
- **Streamline Workflows:** Reduce manual post-processing by integrating entity resolution directly into pre-annotation pipelines.


![Resolution_prediction](/assets/images/annotation_lab/5.9.0/6.png)

- For any selected resolver to be used in the pre-annotation process it is required to incorporate the named entity recognition (NER) model as part of the configuration project during setup.

- To seamlessly integrate the resolver with the NER models, navigate to the "Reuse Resources" page within the project configuration. Subsequently, proceed to the "Customize Labels" section. Here, individually select each label and designate the appropriate resolver from the drop-down menu of Entity Resolution Models.

![Resolver_configuration](/assets/images/annotation_lab/5.9.0/7.gif)

- The role of these resolvers is to transform pre-annotated labels into both code and descriptive representations. To access this functionality, ensure that the "Show Meta in Regions" option is enabled within the task settings.
  
![Resolution_prediction](/assets/images/annotation_lab/5.9.0/8.gif)

- Meta-information associated with a label is stored in a key-value pair format, facilitating easy retrieval and interpretation.

![Resolution_prediction](/assets/images/annotation_lab/5.9.0/9.png)

- While it's possible to copy and modify completions, it's important to note that the resolved code and descriptions cannot be directly edited. In such cases, deletion of the existing content or addition of new key-value pairs is necessary. In instances where no prediction is available, manual annotation of tasks can be performed using lookup codes/terms, provided that a lookup table has been configured.
![Resolver_copy_and_renames](/assets/images/annotation_lab/5.9.0/10.gif)

</div><div class="h3-box" markdown="1">

## Combining Entity Resolvers with Rules and Zero-Shot Prompts

Entity Resolution models can be used not only with NER models but also alongside **Rules** and **Zero-Shot Prompts**, allowing flexible pre-annotation and enrichment workflows.

**How to Use:**
1. Add a Rule or Prompt resource from the **Reuse Resources** page.  
2. Edit the label in **Customize Labels** and assign an Entity Resolver model.  
3. Import and pre-annotate tasks to automatically resolve entities to their canonical forms or codes.

    
![genAI650](/assets/images/annotation_lab/6.5.0/13.gif)

</div>