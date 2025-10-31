New State\-of\-the\-art Accuracy for the 3 Primary Uses of Healthcare Language Models

The speech provided in the YouTube transcript excerpts, delivered by David Alby, CTO at John Snow Labs, focuses on the current state\-of\-the\-art accuracy metrics for medical large language models \(LLMs\) across three primary use cases in healthcare\. The goal is to share key benchmarks and the insights gained from testing and improving those benchmarks for practical application in projects\.

The presentation is structured around three use cases, moving from the most discussed benchmark to the one most frequently seen in production, and finally to a new, growing use case\.

## __1\. Answering Medical Questions \(Medical QA\)__

The first use case discussed is answering medical questions, which is the primary benchmark used for evaluating medical LLMs, but is actually the least common use case seen in production\.

### __Benchmarks and Milestones__

- __State\-of\-the\-Art \(SOTA\):__ John Snow Labs achieved a new state\-of\-the\-art status on the Open Medical LLM Leaderboard \(hosted on Hugging Face\)\. This leaderboard looks at the average performance across __nine benchmark datasets__ designed for medical question answering and reasoning\.
- The speaker notes that their model currently outperforms major models like GPT\-4, Med\-PaLM 2, Llama 3 variants, To, Meditron, and BioMistral on this average benchmark\.
- __Model Size Breakthrough:__ A significant milestone announced was the first large language model with only __8 billion parameters__ that beats both GPT\-4 and Med\-PaLM 2 on the average score of these nine medical reasoning benchmarks\.
- __PubMedQA SOTA:__ Separately, a 7 billion parameter model was the first under 10 billion parameters to beat GPT\-4 on the PubMedQA dataset\. The model achieved 78\.4% accuracy, surpassing the single human performance baseline for biomedical researchers, which was 78%\.

### __The Nine Benchmarks Detailed__

The nine benchmarks are composed of four main data sets \(or suites of data sets\):

1. __MedQA:__ This is a classic question\-answering dataset based on the __US medical licensing exam__\. Questions are natural language patient stories requiring technical understanding \(vitals, lab results\) and slang comprehension\. They are multiple\-choice \(one of four options\), typically asking for the most likely diagnosis, the next test to order, or the right drug to prescribe, and require evidence for the answer\.
2. __MMLU \(Massive Multitask Language Understanding\):__ This test set evaluates college\-level question answering across various subjects\. Five specific datasets within MMLU relate to healthcare: clinical, genomic, biology, medicine, and professional medicine\. These are also multiple\-choice and require understanding medical terminology, context, and temporal order\.
3. __MedMCQA:__ This data is drawn from medical licensing exams, potentially in India\. It is broken down by medical specialties \(e\.g\., pharmacology, surgery, and over 20 other categories\)\. Questions are usually shorter, multiple choice \(four possible answers\), and require providing evidence/explanation for the chosen answer\.
4. __PubMedQA \(Pit QA\):__ This is a __biomedical research dataset__, distinct from clinical data\. Each question is associated with a single academic paper that holds the answer\. The task requires reading the context and question to provide both a __long answer__ \(details of the study\) and a __short answer__ \(usually yes or no\)\.

### __Key Learnings for Medical QA Projects__

The speaker highlights four crucial points for medical QA projects:

1. __Domain Specificity is Key:__ __Healthcare\-specific models generally outperform general\-purpose models__ \(like GPT\-4 or Anthropic\), aligning with the general machine learning finding that task\-specific tuning increases accuracy\.
2. __Overfitting Risks:__ Users must be wary of overfitting, especially with smaller models\. A model that scores very highly \(e\.g\., 90% or 99%\) on one medical benchmark might perform poorly on general medical or general\-purpose questions\. Models should be tested both on domain\-specific benchmarks and general LLM benchmarks to ensure generalization capability\.
3. __Efficiency in Production:__ Smaller, task\-specific models are __far more efficient and cheaper to run in production__\. For instance, a 3 billion parameter model can run on a smartphone, and an 8 billion parameter model can run on a laptop or a server costing less than $1 per hour, compared to $15 to $35 or more per hour for large LLMs\.
4. __Benchmarks Do Not Reflect Reality:__ Benchmarks are useful for comparison but __do not reflect real\-world use cases__\. Customers rarely need LLMs to answer medical licensing exam questions or look up questions based on a single research article\.

## __2\. Understanding Clinical Documents \(Information Extraction\)__

The second use case, which is seen much more frequently in production, is understanding clinical documents about patients, specifically information extraction\.

### __Adverse Events Example__

A case study involving work with the FDA focuses on mining unstructured clinical data \(notes\) to identify Adverse Events \(bad side effects due to opioids\), as Adverse Events are heavily __underreported__ \(potentially over 90%\)\.

This task requires handling complex unstructured medical text that describes events like a patient being over\-sedated, experiencing oxygen desaturation \(almost dying\), and later becoming somnolent after subsequent treatment\.

Key tasks required for this type of medical information extraction include:

1. __Text Classification:__ Determining if a sentence indicates an Adverse Drug Event \(ADE\)\.
2. __Entity Recognition:__ Identifying specific entities like the drug \(e\.g\., Insulin\) and the related symptoms \(e\.g\., drowsiness, blurred vision\)\.
3. __Relation Detection:__ Understanding the semantic relationship between entities to ensure, for example, that a symptom relates to the correct drug entity when multiple drugs are mentioned\.

### __Performance of LLMs in Extraction__

