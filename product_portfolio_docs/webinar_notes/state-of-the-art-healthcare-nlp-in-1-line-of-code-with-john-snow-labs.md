State\-of\-the\-Art Healthcare NLP in 1 Line of Code with John Snow Labs

The speaker in the video is __David Talby__, CTO at __John Snow Labs__\. He focuses on __Natural Language Processing \(NLP\) in healthcare__ and demonstrates how to achieve state\-of\-the\-art medical, clinical, and biomedical NLP using just __one line of Python code__\.

Below is a detailed summary of the speech provided in the transcript excerpts:

### __John Snow Labs and Spark NLP Overview__

David Talby identifies himself as working with the team behind the __Spark NLP library__\. This library offers APIs for Python, Java, and Scala\. Spark NLP is currently the __most popular NLP library in the enterprise__ and outside research for deploying AI systems, especially within the healthcare space\.

Key statistics and market standing for Spark NLP:

- It has been the most popular enterprise NLP library for four years\.
- An industry survey by Gaijin Flow indicated that Spark NLP for Healthcare holds a __59% market share__ within the healthcare and life science domain\.
- The library currently averages around __one and a half million downloads per month__\.

### __Core Use Cases in Healthcare__

John Snow Labs highlights various applications where strong NLP is essential because critical decision\-making information is often only available in __free text__\. These use cases include:

- Clinical decision support\.
- Matching patients to clinical trials\.
- Building real\-world data databases, especially in oncology \(which involves reading pathology, radiology, and sequencing reports\)\.
- Automated question answering on patient data or clinical guidelines\.
- Building __biomedical knowledge graphs__ by reading patents, internal documents, biomedical research, and clinical trial reports\.
- Automatically discovering adverse drug events from clinical data and social media data\.

### __Components for State\-of\-the\-Art NLP__

To achieve state\-of\-the\-art results efficiently, two components are utilized: __Spark NLP for Healthcare__ and the __NLU Library__\.

#### __1\. Spark NLP for Healthcare__

This is a software product built on top of the open\-source Spark NLP library\. It offers:

- Over __4,000 pre\-trained models__ and embeddings\.
- Support for over 200 languages\.
- Ability to scale to a cluster for training or inference\.
- Optimizations done continuously with Intel and NVIDIA for high performance, production deployment, security, and privacy\.
- __Key Healthcare NLP Tasks:__ Clinical Name Entity Recognition \(NER\), entity linking \(mapping entities to terminologies in context\), assertion status detection, relation extraction, and de\-identification\.
- All models are __deep learning transfer learning models__ and are trainable\. Users can use an annotation tool to load their own data, annotate it, and quickly develop high\-accuracy models tuned for specific domains \(e\.g\., dentistry or ophthalmology\) using active learning and transfer learning\.

#### __2\. The NLU Library__

The NLU library is a newer, open\-source library that aims to bring the accuracy, scalability, and production readiness of Spark NLP to the __Python ecosystem with simple Python commands__\.

- A primary goal is that the vast majority of tasks should be executable with __just one line of code__\.
- The library automatically handles downloading, loading, optimizing models, embeddings, and pipelines\.
- It integrates seamlessly within Python, accepting input as a string, a __Pandas data frame__, an array data frame, or a Spark data frame, and returning results in the same format\.

### __General NLU Capabilities and Examples__

The NLU library offers numerous features beyond healthcare, including:

- __Name Entity Recognition \(NER\):__ Identifying entities like people and locations \(e\.g\., identifying "Angela Merkel" as a person and "Germany" as a location\)\.
- __Document Classification:__ Hundreds of pre\-trained models are available, such as models for fake news detection, financial data, or legal data\.
- __Other functions:__ Automated grammar correction, changing writing styles \(e\.g\., from informal to formal\), question answering, dependency analysis, part\-of\-speech tagging, spell checking, sentiment and emotion classification, and translation in many languages\.

### __Defining State\-of\-the\-Art \(SOTA\)__

David Talby emphasizes that __State\-of\-the\-Art \(SOTA\)__ is a strict academic term, not a marketing term\. John Snow Labs measures itself by:

- Demonstrating the best accuracy on competitive academic benchmarks where dozens of research teams have previously competed\.
- Publishing __peer\-reviewed papers__ that validate these results\.
- Releasing the code publicly so that other researchers can reproduce and verify the results\.
- Requiring that the product achieves SOTA results in the context of a system that has __multiple production deployments__, showing it works reliably outside of a lab environment\.

### __State\-of\-the\-Art Clinical and Biomedical Results__

The presentation provides specific examples of how the one\-line\-of\-code approach is used for complex clinical tasks:

__Task__

__Key Functionality and Specific Examples__

__SOTA Claims & Performance__

__Clinical Name Entity Recognition \(NER\)__

Extracting information like drug details \(dosage, frequency, strength, route—e\.g\., "30 milligrams," "po," "q 12 hours"\), clinical risk factors \(obesity, diabetes, hypertension\), and findings from radiology reports\. The software recognizes more than 150 clinical entities\.

A 2021 paper achieved new SOTA accuracy for three competitive benchmarks: 2010 i2b2, 2014 n2c2 text classification, and 2018 n2c2 medication extraction\. A later 2021 paper showed the solution leading AWS Medical Comprehension and Google Cloud Healthcare API by __more than 10% in F1 accuracy__ for extracting medical problems, tests, and drugs\.

__De\-identification__

High\-accuracy identification of sensitive data in free text, including patient names, doctor names, hospital names, addresses, dates, codes, and professions\.

Achieved SOTA accuracy in benchmarks\.

__Biomedical NER__

Reading medical research papers to extract genes, human phenotypes, DNA/protein mutations, species, viruses, and specific gene variants\.

A late 2020 paper achieved new SOTA accuracy for __seven out of eight__ widely used biomedical NER benchmarks\.

__Assertion Status Detection__

Determines if a recognized entity \(e\.g\., "cancer"\) is present, absent, possible, or a family issue\. This is crucial as recognizing the word alone is insufficient\.

A paper published last year improved SOTA accuracy using the MIMIC\-III benchmark data\.

__Relation Extraction__

Finds relationships between entities, such as connecting a symptom to a body part and direction \("numbness in the left hand"\) or linking diagnoses, treatments, and dates\. It can also extract drug\-drug relationships from biomedical data \(e\.g\., PubMed\)\.

New peer\-reviewed papers demonstrate SOTA results for several widely used relation extraction models in the clinical and biomedical domains\.

### __Conclusion and Resources__

Additional capabilities include automated text classification for clinical text, adverse event detection, and question answering on clinical data\.

The speaker invites the audience to attend the __Healthcare NLP Summit__ in early April\. Furthermore, over __300 live demos__ are available at nlp\.johnson\.com/demos, including Streamlit apps and Colab demos, allowing users to test the models on their own data\.

