import pytest

from johnsnowlabs.frameworks.embedding_retrieval import JohnSnowLabsCharSplitter


# https://colab.research.google.com/drive/1J7JpxIkYcOlm01otttJLD6iFLge43dZ9?usp=sharing


def test_integration():
    from langchain.document_loaders import TextLoader
    from langchain.text_splitter import CharacterTextSplitter
    from langchain.vectorstores import FAISS
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.agents.agent_toolkits import create_retriever_tool

    from johnsnowlabs.llm import embedding_retrival

    p = "/home/ckl/Documents/freelance/jsl/johnsnowlabs-4-real/tests/datasets/state_of_the_union.txt"
    loader = TextLoader(p)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    embeddings = embedding_retrival.JohnSnowLabsLangChainEmbedder(
        "en.embed_sentence.bert_base_uncased"
    )  #  OpenAIEmbeddings()
    db = FAISS.from_documents(texts, embeddings)
    retriever = db.as_retriever()
    tool = create_retriever_tool(
        retriever,
        "search_state_of_union",
        "Searches and returns documents regarding the state-of-the-union.",
    )
    tools = [tool]

    from langchain.agents.agent_toolkits import create_conversational_retrieval_agent
    from langchain.chat_models import ChatOpenAI

    open_api_key = "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"
    llm = ChatOpenAI(temperature=0, openai_api_key=open_api_key)
    agent_executor = create_conversational_retrieval_agent(llm, tools, verbose=True)

    result = agent_executor(
        {"input": "what did the president say about going to east of Columbus?"}
    )
    result["output"]
