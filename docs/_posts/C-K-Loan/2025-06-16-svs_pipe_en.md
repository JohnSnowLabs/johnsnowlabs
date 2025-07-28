---
layout: model
title: SVS DEID Pipeline
author: John Snow Labs
name: svs_deid_pipe
date: 2025-06-16
tags: [svs, dicom_wsi, en, licensed]
task: De-identification
language: en
edition: Visual NLP 5.5.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"

deploy:
  sagemaker_link: https://aws.amazon.com/marketplace/pp/prodview-kh7vsfj4pwxry
---


## Description

This pipeline can be used to deidentify SVS files. It removes Protected Health Information (PHI) from metadata tags and pixels. This requires healthcare nlp as well has visual nlp installed.

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/SVS_DEID/){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/svs_pipe_en_5.5.0_3.4_1750116076010.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/svs_pipe_en_5.5.0_3.4_1750116076010.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

{% if page.deploy %}
## Available as Private API Endpoint

{:.tac}
{% include display_platform_information.html %}
{% endif %}

## Predicted Entities
``AGE``, ``CITY``, ``COUNTRY``, ``DATE``, ``DOCTOR``, ``EMAIL``, ``HOSPITAL``, ``IDNUM``, ``ORGANIZATION``, ``PATIENT``, ``PHONE``, ``PROFESSION``, ``STATE``, ``STREET``, ``USERNAME``, ``ZIP``, ``SIGNATURE``.


## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparkocr.utils.svs.phi_cleaning import remove_phi
from sparkocr.utils.svs.tile_extraction import svs_to_tiles
from sparkocr.pretrained import PretrainedPipeline
from sparkocr.utils.svs.phi_redaction import redact_phi_in_tiles
raw_svs_path = './svs_input'
output_deid_tags_path = "./svs_output_deid_tags"
output_tiles_path = "./svs_output_tiles"
output_deid_tags_and_pixels_path = './svs_output_deid_tags_and_pixels'
deid_tags = ['ImageDescription.ScanScope ID', 'ImageDescription.Time Zone', 'ImageDescription.ScannerType']

# 1. Create new SVS file where Tags DEID
remove_phi(raw_svs_path, output_deid_tags_path, verbose=True, append_tags=deid_tags)

# 2. Generate Frames from Raw SVS
svs_to_tiles(raw_svs_path, output_tiles_path, level="auto", thumbnail = True)

# 3. Load the Raw Frames as Spark DF
image_df = spark.read.format("binaryFile").load(output_tiles_path).cache()

# 4. Get Pipe and process it
pipe = PretrainedPipeline("image_deid_multi_model_context_pipeline_cpu", "en", "clinical/ocr")
result = pipe.transform(image_df).cache()

# 5. Create the final SVS File with TAGs and Pixels DEID
deid_info = result.select("path", "coordinates").distinct()
redact_phi_in_tiles(output_deid_tags_path, deid_info, output_tiles_path, output_svs_path=output_deid_tags_and_pixels_path, create_new_svs_file = True)
```

```scala
import com.johnsnowlabs.ocr.utils.svs.phi_cleaning.remove_phi
import com.johnsnowlabs.ocr.utils.svs.tile_extraction.svs_to_tiles
import com.johnsnowlabs.ocr.pretrained.PretrainedPipeline
import com.johnsnowlabs.ocr.utils.svs.phi_redaction.redact_phi_in_tiles
import org.apache.spark.sql.SparkSession

// Create Spark session
val spark = SparkSession.builder()
  .appName("SVS De-identification")
  .getOrCreate()

// Paths
val rawSvsPath = "./svs_input"
val outputDeidTagsPath = "./svs_output_deid_tags"
val outputTilesPath = "./svs_output_tiles"
val outputDeidTagsAndPixelsPath = "./svs_output_deid_tags_and_pixels"

// Tags to de-identify
val deidTags = Seq(
  "ImageDescription.ScanScope ID",
  "ImageDescription.Time Zone",
  "ImageDescription.ScannerType"
)

// Step 1: Remove PHI from SVS tags
remove_phi(
  rawSvsPath,
  outputDeidTagsPath,
  verbose = true,
  append_tags = Some(deidTags)
)

// Step 2: Extract tiles from raw SVS
svs_to_tiles(
  svs_path = rawSvsPath,
  output_path = outputTilesPath,
  level = "auto",
  thumbnail = true
)

// Step 3: Read tiles as binary files
val imageDF = spark.read.format("binaryFile").load(outputTilesPath).cache()

// Step 4: Load de-identification pipeline and run
val pipe = PretrainedPipeline("image_deid_multi_model_context_pipeline_cpu", lang = "en", "clinical/ocr")
val result = pipe.transform(imageDF).cache()

// Step 5: Redact PHI from image tiles using coordinates
val deidInfo = result.select("path", "coordinates").distinct()
redact_phi_in_tiles(
  inputSvsPath = outputDeidTagsPath,
  coordinates = deidInfo,
  tilesPath = outputTilesPath,
  output_svs_path = outputDeidTagsAndPixelsPath,
  create_new_svs_file = true
)
```

</div>

{:.model-param}


## Example

The example below illustrates how protected health information (PHI) appears after de-identification on a tile extracted from an SVS image.

### Input:
![Screenshot](/assets/images/examples_ocr/deid_manip_1.png)

### Output:
![Screenshot](/assets/images/examples_ocr/deid_manip_2.png)

## Model Information

{:.table-model}
|---|---|
|Model Name:|svs_pipe|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.2 GB|

## Included Models

- BinaryToImage
- ImageTextDetectorCraft
- ImageToTextV2
- DocumentAssembler
- DocumentNormalizer
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- RegexMatcherModel
- ChunkConverter
- NerConverterInternalModel
- ChunkMergeModel
- PositionFinder
- ImageDrawRegions
