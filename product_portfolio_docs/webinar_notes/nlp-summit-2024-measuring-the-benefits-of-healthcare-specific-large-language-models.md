NLP Summit 2024 Measuring the Benefits of Healthcare Specific Large Language Models

The speech excerpt details the process and findings of __John Snow Labs__ \(JSL\) regarding the evaluation and benefits of their healthcare\-specific Large Language Models \(LLMs\) compared to generalized models like GPT\-4\. The speaker, Rael, Head of Data Science at JSL, outlines the company's offerings, the rationale for fine\-tuning, the internal evaluation methodology, and the key results\.

### __John Snow Labs' Healthcare AI Ecosystem__

JSL offers two main product lines in healthcare AI:

1. __Healthcare NLP Library:__ This library hosts __more than 2,000 pre\-trained models and pipelines__ used for classical NLP tasks\. It extracts entities, finds relationships, and maps terminologies to standards like ICD, SNOMED, and others\.
2. __Medical LLMs \(MedLLMs\):__ Developed over the last two years, these models are categorized by size using suffixes: 
	1. __MedS:__ Less than three billion parameters \(3B\)\.
	2. __MedM:__ Less than ten billion parameters \(10B\)\.
	3. __MedL:__ Greater than forty billion parameters \(40B\), including 50B and 70B sizes\.

Models less than 10 billion parameters \(MedS and MedM\) are included in the Healthcare NLP library\. These models are fine\-tuned on an internal, in\-house annotated medical data set, as well as some public research data sets\.

The LLMs are designed for specific purposes:

- __MedS__ can be used for summarization and question answering\.
- __MedM__ can handle both summarization/Q&A and open\-ended, close\-book questions \(e\.g\., "how to treat Asthma"\)\.
- __MedN__ is solely fine\-tuned for named entity recognition \(NER\) in a medical context\.

### __The Value of Fine\-Tuning__

The speaker highlights the growing consensus on the benefits of specialized LLMs\. Referencing a recent paper called __Laureland__, the speaker notes that fine\-tuning using frameworks like LoRA significantly enhances LLM performance, sometimes surpassing GPT\-4 on non\-medical benchmarks by an average of 10 points\.

For users with a specific task \(e\.g\., summarization, Q&A based on context, filling forms\), a smaller, fine\-tuned model is preferred over a generalized model because it is __more feasible to deploy locally, scales further, and is cheaper__\.

### __JSL’s Medical LLM Evaluation Methodology__

Recognizing that generalized benchmarks lack clinical context, JSL developed a robust evaluation system\. They based their approach on the principles later echoed in the "Medic" paper, which suggests five dimensions for clinical\-grade LLM evaluation\.

JSL’s internal evaluation compared two of their fine\-tuned models, __MedM__ \(less than 10B, specifically the __8 billion size model__\) and __MedL__ \(greater than 40B\), against __GPT\-4__\.

__Evaluation Dimensions Used:__ JSL focused on three dimensions assessed by human medical doctors:

1. __Factuality:__ Assessing whether the answers contain verifiable and truthful data based on medical knowledge\.
2. __Clinical Relevance:__ The applicability of the information to clinical practice\.
3. __Conciseness:__ The brevity and clarity of the answer \(addressing the verbosity often seen in some LLMs\)\.

__The Evaluation Setup:__

- __Questions:__ Over 450 questions were generated from scratch by physician annotators—experienced medical doctors \(e\.g\., Professor of Pathophysiology, Hematologist, Neurologist\) with 2\-3 years of AI/NLP experience\.
- __Tasks:__ The questions were split evenly across four categories: Medical Summarization, Medical Question Answering in clinical notes, Biomedical Research, and Open\-ended QA in clinical modes\.
- __Randomized Blind Evaluation:__ Annotators received an Excel sheet showing the question, context, and answers labeled only as Model 1, Model 2, and Model 3\. They did not know which actual LLM \(MedM, MedL, or GPT\-4\) corresponded to which label\.
- __Pairwise Comparison:__ Annotators evaluated answers in pairs \(Model 1 vs\. Model 2, Model 1 vs\. Model 3, etc\.\), selecting the preferred model, "neutral" \(equally correct\), or "none"\.

### __Key Results \(8 Billion Model vs\. GPT\-4\)__

The JSL __8 billion size MedM model__ showed strong performance advantages over GPT\-4 across most clinical tasks\.

__Task__

__Dimension__

__JSL 8B Preference__

__GPT\-4 Preference__

__Neutral__

__Medical Summarization__ \(100 Qs\)

Factuality

__47%__

25%

22%

Clinical Relevancy

__48%__

25%

—

__Q&A in Clinical Notes__

Factuality

10% delta

—

Most time equally preferred

Relevancy & Conciseness

12% delta

—

—

__Biomedical Research__

Performance

__Beats GPT\-4__

—

Neutral preferred most often

__Open\-ended Q&A__ \(Close Book\)

Clinical Relevancy

GPT\-4 is better

—

—

Factuality

__5% better__

—

—

__Overall Metrics \(Average across all four tasks\):__

- The 8 billion size model was __5% better than GPT\-4 in Factuality__\.
- It was __over 10% better than GPT\-4 in Conciseness__ \(which is controllable during fine\-tuning\)\.
- Clinical Relevance was described as "head\-to\-head," with the 8B model being 1% worse than GPT\-4\.

If the "Neutral" preference \(where both models were correct\) is distributed evenly, the 8B model was preferred __46% of the time for Factuality__ compared to 41% for GPT\-4\.

### __Evaluation Insights and Challenges__

1. __GPT\-4 as a Judge:__ When GPT\-4 was used as a judge in the evaluation \(acting as a fifth rater\), it __strongly favored its own responses__ over the 8B model, disagreeing significantly with the human medical doctors on factuality and clinical relevancy\. Recent research also indicates that LLMs have the ability to recognize their own outputs\.
2. __Subjectivity and Agreement:__ The calculation of the __Intraclass Correlation Coefficient \(ICC\)__ revealed a __poor agreement among human annotators__ regarding __Factuality__\. However, the annotators were generally consistent in their own individual assessments regarding clinical relevance and conciseness, demonstrating the __subjective nature of LLM evaluation__\.

### __Key Takeaways__

The key conclusions drawn from the evaluation are:

- __Domain\-specific LLMs beat GPT\-4:__ JSL’s healthcare\-specific LLMs surpass GPT\-4 by around 10% on the measured domain\-specific tests after fine\-tuning on specialized data\.
- __Efficiency and Privacy:__ This superior performance was achieved with an __8 billion size model__, which can be deployed __on\-premise, running privately and efficiently without an internet connection__\.
- __Importance of Methodology:__ Evaluation must be done across __multiple dimensions__ and requires __medical expertise__ \(physician annotators\) due to the complexity and subjective nature of assessing LLM output in a clinical setting\.

