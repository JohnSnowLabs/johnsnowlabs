# Embedder Node compatible with haystack framework
import os
import sys
from pathlib import Path
from typing import List, Optional, Union, Dict, Any, Tuple

import numpy as np
from haystack import BaseComponent
from haystack.document_stores import BaseDocumentStore
from haystack.nodes.retriever import EmbeddingRetriever
from haystack.nodes.retriever._base_embedding_encoder import _BaseEmbeddingEncoder
from haystack.schema import Document, MultiLabel
from tqdm.auto import tqdm

from johnsnowlabs.frameworks.embedding_retrieval.utils import (
    get_docsplitter_pipe,
    get_doc_splitter_internal_pipe,
)


class _JohnsnowlabsEmbeddingEncoder(_BaseEmbeddingEncoder):
    def __init__(self, retriever: "EmbeddingRetriever"):
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
            nlp.start(hardware_target="gpu" if retriever.use_gpu else "cpu")
        except Exception as exc:
            raise Exception("Failure starting Spark Session") from exc
            # 3) Load the model
        try:
            self.embedding_model = nlp.load(retriever.embedding_model)
        except Exception as exc:
            raise Exception("Failure loading model") from exc

    def embed(self, texts: Union[List[str], str]) -> np.ndarray:
        return np.asarray(
            self.embedding_model.predict_embeds(texts),
            dtype=float,
        )

    def embed_queries(self, queries: List[str]) -> np.ndarray:
        return self.embed(queries)

    def embed_documents(self, docs: List[Document]) -> np.ndarray:
        return self.embed([d.content for d in docs])

    def train(
        **kwargs,
    ):
        raise NotImplementedError("Training not supported")

    def save(self, save_dir: Union[Path, str]):
        raise NotImplementedError("Saving not supported")


class JohnSnowLabsHaystackEmbedder(EmbeddingRetriever):
    def __init__(
        self,
        embedding_model: str,
        use_gpu: bool = False,
        document_store: Optional[BaseDocumentStore] = None,
        **kwargs,
    ):
        inject()
        kwargs["model_format"] = "johnsnowlabs"
        super().__init__(
            embedding_model=embedding_model,
            document_store=document_store,
            use_gpu=use_gpu,
            **kwargs,
        )


