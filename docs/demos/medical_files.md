---
layout: demopagenew
title: Medical Files Processing - Visual NLP Demos & Notebooks
seotitle: 'Visual NLP: Medical Files Processing - John Snow Labs'
subtitle: Run 300+ live demos and notebooks
full_width: true
permalink: /medical_files
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
        - subtitle: Medical Files Processing - Live Demos & Notebooks
          activemenu: medical_files
      source: yes
      source: 
        - title: Medical Document De-Identification (VLM)
          id: vlm_visual_deid
          image: 
              src: /assets/images/Deidentify_PDF_documents.svg
          excerpt: Redact PHI from scanned clinical documents with bounding-box precision using the JSL Vision OCR plus Spark NLP DEID pipeline. 100% PHI recall, fully on-prem.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/VLM_WORKSHOP/visual-deid
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/vlm-workshop/1.visual_deid.ipynb
        - title: Medical Document Cross-Modal Search (RAG)
          id: vlm_medical_rag
          image: 
              src: /assets/images/Answering_Medical_Questions.svg
          excerpt: Search medical records by text, image, or both using JSL Vision cross-modal embeddings, with Spark NLP entity extraction and ICD-10, RxNorm and SNOMED coding.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/VLM_WORKSHOP/medical-rag
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/vlm-workshop/3.medical_rag.ipynb
        - title: Dermatology Image Classification and Retrieval
          id: vlm_dermatology_rag
          image: 
              src: /assets/images/Image_Classifier_in_Document_Images.svg
          excerpt: Classify skin lesions (91% across 8 classes) and retrieve visually similar cases with ICD-10 coding, powered by JSL Vision image embeddings.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/VLM_WORKSHOP/dermatology-rag
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/vlm-workshop/4.dermatology_rag.ipynb
        - title: Radiology Image Classification and Retrieval
          id: vlm_radiology_rag
          image: 
              src: /assets/images/Detect_Anatomical_and_Observation_Entities_in_Chest_Radiology_Reports.svg
          excerpt: Classify chest X-ray findings and body parts, extract radiology entities, and retrieve similar prior studies on-prem.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/VLM_WORKSHOP/radiology-rag
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/vlm-workshop/5.radiology_rag.ipynb
        - title: Pathology Slide Classification and Retrieval
          id: vlm_pathology_rag
          image: 
              src: /assets/images/Image_Classifier_in_Document_Images.svg
          excerpt: Breast-cancer screening, tissue typing and WBC classification with ICD-O coding over a large histopathology image index.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/VLM_WORKSHOP/pathology-rag
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/vlm-workshop/6.pathology_rag.ipynb
        - title: ECG Waveform Analysis
          id: vlm_ecg_analysis
          image: 
              src: /assets/images/Multilabel_Text_Classification_for_Heart_Disease.svg
          excerpt: Extract cardiac measurements (HR, PR, QRS, QT, Axis) from scanned paper ECGs and triage normal vs abnormal with JSL Vision Structured.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/VLM_WORKSHOP/ecg-analysis
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/vlm-workshop/7.ecg_waveform_analysis.ipynb
        - title: Dicom to Text
          id: dicom_to_text
          image: 
              src: /assets/images/DICOM_to_Text.svg
          excerpt: Recognize text from DICOM format documents. This feature explores both to the text on the image and to the text from the metadata file.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/DICOM_TO_TEXT/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/ocr/DICOM_TO_TEXT.ipynb
        - title: Deidentify DICOM documents
          id: deidentify_dicom_documents_1
          image: 
              src: /assets/images/Deidentify_DICOM_documents_1.svg
          excerpt: Deidentify DICOM documents by masking PHI information on the image and by either masking or obfuscating PHI from the metadata.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/DEID_DICOM_IMAGE/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrImageDeIdentification.ipynb
        - title: Deidentification of Whole Slide Image (WSI)
          id: wsi_deid  
          image: 
              src: /assets/images/De-Identify_DICOM_Images.svg
          excerpt: De-identification of Whole Slide Images
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/WSI_DEID/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrWSIDeidentification.ipynb
        - title: Pretrained Pipelines for Dicom De-Identification 
          id: pp_pdf_deidentification  
          image: 
              src: /assets/images/Deidentify_DICOM_documents.svg
          excerpt: De-identify DICOM files to mask or obfuscate PHI to preserve healthcare privacy.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/PP_DICOM_DEID/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/Dicom/SparkOcrDicomPretrainedPipelines.ipynb
---