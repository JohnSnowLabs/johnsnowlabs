---
layout: docs
header: true
seotitle: Medical Chatbot | John Snow Labs
title: Release Notes
permalink: /docs/en/chatbot/releases/release_notes
key: docs-healthcare-gpt
modify_date: "2024-07-30"
show_nav: true
sidebar:
    nav: healthcare-gpt
---

<div class="h3-box" markdown="1">

## 10-24-2024 Literature Review Enhancements

We are happy to release an enhanced version of the Literature Review feature, aimed at improving user experience, search accuracy, and data extraction. This update includes a redesign of the Literature Review wizard with new, intuitive functionalities. Our goal is to provide users with a more comprehensive and flexible tool for better control over the search, analysis, and extraction steps. The broader search capabilities and refined data extraction options are intended to make research more effective.

</div><div class="h3-box" markdown="1">

### Key Improvements

**1. Advanced Search with Logical Operators**

This release adds the NOT operator to the existing AND and OR search functions, allowing for more nuanced searches by excluding specific combinations of keywords. This improvement empowers users to refine their queries and achieve more precise results, giving them total control over how their searches are structured. Switching between the AND and NOT operators is effortless, giving users total control over how their search queries are structured. For example, if a user wants to avoid certain topics, they can easily toggle the NOT operator to exclude irrelevant results.


**2. Visualization of Query String**

A redesigned user interface visually displays search keywords and their logical relationships, helping users understand how each keyword and operator (OR/AND/NOT) affects search outcomes. This real-time visual representation makes it easier for users to adjust search terms and immediately see their impact, enhancing the clarity and efficiency of the search process.

<img src= "/assets/images/chatbot/LiteratureReviewQuery.png" alt="Literature Review - Visualization of Query String" style="border: 2px solid grey; width=60%">

**3. Targeted Search by Metadata Fields**

Users can now search within specific metadata fields, including Study Title, Text Content, and Journal Name. This targeted approach makes it easier to focus on particular aspects of studies, ensuring search results align more closely with user research objectives, and reducing the time needed to filter irrelevant content.

**4. Unified Search Filters for Efficiency**

All search filters, such as Publication Date, Impact Factor, and Article Type, are now consolidated into Step 1 of the review process. This unified approach enables users to configure all search parameters upfront, providing a clear overview of their search results early in the process and enhancing workflow efficiency.

<img src= "/assets/images/chatbot/LiteratureReviewFilters.png" alt="Literature Review - Filter the Target Studies" style="border: 2px solid grey; width=60%">

**5. Enhanced Data Point Extraction**

The Data Points definition UI (step 2) was enhanced to allow users to define more precisely the target information. Users can provide a clear **Name** (maximum 30 characters) and a **Prompt** definition  (maximum 1500 characters) for each data point, ensuring that the extracted data aligns perfectly with the research objectives. Users can also include examples in the prompt description. The new format is fully compatible with existing literature reviews, which will automatically be updated to reflect these enhancements.

<img src= "/assets/images/chatbot/LiteratureReviewDataPoints.png" alt="Literature Review - Definition of Data Points" style="border: 2px solid grey; width=60%">
  
**6. Enhanced Definition of Inclusion and Exclusion Criteria** 

The Inclusion and Exclusion Criteria section (step 3) has also been refined to allow users to provide a concise **Name** (maximum 30 characters) and detailed **Prompt** definition (maximum 1500 characters) for each criterion, offering greater precision in study selection. The updated format is applicable to both new and existing reviews, automatically updating previous reviews to align with the new system.

<img src= "/assets/images/chatbot/LiteratureReviewDataPoints.png" alt="Literature Review - Definition of Inclusion and Exclusion Criteria" style="border: 2px solid grey; width=60%">


**7. Time-Based Metrics for Literature Review**

To provide greater transparency, we have introduced time-based metrics throughout the Literature Review process, including Queue Time, Progress Time, and Completion Stats. These metrics offer insights into each stage of the review process, enabling users to better manage their workflow and set realistic expectations.

These metrics provide users with key insights, including:
- Queue Time: The time the review spends in queue (e.g., "In queue for less than a minute").
- Progress Time: The duration the review has been running (e.g., "Running for 3 minutes").
- Completion Stats: Once the review is complete, users can view the Completion Date, Start Time, End Time, and Total Time Taken for the entire process.

