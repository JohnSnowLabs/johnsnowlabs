---
layout: docs 
seotitle: NLP | John Snow Labs
title: Utilities for Haystack
permalink: /docs/en/jsl/haystack-utils
key: docs-install
modify_date: "2020-05-26"
header: true
show_nav: true
sidebar:
  nav: jsl
---

<div class="main-docs" markdown="1">


Johnsnowlabs provides the following nodes which can be used inside the [Haystack Framework](https://haystack.deepset.ai/) for scalable pre-processing&embedding on 
[spark clusters](https://spark.apache.org/). With this you can create Easy-Scalable&Production-Grade LLM&RAG applications.
See the [Haystack with Johnsnowlabs Tutorial Notebook](https://github.com/JohnSnowLabs/johnsnowlabs/blob/main/notebooks/haystack_with_johnsnowlabs.ipynb)

## JohnSnowLabsHaystackProcessor
Pre-Process you documents in a scalable fashion in Haystack
based on [Spark-NLP's DocumentCharacterTextSplitter](https://sparknlp.org/docs/en/annotators#documentcharactertextsplitter) and supports all of it's [parameters](https://sparknlp.org/api/python/reference/autosummary/sparknlp/annotator/document_character_text_splitter/index.html#sparknlp.annotator.document_character_text_splitter.DocumentCharacterTextSplitter)

```python
# Create Pre-Processor which is connected to spark-cluster
from johnsnowlabs.llm import embedding_retrieval
processor = embedding_retrieval.JohnSnowLabsHaystackProcessor(
    chunk_overlap=2,
    chunk_size=20,
    explode_splits=True,
    keep_seperators=True,
    patterns_are_regex=False,
    split_patterns=["\n\n", "\n", " ", ""],
    trim_whitespace=True,
)
# Process document distributed on a spark-cluster
processor.process(some_documents)
```

## JohnSnowLabsHaystackEmbedder
Scalable Embedding computation with [any Sentence Embedding](https://nlp.johnsnowlabs.com/models?task=Embeddings) from John Snow Labs in Haystack
You must provide the **NLU reference** of a sentence embeddings to load it.
If you want to use GPU with the Embedding Model, set GPU=True on localhost, it will start a spark-session with GPU jars.
For clusters, you must setup cluster-env correctly, using [nlp.install_to_databricks()](https://nlp.johnsnowlabs.com/docs/en/jsl/install_advanced#into-a-freshly-created-databricks-cluster-automatically) is recommended.

```python 
from johnsnowlabs.llm import embedding_retrieval
from haystack.document_stores import InMemoryDocumentStore

# Write some processed data to Doc store, so we can retrieve it later
document_store = InMemoryDocumentStore(embedding_dim=512)
document_store.write_documents(some_documents)

# Create Embedder which connects is connected to spark-cluster 
retriever = embedding_retrieval.JohnSnowLabsHaystackEmbedder(
    embedding_model='en.embed_sentence.bert_base_uncased',
    document_store=document_store,
    use_gpu=False,
)

# Compute Embeddings distributed in a cluster
document_store.update_embeddings(retriever)

```
</div>