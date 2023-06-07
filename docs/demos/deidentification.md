---
layout: demopagenew
title: De-Identification - Clinical NLP Demos & Notebooks
seotitle: 'Clinical NLP: De-Identification - John Snow Labs'
subtitle: Run 300+ live demos and notebooks
full_width: true
permalink: /deidentification
key: demo
nav_key: demo
article_header:
  type: demo
license: false
mode: immersivebg
show_edit_on_github: false
show_date: false
data:
  sections:  
    - secheader: yes
      secheader:
        - subtitle: De-Identification - Live Demos & Notebooks
          activemenu: deidentification
      source: yes
      source: 
        - title: Detect PHI Entities from Deidentification
          id: detect_demographic_information
          image: 
              src: /assets/images/Detect_demographic_information.svg
          excerpt: Automatically identify demographic information such as <b>Date, Doctor, Hospital, ID number, Medical record, Patient, Age, Profession, Organization, State, City, Country, Street, Username, Zip code, Phone number</b> in clinical documents using three of our pretrained Spark NLP models.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/NER_DEMOGRAPHICS/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_DEMOGRAPHICS.ipynb        
        - title: Deidentify Clinical Notes in Different Languages
          id: deidentify_clinical_notes_different_languages
          image: 
              src: /assets/images/Deidentify_free_text_documents.svg
          excerpt: This demo shows how to deidentify protected health information in English, Spanish, French, Italian, Portuguese, Romanian, and German texts.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/DEID_PHI_TEXT_MULTI/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/DEID_PHI_TEXT_MULTI.ipynb   
        - title: Detect PHI Entities from Deidentification (Arabic)
          id: detect_phi_entities_deidentification_arabic
          image: 
              src: /assets/images/Detect_PHI_for_Deidentification.svg
          excerpt: Detect protected health information in Arabic clinical documents using Spark NLP models, identifying up to 17 entities.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/NER_DEMOGRAPHICS_AR/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/04.1.Clinical_Multi_Language_Deidentification.ipynb
        - title: Consistency on Deidentification
          id: consistency_deidentification
          image: 
              src: /assets/images/Consistency_on_Deidentification.svg
          excerpt: Our De-Identification process shown in this demo ensures data clarity, usability and consistency while prioritizing privacy and security.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/DEIDENTIFICATION_CONSISTENCY/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.Clinical_DeIdentification.ipynb
        - title: Deidentify structured data
          id: deidentify_structured_data
          image: 
              src: /assets/images/Deidentify_structured_data.svg
          excerpt: Deidentify PHI information from structured datasets using out of the box Spark NLP functionality that enforces GDPR and HIPPA compliance, while maintaining linkage of clinical data across files.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/DEID_EHR_DATA
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/DEID_EHR_DATA.ipynb   
        - title: Deidentify DICOM documents
          id: deidentify_dicom_documents
          image: 
              src: /assets/images/Deidentify_DICOM_documents.svg
          excerpt: Deidentify DICOM documents by masking PHI information on the image and by either masking or obfuscating PHI from the metadata.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/DEID_DICOM_IMAGE
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/ocr/DEID_DICOM_IMAGE.ipynb
        - title: De-identify PDF documents - HIPAA Compliance
          id: hipaa_compliance
          image: 
              src: /assets/images/Deidentify_PDF_documents.svg
          excerpt: De-identify PDF documents using HIPAA guidelines by masking PHI information using out of the box Spark NLP models.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/DEID_PDF_HIPAA
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/ocr/DEID_PDF.ipynb
        - title: De-identify PDF documents - GDPR Compliance
          id: gdpr_compliance
          image: 
              src: /assets/images/Deidentify_PDF_documents.svg
          excerpt: De-identify PDF documents using GDPR guidelines by anonymizing PHI information using out of the box Spark NLP models.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/DEID_PDF_GDPR
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/ocr/DEID_PDF.ipynb        
        - title: Deidentify free text documents
          id: deidentify_free_text_documents
          hide: yes
          image: 
              src: /assets/images/Deidentify_free_text_documents.svg
          excerpt: Deidentify free text documents by either masking or obfuscating PHI information using out of the box Spark NLP models that enforce GDPR and HIPPA compliance.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/DEID_PHI_TEXT/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/DEID_PHI_TEXT.ipynb
---