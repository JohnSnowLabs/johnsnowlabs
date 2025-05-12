---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/ocr_release_notes
key: docs-ocr-release-notes
modify_date: "2025-05-09"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 6.0.0

Release date: 09-05-2025

## Visual NLP 6.0.0 Release Notes 🕶️

**We are glad to announce that Visual NLP 6.0.0, has been released! 📢📢📢**

</div><div class="h3-box" markdown="1">

## Changes 🔴

* New SVS Image Deidentification capabilities.
* New improvements for performance and memory consumption in Dicom pipelines.
* New PDF de-identification and obfuscation pipelines.
* New Reference dataset for De-identification.
* New NerOutputCleaner transformer.
* ImageDrawRegions: improved logic for processing coordinates that extend across multiple lines.

</div><div class="h3-box" markdown="1">
## New SVS Image Deidentification capabilities.
Now you can redact metadata together with pixel data in Whole Slide Imaging(WSI) SVS files. For an example of all these capabilities in action, check [this notebook](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrWSIDeidentification.ipynb).

</div><div class="h3-box" markdown="1">
## New improvements for performance and memory consumption in Dicom pipelines.
The improvements in Dicom Processing are related to a number of different components:
### DicomToImageV3 image compression

`DicomToImageV3` instead of returning the raw uncompressed dicom frames as images in the dataframe, it can now compress the image frames under the hood to reduce the memory overhead of dicom based pipelines. 

You can use it at follows: 

* `DicomToImageV3.setCompressionMode()`, either  `enabled`, `disabled` or `auto`,

Example,</br>
```python

# Every file is compressed with compressionQuality
dicom_to_image.setCompressionMode('enabled')

# No file is compressed
dicom_to_image.setCompressionMode('disabled')

# files are compressed if Megapixel >= compressionThreshold
dicom_to_image.setCompressionMode('auto')

```

* `DicomToImageV3.setCompressionThreshold()`, Float or Integer which represents the number of mega-pixels in an image above which compression will be applied on the image, if compressionMode is set to `auto` otherwise no effect.</br>
Mega-pixel metric is computed using this equation:</br>
`Megapixel = image_height * image_width * image_frames / 1048576`

Example,
```python
# Set compression threshold to 1 Megapixel
dicom_to_image.setCompressionThreshold(1)
```

* `DicomToImageV3.setCompressionQuality()`, Integer between 1 and 95. This is the  JPG quality parameter used when compressing images.
Example,
```python
dicom_to_image.setCompressionQuality(60)
```


### DicomPretrainedPipeline & DicomDrawRegions
We are introducing a new class: `DicomPretrainedPipeline`. You can use this class to run Dicom pipelines optimizing for reduced memory consumption.
The class will apply optimizations to avoid unnecessary copies of buffers, and execute stages in the most optimal way to avoid memory problems.

You can construct a `DicomPretrainedPipeline()` in the same way you create a `PretrainedPipeline(name, lang, remote_loc, parse_embeddings, disk_location)`

For example by providing name, language and bucketname,
```python
from sparkocr.pretrained import DicomPretrainedPipeline
optimized_pipe = DicomPretrainedPipeline("dicom_deid_generic_augmented_minimal", "en", "clinical/ocr")
processed_df = optimized_pipe.transform(df)
processed_df.show()
```

Additionally, you can convert a custom pipeline by passing it as first argument to DicomPretrainedPipeline. Only requirement is that the pipeline must contain `DicomToImageV3`, `DicomDrawRegions` and `PositionFinder` stages

```python
pipe = PretrainedPipeline("dicom_deid_generic_augmented_minimal", "en", "clinical/ocr")
optimized_pipe = DicomPretrainedPipeline(pipe)
processed_df = optimized_pipe.transform(df)
```

</div><div class="h3-box" markdown="1">

## New PDF de-identification and obfuscation pipelines.
We are shipping two new PDF de-identification pipelines, each of them using a mix of several models to achieve top level performance:
* `pdf_deid_multi_model_context_pipeline`: this one will detect PHI entities from input PDF files, and return de-identified versions of the documents in which the entities have been masked with a black box.
* `pdf_obfuscation_multi_model_context_pipeline`: this one is similar to the one mentioned above in terms of the set of entities it deals with, with the difference that it will perform obfuscation, that is, entity replacement from original entities to 'fake' versions. This process happens consistently across entities, and across pages of the same document.
This means that if in page 1, Martha is replace by Janice, any other Martha in the same document will undergo the same transformation. The same for dates or any other entity.

These pipelines can achieve an F-score of .93 and .91 in our [standard reference dataset](https://github.com/JohnSnowLabs/pdf-deid-dataset). More about this on next section.

</div><div class="h3-box" markdown="1">

## New Reference dataset for De-identification
The [PDF Deid Dataset](https://github.com/JohnSnowLabs/pdf-deid-dataset) is a fully synthetic collection of medical-style PDF documents created for de-identification tasks.
We provide a collection of original PDF documents containing synthetized PHI elements,  annotations for the entities, metrics for pipelines, and sample result PDFs for the obfuscation case, this is actual documents in which the fake entities have injected.

</div><div class="h3-box" markdown="1">

## NerOutputCleaner
NerOutputCleaner is a newly introduced stage that processes the auxiliary mapping generated by the DeIdentification stage. *This is important because the auxiliary mapping can contain useful entities that were created using text matching.* </br> 
It creates unique NER entries with appropriate chunk_ids and metadata required by PositionFinder, enabling the generation of coordinates. This stage also produces a new auxiliary mapping that includes all necessary metadata required by the ImageDrawRegions stages. Additionally, it supports the use of both regex-based and dictionary-based sources for coordinate generation.
As a result, applying this transformer will enable the creation of *very robust NER and De-identification pipelines*.
Example,

```python
cleaner = NerOutputCleaner() \
    .setInputCol("aux") \
    .setOutputCol("new_aux") \
    .setOutputNerCol("positions_ner")
```

</div><div class="h3-box" markdown="1">

## ImageDrawRegions: improved logic for processing coordinates that extend across multiple lines.
When ImageDrawRegions is used to render fake entities into the output PDFs, many times we need to replace entities that spawn across multiple lines, this adds to the complexity already present in the task in which we need to approximate the font size and  the general rendering dimensions of the replacement texts.
This new version is capable of rendering the replacement fake entities across multiple lines to mimic the layout present in the original document.
For example `Susan Frances Martin` at the top of the document is replaced by `Riccardo Chamberlain` that will spawn two separate lines.

<img width="1104" alt="image" src="https://github.com/user-attachments/assets/e0fc7d90-0427-43c6-910a-e22cd8fdd828" />

![Improved logic in multi-line.](/assets/images/ocr/multi-line_impainting.png)

 

This release is compatible with Spark-NLP 6.0.0, and Spark NLP for Healthcare 6.0.0.

</div><div class="h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
