---
layout: docs
header: true
seotitle: Medical Chatbot | John Snow Labs
title: Release Notes
permalink: /docs/en/chatbot/releases/release_notes
key: docs-healthcare-gpt
modify_date: "2024-04-24"
show_nav: true
sidebar:
    nav: healthcare-gpt
---
<div class="h3-box" markdown="1">

## 05-17-2024 - Introducing Document Q&A and NLP Tools

We are excited to announce two significant enhancements to the Medical Chatbot: the Document Q&A (DocQA) feature and the NLP Tools feature. These additions are designed to streamline your interactions and deepen your engagement with medical texts. The DocQA feature enables seamless management and querying of up to 10 text or PDF documents, providing a focused, session-based interaction. NLP Tools feature introduces a suite of specialized tools for the extraction and analysis of medical information, tailored to your needs. Whether you are interested in extracting entities from your medical text, to de-identify or summarize them, NLP Tools get you covered. These enhancements are part of our continuous effort to provide powerful, user-friendly tools that support and enhance your daily medical information handling and decision-making processes.

## Introducing Document Q&A (DocQA) Feature

### Overview
The DocQA feature enhances the Medical Chatbot by allowing users to upload and interact with up to 10 text (.txt) or PDF (.pdf) documents. This feature is designed to provide tailored answers based on the content of the uploaded documents.

<iframe width="800" height="450" src="https://www.youtube.com/embed/BJ4cXJl7ZyY?si=P1GBmRtTBTmPeRJ0&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>



### Key Features
1.**Document Upload and Session Initiation**
   - Users can upload one or several documents directly into the chat interface.
   - Upon uploading documents, a DocQA session is automatically initiated.
   - Each user is limited to one active DocQA session at any given time.

![Start_DocQA_Session](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/17f402c1-e3ff-4533-b135-fcf47791444a)

2.**Session Management and Visibility**
   - The active DocQA session appears as "Document Q&A" in the Conversation History.
   - This session is pinned to the top of the list and remains there until the session is closed or the conversation is removed.

<img width="2944" alt="Session_Visibility" src="https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/db5b6fd6-867d-4157-9240-c472e23e5719">

3.**Document Management within Sessions**
   - If a document is uploaded in a regular chat while a DocQA session is active, it will be automatically added to the existing session's Target Documents.
   - Uploading more than 10 documents triggers an error message, prompting the user to remove documents before adding new ones.

![Upload_to_existing_session](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/3ad7581f-2c52-4232-a4a9-d2a00b28c37a)

4.**Session Interaction**
   - Users can start a new chat by clicking the "New Chat" button, which opens an empty chat window.
   - Users can seamlessly transition to a new chat at any point to address queries beyond the scope of the DocQA Session.
   - Users can easily navigate back to an active DocQA session via the Conversation History.

![DocQA_Switch_to_Normal_Chat](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/c1acce8b-d8d9-4805-8246-c99ef72d3100)

5.**Session Termination**
   - Removing a DocQA session from the Chat History will end the session and delete the associated files.
   - Removing all the files from the DocQA Session's Target Documents will also end the session.
   - Once a DocQA chat session is ended, it transitions into a read-only mode, providing users with a comprehensive overview of the conversation. 

![Terminate_DocQA_Session](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/1ba5e643-fda4-44f2-ae0a-3ba1d3a7fb70)

6.**Query Handling and Document Interaction**
   - Questions asked within the DocQA session are answered using information from the target documents.
   - Responses include references to the document content. Clicking on a reference will display the document and highlight the relevant paragraph.

![Reference_highlighting](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/91c5dfe2-f77d-463a-af5b-287831d87b41)

### User Benefits

- **Focused Answers:** Provides precise information derived directly from uploaded documents.
- **Efficient Navigation:** Seamlessly switch between general chat and document-specific queries.
- **Resource Management:** Control over the documents within the session ensures relevance and efficiency in information retrieval.
- **Accelerated Learning**: Efficiently reads and analyzes the given documents which helps aid in quick content summarization and analysis for learning.

This feature is part of our ongoing commitment to enhance user interaction and improve the informational value of the Medical Chatbot. We look forward to your feedback and continual engagement with this new functionality.

## Introducing the NLP Tools 

### Overview
The NLP Tools feature is a new addition to the Medical Chatbot, providing specialized capabilities for processing medical texts through Natural Language Processing (NLP). This feature allows users to access five distinct state-of-the-art accuracy tools, each designed for specific tasks related to medical data handling and analysis.

