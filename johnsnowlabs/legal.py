import traceback

from johnsnowlabs.abstract_base.lib_resolver import try_import_lib
from johnsnowlabs.utils.print_messages import log_broken_lib

try:
    if try_import_lib("sparknlp_jsl") and try_import_lib("sparknlp"):
        from sparknlp_jsl.base import FeaturesAssembler

        from sparknlp_jsl.legal import (
            LegalDocumentHashCoder as DocumentHashCoder,
            LegalNerQuestionGenerator as NerQuestionGenerator,
            LegalBertForSequenceClassification as BertForSequenceClassification,
            LegalDocumentMLClassifierModel as DocumentMLClassifierModel,
            LegalDocumentMLClassifierApproach as DocumentMLClassifierApproach,
            DocMapperModel,
            DocMapperApproach,
            LegalBertForSequenceClassification as BertForSequenceClassification,
            LegalBertForTokenClassification as BertForTokenClassification,
            LegalNerApproach as NerApproach,
            LegalNerModel as NerModel,
            LegalClassifierDLApproach as ClassifierDLApproach,
            LegalClassifierDLModel as ClassifierDLModel,
            SentenceEntityResolverModel,
            ChunkMapperModel,
            AssertionDLModel,
            RelationExtractionDLModel,
            ZeroShotRelationExtractionModel,
            ChunkMapperApproach,
            SentenceEntityResolverApproach,
            AssertionDLApproach,
            ZeroShotNerModel,
        )

        # These are licensed annos shared across all libs
        from sparknlp_jsl.annotator import (
            GenericSVMClassifierApproach,
            GenericSVMClassifierModel,
            GenericLogRegClassifierApproach,
            GenericClassifierModel,
            SentenceDetector as TextSplitter,
            MedicalDistilBertForSequenceClassification as DistilBertForSequenceClassification,
            AssertionChunkConverter,
            AssertionLogRegModel,
            DeIdentificationModel,
            DocumentLogRegClassifierModel,
            RelationExtractionModel,
            ChunkMergeModel,
            ChunkMapperModel,
            BertSentenceChunkEmbeddings,
            ChunkKeyPhraseExtraction,
            NerDisambiguatorModel,
            EntityChunkEmbeddings,
            TFGraphBuilder,
            ChunkConverter,
            ChunkFilterer,
            NerConverterInternal,
            NerChunker,
            AssertionFilterer,
            AnnotationMerger,
            RENerChunksFilter,
            ChunkSentenceSplitter,
            ChunkMapperFilterer,
            DateNormalizer,
            GenericClassifierModel,
            ReIdentification,
            Replacer,
            ContextualParserModel,
            AssertionLogRegApproach,
            DeIdentification,
            DocumentLogRegClassifierApproach,
            RelationExtractionApproach,
            ChunkMergeApproach,
            NerDisambiguator,
            ContextualParserApproach,
            GenericClassifierApproach,
            Router,
            NerQuestionGenerator,
            AssertionChunkConverter,
            NameChunkObfuscatorApproach,
            NameChunkObfuscator,
            # Resolution2Chunk,
            ResolverMerger,
        )
        from sparknlp_jsl.modelTracer import ModelTracer

        from sparknlp_jsl.structured_deidentification import StructuredDeidentification

        from sparknlp_jsl import (training_log_parser, Deid)

        from sparknlp_jsl.compatibility import Compatibility
        from sparknlp_jsl.pretrained import InternalResourceDownloader
        from sparknlp_jsl.eval import (
            NerDLMetrics,
            NerDLEvaluation,
            SymSpellEvaluation,
            POSEvaluation,
            NerCrfEvaluation,
            NorvigSpellEvaluation,
        )


except Exception as err:
    if try_import_lib("sparknlp_jsl") and try_import_lib("sparknlp"):
        log_broken_lib("Enterprise Finance")
        print(f"Error Message : {err}")
        print(f"Error Trace: {traceback.format_exc()}")
