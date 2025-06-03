import traceback

from johnsnowlabs.abstract_base.lib_resolver import try_import_lib
from johnsnowlabs.utils.env_utils import reverse_compatibility_import
from johnsnowlabs.utils.print_messages import log_broken_lib

try:
    if try_import_lib("sparknlp_jsl") and try_import_lib("sparknlp"):
        from sparknlp_jsl.functions import *
        from sparknlp_jsl.training import *
        from sparknlp_jsl.utils import *
        from sparknlp_jsl.structured_deidentification import StructuredDeidentification
        from sparknlp_jsl.base import FeaturesAssembler
        from sparknlp_jsl.finance.token_classification.ner.zero_shot_ner import ZeroShotNerModel
        from sparknlp_jsl.training_log_parser import ner_log_parser

        from sparknlp_jsl.finance import (
            GenericClassifierModel,
            FinanceNerQuestionGenerator as NerQuestionGenerator,
            FinanceDocumentHashCoder as DocumentHashCoder,
            FinanceBertForTokenClassification as BertForTokenClassification,
            FinanceDocumentMLClassifierModel as DocumentMLClassifierModel,
            FinanceDocumentMLClassifierApproach as DocumentMLClassifierApproach,
            DocMapperApproach,
            DocMapperModel,
            FinanceNerApproach as NerApproach,
            FinanceNerModel as NerModel,
            FinanceClassifierDLModel as ClassifierDLModel,
            FinanceBertForSequenceClassification as BertForSequenceClassification,
            FinanceBertForSequenceClassification as BertForSequenceClassification,
            FinanceClassifierDLApproach as ClassifierDLApproach,
            DocMapperModel,
            DocMapperApproach,
            SentenceEntityResolverModel,
            ChunkMapperModel,
            AssertionDLModel,
            RelationExtractionDLModel,
            ZeroShotRelationExtractionModel,
            ChunkMapperApproach,
            SentenceEntityResolverApproach,
            AssertionDLApproach,
            FinanceQuestionAnswering as QuestionAnswering,
            FinanceTextGenerator as TextGenerator,
            FinanceSummarizer as Summarizer,
            FinanceFewShotClassifierModel as FewShotClassifierModel,
            FinanceFewShotClassifierApproach as FewShotClassifierApproach,
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
            BertSentenceChunkEmbeddings,
            ChunkKeyPhraseExtraction,
            NerDisambiguatorModel,
            EntityChunkEmbeddings,
            TFGraphBuilder,
            ChunkConverter,
            ChunkFilterer,
            NerConverterInternal,
            NerConverterInternal as NerConverter,
            NerChunker,
            AssertionFilterer,
            AnnotationMerger,
            RENerChunksFilter,
            ChunkSentenceSplitter,
            ChunkMapperFilterer,
            DateNormalizer,
            GenericClassifierModel,
            ReIdentification,
            AssertionLogRegApproach,
            DeIdentification,
            DocumentLogRegClassifierApproach,
            RelationExtractionApproach,
            ChunkMergeApproach,
            NerDisambiguator,
            ContextualParserApproach,
            GenericClassifierApproach,
            Router,
            Replacer,
            ContextualParserModel,
            NameChunkObfuscatorApproach,
            NameChunkObfuscator,
            Resolution2Chunk,
            ResolverMerger,
            NerTemplateRenderModel,
            AverageEmbeddings,
            Doc2ChunkInternal,
            Chunk2Token,
            ExtractiveSummarization,
            ChunkFiltererApproach,
            InternalDocumentSplitter as DocumentSplitter,
            Text2SQL,
            IOBTagger,
            DocumentFiltererByClassifier,
            Flattener,
            EntityRulerInternalApproach as EntityRulerApproach,
            EntityRulerInternalModel as EntityRulerModel,
            TextMatcherInternal as TextMatcher,
            TextMatcherInternalModel as TextMatcherModel,
            RegexMatcherInternal as RegexMatcher,
            RegexMatcherInternalModel as RegexMatcherModel,
            AssertionMerger,
            LightDeIdentification,
            WindowedSentenceModel,
            MultiChunk2Doc,
            FewShotAssertionClassifierModel,
            FewShotAssertionClassifierApproach,
            FewShotAssertionSentenceConverter,
            VectorDBPostProcessor,
            ContextSplitAssembler,
            ContextualAssertion,
            LargeFewShotClassifierModel,
            Mapper2Chunk,
            DocumentFiltererByNER,
            REChunkMerger,
            ContextualEntityFilterer,
            ContextualEntityRuler,
            PretrainedZeroShotNER,
            StructuredJsonConverter,
            BertForAssertionClassification,
            FhirDeIdentification,
            AnnotationConverter
        )

        from sparknlp_jsl.modelTracer import ModelTracer
        from sparknlp_jsl.pipeline_tracer import PipelineTracer
        from sparknlp_jsl.pipeline_output_parser import PipelineOutputParser
        from sparknlp_jsl.updateModels import UpdateModels
        from sparknlp_jsl.text_to_documents_columns import TextToDocumentsColumns
        from sparknlp_jsl import training_log_parser, Deid
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
        print("Performing reverse compatibility import for legal module")
        reverse_compatibility_import(__file__, globals())