### Key Features
1.**Tools Overview**
   - **Deidentification/Obfuscation of PHI**: Automatically detects and masks or obfuscates protected health information (PHI) from medical text to ensure privacy and compliance with data protection regulations. Users can specify to de-identify or obfuscate the medical text based on their requirements. 
   
   <iframe width="800" height="450" src="https://www.youtube.com/embed/odSyX3uKjwg?si=XZZO8aY3t82Iqslu&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

   - **General Medical Entity Extraction**: Identifies and extracts general medical entities from text, facilitating quick access to relevant medical terms and concepts.

   <iframe width="800" height="450" src="https://www.youtube.com/embed/FjAzlImC0zQ?si=N415bCn2AU2h6i6U&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

   - **Oncological Entity Extraction**: Specialized for recognizing and extracting terms related to oncology, aiding in the analysis of cancer-related medical texts.

   <iframe width="800" height="450" src="https://www.youtube.com/embed/qTbH57SI6R0?si=HO8riHFw-cXYeIvK&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

   - **Posology Entity Extraction**: Focuses on extracting dosage and medication instructions from medical documents, crucial for understanding treatment protocols.

   <iframe width="800" height="450" src="https://www.youtube.com/embed/5M5nLUdTb4I?si=7uCei72nxBSpvwMe&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

2.**Customizable Accessibility**
   - Users can enable or disable NLP tools based on their specific needs or preferences, allowing for a personalized experience and control over the processing features used.
3.**Accessing Tools**
   - NLP tools can be invoked in two ways: via regular queries in natural language or by using the '@' operator for direct tool activation.
   - Typing '@' at the beginning of the query box triggers a contextual menu displaying all available tools, similar to tagging functionality in Microsoft Teams.
   - The @ operator also allows direct access to `MedResearch` and `Wikipedia` tools for targeted questions. For instance, when using `@medical_research` at the beginning of your question, the chatbot will directly engage the `MedResearch` tool without requiring the user to select from multiple options, ensuring a streamlined interaction for focused research tasks.
   - Similarly, for Wikipedia and NLP Tools, each tool can be easily selected and utilized with the @ operator as follows:
       - `@search_wikipedia`: Query Wikipedia Pages
       - `@deidentification`: De-identification of Medical Text
       - `@obfuscation`: Obfuscation of Medical Text
       - `@ner_medical`: General Medical Entity Extraction
       - `@ner_medical_oncology `: Oncological Entity Extraction
       - `@ner_medical_posology `: Posology Entity Extraction
   - When interacting with the chatbot, the generated answer prominently displays the tool used for response generation right above the answer itself. This clarification ensures users know which tool was utilized.
   - Similarly, when selecting a specific tool using the '@' Selector in your query, the chosen tool is labeled at the top of the query, making it clear which tool was requested for the response generation.
   - Hence, users can better understand the specialties of these tools and experiment to obtain the best possible responses according to their needs.    
![Risk_Factors](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/e70788ea-77bc-48ca-9583-4e3586605241)

4.**Export results in CSV format**
   - All the Entity Extraction results computed using the NLP tools can be exported in CSV format. For each detected entity, the export also contains confidence information, ensuring transparency and reliability in data analysis.

![CSV_Download](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/18526211-0ebc-43bb-beba-2c2439d479b7)

### User Benefits
- **Enhanced Privacy and Compliance**: Safeguards sensitive information by efficiently deidentifying PHI from medical texts.
- **Focused Content Extraction**: Enables precise extraction of medical entities tailored to general, oncological, and posology contexts, enhancing the utility and accuracy of information retrieval.
- **User-Controlled Flexibility**: Offers the flexibility to tailor tool engagement to individual preferences and requirements.
- **Efficient Tool Access**: Simplifies the process of accessing specific NLP tools through intuitive user interface mechanisms.


## 03-13-2024

We are delighted to announce a new update for the Medical Chatbot, bringing significant improvements across the board to enhance user experience and interaction. Here are some highlights:
- **Enhanced Load Management**: To ensure consistent performance during peak usage, we've implemented a load management feature. This optimizes the handling of concurrent requests, maintaining system efficiency and alerting users during periods of high demand with a clear message to enhance user experience.
- **Contextual Follow-up Question Suggestions**: Elevating user engagement, the chatbot now suggests relevant follow-up questions after each response. This feature, which users can toggle on or off, aids in exploring topics in-depth, fostering a more engaging and seamless information exchange.
- **Response Style Customization**: Users can now easily customize their conversation settings, including response styles, through a more accessible and intuitive interface. This update allows for dynamic response style selection, enhancing the personalization of interactions.
- **Advanced Resource Management**: A new system for managing available resources such as tools and knowledge bases (KBs) has been introduced. Users can now directly control these resources, adjusting the chatbot's capabilities to their preferences and needs, ensuring a more tailored and effective response generation.
- **Enhanced Transparency for Memory-Based Responses**: We've introduced notifications to alert users when a response is generated from the chatbot's memory. This feature encourages users to verify the information, especially considering the fast pace of medical advancements.
- **Ongoing Enhancements and Bug Fixes**: Alongside these new features, we've implemented a range of bug fixes and internal improvements. These are designed to enhance the tool's efficiency and effectiveness, although specific details remain under wraps for now.

