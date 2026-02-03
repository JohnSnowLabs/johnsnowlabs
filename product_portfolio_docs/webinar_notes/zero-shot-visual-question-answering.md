# Zero-Shot Visual Question Answering
Zero-Shot Visual Question Answering

<https://www.johnsnowlabs.com/watch-zero-shot-visual-question-answering/>

<https://youtu.be/hgsRokzYzzY>

<img src="/media/image.jpg" title="Video titled: Zero-Shot Visual Question Answering" style="width:6.3125in;height:3.65625in" />

This detailed summary extracts and organizes the key points presented in the webinar transcript regarding Zero-Shot Document Visual Question Answering (VQA). The speaker is **Alberto**, the leader of the visual NLP team at John Snow Labs (JSL).

### **I. Introduction and Defining Document VQA**

The webinar focuses on **Document Visual Question Answering (VQA)**, particularly the zero-shot flavor applied to documents.

**A. Document VQA Task Description** Document VQA is comparable to question answering in Natural Language Processing (NLP), but it specifically requires the model to **make sense of visual clues** found within the document, such as understanding a graph, chart, or table, to formulate an answer.

- **Extractive Task:** The version discussed is an extractive task, meaning the answer returned by the model must come directly from the text explicitly present in the document.

- **Multi-Step Reasoning:** Solving these problems often involves multi-step reasoning, such as understanding the indications and notes on how to read a graph before extracting the information requested by the question.

- **Technology Blend:** VQA requires a mix of computer vision (to make sense of the image) and NLP (to process the question and relate it to the image). This technique can be applied to other tasks like extracting key values or table processing.

**B. Zero-Shot Concept** The idea behind **zero-shot** is training a model to reason about things it has not explicitly encountered during the training phase. For instance, in a classification problem, the model may be expected to return labels it was not trained on.

**C. Intuition (Not Magic)** Zero-shot is explained as achievable, not magic, by relying on the properties of embeddings.

- If an object detection model is trained using labels like "gray duck," "red bird," and "white cat", it can often extrapolate to unseen combinations like a "white pigeon".

- Since word embeddings (e.g., word2vec or GloVe) place "pigeon" geometrically close to "bird," and the model has seen "white" and "bird," it is capable of understanding what a "white pigeon" is.

- Similarly, "cat" and "dog" embeddings are similar because they often share the same context, appear in the same regions on images, and share lower-level visual features like hair, allowing the model to potentially identify a "gray dog" even if that specific label was not used in training.

### **II. Examples and Visual Importance**

Visual clues are crucial for VQA. For example, interpreting a pyramid diagram requires understanding that when moving up the pyramid, issues become **less critical**.

Another example involves extracting specific data points from tables. To answer "What is the acceptable hemoglobin level," the model must understand the organization of rows and columns, relate the row title ("hemoglobin level") to the column title ("acceptable"), and return the corresponding value (e.g., 14.0).

### **III. Common Architectures**

The field of VQA architecture is an active area of research. Architectures are typically classified based on pre-training objectives, attention types, and the order in which data is processed. The two general types are:

**A. OCR plus Decoder** This type utilizes features derived from explicit OCR processing. They generally use three types of features:

1.  **Layout:** Position information, including bounding boxes (\$x_0, y_0, x_1, y_1\$).

2.  **Text:** Text extracted from the OCR process.

3.  **Image:** Patches taken from the image itself. An instance of this architecture, similar to the layers of LaMDA, uses 2D position embeddings (bounding boxes) combined with text and image embeddings (which may come from a model like Fast R-CNN).

**B. Encoder-Decoder** This is viewed as a cleaner and more simplified architecture. It involves encoding all visual clues using a **Visual Transformer** and then decoding.

- **OCR-Free (\$OCR^3\$):** An example is \$OCR^3\$, which does not rely on explicit OCR. It uses a **Swin Transformer** as a visual encoder and **BART** as a language model decoder.

- **Process:** The image is fed to the encoder, and the question is fed to the decoder. The answer is returned simultaneously as a result of the same decoding process that took the question.

### **IV. Practical Considerations for Real-World Pipelines**

When building real-life VQA pipelines, several challenges must be addressed:

1.  **Question Formulation:** Creating the questions can be difficult, as the creator often possesses existing domain knowledge (e.g., knowing a zip code is on an envelope).

2.  **Document Screening:** To apply the technique effectively to millions of pages, it is necessary to **screen the documents first** and apply the questions only to a smaller, selected number of relevant pages.

3.  **Rephrasing Questions:** It is helpful to rephrase questions. Asking variations like "What is the total amount for the invoice?" versus "What is the amount that was billed?" can result in different-and sometimes better-answers.

### **V. John Snow Labs (JSL) Visual NLP Implementation**

The practical examples use the JSL **Visual NLP** library, also known as **SparkOCR**, which utilizes the distributed capabilities of Apache Spark. The library handles image pre-processing (skew correction, denoising), text detection, table detection/recognition, visual document classification, and document VQA.

**A. Example: Table Question Answering (Stock Reports)** The first example uses reports related to company executives acquiring or selling stock.

- **Pipeline:** The process involves converting PDFs to images, using an **Image Table Detector** to identify table regions, and then feeding questions (e.g., "What is the number of acquired units?") to a pre-trained VQA model.

- **Results:** The pipeline successfully returns values associated with the questions (e.g., units of stock bought or sold, price per unit). Although some irrelevant information might be returned, filtering rules can be applied, such as checking for numbers/dollar signs or using confidence scores.

**B. Example: Invoice Processing** The second example focuses on extracting the total amount invoiced from documents, sourced from the 40K RBL CV dataset.

- **Pipeline:** This uses a **Visual Document Classifier** to ensure the documents are invoices. Three varied questions were used (e.g., "What is the total amount invoiced...?" vs. "What is the dollar amount mentioned...") and fed to the VQA model.

- **Finding on Rotation:** While the pipeline accurately extracted total amounts (e.g., 2683), the results are **"no good"** when documents are rotated 90 degrees. The JSL library offers tools to correct for rotation, which would improve results.

### **VI. Conclusion and Roadmap**

The speaker provided a license for attendees to run the demonstration notebooks themselves on platforms like Colab.

Regarding JSL's future roadmap in VQA:

- They are working on new **specialized models** for specific use cases, such as chart understanding or genetic testing.

- They are considering models that explicitly use **OCR** features, rather than only being OCR-free.

- Continuous work is focused on improving model **accuracy**, **performance**, and reducing **memory consumption**, as these models are currently expensive to run.

- The **NLP Lab** product allows users to do training, data preparation, and download models derived from Visual NLP for use on their own systems.