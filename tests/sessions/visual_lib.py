import os
import sys
import unittest

from johnsnowlabs import nlp, visual
from johnsnowlabs.auto_install.softwares import (SparkHcSoftware,
                                                 SparkNlpSoftware,
                                                 SparkOcrSoftware)
from tests.utils import (clear_installed_jsl_installation,
                         get_finance_pipeline, get_legal_pipeline)

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

def setUpModule():
    nlp.install(browser_login=False, spark_nlp=True, nlp=False, visual=True,
                ocr_license=os.environ.get("VALID_LICENSE"),
                aws_key_id="",
                aws_access_key=""
                )


def tearDownModule():
    clear_installed_jsl_installation()


class InstallationTestCase(unittest.TestCase):
    def test_spark_ocr_is_installed(self):
        installed_products = nlp.check_health()
        self.assertTrue(installed_products[SparkNlpSoftware])
        self.assertFalse(installed_products[SparkHcSoftware])
        self.assertTrue(installed_products[SparkOcrSoftware])

class SparkSessionTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.spark = nlp.start(visual=True)

    def test_healthcare_session(self):
        print("Test OCR session ...")
        pdf_to_image = visual.PdfToImage()
        pdf_to_image.setImageType(visual.ImageType.TYPE_3BYTE_BGR)

        # Detect tables on the page using pretrained model
        # It can be finetuned for have more accurate results for more specific documents
        table_detector = visual.ImageTableDetector.pretrained(
            "general_model_table_detection_v2", "en", "clinical/ocr"
        )
        table_detector.setInputCol("image")
        table_detector.setOutputCol("region")

        # Draw detected region's with table to the page
        draw_regions = visual.ImageDrawRegions()
        draw_regions.setInputCol("image")
        draw_regions.setInputRegionsCol("region")
        draw_regions.setOutputCol("image_with_regions")
        draw_regions.setRectColor(visual.Color.red)

        # Extract table regions to separate images
        splitter = visual.ImageSplitRegions()
        splitter.setInputCol("image")
        splitter.setInputRegionsCol("region")
        splitter.setOutputCol("table_image")
        splitter.setDropCols("image")

        # Detect cells on the table image
        cell_detector = visual.ImageTableCellDetector()
        cell_detector.setInputCol("table_image")
        cell_detector.setOutputCol("cells")
        cell_detector.setAlgoType("morphops")

        # Extract text from the detected cells
        table_recognition = visual.ImageCellsToTextTable()
        table_recognition.setInputCol("table_image")
        table_recognition.setCellsCol("cells")
        table_recognition.setMargin(3)
        table_recognition.setStrip(True)
        table_recognition.setOutputCol("table")

        pipeline = nlp.PipelineModel(
            stages=[
                pdf_to_image,
                table_detector,
                draw_regions,
                splitter,
                cell_detector,
                table_recognition,
            ]
        )

        import pkg_resources

        pdf_example = pkg_resources.resource_filename(
            "sparkocr", "resources/ocr/pdfs/tabular-pdf/data.pdf"
        )
        pdf_example_df = self.spark.read.format("binaryFile").load(pdf_example).cache()
        pipeline.transform(pdf_example_df).show()

