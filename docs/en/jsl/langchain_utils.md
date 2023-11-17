---
layout: docs 
seotitle: NLP | John Snow Labs
title: Utilities for Langchain
permalink: /docs/en/jsl/langchain-utils
key: docs-install
modify_date: "2020-05-26"
header: true
show_nav: true
sidebar:
  nav: jsl
---

<div class="main-docs" markdown="1">





Johnsnowlabs provides the following components which can be used inside the [Langchain Framework](https://www.langchain.com/) for scalable pre-processing&embedding on
[spark clusters](https://spark.apache.org/) as Agent Tools and Pipeline components. With this you can create Easy-Scalable&Production-Grade LLM&RAG applications.
See the [Langchain with Johnsnowlabs Tutorial Notebook](todo)

## JohnSnowLabsHaystackProcessor
Pre-Process you documents in a scalable fashion in Langchain
based on [Spark-NLP's DocumentCharacterTextSplitter](https://sparknlp.org/docs/en/annotators#documentcharactertextsplitter) and supports all of it's [parameters](https://sparknlp.org/api/python/reference/autosummary/sparknlp/annotator/document_character_text_splitter/index.html#sparknlp.annotator.document_character_text_splitter.DocumentCharacterTextSplitter)

```python
from langchain.document_loaders import TextLoader
from johnsnowlabs.llm import embedding_retrieval

loader = TextLoader('/content/state_of_the_union.txt')
documents = loader.load()


from johnsnowlabs.llm import embedding_retrieval

# Create Pre-Processor which is connected to spark-cluster
processor = embedding_retrieval.JohnSnowLabsLangChainCharSplitter(
    chunk_overlap=2,
    chunk_size=20,
    explode_splits=True,
    keep_seperators=True,
    patterns_are_regex=False,
    split_patterns=["\n\n", "\n", " ", ""],
    trim_whitespace=True,
)
# Process document distributed on a spark-cluster
pre_processed_docs = jsl_splitter.split_documents(documents)

```

## JohnSnowLabsHaystackEmbedder
Scalable Embedding computation with [any Sentence Embedding](https://nlp.johnsnowlabs.com/models?task=Embeddings) from John Snow Labs.
You must provide the **NLU reference** of a sentence embeddings to load it.
You can start a spark session by setting `hardware_target` as one of `cpu`, `gpu`, `apple_silicon`, or `aarch` on localhost environments.
For clusters, you must setup the cluster-env correctly, using [nlp.install_to_databricks()](https://nlp.johnsnowlabs.com/docs/en/jsl/install_advanced#into-a-freshly-created-databricks-cluster-automatically) is recommended.

```python 
# Create Embedder which connects is connected to spark-cluster
from johnsnowlabs.llm import embedding_retrieval
embeddings =  embedding_retrieval.JohnSnowLabsLangChainEmbedder('en.embed_sentence.bert_base_uncased',hardware_target='cpu')

# Compute Embeddings distributed
from langchain.vectorstores import FAISS
retriever = FAISS.from_documents(pre_processed_docs, embeddings).as_retriever()

# Create A tool
from langchain.agents.agent_toolkits import create_retriever_tool
tool = create_retriever_tool(
  retriever,
  "search_state_of_union",
  "Searches and returns documents regarding the state-of-the-union."
)


# Use Create LLM Agent with the Tool 
from langchain.agents.agent_toolkits import create_conversational_retrieval_agent
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(openai_api_key='YOUR_API_KEY')
agent_executor = create_conversational_retrieval_agent(llm, [tool], verbose=True)
result = agent_executor({"input": "what did the president say about going to east of Columbus?"})
result['output']

>>>
> Entering new AgentExecutor chain...
Invoking: `search_state_of_union` with `{'query': 'going to east of Columbus'}`
[Document(page_content='miles east of', metadata={'source': '/content/state_of_the_union.txt'}), Document(page_content='in America.', metadata={'source': '/content/state_of_the_union.txt'}), Document(page_content='out of America.', metadata={'source': '/content/state_of_the_union.txt'}), Document(page_content='upside down.', metadata={'source': '/content/state_of_the_union.txt'})]I'm sorry, but I couldn't find any specific information about the president's statement regarding going to the east of Columbus in the State of the Union address.
> Finished chain.
I'm sorry, but I couldn't find any specific information about the president's statement regarding going to the east of Columbus in the State of the Union address.
```


</div>