<img src= "/assets/images/chatbot/LiteratureReviewTimeMetrics.png" alt="Literature Review - Time-Based Metrics" style="border: 2px solid grey; width=100%">

</div><div class="h3-box" markdown="1">

### User Benefits

These enhancements work together to offer the following benefits to our users:

**1. Greater Control and Precision in Search Results:** 
With the introduction of the NOT operator and the enhanced ability to search by specific metadata fields (e.g., title, content, journal name), users can now create more targeted search queries. This enables them to exclude irrelevant results and focus on the most pertinent studies, ensuring a higher level of precision and relevance in their literature reviews. The ability to switch between AND and NOT operators provides flexible control over search behavior, allowing users to tailor their queries to meet specific research needs.

**2. Streamlined and Efficient Workflow:**
By unifying all search filters, including Publication Date, Impact Factor, and Article Type, into the initial step of the review process, users can now set up their entire search framework from the outset. This centralized approach eliminates the need for users to navigate back and forth between different steps, significantly enhancing workflow efficiency. Real-time updates to search parameters make it easier for users to adjust their queries quickly and effectively, resulting in a smoother, faster review process.

**2. Improved Data Extraction, Study Selection, and Transparency**
The revamped Data Points and Inclusion/Exclusion Criteria features offer clearer definitions and a more structured approach to data extraction. Users can now be specific about what data points they want to extract and how they define their inclusion/exclusion criteria. This precision ensures that the extracted data aligns perfectly with the user’s research objectives, leading to more accurate and insightful results. Additionally, the inclusion of time-based performance metrics provides users with complete transparency, allowing them to monitor the progress and time efficiency of their literature reviews.


These upgrades reflect our ongoing commitment to enhancing research tools for a more efficient, precise, and user-friendly experience. We encourage users to explore these new features and see the improvements firsthand.

</div><div class="h3-box" markdown="1">

## 09-24-2024 Introducing Literature Review

We are happy to announce a new feature offered by the Medical Chatbot: Literature Review, specifically tailored to streamline the complex process of medical literature research and review. This tool enables researchers, healthcare professionals or clinicians to efficiently sift through vast amounts of published research to support in-depth meta-analyses, clinical decision-making, or evidence-based practices.

</div><div class="h3-box" markdown="1">

### Overview

The literature review is a critical and multifaceted process that involves **searching**, **reading**, **analyzing**, and **synthesizing** scholarly materials on a given topic to identify existing knowledge in a particular research area. This process helps map out what is already known and allows for the critical evaluation of prior studies to uncover gaps, inconsistencies, or emerging trends. Navigating through all available literature on a given subject requires specialized skills and highly effective search pathways to achieve both sensitivity and specificity in the results. Even for an experienced team of researchers, the task can become overwhelming, time-consuming, and prone to missed insights or errors.

To address these challenges and improve the efficiency and accuracy of the literature review process, the Medical Chatbot introduces the "Literature Review". This advanced AI agent enables users to intelligently search millions of research papers and articles from prestigious databases such as PubMed, BioRxiv, and MedRxiv (as well as custom knowledge bases), and quickly identify relevant studies. Then, with just the push of a button, the tool allows for automated data extraction, making it easy to gather key data points and insights. Users can also define specific inclusion and exclusion criteria to filter results, honing in on the most pertinent studies for their research. This dramatically reduces the manual effort required for conducting comprehensive reviews, allowing for faster, more informed, and more accurate decision-making in clinical and research environments.

</div><div class="h3-box" markdown="1">

### Key Features

**1. Intelligent Search:**
Users can effortlessly search through vast amounts of published research papers and articles from trusted databases such as PubMed, BioRxiv, MedRxiv using simple keywords. The system helps streamline clinical decision-making by rapidly identifying relevant literature.

<iframe width="800" height="450" src="https://www.youtube.com/embed/7MqUPMtuUcI?si=nUiH4cMjh1nFoqgz&hd=1" title="Literature Review - Step 1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**2. Smart Data Extraction:**
Users can define the data points they are interested in, using plain English, and the Medical Chatbot will automatically understand and intelligently scan the filtered literature, identifying and extracting those across all target studies. This automation drastically reduces the manual effort typically required for data extraction, providing users with quick access to key findings.


