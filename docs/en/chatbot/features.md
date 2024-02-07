---
layout: docs
header: true
seotitle: Medical Chatbot | John Snow Labs
title: Features
permalink: /docs/en/chatbot/features
key: docs-healthcare-gpt
modify_date: "2024-02-07"
show_nav: true
sidebar:
    nav: healthcare-gpt
---

## Access Latest Medical Research Results

The Medical Chatbot leverages advanced algorithms to sift through extensive databases, journals, and publications, delivering the most relevant and up-to-date research findings directly to healthcare professionals. This feature ensures that users can stay abreast of the latest developments in their field without the need to manually search through overwhelming volumes of medical literature. By using a natural chat QA interface, the chatbot simplifies the process of finding and accessing new studies, clinical trials, and insights, making it an indispensable tool for medical research and practice.

<iframe src="/assets/images/chatbot/AskMedicalQuestions.gif" width="300" height="200"  style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share" allowFullScreen="true"></iframe>

In this example, you can notice a conversation focused on dry eye disease, starting with a general inquiry. `John` explains what the disease consists of and highlights its symptoms with references from recent literature. If users ask follow-up questions, the `John` can put those into context and understand it has to provide treatment options for the disease mentioned in the previous interactions. Users can also refer to parts of the previous responses to ask for more details. In the above example, I asked for more info on point 1. `John` understands point one refers to artificial tears and gives a detailed overview of the available types of artificial tears with references to sources used to compile the answers. 
You can also guide the chatbot to provide more specific information in the current context. In this example, I was interested to learn more about HA-based artificial tears. Notice that the answer does not generically describe HA-based drops but takes into account the context of the conversation, and explains how those artificial tears can be used for treating dry eye disease. You can also specify in your question if you are interested in studies, clinical trials, or other types of articles. Such as in the above example. 
With this chatbot, you can expect a seamless conversational experience, where the flow of information is as natural and intuitive as a discussion with a trusted colleague. 


## Explainable Responses with Citations
In the field of healthcare, the precision and source of data hold paramount importance. To address this, our medical chatbot has been engineered to offer more than simple information snippets in response to medical inquiries. It serves as a portal to the underlying research from which its answers are derived. This level of transparency is attained through the chatbot's unique citation feature.
The chatbot leverages a constantly updated knowledge graph for its responses, sourced from an extensive array of medical texts. Primary knowledge bases like Pubmed and Medrxiv are refreshed daily, ensuring the provision of the latest information to our users. The chatbot's replies are grounded in data from this knowledge graph, referencing peer-reviewed articles, clinical databases, or user-specific custom KBs. This approach guarantees traceability of information and significantly reduces the occurrence of false or misleading information. This functionality not only adds depth and context to the responses but also aligns with the standards of academic research and evidence-based practice.

<iframe src="/assets/images/chatbot/Citations.mp4" width="300" height="200"  style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share" allowFullScreen="true"></iframe>

Users have the flexibility to direct their questions to specific knowledge bases, enabling access to information tailored to their unique medical specializations or areas of interest.
Our medical chatbot ensures the explainability of its responses, enhancing user comprehension of the logic underlying its conclusions. Each piece of information is substantiated with citations, offering users the opportunity to further investigate the sources.


## Medical Conversations
Designed to simulate an interaction with a knowledgeable colleague, the Medical Chatbot facilitates nuanced medical conversations. It understands context and can manage follow-up questions, ensuring that healthcare professionals can engage in detailed dialogues to extract specific information necessary for clinical decisions or research inquiries. Whether discussing symptoms, treatments, or the latest medical research, the chatbot's conversational capabilities make it an effective tool for dynamic and informative exchanges.

<iframe src="/assets/images/chatbot/Citations.mp4" width="300" height="200"  style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share" allowFullScreen="true"></iframe>

## Summarize Medical Content

In the medical domain, where information is as rich as it is overwhelming, the ability to distill complex content into concise, digestible summaries can prove very convenient. John addresses this challenge head-on, employing advanced language processing to extract key points from lengthy medical texts, research papers, and clinical guidelines, presenting them in a clear and succinct format.

<iframe src="/assets/images/chatbot/Summarize.mp4" width="300" height="200" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share" allowFullScreen="true"></iframe>

In the example above you can notice how the chatbot can take a dense, multi-page document and within moments, offer you a 3 sentence summary that captures the essence of the material. It can highlight the most pertinent information, so you can quickly grasp the salient points without wading through the entire text.
The summary feature is more than a simple truncation of text; it is an intelligent synthesis that understands the context, retains critical details, and omits the less essential ones, ensuring that the heart of the content is preserved and made more accessible.
Whether for academic purposes, patient care, or personal edification, this summarization tool is crafted to save time, reduce cognitive load, and enhance understanding. It empowers healthcare professionals to stay informed and focused, freeing up precious time for the human aspect of medicine—patient interaction.


