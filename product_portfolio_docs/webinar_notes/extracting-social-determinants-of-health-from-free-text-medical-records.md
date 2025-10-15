# Extracting Social Determinants of Health from Free-Text Medical Records
Extracting Social Determinants of Health from Free-Text Medical Records

<https://www.johnsnowlabs.com/watch-extracting-social-determinants-of-health-from-free-text-medical-records/>

<https://youtu.be/JX9oFXJo4M4>

<img src="/media/image.jpg" title="Video titled: [WEBINAR] Extracting Social Determinants of Health from Free-Text Medical Records" style="width:6.3125in;height:3.65625in" />

The webinar transcript provides a detailed overview of how John Snow Labs utilizes Natural Language Processing (NLP) models to extract Social Determinants of Health (SDOH) from free-text medical records.

### **I. Importance and Definition of Social Determinants of Health (SDOH)**

The presentation begins by stressing the importance of SDOH, noting that despite medical advances, **US life expectancy is decreasing**, partly due to the decline in SDOH.

- **Definition:** The CDC, drawing on the World Health Organization, defines SDOH as the **conditions in the places where people live, learn, work, and play** that affect a wide range of health, quality of life risks, and outcomes.

- **Nature:** SDOH are generally **non-medical factors** that profoundly influence health outcomes, such as housing, employment, substance use, personal safety, literacy, and access to healthy food.

- **Data Availability:** Crucially, these SDOH factors are rarely available in structured health data (like ICD-10 codes) but are primarily recorded in **unstructured narrative clinical notes** (free-text nodes).

### **II. The Role of NLP in SDOH Extraction**

NLP is essential because it brings natural language understanding to software, allowing for more human-like communication and unlocking insights from massive amounts of text data.

- **Benefits:** NLP makes it easier to correlate social determinants to patient health and holds the potential to widely improve prevention and treatment.

- **John Snow Labs' (JSL) Offerings:** JSL has a large NLP library for the healthcare and life science industries, including over 2,000 healthcare-related models. JSL provides models designed to extract SDOH information from unstructured data, identify at-risk populations, and address health disparities.

- **Model Types:** JSL uses four primary types of models for this work: Named Entity Recognition (NER) models, Text Classification models, an Assertion model, and pre-trained pipelines.

### **III. Named Entity Recognition (NER) Models**

NER models are NLP tools used to **identify and extract named entities** (specific concepts or proper nouns) from text. They extract words or "chunks" and label them according to predefined entity types (e.g., labeling "marijuana" as substance use or "unemployed" as employment). JSL trains these deep learning models on annotated data sets manually labeled by subject matter experts, such as medical doctors.

JSL currently offers eight NER models focused on SDOH:

1.  **SDOH NER (The Workhorse Model):** This foundational model detects and labels **39 different entities**, including education, housing, age, disability, and eating disorder. It has a micro average F1 score of 94%, which is considered highly satisfactory.

2.  **Demographic entities:** This model extracts seven entities related to demographics.

3.  **Community condition:** Extracts entities like **transportation, housing, food insecurity** (e.g., healthy food), and environmental condition (e.g., "unsafe neighborhood").

4.  **Social environment:** Extracts entities related to social support, **violence or abuse** (physical or emotional abuse), legal issues (e.g., person being in prison), and childhood events.

5.  **Substance use:** This crucial model detects entities like alcohol and smoking, further refining them into specific categories: **substance use, quantity** (e.g., "5 to 6"), **frequency** (e.g., "daily"), and **duration** (e.g., "Last 5 Years").

6.  **Access to healthcare:** Extracts three entities: **access to care, insurance status** (e.g., "uninsured" or "Medicare"), and **healthcare institution** (e.g., clinic or hospital).

7.  **Health behaviors and problems:** Extracts 12 entities, including diet, exercise, obesity, hypertension, and mental health issues like anxiety or depression.

8.  **Income and social status:** Extracts entities such as **education, employment** (e.g., "plumber"), **financial status** (e.g., "low income"), **marital status** (e.g., "divorced"), and population group.

The results from NER models can be viewed using a visualizer or saved as CSV, Excel, or JSON files for future studies.

### **IV. Text Classification Models**

Text classification models assign predefined categories or labels to an entire text based on its content. JSL has seven text classification models related to SDOH, including three focused on insurance.

1.  **Housing insecurity:** Classifies if the patient has "housing insecurity" (unstable/inadequate housing) or "no housing insecurity or not mentioned".

2.  **Mental health:** Classifies text as indicating a "mental disorder" (e.g., citing symptoms like schizophrenia, delusion, or disorganized speech) or "no or not mentioned".

3.  **Under treatment:** Determines if the patient is "under treatment" (actively receiving care) or "not under treatment or not mentioned" (e.g., if the patient chose not to pursue treatment).

4.  **Insurance Status:** Classifies if the person is **"insured," "uninsured"** (e.g., patient has no medical insurance), or **"unknown"** (not mentioned in the text).

5.  **Insurance Coverage:** Assesses the level of coverage as **"good"** (covers all/most needs) or **"poor"** (does not cover all medications/doctor visits, which negatively affects treatment).

6.  **Type of Insurance:** Identifies the type of coverage: **employer, Medicaid, Medicare, military, private, or other/unknown**.

7.  **Transportation insecurity:** Classifies if the patient has **"transportation insecurity"** (lack of access to public transport, car, or ability to drive, leading to problems accessing healthcare/food/employment) or "no transportation insecurity or unknown".

### **V. Assertion Models and Pre-Trained Pipelines**

**Assertion Models** Assertion models are crucial techniques used in conjunction with NER models to detect the **assertion status** of an extracted entity. They determine if the entity extracted by NER is **absent, present, someone else, past, hypothetical, or possible**. This is vital because using only the NER model might extract entities that are explicitly stated as negative or lacking (e.g., "lack of transportation" or "lacking health insurance").

**Pre-Trained Pipelines** For ease of use, JSL offers pre-trained pipelines that combine multiple NLP stages (such as document assembler, tokenizer, embeddings, and NER model) into a single, **"plug and play"** solution. While custom pipelines offer flexibility for defining parameters like Blacklists, Whitelists, and confidence thresholds, pre-trained pipelines like ner_profiling_sdoh allow users to obtain results with a single line of code, albeit with limited capability to fine-tune the components.

### **VI. Future Work**

John Snow Labs is committed to the constant improvement of these models. Future work includes **extending the data set, fine-tuning the models, working to refrain from bias**, and potentially adding a few new entities.