class JohnSnowLabsHaystackDocumentSplitter(BaseComponent):  # BasePreProcessor
    outgoing_edges = 1

    def __init__(
        self,
        chunk_size=500,
        chunk_overlap=0,
        split_patterns=["\n\n", "\n", " ", ""],
        explode_splits=True,
        keep_separators=True,
        patterns_are_regex=False,
        trim_whitespace=True,
        ##### OLD PARAMS #####
        progress_bar: bool = True,
    ):
        """
        :param chunk_size: Size of each chunk of text.
        :param chunk_overlap: Length of the overlap between text chunks , by default `0`.
        :param split_patterns: Patterns to separate the text by in decreasing priority , by default `["\n\n", "\n", " ", ""]`.
        :param explode_splits: Whether to explode split chunks to separate rows , by default `True`.
        :param keep_separators: Whether to keep the separators in the final result , by default `True`.
        :param patterns_are_regex: Whether to interpret the split patterns as regular expressions , by default `False`.
        :param trim_whitespace: Whether to trim whitespaces of extracted chunks , by default `True`.
        :param progress_bar: Whether to show a progress bar.
        """
        super().__init__()
        self.progress_bar = progress_bar
        self.pipe = get_docsplitter_pipe(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            split_patterns=split_patterns,
            explode_splits=explode_splits,
            keep_separators=keep_separators,
            patterns_are_regex=patterns_are_regex,
            trim_whitespace=trim_whitespace,
        )

    def process(
        self,
        documents: Union[dict, Document, List[Union[dict, Document]]] = None,
    ) -> List[Document]:
        """
        Perform document cleaning and splitting. Can take a single document or a list of documents as input and returns a list of documents.
        """
        if isinstance(documents, (Document, dict)):
            ret = self._process_single(document=documents)
        elif isinstance(documents, list):
            ret = self._process_batch(documents=list(documents))
        elif documents is None:
            ret = []
        else:
            raise Exception(
                f"documents provided to PreProcessor.prepreprocess() is not of type list nor Document or None but is {type(documents)} "
            )

        return ret

    def _process_single(
        self,
        document: Union[dict, Document],
    ) -> List[Document]:
        return self.split(document=self.clean(document=document))

    def _process_batch(self, documents: List[Union[dict, Document]]) -> List[Document]:
        nested_docs = [
            self._process_single(d)
            for d in tqdm(
                documents,
                disable=not self.progress_bar,
                desc="Preprocessing",
                unit="docs",
            )
        ]
        return [d for x in nested_docs for d in x]

    def clean(
        self,
        document: Union[dict, Document],
        # not implemented
        clean_whitespace: bool = None,
        clean_header_footer: bool = None,
        clean_empty_lines: bool = None,
        remove_substrings: Optional[List[str]] = None,
    ) -> Document:
        """
        Stub for Feature cleaning procedure
        """
        return document

    def split(
        self,
        document: Union[dict, Document],
    ) -> List[Document]:
        """Perform document splitting on a single document. This method can split on different units, at different lengths,
        with different strides. It can also respect sentence boundaries. Its exact functionality is defined by
        the parameters passed into PreProcessor.__init__(). Takes a single document as input and returns a list of documents.
        """
        # Todo pass params dynamically?
        text = document.content
        texts = [split for split in self.pipe.annotate(text)["splits"]]
        return [
            Document(id_hash_keys=["content", "meta"], content=text, meta=document.meta)
            for i, text in enumerate(texts)
        ]

    def run(
        self,
        query: Optional[str] = None,
        file_paths: Optional[List[str]] = None,
        labels: Optional[MultiLabel] = None,
        documents: Optional[List[Document]] = None,
        meta: Optional[dict] = None,
    ) -> Tuple[Dict, str]:
        """
        Method that will be executed when the node in the graph is called.

        The argument that are passed can vary between different types of nodes
        (e.g. retriever nodes expect different args than a reader node)

        See an example for an implementation in haystack/reader/base/BaseReader.py
        :return:
        """
        # result = {"documents": d.to_dict() for d in self.process(documents)}
        result = {"documents": d for d in self.process(documents)}
        return result, "output_1"

    def run_batch(
        self,
        queries: Optional[Union[str, List[str]]] = None,
        file_paths: Optional[List[str]] = None,
        labels: Optional[Union[MultiLabel, List[MultiLabel]]] = None,
        documents: Optional[Union[List[Document], List[List[Document]]]] = None,
        meta: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None,
        params: Optional[dict] = None,
        debug: Optional[bool] = None,
    ):
        result = {"documents": d for d in self.process(documents)}
        return result, "output_1"


class JohnSnowLabsHaystackMedicalDocumentSplitter(
    JohnSnowLabsHaystackDocumentSplitter
):  # BasePreProcessor
    outgoing_edges = 1

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
        # Haystack Params
        progress_bar: bool = True,
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
        :param tokenizer_exceptions_path: Path to file containing list of exceptions
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

        :param progress_bar: Whether to show a progress bar.
        """
        super().__init__()
        self.progress_bar = progress_bar

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
            sentence_model_architecture=sentence_model_architecture,
            sentence_explode_sentences=sentence_explode_sentences,
            sentence_custom_bounds=sentence_custom_bounds,
            sentence_use_custom_bounds_only=sentence_use_custom_bounds_only,
            sentence_split_length=sentence_split_length,
            sentence_min_length=sentence_min_length,
            sentence_max_length=sentence_max_length,
            sentence_impossible_penultimates=sentence_impossible_penultimates,
        )


def inject():
    # inject the emd encoder into haystack
    from haystack.nodes.retriever import _embedding_encoder

    _embedding_encoder._EMBEDDING_ENCODERS[
        "johnsnowlabs"
    ] = _JohnsnowlabsEmbeddingEncoder
    # inject the retriever into haystack


inject()

# if id_hash_keys is None:
#     id_hash_keys = self.id_hash_keys
#
# if isinstance(document, dict):
#     document["id_hash_keys"] = id_hash_keys
#     document = Document.from_dict(document)
#
# # Mainly needed for type checking
# if not isinstance(document, Document):
#     raise HaystackError(
#         "Document must not be of type 'dict' but of type 'Document'."
#     )
#
# if type(document.content) is not str:
#     return document
#
# text = document.content
# # TODO APPLY PIPE
# self.pipe.annotate(text)
# texts = [split for split in self.pipe.annotate(text)["splits"]]
# if text != document.content:
#     document = deepcopy(document)
#     document.content = text
# return document