<iframe width="800" height="450" src="https://www.youtube.com/embed/m2YldVGOFXU?si=2sm4LJV60D1fNdUa&hd=1" title="Literature Review - Step 2" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**3. Customizable Inclusion and Exclusion Criteria:**
Users can define specific inclusion and exclusion criteria based on their study requirements, making their review highly accurate and targeted. Whether focusing on the intervention, measured outcomes, study population, methodology, or other parameters, these custom criteria ensure that only the most relevant studies are included in the review. The medical chatbot analyzes the literature to verify compliance with these criteria, notifying users of any non-compliant studies and providing a highly accurate literature review.


<iframe width="800" height="450" src="https://www.youtube.com/embed/vG7pGsNqrkA?si=vObgXAE971_y-9Ob&hd=1" title="Literature Review - Step 3" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**4. Data Filtering for Precise Targeting:**
Results can be further refined by filtering literature based on the date range of publication, the impact factor of the study, and the type of study (e.g., clinical trials, reviews, case studies). This allows users to narrow their search and focus on the most relevant studies for their review. Users can specify the exact characteristics they want the included literature to possess for a more accurate and focused review. This ensures that the results align perfectly with the research objectives.


<iframe width="800" height="450" src="https://www.youtube.com/embed/y4NSrKdnWOU?si=HaDcqR-lIZrRSedP&hd=1" title="Literature Review - Step 4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**5. Real-Time Feedback:**
As users enter their search criteria, the chatbot filters and displays relevant literature in real-time. This immediate feedback allows users to open and review papers right away, without having to wait for the entire search process to complete. By streamlining the search process, this feature facilitates faster access to relevant information, saving users time and effort.

**6. Comprehensive Result View:**
The tool provides an intelligent tabular view of all the relevant information from each study, including the title, author, journal, and direct links to the paper. It also displays extracted data points based on user criteria and indicates whether each study complies with the defined inclusion and exclusion criteria. This organized and visual representation saves users significant time and effort in their literature review process.
For a better understanding of the data points, users can hover over individual data cells in the results table to reveal tooltips containing evidence or explanations of the extracted data. This feature ensures that users have easy access to deeper insights without cluttering the main results view, facilitating a better understanding of the extracted information.


<iframe width="800" height="450" src="https://www.youtube.com/embed/cmf13SkFNoQ?si=PzHmgce86IPDxuG9&hd=1" title="Literature Review - Explore Results" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Results are color-coded based on the application of inclusion and exclusion criteria as follows:
- Studies highlighted in green have successfully met all inclusion and exclusion criteria.
- Studies highlighted in red were excluded due to failing at least one of the specified exclusion criteria.
- Studies highlighted in white lacked sufficient information for the chatbot to determine their inclusion or exclusion, as none of the criteria could be validated.

**7. Downloadable CSV Reports:**
Once the review is complete, users can download all the extracted information in a well-organized CSV file. This functionality enables seamless management and further processing of the data, making it easier for users to analyze the information in-depth or share it with team members for collaboration. By exporting study details and compliance with inclusion/exclusion criteria, users can efficiently manage their literature review data and integrate it into broader research workflows or collaborative projects.

**8. Cloning Literature Reviews for Efficiency:**
Once a literature review is completed, users can easily clone the existing review, replicating all the parameters with a single click. This includes search keywords, data points, inclusion and exclusion criteria, and the search filter settings. The cloned review retains all of the original settings, but users can also modify these parameters as needed in the new review. This allows the quick creation of multiple variations of the same literature review, optimizing the process for different research angles or clinical considerations. By eliminating the need to re-enter identical parameters repeatedly, the “Clone” button saves significant time and effort, allowing users to replicate previous work and focus on refining and analyzing new sets of results efficiently.

These features work together to provide a powerful, efficient, and user-friendly experience, enabling researchers to complete literature reviews on thousands of articles in minutes instead of weeks or months of study and manual text synthesis.

</div><div class="h3-box" markdown="1">

### User Benefits

In the medical domain, this tool has been designed to make the following impacts:

**1. Time and Effort Savings:**
The "Literature Review" feature is designed to significantly reduce the manual labor involved in conducting literature reviews. With automated data extraction, customizable filtering, real-time updates, and organized result displays, users can complete comprehensive reviews in a fraction of the time it would take manually. This time-saving aspect is one of the most critical benefits for researchers and clinicians who need to process large amounts of literature quickly.

**2. Specificity for Meta-Analysis:**
For users conducting meta-analyses, this tool allows for a high degree of specificity in selecting literature that matches the desired characteristics. By being able to filter studies based on exact criteria, users can ensure their meta-analysis is robust, accurate, and fully aligned with their research objectives. This improves the quality and precision of the meta-analysis, making the tool invaluable for detailed, data-driven research.

