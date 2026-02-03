# Comparing Frontier LLMs on Analyzing Clinical Narratives
Comparing Frontier LLMs on Analyzing Clinical Narratives

https://www.johnsnowlabs.com/comparing-frontier-llms-on-analyzing-clinical-narratives/

<https://youtu.be/7LfLcGsFyvk>

<img src="/media/image.jpg" title="Video titled: Comparing Frontier LLMs on Analyzing Clinical Narratives" style="width:6.3125in;height:3.65625in" />

The speech provided in the source is a presentation detailing recent benchmarks and comparisons of various **Frontier Large Language Models (LLMs)** and **Clinical Natural Language Processing (NLP) APIs** on tasks specific to **clinical and biomedical text analysis**. The presentation was led by David Albby, CEO of John Snow Labs, and Vasel Kaman, CTO.

The overall goal was to demonstrate how John Snow Labs' (JSL) Medical LLMs perform against top commercial LLMs and leading healthcare-specific cloud APIs in terms of accuracy, relevance, factuality, and cost for production-grade deployments.

## **Part 1: Frontier LLM Benchmarks (Presented by David Albby)**

The first part of the presentation focused on a **blind evaluation** of LLM performance on complex tasks, assessed directly by medical doctors.

### **Models and APIs Compared**

The benchmarks included five commercial LLMs and NLP providers:

| **Category** | **Provider** | **Model/Service** |
|:---|:---|:---|
| **Frontier LLMs** | OpenAI | **GPT-4.5** (newest, highest-end model) |
|  | Anthropic | **Claude 3.7** (frontier, most-used model) |
| **Healthcare APIs** | AWS | Amazon Comprehend Medical |
|  | Microsoft Azure | Text Analytics for Health |
|  | Google Cloud | Healthcare Natural Language API |
| **JSL LLMs** | John Snow Labs | **Medical LLM Medium** (focus of the newer benchmarks) |

### **John Snow Labs' Differentiators**

JSL models emphasize three main advantages for the healthcare and life science community:

1.  **State-of-the-Art Accuracy:** JSL's sole mission is to maintain state-of-the-art performance for healthcare-specific tasks, achieved by constantly integrating new research and ideas into production-grade releases every two weeks.

2.  **Privacy and Compliance:** JSL models run **privately within the user's infrastructure** (VPC, on-premise, or air-gap environment). Data is never sent to JSL or any third party, making it designed for high-compliance deployments in healthcare and life science.

3.  **Pricing Model:** JSL charges **per server per year**, not per token. This model is designed for scalable deployments. While commercial APIs may be cheaper for very small tasks (e.g., one or two pages), analyzing large patient populations (e.g., five million patients) using commercial APIs can cost "high eight figures". JSL enables scaling on a much lower budget by combining licensing and user-hosted hardware costs for fair comparison.

### **Evaluation Methodology**

JSL evaluated models across multiple dimensions, acknowledging the need to assess clinical accuracy, relevance, completeness, safety, clarity, and hallucinations.

- **Custom Questions:** **Over 200 brand new questions** were generated from scratch across four categories to eliminate the chance of **data contamination**, which is common when using existing academic benchmarks.

- **Evaluation Tasks:** The four tasks were:

  - **Medical Text Summarization** (e.g., summarizing radiology reports or discharge notes).

  - **Clinical Information Extraction** (e.g., extracting tumor staging from a pathology report or prescribed drugs).

  - **Biomedical Research** (e.g., determining if a clinical trial was successful based on an abstract).

  - **Open-Ended Medical Knowledge** (e.g., general medical questions without context).

- **Blind Evaluation:** Medical doctors conducted a pairwise blind evaluation: they were shown the original text and the randomized outputs of two different models (Model 1 and Model 2) and asked which they preferred, or if they were the same.

- **Dimensions of Preference:** Doctors evaluated outputs on three dimensions, although conciseness was excluded from the final shown results because it can be controlled by prompting:

  - **Factuality:** Whether the answer or summary conforms to the original source.

  - **Clinical Relevance:** Whether the output includes all facts deemed critical by a physician.

### **Comparative Results (JSL Medical LLM Medium vs. Frontier LLMs)**

#### **1. JSL vs. OpenAI GPT-4.5 (Across all four tasks)**

- **Factuality:** JSL was preferred 18% of the time, compared to 13% for GPT-4.5 (69% were rated the same).

- **Clinical Relevance:** JSL was preferred 29% of the time, compared to 26% for GPT-4.5 (half the time were rated the same).

- **Cost:** The JSL model achieved these results at **1/100th the cost** of running GPT-4.5 for the same tests.

#### **2. JSL vs. Anthropic Claude 3.7 (Across all four tasks)**

- Claude 3.7 was five times more expensive than the JSL Medical Medium LLM.

- **Factuality:** JSL was **heavily favored**.

- **Clinical Relevance:** JSL was **slightly favored**.

#### **3. Task-Specific Results (Clinical Information Extraction)**

This task, which involves extracting specific facts (e.g., key findings, social determinants) from clinical text, is essential for risk prediction and population health models.

