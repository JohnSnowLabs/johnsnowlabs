---
layout: demopagenew
title: Extract Text from Documents - Visual NLP Demos & Notebooks
seotitle: 'Visual NLP: Extract Text from Documents - John Snow Labs'
subtitle: Run 300+ live demos and notebooks
full_width: true
permalink: /extract_text_from_documents
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
          activemenu: extract_text_from_documents
      source: yes
      source: 
        - title: PDF to Text
          id: pdf_to_text
          image: 
              src: /assets/images/PDF_to_Text.svg
          excerpt: Extract text from generated/selectable PDF documents and keep the original structure of the document by using our out-of-the-box Spark OCR library.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/PDF_TO_TEXT/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/ocr/PDF_TO_TEXT.ipynb
        - title: DICOM to Text
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
        - title: Image to Text
          id: image_to_text
          image: 
              src: /assets/images/Image_to_Text.svg
          excerpt: Recognize text in images and scanned PDF documents by using our out-of-the-box Spark OCR library.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/IMAGE_TO_TEXT/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/ocr/IMAGE_TO_TEXT.ipynb
        - title: DOCX to Text
          id: docx-to-text
          image: 
              src: /assets/images/correct.svg
          excerpt: Extract text from Word documents with Spark OCR
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/DOCX_TO_TEXT
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/ocr/DOCX_TO_TEXT.ipynb
        - title: Extract text from Powerpoint slides
          id: extract-text-from-power-point-slides 
          image: 
              src: /assets/images/PPTX_to_Text.svg
          excerpt: This demo shows how PPTX texts can be extracted using Spark OCR.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/PPTX_TO_TEXT/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/ocr/PPTX_TABLE.ipynb
        - title: Detect Text in Document Images
          id: detect_text_document_images 
          image: 
              src: /assets/images/Detect_Text_in_Document_Images.svg
          excerpt: This demo detects text in documents using our pre-trained Spark OCR model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/TEXT_DETECTION_DIT/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrImageTextDetection.ipynb
        - title: Recognize Printed
          id: recognize_printed 
          image: 
              src: /assets/images/Recognize_Printed.svg
          excerpt: This demo includes details about how to recognize printed information in documents using our pre-trained Spark OCR models.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/RECOGNIZE_PRINTED/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrImageToTextPrinted_V2_opt.ipynb
        - title: Detect Text in Document Images
          id: detect_text_document_images 
          image: 
              src: /assets/images/Detect_Text_in_Document_Images_1.svg
          excerpt: This model detects text in documents using our pre-trained Spark OCR model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/TEXT_DETECTION/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/Cards/SparkOcrImageTextDetection.ipynb
        - title: Pretrained pipeline for reading on printed documents
          id: pretrained_pipeline_reading_printed_documents 
          image: 
              src: /assets/images/Pretrained_pipeline_for_reading_on_printed_documents.svg
          excerpt: Pretrained pipeline based on our pre-trained Spark OCR models, pipeline for doing transformer based OCR on printed texts. It ensures precise and efficient text extraction from printed images of various origins and formats, improving the overall OCR accuracy. 
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/PP_IMAGE_PRINTED_TRANSFORMER_EXTRACTION/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrPretrainedPipelinesImagePrintedTransformerExtraction.ipynb
        - title: Pretrained pipeline for reading and removing noise on mixed scanned and digital PDF documents
          id: Pretrained_pipeline_noise_mixed_scanned_digital_documents  
          image: 
              src: /assets/images/Pretrained_pipeline_for_reading_on_mixed_scanned_and_digital_PDF_documents.svg
          excerpt: Pretrained pipeline based on our pre-trained Spark OCR models, pipeline for doing transformer based OCR on printed texts. It ensures precise and efficient text extraction from printed images of various origins and formats, improving the overall OCR accuracy.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/PP_IMAGE_PRINTED_TRANSFORMER_EXTRACTION/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrPretrainedPipelinesMixedScannedDigitalPdfImageCleaner.ipynb
        - title: Pretrained pipeline for reading on printed PDF documents
          id: pretrained_pipeline_reading_printed_documents  
          image: 
              src: /assets/images/Pretrained_pipeline_for_reading_on_printed_documents.svg
          excerpt: Pretrained pipeline based on our pre-trained Spark OCR models, pipeline for doing transformer based OCR on printed texts. It ensures precise and efficient text extraction from printed pdfs of various origins and formats, improving the overall OCR accuracy.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/PP_PDF_PRINTED_TRANSFORMER_EXTRACTION/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrPretrainedPipelinesPdfPrintedTransformerExtraction.ipynb
        - title: Pretrained pipeline for reading on mixed scanned and digital PDF documents
          id: pretrained_pipeline_reading_mixed_scanned_digital_pdf_documents  
          image: 
              src: /assets/images/Pretrained_pipeline_for_reading_on_printed_documents.svg
          excerpt: Pretrained pipeline based on our pre-trained Spark OCR models, for conducting Optical Character Recognition (OCR) on mixed scanned and digital PDF documents. It ensures precise and efficient text extraction from PDFs of various origins and formats, improving the overall OCR accuracy.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/PP_MIXED_SCANNED_DIGITAL_PDF/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrPretrainedPipelinesMixedScannedDigitalPdf.ipynb
---