Transforming Healthcare with Large Language Models

The talk presented by Vaseel Kocherman, Head of Data Science for Healthcare at John Snow Labs, focused on the challenges and opportunities of integrating Large Language Models \(LLMs\) into real\-world clinical practice and patient engagement\. John Snow Labs is a globally distributed Healthcare NLP company, and the data science team has been working with NLP for five years\.

The speech covered the current landscape, limitations, popular trends, and future workflows for LLMs in healthcare:

### __The Problem of Trust and Deployment__

The speaker noted that while new LLMs \(like Llama 2/3 and ChatGPT\) are constantly being announced and improved, the fundamental challenge is deployment\. Organizations must be able to deploy solutions on\-prem to solve specific problems using their own data, especially in air\-gapped environments or while dealing with strict regulatory issues like HIPAA\.

A major concern is __hallucination__, meaning the information returned by LLMs—even sophisticated ones like GPT\-4—cannot always be trusted\. Although LLMs are useful for automation, research indicates that even GPT\-4, with reinforcement learning from human feedback, __is still unable to answer 40% of questions correctly__\. For precise information extraction, which is critical in healthcare settings, LLMs are currently not reliable enough to trust\.

### __Benchmarks vs\. Reality__

The current industry trend is to evaluate new healthcare LLMs using established benchmarks like the USMLE \(United States Medical License Board examinations\), PubMed Q&A, or MMLU\. However, these are research\-focused benchmarks, and in the real world, problems are not solved by answering multiple\-choice questions\. While these models show the potential for automating routine and boring tasks \(like form filling\), freeing up physicians for "intelligent Heavy task," they do not demonstrate true human intelligence\.

The speaker characterized large language models as a "blue JPEG" or a "zipped condensed version of the image that you take a picture with your phone"\. This means LLMs are merely representing the information they were trained on \(trillions of text data tokens\) but __do not inherently understand if the output is factual or relative__\.

### __The Limitations of LLMs in Extraction__

While LLMs perform well in reasoning tasks such as summarizing text or automating processes, they are significantly deficient in simple, precise __information extraction__ tasks, such as finding all oncological entities within a text\. The speaker emphasized that LLMs cannot replace classic NLP techniques, arguing that specialized, narrow models are still necessary, particularly when integrating these capabilities into a professional workflow or product\.

Evidence from John Snow Labs' work supports this:

- They evaluated 15 different entities against GPT\.
- Small, specialized, pre\-trained models from their Healthcare NLP library \(which are less than 15 megabytes in size\) __perform significantly better__ than 70 billion models like GPT\-4 or Llama 2 for specific information extraction\.
- For __de\-identification__ \(masking sensitive information\), GPT failed to detect all sensitive information roughly half the time\. If there were five sensitive pieces, it might only find two but claim it found all of them\. Therefore, for critical tasks like de\-identification, in\-house tools are still preferable\.

### __Popular LLM Trends and the Rise of RAG__

The speaker covered two primary trends in LLM applications in healthcare:

1. __Chat UI Experience:__ Using applications that query multiple popular LLMs simultaneously \(like Bart, Llama 2, ChatGPT\)\. This approach fails to solve real\-world problems because the LLMs have not seen the organization's unique proprietary data\.
2. __Retrieval Augmented Generation \(RAG\):__ RAG is designed to overcome limitations like the LLM's limited context window \(e\.g\., 40K or 50K limit\)\. 
	1. __How RAG Works:__ Documents are embedded and stored in a vector database \(e\.g\., Elasticsearch, Chroma\)\. When a question is asked \(e\.g\., "What is cystic fibrosis?"\), the query is also embedded, and the vector DB returns the top K similar snippets \(like a K\-nearest neighbor search\) from the millions of documents\. The LLM then uses these snippets as context to construct a single answer\.

A significant limitation of RAG is that the LLM is only given the top 5 or 10 results from the vector database\. There is no guarantee that these top K results are the most comprehensive or useful documents needed to answer the question\. Consequently, John Snow Labs is currently working on __post\-filtering and post\-ranking strategies__ to ensure the LLM receives the most useful information possible\.

### __The Value of Small, Specialized Models__

Research suggests that __smaller, domain\-specific models__ outperform large foundational LLMs for specific tasks like Named Entity Recognition \(NER\), relation extraction, or specialized summarization\. For workflows involving highly specific, repeatable jobs \(like filling out forms or finding specific patient cohorts\), a small model, perhaps less than one gigabyte, can be fine\-tuned on the organization's data and will perform better than a massive 70 billion parameter model\.

In the RAG vs\. Fine\-Tuning debate, the speaker noted that their customer experience suggests that RAG is often sufficient most of the time\.

### __The Ultimate Healthcare Workflow: Orchestration__

The speaker highlighted that neither RAG nor LLMs alone can answer complex questions that require __cross\-referencing or correlation__ between thousands of documents across multiple years \(e\.g\., analyzing 10 years of data for 1,000 patients\)\. This is because LLMs and RAG only take a snapshot or vector representation of individual documents\.

The ideal workflow incorporates classical NLP techniques:

1. Classical NLP is used to parse documents and extract key information\.
2. This extracted data is stored in structured formats, such as tabular data or __knowledge graphs__\.
3. The LLM then acts solely as an __interface__ to convert the user's natural language query into a structured query \(like SQL or Cypher\)\.

__Conclusion:__ The central message is that __LLMs should not be used as information extraction agents__\. Instead, they should function as a __smart assistant to orchestrate tasks__ with smaller, specialized models within the workflow\. This approach allows organizations to reduce the size of the LLMs and train them on proprietary data, enabling successful on\-prem deployment\. John Snow Labs plans to ship an on\-prem application incorporating these capabilities by the end of 2023\.

Regarding commercialization, the speaker acknowledged that while buying commercial solutions is easy, building software around these models using an organization's own team and solutions on their own premise will be superior\. The biggest pitfall for developers is that while building initial Proof of Concepts \(POCs\) with LLMs is easy, scaling and productizing them requires dealing with guardrails and ensuring consistent performance, which is a massive struggle\.