- **JSL vs. GPT-4.5:** JSL was preferred **three times more often** on factuality compared to GPT-4.5 when the models were not equal, showing JSL's superior grounding and lower hallucination rates. JSL was also preferred over 50% more often on clinical relevance.

- **JSL vs. Claude 3.7:** JSL was preferred **four times more often** than Claude on factuality when the models were not equal, indicating Claude suffers from greater issues with factuality and hallucinations.

#### **4. Task-Specific Results (Biomedical Q&A)**

This involves answering specific questions based on context like PubMed abstracts or clinical trial results.

- **JSL vs. GPT-4.5:** JSL was preferred **2.5 times more often** on clinical relevance and won more often on factuality. The speaker suggested OpenAI models might be geared toward the general public or laypersons, whereas JSL models were judged by medical professionals focused on clinical utility.

- **JSL vs. Claude 3.7:** The models were very similar on clinical relevance, but JSL was preferred **2.3 times more often** than Claude on **factuality**.

## **Part 2: Granular Task Benchmarks (Presented by Vasel Kaman)**

The second part covered benchmarks on granular, practical tasks crucial in medical settings, comparing not only LLMs but also the clinical NLP APIs from AWS, Azure, and Google. The tasks covered were **Named Entity Recognition (NER)**, **Assertion Status Detection**, **Medical Coding**, and **De-identification**.

### **Named Entity Recognition (NER)**

NER is described as the "pillar of NLP in the medical domain".

- **JSL Healthcare NLP Library:** JSL's library has over **2,500 different pre-trained models**, including **more than 130 NER models** capable of extracting over **400 different medical entities** out of the box. These models are small and efficient, allowing 50 different NER models to run on a single machine without memory errors.

- **Granularity Gap:** The cloud provider APIs (Google, AWS, Azure) are "black box" classic NLP services that only return a **handful of entities** for each category (e.g., only one "problem" entity in Google). JSL offers **more than 20 different entities** just to define granular problem and condition entities (e.g., differentiating heart disease from kidney disease).

- **Customization:** JSL allows users to modify pipelines, rename entities, and turn entities on/off via blacklisting and whitelisting. Cloud providers offer black-box solutions where modification is impossible.

- **Results:** JSL's single pipeline NER model pipeline performed significantly better than all cloud providers, making **two to three times fewer errors**. JSL models achieved accuracy above 95%, even reaching **98%** on some granular entities like alcohol and tobacco consumption.

### **Assertion Status Detection**

This task detects the context of an extracted entity, determining if a condition is present, absent, conditional, associated with someone else (like a family member), or related to a planned or past event.

- **Importance:** Understanding assertion status is vital for filtering irrelevant cases, such as excluding a patient who "denies pain" or whose father has Alzheimer's, for downstream tasks like clinical trials.

- **JSL Approach:** JSL uses **five different algorithms** to accomplish this, moving beyond the 20-year-old regex-based negativity scope detection still used by many institutions. JSL combines these models and has fine-tuned LLM versions as well.

- **Results:** The JSL **combined pipeline** performed significantly better than GPT-4, Azure AI, and AWS Medical Comprehend. JSL also offers specialized pre-trained assertion models for niche domains (e.g., oncology, smoking detection, menopause) to ensure higher accuracy within specific verticals.

### **Medical Coding (Terminology Resolution)**

This involves mapping named entities to specific medical terminologies like **RxNorm**, ICD-10, SNOMED, and MedDRA.

- **ArxNorm Evaluation:** JSL evaluated its RxNorm capacity (used for medication entities).

- **Results:** On top-three accuracy, JSL Healthcare NLP was **30% better** than AWS Medical Comprehend. JSL returned the needed code within the top three results **83% of the time**, versus 56% for AWS.

- **Cost:** To process one million records:

  - **JSL:** Less than **\$5,000** (on-premise).

  - **AWS Medical Comprehend:** More than **\$25,000** (sharing data through API).

  - **GPT-4:** **\$44,000** (finding only 10% of codes, deemed "completely useless").

### **Clinical De-identification (De-ID)**

De-identification is the process of removing or masking Protected Health Information (PHI) according to HIPAA and GDPR.

- **Obfuscation:** For purposes like fine-tuning models, simple masking (blacking out text) renders the data useless. JSL provides **obfuscation**, replacing sensitive entities with **fake entities** while maintaining the document's integrity (e.g., replacing a female name with another female name, or a U.S. address with another U.S. address with the same structure).

- **JSL Solution:** JSL offers an end-to-end suite for text, structured data, and medical imaging (DICOM). The solution supports nine different languages.

- **Results (F1 Score):** JSL's De-ID solution achieved F1 scores between **93% and 98%**, outperforming all competitors.

  - On the binary PHI vs. non-PHI benchmark, JSL hit **96%** (Azure 91%, AWS 83%).

  - **Cost Comparison (1 million records):** JSL was six to seven times cheaper than Azure and AWS.

  - **LLM Comparison:** JSL hit **96%**, while GPT-4.5 achieved 84% and Claude 3.7 achieved 83%. GPT-4.5 was found to be **more than 100 times more expensive** (\$280,000+) than JSL (\$2,500) for processing the same amount of data, despite being 12% less accurate.