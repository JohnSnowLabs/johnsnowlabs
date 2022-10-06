from johnsnowlabs.abstract_base.lib_resolver import try_import_lib
from johnsnowlabs.utils.print_messages import log_broken_lib

try :
    if try_import_lib('sparknlp_jsl') and try_import_lib('sparknlp'):

        # Substitutions
        from sparknlp_jsl.legal import LegalBertForTokenClassification as BertForTokenClassification
        from sparknlp_jsl.legal import LegalNerApproach as NerApproach
        from sparknlp_jsl.legal import LegalNerModel as NerModel
        from sparknlp_jsl.legal import LegalBertForSequenceClassification as BertForSequenceClassification
        from sparknlp_jsl.legal import LegalBertForSequenceClassification as BertForSequenceClassification
        from sparknlp_jsl.legal import LegalClassifierDLApproach as ClassifierDLApproach
        from sparknlp_jsl.legal import LegalClassifierDLModel as ClassifierDLModel
        from sparknlp_jsl.annotator import MedicalDistilBertForSequenceClassification as DistilBertForSequenceClassification
        # from sparknlp_jsl.legal import LegalDocumentHashCoder as DocumentHashCoder
        # from sparknlp_jsl.legal import LegalNerQuestionGenerator as QuestionGenerator
        from sparknlp_jsl.legal.chunk_classification.deid.document_hashcoder import LegalDocumentHashCoder as DocumentHashCoder
        from sparknlp_jsl.legal.seq_generation.qa_ner_generator import LegalNerQuestionGenerator as NerQuestionGenerator



        from sparknlp_jsl.finance import SentenceEntityResolverModel, \
            ChunkMapperModel, \
            AssertionDLModel, \
            RelationExtractionDLModel, \
            ZeroShotRelationExtractionModel, \
            ChunkMapperApproach, \
            SentenceEntityResolverApproach, \
            AssertionDLApproach, \
            ZeroShotNerModel

        # These are licensed annos shared across all libs
        from sparknlp_jsl.annotator import \
            AssertionLogRegModel, \
            DeIdentificationModel, \
            DocumentLogRegClassifierModel, \
            RelationExtractionModel, \
            ChunkMergeModel, \
            ChunkMapperModel, \
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
        # DrugNormalizer, \
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

        pass

except:
    if try_import_lib('sparknlp_jsl') and try_import_lib('sparknlp'):
        log_broken_lib('Enterprise Finance')
