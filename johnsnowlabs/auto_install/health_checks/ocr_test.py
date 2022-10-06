# Convert pdf to image
from johnsnowlabs import *


def run_test():
    spark = jsl.start()
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
