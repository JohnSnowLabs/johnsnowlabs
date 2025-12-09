# Deliver Safe, Fair & Robust Language Models with the NLPTest Library
Deliver Safe, Fair & Robust Language Models with the NLPTest Library

<https://www.johnsnowlabs.com/watch-deliver-safe-fair-robust-language-models-with-the-nlptest-library/>

<https://youtu.be/_Bd9BJmzUEc>

<img src="/media/image.jpg" title="Video titled: Deliver Safe, Fair &amp; Robust Language Models with the NLPTest Library" style="width:6.3125in;height:3.65625in" />

The following is a detailed summary of the speech provided in the source material, which is an excerpt from the webinar "Deliver Safe, Fair & Robust Language Models with the NLPTest Library.mp4."

The presentation introduces the **NLPTest library** delivered by Johnson Labs, which is designed to help deploy **safe, fair, and robust language models** into production.

### **The Need for NLPTest**

The development of NLPTest was driven by a recognized gap in the industry. While the broader AI and NLP communities have identified significant risks related to **bias** and lack of **robustness** (especially following the rise of public applications like ChatGPT), this awareness has mainly resulted in academic publications. Concrete toolkits or production implementations to address these issues have not widely materialized.

The library's design was inspired by several key academic works:

- **CheckList Paper (Ribero and colleagues):** This was the most important inspiration and the starting point for testing capabilities in NLP. The paper demonstrated that when applying certain **perturbations** to input texts, NLP models often fail to maintain consistent predictions. This inspired the implementation of an initial Python library.

- **BBQ Paper (Parish and colleagues):** This paper, released recently, offered concrete examples and applications regarding **bias**. It showed that by creating perturbations related to biases (e.g., race, gender, disability, religion) during question-answering tests, the final answer of a model could be changed a large percentage of the time.

- Other papers addressed biases related to **ethnicity** (especially in the clinical world) and **data leakage** (a crucial topic in clinical NLP).

### **Core Principles of the Library**

The development of NLPTest was guided by three central concepts:

1.  **Thorough Model Testing:** The library promotes the mindset of carrying out unit tests, similar to how software engineers test software. This goes beyond merely obtaining accuracy metrics, which is the standard practice before deployment.

2.  **Caution Against Academic Models:** The creators warn against using or reusing academic models directly in production. Publicly released research models are often built only for research purposes and have not undergone the "test of the real world," which can cause models to break in production.

3.  **Comprehensive Aspect Testing:** NLPTest aims to test aspects beyond mere accuracy, including **robustness, bias, fairness, toxicity, efficiency, safety, and data leakage**.

### **Features and Accessibility**

The NLPTest library is summarized by three main features:

- **Simplicity:** It is extremely simple to use. After a pip install NLP test, users can automatically generate and run test cases in as little as three lines of code.

- **Comprehensiveness:** It includes more than 50 different test types and covers all popular NLP tasks, such as token classification, text classification, question answering, and tasks involving LLMs.

- **Open Source:** It is licensed under the Apache 2.0 license, making it commercially usable. It is also easily extensible, allowing users to add their own test types or test other tasks.

### **Supported Frameworks**

NLPTest is built as a toolkit to support most major and popular NLP frameworks, including LLMs:

- **Traditional NLP:** Johnson Labs (Spark NLP), Hugging Face Transformers, and spaCy.

- **LLMs:** OpenAI, Cohere, AI21 Labs, and the Azure OpenAI API, all built on top of LangChain supported APIs.

### **The Disruptive Workflow**

The library seeks to disrupt the standard model development process, which traditionally prioritizes accuracy until deployment.

The NLPTest workflow integrates unit testing early:

1.  **Training and Generation:** Once a model is trained, the library automatically generates unit test cases focusing on bias, robustness, accuracy, and fairness.

2.  **Testing and Reporting:** The tests are run, and a report is generated showing whether various test categories (like bias or robustness) passed or failed.

3.  **Failure Identification and Risk Mitigation:** A failing test category (e.g., robustness failure due to inability to handle typos) signals that the model is not ready for production. Deploying a failing model carries risks, such as making headlines for discriminatory behavior (bias) or being unreliable in critical applications (robustness).

4.  **Automatic Data Augmentation:** Instead of simply reporting failure, NLPTest addresses the issue by automatically **augmenting the model's training data** (the test set must be kept separate). This augmentation is performed in a single line of code.

5.  **Retraining and Retesting:** The user then retrains a new model using this augmented data. This cycle continues until all tests pass, allowing the user to confidently release the model.

### **Example Test Cases**

The library generates various types of test cases:

- **Bias Testing (Ethnicity/Sentiment):** For a text classification model, a test might compare the model's sentiment prediction on "Jonas Smith is flying tomorrow" (neutral) versus a perturbed version, "Abdul Karim is flying tomorrow". If the second sentence yields a negative sentiment, it indicates clear bias.

- **Robustness Testing (Typos):** The library adds typos (e.g., changing 'O' to 'U' in "Wang Lee is a doctor") to ensure that a Named Entity Recognition (NER) model still correctly detects the name as a person.

- **Bias Testing (Name Replacement/NER):** A test might replace a name like "Wang Lee" with "Juan Moreno" (a Hispanic name). If the model fails to detect "Juan Moreno" as a person, it indicates a bias issue, suggesting the training data needs to be more representative of that ethnicity.

### **Customization and Configuration**

Test standards are entirely customizable. Users can set specific minimum pass rates (e.g., 95% for robustness) based on the importance of that aspect for their application. Conversely, if robustness is not critical, the standard can be lowered. Configuration can be handled through a dictionary passed to the configure method or, as recommended, through a config file.

### **Demonstration and Resources**

A tutorial example demonstrated testing Question Answering using the harness with GPT-3.5 turbo on the tiny BULL test set. The process involves defining the model parameters and desired pass rates, calling generate.run to execute the tests, and calling report to summarize results (e.g., showing a 96% pass rate for lowercasing/uppercasing tests against a set 70% threshold).

The presentation concludes by highlighting key resources:

- **Website:** nlpest.org (provides documentation, supported hubs, and tutorials).

- **GitHub Repository:** Provides the codebase, enables collaboration with contributors, and hosts a discussions page for release announcements and user questions.

- **Community Slack Channel:** Allows users to interact with the team and get answers.