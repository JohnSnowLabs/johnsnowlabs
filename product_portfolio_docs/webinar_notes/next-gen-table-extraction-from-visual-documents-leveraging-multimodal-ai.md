# Next-Gen Table Extraction from Visual Documents Leveraging Multimodal AI
Next-Gen Table Extraction from Visual Documents Leveraging Multimodal AI

https://www.johnsnowlabs.com/watch-webinar-next-gen-table-extraction-from-visual-documents-leveraging-multimodal-ai/

<https://youtu.be/7FMzD4AYOCY>

<img src="/media/image.jpg" title="Video titled: Next-Gen Table Extraction from Visual Documents: Leveraging Multimodal AI" style="width:6.3125in;height:3.65625in" />

The speech provided in the YouTube transcript excerpts details a webinar on **Next-Gen Table Extraction from Visual Documents: Leveraging Multimodal AI**, presented by Alberto from the Visual NLP team at John Snow Labs.

The presentation covered the following key areas:

### **1. Introduction to Visual NLP and Architecture**

The webinar introduced Visual NLP, outlining the process of table extraction and the components of the product.

- **Foundation:** The Visual NLP architecture relies on **Apache Spark** for data distribution and parallel processing. The Visual NLP Library sits atop Spark.

- **Data Ingestion:** The library supports various formats, including **PowerPoint, Microsoft Word, digital and scanned PDFs, and images**.

- **Preprocessing:** The ingestion layer includes image preprocessing features like **denoising** and **skew correction** to enhance OCR quality.

- **Features:** Higher-level multimodal features include visual document classification, visual document NER, visual question answering (VQA), and the core topic: **table detection and recognition**.

### **2. The Table Extraction Problem and Modular Pipeline Approach**

Table extraction aims to recover data found in a specific structure, keeping the text belonging to the same cell together, and maintaining the relations between data pieces.

- **Approach:** John Snow Labs builds pipelines from **interchangeable parts**. This flexibility allows users to customize stages for data ingestion, OCR, and table detection.

- **Core Components:**

  - **Table Identification:** Identifying the tables within a document is crucial because it saves computing power by focusing only on the areas of interest.

  - **OCR:** Necessary for scanned documents or digital images. Users can choose between end-to-end solutions (like Image to HCR) or independent text detection followed by an OCR stage.

  - **Model Selection:** Users can select different models based on their needs, such as a **handwritten OCR model**, a large model, or a super small/fast model if accuracy is less critical.

  - **Cell Detectors:** Various cell detectors are available, differentiated by their accuracy and computational cost.

- **Metrics and Resources:** Metrics for each pipeline stage are constantly updated. All examples and resources shown during the webinar, including notebooks and sample images, are available in the **Spark NLP Workshop repository** under the webinars folder.

### **3. Code Examples and Pipeline Structures**

The presentation detailed how to construct and run pipelines for table extraction.

- **Simple Pipeline Example (Pre-trained):** This pipeline downloads a pre-trained model from the Model Hub. It applies the pipeline to the image and uses the display tables utility function to render the structured result (HTML in a browser environment). The pipeline is noted for being **super fast**.

  - **Output:** The result is a **data frame** containing useful information like the table index and the table's location coordinates.

  - **Stages:** A basic pipeline consists of **Binary to Image**, **Image to HCR** (text coordinate rendering), **Cell Detector**, and **HCR to Text Table** (which combines the elements).

- **Complex Pipeline Example (Real-life Use Case):** This scenario addresses extracting a table from a larger document.

  - The process involves using an **Image Table Detector** to crop the region of interest.

  - An **Image Split Region** component uses that information to create a new image containing only the table.

  - The remaining stages (converting to HCR, Region Cell Detector, HCR to Text Tables) are then applied to the cropped image.

- **CSV Output:** To generate a proper CSV file, the **HCR to Table Transformer** must be configured by setting the table output format to csv. The library automatically handles details like adding quotes to cells that contain commas.

### **4. Alternative Approach: Document Visual Question Answering (DocVQA)**

Visual Question Answering (VQA) provides an alternative to extracting the entire table, focusing instead on extracting specific insights expressed as questions over the image.

- **Functionality:** DocVQA answers questions about a document where the visual structure (like a table) is essential to the answer.

- **Nature:** This is an **extractive task**; the model only returns information explicitly present in the document. It cannot answer questions requiring calculation or synthesis (e.g., counting rows).

- **VQA Pipeline:** A VQA pipeline uses **Binary to Image** and the **Visual Question Answering** model (which requires picking a pre-trained checkpoint).

- **Confidence Scores:** The model provides **confidence scores** with the answers. If a question is unrelated to the document content (e.g., asking about Michael Jackson's records on a poverty report), the answer returned will have a **low confidence score**, which allows users to filter out irrelevant responses.

### **5. Future Directions and Q&A Highlights**

The session concluded by outlining future plans and addressing audience questions.

- **Next Steps:** John Snow Labs plans to continuously add new models and improve metrics. New output formats for tables, such as **JSON and XML**, are coming soon (currently only CSV is natively supported).

- **Custom Models:** The team plans to integrate table recognition training capabilities into the **NLP Lab** tool. This will allow users to train custom models to handle complex layouts, such as tables with tricky borders, no borders, or shaded backgrounds, ensuring maximum accuracy.

- **Borderless Tables:** The presenter confirmed that processing borderless tables requires explicitly including the **cell detector** in the pipeline.

- **Comparison:** The Visual NLP models are reported to be generally **more accurate** and offer a more user-friendly setup than open-source tools like Tabula or Camelot. They also offer better scalability and security for enterprise deployment compared to open-source solutions. When compared to cloud providers' OCR offerings, JSL provides similar or higher accuracy while being generally **cheaper**, as licensing is cluster-based rather than per-page.

- **VQA Architecture:** The VQA models primarily utilize **encoder-decoder architectures**, including models like Donut and Pixel Structure.

- **Platform Support:** The libraries fully support Databricks, including GPU usage, as John Snow Labs is a partner.

- **DocVQA Scope:** DocVQA is not limited to tables; it can handle answering questions about **charts, forms, and other graphic visualizations** where the visual layout is relevant to understanding the content.