---
layout: docs
header: true
seotitle: Medical Chatbot | John Snow Labs
title: Agents
permalink: /docs/en/chatbot/agents
key: docs-healthcare-gpt
modify_date: "2025-03-28"
show_nav: true
sidebar:
    nav: healthcare-gpt
---

<div class="h3-box" markdown="1">

The Medical Chatbot is equipped with several agents and tools, each tailored to meet different information needs and research requirements. These agents are `MedResearch`, `Web Search`, `Medical Agents`, `Drug Insights`, `US Healthcare Provider` and `John's Memory`, collectively providing a comprehensive solution for a wide range of queries.

## MedResearch: Your Gateway to Academic Medical Research

`MedResearch` stands as the cornerstone of the Medical Chatbot, offering exhaustive coverage of academic papers and research results. This tool is meticulously designed to query multiple prestigious databases:
- PubMed
- BioRxiv
- MedRxiv
- MDPI

Whether you're looking for the latest findings in a specific medical field, detailed drug information, or comprehensive research outcomes, MedResearch provides direct access to a vast repository of academic resources. This feature is especially valuable for medical professionals, researchers, and students seeking to base their work on the most current and authoritative sources.

For questions targeting a certain KB, you can turn available KBs on and off according to your preference. 

![Select the KB you want to target with your question](\assets\images\chatbot\KBSelection.png)


> **_NOTE:_**  To enforce the use of this tool, use the @ operator.

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
4. **Up-to-Date Answers:** By searching the entire web, the tool can provide more detailed and diverse answers, drawing from various sources, filtered and structured by the Chatbot's intelligence to give you a well-rounded, accurate perspective.

> **_NOTE:_**  To enforce the use of this tool, use the @ operator. 

</div><div class="h3-box" markdown="1">

## Drug Insights: Get Precise Medication Information

The Drug Insights tool is an advanced feature within the Medical Chatbot, designed to provide comprehensive, FDA-sourced medication information. Whether you need details on dosages, potential side effects, or drug interactions, this tool ensures you receive safe, reliable, and up-to-date insights for informed decision-making.

<iframe width="800" height="450" src="https://www.youtube.com/embed/dzXOlaXtKts?si=FZQpMjSD6UopVNGv&hd=1" title="Drug Insights Agent" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


**Key Features**

**1. Comprehensive Drug Information** 

The Drug Insights agent provides users with information about medications, covering aspects such as active and inactive ingredients, potential side effects, and recommended dosages. Users can inquire about indications and usage guidelines, warnings, contraindications, and specific conditions under which a drug should not be used. Additionally, the tool delivers insights into drug interactions, offering clear guidance on which medications or substances to avoid combining, ensuring safe and informed use.

**2. Context-Aware Responses**

One of the standout features of the Drug Insights agent is its ability to process complex, situational queries. Users can ask questions about medication use based on specific symptoms, age groups, or pre-existing conditions, and the tool provides personalized, context-aware responses. This capability extends to offering advice on storage and handling, ingestion methods, and even how medications interact with certain foods or beverages. By tailoring answers to individual needs, the agent empowers users to make well-informed decisions about their healthcare.

**3. Direct Citations**

To ensure accuracy and credibility, the agent references FDA-approved drug leaflets and related documentation in its responses. These citations are not only included in the generated answers but are also made accessible to users via an intuitive user interface. This allows users to explore the source material in greater depth, gaining a more comprehensive understanding of the medications. The documentation is organized into easily navigable sections, making it simple to find detailed information relevant to the user's query.

> **_NOTE:_**  To enforce the use of this tool, use the @ operator. 

</div><div class="h3-box" markdown="1">

## US Healthcare Provider Search: Find Verified Medical Professionals

The US Healthcare Provider Search tool allows users to locate verified healthcare professionals and organizations across the United States. By leveraging the National Plan and Provider Enumeration System (NPPES) database, maintained by the Centers for Medicare & Medicaid Services (CMS), this tool ensures accurate and up-to-date provider information for patients, researchers, and healthcare professionals.