A consistent finding across the industry is that __current GPT models perform quite poorly on medical information extraction tasks__ compared to traditional deep learning/transfer learning models tuned for the task\. While prompt engineering can yield some results, task\-specific models are much more accurate, faster, and cheaper for production\.

- __Social Determinants of Health \(SDOH\):__ In extracting SDOH \(aspects like housing status, education, and financial stability\) from unstructured text, a recent paper found that __GPT\-4 made three times more mistakes__ than John Snow Labs’ current model\.
- __Entity Normalization:__ LLMs are particularly ill\-suited for normalizing recognized entities to standard medical codes \(e\.g\., ICD\-10\-CM for diagnoses, CPT for procedures, RXNorm for drugs\)\. Models and algorithms designed specifically for contextual normalization show a significant accuracy gap compared to LLMs\.

### __De\-identification \(De\-ID\)__

De\-identification involves detecting sensitive entities \(names, dates of birth, addresses, patient numbers, etc\.\) and then masking or obfuscating them \(e\.g\., replacing names consistently or shifting dates\) to ensure the data is no longer identifiable\.

- __Accuracy:__ Small, task\-specific, state\-of\-the\-art models consistently exceed __98% to 99% accuracy__ on real\-world data\.
- __Human Baseline:__ This algorithmic accuracy is __above the human baseline__\. A single human achieves about 93% accuracy; two humans \(the "four I principal"\) reach 96%; and three humans reach 98%\.
- __GPT\-4 Performance:__ In a recent paper, there was a __33% accuracy gap__ between the best de\-identification algorithms and GPT\-4\. This gap is critical because unless accuracy is near 98%–99% \(above the human baseline\), the data may not be considered reliably de\-identified from a regulatory perspective\.
- __Cost Efficiency:__ Using small, task\-specific models for de\-identification at scale was found to be __two orders of magnitude cheaper__ than using a GPT\-4 API endpoint\.

## __3\. Patient\-Level Reasoning__

The final use case is the "big new upcoming use case," which moves beyond analyzing single documents to reasoning about the patient as a whole\.

### __Real\-World Data Project Example \(Montelukast\)__

A project is underway \(with partners like Oracle Health/Cerner and Kaiser Permanente\) to investigate if and why children had neuro\-psychiatric reactions to the widely used asthma medication Montelukast, which received a black box warning from the FDA\.

- __The Data Challenge:__ Crucially, most information about mental health issues \(e\.g\., agitation, bad dreams, sleepwalking, hallucinations\) is contained only in unstructured notes, as these symptoms often do not receive a specific diagnosis code\. Analyzing this requires synthesizing information across notes collected over many years \(10 to 20 years for children\)\.

### __LLMs for Patient Q&A and Deduction__

LLMs seem to enable patient\-level reasoning by allowing a doctor or researcher to ask a question about the patient as a whole, drawing from hundreds of documents \(structured and unstructured\) without excessive clicking in an EHR system\.

Key capabilities for patient\-level reasoning include:

- __Informed Deduction:__ The model should not just report that information is missing; if the age is not explicitly stated, it should infer the age based on contextual clues across documents \(e\.g\., patient was born prematurely, details about discharge weight\) and make an informed deduction \(e\.g\., "premature infant likely aged between 28 and 35 weeks"\)\.
- __Citations/Referencing:__ The model must provide detailed references so the user can click and verify exactly which paragraph on which page \(especially critical for multi\-hundred\-page documents\) the reference was pulled from\.

### __Required End\-to\-End Architecture__

A complex pipeline is necessary for this end\-to\-end medical reasoning use case:

1. __Information Extraction at the Document Level:__ Apply __state\-of\-the\-art information extraction models__ \(non\-LLMs, for highest accuracy\) to every single document \(radiology, pathology, lab reports, etc\.\)\.
2. __Patient\-Level Reasoning:__ Use small LLMs to take the extracted facts from all documents and integrate them to generate a story or answer about the patient\.
3. __Data Fusion/Data Model Creation:__ The synthesized information is stored in a patient data model, often following standards like OMOP \(relational database\) or a Knowledge Graph\.
4. __Serving/Chatbot:__ A chatbot is used for natural language question answering, but the LLM's primary role is not memory recall; it acts as an __agent__ or __tool__ to convert the natural language question into a query \(Text\-to\-SQL or Graph Query Language\) for the underlying data model\.

### __Text\-to\-SQL Performance__

John Snow Labs has a state\-of\-the\-art healthcare\-specific __Text\-to\-SQL model__ that achieved a new accuracy of 0\.85 on the MIMIC SQL database, outperforming previous SOTA models including SQL Coder, Llama 2, and GPT\-4\. This model serves as the agent/tool to execute natural language queries against the structured data model\.

## __General Conclusions and Recommendations__

The speaker concludes with critical insights for building these complex systems:

- __Pipeline Necessity:__ Achieving state\-of\-the\-art medical reasoning requires a __combination of different models and skills within a pipeline__; attempting to put everything into a single RAG database or rely solely on a huge LLM context window is not effective at scale\.
- __Task Specificity:__ Task\-specific, healthcare\-specific models are the most accurate and the most efficient and economical to run\.
- __LLM Volatility:__ The accuracy of LLMs is improving on a weekly basis, sometimes multiple times a week\. Users should __not get attached to a specific LLM__ \(Llama 2, Llama 3, Mistral, etc\.\)\. System design must be able to __encapsulate and frequently upgrade the LLM__ to take advantage of the rapidly changing state of the art\.
- __Point in Time:__ Any statement made about the accuracy of LLMs is a __point\-in\-time statement__ due to the speed of change in the space\.

