# Accurate Table Extraction from Documents & Images with Spark OCR
Accurate Table Extraction from Documents & Images with Spark OCR

<https://www.johnsnowlabs.com/watch-webinar-accurate-table-extraction-from-documents-images-with-spark-ocr/>

<https://www.youtube.com/watch?v=J7C9VJ1E_-I>

<img src="/media/image.jpg" title="Video titled: Accurate Table Extraction from Documents &amp; Images with Spark OCR" style="width:6.3125in;height:3.65625in" />

The following is a detailed summary and extraction of the speech from the provided YouTube transcript concerning "Accurate Table Extraction from Documents & Images with Spark OCR."

## **Detailed Summary of the Speech**

The webinar, hosted by John Snow Labs, features **Nicola Malnick**, the lead developer of the Spark OCR library, discussing the methodology and functionality for accurate table extraction.

### **I. Motivation and Problem Definition**

The presentation addresses the frequent requests from customers and previous webinar attendees for robust table extraction capabilities. Analyzing documents is crucial, and tables often contain the **most significant data** in items such as financial statements, academic research papers, and clinical trial documentation.

**Challenges with Tables and Traditional OCR:** Documents contain a variety of table formats, including bordered tables, borderless tables, tables with/without background, and tables having only vertical or horizontal lines.

Applying traditional Optical Character Recognition (OCR) to images containing tables often results in **misordered text**. This misordering occurs particularly when cells have a different number of lines, making subsequent processing using Natural Language Processing (NLP) or other techniques difficult. The ultimate goal is to extract this data and present it as a **data frame** for processing pipelines, CSV, or Excel formats.

### **II. The Spark OCR Solution: A Three-Step Pipeline**

Spark OCR implements a complex, multi-stage solution to handle the table extraction problem:

1.  **Detect Table:** Locate the region of the table on the page.

2.  **Detect Cells:** Identify the boundaries of individual cells within the detected table.

3.  **Recognize Text:** Extract the text content from each cell.

#### **A. Step 1: Table Detection**

Table detection is treated as a classical computer vision problem.

- **Model Architecture:** Spark OCR uses deep learning models based on **Cascade Mask Region-based Convolution High Resolution Networks**. This architecture is an evolution of Faster CNN Mask RCNN and demonstrates state-of-the-art accuracy on related tasks.

- **Training Data:** Models are trained using datasets from **ICDR competitions** (2013, 2019) and the **Microsoft Table Bank dataset**.

- **Component:** The ImageTableDetector is a Spark OCR transformer that defines input (image column) and output (detected regions). The output provides the **bounding box** coordinates of the tables detected.

- **Pre-trained Models:** Three pre-trained models are available on the model hub, including general detection models and two models fine-tuned specifically on the ICDR and Table Bank datasets.

#### **B. Step 2: Cell Detection**

Spark OCR implements a few methods for cell detection, with future plans for improvement.

1.  **Contour Method:** This method only works for **bordered tables**. It involves memoizing the image (removing background, standardization) and detecting contours to identify cells.

2.  **Morphological Method:** This method is more broadly useful as it works well for **bordered, borderless, and combined tables**. It uses standardization (removing lines), blurring text, and then calculating **histograms** across axes with thresholding to detect columns and rows.

- **Component:** The ImageTableCellDetector takes the detected table image as input and outputs an array of cells, including coordinates (x, y) and use cases.

- **Future Development:** Developers are working on a **Deep Learning approach** for cell detection to achieve better accuracy, especially for low-quality images or those with background noise, where simple image processing methods fail. This will be based on text detection or computer vision object detection approaches.

#### **C. Step 3: Text Recognition and Structure Output**

The final stage involves extracting the text and compiling the structure.

- **Text Recognition:** The ImageCellToTextTableTransformer uses the output from the table and cell detectors to recognize text within each cell. It can strip extra white spaces and set margin parameters.

- **OCR Solution:** The core OCR uses a wrapper for Tesseract and John Snow Labs' own two-stage deep learning solution: (1) Detect text using a deep learning approach for speed, and (2) Recognize the text using a CRNN component.

- **Output Structure:** The result is stored as a **table structure** in a dedicated output column.

### **III. Building Pipelines and Processing Documents**

A common image processing pipeline includes the three main transformers in sequence: ImageTableDetector, ImageTableCellDetector, and ImageCellsToTextTableTransformer.

For processing **PDF documents**, the PdfToImageTransformer must be added to the pipeline first to render the PDF (searchable or image-based) into an image format that the subsequent detectors can handle.

Notebook examples demonstrate how to set up the Spark sessions (requiring Spark NLP dependencies), read images, and use transformers for conversion (BinaryToImageTransformer), detection, and visualization (ImageDrawRegionsTransformer). To view results effectively, the internal table structure must be "exploded" into separate columns.

### **IV. Roadmap and Future Work**

Key features on the roadmap include:

1.  **Deep Learning Cell Detector:** To improve accuracy, especially for complex tables and poor background conditions.

2.  **Header Detection:** Implementing specific algorithms to **detect and handle complex headers** (including horizontal and vertical headers).

3.  **New Output Formats:** Plans to add **CSV and Excel** formats for output, potentially including HTML if requested by customers.

4.  **Labeling:** Future releases will include output labels for tables, indicating if they are **bordered or borderless**.

Additionally, users can fine-tune the table detection models using the Annotation Lab if they need to detect highly specific tables not covered by the existing pre-trained models.

### **V. Q&A Highlights**

**Performance and Scaling:** Spark OCR focuses on distributed computation using Spark partitions to process single images efficiently. Challenges include managing significant **memory usage** required for image processing. When dealing with very large PDFs (sometimes containing 1,000 to 10,000 pages), the PdfToImageTransformer provides options to distribute pages or split large documents to reduce memory footprint and improve performance.

**Extraction Time:** Table detection and extraction currently take about **10 to 20 seconds per page**, though this depends heavily on the size and quality of the original image.

**Merged Cells:** Currently, Spark OCR may detect merged cells as a single cell. Future updates aim to provide customizable parameters and thresholds to better handle the processing of merged cells.

**GPU Compatibility:** Spark OCR is **GPU compatible** and provides better performance on GPUs, especially for deep learning models. While image processing supports GPU currently, specific builds are needed to fully integrate GPU support for the detection models due to complex dependency requirements.

**LayoutLM Integration:** The Cascade Mask RCNN table detection approach is considered **complementary** to models like LayoutLM (used for document classification or Named Entity Recognition, NAR). It is possible to use the table detector output as input for a fine-tuned LayoutLM model, especially for analyzing structured data like medical forms.

**Borderless Tables:** The current models generally work well for **borderless tables**. Fine-tuning the model may be necessary for highly specific borderless use cases to achieve more accurate results.