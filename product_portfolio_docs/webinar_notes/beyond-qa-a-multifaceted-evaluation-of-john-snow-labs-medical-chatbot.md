Beyond QA: A Multifaceted Evaluation of John Snow Labs’ Medical Chatbot

This response summarizes the speech titled "Beyond QA: A Multifaceted Evaluation of John Snow Labs’ Medical Chatbot" delivered by Vel, the Head of Data Science at John Snow Labs, leading the Healthcare NLP \(H NLP\) team\.

The speech focuses on the capabilities and, more importantly, the limitations of large language models \(LLMs\) in clinical settings, and how Retrieval Augmented Generation \(RAG\) architecture, specifically improved by John Snow Labs \(JSL\), addresses these challenges, culminating in their upcoming medical chatbot\.

### __The Context: LLM Hype and Limitations__

Since the general availability of ChatGPT around October of the previous year, instruction fine\-tuned LLMs have dominated the field\. While highly capable models like GPT\-4, Llama 2, and Mistral exist, and many open\-source models are as effective as GPT\-3\.5, using them for medical challenges presents significant risks\.

- __Accuracy Concerns:__ While LLMs are tested on medical challenge problems \(like MedQA\), and GPT\-4 is often used for ground truth annotation, their performance is inconsistent\.
- __Zero\-Shot Limitations:__ Zero\-shot capability \(asking questions blindly without instruction\) is low; for example, GPT\-3\.5 zero\-shot on MedQA is around 40%\. People use five\-shot prompting \(providing examples and answers\) to direct the LLM toward expected outcomes\.
- __Clinical Risk:__ Even using sophisticated techniques like reinforcement learning with human feedback and five\-shot prompting, GPT\-4 still answers __40% of questions incorrectly__ based on some truthful Q&A benchmarks\. The speaker emphasizes that this is a __high risk__ in clinical settings where users "may never know when it is correct or not"\.

### __Retrieval Augmented Generation \(RAG\) Architecture__

To mitigate the risk of relying solely on an LLM's own knowledge \("closed book capabilities"\), RAG is introduced as a solution\. RAG is the combination of user\-provided documents \(such as PubMed articles or in\-house data\) and an LLM acting as an agent\.

#### __The RAG Process and LLM Role:__

1. __Document Preparation:__ Source documents are split into sizable chunks or "splits"\.
2. __Embedding and Storage:__ Embeddings are generated for each split and written into a Vector DB\.
3. __Retrieval:__ When a user asks a question, its embedding is generated\. The Vector DB returns the top K \(typically three or five\) similar splits\.
4. __Generation:__ These relevant documents \(the "content"\) are sent to the LLM\. The LLM's job is __limited__—it must follow the instruction to respond to the question *based on the content* provided by the Vector DB\. This is intended to prevent hallucination\.

#### __The Five Components of RAG and Associated Perils:__

The RAG architecture involves five stages, each presenting opportunities for improvement or risk if overlooked:

1. __Source Documents:__ Requires excellent __preprocessing__ \(e\.g\., careful OCR for PDFs/scanned images\)\. Results can differ drastically if preprocessing is ignored\. Important features like __metadata extraction__ \(author names, keywords, document titles/types\) can augment the Vector DB\. __Feature engineering__ \(table understanding, summarizing documents, generating text descriptions for charts\) can reduce embedding size and improve quality\.
2. __Document Splitting:__ Strategies \(content\-wise, section\-wise, paragraph\-wise\) and the maximum chunk size are treated as hyper\-parameters that can be easily manipulated to gain instant feedback\.
3. __Embeddings:__ The choice of embedding model \(e\.g\., E5, InstructEmbeddings vs\. OpenAI\) matters, as shown by the MTB \(Massive Text Embeddings\) leaderboard\. OpenAI embeddings, though widely used, rank around 12th or 17th\. Embeddings must also be suitable for use at scale\.
4. __Vector DB:__ Production\-ready RAG requires scalable solutions \(like Elastic or other alternatives\) for millions of documents, as simpler options like Chroma or Qdrant might fail\. Strategies involve different retrieval methods, post\-processing, reranking, and filtering\.
5. __LLM:__ The LLM must be able to follow precise instructions and cite resources\. Poorly written, straightforward prompts can lead the LLM to skip checking the content and answer directly \("black hole in your prompt"\)\.

### __Addressing Scaling Issues with Spark NLP__

A major risk in RAG is handling embeddings at scale\. While many tutorials use small datasets \(10–100 documents\), production environments often involve millions of documents, translating into 10 million or 100 million splits\.

- __The Scaling Problem:__ Generating embeddings for 1 million splits can take days without a proper framework, leading to long iteration times\.
- __Spark NLP Solution:__ Spark NLP 5\.0 introduced Onyx\-optimized and plain versions of embeddings to iterate faster\.
- __Performance Metrics:__ Spark NLP offers significant speed improvements compared to PyTorch\-based collections \(like those in Hugging Face\)\. 
	- For 1,000 documents, the quantized Spark NLP is __three times faster__ than Hugging Face\.
	- For 50,000 documents, the quantized Spark NLP is __seven times faster__ than Hugging Face\.
	- Spark NLP naturally scales over Spark clusters\. Using a 16\-worker Spark cluster, embeddings for __1 million documents__ can be generated in approximately __3 minutes__ \(180 seconds\)\.

### __John Snow Labs’ RAG Benchmark Results__

JSL developed an improved RAG pipeline, acknowledging that many users default to off\-the\-shelf pipelines \(like LangChain or LlamaIndex\)\. JSL used 1,400 diabetes\-related PubMed articles and 200 physician\-created ground truth questions for testing\.

They evaluated the performance using three criteria \(based on RAGAS metrics\):

__Metric__

__Focus__

__Default \(Plain\) Pipeline Score__

__Improved JSL RAG Score__

__Improvement__

__Context Relevancy__

Retrieval \(ratio of required vs\. total sentences in context\)

Less than 10%

Around 17%

Better ratio of relevant content

__Context Recall__

Retrieval \(ability to retrieve all necessary information\)

About 40%

55%

15% jump

__Faithfulness__

Generation \(information consistency, non\-hallucination\)

N/A \(lower than improved\)

N/A

15% better results achieved through improved prompting

__Overall, the improved RAG architecture developed by JSL—which includes context, metadata augmentation, and post\-processing techniques—achieved results that were approximately two times better \(a 20% jump in average metrics\) compared to the plain, default pipelines__\.

### __The John Snow Labs Medical Chatbot__

The forthcoming JSL medical chatbot product aims to solve complex challenges that require moving beyond simple QA by using the LLM as an agent to extract cross\-document relationships and insights from various data types\.

__Key Product Features:__

- __Data Processing:__ Ability to process the user's own in\-house documents and tabular data \(e\.g\., SQL databases created via Healthcare NLP pipelines\)\.
- __Insight Generation:__ Generates insights from documents without relying on the LLM's own internal knowledge\.
- __Tool Use:__ Leverages Healthcare NLP through agents\.
- __On\-Premise Deployment:__ The product is designed to run entirely __on your own premise__\. This means the LLM and the entire infrastructure are local, ensuring operation without relying on an external internet connection\.
- __Advanced Conversation:__ The chatbot can maintain conversational flow within the RAG context \(by handling follow\-up questions\) and explicitly site the source items for its answer, preventing hallucination\.

The medical chatbot is scheduled to be generally available for __on\-premise deployments by the end of 2023__\. The speaker concludes by stating that RAG is a crucial architecture and, in most cases, is favored over fine\-tuning\.