<iframe width="800" height="450" src="https://www.youtube.com/embed/9q3bAgAkPQ0?si=llPGvA8zy3mlQXZP&hd=1" title="Drug Insights Agent" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


**Key Features**

**1. NPPES Database Integration** 

This tool leverages the National Plan and Provider Enumeration System (NPPES), managed by the U.S. Centers for Medicare & Medicaid Services (CMS). The database contains details about healthcare providers and organizations, including their National Provider Identifier (NPI).

**2. DB Query via Natural Language Prompts**

The Medical Chatbot transforms user queries into structured searches, enabling precise retrieval of data from the NPPES database. Users can search by criteria such as name, location, taxonomy (specialty), and other relevant parameters to identify healthcare providers that align with their requirements. 

**3.Data Output**

Results are presented in tabular format, allowing users to specify the details they wish to include. Additionally, the data can be exported as CSV files for future reference or analysis. The chatbot also enhances the user experience by providing  insights and contextual responses that go beyond the data itself, addressing more nuanced queries effectively. 


> **_NOTE:_**  To enforce the use of this tool, use the @ operator. 

</div><div class="h3-box" markdown="1">

## John's Memory: Specialized in Summarization and General Queries

John's Memory is a versatile feature within the Medical Chatbot, dedicated to summarization tasks and answering general questions. This tool is particularly useful when users need a succinct summary of extensive information or when they have broad questions that do not require deep, research-level detail. John's Memory employs advanced NLP (Natural Language Processing) techniques to comprehend, interpret, and condense information, making it an invaluable asset for users who need quick insights or overviews.

</div><div class="h3-box" markdown="1">

## @ Operator for Accessibility

Typing '@' in the query box triggers a contextual menu displaying all available tools, similar to the tagging functionality in Microsoft Teams.

![DocQA Enhancements](https://github.com/user-attachments/assets/e74e33d2-1262-4fc3-9bf2-32f46f3dca97)


For instance, the @ operator also allows direct access to `MedResearch` tool for targeted questions to all active knowledge bases (see [MedResearch](/docs/en/chatbot/tools)). When using `@medical_research` at the beginning of your question, the chatbot will directly engage the MedResearch tool without requiring the user to select from multiple options, ensuring a streamlined interaction for focused research tasks.

Similarly, for Web Search and Medical Agents, each tool can be easily selected and utilized with the @ operator as follows:
 - `@web_search`: Query the Web
 - `@drug_insights`: Learn About Drugs, Their Interactions, and Side Effects
 -  `@text_to_sql_nppes`: Ask About US Medical Providers
 - `@deidentification`: De-identification of Medical Text
 - `@obfuscation`: Obfuscation of Medical Text
 - `@medical`: General Medical Entity Extraction
 - `@oncology`: Oncological Entity Extraction
 - `@posology`: Posology Entity Extraction
 - `@adverse_drug_event`: Adverse Drug Events Extraction
 - `@social_determinants_of_health`: Social Determinants of Health Entity Extraction
 - `@radiology`: Radiological Entity Extraction
 - `@voice_of_the_patient `: Voice of the Patient Entity Extraction

When users select a tool using the @ operator, the name of the tool is displayed above the chatbox for added clarity. The Tool will be used for all consecutive questions after selection to prevent the need of selecting the same tool for every question in the conversation. The users can remove the selection at any time and choose a different task as needed, improving flexibility and control over the chatbot interaction.

The generated answer prominently displays the tool used for response generation right above the answer itself. This clarification ensures that users know which tool was utilized.

Similarly, when selecting a specific tool using the '@' Selector in your query, the chosen tool is labeled at the top of the query, making it clear which tool was requested for the response generation.
Hence, users can better understand the specialties of these tools and experiment to obtain the best possible responses according to their needs.    

</div>