**3. Automated and Intelligent Data Point Extraction:**
Users no longer need to manually comb through articles to extract relevant data points. The Medical chatbot understands simple keywords provided by users and autonomously extracts the required information from filtered research papers. This automated extraction drastically reduces the manual workload associated with literature reviews, ensuring critical data points are collected quickly and accurately while minimizing the risk of human error.

**4. Improved Clinical Decision-Making:**
By providing users with timely and accurate access to relevant studies, the feature directly supports clinical decision-making. With quick and precise data extraction, clinicians and researchers are better equipped to make informed decisions based on the latest and most relevant research. This ensures that decisions are not only quicker but are also grounded in high-quality, peer-reviewed literature, enhancing the overall reliability of the outcomes.

</div><div class="h3-box" markdown="1">

## 08-08-2024 New NLP Tools and Response Styles

We are happy to announce a new release of the Medical Chatbot that includes new NLP Tools, support for response style and an improved chat experience. 

Four healthcare specialized NLP tools are now available: Radiological Entities and Relations Extraction, Social Determinants of Health Extraction, Adverse Drug Events Extraction, and Voice of the Patient Extraction. These are designed to meet the unique challenges of the medical field, ensuring accurate and efficient data extraction and analysis.

Additionally, customizable Response Styles are now also available for tailored interactions. Improvements in chat functionality, including advanced memory management and automatic tool selection, further ensure that the chatbot provides precise, context-aware responses. 

These new features empower healthcare professionals with cutting-edge solutions for more effective decision-making and patient care.


</div><div class="h3-box" markdown="1">
    
### Introducing New NLP Tools

The integration of Natural Language Processing (NLP) tools into the Medical Chatbot has significantly enhanced its capabilities in processing medical texts, specifically in areas such as PHI/PII masking or obfuscation, medical named entity recognition (NER), and relationship extraction. To further support precise and efficient medical data analysis, four new NLP tools have been made available, tailored to meet the specific requirements of the medical field:

- Radiological Entities and Relations Extraction
- Social Determinants of Health Extraction
- Adverse Drug Events Extraction
- Voice of the Patient Extraction

These tools are tailored to meet the unique challenges of the medical field, ensuring accurate and efficient data extraction and analysis, further empowering users with cutting-edge solutions.

