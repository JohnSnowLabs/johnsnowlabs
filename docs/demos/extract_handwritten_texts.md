---
layout: demopagenew
title: Extract handwritten texts - Visual NLP Demos & Notebooks
seotitle: 'Visual NLP: Extract handwritten texts - John Snow Labs'
full_width: true
permalink: /extract_handwritten_texts
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
        - subtitle: Extract handwritten texts - Live Demos & Notebooks
          activemenu: extract_handwritten_texts
      source: yes
      source: 
        - title: Extract Signatures
          id: extract-signatures-new
          image: 
              src: /assets/images/Extract_Signatures_new.svg
          excerpt: This demo shows how handwritten signatures can be extracted from image/pdf documents using Spark OCR.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/DETECT_SIGNATURES/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-ocr-workshop/blob/3.6.0/jupyter/SparkOcrImageSignatureDetection.ipynb
        - title: Detect Handwritten entities
          id: detect-handwritten-entities 
          image: 
              src: /assets/images/Detect_Handwritten_entities.svg
          excerpt: This demo shows how entities can be detected in image or pdf documents using Spark OCR.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/VISUAL_DOCUMENT_HANDWRITTEN_NER/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-ocr-workshop/blob/3.6.0/jupyter/SparkOcrImageHandwrittenDetection.ipynb
        - title: Recognize Handwritten information in Document Images
          id: recognize_handwritten_information_document_images 
          image: 
              src: /assets/images/Recognize_Handwritten_information_in_Document_Images.svg
          excerpt: This demo recognizes handwritten information in documents using our pre-trained Spark OCR model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/RECOGNIZE_HANDWRITTEN/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrImageToTextHandwritten_V2_opt.ipynb
        - title: Detect Handwritten
          id: detect_handwritten 
          image: 
              src: /assets/images/Detect_Handwritten.svg
          excerpt: This demo includes details about how to detect any handwritten text in documents using our pre-trained Spark OCR models.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/DETECT_HANDWRITTEN/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/3.6.0/jupyter/SparkOcrImageHandwrittenDetection.ipynb
---
