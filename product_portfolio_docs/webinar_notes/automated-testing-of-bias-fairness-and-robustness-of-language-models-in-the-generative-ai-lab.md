# Automated Testing of Bias, Fairness, and Robustness of Language Models in the Generative AI Lab
Automated Testing of Bias, Fairness, and Robustness of Language Models in the Generative AI Lab

<https://www.johnsnowlabs.com/automated-testing-of-bias-fairness-and-robustness-of-language-models-in-the-generative-ai-lab/>

<https://youtu.be/4hTXXZUCIF0>

<img src="/media/image.jpg" title="Video titled: Automated Testing of Bias, Fairness, and Robustness of Language Models in the Generative AI Lab" style="width:6.3125in;height:3.65625in" />

The speech provided in the sources, delivered by David Jaini, a senior data scientist at John Snow Labs, focuses on performing **automated testing of bias, fairness, and robustness of language models** using the Generative AI Lab and the associated library, LangTest.

The presentation covers an introduction to John Snow Labs, an overview of the Generative AI Lab, an introduction to LangTest, and a practical example demonstrating how to combine these tools to perform these evaluations on models.

### **John Snow Labs and Products**

John Snow Labs is the company behind **Spark NLP**, which is cited as the top used open-source library for NLP in the industry, having been downloaded over 110 million times. The company offers various products, including the medical chatbot, Visual NLP, Healthcare NLP, and John Snow Labs NLP, which helps clients with domain-specific analysis. The key products highlighted for model evaluation are the Generative AI Lab and LangTest.

### **Motivation for Holistic Evaluation**

The speaker emphasizes that current evaluation efforts must move beyond simply checking for accuracy or top performance. Holistic evaluation is necessary because models can exhibit significant weaknesses under minor changes or biased behavior.

- **Robustness:** Models can fail drastically when small changes are introduced to the input prompt, such as adding a few typos or changing the text casing. For instance, adding two typos to a math question prevented the model from replying correctly. In another example, changing words to synonyms (preserving meaning) caused a sentiment model's output to switch from negative to positive.

- **Bias and Fairness (Crucial for Healthcare):** It is critical to measure how biased or fair a model is before deploying it, especially in fields like healthcare. Simulations show that models may predict specific medical conditions for certain racial or gender groups far more often than the real-world distribution suggests, indicating the model is biased against reality.

### **Key Evaluation Tools**

**1. Generative AI Lab (No-Code Platform):** This platform is a no-code environment featuring a user interface (UI) used to train, tune, and evaluate models. It supports data annotation for tasks like entity recognition and classification, and it integrates with API-based Large Language Models (LLMs). It allows users to manage the entire cycle of model development without needing a deep technical background or being a dedicated data scientist.

**2. LangTest (Python Library):** LangTest is a Python library designed for the **holistic evaluation** of LLMs. While it started with bias, robustness, accuracy, and fairness, it has grown to include capabilities for measuring **toxicity, security**, and **domain-specific tests** (like those for the clinical or healthcare domain).

A crucial capability of LangTest is **data augmentation**. If a model performs poorly on a specific test (e.g., robustness), LangTest can augment the training data, focusing on those weaknesses to improve the model's capabilities in that area.

### **Detailed Definitions of Core Tests**

The speech provides detailed explanations of three core evaluation categories: robustness, fairness, and bias.

| **Test Category** | **Description** | **Expectation & Failure Condition** | **Examples of Tests** |
|:---|:---|:---|:---|
| **Robustness** | Measures the model's ability to maintain the output despite small, non-meaning-altering changes to the input text. | The output should remain the same; the test fails if the output changes after the input modification. | Adding typos, changing text casing, randomizing words, adding/removing words or punctuation, abbreviations, common OCR errors (e.g., 'L' changed to '1'), or speech-to-text confusion errors. |
| **Fairness** | Checks the performance (e.g., accuracy) of the model across different demographic groups. | Performance metrics (like accuracy) when evaluated on text regarding one group (e.g., male) should be similar or the same as when evaluated on another group (e.g., female). | Measuring F1 scores for Named Entity Recognition (NER) models or Rouge scores for Question Answering/Summarization models across gender or other groups. |
| **Bias** | Measures if the output changes when demographics are swapped in the input text. | The output is expected to remain the same if demographics are merely changed. | Changing person names, typically associated with different religious (e.g., Christian to Muslim) or racial/ethnic backgrounds (e.g., Black, Hispanic, Asian, White). Bias testing focuses on gender, economic, racial/ethnic, and religious aspects. |

### **Demonstration and Analysis Workflow**

The demonstration utilized an NER model trained on a small set of **20 synthetic data examples** using a Glove 100 Dimension embedding, emphasizing the model had "lots of rooms for Improvement" due to the limited training data.

#### **1. Setting Up Tests**

The user interface allows the definition of custom entities (e.g., name, age, gender). The user can customize **test suits** by selecting specific robustness tests (e.g., OCR typos, adding typos, changing synonyms) and setting parameters like the passing rate threshold and the probability of changing words in the data.

#### **2. Analyzing Results**

- **Accuracy Test:** A previous accuracy test (Micro F1 score) passed because the model's performance (89%) exceeded the selected minimum pass rate (65%).

- **Bias Test Failures:** The detailed report showed bias failures. When the name "Ahmed" was changed to "Charles" (a first name commonly used by Asian people), the model failed to identify "Charles" as a name entity, suggesting the model's performance might be better in specific population subsets.

- **Fairness Test:** Fairness tests check minimum and maximum score requirements for groups (e.g., male/female). The small, under-trained model failed the minimum score requirement, though it passed the maximum score requirement.

- **Speed Test:** The model successfully passed the speed test by processing 33.7 tokens per second, which was above the required minimum of 10 tokens per second.

- **Robustness Test Failures (OCR Typos):** The newly generated robustness test revealed that **OCR typos severely impacted the model**. In one instance, changing the entity "his" (gender) to "h1s" (with the typo) caused the model to incorrectly reclassify the entity as a "name". Conversely, adding small typos or changing synonyms resulted in the model being fairly robust.

#### **3. Iterative Improvement**

The results guide the next steps for model improvement. Identified weaknesses, such as poor robustness against OCR typos, can be addressed by **augmenting the data** to focus on improving that specific weakness. Users can also annotate more data to improve the model generally. The platform allows users to apply tags to specific tasks and rerun tests only on those subsets to track the impact of retraining or fine-tuning efforts.