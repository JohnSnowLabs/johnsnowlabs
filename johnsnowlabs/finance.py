
from johnsnowlabs.abstract_base.lib_resolver import try_import_lib
from johnsnowlabs.utils.print_messages import log_broken_lib

try:

    if try_import_lib('sparknlp_jsl') and try_import_lib('sparknlp'):
        # Substitutions
        from sparknlp_jsl.finance import FinanceBertForTokenClassification as BertForTokenClassification
        from sparknlp_jsl.finance import FinanceNerApproach as NerApproach
        from sparknlp_jsl.finance import FinanceNerModel as NerModel
        from sparknlp_jsl.finance import FinanceBertForSequenceClassification as BertForSequenceClassification
        from sparknlp_jsl.finance import FinanceBertForSequenceClassification as BertForSequenceClassification
        from sparknlp_jsl.finance import FinanceClassifierDLApproach as ClassifierDLApproach
        from sparknlp_jsl.finance import FinanceClassifierDLModel as ClassifierDLModel
        # from sparknlp_jsl.finance import FinanceDocumentHashCoder as DocumentHashCoder
        # from sparknlp_jsl.finance import FinanceNerQuestionGenerator as QuestionGenerator
        from sparknlp_jsl.finance.chunk_classification.deid.document_hashcoder import FinanceDocumentHashCoder as DocumentHashCoder
        from sparknlp_jsl.finance.seq_generation.qa_ner_generator import FinanceNerQuestionGenerator as NerQuestionGenerator

        from sparknlp_jsl.finance import SentenceEntityResolverModel, \
            ChunkMapperModel, \
            AssertionDLModel, \
            RelationExtractionDLModel, \
            ZeroShotRelationExtractionModel, \
            ChunkMapperApproach, \
            SentenceEntityResolverApproach, \
            AssertionDLApproach, \
            ZeroShotNerModel

        from sparknlp_jsl.annotator import MedicalDistilBertForSequenceClassification as DistilBertForSequenceClassification

        # These are licensed annos shared across all libs
        from sparknlp_jsl.annotator import \
            AssertionLogRegModel, \
            DeIdentificationModel, \
            DocumentLogRegClassifierModel, \
            RelationExtractionModel, \
            ChunkMergeModel, \
            BertSentenceChunkEmbeddings, \
            ChunkKeyPhraseExtraction, \
            NerDisambiguatorModel, \
            EntityChunkEmbeddings, \
            TFGraphBuilder, \
            ChunkConverter, \
            ChunkFilterer, \
            NerConverterInternal, \
            NerChunker, \
            AssertionFilterer, \
            AnnotationMerger, \
            RENerChunksFilter, \
            ChunkSentenceSplitter, \
            ChunkMapperFilterer, \
            DateNormalizer, \
            GenericClassifierModel, \
            ReIdentification

        from sparknlp_jsl.structured_deidentification import StructuredDeidentification
        from sparknlp_jsl.annotator.resolution.resolver_merger import ResolverMerger

        from sparknlp_jsl.base import FeaturesAssembler

        from sparknlp_jsl.annotator import \
            AssertionLogRegApproach, \
            DeIdentification, \
            DocumentLogRegClassifierApproach, \
            RelationExtractionApproach, \
            ChunkMergeApproach, \
            NerDisambiguator, \
            ContextualParserApproach, \
            GenericClassifierApproach, \
            Router, \
            NerQuestionGenerator, \
            DocumentHashCoder

        from sparknlp_jsl.compatibility import Compatibility
        from sparknlp_jsl.pretrained import InternalResourceDownloader
        from sparknlp_jsl.eval import NerDLMetrics, NerDLEvaluation, SymSpellEvaluation, POSEvaluation, \
            NerCrfEvaluation, NorvigSpellEvaluation

except:
    if try_import_lib('sparknlp_jsl') and try_import_lib('sparknlp'):
        log_broken_lib('Enterprise Finance')