## Create Custom Knowledge Bases
Recognizing the diverse needs of medical practices and research domains, the Medical Chatbot allows users to create custom knowledge bases from their private document collections - be they research papers, clinical trial data, or institutional records. For this, `John` applies state-of-the-art natural language processing techniques to understand your documents and to create intelligent knowledge repositories tailored to your unique informational ecosystem. By building a custom knowledge base, you gain a tool that speaks directly to your needs, understands your specific medical dialect, and provides rapid, pinpoint access to the information you rely on. 
This video details the steps for creating a custom knowledge base. 

<iframe src="/assets/images/chatbot/CustomKB.mp4" width="300" height="200"  style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share" allowFullScreen="true"></iframe>

First, the user defines a name for the Knowledge Base and provides a link to an s3 bucket where the target documents reside as well as access credentials to the data. A quick preview of the files located in the s3 bucket is shown so the users can check that the provided bucket is the correct one. After this validation, the ingestion process starts. Currently, the chatbot can process TXT and PDF files.

Once the KB is in place, you can define access permissions with granularity, ensuring that relevant teams, departments, or research groups within your organization can connect with the precise data they need, when they need it, under the governance protocols you set. As such, the medical chatbot ensures that sensitive information remains secure, while still being readily accessible to authorized personnel, thereby enhancing collaboration without compromising confidentiality.


## Ask About Your Own Patients
In the practice of medicine, each patient has a unique narrative, a confluence of history, symptoms, and treatment responses. Usually, this data is presented in an unstructured natural language format. By integrating custom knowledge bases containing patient data, healthcare professionals can ask `John` for detailed insights into patient's medical histories, treatment plans, and progress notes. This capability is governed by strict authentication protocols, ensuring that sensitive patient information remains confidential and accessible only to authorized personnel.

Furthermore, you can easily access the paragraphs used to compile the answers to get more details about the patients and even go back to the source document for further investigation.


<iframe src="/assets/images/chatbot/AskAboutPatients.mp4" width="300" height="200" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share" allowFullScreen="true"></iframe>

## Response Styles and Customization
To accommodate the varied communication preferences of different organizations, the Medical Chatbot offers customizable response styles. Users can select from predefined styles or define their own, adjusting the tone, complexity, and length of responses to match their organizational culture. This flexibility ensures that the chatbot can communicate effectively with healthcare professionals, patients, and research teams alike, in a manner that resonates with each user's expectations.

<iframe src="/assets/images/chatbot/DefineResponseStyle.mp4" width="300" height="200" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write;" allowFullScreen="true"></iframe>

## Bookmarks and Conversation History
The Conversation History and Bookmarks features are designed to enhance the user experience by maintaining a comprehensive log of interactions and allowing for easy retrieval of important information. Healthcare professionals can revisit previous queries and responses, ensuring continuity in ongoing discussions and facilitating easy access to critical information when needed. These features support efficient information management and contribute to the chatbot's utility as a clinical and research tool.

![Check saved Questions, Responses and Entire Conversations](/assets/images/chatbot/Bookmarks.png)

## Authentication and Authorization
The Medical Chatbot is engineered with an advanced security architecture, incorporating rigorous authentication and authorization protocols. At the core of its security framework is the Fine-grained Access Control system. This feature empowers administrative users to meticulously manage permissions and access rights, ensuring that sensitive medical data is exclusively accessible to verified personnel. Administrators have the flexibility to configure access on a granular level - by roles, groups, or individual user credentials. This meticulous approach to data security not only protects sensitive information but also customizes each user's interaction with the chatbot based on their specific clearance and professional requirements, thereby enhancing both the security and the practical utility of the information exchanged.

In terms of integration with existing organizational structures, the Medical Chatbot supports User Federation, seamlessly interfacing with LDAP (Lightweight Directory Access Protocol) and Active Directory. This integration means that user accounts and identities already managed within these systems can be directly linked to the chatbot, streamlining the authentication process and reducing administrative overhead.

Moreover, the chatbot adheres to Standard Protocols such as OpenID Connect and OAuth 2.0, which are globally acknowledged for secure identity management and authorization. This compliance ensures that the chatbot’s authentication methods are both robust and aligned with industry best practices. Additionally, the chatbot introduces Social Login through Identity Brokering, permitting user access via familiar LinkedIn credentials, thus balancing ease of access with stringent security protocols - a critical feature in managing sensitive medical data.
