---
layout: demopagenew
title: Visual Document Understanding - Visual NLP Demos & Notebooks
seotitle: 'Visual NLP: Visual Document Understanding - John Snow Labs'
subtitle: Run 300+ live demos and notebooks
full_width: true
permalink: /visual_document_understanding
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
        - subtitle: Visual Document Understanding - Live Demos & Notebooks
          activemenu: visual_document_understanding
      source: yes
      source: 
        - title: Visual Document Classification
          id: classify_visual_documents
          image: 
              src: /assets/images/Classify_visual_documents.svg
          excerpt: Classify documents using text and layout data with the new features offered by Spark OCR.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/VISUAL_DOCUMENT_CLASSIFY/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOCRVisualDocumentClassifier.ipynb        
        - title: Extract Data from FoundationOne Sequencing Reports
          id: extract-data-from-foundationone-sequencing-reports
          image: 
              src: /assets/images/correct.svg
          excerpt: Extract patient, genomic and biomarker information from FoundationOne Sequencing Reports.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/FOUNDATIONONE_REPORT_PARSING/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/ocr/FOUNDATIONONE_REPORT_PARSING.ipynb 
        - title: Recognize entities in scanned PDFs
          id: recognize_entities_in_scanned_pdfs
          image: 
              src: /assets/images/Recognize_text_in_natural_scenes.svg
          excerpt: 'End-to-end example of regular NER pipeline: import scanned images from cloud storage, preprocess them for improving their quality, recognize text using Spark OCR, correct the spelling mistakes for improving OCR results and finally run NER for extracting entities.'
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/PDF_TEXT_NER/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/ocr/PDF_TEXT_NER.ipynb
        - title: Extract brands from visual documents
          id: extract_brands_from_visual_documents 
          image: 
              src: /assets/images/Extract_brands_from_visual_documents.svg
          excerpt: This demo shows how brands from image can be detected using Spark OCR.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/BRAND_EXTRACTION/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/ocr/BRAND_EXTRACTION.ipynb
        - title: Visual NER Key-Values v2
          id: visual_ner_key_values_v2 
          image: 
              src: /assets/images/Visual_NER_Key-Values_v2.svg
          excerpt: This demo extract the main document key points using our pre-trained Spark OCR model. 
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/VISUAL_DOCUMENT_KEYVALUES_NER_LILT/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOCRVisualDocumentNer-FormParsing.ipynb
        - title: Visual Question Answering
          id: visual_question_asnswering
          image: 
              src: /assets/images/Visual_Question_Answering.svg
          excerpt: This demo allows Inferring the answer from a given image and a text-based question by using our pre-trained Spark OCR models.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/VISUAL_QUESTION_ANSWERING/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrVisualQuestionAnswering.ipynb
        - title: Chart to Text
          id: chart_text
          image: 
              src: /assets/images/Chart_to_Text.svg
          excerpt: Obtain a description of the charts in the image input document by using our Spark OCR model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/CHART_TO_TEXT/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrChartToTextTable.ipynb
        - title: Chart to Text powered by LLM
          id: chart_text_powered_llm
          image: 
              src: /assets/images/Chart_to_Text_powered_by_LLM.svg
          excerpt: Obtain a deeper interpretation of the charts in the image input document by using our Spark OCR model powered by LLM. 
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/CHART_TO_TEXT_LLM/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrChartToTextLLM.ipynb
        - title: Infographic Visual Question Answering
          id: infographic_visual_question_answering
          image: 
              src: /assets/images/Infographic_Visual_Question_Answering.svg
          excerpt: Infer the answer from a given infographic related image and a text-based question by using our pre-trained Spark OCR model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/INFOGRAPHIC_VISUAL_QUESTION_ANSWERING/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/208cebd1353c5b194baadbcea6e32c292eb46a08/jupyter/Cards/SparkOCRInfographicsVisualQuestionAnswering.ipynb
        - title: Checkbox Detection
          id: checkbox_detection
          image: 
              src: /assets/images/Checkbox_Detection.svg
          excerpt: This model detects and classifies checkboxes in document images using our pre-trained Spark OCR model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/CHECKBOX_DETECTION/
          - text: Colab
            type: blue_btn
            url: https://colab.research.google.com/github/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrCheckBoxDetection.ipynb
        - title: Deidentify Images
          id: deidentify_images
          image: 
              src: /assets/images/Deidentify_Images.svg
          excerpt: Deidentify images by masking sensitive information on the image and by either masking or obfuscating.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/DEID_IMAGE/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrImageDeIdentification.ipynb
        - title: De-identify PDF documents - GDPR Compliance
          id: deidentify_pdf_documents_gdpr_compliance
          image: 
              src: /assets/images/De-identify_PDF_documents_GDPR_Compliance.svg
          excerpt: Deidentify PDF documents using GDPR guidelines by anonymizing PHI information using out of the box Spark NLP models.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/DEID_PDF_GDPR/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrImageDeIdentification.ipynb
        - title: De-identify PDF documents - HIPAA Compliance
          id: deidentify_pdf_documents_hippa_compliance
          image: 
              src: /assets/images/De-identify_PDF_documents_HIPAA_Compliance.svg
          excerpt: Deidentify PDF documents using HIPAA guidelines by masking PHI information using out of the box Spark NLP models.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/DEID_PDF_HIPAA/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrImageDeIdentification.ipynb
        - title: Deidentify Images
          id: deidentify_images
          image: 
              src: /assets/images/Deidentify_Images.svg
          excerpt: Deidentify images by masking sensitive information on the image and by either masking or obfuscating.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/DEID_IMAGE/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrImageDeIdentification.ipynb
        - title: De-identify PDF documents - GDPR Compliance
          id: deidentify_pdf_documents_gdpr_compliance
          image: 
              src: /assets/images/De-identify_PDF_documents_GDPR_Compliance.svg
          excerpt: Deidentify PDF documents using GDPR guidelines by anonymizing PHI information using out of the box Spark NLP models.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/DEID_PDF_GDPR/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrImageDeIdentification.ipynb
        - title: Pretrained Pipelines for Image Deidentification
          id: image_deid_multi_model_context_pipeline_cpu
          image: 
              src: /assets/images/Deidentify_Images.svg
          excerpt: Pretrained pipelines to de-identify images by masking sensitive information on the image and by either masking or obfuscating.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/PP_IMAGE_DEID/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrImageDeIdentificationPipelines.ipynb
        - title: Pretrained Pipelines for Image Deidentification
          id: pp_deidentify_pdf_documents
          image: 
              src: /assets/images/Deidentify_PDF_documents.svg
          excerpt: Pretrained pipelines to de-identify PDF documents, by masking or obfuscating PHI information and signatures.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/PP_PDF_DEIDENTIFICATION
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrPdfDeIdentificationPipelines.ipynb
        - title: Image Classifier in Document Images 
          id: image_classifier_document_images
          image: 
              src: /assets/images/Image_Classifier_in_Document_Images.svg
          excerpt: This model classifies document images using our pre-trained Spark OCR model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/IMAGE_CLASSIFIER/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOCRVisualDocumentClassifierv3.ipynb
        - title: Document Layout Analysis 
          id: document_layout_analysis
          image: 
              src: /assets/images/Document_Layout_Analysis.svg
          excerpt: Identify and structure the visual elements in a document by using our pre-trained Spark OCR models.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/LAYOUT_ANALYSIS/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/Cards/SparkOCRDitLayoutAnalyze.ipynb
        - title: Chart to Text
          id: chart_text
          image: 
              src: /assets/images/Chart_to_Text_1.svg
          excerpt: Obtain a deeper interpretation of the charts in the PDF input document by using our Spark OCR model powered by LLM.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/PDF_CHART_TO_TEXT/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrChartToTextLLM.ipynb
        - title: Relation Extraction 
          id: relation_extraction
          image: 
              src: /assets/images/Relation_Extraction.svg
          excerpt: This model detects key-value pairs in documents using our pre-trained Spark OCR model.
          actions:
          - text: Live Demo
            type: normal
            url: https://demo.johnsnowlabs.com/ocr/RELATION_EXTRACTION/
          - text: Colab
            type: blue_btn
            url: https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/FormRecognition/FormRecognitionGeo.ipynb
---
