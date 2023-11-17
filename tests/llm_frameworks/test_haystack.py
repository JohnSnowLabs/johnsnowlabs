from haystack import Document
from mlflow.models import ModelSignature, infer_signature
import os
from haystack.pipelines import RayPipeline

# https://docs.haystack.deepset.ai/docs/pipelines#distributed-pipelines-with-ray
from haystack.nodes import EmbeddingRetriever

from johnsnowlabs.frameworks.embedding_retrieval.haystack_node import (
    JohnSnowLabsHaystackProcessor,
)

# os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
from johnsnowlabs.llm import embedding_retrieval


def get_docs():
    return [
        Document(
            content="I like apples",
            content_type="text",
            id=1,
        ),
        Document(
            content="I like bananas \n and other things \n like icream \n and cats",
            content_type="text",
            id=2,
        ),
    ]


def test_integration():
    from haystack.nodes import PreProcessor
    from haystack import Pipeline
    from haystack.document_stores import InMemoryDocumentStore

    # processor = PreProcessor(
    #     clean_whitespace=True,
    #     split_by="word",
    # )

    processor = JohnSnowLabsHaystackProcessor()

    # Write some processed data to Doc store, so we can retrieve it later
    document_store = InMemoryDocumentStore(embedding_dim=512)
    document_store.write_documents(processor.process(get_docs()))

    # could just use EmbeddingRetriever but mehhh
    retriever = embedding_retrieval.JohnSnowLabsHaystackEmbedder(
        embedding_model="en.embed_sentence.bert_base_uncased",
        # model_format="johnsnowlabs",
        document_store=document_store,
        use_gpu=False,
    )
    document_store.update_embeddings(retriever)

    pipe = Pipeline()
    # pipe.add_node(component=processor, name="Preprocess", inputs=["Query"])
    pipe.add_node(component=processor, name="Preprocess", inputs=["Query"])
    pipe.add_node(component=retriever, name="Embed&Retrieve", inputs=["Query"])
    result = pipe.run(documents=get_docs(), query="lol")
    print(result)
