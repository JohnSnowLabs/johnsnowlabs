---
layout: docs
comment: no
header: true
seotitle: NLP Lab | John Snow Labs
title: Entity Resolution 
permalink: /docs/en/alab/resolvers
key: docs-training
modify_date: "2024-03-24"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
    nav: annotation-lab
---

### Lookup code/terms in Labeling page
NLP Lab version 5.9.0 introduces support for Entity Resolution, allowing users to enhance their annotations by adding lookup datasets. By allowing users to enrich labeled text with additional information, NLP Lab provides the way for improving the context and accuracy of annotations. Lookup functionality is currently supported exclusively by text based NER projects.

### Configuring Lookup
Configuring lookup datasets is straightforward: use the well-known Customize Labels page during project configuration and follow the steps below:
1. Click on the specific label for which you want to add lookup data.
2. Select the desired lookup dataset from the dropdown list.
3. Navigate to the task page and add lookup information to labeled texts.

![LookUpConfiguration](/assets/images/annotation_lab/5.9.0/1.gif)

### Identifying Entities with Lookup Data:
Once setup is done, it is easy to identify entities eligible for lookup by a small ⌄ icon displayed next to them. This icon signifies that lookup data can be added to those entities, providing users with clear guidance on annotation possibilities.

![ViewingIfLookupIsAvailable](/assets/images/annotation_lab/5.9.0/2.png)

### Adding/Viewing and Updating Lookup Data:
**Adding Lookup Data in Labeling Page:** Users can select the available lookup data from the list available for a particular label.

![AddLookup](/assets/images/annotation_lab/5.9.0/3.gif)

**Viewing Lookup Dataset:** Users can view the lookup data or metadata by clicking the gear icon in the labeling page and enabling the "Show Meta in Regions" setting.

![ShowhideMeta](/assets/images/annotation_lab/5.9.0/4.gif)

**Updating Lookup Dataset:** If users wish to change or edit the lookup data, they can simply right-click on the particular entity and choose the new lookup data.

![UpdateLookup](/assets/images/annotation_lab/5.9.0/5.gif)

This new feature enhances the annotation capabilities of NLP Lab, allowing users to enrich their annotations with relevant contextual information from lookup datasets. We're excited to see how this feature empowers users to create more accurate and comprehensive annotations in their projects.

## Pre-annotate metadata using Resolvers 

- NLP Lab 5.9 introduces a pivotal enhancement that expands pre-annotation capabilities with the use of Healthcare resolvers. These resolvers are now conveniently accessible and discoverable on the NLP Models Hub page. Simply apply the "Entity Resolution" filter to view the comprehensive list.

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
