# Consistent Linking, Tokenization, and Obfuscation for Regulatory-Grade De-Identification of Longitudinal Medical Data
Consistent Linking, Tokenization, and Obfuscation for Regulatory-Grade De-Identification of Longitudinal Medical Data

<https://www.johnsnowlabs.com/consistent-linking-tokenization-and-obfuscation-for-regulatory-grade-de-identification-of-longitudinal-medical-data/>

https://www.youtube.com/watch?v=Qn5Q4cezAWQ

The recording outlines a webinar focusing on the **consistent linking of de-identification and obfuscation for regulatory grade patenting of longitudinal medical data** using Johnson Labs (GSL) capabilities via Spark NLP and Healthcare.

## **Key Concepts and Process Overview**

### **Regulatory Grade Medical Data De-identification**

Regulatory grade medical data de-identification is a systematic process designed to remove or transform all Protected Health Information (PHI) from medical data to ensure compliance with privacy laws and standards.

**How it is Achieved:**

1.  **Detection of PHI:** PHI is identified in various formats, including clinical notes, structured/unstructured text, DICOM images, and PDFs. The process initially focuses on identifying direct or indirect identifiers in text, tables, and all modalities.

2.  **Removal or Transformation:** Detected PHIs are either removed (masked) or transformed (obfuscated). Obfuscation involves replacing PHI entities with **realistic faker values**.

3.  **Consistent Linking:** A crucial element where the **same entity receives the same skitted value across all records and time points**.

4.  **Auditability:** The process must be traceable, compliant with laws and standards, and include logs, audits, and documentation.

**Why it Matters:** De-identification protects patient privacy, ensures legal compliance (meeting global/local requirements like HIPAA and GDPR), and enables data-driven healthcare, allowing researchers and clinicians to use rich, real-world datasets without violating confidentiality. It is critical for developing robust AI while maintaining trust.

### **Longitudinal De-identification**

Longitudinal de-identification ensures the consistent de-identification of the same individual across multiple records, encounters, or data types over time.

**Purpose and Principle:** The purpose is to enable patient tracking analysis, support longitudinal research, and preserve data utility while protecting privacy. The core principle is that the **same person is always connected or obfuscated in the same way**, regardless of the data source or encounter dates. This is vital because a patient may have lab results, clinical notes, and imaging across several years, and all records must be consistently linked without exposing true identity.

**Challenges:** Challenges include the variety in data across different sources and handling data from different modalities for the same patient (e.g., unstructured text, tables, scanned PDF images, DICOMs).

### **Obfuscation and Consistent Entity Linking**

**Obfuscation** is the process of replacing sensitive identifiers in medical data with fake but realistic values, guaranteeing that the same individual is always assigned the same fake value across all records and over time.

- **Consistency Requirement:** Consistency must be maintained across all modalities (free text, tables, DICOM). For instance, if patient "John Smith" is obfuscated to "Alex Vidal," this replacement must be identical across all documents and time points for that patient.

- The goal is to protect privacy while still enabling patient tracking over time.

## **GSL De-identification Pipeline Overview**

The Johnson Labs (GSL) approach uses Spark NLP and Healthcare NLP components to build flexible de-identification pipelines.

**Workflow Stages:**

1.  **Input Handling (Multimodal):** The system handles various inputs, including PDFs, DICOM files (metadata and pixel images), clinical text, and structured data like CSVs/tables.

2.  **OCR Integration (If Needed):** If the input is an image-based document (e.g., scan PDF or DICOM image), GSL Visual NLP is used to extract the text.

3.  **NLP Pipeline:** The text is fed into the Spark NLP/Healthcare NLP pipeline, which includes stages like Document Assembler, Sentence Detector, Tokenizer, Word Embedding, and **Named Entity Recognition (NER) models** to detect PHIs.

4.  **Rule-Based Reinforcement:** The detection can be reinforced using rule-based approaches (like contextual parsers or regex matchers) for entities like emails, phone numbers, or age.

5.  **De-identification Annotator:** Detected PHIs are passed to the De-identification Annotator, which supports two modes:

    1.  **Masking:** Replacing PHI with an entity label (e.g., \<PATIENT_NAME\>).

    2.  **Obfuscation:** Replacing PHI with realistic, consistently linked fake values.

**Key Annotator Parameters for Consistency:** The De-identification Annotator allows users to customize the output based on business rules. Key parameters for ensuring robust, consistent obfuscation include:

- consistent_offuscation: Enables consistent replacement (default is true).

- **Fixed Seed:** Setting a fixed seed ensures that running the same pipeline multiple times for the same patient maintains the same obfuscated values.

- offuscate_dates: Enables date obfuscation.

- **Date Placement Offset:** Using set_days (e.g., +10 days) allows the system to maintain the temporal duration between dates in the original document after obfuscation, which is crucial for analysis.

- keep_text_size_for_offuscation: Attempts to ensure the obfuscated text length matches the input length.

- gender_awareness: Uses gender-aware names during obfuscation (affects only names).

- consistent_across_name_parts: Ensures consistency is enforced across different parts of a name. For example, if "John Smith" becomes "Liam Brown," then "John" alone becomes "Liam," and "Smith" alone becomes "Brown".

## **Performance Comparison**

A comparison of performance metrics (F1 score, matching categories) against other healthcare providers (like Amazon, Azure, OpenAI GPT) showed that the GSL solution (Johnson Labs) provides the **best percentage match** and strong F1 scores. For example, GSL detected **Age and Dates with 98% F1 score**.

## **End-to-End GSL Solutions Demo**

The demo illustrated how consistent obfuscation is achieved across various data formats for a single patient, "Martin Chad".

1.  **Unstructured Text:** Clinical notes from multiple encounters were successfully obfuscated. "Martin Chad" was consistently replaced with "Mario Harp". The system preserved the case of the input text and maintained consistency across name parts. The date obfuscation preserved the original date format while applying the fixed day offset.

2.  **Structured Data:** A table (CSV/Excel) for the same patient was processed using the structured de-identification module, yielding the identical, consistent obfuscated values (e.g., age 24 became 28) as found in the unstructured text.

3.  **Scanned PDF:** Because the PDF was scanned, GSL Visual NLP (OCR) was used to extract the text. The PDF identification pipeline successfully applied the same parameters and produced the same consistent obfuscated PHI values ("Mario Harp," age 28) found in the previous structured and unstructured documents.

4.  **DICOM Data:** Visual NLP components processed the DICOM document, which contains both metadata and a pixel image. The patient name and date of birth were consistently obfuscated in the pixel image display and within the DICOM metadata, demonstrating multi-modal longitudinal obfuscation capabilities.

## **Resources**

The presentation concluded by sharing important resources, including the Model Hub (pre-trained models and pipelines), Spark NLP and Healthcare workshop notebooks, documentation for GSL NLP (especially the De-identification Annotator), and GSL live demos.