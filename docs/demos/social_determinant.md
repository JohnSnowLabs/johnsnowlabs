---
layout: demopagenew
title: Social Determinant - Clinical NLP Demos & Notebooks
seotitle: 'Clinical NLP: Social Determinant - John Snow Labs'
subtitle: Run 300+ live demos and notebooks
full_width: true
permalink: /social_determinant
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
        - subtitle: Social Determinant - Live Demos & Notebooks
          activemenu: social_determinant
      source: yes
      source:        
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
        - title: Detect Social Determinants of Health Entities 
          id: detect_social_determinants_health_entities         
          image: 
              src: /assets/images/Generic_Classify_Social_Determinants_of_Health.svg
          excerpt: This demo shows how to detect social determinants of health in medical text using Spark NLP Healthcare NER models.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_NER/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/SOCIAL_DETERMINANT_NER.ipynb
        - title: Detect Assertion Status from Social Determinants of Health (SDOH) Entities 
          id: detect_assertion_status_social_determinants_health_entities         
          image: 
              src: /assets/images/Detect_Assertion_Status_from_Social_Determinants_of_Health_(SDOH)_Entities.svg
          excerpt: 'This demo specializes in classifying assertions in text into six distinct entities: ‘Absent’, ‘Present’, ‘Someone_Else’, ‘Past’, ‘Hypothetical’, and ‘Possible’. Each entity represents a unique type of assertion, such as denoting absence, indicating presence, referring to someone else, discussing past events, speculating hypothetically, or suggesting potential conditions.' 
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/ASSERTION_SDOH/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/36.Social_Determinant_of_Health_Models.ipynb
        - title: Classify Social Support 
          id: classify_social_support         
          image: 
              src: /assets/images/Classify_Social_Determinants_of_Health.svg
          excerpt: This demo shows how you can detect social determinants of health in medical text using Spark NLP Healthcare Sequence Classification models.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_CLASSIFICATION/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/SOCIAL_DETERMINANT_CLASSIFICATION.ipynb    
        - title: SDOH Classification
          id: sdoh_frailty_classification         
          image: 
              src: /assets/images/SDOH_Frailty_For_Classification.svg
          excerpt: This model classifies related to frailty, vulnerability, violence, abuse and mental health status in the clinical documents.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_SEQUENCE_CLASSIFICATION/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/SOCIAL_DETERMINANT_CLASSIFICATION.ipynb            
        - title: Classify Alcohol Status    
          id: classify_alcohol_status         
          image: 
              src: /assets/images/Classify_Alcohol_Status.svg
          excerpt: This demo shows how you can detect alcohol use in medical text using Spark NLP Healthcare Generic Classification model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_ALCOHOL/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/SOCIAL_DETERMINANT_CLASSIFICATION.ipynb
        - title: Classify Tobacco Consumption
          id: classify_tobacco_consumption         
          image: 
              src: /assets/images/Classify_Tobacco_Consumption.svg
          excerpt: This demo shows how you can detect tobacco use in medical text using Spark NLP Healthcare Generic Classification model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_TOBACCO/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/SOCIAL_DETERMINANT_CLASSIFICATION.ipynb
        - title: Extract Access to Healthcare Entities from Social Determinants of Health Texts
          id: extract_access_healthcare_entities_social_determinants_health_texts         
          image: 
              src: /assets/images/Extract_Access_to_Healthcare_Entities_from_Social_Determinants_of_Health_Texts.svg
          excerpt: This demo extracts access to healthcare information related to Social Determinants of Health from various kinds of clinical documents.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/NER_SDOH_ACCESS/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/SOCIAL_DETERMINANT_NER.ipynb
        - title: Extract Health and Behaviors Problems Entities from Social Determinants of Health Texts
          id: extract_health_behaviors_problems_entities_social_determinants_health_texts         
          image: 
              src: /assets/images/Extract_Health_and_Behaviours_Problems_Entities_from_Social_Determinants_of_Health_Texts.svg
          excerpt: This demo extracts health and behaviors problems related to Social Determinants of Health from various kinds of clinical documents.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/NER_SDOH_BEHAVIOURS_PROBLEMS/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/SOCIAL_DETERMINANT_NER.ipynb
        - title: Extract Community Condition Entities from Social Determinants of Health Texts
          id: extract_community_condition_entities_social_determinants_health_texts         
          image: 
              src: /assets/images/Extract_Community_Condition_Entities_from_Social_Determinants_of_Health_Texts.svg
          excerpt: This demo extracts community condition information related to Social Determinants of Health from various kinds of biomedical documents.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/NER_SDOH_COMMUNITY_CONDITION/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/SOCIAL_DETERMINANT_NER.ipynb
---
