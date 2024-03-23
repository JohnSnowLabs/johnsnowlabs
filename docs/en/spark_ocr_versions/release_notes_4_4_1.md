---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/release_notes_4_4_1
key: docs-ocr-release-notes
modify_date: "2023-05-15"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 4.4.1

Release date: 15-05-2023

We are glad to announce that Visual NLP 😎 4.4.1 has been released! This release comes with a number of improvements, bug fixes, new implementations, and more!

### Highlights
#### New Features
* Entirely new implementation for PositionFinder.
* New Base64ToImage Transformer.
* Italian Language Support.
* Control Task Parallelism in ImageToTextV2.
* Fixes & Enhancements
* Most Java Vulnerabilities are gone.
* Improvements in Dicom file processing.
* Fixes in Python installation process.

#### New notebooks

[SparkOcrLightPipelinesBase64.ipynb](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrLightPipelinesBase64.ipynb).

#### New Features
* Entirely new implementation for PositionFinder: PositionFinder has been re-implemented to deal with the limitations of the original version. Many bugs in the previous version simply won't be present in the new implementation. Also, the new version will work with coordinates originated in digital PDFs as well as coordinates originated on images. 

The following methods have been deprecated, and added,

```
.setMatchingWindow():(deprecated)
.setWindowPageTolerance():(deprecated)
.setOcrScaleFactor: (new) Bounding boxes created for OCRed documents(i.e. ImageToText) will be
 vertically scaled up/down by this factor. E.g., provide 1.2, to scale up the coordinates by 20%.
.setPdfScaleFactor: (new) Bounding boxes created for Pdf documents(i.e. PdfToText) will be
 vertically scaled up/down by this factor. E.g., provide 1.2, to scale up the coordinates by 20%.
 ```

The two new methods will allow to apply a vertical scaling for bounding boxes according to the source document type,
so if, for example, the text coordinates were extracted from a digital PDF, and then converted to an image, PositionFinder will be able to read the
original dimensions of the PDF, and scale coordinates accordingly.
Known Limitations: in this new version entities spawning multiple lines won't be supported. We plan to add this support on release 4.4.2.
* New Base64ToImage Transformer.
The new Base64ToImage Transformer is analogous to the BinaryToImage Transformer, but it will use a base64 encoded image as input. Check the sample notebook in this release notes for a practical end-to-end example on how to use it.

* Italian Language Support: support for Italian language has been added, you can start using it similarly to other languages by passing the 'ita' value for the language parameter,
```
    # Run OCR
    ocr = ImageToText()
    ocr.setInputCol("image")
    ocr.setOutputCol("text")
    ocr._set(language="ita")
    ocr.setDownloadModelData(True)
``` 

* Control Task Parallelism in ImageToTextV2.
There's a new parameter 'taskParallelism' in ImageToTextV2 to control the thread parallelism for each task. This way, you have the following options according to your needs to configure your workload,

__Low latency__: you set taskParallelism to a number that can minimize the time for each document to be processed. This competes with the GPU setup. This is the strong scalability situation in which you need a quick response for each document so it can be consumed faster. You turn your document level parallelism to a low value so you work on few documents at a time and apply a high number of resources on each document. One way to achieve this is with reduced partition count in your dataframe.
__High throughput__: you use a higher partition count in the dataframe, and a value of taskParallelism such that you keep the throughput high, without worrying about latency. This is the typical weak scaling situation in which you just scale out the workload through a Spark batch job.
Example,
```
ocr = ImageToTextV2.pretrained("ocr_base_printed_v2_opt", "en", "clinical/ocr") \
    .setRegionsColumn("text_regions") \
    .setInputCols(["image"]) \
    .setOutputCol("text") \
    .setTaskParallelism(12)
```
#### Fixes
* Most vulnerabilities at the Java level were removed: 50 out of 52 reported vulnerabilities were removed from the JAR file of Visual NLP. Only 2 medium vulnerabilities remain.

* Improvements in Dicom file processing,

Added support multiple frame overlay in DicomToImageV3, DicomDrawRegions.
Fixed support 16 bit greyscale images.
Added support 16 bit images (across Visual NLP in general).
 
* Fixes in ImageDrawRegions: ImageDrawRegions now allows scaling of input coordinates acording to the source document against which the coordinates were created. So, for example if the image was created using PdfToImage, using high resolution, and we want to draw the coordinates that were derived from the 'position' column in PdfToImage, we can scale the bounding boxes to account for this change in resolution,

    * setSourceImageHeightCol: sets the name of the column where the original image height is present.
    * setSourceImageWidthCol: sets the name of the column where the original image width is present.
    * setScaleBoundingBoxes: enables/disables the scaling of the bounding boxes. Defaults to 'false'(disabled).

 
Known Limitations: due to mismatch in column types from different annotators returning dimensions, ImageDrawRegions scaling won't work with some of them. This behavior will be fixed on next release.

* Fixes in Python installation process: installation process has been improved especially in environments with newer Python versions like Colab.

#### New Notebooks
SparkOcrLightPipelinesBase64.ipynb: learn how to use the new Base64ToImage Transformer in LightPipelines to feed in memory string buffers to Visual NLP pipelines.
This release is compatible with Spark NLP for Healthcare 4.4.1, and Spark NLP 4.4.1.

</div><div class="prev_ver h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
