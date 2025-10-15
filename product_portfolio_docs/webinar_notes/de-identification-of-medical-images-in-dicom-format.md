# De-Identification of Medical Images in DICOM Format
De-Identification of Medical Images in DICOM Format

https://www.johnsnowlabs.com/de-identification-of-medical-images-in-dicom-format/

<https://youtu.be/095_4jI9Y74>

<img src="/media/image.jpg" title="Video titled: De-Identification of Medical Images in DICOM Format" style="width:6.3125in;height:3.65625in" />

The source provides a detailed summary of a John Snow Labs (JSL) webinar focused on the \*\*de-identification of DICOM (Digital Imaging and Communications in Medicine) filesThe source provides a detailed summary of a John Snow Labs (JSL) webinar focused on the **de-identification of DICOM (Digital Imaging and Communications in Medicine) files**, specifically addressing the removal of Protected Health Information (PHI) from both the metadata and the image pixels. The presentation was led by Alberto.

## **Overview of DICOM Files and Challenges**

### **DICOM File Format**

DICOM is a mature format, having turned 30 years old last year, originally developed for **radiology** and later expanding to other fields like **Cardiology**.

**Key Characteristics:**

- **Data Integrity:** The **metadata is as important as the image data itself**, and they need to stay together.

- **Functionality:** DICOM does not limit its action to images and associated information from medical devices; it is also used for **communication between machines**.

- **Evolution:** The standard is reviewed five times a year, meaning it changes quite often.

### **DICOM Challenges**

DICOM files present several challenges, particularly when attempting de-identification:

1.  **Transfer Syntaxes:** These encompass compression types (lossy or lossless) and rules on how data is stored (e.g., byte ordering, endianness). It is crucial not to interfere with these syntaxes when converting files from an identified to a de-identified version, as moving from lossless to lossy compression can affect image quality.

2.  **Metadata Complexity:** Metadata elements are typically represented as tuples of hexadecimal numbers (group ID and element ID).

    1.  **Manufacturer-Specific Tags:** Some tags can be **manufacturer-specific** and undocumented, making PHI removal challenging because a simple, hardcoded set of tags is insufficient. User-defined tags must be interpreted during processing.

3.  **Volume:** DICOM datasets can be **huge**, often reaching one gigabyte or more per file, which requires solutions like Apache Spark for scalable processing.

### **De-Identification Targets (PHI Removal)**

De-identification targets involve removing PHI from two main areas:

1.  **Metadata:** Removing PHI values from the list of tags (resulting in empty strings for sensitive values).

2.  **Image Pixels:** Removing visible PHI (like accession numbers or patient names) that are overlaid on the image itself, typically by plotting a **black bounding box** over the sensitive text.

## **John Snow Labs' Visual NLP Library**

The solution relies on the JSL's **Visual NLP library (Visp)**, a document understanding library built specifically to solve real-life problems.

**Key Features of Visual NLP:**

- **Security Minded:** It is **not an API**, meaning data (like DICOM files) does not need to be sent to an external endpoint. Users can deploy the solution **on-premises** or in their own environment, ensuring absolute control over the data's location and safety.

- **Scalability:** It relies on **Apache Spark** for distributing the data, which is essential given the large size of DICOM files.

- **Pre-built Features:** It includes curated features, pipelines, and models for tasks like **text detection and recognition** and **Named Entity Recognition (NER) models** for identifying entities within text.

## **De-Identification Pipelines and Techniques**

The presentation demonstrated several pipelines for de-identification, moving from basic text removal to advanced NLP-enhanced techniques.

### **1. Basic Metadata and Initial File Handling**

The initial step involves using the DicomToMetadata transformer to take binary content and return the metadata as a column in a Spark DataFrame. This allows users to compute metrics on file size, frame count, and overall job complexity before processing.

### **2. Basic Text Removal (Black Bounding Box)**

The simplest de-identification pipeline focuses on removing all detected text regions.

- **Dicom Splitter:** This transformer leverages Spark's distributed capabilities to **split multi-frame DICOM files** into individual frames and distribute them across multiple partitions for parallel processing.

- **Dicom to Image:** Pulls out the image from each frame.

- **Detecting Text & Drawing Regions:** Text is detected on the image, and the resulting regions are used to **draw bounding boxes**, hiding all the text.

### **3. NLP-Enhanced De-Identification (Selective Removal)**

The most advanced method uses NLP to selectively remove only sensitive entities, preserving non-PHI text. This prevents simply getting rid of everything on the image.

**The Integrated Pipeline Flow:**

1.  **Dicom to Image:** Extracts the image.

2.  **Image Text Detector & OCR:** Detects text regions and extracts the raw text from those regions.

3.  **NLP Pipeline (Entity Recognition):** The extracted text is processed through an NLP pipeline to identify specific entities.

    1.  **NLP Stages:** This sub-pipeline includes DocumentAssembler, Normalizer, SentenceDetector, Tokenizer, Embeddings, and a **Named Entity Recognition (NER) model**. The NER model is key to detecting specific PHI like **Social Security numbers, patient IDs, age, or date of birth**.

    2.  **NER Converter:** Converts token-level entities (e.g., "congestive heart failure") into single chunks for easier handling.

4.  **Position Finder:** Takes the identified entities and returns the coordinates/bounding boxes corresponding to those specific entities.

5.  **Draw Regions:** Uses the calculated bounding boxes to obscure only the PHI text.

### **4. Metadata-Assisted De-Identification (Complimentary Approach)**

This approach uses PHI clues found in the DICOM metadata to identify and remove corresponding text on the image, acting as a **complimentary approach** to pure ML models.

- **Chunk Merge:** The pipeline uses a ChunkMerge approach to combine entities from multiple sources, allowing specialized models to detect different things simultaneously.

- **Dicom De-identifier:** This model receives text coordinates and metadata and returns entities. It makes sense of **both the metadata and the text on the image**.

- **Final Pipeline:** This combined pipeline uses the DicomMetadataIdentifier (for metadata PHI) and the DicomDeidentifier (which uses metadata clues to target image PHI) alongside the standard text-based NER models, ensuring comprehensive removal.

## **Streaming Capabilities**

The examples demonstrated the ability to run these pipelines in **streaming mode** using Apache Spark's Structured Streaming.

- **Functionality:** The pipeline can connect to a source (like a folder or Kafka system). When a file is dropped in the source, the stream ingests, processes, and produces results to a sync.

- **Microbatch:** Streaming pipelines run on **microbatch** processing, allowing configuration of the number of files processed at a time.