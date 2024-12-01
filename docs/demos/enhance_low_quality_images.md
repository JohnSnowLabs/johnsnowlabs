---
layout: demopagenew
title: Enhance Low-Quality Images - Visual NLP Demos & Notebooks
seotitle: 'Visual NLP: Enhance Low-Quality Images - John Snow Labs'
subtitle: Run 300+ live demos and notebooks
full_width: true
permalink: /enhance_low_quality_images
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
        - subtitle: Enhance Low-Quality Images - Live Demos & Notebooks
          activemenu: enhance_low_quality_images
      source: yes
      source: 
        - title: Remove background noise from scanned documents
          id: remove_background_noise_from_scanned_documents
          image: 
              src: /assets/images/remove_bg.svg
          excerpt: Removing the background noise in a scanned document will highly improve the results of the OCR. Spark OCR is the only library that allows you to finetune the image preprocessing for excellent OCR results.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/BG_NOISE_REMOVER/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/ocr/BG_NOISE_REMOVER.ipynb
        - title: Correct skewness in scanned documents
          id: correct_skewness_in_scanned_documents
          image: 
              src: /assets/images/correct.svg
          excerpt: Correct the skewness of your scanned documents will highly improve the results of the OCR. Spark OCR is the only library that allows you to finetune the image preprocessing for excellent OCR results.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/SKEW_CORRECTION/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/ocr/SKEW_CORRECTION.ipynb
        - title: Recognize text in natural scenes
          id: recognize_text_in_natural_scenes
          image: 
              src: /assets/images/Frame.svg
          excerpt: By using image segmentation and preprocessing techniques Spark OCR recognizes and extracts text from natural scenes.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/NATURAL_SCENE/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/ocr/NATURAL_SCENE.ipynb
        - title: Enhance Faxes or Scanned Documents
          id: enhance_faxes_scanned_documents
          image: 
              src: /assets/images/Healthcare_Enhancelowquality.svg
          excerpt: Improve quality of (old) faxes/scanned documents using Spark OCR.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/ENHANCE_OLD_FAXES/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOCRGPUOperations.ipynb
        - title: Enhance Photo of Documents
          id: enhance_photo_documents
          image: 
              src: /assets/images/Healthcare_EnhancePhotoofDocuments.svg
          excerpt: Improve quality of documents in image format using Spark OCR.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/ENHANCE_DOC_PHOTO/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOCRGPUOperations.ipynb
        - title: Image Cleaner to Improve Quality of Document Images
          id: image_cleaner_improve_quality_document_images
          image: 
              src: /assets/images/Image_Cleaner_to_Improve_Quality_of_Document_Images.svg
          excerpt: This model improves the quality of document images using our pre-trained Spark OCR model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/IMAGE_CLEANER/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/Cards/SparkOcrImageCleaner.ipynb
        - title: Image Processing to Improve Quality of Document Images
          id: image_processing_improve_quality_document_images
          image: 
              src: /assets/images/Image_Processing_to_Improve_Quality_of_Document_Images.svg
          excerpt: This model improves the quality of documents using different image processing algorithms from our pre-trained Spark OCR model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/IMAGE_PROCESSING/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrImagePreprocessing.ipynb
        - title: Pretrained pipeline for reading and removing noise on mixed scanned and digital PDF documents
          id: Pretrained_pipeline_noise_mixed_scanned_digital_pdf_documents  
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
        - title: Pretrained pipeline for reading and skewing correction on mixed scanned and digital documents
          id: Pretrained_pipeline_for_reading_skewing_correction_mixed_scanned_digital_documents  
          image: 
              src: /assets/images/Pretrained_pipeline_for_reading_on_mixed_scanned_and_digital_PDF_documents.svg
          excerpt: Pretrained pipeline based on our pre-trained Spark OCR models, for conducting Optical Character Recognition (OCR) on mixed scanned and digital PDF documents with page rotation correction. It ensures precise and efficient text extraction from PDFs of various origins and formats, improving the overall OCR accuracy.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/PP_MIXED_SCANNED_DIGITAL_PDF_SKEW_CORRECTION/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrPretrainedPipelinesMixedScannedDigitalPdfSkewCorrection.ipynb
---
