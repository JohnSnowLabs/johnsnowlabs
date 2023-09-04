---
layout: topdemos
title: Spark NLP in Action
pagetitle: John Snow Labs NLP - The Demos and Notebooks Hub
excerpt: Run 300+ live demos and notebooks. Try out demo examples to learn and practice various NLP features offered by Spark NLP.
seotitle: John Snow Labs NLP - Demos and Notebooks
subtitle: Run 300+ live demos and notebooks
full_width: true
permalink: /demos
key: demo
nav_key: demolist
demomenu: true
license: false
show_edit_on_github: false
show_date: false
notebooks:
  - source: yes
    source: 
      - title: Healthcare NLP
        image: 
            src: /assets/images/notebooks/Olha_a_doctor_with_a_stethoscope.png
        actions:
        - text: Learn more
          url: https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/healthcare-nlp
      - title: Spark NLP
        image: 
            src: /assets/images/notebooks/spark_nlp.png
        actions:
        - text: Learn more
          type: normal
          url: https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/open-source-nlp
      - title: Visual NLP
        image: 
            src: /assets/images/notebooks/visual_nlp.png
        actions:
        - text: Learn more
          type: normal
          url: https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/visual-nlp
      - title: Legal NLP
        image: 
            src: /assets/images/notebooks/legal_nlp.png
        actions:
        - text: Learn more
          type: normal
          url: https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/legal-nlp
      - title: Finance NLP
        image: 
            src: /assets/images/notebooks/finance_nlp.png
        actions:
        - text: Learn more
          type: normal
          url: https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/finance-nlp
      - title: NLP on 
        image: 
            src: /assets/images/notebooks/databr.png
        logo_image: 
            src: /assets/images/notebooks/databricks_logo_sm.svg
        actions:
        - text: Learn more
          type: normal
          url: https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/databricks/python/healthcare_tutorials_jsl
data:
  sections:  
    - source: yes
      source: 
        - title: Medical Large Language Models
          id: explore_medical_large_language_models
          image: 
              src: /assets/images/Explore_Medical_Large_Language_Models.svg
          excerpt: Explore the use of Medical Large Language Models for tasks like Text Summarization, Generation, and Question Answering.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/MEDICAL_LLM/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/MEDICAL_LLM.ipynb  
        - title: Detect Entities in Clinical Text
          id: detect_clinical_entities_in_text
          image: 
              src: /assets/images/Detect_risk_factors.svg
          excerpt: Identify 77 entity types including Symptom, Treatments, Test, Oncological, Procedure, Diabetes, Drug, Dosage, Date, Imaging Finding, and more.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb
        - title: Information Extraction in Oncology
          id: explore_oncology_notes_spark_models
          image: 
              src: /assets/images/Detect_Oncological_Concepts.svg
          excerpt: Detect clinical entities and relationships related to cancer staging, grading, histology, tumor characteristics, biomarkers, treatments, and outcome measures.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/ONCOLOGY/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/27.Oncology_Model.ipynb
        - title: De-identify Clinical Notes in Different Languages
          id: deidentify_clinical_notes_different_languages
          image: 
              src: /assets/images/Deidentify_free_text_documents.svg
          excerpt: De-identify and obfuscate protected health information (PHI) in English, Spanish, French, Italian, Portuguese, Romanian, and German texts.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/DEID_PHI_TEXT_MULTI/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/DEID_PHI_TEXT_MULTI.ipynb
        - title: Adverse Drug Event Detection
          id: explore_adverse_drug_events_spark_nlp_models   
          image: 
              src: /assets/images/Explore_Adverse_Drug.svg
          excerpt: Detect adverse reactions from drugs described in the clinical text, online reviews, and social media posts.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/ADE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/16.Adverse_Drug_Event_ADE_NER_and_Classifier.ipynb
        - title: Voice of the Patients
          id: vop           
          image: 
              src: /assets/images/Voice_Of_Patient.svg
          excerpt: Extract and classify healthcare-related terms from documents written by patient such as questions, reviews, messages, and social media posts.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/VOP/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/VOICE_OF_PATIENT.ipynb
        - title: Social Determinants of Health
          id: explore_social_determinants_health_spark_nlp_models         
          image: 
              src: /assets/images/Social_Determinants_of_Health.svg
          excerpt: Extract Social Determinants of Healthcare such as employment, education, social support, housing, financial hardship, substance abuse, demographics, and more.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/SDOH/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/36.Social_Determinant_of_Health_Models.ipynb
        - title: Calculate Medicare HCC Risk Score
          id: calculate_medicare_risk_score 
          image: 
              src: /assets/images/Calculate_Medicare_Risk_Score.svg
          excerpt: Automatically calculate patient risk adjustment scores, using ICD codes of diseases that are extracted from clinical notes about a patient.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/HCC_RISK_SCORE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.1.Calculate_Medicare_Risk_Adjustment_Score.ipynb
        - title: Recommend Available Models for Your Text    
          id: detect_available_pretrained_ner_models         
          image: 
              src: /assets/images/Detect_Available_Pretrained_NER_Models.svg
          excerpt: This pipeline is used to explore all the available pretrained entity recognition models at once. It recommends which models will provide results on a given document.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/NER_PROFILING/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb
---




