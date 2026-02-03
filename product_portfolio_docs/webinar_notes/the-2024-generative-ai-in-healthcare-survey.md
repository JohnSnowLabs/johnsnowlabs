# The 2024 Generative AI in Healthcare Survey
The 2024 Generative AI in Healthcare Survey

<https://www.johnsnowlabs.com/watch-webinar-the-2024-generative-ai-in-healthcare-survey/>

<https://youtu.be/EJwtGBmiR_I>

<img src="/media/image.jpg" title="Video titled: The 2024 Generative AI in Healthcare Survey" style="width:6.3125in;height:3.65625in" />

The following is a detailed summary of the speech provided in the YouTube transcript regarding the 2024 Generative AI in Healthcare Survey.

The presentation provides an overview of the survey results focusing on Generative AI (GenAI) usage in the healthcare sector, supplemented by data from broader enterprise surveys and commentary from healthcare domain expert David Talby.

### **Survey Methodology and Focus**

The online survey ran for approximately one month, recruiting respondents through social media, newsletters, and online advertising. While over 300 people completed the survey, the analysis focused on **close to 200 people** working at organizations actively using generative AI. The presenter particularly highlights the responses from the **55 individuals categorized as "technical leaders,"** believing they possess a better understanding of how their organizations evaluate and implement GenAI technologies.

### **Budgeting and Investment**

Broadly speaking, there is significant "bullishness" around GenAI technology, especially within Fortune 500 companies. In the healthcare survey, about **34% of technical leaders** project that they will **double their GenAI budget** between 2023 and 2024. This reflects a general trend toward increased spending on experimentation, recruiting, and project switching, indicating that many view GenAI as a major developing area, akin to the beginning of the internet.

### **Large Language Model (LLM) Usage**

While external surveys show proprietary models like OpenAI being widely used (and Google and Llama being popular general models), the healthcare survey reveals a different priority: **Healthcare-specific models are preferred** over general-purpose models (proprietary or open).

When general models are used by healthcare respondents, **open models are preferred over proprietary models**.

- **Privacy and Compliance:** David Talby notes that a key difference in healthcare is the necessity of privacy and compliance. Sending patient data to external APIs (like Google or OpenAI) is often **"just not an option"**.

- **Accuracy Gap:** General-purpose models are often **"just not that good"** in the healthcare space. Benchmarking within John Snow Labs shows that task-specific models (sometimes not even LLMs) can achieve materially better accuracy, meaning that general LLMs can sometimes result in three, four, five, or six times the number of errors compared to specialized, off-the-shelf models.

- **Proprietary Use:** Proprietary LLMs are mainly used early on for "playing around" with fake data to learn what is possible, as actual patient data, clinical trial results, or protected health information cannot be loaded. When deploying solutions, organizations often start with a model they can deploy behind their firewall, like open-source options, due to cost and control.

### **Key Use Cases in Healthcare**

The survey identified two main areas of initial focus: information extraction/knowledge management (internal) and chatbots/co-pilots (external).

1.  **Internal-Facing Applications:** Organizations are more aggressive in trying out internal use cases. Examples include:

    1.  Information extraction, medical text summarization, transcribing medical encounters, and clinical coding.

    2.  Matching patients to clinical trials.

    3.  Automating tasks around regulatory submissions, billing, coding, and fraud detection, which are traditionally "extremely human intensive".

These internal uses provide a **simple cash-on-cash ROI** (Return on Investment) and allow for a crucial mitigation strategy: **human review** (Human-in-the-Loop).

2.  **External-Facing Applications (More Cautious):** External applications like chatbots answering patient questions are being explored but with more caution. This caution is due to increased risks, particularly around legal issues and reputation damage from hallucinations or mistakes.

An external study conducted by Stanford and MIT on 5,100 customer service agents using a custom LLM found a **14% increase in productivity**. Furthermore, the technology disproportionately benefits agents who were previously "below average," effectively **raising the productivity of less-skilled individuals** and lowering the skills gap.

### **Future Impact and Synthetic Data**

Respondents are excited about the potential for chatbots, transcribing doctor-patient conversations (which requires a speech model and an LLM), and synthetic data generation.

- **Synthetic Data Concerns:** David Talby advises that synthetic data is useful for demos and testing but cautions against using it as a replacement for real patient data, especially when evaluating clinical outcomes. Synthetic data generated by models tends to be **"too clean,"** lacking the noise, conflicting information, bad grammar, and rare "weird cases" found in real-world clinical reports. If a model achieves a high F1 score on synthetic data (e.g., 0.98), it will likely perform significantly worse on real data (e.g., 0.83).

- **Regulatory Status:** Synthetic data **does not count** for medical device claims or clinical trials, which require actual patient data. If used, it must be disclosed to regulators.

### **Evaluation Criteria and Roadblocks**

When evaluating specific LLMs, technical leaders in healthcare prioritize the following:

1.  **Security and Privacy** (considered an "entry ticket" for discussion).

2.  The model being **Healthcare specific**.

3.  **Legal and reputation risk** (including hallucination).

4.  **Accuracy** (the most benchmarked element).

Major roadblocks identified in the survey include **accuracy** (number one), legal/reputation risks, bias and fairness, and the fact that models are often **"not built for healthcare and Life Sciences"**.

### **Enhancing and Customizing Models**

To improve selected models, organizations are engaging in customization. The most common methods in the healthcare space are **Human-in-the-Loop** (getting human feedback to refine the model) and **supervised fine-tuning** (requires labeled prompt-response pairs).

- **Role of Domain Experts:** Successful customization in healthcare **requires the active participation of domain experts** (like medical doctors), who can provide labeled data and feedback. Tools should be non-developer friendly ("no code tools") to ensure that experts who do not know Python or coding can participate in testing and fine-tuning. Domain experts are critical because developers or data scientists may miss crucial clinical details or inconsistencies.

### **Key Takeaways**

The presentation concludes with four main takeaways for the audience:

1.  **Healthcare-specific models are essential** and preferred throughout the evaluation process.

2.  GenAI is a team sport; organizations need **Human-in-the-Loop tools** that are accessible and friendly to non-developers and domain experts.

3.  There is a **significant increase in GenAI budgeting**, driven by competitive pressure and the need to improve patient care and reduce inefficiency.

4.  **Open LLMs continue to improve** and keep pace with proprietary models. They offer flexible licenses and are amenable to fine-tuning, especially with the right tools that allow domain experts to participate.

Finally, the speakers emphasize that generative AI is still very early-compared to the first half mile of a 26-mile marathon-and the fundamentals of AI/Machine Learning (data quality, monitoring, devops) still apply. The focus is expected to shift toward **multimodal** capabilities (handling text, speech, audio, images, video) and the development of more **autonomous agents**.