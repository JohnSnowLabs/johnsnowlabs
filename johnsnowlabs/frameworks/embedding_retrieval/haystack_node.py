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

from johnsnowlabs.frameworks.embedding_retrieval.utils import get_docsplitter_pipe


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


class JohnSnowLabsHaystackProcessor(BaseComponent):  # BasePreProcessor
    outgoing_edges = 1

    def __init__(
        self,
        chunk_overlap=2,
        chunk_size=20,
        explode_splits=True,
        keep_seperators=True,
        patterns_are_regex=False,
        split_patterns=["\n\n", "\n", " ", ""],
        trim_whitespace=True,
        ##### OLD PARAMS #####
        progress_bar: bool = True,
        add_page_number: bool = False,
        max_chars_check: int = 10_000,
    ):
        """
        :param clean_header_footer: Use heuristic to remove footers and headers across different pages by searching
                                     for the longest common string. This heuristic uses exact matches and therefore
                                     works well for footers like "Copyright 2019 by XXX", but won't detect "Page 3 of 4"
                                     or similar.
        :param clean_whitespace: Strip whitespaces before or after each line in the text.
        :param clean_empty_lines: Remove more than two empty lines in the text.
        :param remove_substrings: Remove specified substrings from the text. If no value is provided an empty list is created by default.
        :param split_by: Unit for splitting the document. Can be "word", "sentence", or "passage". Set to None to disable splitting.
        :param split_length: Max. number of the above split unit (e.g. words) that are allowed in one document. For instance, if n -> 10 & split_by ->
                           "sentence", then each output document will have 10 sentences.
        :param split_overlap: Word overlap between two adjacent documents after a split.
                              Setting this to a positive number essentially enables the sliding window approach.
                              For example, if split_by -> `word`,
                              split_length -> 5 & split_overlap -> 2, then the splits would be like:
                              [w1 w2 w3 w4 w5, w4 w5 w6 w7 w8, w7 w8 w10 w11 w12].
                              Set the value to 0 to ensure there is no overlap among the documents after splitting.
        :param split_respect_sentence_boundary: Whether to split in partial sentences if split_by -> `word`. If set
                                                to True, the individual split will always have complete sentences &
                                                the number of words will be <= split_length.
        :param language: The language used by "nltk.tokenize.sent_tokenize" in iso639 format.
            Available options: "ru","sl","es","sv","tr","cs","da","nl","en","et","fi","fr","de","el","it","no","pl","pt","ml"
        :param tokenizer_model_folder: Path to the folder containing the NTLK PunktSentenceTokenizer models, if loading a model from a local path. Leave empty otherwise.
        :param id_hash_keys: Generate the document id from a custom list of strings that refer to the document's
            attributes. If you want to ensure you don't have duplicate documents in your DocumentStore but texts are
            not unique, you can modify the metadata and pass e.g. `"meta"` to this field (e.g. [`"content"`, `"meta"`]).
            In this case the id will be generated by using the content and the defined metadata.
        :param progress_bar: Whether to show a progress bar.
        :param add_page_number: Add the number of the page a paragraph occurs in to the Document's meta
                                field `"page"`. Page boundaries are determined by `"\f"` character which is added
                                in between pages by `PDFToTextConverter`, `TikaConverter`, `ParsrConverter` and
                                `AzureConverter`.
        :param max_chars_check: the maximum length a document is expected to have. Each document that is longer than max_chars_check in characters after pre-processing will raise a warning.
        """
        super().__init__()
        self.progress_bar = progress_bar
        self.pipe = get_docsplitter_pipe(
            chunk_overlap,
            chunk_size,
            explode_splits,
            keep_seperators,
            patterns_are_regex,
            split_patterns,
            trim_whitespace,
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