![New_NLP_Tools](https://github.com/user-attachments/assets/a355d90a-e4bb-4ea0-9e1d-1018e5ec2a36)

#### Tools Overview
All four of the new tools are seamlessly integrated and available via the @ Selector. By simply typing '@' at the beginning of the query box, users can access the @ Selector menu, which displays all available tools (including the 4 new NLP tools).

**1.Extract Radiological Entities and Relations**
Designed to extract radiology-related entities, assign assertion statuses to these entities, and establish relationships between them within clinical documents. This tool specializes in identifying entities such as tests, imaging techniques, and test findings within radiology reports, while also accurately determining their assertion statuses and relations.

**2.Extract Social Determinants of Health**
Engineered to extract all clinical and medical entities considered as Social Determinants of Health (SDoH) from textual data, assign assertion statuses to the identified entities, and detect relationships between entities. Specifically, it identifies socio-environmental health determinants such as access to care, diet, employment, and housing from health records, providing comprehensive insights into factors affecting patient health outcomes.

**3.Extract Adverse Drug Events:**
Designed to identify and extract adverse drug events and related clinical entities from medical texts. This tool can help users identify adverse reactions to drugs (ADE) from various drug reviews, tweets, and medical texts while also providing assertion statuses and relationship analysis.

**4. Extract Voice Of The Patient:**
Designed to detect healthcare-related entities from patient-generated content, assign assertion statuses, and establish relationships between these entities. This tool proficiently identifies clinical and behavioral entities from various sources, including social media posts, blogs, forums, and direct patient communications.

</div><div class="h3-box" markdown="1">

### Customizable Response Styles
    
The Medical Chatbot now offers support for Response Styles via an enhanced, intuitive interface that allows users to easily customize their conversation settings. This feature enables dynamic response style selection, improving the personalization of interactions and empowering users to tailor responses to their specific needs. Users can tailor the generated text to their needs and have greater control over the creative process without the need to rephrase their prompts entirely.

![image](https://github.com/user-attachments/assets/f6807f43-6787-42ac-9e88-8d1a335f3807)


#### Key Features:

- **Streamlined Access:** Each response now includes a Response Style settings button, accessible through the conversation settings icon in the contextual menu.

- **Dynamic Customization:** By default, a standard response style is applied when starting a new conversation. However, you can now effortlessly switch to a different style after the initial response. Simply click the settings button to select your preferred style, and the chatbot will regenerate the response accordingly.

- **Understand Your Preferences:** Once you choose a response style, it will remain active for all subsequent interactions within the current conversation and even future conversations. You can easily modify this setting at any time at any point of the conversation.

- **Custom Response Styles:** Want a unique touch? Create your own Custom Response Style by providing a simple prompt describing your preferred response tone or format. The Medical Chatbot will adapt to your specifications.

Enhance your conversational experience with these new features and enjoy a more tailored and responsive interaction.

</div><div class="h3-box" markdown="1">

### Chat Improvements


We are committed to continuously enhancing the chat and conversational capabilities of the Medical Chatbot. This release  include advanced memory management for conversational history, enabling the Medical Chatbot to handle interactions more effectively and maintain context. Additionally, enhancements in automatic tool selection ensure that the most appropriate tool is chosen for the user's complex queries, providing the most accurate and relevant responses. The Medical Chatbot is now able to understanding the specialties of each tool and applying them appropriately based on the context of the user's query.

</div><div class="h3-box" markdown="1">

## 07-30-2024 - Improved DocQA, New Web Search and Enhanced NLP Tools 

We are happy to announce a new release of the Medical Chatbot, focused on enhancing its capabilities and usability in the medical domain. 

**Highlights**:

- Improved Document Q&A (DocQA) capabilities and accuracy. This feature was refined through ongoing testing, feedback, and technical adjustments to ensure it delivers highly accurate and focused responses based on the targeted documents.
- A new tool for "Web Search", designed to harness the power of advanced search algorithms and LLMs to provide you with the most accurate and relevant information from online sources. 
- Enhanced NLP tools. New capabilities were added to existing tools such as support for assertion labels and relation extraction. 
- Improved UI and easier interactions with available tools and resources. 
 These enhancements are designed to ensure the Medical Chatbot remains highly effective and intuitive, meeting the evolving needs of our users.

</div><div class="h3-box" markdown="1">
   
## DocQA Enhancements 

### Tuned for more accurate responses with precise citations
The DocQA Feature is continuously refined through ongoing testing, feedback, and technical adjustments to ensure it delivers highly accurate and focused responses based on the targeted documents. In this release, the DocQA was enhanced to better handle medical information, providing improved citations and a more comprehensive understanding of the target documents. Additionally, the highlighting of target sections in document previews was refined to offer clearer insights into how responses are formulated based on the available information. These enhancements are part of our commitment to delivering powerful, user-friendly tools that support and elevate your medical information management and decision-making processes.

![Tuned_docQA](https://github.com/user-attachments/assets/e05018fd-2a01-4721-9412-509f91238a18)

</div><div class="h3-box" markdown="1">

### Document upload - file processing status 

The DocQA Session has an improved UI for file upload and processing designed to make the document interactions and processing status more intuitive. During file upload, users are able to remove the selected files using the cross button provided for each file. Furthermore, as the processing of a file begins, the UI indicates the file's status as follows:
1. **Processing:** The current file is being processed, indicated by a loading icon.

![File_processing](https://github.com/user-attachments/assets/152cc921-2c32-4118-8e55-b29c8bc2883a)

2. **Processing Complete:** The file has been successfully processed and is now part of the knowledge base, shown by a green tick icon.

![DocQA Enhancements](https://github.com/user-attachments/assets/0d93f381-7516-4c54-89c1-8ebd19e3495b)

3. **Processing Failed:** There was an issue with file processing, indicated by a red cross icon.

![DocQA Enhancements](https://github.com/user-attachments/assets/d9aab12f-251f-49ee-871a-4ed158f17cd0)

After all files are processed, users can set those as target documents for the current session and start asking questions related to their content.

</div><div class="h3-box" markdown="1">

### Quick access to uploaded documents
In the DocQA session, you can now easily view the content of uploaded documents (both txt and Pdf) by clicking on their name in the "Target Document" section at the top of your chatbot screen. This action opens the selected document in a new tab. 

![Quick_Access_Docs](https://github.com/user-attachments/assets/1db16ea3-dbd5-4e79-9534-0b0c4a26169b)

</div><div class="h3-box" markdown="1">

### More precise references
Responses generated in the DocQA session include citations pointing to specific sections of the document used as references. These sections can be previewed in the Document Preview UI. Now, to enhance usability, reference numbers have been added to each preview, allowing users to easily track and identify the relevant references while reviewing the content.

![DocQA Enhancements](https://github.com/user-attachments/assets/f0bc44fb-8972-4cbf-a1ea-5425390dbcb9)

</div><div class="h3-box" markdown="1">

### Quick load for reference previews
To improve the efficiency of document previews, the chatbot offers a better pre-loading process. This enhancement reduces the time required for document previews for each reference/citation while ensuring accurate section highlighting for both PDF and TXT files.

</div><div class="h3-box" markdown="1">

## Introducing the "Web Search" Tool

### Overview

We are excited to introduce the Web Search tool, an enhancement of the already available Wikipedia search tool. While the Wikipedia search tool effectively provided information from a vast database of general topics, the new Web Search tool extends its capabilities to the entire web, ensuring you receive the most comprehensive and relevant information available.
   
<iframe width="800" height="450" src="https://www.youtube.com/embed/X6s33xuxJAw?si=2dwXuyOQIWNP7OBO&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

</div><div class="h3-box" markdown="1">

### Key Features
1. **Expanded Search Capabilities:** Unlike the Wikipedia search tool, which was limited to Wikipedia's database, the Web Search tool queries the entire web. This ensures access to a broader range of information and resources.
2. **Intelligent Query Handling:** The Web Search tool leverages advanced AI algorithms to understand your queries better and retrieve the most accurate and relevant information.
3. **Smart Tool Selection:** The Medical Chatbot is designed to recognize when to utilize the Web Search tool based on the nature of your queries. This means you get the most appropriate and timely responses without needing to specify the tool explicitly.
4. **Up-to-Date Answers:** By searching the entire web, the tool can provide more detailed and diverse answers, drawing from various sources, filtered and structured by the Chatbot's intelligence to give you a well-rounded accurate perspective.

**Tool Usage and Manual Tool Selection (@ Selector)**
The Web Search Tool is now available in the Tool Selection menu and can be enabled or disabled as needed. Enabling this tool allows the Medical Chabot to intelligently utilize the Web Search Tool based on your query requirements. Additionally, enabling the tool will make it available in the Manual Tool selection menu, allowing users to manually invoke it by typing "@web_search" at the beginning of a query to receive responses specifically using the Web Search tool. The @ selector menu will automatically auto-fill the keyword for the Web Search while typing and the user can easily use the Web Search tool manually for the response generation.

</div><div class="h3-box" markdown="1">

### User Benefits
In the medical domain, this tool can be useful when looking at:
-  patient feedback on the effectiveness of new medications, side effects, and personal experiences with healthcare providers;
-  notifications about recalls of faulty medical devices or alerts on newly discovered device malfunctions;
-  outbreaks of infectious diseases like West Nile, Ebola, Zika, Monkeypox, etc. in specific areas of the world;
-  recent updates on vaccination schedules, new health screening guidelines, and preventive care recommendations;
-  recent changes in healthcare laws, insurance coverage policies, and public health initiatives.
-  newly developed treatments or medical technologies that are in the early stages of deployment but not yet widely studied or published;
-  upcoming health fairs, free screening events, and vaccination drives, etc.

</div><div class="h3-box" markdown="1">

## NLP Tools and Chat Improvements

### Support for entities, assertion statuses, and relations in the NLP Tools

With the integration of NLP tools, the Medical Chatbot supported Named Entity Recognition specialized for the Clinical, Oncology, and Posology domains. In this release, the NLP tools were enhanced to support assertion labels as well as relation discovery between entities. 
The generated responses visually highlight the detected entities and assertion statuses. Users also have the option to download the extraction results in structured format (CSV), to access detailed information on the detected relations between entities as well as information on the confidence of each annotation.

</div><div class="h3-box" markdown="1">

### Updated Tool Names and Descriptions

The tools have been renamed and their descriptions were updated to provide users with a clearer understanding of each tool and its functionalities. These updates are reflected throughout the application, including in key areas such as the Tool section menu and the @ Selector menu. 

![DocQA Enhancements](https://github.com/user-attachments/assets/e74e33d2-1262-4fc3-9bf2-32f46f3dca97)

</div><div class="h3-box" markdown="1">

### Copy response with references 

All responses have a copy button for ease of use. The copy option now also included the related references, including relevant metadata and hyperlinks to the original articles. This information is now appended at the end of the pasted content. This applies to responses generated using all current knowledge bases, including PubMed, bioRxiv, medRxiv, Web Search results, and even DocQ&A responses.

![Copy_Response_citations](https://github.com/user-attachments/assets/38612434-152d-4ae2-8b6c-3576d260fa0a)

</div><div class="h3-box" markdown="1">

### New features for Enterprise Admin Users
Several new Enterprise features have also been added to the Medical Chatbot, specifically designed to enhance the experience for Admin users. Firstly, a comprehensive API documentation is now accessible, providing detailed guidance on integrating and leveraging the chatbot's capabilities within your systems. Additionally, Admin users have the option to extended the trial period for their users, allowing them more time to explore and evaluate the full potential of the platform before making a commitment. Furthermore, significant improvements have been made to the User Management UI, including new filters and a more intuitive interface, making it easier for Admin users to manage and organize their teams effectively. These enhancements are tailored to streamline administrative tasks and optimize the overall user experience.

</div><div class="h3-box" markdown="1">
---

## 05-17-2024 - Introducing DocQ&A and NLP Tools

We are excited to announce two significant enhancements to the Medical Chatbot: the DocQ&A (DocQA) feature and the NLP Tools feature. These additions are designed to streamline your interactions and deepen your engagement with medical texts. The DocQA feature enables seamless management and querying of up to 10 text or PDF documents, providing a focused, session-based interaction. NLP Tools feature introduces a suite of specialized tools for the extraction and analysis of medical information, tailored to your needs. Whether you are interested in extracting entities from your medical text, to de-identify or summarize them, NLP Tools get you covered. These enhancements are part of our continuous effort to provide powerful, user-friendly tools that support and enhance your daily medical information handling and decision-making processes.

</div><div class="h3-box" markdown="1">

## Introducing DocQ&A (DocQA) Feature

### Overview
The DocQA feature enhances the Medical Chatbot by allowing users to upload and interact with up to 10 text (.txt) or PDF (.pdf) documents. This feature is designed to provide tailored answers based on the content of the uploaded documents.

<iframe width="800" height="450" src="https://www.youtube.com/embed/BJ4cXJl7ZyY?si=P1GBmRtTBTmPeRJ0&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

</div><div class="h3-box" markdown="1">

### Key Features
1.**Document Upload and Session Initiation**
   - Users can upload one or several documents directly into the chat interface.
   - Upon uploading documents, a DocQA session is automatically initiated.
   - Each user is limited to one active DocQA session at any given time.

![Start_DocQA_Session](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/17f402c1-e3ff-4533-b135-fcf47791444a)

2.**Session Management and Visibility**
   - The active DocQA session appears as "DocQ&A" in the Conversation History.
   - This session is pinned to the top of the list and remains there until the session is closed or the conversation is removed.

![Introducing DocQ&A](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/db5b6fd6-867d-4157-9240-c472e23e5719)

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

</div><div class="h3-box" markdown="1">

### User Benefits

- **Focused Answers:** Provides precise information derived directly from uploaded documents.
- **Efficient Navigation:** Seamlessly switch between general chat and document-specific queries.
- **Resource Management:** Control over the documents within the session ensures relevance and efficiency in information retrieval.
- **Accelerated Learning**: Efficiently reads and analyzes the given documents which helps aid in quick content summarization and analysis for learning.

This feature is part of our ongoing commitment to enhance user interaction and improve the informational value of the Medical Chatbot. We look forward to your feedback and continual engagement with this new functionality.

</div><div class="h3-box" markdown="1">

## Introducing the NLP Tools 

### Overview
The NLP Tools feature is a new addition to the Medical Chatbot, providing specialized capabilities for processing medical texts through Natural Language Processing (NLP). This feature allows users to access five distinct state-of-the-art accuracy tools, each designed for specific tasks related to medical data handling and analysis.

</div><div class="h3-box" markdown="1">

### Key Features
1. **Tools Overview**
   - **Deidentification/Obfuscation of PHI**: Automatically detects and masks or obfuscates protected health information (PHI) from medical text to ensure privacy and compliance with data protection regulations. Users can specify to de-identify or obfuscate the medical text based on their requirements. 
   
   <iframe width="800" height="450" src="https://www.youtube.com/embed/odSyX3uKjwg?si=XZZO8aY3t82Iqslu&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

   - **General Medical Entity Extraction**: Identifies and extracts general medical entities from text, facilitating quick access to relevant medical terms and concepts.

   <iframe width="800" height="450" src="https://www.youtube.com/embed/FjAzlImC0zQ?si=N415bCn2AU2h6i6U&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

   - **Oncological Entity Extraction**: Specialized for recognizing and extracting terms related to oncology, aiding in the analysis of cancer-related medical texts.

   <iframe width="800" height="450" src="https://www.youtube.com/embed/qTbH57SI6R0?si=HO8riHFw-cXYeIvK&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

   - **Posology Entity Extraction**: Focuses on extracting dosage and medication instructions from medical documents, crucial for understanding treatment protocols.

   <iframe width="800" height="450" src="https://www.youtube.com/embed/5M5nLUdTb4I?si=7uCei72nxBSpvwMe&hd=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

2. **Customizable Accessibility**
   - Users can enable or disable NLP tools based on their specific needs or preferences, allowing for a personalized experience and control over the processing features used.
3. **Accessing Tools**
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

4. **Export results in CSV format**
   - All the Entity Extraction results computed using the NLP tools can be exported in CSV format. For each detected entity, the export also contains confidence information, ensuring transparency and reliability in data analysis.

![CSV_Download](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/18526211-0ebc-43bb-beba-2c2439d479b7)

</div><div class="h3-box" markdown="1">

### User Benefits
- **Enhanced Privacy and Compliance**: Safeguards sensitive information by efficiently deidentifying PHI from medical texts.
- **Focused Content Extraction**: Enables precise extraction of medical entities tailored to general, oncological, and posology contexts, enhancing the utility and accuracy of information retrieval.
- **User-Controlled Flexibility**: Offers the flexibility to tailor tool engagement to individual preferences and requirements.
- **Efficient Tool Access**: Simplifies the process of accessing specific NLP tools through intuitive user interface mechanisms.

</div><div class="h3-box" markdown="1">

---

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
   
![Response Style Customization](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/f2e12115-604d-4e17-b51e-68e25c0212d2)

</div><div class="h3-box" markdown="1">

### Dynamic Response Style Selection

Upon initiating a new conversation, the Default response style is applied. However, users now have the flexibility to change the response style after the first response is generated by the chatbot. By clicking on the conversation settings button, users can select a different style, prompting the chatbot to regenerate the response in the new style. This selected style will persist for all subsequent interactions within the current conversation until the conversation concludes or the user opts to change the style again.

![Response Style Customization](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/26996a41-a9f6-455f-8ea2-b238f850b090)

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

![Tools Selection](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/b9b2f9fd-e938-43c6-a050-e2e201f78cb2)

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

![Enhanced Transparency for LLM Memory-Based Responses](https://github.com/JohnSnowLabs/johnsnowlabs/assets/85957146/2ba0c6b5-c7f8-42aa-aa82-1528e9e0fceb)

</div><div class="h3-box" markdown="1">

## Ongoing Enhancements and Bug Fixes

In addition to the new UI features, this update includes a series of bug fixes and improvements aimed at optimizing the internal management of knowledge bases (KBs) and tools. These enhancements are designed to improve the efficiency and effectiveness of the tool, ensuring that users receive the most accurate and relevant responses. While the specifics of these updates are not disclosed at this time, we assure our users that these changes significantly contribute to the robustness and reliability of the Medical Chatbot's operations.

We believe these updates, both in enhancing transparency and usability and in improving the internal workings of the chatbot, will greatly enrich the user experience. We remain committed to continuous improvement and innovation, always prioritizing the needs and satisfaction of our users.

</div><div class="h3-box" markdown="1">
   ---

## 02-21-2024

**Welcome to the Medical Chatbot Documentation and Updates Hub!**

We are excited to announce the launch of the Medical Chatbot Releases Page, a centralized repository for all the latest features, enhancements, and resolutions of known issues within the Medical Chatbot platform. This dedicated space is designed to keep users informed of the most recent developments, enabling seamless testing and facilitating the provision of valuable feedback. Our commitment is to ensure that users have immediate access to the latest information, empowering them to leverage the full capabilities of the Medical Chatbot effectively. Stay updated with us as we continue to improve and expand the functionalities of the Medical Chatbot to meet and exceed your expectations.

</div>