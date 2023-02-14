import traceback

from johnsnowlabs.abstract_base.lib_resolver import try_import_lib
from johnsnowlabs.auto_install.softwares import Software
from johnsnowlabs.utils.print_messages import log_outdated_lib, log_broken_lib

warning_logged = False

try:
    if try_import_lib("sparknlp_jsl") and try_import_lib("sparknlp"):
        # Pretrained
        from sparknlp_jsl.annotator import (
            GenericSVMClassifierApproach,
            GenericSVMClassifierModel,
            GenericLogRegClassifierApproach,
            GenericClassifierModel,
            AssertionLogRegModel,
            AssertionDLModel,
            DeIdentificationModel,
            DocumentLogRegClassifierModel,
            RelationExtractionModel,
            RelationExtractionDLModel,
            ChunkMergeModel,
            SentenceEntityResolverModel,
            ChunkMapperModel,
            BertSentenceChunkEmbeddings,
            ChunkKeyPhraseExtraction,
            NerDisambiguatorModel,
            EntityChunkEmbeddings,
            ZeroShotRelationExtractionModel,
            TFGraphBuilder,
            ChunkConverter,
            ChunkFilterer,
            NerConverterInternal,
            NerChunker,
            AssertionFilterer,
            AnnotationMerger,
            RENerChunksFilter,
            ChunkSentenceSplitter,
            DrugNormalizer,
            ChunkMapperFilterer,
            DateNormalizer,
            GenericClassifierModel,
            ReIdentification,
            ZeroShotNerModel,
            Replacer,
            AssertionChunkConverter,
            AssertionLogRegApproach,
            AssertionDLApproach,
            DeIdentification,
            DocumentLogRegClassifierApproach,
            RelationExtractionApproach,
            ChunkMergeApproach,
            SentenceEntityResolverApproach,
            ChunkMapperApproach,
            NerDisambiguator,
            ContextualParserApproach,
            ContextualParserModel,
            GenericClassifierApproach,
            Router,
            NerQuestionGenerator,
            DocumentHashCoder,
            DocMapperModel,
            DocMapperApproach,
            NameChunkObfuscatorApproach,
            NameChunkObfuscator,
            DocumentMLClassifierApproach,
            DocumentMLClassifierModel,
            Resolution2Chunk,
        )
        from sparknlp_jsl.structured_deidentification import StructuredDeidentification
        from sparknlp_jsl.modelTracer import ModelTracer
        from sparknlp_jsl import (training_log_parser, Deid)

        from sparknlp_jsl.base import FeaturesAssembler

        from sparknlp_jsl.annotator.resolution.resolver_merger import ResolverMerger

        from sparknlp_jsl.annotator import (
            MedicalDistilBertForSequenceClassification as DistilBertForSequenceClassification,
            MedicalBertForSequenceClassification as BertForSequenceClassification,
            MedicalBertForTokenClassifier as BertForTokenClassification,
            MedicalNerModel as NerModel,
            MedicalNerApproach as NerApproach,

        )
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

        from sparknlp_jsl.functions import *
        from sparknlp_jsl.training import *
except Exception as err:
    log_broken_lib(Software.spark_hc)
    print(f"Error Message : {err}")
    print(f"Error Trace: {traceback.format_exc()}")

if try_import_lib("sparknlp_jsl") and try_import_lib("sparknlp"):
    if not Software.spark_hc.check_installed_correct_version() and not warning_logged:
        warning_logged = True
        import sparknlp_jsl

        log_outdated_lib(Software.spark_hc, sparknlp_jsl.version())
