from johnsnowlabs import try_import_lib

if try_import_lib("haystack"):
    from johnsnowlabs.frameworks.embedding_retrieval.haystack_node import (
        JohnSnowLabsHaystackEmbedder,
        JohnSnowLabsHaystackDocumentSplitter,
        JohnSnowLabsHaystackMedicalDocumentSplitter,
    )

if try_import_lib("langchain"):
    from johnsnowlabs.frameworks.embedding_retrieval.langchain_node import (
        JohnSnowLabsLangChainEmbedder,
        JohnSnowLabsLangChainDocumentSplitter,
        JohnSnowLabsLangChainMedicalDocumentSplitter,
    )
