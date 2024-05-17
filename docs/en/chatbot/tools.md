---
layout: docs
header: true
seotitle: Medical Chatbot | John Snow Labs
title: Tools
permalink: /docs/en/chatbot/tools
key: docs-healthcare-gpt
modify_date: "2024-05-17"
show_nav: true
sidebar:
    nav: healthcare-gpt
---

<div class="h3-box" markdown="1">

The Medical Chatbot is equipped with three dynamic tools, each tailored to meet different information needs and research requirements. These tools are `MedResearch`, `Wikipedia`, and `John's Memory`, collectively providing a comprehensive solution for a wide range of queries.

## MedResearch: Your Gateway to Academic Medical Research

`MedResearch` stands as the cornerstone of the Medical Chatbot, offering exhaustive coverage of academic papers and research results. This tool is meticulously designed to query multiple prestigious databases:
- PubMed
- BioRxiv
- MedRxiv

along with specialized custom knowledge bases such as:
- Drug Leaflets - a Knowledge Base that indexes Drug data published by [FDA](www.fda.gov)
- Cigna Insurance Plans - a Knowledge base that indexes insurance plans (large PDF documents) offered by Cigna  

Whether you're looking for the latest findings in a specific medical field, detailed drug information, or comprehensive research outcomes, MedResearch provides direct access to a vast repository of academic resources. This feature is especially valuable for medical professionals, researchers, and students seeking to base their work on the most current and authoritative sources.

For questions targeting a certain KB, you can turn available KBs on and off according to your preference. 

![Select the KB you want to target with your question](\assets\images\chatbot\KBSelection.png)


> **_NOTE:_**  To enforce the use of this tool add the following sentence at the end of your query: **Ask MedResearch.**

</div><div class="h3-box" markdown="1">

## NLP Tools 
The NLP Tools feature is a new addition to the Medical Chatbot, providing specialized capabilities for processing medical texts through Natural Language Processing (NLP). This feature allows users to access five distinct state-of-the-art accuracy tools, each designed for specific tasks related to medical data handling and analysis.

### Deidentification/Obfuscation of PHI

Automatically detects and masks or obfuscates personally identifiable information (PHI) from medical text to ensure privacy and compliance with data protection regulations.
   
   <iframe width="800" height="450" src="https://www.youtube.com/embed/odSyX3uKjwg?si=XZZO8aY3t82Iqslu&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### General Medical Entity Extraction
Identifies and extracts general medical entities from text, facilitating quick access to relevant medical terms and concepts.

   <iframe width="800" height="450" src="https://www.youtube.com/embed/FjAzlImC0zQ?si=N415bCn2AU2h6i6U&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Oncological Entity Extraction
Specialized for recognizing and extracting terms related to oncology, aiding in the analysis of cancer-related medical texts.

   <iframe width="800" height="450" src="https://www.youtube.com/embed/qTbH57SI6R0?si=HO8riHFw-cXYeIvK&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Posology Entity Extraction
Focuses on extracting dosage and medication instructions from medical documents, crucial for understanding treatment protocols.

   <iframe width="800" height="450" src="https://www.youtube.com/embed/5M5nLUdTb4I?si=7uCei72nxBSpvwMe&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


**Export results in csv format-** All results computed using the NLP tools can be exported in csv format. For each detected entity the export also contains confidence information.

**NLP Tools activation-** Users can enable or disable NLP tools based on their specific needs or preferences, allowing for a personalized experience and control over the processing features used.

**Accessing NLP Tools-** NLP tools can be invoked in two ways: via regular queries in natural language or by using the '@' operator for direct tool activation.

**User Benefits**
- **Enhanced Privacy and Compliance**: Safeguards sensitive information by efficiently deidentifying PHI from medical texts.
- **Focused Content Extraction**: Enables precise extraction of medical entities tailored to general, oncological, and posology contexts, enhancing the utility and accuracy of information retrieval.
- **User-Controlled Flexibility**: Offers the flexibility to tailor tool engagement to individual preferences and requirements.
- **Efficient Tool Access**: Simplifies the process of accessing specific NLP tools through intuitive user interface mechanisms.


## Wikipedia: Answering Short or Generic Questions

For users seeking quick answers to short or generic questions, the Medical Chatbot integrates seamlessly with Wikipedia. This feature is designed to fetch concise and reliable information from the vast expanse of Wikipedia's medical content. Whether it's a brief overview of a medical condition, historical context, or general health information, this tool ensures users can obtain quick answers efficiently. It's an excellent resource for those in need of rapid, accessible, and accurate information without the need for deep research.

> **_NOTE:_**  To enforce the use of this tool add the following sentence at the end of your query: **Ask Wikipedia.** or use the @ operator. 

</div><div class="h3-box" markdown="1">

## John's Memory: Specialized in Summarization and General Queries

John's Memory is a versatile feature within the Medical Chatbot, dedicated to summarization tasks and answering general questions. This tool is particularly useful when users need a succinct summary of extensive information or when they have broad questions that do not require deep, research-level detail. John's Memory employs advanced NLP (Natural Language Processing) techniques to comprehend, interpret, and condense information, making it an invaluable asset for users who need quick insights or overviews.

</div>

## @ Operator for Accessibility

Typing '@' in the query box triggers a contextual menu displaying all available tools, similar to tagging functionality in Microsoft Teams.

![Risk_Factors](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/e70788ea-77bc-48ca-9583-4e3586605241)


For instance, the @ operator also allows direct access to `MedResearch` tool for targeted questions to all active knowledgebases (see [MedResearch](/docs/en/chatbot/tools)). When using `@MedResearch` at the beginning of your question, the chatbot will directly engage the MedResearch tool without requiring user to select from multiple options, ensuring a streamlined interaction for focused research tasks.

Similarly, for Wikipedia and NLP Tools, each tool can be easily selected and utilized with the @ operator as follows:
 - `@search_wikipedia`: Query Wikipedia Pages
 - `@deidentification`: De-identification of Medical Text
 - `@obfuscation`: Obfuscation of Medical Text
 - `@ner_medical`: General Medical Entity Extraction
 - `@ner_medical_oncology `: Oncological Entity Extraction
 - `@ner_medical_posology `: Posology Entity Extraction

When interacting with the chatbot, the generated answer prominently displays the tool used for response generation right above the answer itself. This clarification ensures users know which tool was utilized.

Similarly, when selecting a specific tool using the '@' Selector in your query, the chosen tool is labeled at the top of the query, making it clear which tool was requested for the response generation.
Hence, users can better understand the specialties of these tools and experiment to obtain the best possible responses according to their needs.    

