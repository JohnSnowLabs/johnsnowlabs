---
layout: demopagenew
title: Diagnoses & Procedures - Clinical NLP Demos & Notebooks
seotitle: 'Clinical NLP: Diagnoses & Procedures - John Snow Labs'
subtitle: Run 300+ live demos and notebooks
full_width: true
permalink: /diagnoses_procedures
key: demo
nav_key: demo
nav_key: demo
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
        - subtitle: Diagnoses & Procedures - Live Demos & Notebooks
          activemenu: diagnoses_procedures
      source: yes
      source:    
        - title: Detect clinical entities in text with different ner models
          id: detect_clinical_entities_text_different_ner_models
          image: 
              src: /assets/images/Detect_clinical_entities_in_text_with_different_ner_models.svg
          excerpt: Automatically detect clinical entities using our different NER deep learning models.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/NER/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb        
        - title: Detect clinical entities in text
          id: detect_clinical_entities_in_text
          image: 
              src: /assets/images/Detect_risk_factors.svg
          excerpt: Automatically detect more than 50 clinical entities using our NER deep learning model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL/
          - text: Colab
            type: blue_btn
            url: https://githubtocolab.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb  
        - title: Detect Clinical Entities in Text (Multilingual)
          id: detect_clinical_entities_text_multilingual
          image: 
              src: /assets/images/Detect_Clinical_Entities_in_Text_Multilingual.svg
          excerpt: This demo automatically identify the entities of Problem, Test, and Treatment Entities in medical texts.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CLINICAL_MULTI.ipynb
        - title: Model Augmentation with LangTest
          id: model_augmentation_langtest
          image: 
              src: /assets/images/Model_Augmentation_with_LangTest.svg
          excerpt: In this demo, We are showing the results of the Original Model on the original text and on the corruped text. In addition, We are showing the result of the Langtest model which is augmented with langtest library for corrupted text cases.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/LANGTEST_NER/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/LANGTEST_NER.ipynb
        - title: Identify diagnosis and symptoms assertion status
          id: identify_diagnosis_and_symptoms_assertion_status
          image: 
              src: /assets/images/Identify_diagnosis_and_symptoms_assertion_status.svg
          excerpt: Automatically detect if a diagnosis or a symptom is present, absent, uncertain or associated to other persons (e.g. family members).
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/ASSERTION/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/ASSERTION.ipynb
        - title: Detect diagnosis and procedures
          id: detect_diagnosis_and_procedures
          image: 
              src: /assets/images/Detect_diagnosis_and_procedures.svg
          excerpt: Automatically identify diagnoses and procedures in clinical documents using the pretrained Spark NLP clinical models.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/NER_DIAG_PROC/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_DIAG_PROC.ipynb
        - title: Detect temporal relations for clinical events
          id: detect_temporal_relations_for_clinical_events
          image: 
              src: /assets/images/Grammar_Analysis.svg
          excerpt: 'Automatically identify three types of relations between clinical events: After, Before and Overlap using our pretrained clinical Relation Extraction (RE) model.'
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/RE_CLINICAL_EVENTS/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/RE_CLINICAL_EVENTS.ipynb
        - title: Detect causality between symptoms and treatment
          id: detect_causality_between_symptoms_and_treatment
          image: 
              src: /assets/images/Grammar_Analysis.svg
          excerpt: Automatically identify relations between symptoms and treatment using our pretrained clinical Relation Extraction (RE) model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/RE_CLINICAL/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/RE_CLINICAL.ipynb
        - title: Detect relations between body parts and clinical entities
          id: detect_relations_between_body_parts_and_clinical_entities
          image: 
              src: /assets/images/Detect_relations.svg
          excerpt: Use pre-trained relation extraction models to extract relations between body parts and clinical entities.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/RE_BODYPART_ENT/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/10.1.Clinical_Relation_Extraction_BodyParts_Models.ipynb
        - title: Detect how dates relate to clinical entities
          id: detect_how_dates_relate_to_clinical_entities
          image: 
              src: /assets/images/ExtractRelationships_2.svg
          excerpt: Detect clinical entities such as problems, tests and treatments, and how they relate to specific dates.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/healthcare/RE_CLINICAL_DATE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/RE_CLINICAL_DATE.ipynb
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