# Automated Text Generation & Data-Augmentation for Medicine, Finance, Law, and E-Commerce
Automated Text Generation & Data-Augmentation for Medicine, Finance, Law, and E-Commerce

<https://www.johnsnowlabs.com/automated-text-generation-data-augmentation-for-medicine-finance-law-and-e-commerce/>

<https://www.youtube.com/watch?v=JxPXj0AKgss>

<img src="/media/image.jpg" title="Video titled: Automated Text Generation &amp; Data-Augmentation for Medicine, Finance, Law, and E-Commerce" style="width:6.3125in;height:3.65625in" />

This detailed summary extracts and synthesizes the speech presented in the video "Automated Text Generation & Data-Augmentation for Medicine, Finance, Law, and E-Commerce."

The presentation was delivered by **Christian Kasim Noon**, a lead data scientist at John Snow Labs. The focus of the tutorial is demonstrating how to apply **automated text generation** and **data augmentation techniques** to various fields, including **medicine, finance, law, and e-commerce**, using the **NLU library**.

### **Overview of the NLU Library**

The NLU library is a simple wrapper built around **Spark NLP**. Spark NLP is highlighted as a big data library focused on being highly accurate, scalable, and fast. In five years since its release, it has become the most used NLP library in the industry, accumulating millions of downloads and recognition from technology experts.

Key features of the NLU library and Spark NLP include:

- Coverage of **over 9000 models** and **over 200 languages**.

- Inclusion of advanced Transformer and deep learning architectures, such as all the **bertology models**.

- Handling simpler tasks like tokenization and spell checking.

- All features are backed up by peer-reviewed papers.

- NLU allows users to access all these capabilities in just **one single line of code**.

To use the library, only two functions are essential: nlu.load(model_name), which returns a model object, and model_object.predict(), which runs the prediction. The library works with all Pythonic data structures, including strings, lists of strings, Pandas DataFrames, and big data structures like Spark, Ray, or Tusk DataFrames.

### **Text Generation: Theory and Control**

Text generation is a capability often seen in Natural Language Generation (NLG) systems, such as voice assistants like Alexa, Cortana, Google Assistant, and Siri. These systems are capable of generating creative stories, poetry, narratives, and even fake news.

The presentation uses **GPT-2**, the generative model from OpenAI, for demonstration purposes.

#### **Language Models and Probability**

Generating text relies on understanding **language models (LMs)**. An LM is defined as a **probability distribution** where the sample space (\$\Omega\$) is the set of words (or vocabulary) the model was trained on. The LM models the distribution of words in human language and their conditional dependencies (e.g., the probability of a word occurring given the preceding text).

Text generation is achieved by **sampling** (drawing elements) from this probability distribution. The process involves using the conditional probability \$P(x \text{ given } y)\$ to generate a token, appending that new token to the sequence, and repeating the process until a desired length is reached.

#### **Sampling Algorithms and Parameters**

Initial demonstrations showed that using the default settings for generation resulted in **repeating generations** because it utilized an **Arg Max based sampling algorithm** which simply picked the token with the highest probability. By setting the do_sample parameter to **true**, generations become random and non-repetitive.

To gain more control over the generation process, the main techniques discussed are sophisticated sampling methods:

1.  **Top K Sampling:** The model selects a token randomly only from the top K most probable tokens.

2.  **Top P Sampling (Nucleus Sampling):** The model selects tokens whose collective probability sums up to at least P.

3.  **Temperature Parameter:** This parameter reshapes the soft marks that define the sample distribution.

Intuitively, **higher values** for K, P, and Temperature lead to a model that is more **diverse, risky, and creative**, but also potentially less coherent and logical. **Lower values** result in generations that are more **generic and logical**.

#### **Prompt Engineering**

**Prompt engineering** is defined as the art of finding the best input texts (prompts) that instruct the model to generate text satisfying specific demands. By carefully conditioning the model (e.g., providing an example list of movies before asking it to continue), the distribution is reshaped so that relevant tokens (like movie titles and numbers) have a higher probability of occurrence, avoiding "garbage tokens".

### **Domain-Specific Text Generation Use Cases**

GPT-2 can be applied across numerous industries for both creative and structural tasks:

- **Structured Financial Data:** Text generation can be used to generate labels or descriptions based on historical price data (e.g., weekly stock prices). When applying this, parameters like temperature, top P, and top K should be set **lower** to ensure the model stays within a narrow set of appropriate tokens.

- **Medicine:** The model can generate **treatment recommendations** for specific patient problems (e.g., predicting that diarrhea can be treated with "sodium chloride").

- **Copywriting/E-Commerce:** Generating marketing texts or inspirational product descriptions for a startup's inventory (e.g., for hoodies, soap, or beard products).

- **Product Recommendation:** Generating lists of recommendations for items like movies, video games, or books by supplying a partial list as a prompt.

- **Creative Writing (Lyrics and Literature):** GPT-2 can generate new song lyrics that are catchy and rhymey, or even generate entire books or rewrite favorite movie scripts.

- **Code Generation:** The model can be used to describe existing code or generate new Scala or Python code, similar to tools like GitHub Co-Pilot.

### **Leveraging Generative Models for Data Augmentation**

Data augmentation involves using large language models, which are trained on nearly the entire web, to generate sophisticated and realistic text. This generated text can be used as synthetic **training data** for NLP problems, effectively increasing the dataset size. This process improves the accuracy of smaller classifier models that are trained afterward.

#### **Augmentation Methodology and Experimentation**

A simple augmentation method demonstrated is **concatenating or cutting off a piece of text and prefixing it with the label** (e.g., label + text) and then asking the model to generate more words.

The experiments compared a "vanilla model" (trained on the standard, limited data) against an "augmented model" (trained on the combined real and synthetic data):

1.  **Preparation:** A baseline classifier was trained on a limited news dataset (100 examples per class).

2.  **Prompting:** Prompts were engineered by taking the label and appending the first 15 characters of the original data (e.g., Sci News headline Company claims...).

3.  **Generation:** The model generated synthetic training examples (fake news).

4.  **Cleaning:** **Crucially, the prompt containing the label was split off and removed** from the augmented text before training the new classifier to prevent label leakage.

5.  **Training & Evaluation:** The augmented classifier was trained and evaluated.

#### **Results Across Domains**

The results showed that data augmentation generally led to accuracy improvements on the test data set:

- **News Data:** The augmented model achieved a major improvement in the Business class (from around 64% accuracy to 70% accuracy) and showed improvements in Sci-Tech.

- **Finance Data (Fake Tweets):** Showed a minor improvement.

- **Medical Data (Journal Reports):** Showed significant improvements, including a 14% and 10% increase in two journal classes.

- **Legal Data (Contract Clauses):** Showed a nice improvement of 4% overall and almost 20% in specific classes like "base salary" and "investment".

These models can be further scaled using big data clusters or combined into an ensemble classifier using a voting algorithm.

### **Conclusion: Other Language Models**

Beyond GPT-2, other large language models are available for text generation tasks:

- **Google's T5:** Useful for summarization, answering questions, or generating SQL text.

- **Microsoft's Marian NMT:** Used for translating between 200 languages.