These updates aim to provide a more personalized, engaging, and reliable chatbot experience. For more detailed information on these enhancements and how they can improve your interaction with the Medical Chatbot, we invite you to read the full release notes.

</div><div class="h3-box" markdown="1">

## Enhanced Load Management for Improved User Experience

In our continuous effort to ensure the reliability and responsiveness of the Medical Chatbot, especially during periods of high user engagement, we have implemented a load management feature that effectively limits the number of concurrent requests to maintain optimal system performance.

With the introduction of this feature, should the user volume exceed the system's configured threshold, resulting in an inability to process additional requests, the Medical Chatbot's user interface will now display a clear and informative message: “We’re experiencing exceptionally high demand in the Medical Chatbot. Please try again in a few minutes.” This message is designed to inform users of the current high demand and guide them to retry their request after a brief period, ensuring a better user experience during peak times.

![high demand final](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/515acf12-6e26-47b2-9e76-a0c73004eded)


</div><div class="h3-box" markdown="1">

## Introducing Contextual Follow-up Question Suggestions

In our latest update, we are excited to introduce a significant enhancement to the user interaction experience within the Medical Chatbot. This new feature aims to enrich the dialogue between the user and the chatbot, providing a more engaging and seamless information exchange.

</div><div class="h3-box" markdown="1">

### Follow-up Question Suggestions

After the Medical Chatbot generates a response to a user's medical query, the system will now automatically present a set of follow-up questions that are relevant to the current topic. These suggestions are designed to anticipate the user's potential next steps or inquiries, based on the context of the conversation. 

The suggested questions will be displayed just above the chat box, making it easy for users to view and select. By simply clicking on one of these suggestions, users can continue their conversation without the need to manually input their next question. This feature not only enhances the user experience by making interactions more fluid and intuitive but also helps in deepening the exploration of topics relevant to the user's needs. 

</div><div class="h3-box" markdown="1">

### User-Controlled Suggestions

Recognizing the diverse preferences of our users, we have incorporated the flexibility to toggle the follow-up question suggestions feature on or off. This customization option allows users to tailor their interaction with the Medical Chatbot according to their desired level of guidance and exploration within the conversation. Whether users prefer a more self-directed inquiry or guided discovery, this feature enhances the platform's adaptability to individual user needs.
Furthermore, the generation of follow-up questions has been intelligently engineered to specifically address medical-based queries and responses, ensuring the delivery of high-quality suggestions only whenever pertinent. 

![Suggestions_1](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/26aaa19f-aa9b-420c-b4df-bcdcd96a237a)

</div><div class="h3-box" markdown="1">

## Response Style Customization

In our ongoing efforts to improve the user interface and overall experience of the Medical Chatbot, we are excited to announce an enhancement to how users can customize their conversation settings, specifically regarding response styles.

</div><div class="h3-box" markdown="1">

### Enhanced Accessibility of Conversation Settings

To provide a more intuitive and accessible way for users to customize their interaction with the Medical Chatbot, we have 
repositioned the conversation settings. Previously located next to the "New Conversation" button within a settings pop-up, these settings could be overlooked by users. We have addressed this by moving the conversation settings to a more prominent position:
1. **Contextual Menu Placement**: The contextual menu, which includes the conversation settings, has been relocated below the response box. This change ensures visibility immediately after a response is generated, especially important when dealing with longer responses that could previously obscure the menu.
2. **Dedicated Settings Icon**: A settings icon has been introduced to the contextual menu for conversation settings, making it easier for users to find and adjust their response style preferences. The response style options have been removed from the Chat settings pop-up and are now accessible via a separate pop-up when the user clicks on the conversation settings icon in the contextual menu. This approach allows for a more streamlined and focused user experience.
   
![Screenshot 2024-03-13 at 2 33 19 PM](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/f2e12115-604d-4e17-b51e-68e25c0212d2)

</div><div class="h3-box" markdown="1">

### Dynamic Response Style Selection

