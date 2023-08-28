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
        - title: Detect PHI Entities from Deidentification 
          id: detect_phi_entities_deidentification_2
          image: 
              src: /assets/images/FreeText.svg
          excerpt: This demo shows how to deidentify protected health information.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/DEID_LIVE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/DEID_PHI_TEXT_MULTI.ipynb
        - title: Explore Adverse Drug Events with Spark NLP Models
          id: explore_adverse_drug_events_spark_nlp_models   
          image: 
              src: /assets/images/Explore_Adverse_Drug.svg
          excerpt: This demo shows how detect adverse reactions of drugs in reviews, tweets, and medical text using Spark NLP Healthcare NER, Sequence Classification, Assertion Status, and Relation Extraction models.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/ADE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/16.Adverse_Drug_Event_ADE_NER_and_Classifier.ipynb
        - title: Explore Oncology Notes with Spark NLP Models
          id: explore_oncology_notes_spark_models
          image: 
              src: /assets/images/Detect_Oncological_Concepts.svg
          excerpt: This demo shows how oncological terms can be detected using Spark NLP Healthcare NER, Assertion Status, and Relation Extraction models.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/ONCOLOGY/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/27.Oncology_Model.ipynb
        - title: Voice of Patients
          id: vop           
          image: 
              src: /assets/images/Voice_Of_Patient.svg
          excerpt: This demo extracts and classifies healthcare-related terms from the documents transferred from the patient’s own sentences.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/VOP/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/VOICE_OF_PATIENT.ipynb
        - title: Explore Social Determinants of Health with Spark NLP Models 
          id: explore_social_determinants_health_spark_nlp_models         
          image: 
              src: /assets/images/Social_Determinants_of_Health.svg
          excerpt: This demo shows how social determinant terms can be detected using Spark NLP Healthcare NER and Text Classification.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/SDOH/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/36.Social_Determinant_of_Health_Models.ipynb
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
        - title: Calculate Medicare HCC Risk Score
          id: calculate_medicare_risk_score 
          image: 
              src: /assets/images/Calculate_Medicare_Risk_Score.svg
          excerpt: This demo shows how to calculate medical risk adjustment scores automatically using ICD codes of diseases.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/HCC_RISK_SCORE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.1.Calculate_Medicare_Risk_Adjustment_Score.ipynb
        - title: Detect Available Pretrained NER Models    
          id: detect_available_pretrained_ner_models         
          image: 
              src: /assets/images/Detect_Available_Pretrained_NER_Models.svg
          excerpt: This pipeline can be used to explore all the available pretrained NER models at once. When you run this pipeline over your text, you will end up with the predictions coming out of each pretrained clinical NER model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/NER_PROFILING/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb                
---




