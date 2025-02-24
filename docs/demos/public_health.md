---
layout: demopagenew
title: Public Health - Biomedical NLP Demos & Notebooks
seotitle: 'Biomedical NLP: Public Health - John Snow Labs'
subtitle: Run 300+ live demos and notebooks
full_width: true
permalink: /public_health
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
        - subtitle: Public Health - Live Demos & Notebooks
          activemenu: public_health
      source: yes
      source:        
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
        - title: Voice of Patients NER
          id: voice_patients           
          image: 
              src: /assets/images/Voice_of_the_Patients.svg
          excerpt: This demo extracts healthcare-related terms from the documents transferred from the patient’s own sentences.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/VOP_NER/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/VOICE_OF_PATIENT.ipynb
        - title: Assertion Status for Voice of the Patients 
          id: assertion_status_voice_patients           
          image: 
              src: /assets/images/Assertion_Status_for_Voice_of_the_Patients.svg
          excerpt: Assertion status model used to predict if an NER chunk refers to a positive finding from the patient (Present_Or_Past), or if it refers to a family member or another person (SomeoneElse) or if it is mentioned but not as something present (Hypothetical_Or_Absent).
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/ASSERTION_VOP/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/35.Voice_of_Patient_Models.ipynb
        - title: Side Effect Classifier(VOP)   
          id: side_effect_classifier_vop 
          image: 
              src: /assets/images/Side_Effect.svg
          excerpt: This demo showcases a classification model designed to detect mentions of side effects in patient-written texts.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/VOP_CLASSIFICATION_SIDE_EFFECT/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/VOICE_OF_PATIENT.ipynb
        - title: Classify Self-Reported Age from Posts  
          id: classify_self_report_age_tweet   
          image: 
              src: /assets/images/Classify_Self_Report_Age_Tweet.svg
          excerpt: These models classify self-report the exact age into social media data.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/PUBLIC_HEALTH_AGE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/PUBLIC_HEALTH_MB4SC.ipynb        
        - title: Detect Adverse Drug Events from Posts   
          id: detect_adverse_drug_events_tweet    
          image: 
              src: /assets/images/Detect_Adverse_Drug_Events_in_Tweet.svg
          excerpt: These models classify self-report the exact age into social media data.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/PUBLIC_HEALTH_ADE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/PUBLIC_HEALTH_MB4SC.ipynb        
        - title: Detection of disease mentions in Spanish tweets 
          id: detection_disease_mentions_spanish_tweets       
          image: 
              src: /assets/images/Detection_of_disease_mentions_in_Spanish_tweets.svg
          excerpt: This model extracts disease entities in Spanish tweets.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/PUBLIC_HEALTH_NER_DISEASE_ES/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/PUBLIC_HEALTH_NER_DISEASE_ES.ipynb         
        - title: Self-Treatment and Drug Changes Classifier in Social Media
          id: selftreatment_drug_changes_classifier_social_media         
          image: 
              src: /assets/images/Self_Treatment_Changes_Classifier_in_Tweets.svg
          excerpt: This model classifies people non-adherent to their treatments and drugs on social media.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/PUBLIC_HEALTH_CHANGE_DRUG_TREATMENT/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/PUBLIC_HEALTH_MB4SC.ipynb                
        - title: Classify Public Health Mentions
          id: classify_public_health_mentions           
          image: 
              src: /assets/images/Classify_Public_Health_Mentions.svg
          excerpt: This model classify public health mentions in social media text.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/PUBLIC_HEALTH_MENTIONS/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/PUBLIC_HEALTH_MB4SC.ipynb     
        - title: Multilabel Text Classification For Respiratory Disease
          id: multilabel_text_classification_respiratory_disease           
          image: 
              src: /assets/images/Multilabel_Text_Classification_For_Respiratory_Disease.svg
          excerpt: 'The PHS-BERT Respiratory Disease Classifier Model is a specialized text classification system, engineered to accurately identify and categorize textual mentions of four prominent respiratory diseases: Asthma, Chronic Obstructive Pulmonary Disease (COPD), Emphysema, and Chronic bronchitis.'
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_RESPIRATORY/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/PUBLIC_HEALTH_CLASSIFIER_DL.ipynb
        - title: Multilabel Text Classification for Heart Disease
          id: multilabel_text_classification_heart_disease           
          image: 
              src: /assets/images/Multilabel_Text_Classification_for_Heart_Disease.svg
          excerpt: 'The PHS-BERT Heart Disease Classifier Model is a specialized text classification system, engineered to accurately identify and categorize textual mentions of three prominent cardiovascular diseases: Hypertension, Coronary Artery Disease, and Myocardial Infarction.'
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_HEART_DISEASE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/PUBLIC_HEALTH_CLASSIFIER_DL.ipynb
---
