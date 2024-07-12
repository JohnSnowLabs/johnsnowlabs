---
layout: demopagenew
title: Extract Tables - Visual NLP Demos & Notebooks
seotitle: 'Visual NLP: Extract Tables - John Snow Labs'
subtitle: Run 300+ live demos and notebooks
full_width: true
permalink: /extract_tables
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
        - subtitle: Extract Tables - Live Demos & Notebooks
          activemenu: extract_tables
      source: yes
      source: 
        - title: Extract tables from selectable PDFs
          id: extract_tables_from_pdfs
          image: 
              src: /assets/images/Extract_tables_from_PDFs.svg
          excerpt: Extract tables from selectable PDF documents with Spark OCR.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/PDF_TEXT_TABLE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/ocr/PDF_TEXT_TABLE.ipynb
        - title: Detect and extract tables in scanned PDFs 
          id: detect_tables_extract_text 
          image: 
              src: /assets/images/Detect_sentences_in_text.svg
          excerpt: Detect and extract structured tables from scanned PDF documents & images with Spark OCR.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/IMAGE_TABLE_DETECTION/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrImageTableDetection.ipynb
        - title: Extract tables from Powerpoint slides 
          id: extract_tables_from_power_point_slide  
          image: 
              src: /assets/images/PPTX_to_Table.svg
          excerpt: This demo shows how PPTX tables can be extracted using Spark OCR.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/PPTX_TABLE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/ocr/PPTX_TABLE.ipynb
        - title: Table and Form detection in Document Images
          id: table_form_detection_document_images  
          image: 
              src: /assets/images/Table_and_Form_detection_in_Document_Images.svg
          excerpt: This demo detects tables and forms in documents using our pre-trained Spark OCR model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/IMAGE_TABLE_FORM_DETECTION/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrImageTableAndFormDetection.ipynb
        - title: Image Region Cell Detection
          id: image_region_cell_detection  
          image: 
              src: /assets/images/Image_Region_Cell_Detection.svg
          excerpt: This demo includes details about how to detect the table cells of document images using our pre-trained Spark OCR model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/IMAGE_REGION_CELL_DETECTION/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrImageTableRecognitionWHOCR.ipynb
---
