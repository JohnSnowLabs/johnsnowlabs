from johnsnowlabs.auto_install.softwares import Software
from johnsnowlabs.utils.print_messages import log_outdated_lib, log_broken_lib
from johnsnowlabs.abstract_base.lib_resolver import try_import_lib

warning_logged = False

try:
    if try_import_lib('sparknlp_jsl') and try_import_lib('sparknlp'):
        # Pretrained
        from sparknlp_jsl.annotator import \
            AssertionLogRegModel, \
            AssertionDLModel, \
            DeIdentificationModel, \
            DocumentLogRegClassifierModel, \
            RelationExtractionModel, \
            RelationExtractionDLModel, \
            ChunkMergeModel, \
            SentenceEntityResolverModel, \
            ChunkMapperModel, \
            BertSentenceChunkEmbeddings, \
            ChunkKeyPhraseExtraction, \
            NerDisambiguatorModel, \
            EntityChunkEmbeddings, \
            ZeroShotRelationExtractionModel, \
            TFGraphBuilder, \
            ChunkConverter, \
            ChunkFilterer, \
            NerConverterInternal, \
            NerChunker, \
            AssertionFilterer, \
            AnnotationMerger, \
            RENerChunksFilter, \
            ChunkSentenceSplitter, \
            DrugNormalizer, \
            ChunkMapperFilterer, \
            DateNormalizer, \
            GenericClassifierModel, \
            ReIdentification, \
            ZeroShotNerModel
        from sparknlp_jsl.structured_deidentification import StructuredDeidentification

        from sparknlp_jsl.base import FeaturesAssembler

        from sparknlp_jsl.annotator import \
            AssertionLogRegApproach, \
            AssertionDLApproach, \
            DeIdentification, \
            DocumentLogRegClassifierApproach, \
            RelationExtractionApproach, \
            ChunkMergeApproach, \
            SentenceEntityResolverApproach, \
            ChunkMapperApproach, \
            NerDisambiguator, \
            ContextualParserApproach, \
            GenericClassifierApproach, \
            Router, \
            NerQuestionGenerator, \
            DocumentHashCoder

        from sparknlp_jsl.annotator.resolution.resolver_merger import ResolverMerger

        from sparknlp_jsl.annotator import MedicalNerModel as NerModel
        from sparknlp_jsl.annotator import MedicalNerApproach as NerApproach
        from sparknlp_jsl.annotator import MedicalBertForTokenClassifier as BertForTokenClassifier
        from sparknlp_jsl.annotator import \
            MedicalDistilBertForSequenceClassification as DistilBertForSequenceClassification
        from sparknlp_jsl.annotator import MedicalBertForSequenceClassification as BertForSequenceClassification
        from sparknlp_jsl.compatibility import Compatibility
        from sparknlp_jsl.pretrained import InternalResourceDownloader
        from sparknlp_jsl.eval import NerDLMetrics, NerDLEvaluation, SymSpellEvaluation, POSEvaluation, \
            NerCrfEvaluation, NorvigSpellEvaluation

        # from sparknlp.base import *
        # from sparknlp.annotator import *
        # from sparknlp_jsl.annotator import *
        # from sparknlp_jsl.base import *

        # FinanceBertForSequenceClassification,\
        # FinanceNerModel,\
        # FinanceBertForTokenClassification,\
        # LegalNerModel,\
        # LegalBertForTokenClassification,\
        # LegalBertForSequenceClassification

        from sparknlp_jsl.functions import *
        from sparknlp_jsl.training import *
except:
    log_broken_lib(Software.spark_hc)

if try_import_lib('sparknlp_jsl') and try_import_lib('sparknlp'):
    if not Software.spark_hc.check_installed_correct_version() and not warning_logged:
        warning_logged = True
        import sparknlp_jsl
        log_outdated_lib(Software.spark_hc, sparknlp_jsl.version())