Upon initiating a new conversation, the Default response style is applied. However, users now have the flexibility to change the response style after the first response is generated by the chatbot. By clicking on the conversation settings button, users can select a different style, prompting the chatbot to regenerate the response in the new style. This selected style will persist for all subsequent interactions within the current conversation until the conversation concludes or the user opts to change the style again.

![response style_1](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/26996a41-a9f6-455f-8ea2-b238f850b090)

</div><div class="h3-box" markdown="1">

## Introducing Advanced Resource Management

We are excited to announce an enhancement in how users interact with and manage the resources available within the Medical Chatbot. This update introduces a more intuitive way for users to visualize and control the tools and knowledge bases (KBs) that assist in generating responses to their queries.

</div><div class="h3-box" markdown="1">

### Streamlined Access to Tools and Knowledge Bases

To improve accessibility and user experience, we have made the following changes:
1. **Enhanced Tools Accessibility**: The Chat settings popup, previously located next to the "New Chat" button, has been replaced. We've introduced a "Tools" link situated within the chat box. This popup provides direct access to the various resources available to the chatbot.
2. **Dynamic Resource Display and Management**: Upon accessing the "Tools" section, users will now be presented with a list of available tools, including but not limited to Wikipedia and MedResearch, with future additions such as NLPTools and Text2SQL anticipated. This feature allows users to easily toggle these resources on or off, directly influencing the tools that the Language Learning Model (LLM) leverages to respond to queries.
3. **Customizable Knowledge Base Interaction**: When the MedResearch tool is enabled, users will be shown a list of accessible KBs, similar to the existing functionality. Importantly, users now have the capability to individually activate or deactivate these KBs. This flexibility ensures that the queries are matched against the most relevant and preferred knowledge bases, enhancing the accuracy and relevance of the chatbot's responses. 
When all tools are turned off, John will respond from its memory. See next section for details.


![Tools_Selection_Gif](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/b9b2f9fd-e938-43c6-a050-e2e201f78cb2)

</div><div class="h3-box" markdown="1">

## Enhanced Transparency for LLM Memory-Based Responses

In our ongoing commitment to ensuring the accuracy and reliability of the information provided by John, we are introducing a new feature designed to enhance user awareness and encourage verification of information.

</div><div class="h3-box" markdown="1">

### Notification for Memory-Based Responses

To address instances where the chatbot generates answers from previously acquired knowledge or "memory", we have implemented a notification system to alert users. This is particularly important as it pertains to the dynamic nature of medical information and developments.

</div><div class="h3-box" markdown="1">

### Updated User Interface Notification

When John provides a response drawn from memory, the following changes will be evident in the user interface:
- **Notification Replaces References**: The usual "References" section will be substituted with a distinct notification to users. This alert aims to inform users that the response has been generated based on information available up to a certain date, highlighting that it may not include the latest findings or updates.
- **Content of the Notification**: The notification will convey the following message: “Please note that this response was generated from John's memory and may not reflect the most recent developments. For the most current information, consider verifying details from up-to-date sources.” This message is designed to prompt users to seek out the most current data for their inquiries, ensuring they have access to the most accurate and relevant information.

![image](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/2ba0c6b5-c7f8-42aa-aa82-1528e9e0fceb)

</div><div class="h3-box" markdown="1">

## Ongoing Enhancements and Bug Fixes

In addition to the new UI features, this update includes a series of bug fixes and improvements aimed at optimizing the internal management of knowledge bases (KBs) and tools. These enhancements are designed to improve the efficiency and effectiveness of the tool, ensuring that users receive the most accurate and relevant responses. While the specifics of these updates are not disclosed at this time, we assure our users that these changes significantly contribute to the robustness and reliability of the Medical Chatbot's operations.

We believe these updates, both in enhancing transparency and usability and in improving the internal workings of the chatbot, will greatly enrich the user experience. We remain committed to continuous improvement and innovation, always prioritizing the needs and satisfaction of our users.

</div><div class="h3-box" markdown="1">

## 02-21-2024

**Welcome to the Medical Chatbot Documentation and Updates Hub!**

We are excited to announce the launch of the Medical Chatbot Releases Page, a centralized repository for all the latest features, enhancements, and resolutions of known issues within the Medical Chatbot platform. This dedicated space is designed to keep users informed of the most recent developments, enabling seamless testing and facilitating the provision of valuable feedback. Our commitment is to ensure that users have immediate access to the latest information, empowering them to leverage the full capabilities of the Medical Chatbot effectively. Stay updated with us as we continue to improve and expand the functionalities of the Medical Chatbot to meet and exceed your expectations.

</div>
