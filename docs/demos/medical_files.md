---
layout: demopagenew
title: Extract Text from Documents - Visual NLP Demos & Notebooks
seotitle: 'Visual NLP: Extract Text from Documents - John Snow Labs'
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
        - subtitle: Extract Text from Documents - Live Demos & Notebooks
          activemenu: medical_files
      source: yes
      source: 
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
          id: wsi_deid  
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