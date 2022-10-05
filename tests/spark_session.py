from johnsnowlabs import *
import unittest
import pkg_resources

# finance.ClassifierDLApproach()
class ImportTestCase(unittest.TestCase):
    def test_sparknlp_session(self):
        jsl.start()
        d = nlp.DocumentAssembler().setInputCol('text').setOutputCol('doc')
        t = nlp.Tokenizer().setInputCols('doc').setOutputCol('tok')
        c = nlp.DeBertaForTokenClassification().setInputCols(['tok', 'doc']).setOutputCol('class')
        p = Pipeline(stages=[d, t])
        p = nlu.to_nlu_pipe(p)
        print(p.predict("Hello World"))

    def test_sparknlp_gpu_session(self):
        jsl.start(hardware_target='gpu')
        d = nlp.DocumentAssembler().setInputCol('text').setOutputCol('doc')
        t = nlp.Tokenizer().setInputCols('doc').setOutputCol('tok')
        c = nlp.DeBertaForTokenClassification().setInputCols(['tok', 'doc']).setOutputCol('class')
        p = Pipeline(stages=[d, t])
        p = nlu.to_nlu_pipe(p)
        print(p.predict("Hello form John SNow labs"))

    def test_sparknlp_m1_session(self):
        import os
        jsl.start(hardware_target='m1')
        d = nlp.DocumentAssembler().setInputCol('text').setOutputCol('doc')
        t = nlp.Tokenizer().setInputCols('doc').setOutputCol('tok')
        c = nlp.DeBertaForTokenClassification().pretrained().setInputCols(['tok', 'doc']).setOutputCol('class')
        nlp.UniversalSentenceEncoder.pretrained()
        p = Pipeline(stages=[d, t])
        p = nlu.to_nlu_pipe(p)
        print(p.predict("Hello form John SNow labs"))

    def test_healthcare_session(self):
        jsl.start()
        d = nlp.DocumentAssembler().setInputCol('text').setOutputCol('doc')
        t = nlp.Tokenizer().setInputCols('doc').setOutputCol('tok')
        c = medical.BertForTokenClassifier().pretrained().setInputCols(['tok', 'doc']).setOutputCol('class')
        p = Pipeline(stages=[d, t, c])
        p = nlu.to_nlu_pipe(p)
        print(p.predict("Hello form John SNow labs"))

    def test_ocr_session(self):
        # Convert pdf to image
        p = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/4_1_LATEST_OCR_HC_BCK.json'
        spark = jsl.start(json_license_path=p)

        pdf_to_image = ocr.PdfToImage()
        pdf_to_image.setImageType(jsl.ocr.ImageType.TYPE_3BYTE_BGR)

        # Detect tables on the page using pretrained model
        # It can be finetuned for have more accurate results for more specific documents
        table_detector = ocr.ImageTableDetector.pretrained("general_model_table_detection_v2", "en", "clinical/ocr")
        table_detector.setInputCol("image")
        table_detector.setOutputCol("region")

        # Draw detected region's with table to the page
        draw_regions = ocr.ImageDrawRegions()
        draw_regions.setInputCol("image")
        draw_regions.setInputRegionsCol("region")
        draw_regions.setOutputCol("image_with_regions")
        draw_regions.setRectColor(jsl.ocr.Color.red)

        # Extract table regions to separate images
        splitter = ocr.ImageSplitRegions()
        splitter.setInputCol("image")
        splitter.setInputRegionsCol("region")
        splitter.setOutputCol("table_image")
        splitter.setDropCols("image")

        # Detect cells on the table image
        cell_detector = ocr.ImageTableCellDetector()
        cell_detector.setInputCol("table_image")
        cell_detector.setOutputCol("cells")
        cell_detector.setAlgoType("morphops")

        # Extract text from the detected cells
        table_recognition = ocr.ImageCellsToTextTable()
        table_recognition.setInputCol("table_image")
        table_recognition.setCellsCol('cells')
        table_recognition.setMargin(3)
        table_recognition.setStrip(True)
        table_recognition.setOutputCol('table')

        pipeline = PipelineModel(stages=[
            pdf_to_image,
            table_detector,
            draw_regions,
            splitter,
            cell_detector,
            table_recognition
        ])

        import pkg_resources
        pdf_example = pkg_resources.resource_filename('sparkocr', 'resources/ocr/pdfs/tabular-pdf/data.pdf')
        pdf_example_df = spark.read.format("binaryFile").load(pdf_example).cache()
        pipeline.transform(pdf_example_df).show()

    def test_legal_session(self):
        jsl.start()

        LightPipeline(self.get_legal_pipe()).fullAnnotate("Shwrm")

    def test_finance_session(self):
        jsl.start()
        LightPipeline(self.get_finance_pipe()).fullAnnotate("unit")

    @staticmethod
    def get_finance_pipe() -> PipelineModel:
        documentAssembler = DocumentAssembler() \
            .setInputCol("text") \
            .setOutputCol("ner_chunk")

        embeddings = UniversalSentenceEncoder.pretrained("tfhub_use", "en") \
            .setInputCols("ner_chunk") \
            .setOutputCol("sentence_embeddings")

        resolver = finance.SentenceEntityResolverModel.pretrained("finel_tickers2names", "en", "finance/models") \
            .setInputCols(["ner_chunk", "sentence_embeddings"]) \
            .setOutputCol("name") \
            .setDistanceFunction("EUCLIDEAN")

        return PipelineModel(
            stages=[
                documentAssembler,
                embeddings,
                resolver])

    @staticmethod
    def get_legal_pipe() -> PipelineModel:
        z = legal.ZeroShotRelationExtractionModel.pretrained("finre_zero_shot", "en", "finance/models")
        documentAssembler = DocumentAssembler() \
            .setInputCol("text") \
            .setOutputCol("ner_chunk")

        embeddings = UniversalSentenceEncoder.pretrained("tfhub_use", "en") \
            .setInputCols("ner_chunk") \
            .setOutputCol("sentence_embeddings")

        resolver = legal.SentenceEntityResolverModel.pretrained("legel_crunchbase_companynames", "en", "legal/models") \
            .setInputCols(["ner_chunk", "sentence_embeddings"]) \
            .setOutputCol("name") \
            .setDistanceFunction("EUCLIDEAN")

        return PipelineModel(
            stages=[
                documentAssembler,
                embeddings,
                resolver])

    @staticmethod
    def get_cross_lib_pipe() -> PipelineModel:
        # Returns pipe with one anno per lib
        # TODO add some fancy OCR DL models?
        doc2text = ocr.DocToText().setInputCol("content").setOutputCol("text")
        d = nlp.DocumentAssembler().setInputCol('text').setOutputCol('doc')
        t = nlp.Tokenizer().setInputCols('doc').setOutputCol('tok')
        # One classifier per NLP lib

        c1 = medical.BertForTokenClassifier().pretrained() \
            .setInputCols(['tok', 'doc']) \
            .setOutputCol('medical')

        c2 = nlp.DeBertaForTokenClassification() \
            .setInputCols(['tok', 'doc']) \
            .setOutputCol('opene_source')

        c3 = finance.BertForSequenceClassification \
            .pretrained("finclf_augmented_esg", "en", "finance/models") \
            .setInputCols(['tok', 'doc']) \
            .setOutputCol("finance")

        c4 = legal.BertForSequenceClassification \
            .pretrained("legclf_bert_judgements_agent", "en", "legal/models") \
            .setInputCols(['tok', 'doc']) \
            .setOutputCol("legal")

        return Pipeline(stages=[doc2text, d, t, c1, c2, c3, c4])

    def test_simple_cross_lib(self):
        spark = jsl.start()
        doc_example = pkg_resources.resource_filename('sparkocr', 'resources/ocr/docs/doc2.docx')
        df = spark.read.format("binaryFile").load(doc_example).cache()
        self.get_cross_lib_pipe().fit(df).transform(df).show()

    def test_simple_cross_lib_gpu(self):
        spark = jsl.start(hardware_target='gpu')
        doc_example = pkg_resources.resource_filename('sparkocr', 'resources/ocr/docs/doc2.docx')
        df = spark.read.format("binaryFile").load(doc_example).cache()
        self.get_cross_lib_pipe().fit(df).transform(df).show()

    def test_cross_engine_session(self):
        import itertools
        # Test every combination of jars with CPU jars
        for c in range(3):
            p = itertools.combinations(['nlp-cpu', 'ocr', 'hc'], c)
            for pp in p: print(pp)

        # Test every combination of jars with GPU jars
        for c in range(3):
            p = itertools.combinations(['nlp-gpu', 'ocr', 'hc'], c)
            for pp in p: print(pp)


if __name__ == '__main__':
    unittest.main()
