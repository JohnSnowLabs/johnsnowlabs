# Combining Prompt Engineering, Programmatic Labelling, and Model Tuning in the No-Code NLP Lab
Combining Prompt Engineering, Programmatic Labelling, and Model Tuning in the No-Code NLP Lab

<https://www.johnsnowlabs.com/watch-combining-prompt-engineering-programmatic-labelling-and-model-tuning-in-the-no-code-nlp-lab/>

<https://youtu.be/iwx99AeWu7A>

<img src="/media/image.jpg" title="Video titled: Combining Prompt Engineering, Programmatic Labelling, and Model Tuning in the No-Code NLP Lab" style="width:6.3125in;height:3.65625in" />

The speech is presented by **Datra Bitash**, the head of product at Johnson Labs, and focuses on demonstrating how to combine **prompt engineering, programmatic labeling, and model tuning** within the **no-code NLP lab**. The NLP lab was formerly known as the annotation lab.

Below is a detailed summary of the presentation content:

### **I. Introduction and NLP Lab Overview**

The NLP lab is a **production-ready tool for annotating unstructured documents in any domain**. It is designed to be an easy-to-use tool for **domain experts without data science knowledge**.

**Key Enterprise Features:**

- It is highly scalable and imposes **no restrictions** on the number of users, projects, documents, pages, trained models, or the number of ganotations run.

- It includes enterprise-level features such as security and privacy, team and project management, various analytics, support for different workflows, and a **complete audit trail** of all user actions.

**Basic Functionality and Collaboration:**

- The most basic feature is **text annotation**, where users load a document, select a chunk of text, and assign it to a specific entity within a predefined taxonomy.

- Teams can collaborate on projects by importing documents (which become tasks) and splitting the load among annotators.

- The NLP lab maintains a status for each task (in progress, submitted, reviewed). Tasks can be assigned to different annotators and reviewers, and tags can be applied for further exploitation, such as model training or selective exporting. Users can also comment on tasks for enhanced collaboration.

### **II. Resources for Pre-annotation**

Pre-annotation is essential so that annotation teams do not have to start from scratch. The NLP lab offers a hub of resources for this purpose:

1.  **NLP Models Hub:** This feature provides **direct integration with the public NLP models hub**, giving access to **over 10,000 pre-trained models** in domains like healthcare, finance, and legal. Users can search and filter models based on task (NER, text classification, relation extraction, assertion status detection) or language. Models can be easily downloaded to the user's local private models hub.

2.  **Private Resources:** The lab maintains four dedicated pages for private resources: **models** (downloaded, trained in-lab, or custom-trained and imported), **embeddings**, **rules**, and **prompts**.

3.  **Playground:** This feature was recently added to allow users to **quickly test pre-annotation resources** (rules, prompts, and models) on custom text without needing to set up a full project.

### **III. Programmatic Labeling (Rules)**

Programmatic labeling uses rules to identify entities with a **relatively stable form**, such as vital signs.

- Rules are created by defining a name, scope, and matching criteria.

- The NLP lab supports both **regular expression based rules** and **dictionary based rules** (uploading a set of keywords or a CSV file).

- Rules can define the context where the entities need to be identified, often using a bunch of keywords. This prevents non-target text, like all numbers, from being identified.

### **IV. Prompt Engineering**

The goal of prompt engineering is to define and craft **natural language questions** that are fed into a question-answering model along with the input text. This guides the model to perform tasks, such as identifying entities and relations, for which it was not explicitly trained.

- **Entity Prompts:** When creating an entity prompt, users define a question that the QA model will use. A simple example was shown for identifying dates. The speaker demonstrated that iteratively adding questions to the prompt can modify the results, potentially leading to identifying missed entities but also adding false positives.

- **Relation Prompts:** For relation prompts, users select the type as "relation" and choose the domain (healthcare, finance, or legal). The questions must be defined with respect to two existing entities (selected from the taxonomy). Example questions include templates like "test has result" or "generated some results". The resulting relation annotations are dependent on the correct identification of the source entities by the used models.

### **V. Combining Resources in an Annotation Project**

The presentation demonstrated how to mix rules, prompts, and models into a single pre-annotation pipeline.

1.  **Project Setup:** A project is created (e.g., for clinical document annotation) and configured with a template like Named Entity Recognition.

2.  **Resource Selection:** Users select the desired rules (e.g., for vital signs), prompts (e.g., for dates and clinical trial ID), and models.

3.  **Taxonomy Linking:** These resources and their corresponding entities are added to the project's taxonomy and linked behind the scenes with the rules, prompts, and models used for pre-anotation. Users can selectively include only specific entities predicted by a certain model.

4.  **Pre-annotation Run:** Documents are imported, and the pre-anotation button runs the configured pipeline.

5.  **Result Exploration and Correction:** The generated annotations are displayed, along with a **confidence score** assigned to each entity. Annotators can filter pre-anotations based on low confidence scores to focus their efforts on high-confidence suggestions, thereby **reducing the correction load**. Annotators correct the results and submit the task, creating the final version of the annotation.

### **VI. Training a New Model**

To further automate annotation, a new model can be trained using the corrected annotations.

- **Training Data:** The speaker used a previously annotated project with 50 completed tasks (status: submitted).

- **Training Process:** From the train screen, users select the model type (NE, classification, or assertion status). Default parameters are generally accurate, and users can choose the data split (e.g., random split) and opt to generate a **confusion matrix**.

- **Time and Analysis:** Training typically takes between 5 to 10 minutes for 50 tasks. The confusion matrix, while potentially complex for large taxonomies, helps identify confusion between entities, offering insight into possible taxonomy restructuring needed for better results.

- **Model Availability:** Once trained, the model appears on the models page, complete with **benchmarking information**. Low accuracy scores indicate that the training data does not contain enough examples for those specific entities, signaling where more documents should be added.

- The new model can be used for pre-anotation in future projects or downloaded for deployment in a production environment.

- **Iteration:** It is recommended to start training the first version of the model after **50 completions** and then iteratively improve accuracy by adding extra data.

### **VII. Availability**

The NLP lab is available on the **AWS and Azure marketplaces**. It can also be deployed on a user's **local infrastructure**, which is useful for air-gapped environments or those who prefer to use their own servers. Support is offered via Slack.