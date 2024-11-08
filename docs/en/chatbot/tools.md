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

The Medical Chatbot is equipped with dynamic tools, each tailored to meet different information needs and research requirements. These tools are `MedResearch`, `Web Search`, `Medical Agents`, and `John's Memory`, collectively providing a comprehensive solution for a wide range of queries.

## MedResearch: Your Gateway to Academic Medical Research

`MedResearch` stands as the cornerstone of the Medical Chatbot, offering exhaustive coverage of academic papers and research results. This tool is meticulously designed to query multiple prestigious databases:
- PubMed
- BioRxiv
- MedRxiv

along with specialized custom knowledge bases such as:
- Drug Leaflets - a Knowledge Base that indexes Drug data published by [FDA](https://www.fda.gov/)
- Cigna Insurance Plans - a Knowledge base that indexes insurance plans (large PDF documents) offered by Cigna  

Whether you're looking for the latest findings in a specific medical field, detailed drug information, or comprehensive research outcomes, MedResearch provides direct access to a vast repository of academic resources. This feature is especially valuable for medical professionals, researchers, and students seeking to base their work on the most current and authoritative sources.

For questions targeting a certain KB, you can turn available KBs on and off according to your preference. 

![Select the KB you want to target with your question](\assets\images\chatbot\KBSelection.png)


> **_NOTE:_**  To enforce the use of this tool add the following sentence at the end of your query: **Ask MedResearch.**

</div><div class="h3-box" markdown="1">

## Medical Agents 
The Medical Agents are a new addition to the Medical Chatbot, providing specialized capabilities for processing medical texts through Natural Language Processing (NLP). They allow users to access nine distinct state-of-the-art accuracy tools, each designed for specific tasks related to medical data handling and analysis. Collectively, these Medical Agents have the ability to extract **261 distinct entity types**. Additionally, they can assign **assertion statuses** to these entities and establish complex **relationships** between them.

</div><div class="h3-box" markdown="1">

### Deidentification/Obfuscation of PHI

Automatically detects and masks or obfuscates personally identifiable information (PHI) from medical text to ensure privacy and compliance with data protection regulations.
   
<iframe width="800" height="450" src="https://www.youtube.com/embed/odSyX3uKjwg?si=XZZO8aY3t82Iqslu&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

</div><div class="h3-box" markdown="1">

### General Medical Entity Extraction
Identifies and extracts general medical entities from text, facilitating quick access to relevant medical terms and concepts.

<iframe width="800" height="450" src="https://www.youtube.com/embed/FjAzlImC0zQ?si=N415bCn2AU2h6i6U&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

</div><div class="h3-box" markdown="1">

### Oncological Entity Extraction
Specialized for recognizing and extracting terms related to oncology, aiding in the analysis of cancer-related medical texts.

<iframe width="800" height="450" src="https://www.youtube.com/embed/qTbH57SI6R0?si=HO8riHFw-cXYeIvK&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

</div><div class="h3-box" markdown="1">

### Posology Entity Extraction
Focuses on extracting dosage and medication instructions from medical documents, crucial for understanding treatment protocols.

<iframe width="800" height="450" src="https://www.youtube.com/embed/5M5nLUdTb4I?si=7uCei72nxBSpvwMe&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

</div><div class="h3-box" markdown="1">

To further support precise and efficient medical data analysis, four new Medical Agents have been made available, tailored to meet the specific requirements of the medical field. Those are seamlessly integrated and available via the @ Selector. By simply typing ‘@’ at the beginning of the query box, users can access the @ Selector menu, which displays all available tools (including the 4 new Medical Agents).

</div><div class="h3-box" markdown="1">
    
![New_NLP_Tools](https://github.com/user-attachments/assets/a355d90a-e4bb-4ea0-9e1d-1018e5ec2a36)

### Extract Radiological Entities and Relations
Designed to extract radiology-related entities, assign assertion statuses to these entities, and establish relationships between them within clinical documents. This tool specializes in identifying entities such as tests, imaging techniques, and test findings within radiology reports, while also accurately determining their assertion statuses and relations.

### Extract Social Determinants of Health
Engineered to extract all clinical and medical entities considered as Social Determinants of Health (SDoH) from textual data, assign assertion statuses to the identified entities, and detect relationships between entities. Specifically, it identifies socio-environmental health determinants such as access to care, diet, employment, and housing from health records, providing comprehensive insights into factors affecting patient health outcomes.

### Extract Adverse Drug Events
Designed to identify and extract adverse drug events and related clinical entities from medical texts. This tool can help users identify adverse reactions to drugs (ADE) from various drug reviews, tweets, and medical texts while also providing assertion statuses and relationship analysis.

### Extract Voice Of The Patient
Designed to detect healthcare-related entities from patient-generated content, assign assertion statuses, and establish relationships between these entities. This tool proficiently identifies clinical and behavioral entities from various sources, including social media posts, blogs, forums, and direct patient communications.

</div><div class="h3-box" markdown="1">

**Export results in CSV format-** All results computed using the Medical Agents can be exported in CSV format. For each detected entity the export also contains confidence information.

**Medical Agents activation-** Users can enable or disable the agents based on their specific needs or preferences, allowing for a personalized experience and control over the processing features used.

**Accessing Medical Agents-** Medical Agents can be invoked in two ways: via regular queries in natural language or by using the '@' operator for direct activation.

**User Benefits**
- **Enhanced Privacy and Compliance**: Safeguards sensitive information by efficiently deidentifying PHI from medical texts.
- **Focused Content Extraction**: Enables precise extraction of medical entities tailored to general, oncological, and posology contexts, enhancing the utility and accuracy of information retrieval.
- **User-Controlled Flexibility**: Offers the flexibility to tailor tool engagement to individual preferences and requirements.
- **Efficient Tool Access**: Simplifies the process of accessing specific Medical Agents through intuitive user interface mechanisms.

</div><div class="h3-box" markdown="1">

## Web Search: For Latest News or Generic Questions

Designed for users needing quick answers to short or generic questions, the Search Web tool is an enhancement of the existing Wikipedia search function. While the Wikipedia search tool offers reliable information from a vast database of general topics, the Search Web tool expands these capabilities by tapping into the entire web. This ensures you access the most comprehensive and relevant information available, making it your go-to solution for swift, accurate insights.

<iframe width="800" height="450" src="https://www.youtube.com/embed/X6s33xuxJAw?si=2dwXuyOQIWNP7OBO&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Key Features**
1. **Expanded Search Capabilities:** Unlike the Wikipedia search tool, which was limited to Wikipedia's database, the Web Search tool queries the entire web. This ensures access to a broader range of information and resources.
2. **Intelligent Query Handling:** The Web Search tool leverages advanced AI algorithms to understand your queries better and retrieve the most accurate and relevant information.
3. **Smart Tool Selection:** The Medical Chatbot is designed to recognize when to utilize the Web Search tool based on the nature of your queries. This means you get the most appropriate and timely responses without needing to specify the tool explicitly.
4. **Up-to-Date Answers:** By searching the entire web, the tool can provide more detailed and diverse answers, drawing from various sources, filtered and structured by the Chatbot's intelligence to give you a well-rounded accurate perspective.

> **_NOTE:_**  To enforce the use of this tool, add the following phrase at the beginning/end of your query: **Search Web** or use the @ operator. 

</div><div class="h3-box" markdown="1">

## John's Memory: Specialized in Summarization and General Queries

John's Memory is a versatile feature within the Medical Chatbot, dedicated to summarization tasks and answering general questions. This tool is particularly useful when users need a succinct summary of extensive information or when they have broad questions that do not require deep, research-level detail. John's Memory employs advanced NLP (Natural Language Processing) techniques to comprehend, interpret, and condense information, making it an invaluable asset for users who need quick insights or overviews.

</div><div class="h3-box" markdown="1">

## @ Operator for Accessibility

Typing '@' in the query box triggers a contextual menu displaying all available tools, similar to tagging functionality in Microsoft Teams.

![DocQA Enhancements](https://github.com/user-attachments/assets/e74e33d2-1262-4fc3-9bf2-32f46f3dca97)


For instance, the @ operator also allows direct access to `MedResearch` tool for targeted questions to all active knowledgebases (see [MedResearch](/docs/en/chatbot/tools)). When using `@MedResearch` at the beginning of your question, the chatbot will directly engage the MedResearch tool without requiring the user to select from multiple options, ensuring a streamlined interaction for focused research tasks.

Similarly, for Web Search and Medical Agents, each tool can be easily selected and utilized with the @ operator as follows:
 - `@web_search`: Query the Web
 - `@deidentification`: De-identification of Medical Text
 - `@obfuscation`: Obfuscation of Medical Text
 - `@medical`: General Medical Entity Extraction
 - `@oncology`: Oncological Entity Extraction
 - `@posology`: Posology Entity Extraction
 - `@adverse_drug_event`: Adverse Drug Events Extraction
 - `@social_determinants_of_health`: Social Determinants of Health Entity Extraction
 - `@radiology`: Radiological Entity Extraction
 - `@voice_of_the_patient `: Voice of the Patient Entity Extraction

When interacting with the chatbot, the generated answer prominently displays the tool used for response generation right above the answer itself. This clarification ensures users know which tool was utilized.

Similarly, when selecting a specific tool using the '@' Selector in your query, the chosen tool is labeled at the top of the query, making it clear which tool was requested for the response generation.
Hence, users can better understand the specialties of these tools and experiment to obtain the best possible responses according to their needs.    

</div>
