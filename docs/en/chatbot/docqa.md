---
layout: docs
header: true
seotitle: Medical Chatbot | John Snow Labs
title: DocQA
permalink: /docs/en/chatbot/docqa
key: docs-healthcare-gpt
modify_date: "2024-05-17"
show_nav: true
sidebar:
    nav: healthcare-gpt
---

<div class="h3-box" markdown="1">

The DocQA feature enhances the Medical Chatbot by allowing users to upload and interact with up to 10 text (.txt) or PDF (.pdf) documents. This feature is designed to provide tailored answers based on the content of the uploaded documents.

<iframe width="800" height="450" src="https://www.youtube.com/embed/BJ4cXJl7ZyY?si=P1GBmRtTBTmPeRJ0&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

</div><div class="h3-box" markdown="1">

## Key Features

### Document Upload and Session Initiation
   - Users can upload one or several documents directly into the chat interface.
   - Upon uploading documents, a DocQA session is automatically initiated.
   - Each user is limited to one active DocQA session at any given time.


![Start_DocQA_Session](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/17f402c1-e3ff-4533-b135-fcf47791444a)

</div><div class="h3-box" markdown="1">

### Session Management and Visibility
   - The active DocQA session appears as DocQA in the Conversation History.
   - This session is pinned to the top of the list and remains there until the session is closed or the conversation is removed.


<img width="2944" alt="Session_Visibility" src="https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/db5b6fd6-867d-4157-9240-c472e23e5719">

</div><div class="h3-box" markdown="1">

### Document Management within Sessions
   - If a document is uploaded in a regular chat while a DocQA session is active, it will be automatically added to the existing session's Target Documents.
   - Uploading more than 10 documents triggers an error message, prompting the user to remove documents before adding new ones.


![Upload_to_existing_session](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/3ad7581f-2c52-4232-a4a9-d2a00b28c37a)

</div><div class="h3-box" markdown="1">

### Session Interaction
   - Users can start a new chat by clicking the "New Chat" button, which opens an empty chat window.
   - Users can seamlessly transition to a new chat at any point to address queries beyond the scope of the DocQA Session.
   - Users can easily navigate back to an active DocQA session via the Conversation History.


![DocQA_Switch_to_Normal_Chat](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/c1acce8b-d8d9-4805-8246-c99ef72d3100)

</div><div class="h3-box" markdown="1">

### Session Termination
   - Removing a DocQA session from the Chat History will end the session and delete the associated files.
   - Removing all the files from the DocQA Session's Target Documents will also end the session.
   - Once a DocQA chat session is ended, it transitions into a read-only mode, providing users with a comprehensive overview of the conversation. 


![Terminate_DocQA_Session](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/1ba5e643-fda4-44f2-ae0a-3ba1d3a7fb70)

</div><div class="h3-box" markdown="1">

### Query Handling and Document Interaction
   - Questions asked within the DocQA session are answered using information from the target documents.
   - Responses include references to the document content. Clicking on a reference will display the document and highlight the relevant paragraph.


![Reference_highlighting](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/91c5dfe2-f77d-463a-af5b-287831d87b41)

**User Benefits**
- **Focused Answers:** Provides precise information derived directly from uploaded documents.
- **Efficient Navigation:** Seamlessly switch between general chat and document-specific queries.
- **Resource Management:** Control over the documents within the session ensures relevance and efficiency in information retrieval.
- **Accelerated Learning**: Efficiently reads and analyzes the given documents which helps aid in quick content summarization and analysis for learning.

This feature is part of our ongoing commitment to enhance user interaction and improve the informational value of the Medical Chatbot. We look forward to your feedback and continual engagement with this new functionality.

</div>