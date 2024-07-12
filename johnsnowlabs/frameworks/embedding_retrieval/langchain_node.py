import os
import sys
from typing import Any, List

from langchain.embeddings.base import Embeddings

# from langchain.pydantic_v1 import BaseModel, Extra
from pydantic import BaseModel, Extra

from johnsnowlabs.frameworks.embedding_retrieval.utils import (
    get_docsplitter_pipe,
    get_doc_splitter_internal_pipe,
)


class JohnSnowLabsLangChainEmbedder(BaseModel, Embeddings):
    """JohnSnowLabs embedding models

    To use, you should have the ``johnsnowlabs`` python package installed.
    Example:        .. code-block:: python
            from langchain.embeddings.johnsnowlabs import JohnSnowLabsEmbeddings
            document = "foo bar"
            embedding = JohnSnowLabsEmbeddings('embed_sentence.bert')
            output = embedding.embed_query(document)
    """

    async def aembed_documents(self, texts: List[str]) -> List[List[float]]:
        raise NotImplementedError("JohnSnowLabsEmbeddings does not support async yet")

    async def aembed_query(self, text: str) -> List[float]:
        raise NotImplementedError("JohnSnowLabsEmbeddings does not support async yet")

    model: Any

    def __init__(
        self, model="embed_sentence.bert", hardware_target="cpu", **kwargs: Any
    ):
        """Initialize the johnsnowlabs model."""
        super().__init__(**kwargs)
        # 1) Check imports
        try:
            from johnsnowlabs import nlp
            from nlu.pipe.pipeline import NLUPipeline
        except ImportError as exc:
            raise ImportError(
                "Could not import johnsnowlabs python package. "
                "Please install it with `pip install johnsnowlabs`."
            ) from exc

            # 2) Start a Spark Session
        try:
            os.environ["PYSPARK_PYTHON"] = sys.executable
            os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
            nlp.start(hardware_target=hardware_target)
        except Exception as exc:
            raise Exception("Failure starting Spark Session") from exc
            # 3) Load the model
        try:
            if isinstance(model, str):
                self.model = nlp.load(model)
            elif isinstance(model, NLUPipeline):
                self.model = model
            else:
                self.model = nlp.to_nlu_pipe(model)
        except Exception as exc:
            raise Exception("Failure loading model") from exc

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Compute doc embeddings using a JohnSnowLabs transformer model.

        Args:            texts: The list of texts to embed.
        Returns:            List of embeddings, one for each text."""

        return self.model.predict_embeds(texts)

    def embed_query(self, text: str) -> List[float]:
        """Compute query embeddings using a JohnSnowLabs transformer model.
        Args:            text: The text to embed.
        Returns:            Embeddings for the text."""
        return self.model.predict_embeds(text)[0]


class JohnSnowLabsLangChainDocumentSplitter:
    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 0,
        split_patterns: list = ["\n\n", "\n", " ", ""],
        explode_splits: bool = True,
        keep_separators: bool = True,
        patterns_are_regex: bool = False,
        trim_whitespace: bool = True,
    ):
        """
        :param chunk_size: Size of each chunk of text.
        :param chunk_overlap: Length of the overlap between text chunks , by default `0`.
        :param split_patterns: Patterns to separate the text by in decreasing priority , by default `["\n\n", "\n", " ", ""]`.
        :param explode_splits: Whether to explode split chunks to separate rows , by default `True`.
        :param keep_separators: Whether to keep the separators in the final result , by default `True`.
        :param patterns_are_regex: Whether to interpret the split patterns as regular expressions , by default `False`.
        :param trim_whitespace: Whether to trim whitespaces of extracted chunks , by default `True`.
        """
        self.pipe = get_docsplitter_pipe(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            split_patterns=split_patterns,
            explode_splits=explode_splits,
            keep_separators=keep_separators,
            patterns_are_regex=patterns_are_regex,
            trim_whitespace=trim_whitespace,
        )

    def split_documents(self, docs):
        return split_lang_docs(self.pipe, docs)


class JohnSnowLabsLangChainMedicalDocumentSplitter(JohnSnowLabsLangChainDocumentSplitter):
    def __init__(
        self,
        # Splitter params
        split_mode: str = "recursive",
        chunk_size: int = 500,
        chunk_overlap: int = 0,
        split_patterns: list = None,    # different value for split modes
        explode_splits: bool = True,
        keep_separators: bool = True,
        patterns_are_regex: bool = False,
        trim_whitespace: bool = True,
        sentence_awareness: bool = False,
        max_length: int = None,         # different value for split modes
        custom_bounds_strategy: str = "prepend",
        case_sensitive: bool = False,
        meta_data_fields: list = [],
        enable_sentence_increment: bool = False,
        # Tokenizer Params
        tokenizer_target_pattern: str = None,
        tokenizer_prefix_pattern: str = None,
        tokenizer_suffix_pattern: str = None,
        tokenizer_infix_patterns: list = None,
        tokenizer_exceptions: list = None,
        tokenizer_exceptions_path: str = None,
        tokenizer_case_sensitive_exceptions: bool = None,
        tokenizer_context_chars: list = None,
        tokenizer_split_pattern: str = None,
        tokenizer_split_chars: list = None,
        tokenizer_min_length: int = None,
        tokenizer_max_length: int = None,
        # Sentence Detector Params
        sentence_model_architecture: str = None,
        sentence_explode_sentences: bool = None,
        sentence_custom_bounds: list = None,
        sentence_use_custom_bounds_only: bool = None,
        sentence_split_length: int = None,
        sentence_min_length: int = None,
        sentence_max_length: int = None,
        sentence_impossible_penultimates: list = None,
    ):
        """
        :param split_mode: The split mode to determine how text should be segmented. Default: 'recursive'.
            It should be one of the following values:
                - "char": Split text based on individual characters.
                - "token": Split text based on tokens.
                - "sentence": Split text based on sentences.
                - "recursive": Split text recursively using a specific algorithm.
                - "regex": Split text based on a regular expression pattern.
        :param chunk_size: Size of each chunk of text. This param is applicable only for "recursive" split_mode.
        :param chunk_overlap: Length of the overlap between text chunks , by default `0`. This param is applicable only for "recursive" split_mode.
        :param split_patterns: Patterns to separate the text by in decreasing priority , by default `["\n\n", "\n", " ", ""]`.
        :param explode_splits: Whether to explode split chunks to separate rows , by default `True`.
        :param keep_separators: Whether to keep the separators in the final result , by default `True`.
        :param patterns_are_regex: Whether to interpret the split patterns as regular expressions , by default `False`.
        :param trim_whitespace: Whether to trim whitespaces of extracted chunks , by default `True`.
        :param sentence_awareness: Whether to split the document by sentence awareness if possible. Default: False.
            If true, it can stop the split process before maxLength. This param is not applicable only for "regex" and "recursive" split_mode.
        :param max_length: The maximum length allowed for spitting. The mode in which the maximum length is specified:
            - "char": Maximum length is measured in characters. Default: 512
            - "token": Maximum length is measured in tokens. Default: 128
            - "sentence": Maximum length is measured in sentences. Default: 8
        :param custom_bounds_strategy: The custom bounds strategy for text splitting using regular expressions.
            This param is applicable only for "regex" split_mode. It should be one of the following values:
                - "none": No custom bounds are applied.
                - "prepend": Custom bounds are prepended to the split documents.
                - "append": Custom bounds are appended to the split documents.
                - Default: "prepend".
        :param case_sensitive: Whether to use case sensitive when matching regex, by default `False`.
        :param meta_data_fields: Metadata fields to add specified data in columns to the metadata of the split documents.
            You should set column names to read columns.
        :param enable_sentence_increment: Whether the sentence index should be incremented in the metadata of the annotator. Default: False.

        Tokenizer parameters
        --------------------
        :param tokenizer_target_pattern: Pattern to grab from text as token candidates, by default ``\\S+``
        :param tokenizer_prefix_pattern: Regex with groups and begins with ``\\A`` to match target prefix, by default ``\\A([^\\s\\w\\$\\.]*)``
        :param tokenizer_suffix_pattern: Regex with groups and ends with ``\\z`` to match target suffix, by default ``([^\\s\\w]?)([^\\s\\w]*)\\z``
        :param tokenizer_infix_patterns: Regex patterns that match tokens within a single target. groups identify different sub-tokens. multiple defaults
        :param tokenizer_exceptions: Words that won't be affected by tokenization rules
        :param tokenizer_exceptions_path: Path to txt file with list of token exceptions
        :param tokenizer_case_sensitive_exceptions: Whether to care for case sensitiveness in exceptions, by default True
        :param tokenizer_context_chars: Character list used to separate from token boundaries, by default ['.', ',', ';', ':', '!', '?', '*', '-', '(', ')', '"', "'"]
        :param tokenizer_split_pattern: Pattern to separate from the inside of tokens. Takes priority over splitChars.
        :param tokenizer_split_chars: Character list used to separate from the inside of tokens
        :param tokenizer_min_length: The minimum allowed length for each token, by default 0
        :param tokenizer_max_length: The maximum allowed length for each token, by default 99999

        SentenceDetectorDLModel parameters
        ----------------------------------
        :param sentence_model_architecture: Model architecture (CNN)
        :param sentence_explode_sentences: Whether to explode each sentence into a different row, for better parallelization. Defaults to false.
        :param sentence_custom_bounds: Characters used to explicitly mark sentence bounds, by default []
        :param sentence_use_custom_bounds_only: Only utilize custom bounds in sentence detection, by default False
        :param sentence_split_length: Length at which sentences will be forcibly split
        :param sentence_min_length: The minimum allowed length for each sentence, by default 0
        :param sentence_max_length: The maximum allowed length for each sentence, by default 99999
        :param sentence_impossible_penultimates: Impossible penultimates - list of strings which a sentence can't end with
        """
        self.pipe = get_doc_splitter_internal_pipe(
            split_mode=split_mode,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            split_patterns=split_patterns,
            explode_splits=explode_splits,
            keep_separators=keep_separators,
            patterns_are_regex=patterns_are_regex,
            trim_whitespace=trim_whitespace,
            sentence_awareness=sentence_awareness,
            max_length=max_length,
            custom_bounds_strategy=custom_bounds_strategy,
            case_sensitive=case_sensitive,
            meta_data_fields=meta_data_fields,
            enable_sentence_increment=enable_sentence_increment,
            # Tokenizer Params
            tokenizer_target_pattern=tokenizer_target_pattern,
            tokenizer_prefix_pattern=tokenizer_prefix_pattern,
            tokenizer_suffix_pattern=tokenizer_suffix_pattern,
            tokenizer_infix_patterns=tokenizer_infix_patterns,
            tokenizer_exceptions=tokenizer_exceptions,
            tokenizer_exceptions_path=tokenizer_exceptions_path,
            tokenizer_case_sensitive_exceptions=tokenizer_case_sensitive_exceptions,
            tokenizer_context_chars=tokenizer_context_chars,
            tokenizer_split_pattern=tokenizer_split_pattern,
            tokenizer_split_chars=tokenizer_split_chars,
            tokenizer_min_length=tokenizer_min_length,
            tokenizer_max_length=tokenizer_max_length,
            # Sentence Detector Params
            sentence_model_architecture=sentence_model_architecture,
            sentence_explode_sentences=sentence_explode_sentences,
            sentence_custom_bounds=sentence_custom_bounds,
            sentence_use_custom_bounds_only=sentence_use_custom_bounds_only,
            sentence_split_length=sentence_split_length,
            sentence_min_length=sentence_min_length,
            sentence_max_length=sentence_max_length,
            sentence_impossible_penultimates=sentence_impossible_penultimates,
        )


def split_lang_doc(pipe, doc):
    from langchain.schema.document import Document

    return [
        Document(page_content=split, metadata=doc.metadata)
        for split in pipe.annotate(doc.page_content)["splits"]
    ]


def split_lang_docs(pipe, docs):
    return [split for doc in docs for split in split_lang_doc(pipe, doc)]
