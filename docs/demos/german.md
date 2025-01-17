---
layout: demopagenew
title: German - Medical NLP Demos & Notebooks
seotitle: 'Medical NLP: German - John Snow Labs'
subtitle: Run 300+ live demos and notebooks
full_width: true
permalink: /german
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
        - subtitle: German - Live Demos & Notebooks
          activemenu: german
      source: yes
      source:           
        - title: Detect symptoms, treatments and other clinical information in German
          id: detect_symptoms
          image: 
              src: /assets/images/Detect_causality_between_symptoms.svg
          excerpt: Automatically identify symptoms, diagnoses, procedures, body parts or medication in German clinical texts.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/NER_HEALTHCARE_DE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_HEALTHCARE_DE.ipynb
        - title: Resolve German Clinical Health Information using the SNOMED taxonomy
          id: resolve_german_clinical_health_information_using_snomed_taxonomy 
          image: 
              src: /assets/images/Resolve_German_Clinical_Health_Information_using_the_SNOMED_taxonomy.svg
          excerpt: This demo shows how German clinical health information (like diagnoses/procedures) can be mapped to codes using the SNOMED taxonomy.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/ER_SNOMED_DE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/14.German_Healthcare_Models.ipynb
        - title: Resolve German Clinical Findings using the ICD10-GM taxonomy 
          id: resolve_german_clinical_findings_using_icd10_gm_taxonomy 
          image: 
              src: /assets/images/Resolve_German_Clinical_Findings_using_the_ICD10-GM_taxonomy.svg
          excerpt: This demo shows how German clinical findings can be mapped to codes using the ICD10-GM taxonomy.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/ER_ICD10_GM_DE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/ER_ICD10_GM_DE.ipynb
        - title: Detect PHI terminology in German medical text
          id: detect_phi_terminology_german_medical_text  
          image: 
              src: /assets/images/Detect_PHI_terminology_German_medical_text.svg
          excerpt: This demo shows how Protected Health Information (PHI) in German that may need to be de-identified can be extracted using Spark NLP Healthcare NER model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/NER_DEID_DE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.1.Clinical_Multi_Language_Deidentification.ipynb 
        - title: Deidentify German Medical texts
          id: deidentify_german_medical_texts   
          image: 
              src: /assets/images/Deidentify_German_Medical_texts.svg
          excerpt: This demo shows how to deidentify protected health information in German medical texts.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/DEID_PHI_TEXT_DE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.1.Clinical_Multi_Language_Deidentification.ipynb
        - title: Classify Public Health Mentions in German
          id: classify_public_health_mentions_de          
          image: 
              src: /assets/images/Classify_Public_Health_Mentions.svg
          excerpt: This model classify public health mentions in social media text.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/PUBLIC_HEALTH_MENTIONS_DE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/PUBLIC_HEALTH_MENTIONS_DE.ipynb           
---