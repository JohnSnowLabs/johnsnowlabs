# Text classification and named entity recognition with BertForTokenClassification & BertForSequenceClassification
Text classification and named entity recognition with BertForTokenClassification & BertForSequenceClassification

https://www.johnsnowlabs.com/text-classification-and-named-entity-recognition-with-bertfortokenclassification-bertforsequenceclassification/

<https://www.youtube.com/watch?v=B3xB9gaBosw>

<img src="/media/image.jpg" title="Video titled: Text classification and named entity recognition with BertForTokenClassification" style="width:6.3125in;height:3.65625in" />

The following is a detailed summary extracted from the transcript of the YouTube video "Text classification and named entity recognition with BertForTokenClassification," presented by Luca, a data scientist at John Snow Labs.

### **Overview and Key Tasks**

The presentation focuses on two Natural Language Processing (NLP) tasks: **token classification** and **text classification**, utilizing two BERT-based models: BertForTokenClassification and BertForSequenceClassification.

#### **1. Token Classification (Named Entity Recognition - NER)**

Token classification is also known as Named Entity Recognition (NER). In this task, a sequence of words or a sentence is fed into the system. The goal is to detect single words or groups of words (tokens) relevant to a specific use case. Each token within the sentence is assigned a tag.

- **Example:** In a sentence, "Mark Zuckerberg" might receive a **person** tag, while "Facebook" receives an **organization** tag.

#### **2. Text Classification (Sequence Classification)**

Text classification involves attempting to classify an entire sentence or a full document.

- **Example:** The task can be classifying whether a message is **spam or not spam**.

### **Introduction to BERT-Based Models**

The tasks are performed using BERT-based models.

#### **BERT Architecture and Breakthrough**

- **Definition:** BERT stands for **Bi-directional Encoder Representations from Transformers**. It was introduced in a paper submitted to arXiv in 2018 by Jacob Devlin and colleagues at Google.

- **Architecture:** BERT is a language model built with a **multi-layer bi-directional transformer architecture**, comprising stacked encoder blocks.

- **Bi-directionality:** The breakthrough of BERT was its ability to look at context **bi-directionally**. Previously, large language models like OpenAI's GPT could only look to the left of each token. BERT allows each token to attend to tokens on both the left and the right side.

- **Effectiveness:** This functionality allows pre-trained BERT models to perform well at a wide range of tasks, including token and text classification, usually requiring only an additional output layer without substantial architecture modifications.

#### **Model Modifications for Specific Tasks**

- **For Token Classification:** The base language model is restructured simply by **slapping a linear layer on top of the hidden state outputs**. This allows the model to classify each token and assign a class (e.g., 'O' for no label, or 'Person' label).

- **For Text Classification (Sequence Classification):** The sequence of tokens is fed into the model with a special **\[CLS\] token (Classification token)** added at the start. A linear layer is then placed directly on top of the output corresponding to this \[CLS\] token to classify the entire text sequence.

### **Using BERT Models within Spark NLP**

These models are integrated for use within the Spark NLP library.

#### **Spark NLP Library Details**

Spark NLP is a highly popular open-source NLP library built on top of Apache Spark. This foundation provides the unique ability to **scale on clusters and process huge amounts of documents**. It is actively maintained by John Snow Labs, is the most used library in the enterprise sector, and boasts nearly two million downloads per month. Spark NLP includes **over 6,000 pre-trained models** across over 250 languages, including various transformer models like BERT.

#### **Assembling the Pipeline**

The core component of Spark NLP is assembling components into a **Spark pipeline**.

##### **1. Pipeline for Token Classification (NER)**

A typical pipeline involves:

1.  **DocumentAssembler**: Takes a text column as input.

2.  **Tokenizer**: Tokenizes the text.

3.  **BertForTokenClassification**: A pre-trained model (e.g., one trained on the CoNLL 2003 dataset, which detects basic NER classes like person, locations, organizations, and miscellaneous). This model takes the token and document columns as input and outputs an NER column.

4.  **NerConverter**: This optional but often-used component converts the raw output, which is in IOB format (e.g., B-Person, I-Person), into a more manageable **chunk format** (where a group of words like "John Parker" is assigned a single chunk called "Person").

The pipeline is assembled, fitted to sample text, and then used to transform the data to obtain results (e.g., recognizing "John Parker" as a person and "New York" as a location).

##### **2. Pipeline for Sequence Classification**

This process is almost identical to token classification:

1.  **DocumentAssembler**.

2.  **Tokenizer**.

3.  **BertForSequenceClassification**: A pre-trained model (e.g., one trained to identify whether IMDb movie reviews are positive or negative).

The assembled pipeline can take sample texts (e.g., "I really like that movie" and "The last movie i watched is awful"), fit them to the pipeline model, and generate predictions (Positive and Negative, respectively).

### **Model Availability and Custom Training**

All pre-trained models, including sequence and token classification models, are available on the **NLP Model Hub**. Model cards on the hub provide detailed explanations, usage guidelines, and what the models should be used for.

John Snow Labs also offers a licensed library, **Spark NLP for Healthcare**, which is specific to healthcare and contains many pre-trained models for various healthcare-specific NLP tasks.

For users who need to **train custom transformers**, this can be done using PyTorch or TensorFlow, often along with the Hugging Face transformers library or its Trainer class. These newly trained models can then be imported into Spark NLP, enabling them to scale effortlessly. Instructions and notebooks for importing models into Spark NLP are available in a discussion thread on the open-source repository.