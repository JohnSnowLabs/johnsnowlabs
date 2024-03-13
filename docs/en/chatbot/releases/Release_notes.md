---
layout: docs
header: true
seotitle: Medical Chatbot | John Snow Labs
title: Release Notes
permalink: /docs/en/chatbot/releases/release_notes
key: docs-healthcare-gpt
modify_date: "2024-03-15"
show_nav: true
sidebar:
    nav: healthcare-gpt
---
<div class="h3-box" markdown="1">


## 03-15-2024

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

![high demand](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/d0e5408c-53f2-4116-9f54-aa286f748e9b)

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
1. Contextual Menu Placement: The contextual menu, which includes the conversation settings, has been relocated below the response box. This change ensures visibility immediately after a response is generated, especially important when dealing with longer responses that could previously obscure the menu.
2. Dedicated Settings Icon: A settings icon has been introduced to the contextual menu for conversation settings, making it easier for users to find and adjust their response style preferences. The response style options have been removed from the Chat settings pop-up and are now accessible via a separate pop-up when the user clicks on the conversation settings icon in the contextual menu. This approach allows for a more streamlined and focused user experience.
   
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
1. Enhanced Tools Accessibility: The Chat settings popup, previously located next to the "New Chat" button, has been replaced. We've introduced a "Tools" link situated within the chat box. This popup provides direct access to the various resources available to the chatbot.
2. Dynamic Resource Display and Management: Upon accessing the "Tools" section, users will now be presented with a list of available tools, including but not limited to Wikipedia and MedResearch, with future additions such as NLPTools and Text2SQL anticipated. This feature allows users to easily toggle these resources on or off, directly influencing the tools that the Language Learning Model (LLM) leverages to respond to queries.
3. Customizable Knowledge Base Interaction: When the MedResearch tool is enabled, users will be shown a list of accessible KBs, similar to the existing functionality. Importantly, users now have the capability to individually activate or deactivate these KBs. This flexibility ensures that the queries are matched against the most relevant and preferred knowledge bases, enhancing the accuracy and relevance of the chatbot's responses. 
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
- Notification Replaces References: The usual "References" section will be substituted with a distinct notification to users. This alert aims to inform users that the response has been generated based on information available up to a certain date, highlighting that it may not include the latest findings or updates.
- Content of the Notification: The notification will convey the following message: “Please note that this response was generated from John's memory and may not reflect the most recent developments. For the most current information, consider verifying details from up-to-date sources.” This message is designed to prompt users to seek out the most current data for their inquiries, ensuring they have access to the most accurate and relevant information.

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
