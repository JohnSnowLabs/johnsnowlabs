---
layout: demopagenew
title: Classify Legal Texts - Legal NLP Demos & Notebooks
seotitle: 'Legal NLP: Classify Legal Texts - John Snow Labs'
subtitle: Run 300+ live demos and notebooks
full_width: true
permalink: /legal_text_classification
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
        - subtitle: Classify Legal Texts - Live Demos & Notebooks
          activemenu: legal_text_classification
      source: yes
      source:         
        - title: Classify hundreds types of clauses (Binary - clause detected or not)
          id: legal_clauses_classification    
          image: 
              src: /assets/images/Legal_Clauses_Classification.svg
          excerpt: These models check for specific clauses in legal texts, returning them (for example, "investments", "loans", etc. ) or “other” if the clause was not found.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/legal/CLASSIFY_LEGAL_CLAUSES/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/legal-nlp/04.0.Clause_Document_Classification.ipynb
        - title: Classify 15 types of clauses (Multilabel)  
          id: classify_texts_15_types_legal_clauses     
          image: 
              src: /assets/images/Classify_texts_into_15_types_of_legal_clauses.svg
          excerpt: Using Multilabel Document Classification, where several classes can be assigned to a text, this demo will analyse and provide the best class or classes given an input text. This demo can be used to detect relevant clauses in a legal text.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/legal/LEGMULTICLF_LEDGAR/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/legal-nlp/04.0.Clause_Document_Classification.ipynb
        - title: Classify Law Stack Exchange Questions
          id: classify_law_stack_exchange_questions    
          image: 
              src: /assets/images/Classify_Law_Stack_Exchange_Questions.svg
          excerpt: This demo classifies a wide variety of legal issues. The model demonstrates remarkable proficiency in predicting `business`, `constitutional-law`, `contract-law`, `copyright`, `criminal-law`, `employment`, `liability`, `privacy`, `tax-law`, and `trademark`.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/legal/CLASSIFICATION_LAW_EXCHANGE/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/legal-nlp/04.0.Clause_Document_Classification.ipynb
        - title: Classify Judgements Clauses 
          id: classify_judgements_clauses      
          image: 
              src: /assets/images/Classify_Judgements_Clauses.svg
          excerpt: These models analyze and identify if a clause is a decision, talks about a legal basis, a legitimate purpose, etc. and if an argument has been started by the ECHR, Commission/Chamber, the State, Third Parties, etc.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/legal/LEG_JUDGEMENTS_CLF/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/legal-nlp/04.0.Clause_Document_Classification.ipynb
        - title: Classify Document into their Legal Type  
          id: classify_document_legal_type       
          image: 
              src: /assets/images/Classify_Document_into_their_Legal_Type.svg
          excerpt: This demo shows how to classify long texts / documents into a subsample of 8 different types.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/legal/CLASSIFY_LEGAL_DOCUMENTS/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/legal/CLASSIFY_LEGAL_DOCUMENTS.ipynb
        - title: Classify Swiss Judgements Documents  
          id: classify_swiss_judgements_documents       
          image: 
              src: /assets/images/Classify_Swiss_Judgements_Documents.svg
          excerpt: This demo shows how to classify Swiss Judgements documents in English, German, French, Italian into Civil Law, Insurance Law, Public Law, Social Law, Penal Law or Other.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/legal/LEGCLF_SWISS_JUDGEMENTS/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/legal-nlp/04.0.Clause_Document_Classification.ipynb
        - title: Determine the category of a section within a subpoena
          id: determine_category_section_within_subpoena       
          image: 
              src: /assets/images/Determine_the_category_of_a_section_within_a_subpoena.svg
          excerpt: This is a multiclass classification model designed to determine the category of a section within a subpoena. A subpoena is a formal document issued by a court, grand jury, legislative body or committee, or authorized administrative agency. It commands an individual to appear at a specific time and provide testimony, either orally or in writing, regarding the matter specified in the document.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/legal/CLASSIFICATION_SUBPOENA/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/legal-nlp/04.0.Clause_Document_Classification.ipynb
        - title: Legal Contract NLI
          id: legal_contract_nli       
          image: 
              src: /assets/images/Legal_Contract_NLI.svg
          excerpt: This is a text-to-text generation model (encode-decoder architecture) that has undergone fine-tuning on contract for Natural Language Inference on in-house curated dataset, aiming to streamline and expedite the contract review process. The objective of this task is to provide a system with a set of hypotheses, like “Some obligations of Agreement may survive termination,” along with a contract, and task it with classifying whether each hypothesis is entailed, contradicted, or not mentioned (neutral) by the contract.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/legal/LEGGEN_CONTRACT_NLI/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/legal-nlp/04.0.Clause_Document_Classification.ipynb
---